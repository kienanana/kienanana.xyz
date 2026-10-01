"""Run inside Anki's debug console with runpy.run_path(..., run_name='__main__')."""
import json
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parent
MANAGED='is4226::lectures5a5b6_recall'
HOME='IS4226::Lectures 5-6'
NAMES={'5a':'IS4226 L5A','5b':'IS4226 L5B','6':'IS4226 L6'}

def run():
 from aqt import mw
 from anki.consts import DYN_ADDED
 col=mw.col
 cards=json.loads((ROOT/'lectures5a5b6_cards.json').read_text())
 assert len({c['id'] for c in cards})==len(cards)==109
 model=col.models.by_name('IS4226 Basic')
 assert model and len(model['tmpls'])==1
 for name in NAMES.values():
  d=col.decks.by_name(name)
  assert not d or d.get('dyn'), f'{name} is not filtered'
 d=col.decks.by_name(HOME)
 assert not d or not d.get('dyn')
 plan=[]
 for c in cards:
  tag='is4226_l56_id_'+c['id'].replace('-','_')
  ids=col.find_notes('tag:'+tag)
  assert len(ids)<=1
  note=col.get_note(ids[0]) if ids else None
  if note: assert note.mid==model['id'] and note['Card ID']==c['id']
  plan.append((c,tag,note))
 unrelated=col.find_notes('-tag:'+MANAGED)
 before={nid: (list(col.get_note(nid).fields),list(col.get_note(nid).tags)) for nid in unrelated}
 backup={'decks':list(col.decks.all()),'managed_notes':[{'id':n.id,'fields':list(n.fields),'tags':n.tags} for _,_,n in plan if n]}
 stamp=datetime.now().strftime('%Y%m%d-%H%M%S')
 (ROOT/f'lectures5a5b6_backup_{stamp}.json').write_text(json.dumps(backup,ensure_ascii=False,indent=2))
 home=col.decks.id(HOME)
 created=updated=0
 noteids=[]
 for c,tag,note in plan:
  new=note is None
  if new: note=col.new_note(model)
  fields={'Card ID':c['id'],'Front':c['front'],'Back':c['back'],'Explanation':'','Source':c['source']}
  for k,v in fields.items(): note[k]=v
  note.tags=sorted(set(note.tags+c['tags']+[tag,MANAGED]))
  if new: col.add_note(note,home); created+=1
  else: col.update_note(note); updated+=1
  noteids.append(note.id)
  check=col.get_note(note.id)
  assert all(check[k]==v for k,v in fields.items())
 result=[]
 for chapter,name in NAMES.items():
  query=f'tag:{MANAGED} tag:is4226::l{chapter}'
  selected=col.find_cards(query)
  expected=sum(c['chapter']==chapter for c in cards)
  assert len(selected)==expected
  borrowed=[cid for cid in selected if col.get_card(cid).odid]
  if borrowed: col.sched.remFromDyn(borrowed)
  existing=col.decks.by_name(name)
  did=existing['id'] if existing else col.decks.new_filtered(name)
  deck=col.decks.get(did)
  deck.update(terms=[[query,10000,DYN_ADDED]],resched=True,separate=False)
  col.decks.save(deck)
  col.sched.rebuild_filtered_deck(did)
  loaded=col.find_cards(f'deck:"{name}"')
  assert len(loaded)==len(col.find_cards(query+' -is:suspended -is:buried'))
  assert all((col.get_card(cid).odid or col.get_card(cid).did)==home for cid in selected)
  result.append({'name':name,'query':query,'total':expected,'loaded':len(loaded),'rescheduling':True})
 assert all((list(col.get_note(nid).fields),list(col.get_note(nid).tags))==old for nid,old in before.items())
 receipt={'created':created,'updated':updated,'deleted':0,'verified':len(noteids),'unrelated_notes_unchanged':len(before),'home':HOME,'filtered_decks':result,'note_ids':noteids}
 (ROOT/'lectures5a5b6_import_report.json').write_text(json.dumps(receipt,indent=2)+'\n')
 mw.reset()
 mw.moveToState('deckBrowser')
 print(json.dumps(receipt,indent=2))

if __name__=='__main__': run()
