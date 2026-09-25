"""Offline regression checks for the French Anki importer.
Run: python3 test_french.py /path/to/french.py
"""
import importlib.util
import json
from pathlib import Path
import sys
import unittest
path = Path(sys.argv.pop(1)) if len(sys.argv)>1 else Path.home()/'Documents/obsidian-scripts/french.py'
spec=importlib.util.spec_from_file_location('french',path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class ImportTests(unittest.TestCase):
 def setUp(self):
  self.entries=m.load_banks('LAF2201')+m.load_grammar('LAF2201')
 def test_table_coverage_and_prose_exclusion(self):
  e={x['french']:x for x in self.entries}
  for word in ['blanc / blanche','faire du jardinage','animé / animée','tranquille','devenir','un milliard']:
   self.assertIn(word,e)
  self.assertEqual(e['neuf / neuve']['english'],'brand-new / unused')
  self.assertIn('plural',e['neuf / neuve']['notes'])
  self.assertEqual(e['devenir']['english'],'to become')
  self.assertFalse(any(x.startswith(('Simple colour','Compound colour','Marron,')) for x in e))
  self.assertIn("l'été dernier",e);self.assertIn("l'hiver dernier",e)
  self.assertNotIn('nouveau / nouvelle',e)
 def test_sources_and_keys(self):
  keys=[m.build_note(e)['fields']['Key'] for e in self.entries]
  self.assertEqual(len(keys),len(set(keys)))
  for e in self.entries:
   if e.get('source'):self.assertTrue((m.VAULT/e['source']).exists(),e['source'])
 def test_legacy_match_preserves_key_tags_and_notes(self):
  entry=next(e for e in self.entries if e['french']=='une statue vivante')
  old={'noteId':7,'fields':{k:{'value':v} for k,v in {'French':'une statue vivante','English':'living statue','Notes':'My example','Key':'laf2201-statue-vivante'}.items()},'tags':['laf2201','tut1','personal']}
  plan=m.make_plan([entry],[old])[0]
  self.assertEqual(plan['old']['noteId'],7)
  self.assertNotIn('Key',plan['fields']);self.assertNotIn('Notes',plan['fields'])
  self.assertIn('fr::laf2201',plan['tags'])
  self.assertIn('personal',old['tags'])
 def test_renamed_front_matches_existing(self):
  e=next(e for e in self.entries if e['french']=='pareil / pareille')
  old={'noteId':8,'fields':{k:{'value':v} for k,v in {'French':'pareil','English':'same','Notes':'','Key':'pareil'}.items()},'tags':['fr::managed']}
  p=m.make_plan([e],[old])[0]
  self.assertEqual(p['action'],'update');self.assertEqual(p['old']['noteId'],8)
 def test_second_run_is_noop(self):
  old=[]
  for i,e in enumerate(self.entries):
   n=m.build_note(e)
   old.append(dict(noteId=i+1,fields={k:{'value':v} for k,v in n['fields'].items()},tags=n['tags']))
  self.assertTrue(all(p['action']=='unchanged' for p in m.make_plan(self.entries,old)))
 def test_ambiguity_fails_before_mutation(self):
  e=self.entries[0];n=m.build_note(e)
  old=[dict(noteId=i,fields={k:{'value':v} for k,v in n['fields'].items()},tags=n['tags']) for i in [1,2]]
  with self.assertRaises(ValueError):m.make_plan([e],old)
 def test_shared_course_tags_survive_deduplication(self):
  both=m.load_banks()
  e=next(x for x in both if x['french']=='blanc / blanche')
  self.assertEqual(set(e['courses']),{'LAF1201','LAF2201'})
  self.assertEqual(m.build_note(next(x for x in self.entries if x['french']=='une batterie'))['deckName'],'French::Vocab')

if __name__=='__main__':unittest.main()
