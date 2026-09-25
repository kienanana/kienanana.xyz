---
tags:
  - y4s1
---

# IS4226 Quiz 1 Anki deck (v2)

This is a source-audited recall deck for Weeks 1–3. Its 87 cards were derived from the five lecture notes and their 28 embedded images, without filtering or transforming the former 107-card set.

## Canonical files

- `source_inventory.md`: complete heading/image audit and inclusion decisions.
- `source_issues.md`: ambiguities and inconsistencies preserved rather than silently corrected.
- `is4226_core_cards_v2.json`: source cards with semantic IDs and inventory mappings.
- `is4226_quiz1_cards.json`: validated import artifact produced by the build script.

The older JSON/TSV/card-practice files are obsolete inputs and retained only as migration history. Neither v2 script reads them.

## Build and synchronize

```sh
python3 /Users/kienanana/Documents/obsidian-scripts/is4226_build_deck.py

# Safe preview; makes no Anki changes
python3 /Users/kienanana/Documents/obsidian-scripts/is4226_import_anki.py

# Apply after reviewing the preview
python3 /Users/kienanana/Documents/obsidian-scripts/is4226_import_anki.py --apply
```

The importer manages only v2 notes or notes bearing signatures from prior IS4226 importers, and only the `IS4226 Basic` model with a populated `Card ID`. It does not use broad deck deletion and will not touch French or unrelated notes.

Deck: `IS4226::Quiz 1`  
Managed tag: `is4226::managed_v2`

## Filtered decks after replacement

Empty all existing IS4226 filtered decks, then rebuild them with:

```text
tag:is4226::managed_v2 tag:is4226::w1
tag:is4226::managed_v2 tag:is4226::w2
tag:is4226::managed_v2 tag:is4226::w3
```

Cards have exactly one week tag unless a future source explicitly belongs to multiple weeks. Future calculation drills belong in `IS4226::Optional Calculation Practice`, not this core deck.
