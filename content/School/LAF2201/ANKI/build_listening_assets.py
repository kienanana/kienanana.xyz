"""Offline build from the read-only Anki snapshot; no collection writes."""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'listening'
DECKS = {
    'housing': 'LAF2201 Listening::Unité 7 - Housing',
    'life_changes': 'LAF2201 Listening::Unité 7 - Life Changes',
    'health': 'LAF2201 Listening::Unité 8 - Health and Wellbeing',
    'technology': 'LAF2201 Listening::Unité 8 - Technology and Communication',
}
TAGS = {
    'housing': ['fr::laf2201::topic::housing', 'fr::laf2201::batch_20261020::housing'],
    'life_changes': ['fr::laf2201::topic::life_changes', 'fr::laf2201::batch_20261020::life_changes', 'fr::laf2201::batch_20261020::abroad'],
    'health': ['fr::laf2201::unit8::health'],
    'technology': ['fr::laf2201::unit8::technology', 'fr::laf2201::unit8::general', 'fr::laf2201::unit8::education'],
}
# Deliberately overlap useful words between topics; each deck can be studied alone.
EXTRAS = {
    'housing': ['un mur', 'un toit'],
    'life_changes': ['une société de déménagement', 'un tarif', 'les tarifs', 'une condition', 'les conditions de déménagement'],
    'health': ['une astuce', 'avant de + infinitive', 'penser à', 'proposer', 'mémoriser'],
    'technology': [],
}
OVERRIDES = {
    'App.': 'un appartement', 'P.': 'une pièce', 'loy.': 'un loyer',
    'ch.': 'une chambre', 'sdb': 'une salle de bains', 'imm.': 'un immeuble',
    'ss. asc.': 'sans ascenseur', 's/cour': 'sur cour', 'rdc.': 'le rez-de-chaussée',
    'dche': 'une douche', 'rft à neuf': 'refait à neuf', 'cuis. éq.': 'une cuisine équipée',
    'gd séj.': 'un grand séjour', 'ds pte rés.': 'dans une petite résidence',
    '2e ét.': 'le deuxième étage', 'Chauf. ind.': 'le chauffage individuel',
    'faire + une mesure': "L'appartement fait cinquante mètres carrés.",
    'faire + measurement': "L'appartement fait cinquante mètres carrés.",
    'chercher à + infinitive': 'Je cherche à louer un appartement.',
    'plus… que': 'Cet appartement est plus grand que le studio.',
    'moins… que': 'Cet appartement est moins cher que la maison.',
    'aussi… que': 'Cet appartement est aussi lumineux que le studio.',
    'plus de… que': "Il y a plus de pièces que dans l'autre appartement.",
    'moins de… que': "Il y a moins de bruit que dans l'autre appartement.",
    'autant de… que': "Il y a autant de chambres que dans l'autre maison.",
    'avoir la chance de + infinitive': "J'ai la chance de vivre à la campagne.",
    'arrêter de + infinitive': "J'ai arrêté de travailler le samedi.",
    'avoir envie de + noun / infinitive': "J'ai envie de changer de vie. J'ai envie de vacances.",
    'Je souhaiterais…': 'Je souhaiterais déménager.',
    "j'aimerais…": "J'aimerais vivre au Canada.",
    'ne… plus': 'Je ne travaille plus en ville.',
    'pour + infinitive': 'Je déménage pour changer de vie.',
    'venir de + infinitive': 'Je viens de déménager.',
    'être en train de + infinitive': 'Je suis en train de monter mes meubles.',
    'avoir mal à la / au / à l\' / aux + partie du corps': "J'ai mal à la tête. J'ai mal au dos. J'ai mal à l'épaule. J'ai mal aux dents.",
    'rester concentré / concentrée': 'rester concentré. rester concentrée.',
    'un / une scientifique': 'un scientifique. une scientifique.',
    'être capable de + infinitive': 'Ce robot est capable de marcher.',
    'sembler + adjective': 'Ce robot semble naturel.',
    'avant de + infinitive': "Éteignez votre écran avant de dormir.",
    'Je pense que…': 'Je pense que cet objet est utile.',
    'Je trouve que…': 'Je trouve que cette invention est pratique.',
    'À mon avis,…': 'À mon avis, ce robot est efficace.',
    'réessayer de + infinitive': 'Je vais réessayer de vous appeler.',
    'Je suis bien au… ? / C\'est bien le… ?': 'Je suis bien au service client ? C\'est bien le service client ?',
    'Pourrais-je parler à… ?': 'Pourrais-je parler à Madame Martin ?',
    'Je voudrais parler à…': 'Je voudrais parler à Madame Martin.',
    'Je vous appelle pour…': 'Je vous appelle pour demander des renseignements.',
    'X est là ?': 'Marie est là ?',
    'Je vous le / la passe.': 'Je vous le passe. Je vous la passe.',
    "Je suis désolé(e), il n'est pas là.": "Je suis désolé, il n'est pas là.",
    'Bon, alors je raccroche…': 'Bon, alors je raccroche.',
}


def plain(value):
    value = re.sub(r'<br\s*/?>', ' ', value, flags=re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', '', value))).strip()


def spoken(value):
    text = plain(value)
    if text in OVERRIDES:
        return OVERRIDES[text]
    text = re.sub(r'\([^)]*\)', '', text)
    text = text.replace('…', '. ').replace(' / ', '. ')
    text = re.sub(r'\s+', ' ', text).strip()
    if '+' in text or re.search(r'\b(infinitive|adjective|measurement|noun)\b', text):
        raise ValueError('Unresolved spoken shorthand: ' + value)
    return text


def build(snapshot):
    notes = json.loads(Path(snapshot).read_text())['result']
    notes = [n for n in notes if n['modelName'] == 'French Vocab']
    by_text = {}
    for n in notes:
        by_text.setdefault(plain(n['fields']['French']['value']), []).append(n)
    rows = []
    for topic, deck in DECKS.items():
        chosen = {n['noteId']: (n, 'Core topic') for n in notes if set(n['tags']) & set(TAGS[topic])}
        for text in EXTRAS[topic]:
            matches = by_text.get(text, [])
            if len(matches) != 1:
                raise ValueError(f'Expected exactly one source for {text!r}: {len(matches)}')
            chosen.setdefault(matches[0]['noteId'], (matches[0], 'Related topic vocabulary'))
        for n in notes:
            tags = set(n['tags'])
            text = plain(n['fields']['French']['value'])
            correspondence = 'fr::laf2201::batch_20261020::correspondence' in tags
            telephone = 'fr::laf2201::batch_20261020::telephone' in tags
            if topic == 'life_changes' and correspondence and text not in ['un mur', 'un toit']:
                chosen.setdefault(n['noteId'], (n, 'Moving: address changes and correspondence'))
            if topic == 'technology' and ((telephone and text not in EXTRAS['life_changes']) or (correspondence and text not in ['un mur', 'un toit', 'un changement d\'adresse', 'la semaine prochaine', 'avoir lieu', 'un service administratif'])):
                chosen.setdefault(n['noteId'], (n, 'Telephone and written communication'))
        for nid, (n, reason) in sorted(chosen.items()):
            fields = {k: v['value'] for k, v in n['fields'].items()}
            speech = spoken(fields['French'])
            digest = hashlib.sha256(('Thomas|175|' + speech).encode()).hexdigest()[:24]
            rows.append(dict(key=f'{topic}:{nid}', topic=topic, deck=deck, source_id=nid,
                             source_fields=fields, source_tags=n['tags'], french=fields['French'],
                             english=fields['English'], notes=fields['Notes'], spoken=speech,
                             audio=f'laf2201_listen_{digest}.wav', reason=reason))
    # All four core topics and every imported Unit 8 entry must be represented.
    covered = {r['source_id'] for r in rows}
    required = {n['noteId'] for n in notes if 'fr::laf2201::unit8' in n['tags'] or any(t in n['tags'] for ts in TAGS.values() for t in ts)}
    assert required <= covered, f'Missing source notes: {required - covered}'
    OUT.mkdir(exist_ok=True)
    (OUT / 'manifest.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    lines = ['# LAF2201 listening coverage', '', 'Built from the live collection on 2026-11-05. All source notes are preserved.', '', 'Each row becomes one independently scheduled listening card. Shared words may appear in more than one topic.', '', '| Topic | Cards |', '| --- | ---: |']
    for topic in DECKS:
        lines.append(f'| {topic} | {sum(r["topic"] == topic for r in rows)} |')
    for topic in DECKS:
        lines += ['', '## ' + DECKS[topic], '', '| French | Spoken audio | Coverage |', '| --- | --- | --- |']
        for r in rows:
            if r['topic'] == topic:
                lines.append('| ' + ' | '.join(plain(str(r[k])).replace('|', '/') for k in ['french', 'spoken', 'reason']) + ' |')
    (OUT / 'coverage.md').write_text('\n'.join(lines) + '\n')
    print({topic: sum(r['topic'] == topic for r in rows) for topic in DECKS})
    print('Unique audio files:', len({r['audio'] for r in rows}))


def generate():
    media = OUT / 'media'
    media.mkdir(exist_ok=True)
    rows = json.loads((OUT / 'manifest.json').read_text())
    jobs = {r['audio']: r['spoken'] for r in rows}
    for i, (filename, text) in enumerate(jobs.items(), 1):
        target = media / filename
        if target.exists() and target.stat().st_size > 500:
            continue
        temporary = Path('/private/tmp') / (filename + '.aiff')
        subprocess.run(['say', '-v', 'Thomas', '-r', '175', '-o', str(temporary), text], check=True)
        subprocess.run(['afconvert', '-f', 'WAVE', '-d', 'LEI16', str(temporary), str(target)], check=True)
        import wave
        with wave.open(str(target)) as audio:
            if audio.getnframes() <= 0:
                raise RuntimeError('Empty speech file; speech synthesis needs access to the Mac voice service: ' + str(target))
        temporary.unlink()
        if i % 25 == 0:
            print(f'Generated {i}/{len(jobs)}', flush=True)
    print('Finished:', len(jobs), 'verified audio files', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == '--audio':
        generate()
    else:
        build(sys.argv[1])
