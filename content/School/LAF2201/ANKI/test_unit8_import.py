"""Offline checks for the unit-8 import, using the read-only AnkiConnect snapshot."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('unit8', ROOT / 'add_unit8_vocab_in_anki.py')
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
SNAPSHOT = ROOT.parents[2] / 'output/laf2201-unit8-review/anki-current-notes.json'


class ImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = u.load_entries()
        cls.current = json.loads(SNAPSHOT.read_text())
        cls.plan = u.make_plan(cls.entries, cls.current)

    def test_no_example_sentence_cards(self):
        fronts = {e['french'] for e in self.entries}
        self.assertIn('un souci', fronts)
        self.assertNotIn('oublier ses soucis', fronts)
        self.assertNotIn('Cette montre a beaucoup de succès.', fronts)
        self.assertIn('oublier ses soucis', next(e['notes'] for e in self.entries if e['french'] == 'un souci'))

    def test_explicit_aliases_reuse_existing_notes(self):
        by_front = {p['entry']['french']: p for p in self.plan}
        for front in ['le bras', 'la tête', 'la main', 'la motivation', 'une brosse à dents', 'aider à + infinitive']:
            self.assertIsNotNone(by_front[front]['old'], front)
        self.assertEqual(by_front['une brosse à dents']['note']['fields']['French'], 'une brosse à dents')
        # A patient (noun) is not the adjective "patient" already learned.
        self.assertIsNone(by_front['un patient / une patiente']['old'])

    def test_preserves_reused_fields_and_keys(self):
        for p in self.plan:
            if not p['old']:
                continue
            for key in ['English', 'Key']:
                self.assertEqual(p['note']['fields'][key], p['old']['fields'][key]['value'])
            if 'reuse_note' not in p['entry']:
                self.assertEqual(p['note']['fields']['Notes'], p['old']['fields']['Notes']['value'])

    def test_rerun_reuses_every_note_and_annotations_do_not_grow(self):
        after = [{'noteId': p['old']['noteId'] if p['old'] else -i-1,
                  'tags': p['note']['tags'],
                  'fields': {k: {'value': v} for k, v in p['note']['fields'].items()}}
                 for i, p in enumerate(self.plan)]
        again = u.make_plan(self.entries, after)
        self.assertTrue(all(p['old'] for p in again))
        self.assertEqual([p['note']['fields'] for p in again], [p['note']['fields'] for p in self.plan])

    def test_ambiguous_alias_stops_before_writes(self):
        entry = next(e for e in self.entries if e['french'] == 'le bras')
        original = next(p['old'] for p in self.plan if p['entry']['french'] == 'le bras')
        duplicate = dict(original, noteId=-123)
        with self.assertRaises(ValueError):
            u.make_plan([entry], [original, duplicate])

    def test_old_deck_name_reused_and_collision_rejected(self):
        from types import SimpleNamespace
        legacy = {'id': 123, 'name': u.LEGACY_NAMES['health'], 'dyn': 1}
        decks = {legacy['name']: legacy}
        manager = SimpleNamespace(by_name=decks.get)
        self.assertIs(u.find_topic_deck(manager, 'health'), legacy)
        decks[u.TOPICS['health']] = {'id': 456, 'name': u.TOPICS['health'], 'dyn': 1}
        with self.assertRaises(RuntimeError):
            u.find_topic_deck(manager, 'health')

    def test_existing_queries_preserved_and_batch_members_exclusive(self):
        old = {'name': u.TOPICS['general'], 'terms': [['tag:fr::laf2201::topic::general', 100, 0]]}
        query = u.deck_query('general', old)
        self.assertIn(old['terms'][0][0], query)
        self.assertIn('-tag:fr::laf2201::unit8', query)
        self.assertIn(u.PREFIX + 'general', query)
        self.assertEqual(query, u.deck_query('general', dict(old, terms=[[query, 1000000, 0]])))
        with self.assertRaises(ValueError):
            u.deck_query('general', dict(old, terms=[]))


if __name__ == '__main__':
    unittest.main()
