"""Run inside Anki's debug console to consolidate the life_changes practice decks."""
from pathlib import Path
from datetime import datetime
import json

def run():
    from aqt import mw
    col=mw.col
    target=col.decks.by_name('LAF2201 Topics::Life Changes')
    source=col.decks.by_name('LAF2201 Topics::Life Changes and Moving')
    if not source:
        print('Life Changes decks are already combined.'); return
    if not target or not target.get('dyn') or not source.get('dyn'):
        raise RuntimeError('Expected two filtered decks; no changes made.')
    if any(d.name.startswith(source['name'] + '::') for d in col.decks.all_names_and_ids()):
        raise RuntimeError('Source deck has child decks; no changes made.')
    query='tag:fr::laf2201 (tag:fr::laf2201::topic::life_changes OR tag:fr::laf2201::batch_20261020::life_changes)'
    ids=set(col.find_cards(query))
    ids.update(col.find_cards('deck:"LAF2201 Topics::Life Changes"'))
    ids.update(col.find_cards('deck:"LAF2201 Topics::Life Changes and Moving"'))
    attrs=('id','nid','did','odid','due','odue','ivl','factor','reps','lapses')
    before=[{k:getattr(col.get_card(cid),k) for k in attrs} for cid in sorted(ids)]
    root=Path(__file__).resolve().parent
    (root/'backups').mkdir(exist_ok=True)
    backup=root/'backups'/('life_changes-merge-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json')
    backup.write_text(json.dumps(dict(cards=before,decks=[target,source],tags={str(c['nid']):col.get_note(c['nid']).tags for c in before}),ensure_ascii=False,indent=2)+'\n')
    revlog=col.db.scalar('select count(*) from revlog')
    borrowed=[c['id'] for c in before if c['odid']]
    if borrowed: col.sched.remFromDyn(borrowed)
    for nid in {c['nid'] for c in before}:
        note=col.get_note(nid)
        if 'fr::laf2201::topic::life_changes' not in note.tags:
            note.tags.append('fr::laf2201::topic::life_changes');col.update_note(note)
    # Preserve existing random order and preview settings, expanding membership.
    target['terms'][0][0]='tag:fr::laf2201 tag:fr::laf2201::topic::life_changes'
    target['terms'][0][1]=1000000
    col.decks.save(target)
    col.sched.rebuild_filtered_deck(target['id'])
    eligible=set(col.find_cards(query+' -is:suspended -is:buried'))
    loaded=set(col.find_cards('deck:"LAF2201 Topics::Life Changes"'))
    if loaded!=eligible: raise RuntimeError(f'Membership check failed; backup: {backup}')
    for old in before:
        c=col.get_card(old['id'])
        assert all(getattr(c,k)==old[k] for k in ('ivl','factor','reps','lapses'))
        assert (c.odid or c.did)==(old['odid'] or old['did'])
        assert (c.odue if c.odid else c.due)==(old['odue'] if old['odid'] else old['due'])
    assert col.db.scalar('select count(*) from revlog')==revlog
    assert not col.find_cards('deck:"LAF2201 Topics::Life Changes and Moving"')
    col.decks.remove([source['id']])
    receipt=dict(combined_cards=len(ids),loaded=len(loaded),backup=str(backup))
    (root/'life_changes-merge-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    mw.reset();mw.moveToState('deckBrowser')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': run()
