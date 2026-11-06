"""Run inside Anki's debug console to consolidate the housing practice decks."""
from pathlib import Path
from datetime import datetime
import json

def run():
    from aqt import mw
    col=mw.col
    target=col.decks.by_name('LAF2201 Topics::Housing')
    source=col.decks.by_name('LAF2201 Topics::Housing and Furniture')
    if not source:
        print('Housing decks are already combined.'); return
    if not target or not target.get('dyn') or not source.get('dyn'):
        raise RuntimeError('Expected two filtered decks; no changes made.')
    query='tag:fr::laf2201 (tag:fr::laf2201::topic::housing OR tag:fr::laf2201::batch_20261020::housing)'
    ids=set(col.find_cards(query))
    ids.update(col.find_cards('deck:"LAF2201 Topics::Housing"'))
    ids.update(col.find_cards('deck:"LAF2201 Topics::Housing and Furniture"'))
    attrs=('id','nid','did','odid','due','odue','ivl','factor','reps','lapses')
    before=[{k:getattr(col.get_card(cid),k) for k in attrs} for cid in sorted(ids)]
    root=Path(__file__).resolve().parent
    backup=root/'backups'/('housing-merge-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json')
    backup.write_text(json.dumps(dict(cards=before,decks=[target,source],tags={str(c['nid']):col.get_note(c['nid']).tags for c in before}),ensure_ascii=False,indent=2)+'\n')
    revlog=col.db.scalar('select count(*) from revlog')
    borrowed=[c['id'] for c in before if c['odid']]
    if borrowed: col.sched.remFromDyn(borrowed)
    for nid in {c['nid'] for c in before}:
        note=col.get_note(nid)
        if 'fr::laf2201::topic::housing' not in note.tags:
            note.tags.append('fr::laf2201::topic::housing');col.update_note(note)
    # Preserve existing random order and preview settings, expanding membership.
    target['terms'][0][0]='tag:fr::laf2201 tag:fr::laf2201::topic::housing'
    target['terms'][0][1]=1000000
    col.decks.save(target)
    col.sched.rebuild_filtered_deck(target['id'])
    eligible=set(col.find_cards(query+' -is:suspended -is:buried'))
    loaded=set(col.find_cards('deck:"LAF2201 Topics::Housing"'))
    if loaded!=eligible: raise RuntimeError(f'Membership check failed; backup: {backup}')
    for old in before:
        c=col.get_card(old['id'])
        assert all(getattr(c,k)==old[k] for k in ('ivl','factor','reps','lapses'))
        assert (c.odid or c.did)==(old['odid'] or old['did'])
        assert (c.odue if c.odid else c.due)==(old['odue'] if old['odid'] else old['due'])
    assert col.db.scalar('select count(*) from revlog')==revlog
    assert not col.find_cards('deck:"LAF2201 Topics::Housing and Furniture"')
    col.decks.remove([source['id']])
    receipt=dict(combined_cards=len(ids),loaded=len(loaded),backup=str(backup))
    (root/'housing-merge-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    mw.reset();mw.moveToState('deckBrowser')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': run()
