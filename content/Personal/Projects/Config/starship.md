---
class: software
tags:
  - productivity
  - workflow
source: https://starship.rs/
related:
author:
date: 2026-03-07
updated: 2026-03-07 14:11:53
aliases:
---
Starship is the prompt I'm using for my shell. It displays contextual information about my current directory, git status, programming languages etc. 

![[Screenshot 2026-03-08 at 9.46.36 PM.png]]

## Configuration
### Color Palette
**Theme**: Catppuccin Mocha (`palette = "catppuccin_mocha"`)
- Full color palette defined with all Catppuccin Mocha colors
- Consistent dark theme across the prompt
### Prompt Layout
**Left side** (`format`):
- Shows default modules and the prompt character
**Right side** (`right_format`):
- Git information (branch, status)
- Programming language versions (Go, Python, Node.js, Rust)
- Cloud/infrastructure info (AWS, Kubernetes - though k8s is disabled)
### Styling
- **Prompt character**: ➜ (green on success, red on error)
- **Colors**: Full Catppuccin Mocha palette (rosewater, flamingo, pink, mauve, red, maroon, peach, yellow, green, teal, sky, sapphire, blue, lavender, etc.)
- **Icons**: Nerd Font icons for git, languages, and cloud services