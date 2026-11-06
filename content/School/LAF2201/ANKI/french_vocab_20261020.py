#!/usr/bin/env python3
"""Sync French vocabulary from Obsidian vocab banks into Anki via AnkiConnect.

Each `LAF#### Vocab Bank.md` note is parsed into one Anki note per entry. Sync is
idempotent and updates in place, so review history survives edits to the banks.

Usage:
    french.py              sync to Anki
    french.py --dry-run    show what would change, touch nothing
    french.py --gaps       report lecture vocab not yet filed into a bank
    french.py --tsv PATH   write an importable TSV instead of using AnkiConnect
    french.py --sync       sync, then push to AnkiWeb
    french.py --course LAF2201 --dry-run   preview one course
    french.py --course LAF2201             sync one course, including grammar.json

LAF2201 supports translated bullets and vocabulary tables. Existing notes are
matched by stable key or French text, including legacy imports. Their IDs,
existing tags, decks and review scheduling are retained. New cards go to the normal
home deck French::Vocab; LAF2201 may be a filtered study deck. No notes are deleted. Each applied run saves a backup in the vault.

Requires the AnkiConnect add-on (Tools > Add-ons > Get Add-ons > 2055492159).
"""

import sys
import argparse
import html
from datetime import datetime
import re
import json
import unicodedata
import urllib.request
import urllib.error
from pathlib import Path

VAULT = Path.home() / "Documents" / "VAULT"
BANK_GLOB = "School/LAF*/NOTES/LAF* Vocab Bank.md"

ANKI_URL = "http://127.0.0.1:8765"
ANKI_VERSION = 6
DECK = "French::Vocab"
MODEL = "French Vocab"
FIELDS = ["French", "English", "Notes", "Key"]
MANAGED_TAG = "fr::managed"

# Bullets opening with these are cross-references, not vocabulary.
SKIP_PREFIXES = ("see ", "revise ", "recap ", "note:")

# " — ", " – ", " - " or ": " may separate the French term from its gloss.
SEPARATOR = re.compile(r"\s+—\s+|\s+–\s+|\s+-\s+|:\s+")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BULLET = re.compile(r"^(\s*)[-*]\s+(.*)$")
WIKILINK = re.compile(r"!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
PARENTHETICAL_NOTE = re.compile(r"\*\(([^)]+)\)\*")
# "# Shops (Les commerces)" -> the French gloss is decoration, not category.
HEADING_GLOSS = re.compile(r"\s*\((?:Les |La |Le |L')[^)]*\)\s*$", re.IGNORECASE)
# "### 🟢 Uncountable -> du / de la" annotates grammar, it is not a category.
GRAMMAR_HEADING = re.compile(r"^[🟢🔵]|^(Un)?[Cc]ountable\b|^en\b|^à\b")

CARD_FRONT = """<div class="french">{{French}}</div>"""
CARD_BACK = """{{FrontSide}}<hr id=answer>
<div class="english">{{English}}</div>
{{#Notes}}<div class="note">{{Notes}}</div>{{/Notes}}"""
CARD_CSS = """.card {
  font-family: -apple-system, Helvetica, sans-serif;
  font-size: 28px;
  text-align: center;
  color: #1a1a1a;
  background: #fdfdfd;
}
.english { font-size: 24px; }
.note { font-size: 16px; color: #888; margin-top: 12px; font-style: italic; }
.nightMode .card { color: #e8e8e8; background: #2c2c2c; }
.nightMode .note { color: #999; }"""


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

def strip_markdown(text: str) -> str:
    text = WIKILINK.sub(lambda m: m.group(2) or m.group(1), text)
    text = re.sub(r"[*_`]+", "", text)
    return text.strip()


def fold(text: str) -> str:
    """Accent- and case-folded form, used as the stable sync identity."""
    decomposed = unicodedata.normalize("NFKD", text.lower())
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", stripped.replace("’", "'")).strip()


def slug(text: str) -> str:
    """Slugify a "Food > Fruits" heading path into Anki's food::fruits form."""
    parts = [re.sub(r"[^a-z0-9]+", "-", fold(p)).strip("-") for p in text.split(">")]
    return "::".join(p for p in parts if p) or "misc"


def strip_frontmatter(lines: list) -> list:
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
    return lines


def parse_legacy_bank(path: Path, course: str) -> list:
    """Return [{french, english, notes, category, course, line}] for one bank."""
    lines = strip_frontmatter(path.read_text(encoding="utf-8").splitlines())
    entries, stack = [], {}

    for offset, raw in enumerate(lines):
        heading = HEADING.match(raw)
        if heading:
            level, title = len(heading.group(1)), strip_markdown(heading.group(2))
            stack[level] = title
            for deeper in [k for k in stack if k > level]:
                del stack[deeper]
            continue

        bullet = BULLET.match(raw)
        if not bullet:
            continue
        body = bullet.group(2).strip()
        if not body or body.lower().startswith(SKIP_PREFIXES):
            continue

        notes = ""
        aside = PARENTHETICAL_NOTE.search(body)
        if aside:
            notes = aside.group(1).strip()
            body = body.replace(aside.group(0), " ")

        parts = SEPARATOR.split(strip_markdown(body), maxsplit=1)
        if len(parts) != 2:
            continue
        french, english = parts[0].strip(), parts[1].strip()
        if not french or not english:
            continue

        # Headings that name a topic rather than a grammar rule, outermost
        # first, so "# Food" > "## Fruits" becomes the tag food::fruits.
        topical = []
        for level in sorted(stack):
            title = HEADING_GLOSS.sub("", stack[level]).strip()
            if title and not GRAMMAR_HEADING.match(title):
                topical.append(title)
        category = " > ".join(topical) if topical else "misc"

        entries.append({
            "french": french,
            "english": english,
            "notes": notes,
            "category": category,
            "course": course,
            "line": f"{path.name}:{offset + 1}",
        })
    return entries


def parse_bank(path: Path, course: str) -> list:
    # The earlier bank format remains supported for LAF1201.
    if course != "LAF2201":
        return parse_legacy_bank(path, course)
    entries, stack, headers = [], {}, []

    def emit(french, english, notes="", line=0):
        french, english = strip_markdown(french), strip_markdown(english)
        if french == "nouveau / nouvelle":
            french = "nouveau (nouvel) / nouvelle"
        if not french or not english:
            raise ValueError(f"Empty vocabulary at {path}:{line}")
        entries.append(dict(french=french, english=english, notes=strip_markdown(notes),
                            category=" > ".join(HEADING_GLOSS.sub("", stack[k]).strip() for k in sorted(stack)),
                            course=course, courses=[course], line=f"{path.name}:{line}"))

    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        heading = HEADING.match(raw)
        if heading:
            level = len(heading[1]); stack[level] = strip_markdown(heading[2])
            stack = {k: v for k, v in stack.items() if k <= level}
            headers = []
            continue
        if raw.startswith("|"):
            cells = [strip_markdown(c) for c in raw.strip().strip("|").split("|")]
            if all(re.fullmatch(r"[: -]+", c) for c in cells):
                continue
            if not headers:
                headers = cells
                continue
            if len(cells) != len(headers):
                raise ValueError(f"Malformed table at {path}:{lineno}")
            if headers == ["Masculine", "Feminine", "English"]:
                masculine, feminine, english = cells
                emit(masculine if masculine == feminine else f"{masculine} / {feminine}", english, line=lineno)
            elif headers == ["Expression", "English"]:
                emit(*cells, line=lineno)
            elif headers == ["Adjective", "English", "Opposite", "English"]:
                emit(cells[0], cells[1], line=lineno); emit(cells[2], cells[3], line=lineno)
            elif headers == ["Infinitive", "English", "Past participle"]:
                emit(cells[0], cells[1], "Participe passé: " + cells[2] + ". See Passé Composé for auxiliary and agreement rules.", lineno)
            elif headers == ["Number", "French"]:
                emit(cells[1], cells[0], line=lineno)
            elif headers == ["When", "Infinitive", "With je (present tense)", "English"]:
                emit(cells[1], cells[3], cells[2] + " · " + cells[0], lineno)
            elif headers == ["Abbreviation", "Full form", "English"]:
                emit(cells[0], cells[2], "Full form: " + cells[1], lineno)
            else:
                raise ValueError(f"Unsupported table at {path}:{lineno}: {headers}")
            continue
        headers = []
        bullet = BULLET.match(raw)
        if not bullet or not stack:
            continue
        body = bullet[2]
        # Only explicit translation bullets: prose/grammar bullets are not cards.
        if " — " not in body:
            continue
        for segment in re.split(r";\s+(?=[^;]+ — )", body):
            if segment.strip().lower().startswith("also "):
                if entries:
                    entries[-1]["notes"] += " · " + strip_markdown(segment)
                continue
            asides = PARENTHETICAL_NOTE.findall(segment)
            segment = PARENTHETICAL_NOTE.sub("", segment)
            front, back = segment.split(" — ", 1)
            extra = []
            markers = [(back.index(marker), marker) for marker in (" → ", ": ", "; ") if marker in back]
            if markers:
                _, marker = min(markers)
                back, rest = back.split(marker, 1)
                extra.append(rest)
            emit(front, back, " · ".join(asides + extra), lineno)
    return entries


def load_banks(course=None) -> list:
    entries = []
    for path in sorted(VAULT.glob(BANK_GLOB)):
        name = re.search(r"LAF\d{4}", path.name).group()
        if course and name != course:
            continue
        found = parse_bank(path, name)
        print(f"  {name}: {len(found)} vocabulary entries")
        entries.extend(found)
    if not entries:
        raise ValueError("No vocabulary banks found for the selected course")
    unique = {}
    for entry in entries:
        key = fold(entry["french"])
        if key in unique:
            old = unique[key]
            courses = sorted(set(old.get("courses", [old["course"]]) + [entry["course"]]))
            if len(entry["english"]) > len(old["english"]):
                unique[key] = entry
            unique[key]["courses"] = courses
        else:
            entry.setdefault("courses", [entry["course"]])
            unique[key] = entry
    return list(unique.values())


def build_note(entry: dict) -> dict:
    courses = entry.get("courses", [entry["course"]])
    tags = [MANAGED_TAG, f"fr::{slug(entry['category'])}"] + [f"fr::{c.lower()}" for c in courses]
    if entry.get("kind") == "grammar":
        tags += ["fr::grammar", "fr::grammar_id::" + entry["id"]]
    return {
        "deckName": DECK,
        "modelName": MODEL,
        "fields": {"French": html.escape(entry["french"]), "English": html.escape(entry["english"]),
                   "Notes": html.escape(entry.get("notes", "")),
                   "Key": entry.get("key", fold(entry["french"]))},
        "tags": sorted(set(tags)),
        "options": {"allowDuplicate": False},
    }


# --------------------------------------------------------------------------
# AnkiConnect
# --------------------------------------------------------------------------

def anki(action: str, **params):
    payload = json.dumps({"action": action, "version": ANKI_VERSION,
                          "params": params}).encode()
    request = urllib.request.Request(
        ANKI_URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read())
    except urllib.error.URLError as e:
        print(f"error: cannot reach AnkiConnect at {ANKI_URL} — {e}\n"
              f"       Is Anki running with the AnkiConnect add-on installed?\n"
              f"       Tools > Add-ons > Get Add-ons > code 2055492159",
              file=sys.stderr)
        sys.exit(1)

    if body.get("error"):
        print(f"error: AnkiConnect '{action}' failed — {body['error']}", file=sys.stderr)
        sys.exit(1)
    return body["result"]


def ensure_model_and_deck():
    if MODEL not in anki("modelNames"):
        anki("createModel", modelName=MODEL, inOrderFields=FIELDS, css=CARD_CSS,
             cardTemplates=[{"Name": "FR to EN", "Front": CARD_FRONT, "Back": CARD_BACK}])
        print(f"  created note type {MODEL!r}")
    if DECK not in anki("deckNames"):
        anki("createDeck", deck=DECK)
        print(f"  created deck {DECK!r}")


def existing_notes() -> list:
    ids = anki("findNotes", query=f'"note:{MODEL}"')
    result = []
    for start in range(0, len(ids), 100):
        result.extend(anki("notesInfo", notes=ids[start:start+100]))
    return result


def plain(value):
    return html.unescape(re.sub(r"<[^>]*>", "", value)).strip()


def front_aliases(entry):
    aliases = [entry["french"]] + entry.get("aliases", [])
    # Explicit migrations preserve the identities of the older short fronts.
    migrations = {
        "pareil / pareille": ["pareil"],
        "emprunter quelque chose à quelqu'un": ["emprunter"],
        "beau (bel) / belle": ["beau / belle", "beau"],
        "vieux (vieil) / vieille": ["vieux / vieille", "vieux"],
        "nouveau (nouvel) / nouvelle": ["nouveau / nouvelle", "nouveau"],
    }
    aliases += migrations.get(entry["french"], [])
    return {fold(a) for a in aliases}


def make_plan(entries, current):
    by_key, by_front = {}, {}
    for info in current:
        by_key.setdefault(info["fields"]["Key"]["value"], []).append(info)
        by_front.setdefault(fold(plain(info["fields"]["French"]["value"])), []).append(info)
    plan, claimed = [], set()
    for entry in entries:
        note = build_note(entry)
        candidates = by_key.get(note["fields"]["Key"], [])[:]
        if not candidates:
            for alias in front_aliases(entry):
                candidates.extend(by_front.get(alias, []))
        candidates = {n["noteId"]: n for n in candidates}
        if len(candidates) > 1:
            raise ValueError(f"Ambiguous existing notes for {entry['french']}: {list(candidates)}")
        old = next(iter(candidates.values()), None)
        if old:
            nid = old["noteId"]
            if nid in claimed:
                raise ValueError(f"Two source entries match note {nid}: {entry['french']}")
            claimed.add(nid)
            # Do not replace legacy IDs, move cards, or remove user tags.
            note["fields"]["Key"] = old["fields"]["Key"]["value"]
            if not note["fields"]["Notes"]:
                note["fields"]["Notes"] = old["fields"]["Notes"]["value"]
            fields = {k: v for k, v in note["fields"].items() if v != old["fields"][k]["value"]}
            tags = sorted(set(note["tags"]) - set(old["tags"]))
            action = "update" if fields or tags else "unchanged"
        else:
            fields, tags, action = {}, [], "add"
        plan.append(dict(action=action, entry=entry, note=note, old=old, fields=fields, tags=tags))
    return plan


def load_grammar(course=None):
    if course and course != "LAF2201":
        return []
    path = VAULT / "School/LAF2201/ANKI/grammar.json"
    if not path.exists():
        return []
    cards = json.loads(path.read_text())
    seen = set()
    for card in cards:
        if card["id"] in seen:
            raise ValueError("Duplicate grammar ID: " + card["id"])
        seen.add(card["id"])
        card.update(course="LAF2201", courses=["LAF2201"], kind="grammar", line=str(path.name),
                    key="laf2201-" + card["id"])
        card["notes"] = card.get("notes", "") + " Source: " + card["source"]
    return cards


def sync(entries: list, dry_run: bool, push: bool, report=None):
    current = existing_notes()
    plan = make_plan(entries, current)
    counts = {action: sum(p["action"] == action for p in plan) for action in ("add", "update", "unchanged")}
    for p in plan:
        if p["action"] != "unchanged":
            print(f"  {p['action']:6} {p['entry']['french']} — {p['entry']['english']}")
    print(json.dumps(counts))
    if report:
        Path(report).write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    if dry_run:
        print("Dry run — nothing written to Anki")
        return counts
    for deck in {p["note"]["deckName"] for p in plan if p["action"] == "add"}:
        config = anki("getDeckConfig", deck=deck)
        if config and config.get("dyn"):
            raise ValueError(f"Cannot import into filtered deck {deck}; choose a normal home deck")
    affected = [p["old"] for p in plan if p["old"]]
    # Resolve IDs using findCards; older add-on versions may omit cards in notesInfo.
    card_ids = []
    for start in range(0, len(affected), 100):
        query = " OR ".join(f"nid:{n['noteId']}" for n in affected[start:start+100])
        if query:
            card_ids.extend(anki("findCards", query=query))
    cards = []
    for start in range(0, len(card_ids), 100):
        cards.extend(anki("cardsInfo", cards=card_ids[start:start+100]))
    backup_dir = VAULT / "School/LAF2201/ANKI/backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = backup_dir / (datetime.now().strftime("%Y%m%d-%H%M%S-%f") + ".json")
    backup.write_text(json.dumps({"notes": affected, "cards": cards, "plan": plan}, ensure_ascii=False, indent=2) + "\n")
    print("Backup:", backup)
    if MODEL not in anki("modelNames"):
        ensure_model_and_deck()
    for deck in sorted({p["note"]["deckName"] for p in plan if p["action"] == "add"}):
        anki("createDeck", deck=deck)
    added = []
    for p in plan:
        if p["action"] == "add":
            nid = anki("addNote", note=p["note"])
            if not nid:
                raise RuntimeError("Anki did not return an ID for " + p["entry"]["french"])
            added.append(nid)
        elif p["action"] == "update":
            if p["fields"]:
                anki("updateNoteFields", note={"id": p["old"]["noteId"], "fields": p["fields"]})
            if p["tags"]:
                anki("addTags", notes=[p["old"]["noteId"]], tags=" ".join(p["tags"]))
    receipt = backup.with_suffix(".receipt.json")
    receipt.write_text(json.dumps({"added_note_ids": added, "counts": counts}, indent=2) + "\n")
    after = make_plan(entries, existing_notes())
    pending = [p for p in after if p["action"] != "unchanged"]
    if pending:
        raise RuntimeError(f"Verification failed: {len(pending)} pending changes")
    # Editing fields/tags must leave scheduling and review counters intact.
    scheduling = ("cardId", "note", "deckName", "type", "queue", "due", "interval", "factor", "reps", "lapses", "left")
    verified = []
    for start in range(0, len(card_ids), 100):
        verified.extend(anki("cardsInfo", cards=card_ids[start:start+100]))
    before_by_id = {c["cardId"]: c for c in cards}
    for c in verified:
        old = before_by_id[c["cardId"]]
        if any(old.get(k) != c.get(k) for k in scheduling):
            raise RuntimeError("Scheduling changed for card " + str(c["cardId"]))
    print(f"Verified: {len(after)} entries match; {len(verified)} existing cards retain their scheduling.")
    if push:
        anki("sync")
    return counts


def write_tsv(entries: list, path: Path):
    with path.open("w", encoding="utf-8") as f:
        f.write("#separator:tab\n#html:true\n#notetype:" + MODEL + "\n")
        f.write("#tags column:5\n#deck column:6\n")
        for entry in entries:
            note = build_note(entry)
            fields = note["fields"]
            f.write("\t".join([fields["French"], fields["English"], fields["Notes"],
                               fields["Key"], " ".join(note["tags"]), note["deckName"]]) + "\n")
    print(f"  wrote {len(entries)} rows -> {path}")


# --------------------------------------------------------------------------
# gap report
# --------------------------------------------------------------------------

# Matches "## [[LAF2201 Vocab Bank|Vocab Bank]]" and the plain "## Vocab Bank:" form.
GAP_HEADING = re.compile(r"^#{1,6}\s+.*Vocab Bank", re.IGNORECASE)


def scan_gaps(entries: list):
    known = {fold(e["french"]) for e in entries}
    banks = {p.name for p in VAULT.glob(BANK_GLOB)}
    total = 0

    for path in sorted(VAULT.glob("School/LAF*/**/*.md")):
        if path.name in banks:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        missing = []
        for i, line in enumerate(lines):
            if not GAP_HEADING.match(line):
                continue
            # Section = consecutive bullets, blanks allowed, ending at the
            # first line that is neither. Keeps exercise prose out.
            for j in range(i + 1, len(lines)):
                body = lines[j]
                if not body.strip():
                    continue
                bullet = BULLET.match(body)
                if not bullet:
                    break
                text = bullet.group(2).strip()
                if text.lower().startswith(SKIP_PREFIXES):
                    continue
                text = PARENTHETICAL_NOTE.sub(" ", text)
                parts = SEPARATOR.split(strip_markdown(text), maxsplit=1)
                if len(parts) != 2:
                    continue
                french, english = parts[0].strip(), parts[1].strip()
                if french and english and fold(french) not in known:
                    missing.append((j + 1, french, english))
        if missing:
            print(f"\n{path.relative_to(VAULT)}")
            for lineno, french, english in missing:
                print(f"  :{lineno:<4} {french}  —  {english}")
            total += len(missing)

    print(f"\n  {total} entr{'y' if total == 1 else 'ies'} not yet filed into a bank")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sync", action="store_true", help="also sync to AnkiWeb")
    parser.add_argument("--gaps", action="store_true")
    parser.add_argument("--tsv", type=Path)
    parser.add_argument("--course", help="limit to one course, e.g. LAF2201")
    parser.add_argument("--report", type=Path, help="save the exact sync plan as JSON")
    args = parser.parse_args()
    entries = load_banks(args.course)
    if args.gaps:
        scan_gaps(entries)
    else:
        entries += load_grammar(args.course)
        if args.tsv:
            write_tsv(entries, args.tsv)
        else:
            sync(entries, args.dry_run, args.sync, args.report)


if __name__ == "__main__":
    main()
