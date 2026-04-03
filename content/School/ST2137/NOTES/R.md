---
class: note
tags:
  - R
source:
related:
author:
date: 2026-03-10
updated: 2026-03-10 15:57:49
aliases:
---
## Useful Functions 
- `.cor(x,y,method="pearson")` 
	- default method = pearson
		- other methods: "spearman" and "kendall"
- `.aggregate(x~y, data=, FUN=summary)`
	- splits data into subsets, computes summary statistics for each, returns result in a convenient form
	- x grouped by y 
		- x: var you want to summarise
		- y: grouping var 
	- `summary` gives Min, Q1, Median, Mean, 3Q, Max
---
Full reference: [[R Glossary]]
