---
class: software
tags:
  - python
  - numpy
source:
related:
author:
date: 2026-03-10
updated: 2026-03-10 10:32:47
aliases:
---
Numpy is a Python library used for working with arrays. It also has functions for linear algebra, fourier transform, and matrices. Numpy serves to provide an array object that is way faster to process than the traditional Python lists.


## Useful Functions 
- np`.arange(start,stop,step)`
	- exclusive of stop
	- returns ndarray of evenly spaced values 
- np`.where(condition, x, y)`
	- where condition true, yield x, otherwise yield y

```python
np.where([[True, False], [True, True]],
         [[1, 2], [3, 4]],
         [[9, 8], [7, 6]])
# array([[1, 8],
#       [3, 4]])

df_liverpool_2223["result"] = np.where(
	df_liverpool_2223.GF > df_liverpool_2223.GA, 'W',
	    np.where(df_liverpool_2223.GF < df_liverpool_2223.GA, 'L', 
	        np.where(df_liverpool_2223.GF == df_liverpool_2223.GA, 'D', ''))) 

df_liverpool_2223["pts"] = np.where(df_liverpool_2223.result == 'W', 3, 
                            np.where(df_liverpool_2223.result == 'D', 1, 0))
```

- np`.quantile(a, q)`
	- a: array, q: quantile
	- useful for getting **IQR** 