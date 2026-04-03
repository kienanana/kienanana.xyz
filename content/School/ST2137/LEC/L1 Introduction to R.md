---
class: note
tags:
  - R
source:
related:
author:
date: 2026-03-09
updated: 2026-03-09 16:29:06
aliases:
---
## stuff not in lec notes:
### Data Exploration Best Practices
1. open in text editor to inspect
2. check for:
	- comments at beginning or end
	- column separators (tabs, semicolons, commas)
	- special missing value codes
	- expected number of rows 

eg. crab.txt has 174 lines, expect 173 rows (minus header), verify with nrow(data) == 173

### Reading FIve-Number Summary
- distance Q1 to median
- distance median to Q3
	- if equal: symmetric in the middle
- distance min to Q1 
- distance Q3 to max
	- if unequal: skewed outside the middle 
:LiLightbulb: if mean smaller than median -> skewed left

