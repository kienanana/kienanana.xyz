"""Integration check in a temporary collection using the installed Anki Python API.
Never opens the real collection. Requires Anki's Python environment.
"""
from pathlib import Path
import importlib.util, json, sys, tempfile, types
from anki.collection import Collection
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('listening_import',ROOT/'create_listening_decks_in_anki.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=json.loads((ROOT/'listening/manifest.json').read_text())
selected=[dict(r) for r in rows]
expected=len(selected)
assert expected == 501
with tempfile.TemporaryDirectory(prefix='laf-listening-test-',dir='/private/tmp') as tmp:
 p=Path(tmp); col=Collection(str(p/'collection.anki2'))
 sm=col.models.new('French Vocab')
 for f in ['French','English','Notes','Key']:col.models.add_field(sm,col.models.new_field(f))
 t=col.models.new_template('FR to EN');t.update(qfmt='{{French}}',afmt='{{English}}');col.models.add_template(sm,t);col.models.add(sm)
 source_map={}
 for r in selected:
  original_id=r['source_id']
  if original_id in source_map:
   r['source_id']=source_map[original_id];r['key']=r['topic']+':'+str(r['source_id']);continue
  n=col.new_note(sm)
  for k,v in r['source_fields'].items():n[k]=v
  n.tags=r['source_tags'];col.add_note(n,col.decks.id('Original French'))
  source_map[original_id]=n.id
  r['source_id']=n.id;r['key']=r['topic']+':'+str(n.id)
  card=n.cards()[0];card.reps=10;card.ivl=9;card.due=7;col.update_card(card)
 assets=p/'listening';assets.mkdir();(assets/'media').symlink_to(ROOT/'listening/media',target_is_directory=True)
 (assets/'manifest.json').write_text(json.dumps(selected))
 m.ROOT=p;m.ASSETS=assets
 sys.modules['aqt']=types.SimpleNamespace(mw=types.SimpleNamespace(col=col,reset=lambda:None,moveToState=lambda s:None))
 m.run();first=json.loads((assets/'import-receipt.json').read_text())
 assert sum(s['created'] for s in first['decks'].values())==expected
 ids=col.find_notes('tag:'+m.TAG)
 assert len(ids)==expected
 for nid in ids:
  note=col.get_note(nid);card=note.cards()[0]
  question=card.question()
  assert note['French'] not in question
  assert len(card.question_av_tags()) == 1
 m.run();second=json.loads((assets/'import-receipt.json').read_text())
 assert sum(s['created'] for s in second['decks'].values())==0
 assert sum(s['unchanged'] for s in second['decks'].values())==expected
 assert col.find_notes('tag:'+m.TAG)==ids
 n=col.get_note(selected[0]['source_id']);n['English']='changed source';col.update_note(n)
 try:m.run()
 except RuntimeError as e:assert 'has changed' in str(e)
 else:raise AssertionError('Source drift should stop import')
 assert len(col.find_notes('tag:'+m.TAG))==expected
 col.close()
print('PASS: real Anki 26.9.2 import, audio-only rendering, all four decks, rerun identity, original scheduling preservation, and source-drift guard')
