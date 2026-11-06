"""Import the curated L7/TUT 5–6 vocabulary; --apply writes to local Anki."""
from pathlib import Path
import argparse,importlib.util,json
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('french','/Users/kienanana/Documents/obsidian-scripts/french.py')
french=importlib.util.module_from_spec(spec);spec.loader.exec_module(french)
base_build=french.build_note

def build(entry):
    note=base_build(entry)
    note['tags'] += ['fr::laf2201::topic::'+entry['topic'],'fr::laf2201::unit7_important']
    return note

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    entries=json.loads((ROOT/'new-vocab-20261013.json').read_text())
    french.build_note=build
    french.sync(entries,dry_run=not args.apply,push=False,report=ROOT/'new-vocab-import-plan.json')
