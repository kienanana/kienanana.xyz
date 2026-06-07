#!/usr/bin/env bash
# Sync notes from the Obsidian vault into Quartz's content/ folder.
# Excludes the Private folder and Obsidian/git housekeeping files.
# Pass --dry-run to preview changes without writing anything.
set -euo pipefail

VAULT="$HOME/Documents/VAULT"
CONTENT="$HOME/Documents/quartz/content"

rsync -av --delete \
  --exclude 'Private' \
  --exclude '.obsidian' \
  --exclude '.smart-env' \
  --exclude '.claude' \
  --exclude '.git' \
  --exclude '.gitignore' \
  --exclude 'templater' \
  --exclude 'index.md' \
  "$@" \
  "$VAULT/" "$CONTENT/"
