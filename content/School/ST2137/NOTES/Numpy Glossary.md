---
class: note
tags:
  - y3s2
  - python
  - numpy
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 03:25:32
aliases:
---
> Quick reference: [[Numpy]]
## QUICK REFERENCE CARD

### Most Used Functions


```python
# Creation
np.array(), np.arange(), np.zeros(), np.ones(), np.repeat()

# Shape & Reshape
arr.shape, arr.reshape(), arr.T, arr.flatten()

# Indexing
arr[i], arr[i:j], arr[mask], arr[row, col]

# Math
np.mean(), np.sum(), np.std(), np.min(), np.max()

# Conditionals
np.where(), arr > 5, arr[arr > 5]

# Manipulation
np.concatenate(), np.concat(), np.vstack(), np.hstack(), np.outer()

# Random
np.random.rand(), np.random.randn(), np.random.randint()

# Statistics
np.mean(), np.median(), np.std(), np.quantile()

# Linear Algebra
arr @ arr2, np.dot(), np.outer(), np.trace(), np.linalg.inv()

# Categorical Analysis (from Assignment)
np.outer(), np.trace(), np.sum(w * matrix)
```

---
## IMPORTING


```python
import numpy as np
```

---

## CREATING ARRAYS

### From Lists


```python
np.array([1, 2, 3])                    # 1D array
np.array([[1,2], [3,4]])               # 2D array
np.array([1, 2, 3], dtype=float)       # specify data type
```

### Sequences


```python
np.arange(start, stop, step)           # like range(), exclusive of stop
np.arange(0, 10, 2)                    # 0, 2, 4, 6, 8
np.arange(10)                          # 0, 1, 2, ..., 9
np.linspace(0, 10, 5)                  # 5 evenly spaced: 0, 2.5, 5, 7.5, 10
np.linspace(0, 1, 100)                 # 100 points from 0 to 1
```

### Special Arrays


```python
np.zeros(5)                            # [0, 0, 0, 0, 0]
np.zeros((3, 4))                       # 3x4 array of zeros
np.ones(5)                             # [1, 1, 1, 1, 1]
np.ones((2, 3))                        # 2x3 array of ones
np.eye(3)                              # 3x3 identity matrix
np.empty(5)                            # uninitialized array (random values)
np.full(5, 7)                          # [7, 7, 7, 7, 7]
np.full((2, 3), 7)                     # 2x3 array filled with 7
```

### Random Arrays


```python
np.random.rand(5)                      # 5 random values [0, 1)
np.random.rand(3, 4)                   # 3x4 random values [0, 1)
np.random.randn(5)                     # 5 values from standard normal
np.random.randint(0, 10, 5)            # 5 random integers [0, 10)
np.random.uniform(0, 1, 5)             # 5 uniform random [0, 1)
```

---

## ARRAY PROPERTIES


```python
arr.shape                              # dimensions tuple (rows, cols, ...)
arr.ndim                               # number of dimensions
arr.size                               # total number of elements
arr.dtype                              # data type of elements
arr.itemsize                           # size of each element in bytes
```

**Examples:**


```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape       # (2, 3)
arr.ndim        # 2
arr.size        # 6
arr.dtype       # dtype('int64')
```

---

## RESHAPING ARRAYS

### Basic Reshaping


```python
arr.reshape(rows, cols)                # reshape to new dimensions
arr.reshape(2, 3)                      # 2 rows, 3 columns
arr.flatten()                          # flatten to 1D (copy)
arr.ravel()                            # flatten to 1D (view if possible)
arr.T                                  # transpose
```

### The -1 Trick (AUTO-CALCULATE DIMENSION)

**The Rule:** `-1` means "calculate this dimension automatically based on the total number of elements and other dimensions"


```python
# Example: 6 elements
arr = np.array([1, 2, 3, 4, 5, 6])

# Make column vector (6 rows, 1 column)
arr.reshape(-1, 1)                     # "I want 1 column, you figure out rows"
# [[1], [2], [3], [4], [5], [6]]

# Make row vector (1 row, 6 columns)  
arr.reshape(1, -1)                     # "I want 1 row, you figure out columns"
# [[1, 2, 3, 4, 5, 6]]

# Make 2x3 matrix
arr.reshape(2, -1)                     # "I want 2 rows, you calculate columns"
# [[1, 2, 3], [4, 5, 6]]

arr.reshape(-1, 3)                     # "I want 3 columns, you calculate rows"
# [[1, 2, 3], [4, 5, 6]]

# Flatten to 1D
arr.reshape(-1)                        # [1, 2, 3, 4, 5, 6]
```

**Why use -1?**

- Works with any array size (dynamic/reusable code)
- Avoids mental math errors
- Clear intent: "I care about this dimension, calculate the other"

**Common patterns:**


```python
arr.reshape(-1, 1)     # Column vector (for scikit-learn, plotting)
arr.reshape(1, -1)     # Row vector
arr.reshape(-1)        # Flatten to 1D
```

**Lecture quote:** "Reshape with -1 auto-calculates dimension"

---

## INDEXING & SLICING

### Basic Indexing (0-based!)


```python
arr[0]                                 # first element
arr[-1]                                # LAST element (different from R!)
arr[1:4]                               # elements at indices 1, 2, 3 (excludes 4)
arr[::2]                               # every 2nd element
arr[::-1]                              # reverse array
```

### 2D Indexing


```python
arr[row, col]                          # single element
arr[0, :]                              # first row (all columns)
arr[:, 0]                              # first column (all rows)
arr[1:3, 0:2]                          # subarray: rows 1-2, cols 0-1
arr[0]                                 # same as arr[0, :] (first row)
```

### Fancy Indexing


```python
arr[[0, 2, 4]]                         # elements at indices 0, 2, 4
arr[[0, 2], [1, 3]]                    # elements at (0,1) and (2,3)
```

### Boolean Indexing


```python
arr[arr > 5]                           # elements greater than 5
arr[(arr > 5) & (arr < 10)]            # AND condition (use &)
arr[(arr < 3) | (arr > 7)]             # OR condition (use |)
arr[~(arr > 5)]                        # NOT condition (use ~)
```

**Important:** Use `&`, `|`, `~` for element-wise operations, NOT `and`, `or`, `not`

---

## ARRAY OPERATIONS

### Arithmetic Operations (Element-wise)


```python
arr + 5                                # add scalar to all elements
arr - 3                                # subtract scalar
arr * 2                                # multiply by scalar
arr / 2                                # divide by scalar
arr ** 2                               # square all elements
arr % 2                                # modulo
arr // 2                               # integer division

# Between arrays (same shape)
arr1 + arr2                            # element-wise addition
arr1 - arr2                            # element-wise subtraction
arr1 * arr2                            # element-wise multiplication
arr1 / arr2                            # element-wise division
```

### Mathematical Functions


```python
np.exp(arr)                            # e^x for each element
np.log(arr)                            # natural log
np.log10(arr)                          # log base 10
np.sqrt(arr)                           # square root
np.abs(arr)                            # absolute value
np.sin(arr), np.cos(arr), np.tan(arr) # trigonometric
np.round(arr, decimals=2)              # round to 2 decimals
np.floor(arr), np.ceil(arr)            # floor and ceiling
```

---

## MATRIX OPERATIONS

### Matrix Multiplication


```python
arr1 @ arr2                            # matrix multiplication (Python 3.5+)
np.dot(arr1, arr2)                     # matrix multiplication
np.matmul(arr1, arr2)                  # matrix multiplication
```

### Linear Algebra


```python
np.linalg.inv(matrix)                  # matrix inverse
np.linalg.det(matrix)                  # determinant
np.linalg.eig(matrix)                  # eigenvalues and eigenvectors
np.linalg.solve(A, b)                  # solve Ax = b
np.trace(matrix)                       # trace (sum of diagonal)
np.transpose(arr)                      # transpose (same as arr.T)
```

**Additional matrix operations:**


```python
# Outer product (important for expected counts!)
np.outer(a, b)                         # outer product of vectors a and b
# Result: matrix where element [i,j] = a[i] * b[j]

# Example from Assignment: Expected counts under independence
row_margins = [0.5, 0.5]               # row probabilities
col_margins = [0.6, 0.4]               # column probabilities
expected = n * np.outer(row_margins, col_margins)
# [[0.5*0.6*n, 0.5*0.4*n],
#  [0.5*0.6*n, 0.5*0.4*n]]

# Trace (sum of diagonal) - for agreement measures
matrix = np.array([[10, 2], [3, 15]])
np.trace(matrix)                       # 10 + 15 = 25
# Used in Cohen's Kappa: observed agreement = trace(prob_matrix)
```

**Example from Tutorial 1:**


```python
# Least squares: beta_hat = (X^T X)^-1 X^T y
X = np.column_stack([np.ones(n), x_values])  # design matrix
y = y_values.reshape(-1, 1)
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y
```

---

## STATISTICAL FUNCTIONS

### Descriptive Statistics


```python
np.mean(arr)                           # mean (average)
np.median(arr)                         # median
np.std(arr)                            # standard deviation
np.var(arr)                            # variance
np.min(arr), np.max(arr)               # minimum, maximum
np.sum(arr)                            # sum of all elements
np.prod(arr)                           # product of all elements

# With axis parameter
np.mean(arr, axis=0)                   # mean of each column
np.mean(arr, axis=1)                   # mean of each row
np.sum(arr, axis=0)                    # sum of each column
```

### Quantiles


```python
np.quantile(arr, 0.5)                  # median (50th percentile)
np.quantile(arr, [0.25, 0.75])         # Q1, Q3
np.percentile(arr, [25, 50, 75])       # same as quantile with %
```

### Finding Elements


```python
np.argmin(arr)                         # index of minimum
np.argmax(arr)                         # index of maximum
np.where(arr == arr.max())             # ALL indices where value is max
np.where(arr > 5)                      # indices where condition is True
```

**Lecture note:** `which.max()` in R returns only FIRST index on ties; use `np.where()` for all

---

## CONDITIONAL OPERATIONS

### np.where() - THE WORKHORSE


```python
np.where(condition, value_if_true, value_if_false)
```

**Basic example:**


```python
arr = np.array([1, 5, 10, 15, 20])
np.where(arr > 10, 'high', 'low')
# array(['low', 'low', 'low', 'high', 'high'])
```

**Nested np.where() - Multiple conditions:**


```python
# From Tutorial 2: Classify game results
result = np.where(df.GF > df.GA, 'W',           # if GF > GA: Win
             np.where(df.GF < df.GA, 'L',       # else if GF < GA: Loss
                 np.where(df.GF == df.GA, 'D', '')))  # else if equal: Draw

# Points based on result
pts = np.where(result == 'W', 3,                # Win = 3 points
          np.where(result == 'D', 1, 0))        # Draw = 1, Loss = 0
```

**2D array example:**


```python
np.where([[True, False], [True, True]],
         [[1, 2], [3, 4]],              # values if True
         [[9, 8], [7, 6]])              # values if False
# Returns: array([[1, 8], [3, 4]])
```

**Get indices where condition is True:**


```python
indices = np.where(arr > 10)            # returns tuple of arrays
arr[indices]                            # extract those elements
```

---

## ARRAY MANIPULATION

### Stacking & Concatenation


```python
np.concatenate([arr1, arr2])           # concatenate along axis 0
np.concatenate([arr1, arr2], axis=1)   # concatenate along axis 1
np.concat([arr1, arr2])                # alias for concatenate (NumPy 2.0+)
np.vstack([arr1, arr2])                # stack vertically (rows)
np.hstack([arr1, arr2])                # stack horizontally (columns)
np.column_stack([arr1, arr2])          # stack 1D arrays as columns
```

**Example:**


```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.vstack([a, b])                      # [[1,2,3], [4,5,6]]
np.hstack([a, b])                      # [1,2,3,4,5,6]
np.column_stack([a, b])                # [[1,4], [2,5], [3,6]]
```

**From Assignment:**


```python
# Concatenate arrays with different values
rater_A = np.concat([np.repeat(1, 120), np.repeat(2, 5)])
# Result: 120 ones followed by 5 twos
```

### Splitting


```python
np.split(arr, sections)                # split into equal sections
np.array_split(arr, sections)          # split (allows unequal)
np.hsplit(arr, sections)               # split horizontally (columns)
np.vsplit(arr, sections)               # split vertically (rows)
```

### Adding/Removing Elements


```python
np.append(arr, values)                 # append values to end
np.insert(arr, index, values)          # insert at index
np.delete(arr, index)                  # delete at index
```

### Applying Functions Along an Axis


```python
# np.apply_along_axis — apply a 1D function along a chosen axis
np.apply_along_axis(func, axis, arr)

# axis=0: apply func to each COLUMN (function receives one column at a time)
# axis=1: apply func to each ROW (function receives one row at a time)

# Examples:
np.apply_along_axis(np.mean, axis=0, arr=matrix)      # column means
np.apply_along_axis(np.mean, axis=1, arr=matrix)      # row means

# With custom lambda (e.g. trimmed mean for each column)
from scipy import stats
np.apply_along_axis(lambda x: stats.trim_mean(x, 0.1), axis=0, arr=matrix)
```

### Creating Arrays Like Another


```python
np.zeros_like(arr)                     # zero array with same shape & dtype
np.zeros_like(arr, dtype=float)        # same shape, force float dtype
np.ones_like(arr)                      # ones array with same shape & dtype
```

### Repeating


```python
np.repeat(arr, repeats)                # repeat each element
np.repeat([1, 2], 3)                   # [1, 1, 1, 2, 2, 2]
np.repeat(1, 120)                      # repeat single value: [1, 1, 1, ...]
np.tile(arr, reps)                     # tile entire array
np.tile([1, 2], 3)                     # [1, 2, 1, 2, 1, 2]
```

**From Tutorial 3:**


```python
# Repeat labels for reshaping data
grade_type = np.repeat(['first', 'second', 'final'], repeats=395)
# Creates 1185 labels (395 of each)
```

**From Assignment:**


```python
# Create repeated data for categorical analysis
rater_A = np.concat([np.repeat(1, 120), np.repeat(2, 5)])
# Creates: [1, 1, ...(120 times), 2, 2, 2, 2, 2]
```

---

## SORTING & SEARCHING

### Sorting


```python
np.sort(arr)                           # return sorted copy
arr.sort()                             # sort in place
np.argsort(arr)                        # indices that would sort array
np.sort(arr)[::-1]                     # sort descending
```

**Example:**


```python
arr = np.array([3, 1, 2])
np.sort(arr)                           # [1, 2, 3]
np.argsort(arr)                        # [1, 2, 0] - indices for sorting
```

### Searching


```python
np.argmin(arr)                         # index of minimum
np.argmax(arr)                         # index of maximum
np.where(condition)                    # indices where True
np.searchsorted(sorted_arr, value)     # index to insert value
```

---

## RANDOM NUMBER GENERATION

### New-Style RNG (Preferred)

**Use `np.random.default_rng()` instead of `np.random.seed()` in modern NumPy:**


```python
rng = np.random.default_rng(42)        # create RNG with seed

# Generation methods (same distributions as legacy, new API)
rng.normal(loc=0, scale=1, size=100)   # normal
rng.uniform(low=0, high=1, size=100)   # uniform
rng.integers(0, 10, size=5)            # integers [0, 10)
rng.choice(arr, size=10)               # sample from array
rng.choice(arr, size=10, replace=False) # without replacement

# Passing rng to scipy functions
from scipy.stats import bootstrap
res = bootstrap((data,), np.mean, random_state=rng)
```

**Why prefer this?** Each `default_rng()` instance is independent — avoids shared global state; safer in loops and simulations.

### Legacy API (Still Works)


```python
np.random.seed(42)                     # set global seed for reproducibility
```

### Legacy Random Sampling


```python
np.random.rand(5)                      # 5 uniform [0, 1)
np.random.randn(5)                     # 5 standard normal
np.random.randint(0, 10, 5)            # 5 integers [0, 10)
np.random.uniform(low, high, size)     # uniform in range
np.random.normal(mean, std, size)      # normal distribution
np.random.choice(arr, size)            # random sample from array
np.random.choice(arr, size, replace=False)  # without replacement
```

**Jittering (from Tutorial 3):**


```python
# Add small random noise to avoid overplotting
jittered = arr + np.random.uniform(-0.2, 0.2, size=len(arr))
```

---

## SPECIAL MATHEMATICAL FUNCTIONS

### Logarithms & Exponentials


```python
np.exp(arr)                            # e^x
np.log(arr)                            # natural log
np.log10(arr)                          # log base 10
np.log2(arr)                           # log base 2
```

### Factorial (from Tutorial 3)


```python
from scipy.special import gammaln
gammaln(n + 1)                         # log(n!)
# Used in Poisson-ness plot: phi = gammaln(k + 1) + np.log(Xk/N)
```

---

## BROADCASTING

**Broadcasting:** NumPy's way of operating on arrays of different shapes

**Rules:**

1. If arrays have different numbers of dimensions, pad smaller shape with 1s on the left
2. Arrays are compatible if dimensions are equal OR one is 1
3. After broadcasting, each array behaves as if it had shape equal to element-wise max

**Examples:**


```python
# Scalar broadcasting
arr = np.array([1, 2, 3])
arr + 5                                # [6, 7, 8] - 5 broadcasts to [5,5,5]

# 1D to 2D broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])            # shape (2, 3)
row = np.array([10, 20, 30])           # shape (3,)
arr + row                              # row broadcasts to each row of arr

# Column broadcasting (need reshape!)
col = np.array([10, 20]).reshape(-1, 1)  # shape (2, 1)
arr + col                              # col broadcasts to each column
```

**From Tutorial 4 (important!):**


```python
# Dividing by row sums to get proportions
table = np.array([[47, 41], [166, 141]])
row_sums = table.sum(axis=1).reshape(-1, 1)  # MUST reshape to (2,1)
proportions = table / row_sums         # broadcasts correctly
```

---

## SAVING & LOADING


```python
np.save('array.npy', arr)              # save single array
arr = np.load('array.npy')             # load single array

np.savez('arrays.npz', a=arr1, b=arr2) # save multiple arrays
data = np.load('arrays.npz')           # load multiple
arr1 = data['a']
arr2 = data['b']

np.savetxt('data.txt', arr)            # save as text
arr = np.loadtxt('data.txt')           # load from text
```

---

## HISTOGRAM FUNCTIONS


```python
counts, bins = np.histogram(data, bins=10)
# Returns:
# - counts: frequency in each bin
# - bins: bin edges (length = n_bins + 1)

counts, bins = np.histogram(data, bins=[0, 10, 20, 30])  # custom bins
```

**Important notes:**

- NumPy histograms are **left-closed, right-open** [a, b)
- Last bin is **closed on both ends** [a, b]
- This is **different from R** which is right-closed (a, b]

**From lectures:** "Python histogram convention (left-closed) differs from R (right-closed) — be careful when reproducing analyses"

---

## MASKING & FILTERING


```python
# Create boolean mask
mask = arr > 5

# Apply mask
filtered = arr[mask]

# Modify using mask
arr[mask] = 0                          # set all values > 5 to 0

# Count True values
np.sum(mask)                           # or mask.sum()

# Check if any/all
np.any(mask)                           # True if at least one True
np.all(mask)                           # True if all True
```

---

## USEFUL TRICKS FROM LECTURES

### Negative Indexing Difference


```python
# Python: negative index means "from end"
arr = np.array([10, 20, 30, 40, 50])
arr[-1]                                # 50 (LAST element)
arr[-2]                                # 40 (second to last)

# R: negative index means "drop element"  
# Be careful when translating code!
```

**Lecture quote:** "Negative indexing: Python (-1 = last element) vs R (-1 = drop element) — critical difference"

### Slice Endpoint


```python
arr[1:4]                               # indices 1, 2, 3 (EXCLUDES 4)
# This is standard Python behavior
# BUT: pandas .loc INCLUDES endpoint (inconsistency!)
```

**Lecture quote:** "Slice endpoint: excluded in standard Python, but INCLUDED in pandas .loc (inconsistency explicitly warned)"

---

## COMMON PATTERNS

### Creating Design Matrix (for regression)


```python
# Add column of ones for intercept
X = np.column_stack([np.ones(n), x_values])
# or
X = np.c_[np.ones(n), x_values]
```

### Computing Pairwise Operations


```python
# From Tutorial 1: compute all pairwise slopes
from itertools import combinations
pairs = list(combinations(range(n), 2))
slopes = [(y[j]-y[i])/(x[j]-x[i]) for i, j in pairs]
robust_slope = np.median(slopes)
```

### Conditional Cumulative Sum


```python
# Cumulative sum
np.cumsum(arr)

# Cumulative sum with condition
cumsum = np.cumsum(arr > threshold)
```

---

## IMPORTANT CONCEPTS

### Array vs List

**Use arrays when:**

- Need mathematical operations
- Working with numerical data
- Performance matters
- Need multi-dimensional data

**Use lists when:**

- Mixed data types
- Growing/shrinking frequently
- Simple operations

### Views vs Copies


```python
view = arr[1:5]                        # creates view (shares memory)
view[0] = 999                          # MODIFIES original arr!

copy = arr[1:5].copy()                 # creates copy (independent)
copy[0] = 999                          # does NOT modify arr
```

**Rule:** Basic slicing creates views; fancy indexing creates copies

### Memory Order

NumPy stores arrays in **row-major order (C-style)** by default

- Elements in same row are contiguous in memory
- This affects performance of row vs column operations

---

## DEBUGGING TIPS


```python
# Check array properties
arr.shape                              # dimensions
arr.dtype                              # data type
arr.size                               # total elements

# Identify issues
np.isnan(arr).any()                    # check for NaN
np.isinf(arr).any()                    # check for infinity
np.isfinite(arr).all()                 # check all finite

# Print with formatting
np.set_printoptions(precision=2)       # 2 decimal places
np.set_printoptions(suppress=True)     # suppress scientific notation
```

---

## COMMON MISTAKES

❌ **Using wrong operators for arrays**


```python
# WRONG
arr1 and arr2                          # only checks first element
arr1 or arr2                           # only checks first element

# CORRECT
arr1 & arr2                            # element-wise AND
arr1 | arr2                            # element-wise OR
```

❌ **Forgetting to reshape for broadcasting**


```python
# WRONG
arr / arr.sum(axis=1)                  # wrong shape!

# CORRECT
arr / arr.sum(axis=1).reshape(-1, 1)   # reshapes to column
```

❌ **Confusing attributes and methods**


```python
# WRONG
arr.shape()                            # shape is attribute!

# CORRECT
arr.shape                              # no parentheses
arr.reshape(2, 3)                      # reshape is method
```

❌ **Modifying view unintentionally**


```python
# WRONG (if you want copy)
subset = arr[1:5]
subset[0] = 999                        # modifies original!

# CORRECT
subset = arr[1:5].copy()
subset[0] = 999                        # safe
```

---

## CATEGORICAL DATA ANALYSIS PATTERNS

### Computing Pearson Residuals


```python
# From Assignment: Pearson residuals for contingency tables
# Residual = (observed - expected) / sqrt(expected)

# Given contingency table
n_ij = tab.values                      # observed counts
n = n_ij.sum()                         # total

# Marginal probabilities
pi_i_plus = n_ij.sum(axis=1) / n       # row marginals
pi_plus_j = n_ij.sum(axis=0) / n       # column marginals

# Expected counts under independence using outer product
mu_ij = n * np.outer(pi_i_plus, pi_plus_j)

# Pearson residuals
r = (n_ij - mu_ij) / np.sqrt(mu_ij)
```

**Interpretation:**

- Large positive residuals: more observations than expected
- Large negative residuals: fewer observations than expected
- For agreement: large positive on diagonal, negative off-diagonal

### Cohen's Kappa (Agreement Measure)


```python
# Measure of inter-rater agreement
# κ = (observed_agreement - expected_agreement) / (1 - expected_agreement)

# Joint probabilities
pi_ij = n_ij / n

# Observed agreement (diagonal sum)
observed_agreement = np.trace(pi_ij)

# Expected agreement under independence
expected_agreement = np.sum(pi_i_plus * pi_plus_j)

# Cohen's Kappa
kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
```

**Range:** -1 to 1

- κ = 1: perfect agreement
- κ = 0: agreement by chance
- κ < 0: worse than chance

### Weighted Kappa (Ordinal Agreement)


```python
# For ordered categories, penalize disagreements by distance
I = 4  # number of categories

# Create weight matrix: w_ij = 1 - |i-j|/(I-1)
w = np.zeros((I, I))
for i in range(I):
    for j in range(I):
        w[i, j] = 1 - abs(i - j) / (I - 1)

# Weighted observed agreement
weighted_observed = np.sum(w * pi_ij)

# Weighted expected agreement  
weighted_expected = np.sum(w * np.outer(pi_i_plus, pi_plus_j))

# Weighted Kappa
kappa_w = (weighted_observed - weighted_expected) / (1 - weighted_expected)
```

**Key insight:** Weighted kappa is more lenient, gives credit for "near agreement"

---
## KEY TAKEAWAYS FROM LECTURES

- "Reshape with -1 auto-calculates dimension"
- "Python (-1 = last element) vs R (-1 = drop element) — critical difference"
- ".shape is attribute (no parentheses); .reshape() is method (needs parentheses)"
- "Slice endpoint: excluded in standard Python, but INCLUDED in pandas .loc"
- "Python histogram convention (left-closed) differs from R (right-closed)"
- "NumPy is way faster than Python lists for numerical operations"