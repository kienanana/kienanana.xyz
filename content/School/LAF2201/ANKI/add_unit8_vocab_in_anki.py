"""Run in Anki's debug console. AnkiConnect is used for the preparatory audit.
The console import uses mw.col directly to avoid calling AnkiConnect from its own UI thread.
No sync, deletion, or changes to the normal home decks of existing cards.
Offline preview: python3 add_unit8_vocab_in_anki.py --preview SNAPSHOT.json
"""
from pathlib import Path
from datetime import datetime
import importlib.util
import json
import html
import sys

ROOT = Path(__file__).resolve().parent
PREFIX = 'fr::laf2201::unit8::'
TOPICS = {
    'health': 'LAF2201 Topics::Unité 8 - Situation 1 - Health and Wellbeing',
    'technology': 'LAF2201 Topics::Unité 8 - Situations 2-3 - Technology and Communication',
    'education': 'LAF2201 Topics::Work and Education',
    'general': 'LAF2201 Topics::General Vocabulary',
}
LEGACY_NAMES = {
    'health': 'LAF2201 Topics::Health and Wellbeing',
    'technology': 'LAF2201 Topics::Technology and Communication',
}
ATTRS = ('id', 'nid', 'did', 'odid', 'due', 'odue', 'type', 'queue',
         'ivl', 'factor', 'reps', 'lapses', 'left')


def find_topic_deck(manager, topic):
    name = TOPICS[topic]
    deck = manager.by_name(name)
    legacy = manager.by_name(LEGACY_NAMES[topic]) if topic in LEGACY_NAMES else None
    if deck and legacy and deck['id'] != legacy['id']:
        raise RuntimeError(f'Both old and new topic names exist for {topic}; no changes made.')
    deck = deck or legacy
    if deck and not deck.get('dyn'):
        raise RuntimeError(f'{deck["name"]} is a normal deck; no changes made.')
    return deck


def source_module():
    spec = importlib.util.spec_from_file_location('laf2201_unit8_source', ROOT / 'french_vocab_20261020.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_entries():
    entries = json.loads((ROOT / 'unit8-vocab.json').read_text())
    seen = set()
    mod = source_module()
    for e in entries:
        if e['topic'] not in TOPICS or not e['french'].strip() or not e['english'].strip():
            raise ValueError(f'Invalid manifest entry: {e}')
        key = mod.fold(e['french'])
        if key in seen:
            raise ValueError(f'Duplicate vocabulary front: {e["french"]}')
        seen.add(key)
    return entries


def make_plan(entries, current):
    mod = source_module()
    plan = mod.make_plan(entries, current)
    for item in plan:
        entry = item['entry']
        item['note']['tags'] += [PREFIX + entry['topic'], 'fr::laf2201::unit8']
        # Reuse all existing content, except two explicit explanatory additions
        # and the legacy toothbrush spelling correction listed in the manifest.
        if item['old']:
            fields = {k: item['old']['fields'][k]['value'] for k in mod.FIELDS}
            extra = entry.get('reuse_note')
            if extra and html.escape(extra) not in fields['Notes']:
                fields['Notes'] += ('<br>' if fields['Notes'] else '') + html.escape(extra)
            old_front = mod.plain(fields['French'])
            if entry.get('correct_legacy_front') == old_front:
                fields['French'] = html.escape(entry['french'])
            item['note']['fields'] = fields
    return plan


def deck_query(topic, existing=None):
    query = f'tag:fr::laf2201 tag:{PREFIX}{topic}'
    if existing:
        terms = existing.get('terms', [])
        if len(terms) != 1 or not terms[0][0].strip():
            raise ValueError(f'Expected one search term in {existing["name"]}; no changes made.')
        old = terms[0][0]
        # Keep all previous members of reused topic decks. Do not grow the
        # query on subsequent runs.
        if PREFIX + topic not in old:
            query = f'(({old}) -tag:fr::laf2201::unit8) OR ({query})'
        else:
            query = old
    return query


def summary(plan):
    result = {'entries': len(plan), 'new_notes': 0, 'reused_notes': 0, 'topics': []}
    for topic, name in TOPICS.items():
        rows = [p for p in plan if p['entry']['topic'] == topic]
        new = sum(p['old'] is None for p in rows)
        result['new_notes'] += new
        result['reused_notes'] += len(rows) - new
        result['topics'].append({'name': name, 'unit8_entries': len(rows), 'new_notes': new,
                                 'reused_notes': len(rows) - new})
    return result


def run():
    from aqt import mw
    from anki.consts import DYN_RANDOM
    col = mw.col
    if not col:
        raise RuntimeError('Open an Anki profile first.')
    mod = source_module()
    entries = load_entries()
    model = col.models.by_name(mod.MODEL)
    home = col.decks.by_name(mod.DECK)
    if not model or not home or home.get('dyn'):
        raise RuntimeError('Expected French Vocab note type and normal French::Vocab deck; no changes made.')
    if not set(mod.FIELDS).issubset({f['name'] for f in model['flds']}):
        raise RuntimeError('French Vocab fields have changed; no changes made.')
    parent = col.decks.by_name('LAF2201 Topics')
    if parent and parent.get('dyn'):
        raise RuntimeError('LAF2201 Topics must be a normal parent deck; no changes made.')

    decks, queries = {}, {}
    for topic, name in TOPICS.items():
        deck = find_topic_deck(col.decks, topic)
        decks[topic] = deck
        queries[topic] = deck_query(topic, deck)

    current = []
    for nid in col.find_notes('"note:French Vocab"'):
        note = col.get_note(nid)
        current.append({'noteId': nid, 'tags': list(note.tags),
                        'fields': {k: {'value': note[k]} for k in mod.FIELDS}})
    plan = make_plan(entries, current)  # All duplicate/ambiguity checks precede writes.
    print(json.dumps(summary(plan), ensure_ascii=False, indent=2))
    old_ids = {p['old']['noteId'] for p in plan if p['old']}
    affected = set()
    for nid in old_ids:
        affected.update(col.find_cards(f'nid:{nid}'))
    for topic, name in TOPICS.items():
        affected.update(col.find_cards(queries[topic]))
        if decks[topic]:
            affected.update(col.find_cards(f'deck:"{decks[topic]["name"]}"'))
    before = [{k: getattr(col.get_card(cid), k) for k in ATTRS} for cid in sorted(affected)]
    before_notes = {str(nid): {'tags': list(col.get_note(nid).tags),
                             'fields': {k: col.get_note(nid)[k] for k in mod.FIELDS}}
                    for nid in old_ids}
    backup_dir = ROOT / 'backups'
    backup_dir.mkdir(exist_ok=True)
    backup = backup_dir / ('unit8-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.json')
    backup.write_text(json.dumps({'plan': plan, 'notes': before_notes, 'cards': before,
                                  'decks': list(col.decks.all())}, ensure_ascii=False, indent=2) + '\n')
    revlogs = col.db.scalar('select count(*) from revlog')
    for topic, deck in decks.items():
        if deck and deck['name'] != TOPICS[topic]:
            col.decks.rename(deck, TOPICS[topic])
    added, selected, updated = [], [], []
    for item in plan:
        desired = item['note']
        if item['old']:
            note = col.get_note(item['old']['noteId'])
            # Keep all unrelated tags and fields. This batch's four tags are
            # exclusive so a card is assigned to only one target topic here.
            tags = sorted(set([t for t in note.tags if not t.startswith(PREFIX)] + desired['tags']))
            fields_changed = any(note[k] != v for k, v in desired['fields'].items())
            if sorted(note.tags) != tags or fields_changed:
                note.tags = tags
                for k, v in desired['fields'].items():
                    note[k] = v
                col.update_note(note)
                updated.append(note.id)
        else:
            note = col.new_note(model)
            for k, v in desired['fields'].items():
                note[k] = v
            note.tags = sorted(set(desired['tags']))
            col.add_note(note, home['id'])
            added.append(note.id)
        selected.append(note.id)

    # Selected existing cards may already be borrowed by another practice deck.
    borrowed = [c['id'] for c in before if c['nid'] in old_ids and c['odid']]
    if borrowed:
        col.sched.remFromDyn(borrowed)
    results = []
    for topic, name in TOPICS.items():
        existing = decks[topic]
        did = existing['id'] if existing else col.decks.new_filtered(name)
        deck = col.decks.get(did)
        deck.update(terms=[[queries[topic], 1000000, DYN_RANDOM]], resched=False, separate=False,
                    previewDelay=1, previewAgainSecs=60, previewHardSecs=600, previewGoodSecs=0)
        col.decks.save(deck)
        col.sched.rebuild_filtered_deck(did)
        eligible = set(col.find_cards(f'({queries[topic]}) -is:suspended -is:buried'))
        loaded = set(col.find_cards(f'deck:"{name}"'))
        if loaded != eligible:
            raise RuntimeError(f'Membership check failed for {name}; backup: {backup}')
        results.append({'name': name, 'created': existing is None,
                        'total_topic_cards': len(col.find_cards(queries[topic])), 'loaded': len(loaded)})

    for old in before:
        card = col.get_card(old['id'])
        for attr in ('ivl', 'factor', 'reps', 'lapses'):
            if getattr(card, attr) != old[attr]:
                raise RuntimeError(f'Card {card.id}: {attr} changed; backup: {backup}')
        if (card.odid or card.did) != (old['odid'] or old['did']):
            raise RuntimeError(f'Home deck changed for {card.id}; backup: {backup}')
        if (card.odue if card.odid else card.due) != (old['odue'] if old['odid'] else old['due']):
            raise RuntimeError(f'Home due changed for {card.id}; backup: {backup}')
    if col.db.scalar('select count(*) from revlog') != revlogs:
        raise RuntimeError(f'Review log changed; backup: {backup}')
    for item, nid in zip(plan, selected):
        note = col.get_note(nid)
        if any(note[k] != v for k, v in item['note']['fields'].items()):
            raise RuntimeError(f'Content verification failed for {nid}; backup: {backup}')
        if PREFIX + item['entry']['topic'] not in note.tags:
            raise RuntimeError(f'Topic verification failed for {nid}; backup: {backup}')
    after = [{'noteId': nid, 'tags': list(col.get_note(nid).tags),
              'fields': {k: {'value': col.get_note(nid)[k]} for k in mod.FIELDS}}
             for nid in selected]
    if any(p['old'] is None for p in make_plan(entries, after)):
        raise RuntimeError(f'Rerun would add duplicate notes; backup: {backup}')
    receipt = dict(summary(plan), added_note_ids=added, updated_note_ids=updated,
                   decks=results, backup=str(backup), rescheduling=False, ankiweb_sync=False)
    (ROOT / 'unit8-import-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    mw.reset()
    mw.moveToState('deckBrowser')
    print('Unité 8 import complete. Receipt: ' + str(ROOT / 'unit8-import-receipt.json'))
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    if '--preview' in sys.argv:
        current = json.loads(Path(sys.argv[sys.argv.index('--preview') + 1]).read_text())
        print(json.dumps(summary(make_plan(load_entries(), current)), ensure_ascii=False, indent=2))
    else:
        run()
