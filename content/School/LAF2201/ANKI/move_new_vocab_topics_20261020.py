"""Move the imported filtered decks by renaming; preserve deck/card identities."""
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = 'LAF2201 New Vocab 2026-10-20'
NEW = 'LAF2201 Topics'

def call(action, **params):
    request = urllib.request.Request('http://127.0.0.1:8765', json.dumps(dict(action=action,version=6,params=params)).encode(), {'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=30) as response: result=json.load(response)
    if result.get('error'): raise RuntimeError(result['error'])
    return result['result']

def rename(name, target):
    request = urllib.request.Request('http://127.0.0.1:8765/api/v1', json.dumps(dict(jsonrpc='2.0',id=1,method='decks.update',params=dict(deck={'name':name},name=target))).encode(), {'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=30) as response: result=json.load(response)
    if result.get('error'): raise RuntimeError(result['error'])
    return result['result']

def main():
    decks=call('deckNamesAndIds')
    moves={name: NEW+'::'+('Daily Routines - Additional Vocabulary' if name.split('::')[-1]=='Daily Routines' else name.split('::')[-1]) for name in decks if name.startswith(OLD+'::')}
    for name,target in moves.items():
        if target in decks: raise RuntimeError('Target exists: '+target)
    ids=call('findCards',query='tag:fr::laf2201::added_20261020')
    before=call('cardsInfo',cards=ids)
    if moves: (ROOT/'backups/topic-move-20261020.json').write_text(json.dumps(dict(decks=decks,cards=before,moves=moves),ensure_ascii=False,indent=2)+'\n')
    for name,target in moves.items():
        rename(name,target)
    after_decks=call('deckNamesAndIds')
    for name,target in moves.items():
        assert after_decks[target]==decks[name], target
        assert name not in after_decks
    after=call('cardsInfo',cards=ids)
    keys=('cardId','note','type','queue','due','interval','factor','reps','lapses','left')
    old_by_id={c['cardId']:c for c in before}
    for card in after:
        assert all(card.get(k)==old_by_id[card['cardId']].get(k) for k in keys),card['cardId']
    # The former parent can be removed only once it has no children or cards.
    if OLD in after_decks:
        assert not any(n.startswith(OLD+'::') for n in after_decks)
        assert not call('findCards',query='deck:"'+OLD+'"')
        call('deleteDecks',decks=[OLD],cardsToo=True)
    call('guiDeckBrowser')
    receipt=dict(moved=moves,verified_cards=len(ids),decks=call('deckNames'))
    (ROOT/'topic-move-20261020-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
