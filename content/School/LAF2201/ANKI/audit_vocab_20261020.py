"""Read-only AnkiConnect comparison; writes local reports only."""
import importlib.util,json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('french_audit',ROOT/'french_vocab_20261020.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
entries=json.loads((ROOT/'bank-vocab-20261020.json').read_text())
current=f.existing_notes()
plan=f.make_plan(entries,current)
missing=[p['entry'] for p in plan if p['action']=='add']
for e in missing:
    c=e['category']
    if c.startswith('Telephone'): t='telephone'
    elif c.startswith('Changes of address'): t='correspondence'
    elif c.startswith('Further family and housing'):
        t='family' if c.endswith(' > Family') else 'abroad' if c.endswith(' > Moving abroad') else 'housing'
    elif c.startswith('Housing'): t='housing'
    elif c.startswith('Life changes'): t='life_changes'
    elif c.startswith('Family'): t='family'
    elif c.startswith('Further useful'): t='expressions'
    elif c.startswith('Verbes pronominaux'): t='routine'
    elif c.startswith('Film genres'): t='films'
    else: t='other'
    e['topic']=t
(ROOT/'new-vocab-20261020.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2)+'\n')
summary={'existing_french_notes':len(current),'existing_course_notes':sum('fr::laf2201' in n['tags'] for n in current),'unique_bank_entries':len(entries),'already_present':len(entries)-len(missing),'missing_notes':len(missing),'topics':dict(Counter(e['topic'] for e in missing)),'categories':dict(Counter(e['category'] for e in missing)),'decks':f.anki('deckNames')}
(ROOT/'vocab-audit-20261020.json').write_text(json.dumps({'summary':summary,'plan':plan},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
