#!/usr/bin/env python3
"""Add/update L4 recall cards using the existing IS4226 Anki helpers; never delete notes."""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
CARDS = ROOT / 'is4226_week4_cards.json'
DECK = 'IS4226::Week 4'
MANAGED = 'is4226::week4_recall'
HELPER = Path.home() / 'Documents/obsidian-scripts/is4226_import_anki.py'


def load_cards():
    cards = json.loads(CARDS.read_text())
    assert cards, 'Empty input'
    ids, fronts = set(), set()
    for c in cards:
        assert c['id'].startswith('is4226-w4-') and c['id'] not in ids
        assert c['front'].strip() and c['front'] not in fronts
        assert c['back'].strip() and c['source'].startswith('L4 ')
        assert c['week'] == 4 and 'is4226::w4' in c['tags']
        assert c['type'] == 'recall'
        ids.add(c['id'])
        fronts.add(c['front'])
    return cards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    cards = load_cards()
    if args.validate_only:
        print(f'Validated {len(cards)} unique L4 recall cards.')
        return
    spec = importlib.util.spec_from_file_location('is4226_existing', HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.DECK = DECK
    helper.MANAGED = MANAGED
    # The Quiz 1 importer searches is4226_id_* when deleting stale notes.
    # Keep Week 4 ownership outside that namespace, and never call its main().
    helper.stable = lambda cid: 'is4226_w4_id_' + cid.replace('-', '_')
    plan = []
    for c in cards:
        payload = helper.payload(c)
        found = helper.invoke('findNotes', query=f'tag:{helper.stable(c["id"])}')
        if len(found) > 1:
            raise RuntimeError(f'Duplicate identity: {c["id"]}')
        if found:
            info = helper.invoke('notesInfo', notes=found)[0]
            if info['modelName'] != helper.MODEL or info['fields']['Card ID']['value'] != c['id']:
                raise RuntimeError(f'Identity mismatch: {c["id"]}')
        plan.append((c, payload, found))
    created = sum(not found for _, _, found in plan)
    print(f'Plan: create={created}, update={len(cards)-created}, delete=0; deck={DECK}')
    if not args.apply:
        return
    # Snapshot unrelated notes so the verification can confirm they stayed unchanged.
    unrelated_ids = helper.invoke('findNotes', query=f'-tag:{MANAGED}')
    before = helper.invoke('notesInfo', notes=unrelated_ids)
    helper.ensure(True)
    imported = []
    for c, payload, found in plan:
        if found:
            helper.invoke('updateNoteFields', note={'id': found[0], 'fields': payload['fields']})
            helper.invoke('addTags', notes=found, tags=' '.join(payload['tags']))
            imported.append(found[0])
        else:
            imported.append(helper.invoke('addNote', note=payload))
    infos = helper.invoke('notesInfo', notes=imported)
    for (c, payload, _), info in zip(plan, infos):
        assert info['fields']['Card ID']['value'] == c['id']
        assert all(info['fields'][k]['value'] == v for k, v in payload['fields'].items())
        assert set(payload['tags']) <= set(info['tags'])
    after = helper.invoke('notesInfo', notes=unrelated_ids)
    assert before == after, 'Unrelated notes changed during import; inspect Anki.'
    report = {'deck': DECK, 'created': created, 'updated': len(cards)-created,
              'deleted': 0, 'verified': len(infos), 'unrelated_notes_unchanged': len(before),
              'note_ids': imported}
    (ROOT / 'week4_import_report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
