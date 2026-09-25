# LAF2201 Anki

Vocabulary comes from [[LAF2201 Vocab Bank]]. Grammar prompts, answers and source paths are maintained in [grammar.json](grammar.json). The importer is `/Users/kienanana/Documents/obsidian-scripts/french.py`.

Preview changes:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 /Users/kienanana/Documents/obsidian-scripts/french.py --course LAF2201 --dry-run
```

Apply to the open Anki collection:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 /Users/kienanana/Documents/obsidian-scripts/french.py --course LAF2201
```

Add `--sync` only when an AnkiWeb sync is wanted. AnkiConnect must be running.

New cards go into the normal home deck **French::Vocab**. **LAF2201 is a filtered study deck**, using `deck:French::Vocab tag:fr::laf2201` with a 100-card limit. Use its Rebuild button to refresh the study batch after importing. Existing shared vocabulary stays in its current deck and gains the `fr::laf2201` tag. Search `tag:fr::laf2201` in Anki to see the complete course set, including shared vocabulary. Grammar also has `fr::grammar` and stable per-prompt ID tags.

The importer reads translated bullets and the bank's colour, activity, atmosphere, adjective, movement-verb and number tables. Prose rules are excluded; selected rules become focused grammar questions instead. Unsupported table layouts stop the import rather than silently omitting material. Within LAF2201, the two occurrences of *nouveau / nouvelle* are consolidated, and last summer / last winter are separate vocabulary entries to preserve the original cards.

Matching uses existing keys, normalized French text, and explicit aliases for renamed fronts. Legacy TUT 1 keys are retained. Routine sync edits existing notes in place; it does not delete or move cards. On 2026-09-07, a one-time repair moved 39 unreviewed cards incorrectly imported directly into the filtered deck to French::Vocab, preserving their IDs, new-card positions and review counters. Existing tags are preserved. Shared vocabulary is reused across courses. New conflicting matches stop the import for inspection.

Each applied run saves the affected notes, card scheduling state and exact plan in `backups/`, followed by a receipt containing newly added note IDs. It then verifies the content, checks that a repeated import has no pending changes, and compares existing scheduling and review counters. These JSON files are recovery/audit data, not a full Anki collection backup.

Offline regression checks:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 School/LAF2201/ANKI/test_french.py /Users/kienanana/Documents/obsidian-scripts/french.py
```

## Update on 2026-09-07

- 251 cards added: 192 vocabulary and 59 grammar.
- 58 existing notes updated (fields and/or tags); 14 already matched.
- 323 course entries: 240 vocabulary and 83 grammar, including 12 reused shared French vocabulary cards.
- Verified all 323 entries match the sources with no pending changes on a second pass.
- Verified scheduling and review counters on all 72 reused cards after the home-deck repair.
- Seven offline regression tests passed.
- The original importer, pre-import notes/card states, and added-note IDs are in `backups/`.

Filtered-deck behavior: [Anki manual](https://docs.ankiweb.net/filtered-decks.html).

## Update on 2026-09-23

- Checked all 51 embedded screenshots/photos in L5–L6 and TUT 3–4, including the recruitment exercise added to TUT 4 on 23 September. Audio-only responses were not independently verified.
- Consolidated the newer written notes and added 80 further screenshot vocabulary entries plus nine Unité 6 grammar prompts.
- Imported 227 new notes (218 vocabulary, nine grammar); updated or tagged eight shared notes; 533 entries already matched.
- Verified all 768 course entries match the sources, with no pending changes. All 541 existing cards retained their scheduling and review counters.
- Seven offline importer checks and `git diff --check` passed.
- Backup: [20260923-161633-591144.json](backups/20260923-161633-591144.json); [receipt](backups/20260923-161633-591144.receipt.json).
- Imported into local Anki; no AnkiWeb sync requested. Rebuild the LAF2201 filtered deck to refresh its study batch.
