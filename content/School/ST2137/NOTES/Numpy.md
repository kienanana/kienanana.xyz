---
class: software
tags:
  - y3s2
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
- np`.linspace(start, stop, n)`
	- returns n evenly spaced values, **inclusive** of both endpoints
	- use for generating x-ranges for prediction plots
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
- np`.zeros(n)` / np`.ones(n)` — initialise result arrays for simulation loops
- np`.sqrt(x)`, np`.floor(x)`, np`.exp(x)` — element-wise math on arrays
- np`.sum(arr)` / np`.sum(c**2 / n_vals)` — used in contrast SE calculations

## Random Number Generation (L10)
```python
# Modern API — preferred for reproducibility
rng = np.random.default_rng(seed=2137)

# Pass rng into scipy .rvs() calls:
from scipy.stats import norm, gamma, poisson, binom

X = norm.rvs(0, 1, size=100, random_state=rng)
X = gamma.rvs(2, scale=3, size=50, random_state=rng)
X = poisson.rvs(1.3, size=50, random_state=rng)
X = binom.rvs(2, 0.3, size=50, random_state=rng)
```
- Always set seed **before** the simulation loop for reproducibility
- `rng` is passed as `random_state=rng` to scipy distribution `.rvs()`

## Simulation Pattern (L10)
```python
rng = np.random.default_rng(2137)
output_vec = np.zeros(100)          # pre-allocate result array
n = 20
lambda_ = 0.5

for i in range(100):
    X = poisson.rvs(0.5, size=n, random_state=rng)
    Xbar = X.mean()
    s = X.std()
    t = norm.ppf(0.975)
    CI = [Xbar - t*s/np.sqrt(n), Xbar + t*s/np.sqrt(n)]
    if CI[0] < lambda_ and CI[1] > lambda_:
        output_vec[i] = 1
output_vec.mean()                   # estimated coverage
```

---
Full reference: [[Numpy Glossary]]
