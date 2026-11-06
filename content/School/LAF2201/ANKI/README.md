# LAF2201 Anki

## Important Unité 7 vocabulary — manual import

Run [add_unit7_vocab_in_anki.py](add_unit7_vocab_in_anki.py) in Anki's debug console:

```python
import runpy; runpy.run_path('/Users/kienanana/Documents/VAULT/School/LAF2201/ANKI/add_unit7_vocab_in_anki.py', run_name='__main__')
```

The curated [manifest](new-vocab-20261013.json) contains 201 important entries from L7 and TUT 5–6: 81 housing, 50 life changes, 32 family, seven film genres, and 31 frequency/general expressions. The preview on 2026-10-13 found 189 new notes and 12 existing matches. The script creates **LAF2201 Topics::Housing** and **LAF2201 Topics::Life Changes**, refreshes the four relevant existing topic decks, and retains normal home decks and review history. Practice decks have rescheduling disabled, as with the existing topics. It saves a backup before changes and a verification receipt afterward; reruns reuse existing notes. It does not sync to AnkiWeb. The manual import has not yet been run.

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

## Missing vocabulary prepared on 2026-10-20

Live AnkiConnect audit: 1,333 French notes, including 998 tagged LAF2201.
Of 1,153 unique vocabulary entries in the current bank, 909 matched existing
notes and 244 were missing. Grammar was excluded from this vocabulary audit.
The parser copy `french_vocab_20261020.py` also handles the chronological routine
and housing abbreviation tables, and excludes the English “also dear” annotation
from French fronts.

Prepared, **not imported**: [manifest](new-vocab-20261020.json),
[audit](vocab-audit-20261020.json), and
[manual importer](add_missing_vocab_20261020_in_anki.py).

In Anki, open the debug console (Mac: Cmd+Shift+;) and run:

```python
import runpy; runpy.run_path('/Users/kienanana/Documents/VAULT/School/LAF2201/ANKI/add_missing_vocab_20261020_in_anki.py', run_name='__main__')
```

This creates nine filtered practice decks under **LAF2201 New Vocab 2026-10-20**:
Housing and Furniture (83), Family and Relationships (20), Life Changes and
Moving (23), Films and Stories (17), Everyday Expressions (21), Moving Abroad
(15), Telephone Calls (41), Address Changes and Correspondence (19), and Daily
Routines (5). New cards live in French::Vocab. Practice rescheduling is disabled.
The importer rechecks for existing matches, leaves reused note fields untouched,
saves a local audit backup, verifies content and existing review counters, and
writes `vocab-20261020-manual-receipt.json`. It can be rerun and does not sync
to AnkiWeb. Counts may shrink if other imports happen before running it.

## Unité 8 — prepared on 2026-11-03

Read-only AnkiConnect inspection found 1,577 `French Vocab` notes. The curated
[manifest](unit8-vocab.json) contains 171 unique entries from the Unité 8 lesson
banks and the activity-book audit: **158 new notes and 13 existing matches** at
preview time. This covers the previously unimported body/health and L10 vocabulary
as well as the later activity-book additions. Examples stay on the back of their
headword card; they are not separately imported. Grammar is excluded.

Run [add_unit8_vocab_in_anki.py](add_unit8_vocab_in_anki.py) inside Anki's debug
console (Mac: Cmd+Shift+;), then execute with Cmd+Return:

```python
import runpy; runpy.run_path('/Users/kienanana/Documents/VAULT/School/LAF2201/ANKI/add_unit8_vocab_in_anki.py', run_name='__main__')
```

| Topic deck | Action | Unit 8 entries | New at preview | Reused |
| --- | --- | ---: | ---: | ---: |
| Unité 8 - Situation 1 - Health and Wellbeing | Create under LAF2201 Topics | 66 | 60 | 6 |
| Unité 8 - Situations 2-3 - Technology and Communication | Create under LAF2201 Topics | 82 | 76 | 6 |
| Work and Education | Extend existing deck | 10 | 9 | 1 |
| General Vocabulary | Extend existing deck | 13 | 13 | 0 |

AnkiConnect is used for the preparatory inspection. The script runs through Anki's
collection API inside its console; calling the AnkiConnect HTTP server from its own
UI thread could deadlock. The script rechecks current notes before writing. New
notes live in **French::Vocab**, and topic decks are filtered practice decks with
rescheduling disabled. Selected existing cards are returned from any other
filtered deck before loading the target topic. The two reused topic searches keep
previous entries, except Unit 8 cards assigned to another of these four topics.
No decks or notes are deleted, and no AnkiWeb sync is performed.

Existing content and tags are preserved, with three explicit exceptions: the old
`une brosse à dent` spelling becomes `une brosse à dents`; the reused `les yeux`
card gains the singular `l'œil` in Notes; and the reused `aider` card gains its
`aider quelqu'un à + infinitive` construction in Notes. Keys and note IDs remain
unchanged. Existing home decks, home due values, review counters and the review log
are verified after import.

A timestamped backup of the plan, reused notes, affected card states and deck
settings is saved in `backups/` before writes. The script creates
`unit8-import-receipt.json` after verification and can be rerun without adding
duplicate notes. The current [preview](unit8-preview.json) is not an import receipt.
The script has been prepared and tested offline; it has **not** been run against
the collection.

Offline checks (seven tests: examples, aliases, content, reruns, ambiguous matches,
existing deck searches, and legacy deck-name handling):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 School/LAF2201/ANKI/test_unit8_import.py
```

The two new decks include the unit and situation in their names. The shared Work
and Education and General Vocabulary decks retain their existing names. If the
script was already run with the original two names, rerunning renames those decks
in place rather than creating duplicates.
