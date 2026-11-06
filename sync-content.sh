#!/usr/bin/env bash
# Sync notes from the Obsidian vault into Quartz's content/ folder.
# Excludes private notes, generated work files, and tool housekeeping.
# Pass --dry-run to preview changes without writing anything.
set -euo pipefail

VAULT="$HOME/Documents/VAULT"
CONTENT="$HOME/Documents/quartz/content"

rsync -av --delete \
  --exclude 'Private' \
  --exclude 'output' \
  --exclude 'ANKI' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude '.codex' \
  --exclude '.agents' \
  --exclude '.obsidian' \
  --exclude '.smart-env' \
  --exclude '.claude' \
  --exclude '.git' \
  --exclude '.gitignore' \
  --exclude 'templater' \
  --exclude 'index.md' \
  "$@" \
  "$VAULT/" "$CONTENT/"
