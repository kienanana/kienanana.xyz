"""Run with runpy.run_path() inside Anki's debug console. Reusable after imports."""
from pathlib import Path
from datetime import datetime
import importlib.util
import json
import html
from collections import Counter

ROOT = Path(__file__).resolve().parent
PREFIX = 'fr::laf2201::topic::'
TOPICS = {
 'clothing': 'Clothing and Shopping',
 'people': 'People and Feelings',
 'work': 'Work and Education',
 'routine': 'Daily Routines',
 'leisure': 'Music, Arts and Leisure',
 'time': 'Time, Holidays and Numbers',
 'communication': 'Appointments and Communication',
 'general': 'General Vocabulary',
 'past': 'Grammar - Past Tenses',
 'grammar': 'Grammar - Other',
}

def classify(e):
    c, f = e['category'], e['french'].lower()
    if e.get('kind') == 'grammar':
        return 'past' if c.split(' > ')[-1] in ('Passé composé','Past participles','Imparfait','Tense choice') else 'grammar'
    if c.startswith(('Clothing','Colours','Shopping','Laundry')): return 'clothing'
    if c.startswith(('Atmosphere','Emotions','Describing people','Personal qualities','Décrire une personne')): return 'people'
    if c.startswith(('Education','Work and','Travail et','Profil professionnel')): return 'work'
    if c.startswith(('Music','Activities','Art')): return 'leisure'
    if c.startswith(('Time','Large numbers')): return 'time'
    if c.startswith('Prendre rendez-vous') or c.endswith('Question words'): return 'communication'
    if c.startswith('Verbes pronominaux'): return 'routine'
    if c.startswith('More routine'):
        if 'Describing colleagues' in c: return 'work'
        if f.startswith(('se ','s’',"s'",'prendre son','ça fait','une danseuse','une trottinette')): return 'routine'
        return 'time'
    if c.endswith('Personality and casting'):
        if f.startswith(('un rôle','un premier','un rôle secondaire','un long métrage','un court métrage','un casting','réaliser','intitulé','le cinéma')): return 'leisure'
        if f.startswith(('un recruteur','rechercher','un domaine','un directeur')): return 'work'
        return 'people'
    if c.endswith('Daily routine and sequencing'): return 'routine'
    if c.endswith('Recruitment and professional profiles'):
        if f.startswith(('un parapluie','une casquette','une valise','des lunettes','des gants','une tunique')): return 'clothing'
        if f.startswith(('frisé','malin','une main','un bras','le dos','une tête','le bout','une drôle')): return 'people'
        if f.startswith(('c’est parfait',"c'est parfait",'allô','asseyez')): return 'communication'
        if f in ('derrière','fumer','tenir'): return 'general'
        return 'work'
    return 'general'

def run():
    from aqt import mw
    from anki.consts import DYN_RANDOM
    spec=importlib.util.spec_from_file_location('french_topic_source','/Users/kienanana/Documents/obsidian-scripts/french.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    entries=mod.load_banks('LAF2201')+mod.load_grammar('LAF2201')
    source={mod.fold(e['french']):e for e in entries}
    col=mw.col
    note_ids=col.find_notes('tag:fr::laf2201')
    assignments={}
    for nid in note_ids:
        note=col.get_note(nid)
        key=mod.fold(html.unescape(note['French']))
        if key not in source: raise RuntimeError(f'Unmapped course note {nid}: {note["French"]}')
        assignments[nid]=classify(source[key])
    if set(assignments.values()) != set(TOPICS): raise RuntimeError('Empty or missing topic; no changes made.')
    names={key:'LAF2201 Topics::'+value for key,value in TOPICS.items()}
    for name in names.values():
        d=col.decks.by_name(name)
        if d and not d.get('dyn'): raise RuntimeError(f'{name} exists as a normal deck.')
    parent=col.decks.by_name('LAF2201 Topics')
    if parent and parent.get('dyn'): raise RuntimeError('Topic parent must be a normal deck.')
    ids=col.find_cards('tag:fr::laf2201')
    attrs=('id','nid','did','odid','due','odue','type','queue','ivl','factor','reps','lapses','left')
    before=[{k:getattr(col.get_card(cid),k) for k in attrs} for cid in ids]
    backup=ROOT/'backups'/('topic-decks-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json')
    backup.write_text(json.dumps({'cards':before,'tags':{nid:col.get_note(nid).tags for nid in note_ids},'decks':list(col.decks.all())},ensure_ascii=False,indent=2))
    revlogs=col.db.scalar('select count(*) from revlog')
    for nid,topic in assignments.items():
        note=col.get_note(nid)
        tags=[t for t in note.tags if not t.startswith(PREFIX)]+[PREFIX+topic]
        if sorted(tags)!=sorted(note.tags):
            note.tags=tags
            col.update_note(note)
    # Cards cannot occupy two filtered decks. Return course cards to their home
    # decks before building mutually exclusive topic batches. Keep old decks.
    borrowed=[c['id'] for c in before if c['odid']]
    if borrowed: col.sched.remFromDyn(borrowed)
    result=[]
    for key,name in names.items():
        query=f'tag:fr::laf2201 tag:{PREFIX}{key}'
        existing=col.decks.by_name(name)
        did=existing['id'] if existing else col.decks.new_filtered(name)
        deck=col.decks.get(did)
        deck.update(terms=[[query,1000000,DYN_RANDOM]],resched=False,separate=False,
                    previewDelay=1,previewAgainSecs=60,previewHardSecs=600,previewGoodSecs=0)
        col.decks.save(deck)
        col.sched.rebuild_filtered_deck(did)
        result.append({'name':name,'query':query,'total':len(col.find_cards(query)),
                       'loaded':len(col.find_cards(f'deck:"{name}"'))})
        eligible=len(col.find_cards(query+' -is:suspended -is:buried'))
        assert result[-1]['loaded']==eligible, (name, result[-1], eligible)
    for old in before:
        c=col.get_card(old['id'])
        for attr in ('ivl','factor','reps','lapses'):
            assert getattr(c,attr)==old[attr],(c.id,attr)
        assert (c.odid or c.did)==(old['odid'] or old['did']),c.id
        assert (c.odue if c.odid else c.due)==(old['odue'] if old['odid'] else old['due']),c.id
    assert col.db.scalar('select count(*) from revlog')==revlogs
    assert len(col.find_cards('tag:fr::laf2201'))==len(ids)
    receipt={'topics':result,'cards':len(ids),'notes':len(note_ids),'backup':str(backup),'rescheduling':False,'limit':1000000}
    (ROOT/'topic-decks.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    mw.reset()
    mw.moveToState('deckBrowser')
    print(json.dumps(receipt,ensure_ascii=False,indent=2))

if __name__=='__main__':
    run()
