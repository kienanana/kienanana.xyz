---
class: note
tags:
  - python
  - R
source:
related:
author:
date: 2026-03-09
updated: 2026-03-09 22:39:45
aliases:
---
## Common Python Mistakes 

```python
# WRONG - trying to index with a list 
x_list[[0,2]] 
# error: "list indices must be integers or slices, not list"
```

- Solution: use numpy or pandas for advanced indexing 

```python
# Tuple Immutability 
x_tuple[0] = 10
# error: "'tuple' object does not support item assignment"
```

## Common R Mistakes

#### `which.max` with ties:
- returns only FIRST index with max value 
- for all ties, use `which(x == max(x))`

#### useful thing about factors:
- converting to factor BEFORE summary() gives frequency table 
- without factor: gives 5 number summary 


## Python Stuff
#### :LiLightbulb: enumerate() Usage:

```python
for idx, (key, val) in enumerate(dict.items()): 
	print(f"{idx+1}. The gender of {key} is {val}")
```

#### :LiLightbulb: Advanced F-strings Formatting:
- `{x:2d}` : pad integer to 2 characters
- `{x**2:2d}` : evaluate expression, then format 
- `{x:0.2f}` : float with 2 decimal places 

