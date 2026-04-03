---
class: software
tags:
  - productivity
  - workflow
source: https://github.com/tmux/tmux/wiki
related:
author:
date: 2026-03-08
updated: 2026-03-08 21:48:00
aliases:
---
tmux is a terminal multiplexer that lets me manage multiple terminal sessions, split windows into panes, and keep sessions running in the background. really cool stuff. 

![[Screenshot 2026-03-08 at 9.54.59 PM.png]]

## Configuration
### Prefix Key
- **Current**: `C-a` (Ctrl + a)
- **Default**: `C-b` (unbind in config)
	- i changed this because it's easier to reach
### Plugin Manager (TPM)
**Installed plugins**:
- **tmux-sensible**: Sensible default settings for tmux
- **vim-tmux-navigator**: Seamless navigation between vim splits and tmux panes
- **tmux2k**: Modern theme with powerline support
- **tpm**: Plugin manager itself

**Installing plugins on new machine**:
- prefix + I (Ctrl+a, then Shift+i) (( within tmux ))
### Theme Configuration (tmux2k)
- **Style**: Powerline
- **Status bar behavior**:
    - Hidden when nvim is active (via hooks)
    - Shows when other programs are running
### Window Management
- **New window**: `prefix + c`
- **Switch windows**: `prefix + n/p` (next/previous) or `prefix + [number]`
- **Rename window**: `prefix + ,`
- **Close window**: `prefix + &`
### Pane Management
- **Split horizontal**: `prefix + "`
- **Split vertical**: `prefix + %`
- **Navigate panes**: `C-h/j/k/l` (via vim-tmux-navigator)
- **Resize panes**: `prefix + [arrow keys]`
- **Close pane**: `prefix + x`
### Session Management
- **New session**: `tmux new -s [name]`
- **List sessions**: `tmux ls` or `prefix + s`
- **Attach session**: `tmux attach -t [name]`
- **Detach session**: `prefix + d`
- **Switch sessions**: `prefix + s` (interactive)