# LAF2201 listening decks

Prepared from the live Anki collection on 5 November 2026. These are new normal
decks with independent listening progress. Your original notes, reading cards,
filtered decks, scheduling and review history are preserved.

| Deck under LAF2201 Listening | Cards | Coverage |
| --- | ---: | --- |
| Unité 7 - Housing | 166 | Full Housing topic, furniture, rental advertisements, comparisons, wall and roof |
| Unité 7 - Life Changes | 110 | Full Life Changes topic, moving abroad, moving enquiries, address changes and correspondence |
| Unité 8 - Health and Wellbeing | 71 | Full Health topic plus relevant advice and memory vocabulary |
| Unité 8 - Technology and Communication | 154 | Full Technology topic, telephone and written communication, Unit 8 general expressions and language learning |

All 171 notes tagged for the Unit 8 import appear in the listening set. Shared
words deliberately appear in more than one topic when useful. The complete
483-note source set becomes 501 listening cards, using 471 unique recordings.
This covers the existing imported topic vocabulary and selected related words;
it is not a claim that every possible exam word has been predicted.

## Import in Anki

Open Anki, press **Cmd+Shift+;**, paste this line, then press **Cmd+Return**:

```python
import runpy; runpy.run_path('/Users/kienanana/Documents/VAULT/School/LAF2201/ANKI/create_listening_decks_in_anki.py', run_name='__main__')
```

Wait for `Done. Open LAF2201 Listening.` and close the console. The script copies
the prepared recordings into Anki's media folder and adds the four decks. It
saves an audit backup and import receipt, checks existing card states and source
notes, and can be rerun without duplicate listening cards. It stops before
changes if a source note has changed since preparation.

No AnkiWeb sync is triggered. After checking playback locally, sync Anki normally
and let media syncing finish if you want the recordings on another device.

## Study

The front plays French audio without revealing the written word. Press **R** to
replay. Recall the meaning (or write what you heard), then reveal French, English,
the exact spoken text, and the original notes/examples. Rate your listening
recognition, independently of whether you already know the written word.

The recordings use the installed French (France) **Thomas** synthetic voice at
175 words per minute. No TTS add-on, account, API key or on-device French voice
installation is needed for playback. Housing abbreviations are spoken in full;
gender alternatives are read separately; grammar formulas use short grammatical
examples instead of reading English labels such as “infinitive”. The exact spoken
wording is displayed on the back. These are vocabulary recordings, not textbook
dialogues or authentic multi-speaker listening exercises.

Study one child deck at a time. The daily new-card limit may show fewer cards than
the total above; use Browse to see all cards. Start with the normal daily batch
instead of trying to learn all 501 at once.

See [coverage.md](coverage.md) for every source expression and spoken version.
The generated manifest and WAV files are kept here so the console script can be
run without network access.

## Maintenance

`build_listening_assets.py` prepares the manifest from a read-only AnkiConnect
notes snapshot. `--audio` generates missing WAV files with macOS `say` and
`afconvert`; generation verifies that each file contains audio frames.
`test_listening_import.py` checks the full import and rerun against a temporary
collection using the installed Anki API, including question audio, hidden French,
original card-state preservation and refusal to import changed source notes.
