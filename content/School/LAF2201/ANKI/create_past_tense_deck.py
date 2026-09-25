"""Run inside Anki's debug console, where `mw` is available."""

import json
from datetime import datetime
from pathlib import Path

from aqt import mw
from anki.consts import DYN_RANDOM


def create_past_tense_deck():
    col = mw.col
    name = "LAF2201 Past Tenses"
    query = (
        "tag:fr::laf2201 (tag:fr::grammar::passe-compose OR "
        "tag:fr::grammar::past-participles OR tag:fr::grammar::imparfait OR "
        "tag:fr::grammar::tense-choice)"
    )
    ids = col.find_cards(query)
    if not ids:
        raise RuntimeError("No matching past-tense cards found; nothing changed.")
    existing = col.decks.by_name(name)
    if existing and not existing.get("dyn"):
        raise RuntimeError(f"{name} already exists as a normal deck; nothing changed.")
    cards = [col.get_card(cid) for cid in ids]
    attrs = ("id", "nid", "did", "odid", "due", "odue", "type", "queue",
             "ivl", "factor", "reps", "lapses", "left")
    before = [{k: getattr(c, k) for k in attrs} for c in cards]
    backup_dir = Path(__file__).parent / "backups"
    backup_dir.mkdir(exist_ok=True)
    backup = backup_dir / ("past-tense-deck-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".json")
    backup.write_text(json.dumps({"name": name, "query": query,
                                 "previous_deck": existing, "cards": before}, indent=2))
    # Return only the selected cards from other filtered decks to their home decks.
    borrowed = [c.id for c in cards if c.odid]
    if borrowed:
        col.sched.remFromDyn(borrowed)
    did = existing["id"] if existing else col.decks.new_filtered(name)
    deck = col.decks.get(did)
    deck.update(terms=[[query, 9999, DYN_RANDOM]], resched=False, separate=False,
                previewDelay=1, previewAgainSecs=60, previewHardSecs=600,
                previewGoodSecs=0)
    col.decks.save(deck)
    col.sched.rebuild_filtered_deck(did)
    actual = col.find_cards(f'deck:"{name}"')
    for old in before:
        card = col.get_card(old["id"])
        assert (card.ivl, card.reps, card.lapses) == (old["ivl"], old["reps"], old["lapses"])
        assert (card.odid or card.did) == (old["odid"] or old["did"])
    col.decks.select(did)
    mw.reset()
    mw.moveToState("overview")
    print(f"Created {name}: {len(actual)} of {len(ids)} matching cards. Rescheduling OFF.")
    if len(actual) < len(ids):
        print("Some matching cards are unavailable (for example, buried or suspended).")
    print(f"Backup: {backup}")


create_past_tense_deck()
