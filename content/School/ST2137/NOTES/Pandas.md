---
class:
tags:
  - python
  - pandas
  - python
  - pandas
source:
related:
author:
date: 2026-03-10
updated: 2026-03-10 10:33:11
aliases:
---
Pandas is a Python library used for data analysis and manipulation. IT provides these useful data structures: **Series (1D)** and **DataFrame (2D)** and has functions for cleaning and manipulating data. 

## Useful Functions 
- df["col"]`.value_counts()`
- df`.iterrows`
	- returns index, data
	- index: label index of the row
	- data: the data of the row as a **Series**
- df`.groupby(by="col")
	- unique val of col, df of entries 
	![[Screenshot 2026-03-10 at 1.25.58 PM.png]]
	- you can take this further and apply y.pts`.sum()` for example
- df`.cumsum()`
	- default: axis = 0 (or 'index' or None)
		- *Vertical* (downwards)
	- axis = 1  = 'columns'
		- *Horizontal* (across)
- logical statement: eg. df['col'] >= 40
	- true/false for each row 	
	- take this further by doing df`[this entire logical statment]`
		- filter df to just the rows that were True 
		- get specific col as **Series** with df`[logic]['col']` 
			- get value from specific row with `.iloc[idx]`
	- if *multiple conditions:*
		- **MUST bracket** each condition 
		- eg. data1`[(data1['color']==2) | (data1['spine']==1)]`
- series`.str.cat(sep=None)`
	- concat using separator. if None, concat all into one long string 
- **.loc** : uses index / column NAMES, **includes endpoint** in slices 
	- supports conditional filtering eg. `df.loc[df['col'] > 2`
	- examples:

- **iloc** : uses integer POSITIONS, **excludes endpoint** 
	- does not directly support boolean indexing in the same way

```python
# first 10 rows:
df.iloc[:10]

# alternate rows from the first 10 rows starting with the first 
df.iloc[::2, :10]

# every alternate rows, and cols A, B, C
df.iloc[::2][['A','B','C']]

# the last 5 rows
df.iloc[-5:]

# all rows in reverse order
df.iloc[::-1]
```

- `pd.to_datetime(df['date'])`
- 
---
Full reference: [[Pandas Glossary]]
