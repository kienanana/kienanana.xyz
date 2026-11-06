"""Run in Anki's debug console. Adds four normal audio-only listening decks.

Uses pre-generated local WAV files. No network, sync, source-card changes,
filtered-deck rebuilds or deletions. Rerunning reuses listening note IDs.
"""
from pathlib import Path
from datetime import datetime
import html
import json
import wave

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'listening'
MODEL = 'LAF2201 Listening Audio'
TAG = 'laf2201_listening_v1'
FIELDS = ['French', 'English', 'Audio', 'Spoken', 'Notes', 'Source', 'Key']
FRONT = '''<div class="prompt">Listen. What does it mean?</div>
<div class="audio">{{Audio}}</div>'''
BACK = '''{{FrontSide}}<hr id="answer">
<div class="french">{{French}}</div>
<div class="english">{{English}}</div>
<div class="spoken">Recording: {{Spoken}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}'''
CSS = '''.card { font-family: -apple-system, Helvetica, Arial, sans-serif;
font-size: 24px; text-align: center; line-height: 1.5; }
.prompt { font-size: 18px; opacity: .75; margin: 16px; }
.audio { margin: 22px; } .french { font-size: 30px; margin: 12px; }
.english { margin: 12px; } .spoken { font-size: 18px; opacity: .8; margin: 18px; }
.notes { font-size: 16px; opacity: .75; margin: 18px; }'''


def expected_fields(row, audio_name=None):
    return {
        'Key': row['key'],
        'Audio': '[sound:' + (audio_name or row['audio']) + ']',
        'Spoken': html.escape(row['spoken']),
        'French': row['french'],
        'English': row['english'],
        'Notes': row['notes'],
        'Source': html.escape(f"Original note {row['source_id']}; {row['reason']}; snapshot 2026-11-05"),
    }


def run():
    from aqt import mw
    col = mw.col
    rows = json.loads((ASSETS / 'manifest.json').read_text())
    if not rows or len({r['key'] for r in rows}) != len(rows):
        raise RuntimeError('Empty manifest or duplicate keys; no changes made.')

    # Complete all checks before adding anything to the collection.
    source_ids = {r['source_id'] for r in rows}
    sources = {}
    for row in rows:
        source = col.get_note(row['source_id'])
        if dict(source.items()) != row['source_fields']:
            raise RuntimeError(f"Source note {source.id} has changed since preparation; no changes made. Rebuild the listening manifest first.")
        sources[str(source.id)] = dict(fields=dict(source.items()), tags=list(source.tags))
    for filename in {r['audio'] for r in rows}:
        with wave.open(str(ASSETS / 'media' / filename)) as audio:
            if audio.getnframes() <= 0 or audio.getframerate() <= 0:
                raise RuntimeError('Invalid audio: ' + filename)
    for name in {r['deck'] for r in rows}:
        deck = col.decks.by_name(name)
        if deck and deck.get('dyn'):
            raise RuntimeError(f'{name} must be a normal deck; no changes made.')

    model = col.models.by_name(MODEL)
    if model:
        if [f['name'] for f in model['flds']] != FIELDS or len(model['tmpls']) != 1:
            raise RuntimeError('Existing listening note type has a different schema; no changes made.')
        template = model['tmpls'][0]
        if template['qfmt'] != FRONT or template['afmt'] != BACK:
            raise RuntimeError('Listening templates have been edited; no changes made. Review before rerunning.')
    existing = {}
    for nid in col.find_notes(f'note:"{MODEL}"') if model else []:
        note = col.get_note(nid)
        key = note['Key']
        if TAG not in note.tags or key in existing:
            raise RuntimeError('Unmanaged or duplicate listening note; no changes made.')
        existing[key] = note

    # Audit all existing card state, including originals in filtered decks.
    before_cards = col.db.all('select * from cards order by id')
    before_revlog = col.db.scalar('select count(*) from revlog')
    original_ids = {r[0] for r in before_cards}
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup = ROOT / 'backups' / f'listening-{stamp}.json'
    backup.parent.mkdir(exist_ok=True)
    backup.write_text(json.dumps(dict(sources=sources, cards=before_cards,
        existing_listening={str(n.id): dict(fields=dict(n.items()), tags=n.tags) for n in existing.values()},
        model=model, manifest=rows), ensure_ascii=False, indent=2) + '\n')

    if model is None:
        model = col.models.new(MODEL)
        for name in FIELDS:
            col.models.add_field(model, col.models.new_field(name))
        template = col.models.new_template('Listen to French')
        template.update(qfmt=FRONT, afmt=BACK)
        col.models.add_template(model, template)
        model['css'] = CSS
        col.models.add(model)

    decks = {name: col.decks.id(name) for name in sorted({r['deck'] for r in rows})}
    imported_media = {}
    for filename in sorted({r['audio'] for r in rows}):
        imported_media[filename] = col.media.add_file(str(ASSETS / 'media' / filename))
    counts = {name: dict(created=0, updated=0, unchanged=0, total=0) for name in decks}
    added = []
    for row in rows:
        fields = expected_fields(row, imported_media[row['audio']])
        note = existing.get(row['key'])
        stats = counts[row['deck']]
        stats['total'] += 1
        if note:
            if dict(note.items()) != fields:
                for name, value in fields.items():
                    note[name] = value
                col.update_note(note)
                stats['updated'] += 1
            else:
                stats['unchanged'] += 1
        else:
            note = col.new_note(model)
            for name, value in fields.items():
                note[name] = value
            note.tags = [TAG, 'laf2201_listening::' + row['topic']]
            col.add_note(note, decks[row['deck']])
            added.append(note.id)
            stats['created'] += 1
        if dict(col.get_note(note.id).items()) != fields:
            raise RuntimeError('Listening content verification failed: ' + row['key'])
        cards = note.cards()
        if len(cards) != 1:
            raise RuntimeError('Expected exactly one listening card: ' + row['key'])
        if cards[0].id not in original_ids and (cards[0].odid or cards[0].did) != decks[row['deck']]:
            raise RuntimeError('New listening card placed in wrong deck: ' + row['key'])

    after_cards = [r for r in col.db.all('select * from cards order by id') if r[0] in original_ids]
    if after_cards != before_cards:
        raise RuntimeError('Existing card state changed; inspect backup: ' + str(backup))
    if col.db.scalar('select count(*) from revlog') != before_revlog:
        raise RuntimeError('Review log count changed; inspect backup: ' + str(backup))
    for nid in source_ids:
        note = col.get_note(nid)
        before = sources[str(nid)]
        if dict(note.items()) != before['fields'] or list(note.tags) != before['tags']:
            raise RuntimeError('Original note changed: ' + str(nid))
    receipt = dict(decks=counts, added_note_ids=added, media_files=len(imported_media),
                   original_notes_verified=len(source_ids), original_cards_verified=len(before_cards),
                   backup=str(backup), sync=False)
    (ASSETS / 'import-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    mw.reset()
    mw.moveToState('deckBrowser')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    print('Done. Open LAF2201 Listening. Replay audio with R. No AnkiWeb sync was performed.')


if __name__ == '__main__':
    run()
