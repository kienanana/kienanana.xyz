import importlib.util,json
from pathlib import Path
p=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('move',p/'move_new_vocab_topics_20261020.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
out={}
for name in ('Housing','Housing and Furniture'):
 ids=m.call('findCards',query='deck:"LAF2201 Topics::'+name+'"')
 cards=m.call('cardsInfo',cards=ids)
 notes=m.call('notesInfo',notes=sorted({c['note'] for c in cards}))
 out[name]={'cards':cards,'notes':notes}
a={n['fields']['French']['value'].casefold():n['noteId'] for n in out['Housing']['notes']}
b={n['fields']['French']['value'].casefold():n['noteId'] for n in out['Housing and Furniture']['notes']}
out['same_fronts']=sorted(a.keys()&b.keys())
(p/'housing-overlap-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':{k:len(v['cards']) for k,v in out.items() if isinstance(v,dict)},'same_fronts':out['same_fronts']},ensure_ascii=False,indent=2))
for k in ('Housing','Housing and Furniture'):
 print(k,':',', '.join(n['fields']['French']['value'] for n in out[k]['notes'][:15]))
