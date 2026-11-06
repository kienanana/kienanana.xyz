"""Run in Anki's debug console with runpy.run_path(..., run_name='__main__').
Imports the curated L7/TUT 5–6 vocabulary and builds topic practice decks.
No AnkiConnect or AnkiWeb sync needed. Safe to rerun; IDs/history are retained.
"""
from pathlib import Path
from datetime import datetime
import importlib.util
import json
import html

ROOT = Path(__file__).resolve().parent
PREFIX = 'fr::laf2201::topic::'
TOPICS = {
    'housing': 'Housing',
    'life_changes': 'Life Changes',
    'people': 'People and Feelings',
    'leisure': 'Music, Arts and Leisure',
    'time': 'Time, Holidays and Numbers',
    'general': 'General Vocabulary',
}


def run():
    from aqt import mw
    from anki.consts import DYN_RANDOM
    spec = importlib.util.spec_from_file_location('unit7_french', '/Users/kienanana/Documents/obsidian-scripts/french.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    entries = json.loads((ROOT / 'new-vocab-20261013.json').read_text())
    original_build = mod.build_note

    def build(entry):
        note = original_build(entry)
        note['tags'] += [PREFIX + entry['topic'], 'fr::laf2201::unit7_important']
        return note

    mod.build_note = build
    col = mw.col
    model = col.models.by_name(mod.MODEL)
    if not model:
        raise RuntimeError('The existing French Vocab note type is missing; no changes made.')
    home = col.decks.by_name(mod.DECK)
    if not home or home.get('dyn'):
        raise RuntimeError('French::Vocab must exist as a normal home deck; no changes made.')
    names = {key: 'LAF2201 Topics::' + name for key, name in TOPICS.items()}
    for name in names.values():
        deck = col.decks.by_name(name)
        if deck and not deck.get('dyn'):
            raise RuntimeError(f'{name} already exists as a normal deck; no changes made.')

    current = []
    for nid in col.find_notes('"note:French Vocab"'):
        note = col.get_note(nid)
        current.append({'noteId': nid, 'tags': list(note.tags),
                        'fields': {key: {'value': note[key]} for key in mod.FIELDS}})
    plan = mod.make_plan(entries, current)
    existing_ids = [p['old']['noteId'] for p in plan if p['old']]
    card_ids = set(col.find_cards('tag:fr::laf2201'))
    for nid in existing_ids:
        card_ids.update(col.find_cards(f'nid:{nid}'))
    attrs = ('id', 'nid', 'did', 'odid', 'due', 'odue', 'type', 'queue', 'ivl', 'factor', 'reps', 'lapses', 'left')
    before = [{key: getattr(col.get_card(cid), key) for key in attrs} for cid in sorted(card_ids)]
    backup_dir = ROOT / 'backups'
    backup_dir.mkdir(exist_ok=True)
    backup = backup_dir / ('unit7-manual-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.json')
    backup.write_text(json.dumps({'plan': plan, 'cards': before, 'decks': list(col.decks.all())}, ensure_ascii=False, indent=2) + '\n')
    review_count = col.db.scalar('select count(*) from revlog')
    added, selected, changed = [], [], 0
    # All matching and deck checks finish before writes. Every reused note is
    # updated in place; only its topic tags are reassigned.
    for item in plan:
        desired = item['note']
        if item['old']:
            nid = item['old']['noteId']
            note = col.get_note(nid)
            for key, value in item['fields'].items():
                note[key] = value
            tags = sorted(set([t for t in note.tags if not t.startswith(PREFIX)] + desired['tags']))
            if item['fields'] or sorted(note.tags) != tags:
                note.tags = tags
                col.update_note(note)
                changed += 1
        else:
            note = col.new_note(model)
            for key, value in desired['fields'].items():
                note[key] = value
            note.tags = desired['tags']
            col.add_note(note, home['id'])
            nid = note.id
            added.append(nid)
        selected.append(nid)

    # A card can occupy only one filtered deck. Return the selected cards to
    # their homes, then build the two new decks and refresh existing topics.
    borrowed = [c['id'] for c in before if c['nid'] in selected and c['odid']]
    if borrowed:
        col.sched.remFromDyn(borrowed)
    results = []
    for key, name in names.items():
        query = f'tag:fr::laf2201 tag:{PREFIX}{key}'
        existing = col.decks.by_name(name)
        did = existing['id'] if existing else col.decks.new_filtered(name)
        deck = col.decks.get(did)
        deck.update(terms=[[query, 1000000, DYN_RANDOM]], resched=False, separate=False,
                    previewDelay=1, previewAgainSecs=60, previewHardSecs=600, previewGoodSecs=0)
        col.decks.save(deck)
        col.sched.rebuild_filtered_deck(did)
        loaded = len(col.find_cards(f'deck:"{name}"'))
        eligible = len(col.find_cards(query + ' -is:suspended -is:buried'))
        if loaded != eligible:
            raise RuntimeError(f'Deck verification failed for {name}: {loaded} loaded, {eligible} eligible. Backup: {backup}')
        results.append({'name': name, 'total': len(col.find_cards(query)), 'loaded': loaded})

    for old in before:
        card = col.get_card(old['id'])
        for attr in ('ivl', 'factor', 'reps', 'lapses'):
            if getattr(card, attr) != old[attr]:
                raise RuntimeError(f'Review history changed for card {card.id}; backup: {backup}')
        if (card.odid or card.did) != (old['odid'] or old['did']):
            raise RuntimeError(f'Home deck changed for card {card.id}; backup: {backup}')
        if (card.odue if card.odid else card.due) != (old['odue'] if old['odid'] else old['due']):
            raise RuntimeError(f'Home due value changed for card {card.id}; backup: {backup}')
    if col.db.scalar('select count(*) from revlog') != review_count:
        raise RuntimeError(f'Review log changed; backup: {backup}')
    for item, nid in zip(plan, selected):
        note = col.get_note(nid)
        if any(note[key] != value for key, value in item['note']['fields'].items()):
            raise RuntimeError(f'Content verification failed for {nid}; backup: {backup}')
        if PREFIX + item['entry']['topic'] not in note.tags:
            raise RuntimeError(f'Topic tag missing on {nid}; backup: {backup}')
    receipt = {'selected_entries': len(entries), 'added_notes': len(added),
               'updated_existing_notes': changed, 'added_note_ids': added,
               'decks': results, 'backup': str(backup), 'rescheduling': False}
    (ROOT / 'unit7-manual-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    mw.reset()
    mw.moveToState('deckBrowser')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
