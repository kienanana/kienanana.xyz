---
class: software
tags:
  - productivity
  - workflow
source: https://github.com/asmvik/skhd
related:
author:
date: 2026-03-08
updated: 2026-03-08 22:46:12
aliases:
---
skhd is a simple hotkey daemon for macOS. I had heard of this before, but this was explicitly recommended by my boss as he uses it to define keyboard shortcuts to open specific applications. I also mainly use this to control [[yabai]] so it's really useful. 

### Modifier Key Setup
- **Primary modifier**: `fn` (for app launching)
- **Window management**: `alt`, `shift+alt`, `ctrl+alt`
- **Why I chose these**: `fn` is rarely used by system/apps, making it safe for custom shortcuts
## Keybinding Categories
### Application Launcher (fn)

```bash
fn + c → Cursor
fn + s → Slack
fn + m → Spotify
fn + n → Notion
fn + b → Google Chrome
fn + i → iTerm
fn + d → TablePlus
fn + g → Ghostty
fn + a → Claude
fn + v → VS Code
fn + f → Figma
fn + z → Zen
fn + t → Telegram
```

### Window Focus (alt + hjkl)

```bash
alt + j → focus south (down)
alt + k → focus north (up)
alt + h → focus west (left)
alt + l → focus east (right)

# Display focus
alt + s → focus west display
alt + g → focus east display
```

### Layout Manipulation (shift + alt)

```bash
shift + alt + e → balance space (equalize window sizes)
shift + alt + r → rotate layout 270°
shift + alt + y → mirror y-axis (flip vertical)
shift + alt + x → mirror x-axis (flip horizontal)
```

### Window Movement - Swap (shift + alt + hjkl)

```bash
shift + alt + j → swap window south
shift + alt + k → swap window north  
shift + alt + h → swap window west
shift + alt + l → swap window east
```

### Window Modification (shift + alt)

```bash
shift + alt + m → toggle zoom-fullscreen
shift + alt + t → toggle float (with grid positioning)
```

### Window Movement - Warp (ctrl + alt + hjkl)

```bash
ctrl + alt + j → warp window south
ctrl + alt + k → warp window north
ctrl + alt + h → warp window west
ctrl + alt + l → warp window east
```

### Move Between Displays/Spaces (shift + alt)

```bash
# Display movement
shift + alt + s → move window + focus to west display
shift + alt + g → move window + focus to east display

# Space movement
shift + alt + p → move window to previous space
shift + alt + n → move window to next space

# Direct space targeting
shift + alt + 1 → move window to space 1
shift + alt + 2 → move window to space 2
shift + alt + 3 → move window to space 3
shift + alt + 4 → move window to space 4
shift + alt + 5 → move window to space 5
shift + alt + 6 → move window to space 6
shift + alt + 7 → move window to space 7
```

### Window Resizing (shift + alt + wasd)

```bash
shift + alt + a → resize left
shift + alt + d → resize right
shift + alt + w → resize top
shift + alt + s → resize bottom
```

### Yabai Service Control (ctrl + alt)

```bash
ctrl + alt + q → stop yabai
ctrl + alt + s → start yabai
ctrl + alt + r → restart yabai
```






