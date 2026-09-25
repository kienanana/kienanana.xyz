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

Requires the AnkiConnect add-on (Tools > Add-ons > Get Add-ons > 2055492159).
"""

import sys
import re
import json
import unicodedata
import urllib.request
import urllib.error
from pathlib import Path

VAULT = Path.home() / "Documents" / "VAULT"
BANK_GLOB = "School/LAF*/NOTES/LAF* Vocab Bank.md"

ANKI_URL = "http://localhost:8765"
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


def parse_bank(path: Path, course: str) -> list:
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


def load_banks() -> list:
    paths = sorted(VAULT.glob(BANK_GLOB))
    if not paths:
        print(f"error: no vocab banks matched {BANK_GLOB} under {VAULT}", file=sys.stderr)
        sys.exit(1)

    entries = []
    for path in paths:
        course = re.search(r"LAF\d{4}", path.name).group()
        found = parse_bank(path, course)
        print(f"  {course}: {len(found):3d} entries  ({path.name})")
        entries += found

    seen, unique = {}, []
    for entry in entries:
        key = fold(entry["french"])
        if key in seen:
            other = seen[key]
            print(f"  warning: duplicate {entry['french']!r}\n"
                  f"      {other['line']} [{other['course']}] {other['english']}\n"
                  f"      {entry['line']} [{entry['course']}] {entry['english']}",
                  file=sys.stderr)
            # Keep the richer gloss rather than silently dropping one.
            if len(entry["english"]) > len(other["english"]):
                unique[unique.index(other)] = entry
                seen[key] = entry
            continue
        seen[key] = entry
        unique.append(entry)
    return unique


def build_note(entry: dict) -> dict:
    tags = [MANAGED_TAG, f"fr::{slug(entry['category'])}", f"fr::{entry['course'].lower()}"]
    return {
        "deckName": DECK,
        "modelName": MODEL,
        "fields": {
            "French": entry["french"],
            "English": entry["english"],
            "Notes": entry["notes"],
            "Key": fold(entry["french"]),
        },
        "tags": tags,
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


def existing_notes() -> dict:
    ids = anki("findNotes", query=f"tag:{MANAGED_TAG}")
    if not ids:
        return {}
    return {
        info["fields"]["Key"]["value"]: {
            "id": info["noteId"],
            "fields": {k: v["value"] for k, v in info["fields"].items()},
            "tags": set(info["tags"]),
        }
        for info in anki("notesInfo", notes=ids)
    }


def sync(entries: list, dry_run: bool, push: bool):
    if not dry_run:
        ensure_model_and_deck()
    current = existing_notes()

    new, updated, retagged, unchanged = [], [], [], 0
    for entry in entries:
        note = build_note(entry)
        key = note["fields"]["Key"]
        old = current.get(key)
        if old is None:
            new.append((entry, note))
            continue
        field_change = [
            f for f in ("French", "English", "Notes")
            if old["fields"].get(f, "") != note["fields"][f]
        ]
        tag_change = set(note["tags"]) != old["tags"]
        if field_change:
            updated.append((entry, note, old, field_change))
        elif tag_change:
            retagged.append((entry, note, old))
        else:
            unchanged += 1

    stale = [(k, v) for k, v in current.items()
             if k not in {fold(e["french"]) for e in entries}]

    for entry, _ in new:
        print(f"  + {entry['french']}  —  {entry['english']}  [{entry['category']}]")
    for entry, note, old, changed in updated:
        for field in changed:
            print(f"  ~ {entry['french']}  {field}: "
                  f"{old['fields'].get(field, '')!r} -> {note['fields'][field]!r}")
    for entry, note, old in retagged:
        print(f"  # {entry['french']}  tags: "
              f"{sorted(old['tags'])} -> {sorted(note['tags'])}")

    if stale:
        print(f"\n  {len(stale)} note(s) in Anki no longer in any bank — NOT deleted:")
        for key, note in stale:
            print(f"      {note['fields'].get('French', key)}")
        print(f"      review with:  \"note:{MODEL}\" tag:{MANAGED_TAG}")

    print(f"\n  +{len(new)} new / ~{len(updated)} updated / "
          f"#{len(retagged)} retagged / {unchanged} unchanged")

    if dry_run:
        print("\n  dry run — nothing written")
        return
    if new:
        anki("addNotes", notes=[n for _, n in new])
    for _, note, old, _ in updated:
        anki("updateNoteFields", note={"id": old["id"], "fields": note["fields"]})
    tag_targets = [(n, o) for _, n, o, _ in updated] + [(n, o) for _, n, o in retagged]
    for note, old in tag_targets:
        add = set(note["tags"]) - old["tags"]
        remove = old["tags"] - set(note["tags"])
        if add:
            anki("addTags", notes=[old["id"]], tags=" ".join(sorted(add)))
        if remove:
            anki("removeTags", notes=[old["id"]], tags=" ".join(sorted(remove)))
    if push:
        anki("sync")
        print("  pushed to AnkiWeb")


def write_tsv(entries: list, path: Path):
    with path.open("w", encoding="utf-8") as f:
        f.write("#separator:tab\n#html:false\n#notetype:" + MODEL + "\n")
        f.write("#deck:" + DECK + "\n#tags column:5\n")
        for entry in entries:
            note = build_note(entry)
            fields = note["fields"]
            f.write("\t".join([fields["French"], fields["English"], fields["Notes"],
                               fields["Key"], " ".join(note["tags"])]) + "\n")
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
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    push = "--sync" in args
    gaps = "--gaps" in args
    tsv = None
    if "--tsv" in args:
        i = args.index("--tsv")
        if i + 1 >= len(args):
            print("error: --tsv requires a path", file=sys.stderr)
            sys.exit(1)
        tsv = Path(args[i + 1])

    unknown = [a for a in args
               if a.startswith("-") and a not in ("--dry-run", "--sync", "--gaps", "--tsv")]
    if unknown:
        print(f"error: unknown option(s): {' '.join(unknown)}\n\n{__doc__}", file=sys.stderr)
        sys.exit(1)

    entries = load_banks()
    print(f"  {len(entries)} unique entries\n")

    if gaps:
        scan_gaps(entries)
    elif tsv:
        write_tsv(entries, tsv)
    else:
        sync(entries, dry_run, push)


if __name__ == "__main__":
    main()
