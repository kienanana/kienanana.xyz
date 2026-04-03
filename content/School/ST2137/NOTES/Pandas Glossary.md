---
class: note
tags:
  - numpy
  - pandas
  - python
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 03:22:03
aliases:
---
> Quick reference: [[Pandas]]
## QUICK REFERENCE CARD

### Most Used Functions

python

```python
# Reading
pd.read_csv(), pd.read_excel()

# Inspection
df.head(), df.info(), df.describe(), df.shape

# Selection
df['col'], df[['col1','col2']], df.loc[], df.iloc[]

# Filtering
df[df['col'] > value]

# Grouping
df.groupby('col').agg()

# Statistics
df.mean(), df.median(), df.std(), df.corr()

# Manipulation
df.drop(), df.rename(), df.sort_values()

# Missing data
df.isnull(), df.dropna(), df.fillna()

# Combining
pd.concat(), pd.merge(), pd.crosstab()

# Styling (from Assignment)
df.style.background_gradient(axis=1)
```

---

## IMPORTING

python

```python
import pandas as pd
import numpy as np  # often used together
```

---

## DATA STRUCTURES

### Series (1D)

python

```python
import pandas as pd

# Create Series
s = pd.Series([1, 2, 3, 4])
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Access
s[0]                                   # by position
s['a']                                 # by index label
s.iloc[0]                              # by integer position (explicit)
s.loc['a']                             # by label (explicit)
```

### DataFrame (2D)

python

```python
# Create DataFrame
df = pd.DataFrame({'col1': [1,2,3], 'col2': ['a','b','c']})
df = pd.read_csv("file.csv")

# From dict of lists
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})
```

---

## READING & WRITING DATA

### Reading Files

python

```python
# CSV
pd.read_csv("file.csv")                         # default: has header
pd.read_csv("file.csv", header=None)            # no header
pd.read_csv("file.csv", delimiter=";")          # custom delimiter
pd.read_csv("file.csv", names=['col1','col2'])  # specify names

# Excel
pd.read_excel("file.xlsx")
pd.read_excel("file.xlsx", sheet_name="Sheet2")

# JSON
pd.read_json("file.json")

# Text files (more control)
pd.read_table("file.txt", delimiter="\t")
```

### Writing Files

python

```python
df.to_csv("output.csv", index=False)            # save as CSV
df.to_excel("output.xlsx", index=False)         # save as Excel
df.to_json("output.json")                       # save as JSON
```

---

## DATAFRAME INSPECTION

### Basic Info

python

```python
df.head()                              # first 5 rows
df.head(10)                            # first 10 rows
df.tail()                              # last 5 rows
df.info()                              # column types, non-null counts
df.describe()                          # summary statistics (numeric cols)
df.shape                               # (rows, cols) - attribute, no ()
len(df)                                # number of rows
df.columns                             # column names
df.dtypes                              # data types of columns
df.index                               # row index
```

### Quick Checks

python

```python
df.isnull().sum()                      # count nulls per column
df.duplicated().sum()                  # count duplicate rows
df['col'].unique()                     # unique values
df['col'].nunique()                    # count unique values
df['col'].value_counts()               # frequency table
```

---

## SELECTING DATA

### Column Selection

python

```python
df['col']                              # single column → Series
df[['col']]                            # single column → DataFrame
df[['col1', 'col2']]                   # multiple columns
```

### Row Selection

python

```python
df[0:5]                                # first 5 rows (slicing)
df[df['age'] > 25]                     # filter by condition
```

### loc (Label-based)

**Uses index/column NAMES, INCLUDES endpoint in slices**

python

```python
df.loc[0]                              # row with index 0
df.loc[0:5]                            # rows 0 to 5 (INCLUSIVE)
df.loc[:, 'col']                       # all rows, one column
df.loc[0:5, 'col1':'col3']             # rows 0-5, cols col1-col3
df.loc[df['age'] > 25]                 # filter rows
df.loc[df['age'] > 25, 'name']         # filtered rows, one column
```

### iloc (Position-based)

**Uses integer POSITIONS, EXCLUDES endpoint**

python

```python
df.iloc[0]                             # first row
df.iloc[0:5]                           # rows 0-4 (excludes 5)
df.iloc[:, 0]                          # all rows, first column
df.iloc[0:5, 0:3]                      # rows 0-4, cols 0-2
df.iloc[-5:]                           # last 5 rows
df.iloc[::-1]                          # reverse row order

# Examples from tutorial:
df.iloc[0:10]                          # first 10 rows
df.iloc[0:10:2]                        # first 10, every 2nd row
df.iloc[0::2, [0, 2, 3, 4]]            # alternate rows, specific cols
df.iloc[-5:]                           # last 5 rows
df.iloc[::-1]                          # all rows reversed
```

### Boolean Indexing

python

```python
# Single condition
df[df['Gender'] == 'M']                # males
df[df['Age'] > 25]                     # age > 25

# Multiple conditions (MUST bracket each!)
df[(df['Gender'] == 'M') & (df['Age'] > 25)]     # AND
df[(df['Gender'] == 'M') | (df['Grade'] == 'A')]  # OR

# Using query (alternative syntax)
df.query('Age > 25 and Gender == "M"')
```

---

## MODIFYING DATA

### Adding Columns

python

```python
df['new_col'] = values                 # add new column
df['total'] = df['col1'] + df['col2']  # calculated column
df.insert(1, 'new_col', values)        # insert at position 1
```

### Renaming

python

```python
df.rename(columns={'old': 'new'})      # rename columns
df.rename(columns={'old': 'new'}, inplace=True)  # modify in place
df.columns = ['new1', 'new2', 'new3']  # rename all
```

### Dropping

python

```python
df.drop('col', axis=1)                 # drop column
df.drop(['col1', 'col2'], axis=1)      # drop multiple columns
df.drop(0, axis=0)                     # drop row by index
df.drop_duplicates()                   # drop duplicate rows
df.dropna()                            # drop rows with any NaN
```

### Type Conversion

python

```python
df['col'].astype(int)                  # convert to integer
df['col'].astype(float)                # convert to float
df['col'].astype(str)                  # convert to string
pd.to_datetime(df['date'])             # convert to datetime
pd.to_numeric(df['col'])               # convert to numeric
```

---

## GROUPING & AGGREGATION

### groupby()

python

```python
# Returns iterable of (key, dataframe) tuples
for group_name, group_df in df.groupby('column'):
    print(group_name)
    print(group_df)

# With enumerate
for i, (group_name, group_df) in enumerate(df.groupby('column')):
    print(f"Group {i}: {group_name}")
```

### Aggregation After groupby

python

```python
df.groupby('col').mean()               # mean by group
df.groupby('col').sum()                # sum by group
df.groupby('col').count()              # count by group
df.groupby('col').agg(['mean', 'sum']) # multiple aggregations
df.groupby('col')['col2'].sum()        # sum col2 for each group

# Custom aggregation
df.groupby('col').agg({'col1': 'mean', 'col2': 'sum'})

# Example from tutorial:
for opponent, group in df.groupby('Opponent'):
    print(f"Points against {group.Opponent.iloc[0]}: {group.pts.sum()}")
```

### split-apply-combine Pattern

**This is THE paradigm for data analysis!**

1. **Split** data into groups (groupby)
2. **Apply** function to each group (agg, transform, apply)
3. **Combine** results back together

python

```python
# Example: mean score by gender
df.groupby('gender')['score'].mean()
```

---

## SORTING

python

```python
df.sort_values('col')                           # sort by column (ascending)
df.sort_values('col', ascending=False)          # descending
df.sort_values(['col1', 'col2'])                # sort by multiple
df.sort_index()                                 # sort by index
```

---

## COMBINING DATA

### Concatenating

python

```python
pd.concat([df1, df2])                  # stack vertically (rows)
pd.concat([df1, df2], axis=1)          # stack horizontally (cols)
```

### Merging

python

```python
pd.merge(df1, df2, on='key')           # inner join
pd.merge(df1, df2, on='key', how='left')   # left join
pd.merge(df1, df2, on='key', how='outer')  # outer join
```

---

## STRING OPERATIONS

### Series String Methods (.str)

python

```python
df['col'].str.upper()                  # uppercase
df['col'].str.lower()                  # lowercase
df['col'].str.title()                  # title case
df['col'].str.strip()                  # remove whitespace
df['col'].str.replace('old', 'new')    # replace
df['col'].str.contains('pattern')      # check if contains
df['col'].str.split(',')               # split by delimiter
df['col'].str.cat(sep='')              # concatenate all (tutorial)
# If sep=None, concat to single long string
df['col'].str.len()                    # length of each string
df['col'].str[:3]                      # first 3 characters
```

---

## APPLYING FUNCTIONS

### apply()

python

```python
# Apply function to each column (axis=0, default)
df.apply(np.sum)

# Apply to each row (axis=1)
df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# Apply to single column
df['col'].apply(lambda x: x**2)
```

### map()

python

```python
# Map values in Series (one-to-one mapping)
df['col'].map({1: 'A', 2: 'B', 3: 'C'})
df['col'].map(lambda x: x*2)
```

### applymap()

python

```python
# Apply function to every element in DataFrame
df.applymap(lambda x: x*2)             # DEPRECATED, use .map() on df
df.map(lambda x: x*2)                  # NEW in pandas 2.1+
```

---

## ITERATING (Use Sparingly!)

**Note:** Iteration is slow in pandas. Use vectorized operations when possible!

python

```python
# iterrows() - returns (index, Series)
for index, row in df.iterrows():
    print(row['col'])
    # row is a Series

# itertuples() - faster, returns namedtuple
for row in df.itertuples():
    print(row.col)
    # access with dot notation
```

---

## CUMULATIVE OPERATIONS

python

```python
df['col'].cumsum()                     # cumulative sum
df['col'].cumprod()                    # cumulative product
df['col'].cummax()                     # cumulative maximum
df['col'].cummin()                     # cumulative minimum

# Default axis=0 (down rows)
# Use axis=1 for across columns
```

---

## RESHAPING DATA

### Pivot & Melt

python

```python
# Wide to long (melt)
pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])

# Long to wide (pivot)
df.pivot(index='row', columns='col', values='value')

# Pivot table (aggregation)
df.pivot_table(values='val', index='row', columns='col', aggfunc='mean')
```

### Stack & Unstack

python

```python
df.stack()                             # pivot columns to rows
df.unstack()                           # pivot rows to columns
```

---

## CONTINGENCY TABLES

### crosstab()

python

```python
# Create contingency table
pd.crosstab(df['col1'], df['col2'])

# With row/column totals
pd.crosstab(df['col1'], df['col2'], margins=True)

# Normalized (proportions)
pd.crosstab(df['col1'], df['col2'], normalize='index')   # row props
pd.crosstab(df['col1'], df['col2'], normalize='columns') # col props
pd.crosstab(df['col1'], df['col2'], normalize='all')     # overall props

# Convert from crosstab to long format (for Kendall's tau)
# Need to expand back to original observations
```

**From Assignment:** Extract values for numerical operations

python

```python
# Create contingency table
tab = pd.crosstab(df['A'], df['B'])

# Extract as numpy array for calculations
n_ij = tab.values                      # numpy array of counts
n = n_ij.sum()                         # total count

# Now can do matrix operations
row_sums = n_ij.sum(axis=1)            # row totals
col_sums = n_ij.sum(axis=0)            # column totals
```

**Key insight:** `.values` gives you the underlying numpy array for mathematical operations

---

## MISSING DATA

python

```python
df.isnull()                            # check for NaN (returns bool df)
df.notnull()                           # opposite of isnull()
df.isnull().sum()                      # count NaN per column
df.dropna()                            # drop rows with any NaN
df.dropna(axis=1)                      # drop columns with any NaN
df.fillna(value)                       # fill NaN with value
df.fillna(df.mean())                   # fill with column means
df.interpolate()                       # interpolate missing values
```

---

## PLOTTING (PANDAS)

### Built-in Plotting

python

```python
# Uses matplotlib backend
df.plot()                              # line plot
df.plot(kind='scatter', x='col1', y='col2')
df.plot(kind='bar')                    # bar chart
df.plot(kind='barh')                   # horizontal bar
df.plot(kind='hist')                   # histogram
df.plot(kind='box')                    # box plot
df.plot(kind='density')                # density plot
df.plot(kind='kde')                    # KDE (same as density)

# Histogram options
df['col'].hist(bins=20)                # histogram with 20 bins
df[['col1','col2','col3']].hist(layout=(1,3), figsize=(12,4))

# Stacked bar chart
pd.crosstab(df.col1, df.col2).plot(kind='bar', stacked=True)
```

### Plot Parameters

python

```python
# Common arguments
figsize=(width, height)                # figure size in inches
color='blue'                           # color
alpha=0.5                              # transparency (0-1)
grid=True                              # show grid
xlabel='X', ylabel='Y'                 # axis labels
title='Title'                          # plot title
legend=True                            # show legend
```

---

## STATISTICS & SCIPY

### Descriptive Statistics

python

```python
df['col'].mean()                       # mean
df['col'].median()                     # median
df['col'].std()                        # standard deviation
df['col'].var()                        # variance
df['col'].min(), df['col'].max()       # min, max
df['col'].quantile([0.25, 0.75])       # quartiles
df['col'].describe()                   # summary statistics
df.corr()                              # correlation matrix
```

### Correlation

python

```python
df[['col1', 'col2']].corr()            # correlation matrix
df['col1'].corr(df['col2'])            # correlation between two

# Styling heatmap
corr_matrix = df.corr()
corr_matrix.style.background_gradient(
    cmap='coolwarm_r',                 # blue=positive, red=negative
    axis=None,                         # color across entire matrix
    vmin=-1, vmax=1                    # symmetric color scale
)
```

---

## STYLING DATAFRAMES

### background_gradient() - Color Coding

python

```python
# Basic usage
df.style.background_gradient()                  # color by column (default)
df.style.background_gradient(axis=0)            # color by column (explicit)
df.style.background_gradient(axis=1)            # color by ROW
df.style.background_gradient(axis=None)         # color across ENTIRE table

# Custom color maps
df.style.background_gradient(cmap='Blues')      # blue gradient
df.style.background_gradient(cmap='coolwarm')   # blue-white-red
```

**From Assignment:** Contingency table styling

python

```python
# Default: colors within each column
pd.crosstab(df['A'], df['B']).style.background_gradient()

# Better for contingency tables: color within each row
pd.crosstab(df['A'], df['B']).style.background_gradient(axis=1)
# Shows which categories rater B tends to choose given rater A's choice
```

**When to use each axis:**

- **axis=0** (default): Compare values down each column
    - Use for: comparing different rows within same variable
- **axis=1**: Compare values across each row
    - Use for: contingency tables, showing conditional distributions
- **axis=None**: Compare all values in entire DataFrame
    - Use for: correlation matrices, symmetric data

**From Lectures:** Correlation matrix styling

python

```python
# Symmetric color scale for correlations
df.corr().style.background_gradient(
    cmap='coolwarm_r',
    axis=None,                         # CRITICAL: compare all cells
    vmin=-1, vmax=1                    # CRITICAL: symmetric scale
)
```

### Hypothesis Tests (scipy.stats)

python

```python
from scipy import stats

# Chi-square test
chi2, p, dof, expected = stats.chi2_contingency(table)
# Returns: (chi2_statistic, p_value, degrees_of_freedom, expected_frequencies)

# Fisher's exact test (2x2 tables)
oddsratio, p = stats.fisher_exact(table)

# t-test
stats.ttest_ind(group1, group2)        # independent samples
stats.ttest_1samp(sample, pop_mean)    # one-sample

# Kendall's tau
stats.kendalltau(x, y)                 # returns KendalltauResult
result = stats.kendalltau(x, y)
result.statistic                       # tau value
result.pvalue                          # p-value

# Linear regression
slope, intercept, r, p, stderr = stats.linregress(x, y)
```

---

## CATEGORICAL DATA (STATSMODELS)

python

```python
from statsmodels.api import stats as sms
from statsmodels.graphics.mosaicplot import mosaic

# Odds ratio & relative risk (2x2 tables)
from statsmodels.stats.contingency_tables import Table2x2
table_obj = Table2x2(table_array)
table_obj.oddsratio                    # odds ratio
table_obj.riskratio                    # relative risk (different rows/cols)
table_obj.summary()                    # full summary

# Mosaic plot
mosaic(df, ['col1', 'col2'])
mosaic(df, ['col1', 'col2'], statistic=True)  # color by residuals
# Green = neutral (Python), Blue/Red = pos/neg residuals
```

---

## MATPLOTLIB BASICS

python

```python
import matplotlib.pyplot as plt

# Basic plotting
plt.plot(x, y)                         # line plot
plt.scatter(x, y)                      # scatter plot
plt.hist(data, bins=20)                # histogram
plt.bar(x, height)                     # bar chart
plt.boxplot(data)                      # box plot

# Customization
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.legend(['line1', 'line2'])
plt.grid(True)
plt.xlim(0, 10)                        # x-axis limits
plt.ylim(0, 100)                       # y-axis limits

# Multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x, y)                     # plot on first subplot
axes[1].hist(data)                     # plot on second subplot
axes[2].scatter(x, y)                  # plot on third subplot

# Save figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()
```

---

## ADVANCED PANDAS

### Method Chaining

python

```python
# Wrap in parentheses, one method per line for readability
result = (df
    .query('age > 25')
    .groupby('gender')
    ['score']
    .mean()
    .sort_values(ascending=False)
)
```

### SettingWithCopyWarning

**IMPORTANT:** Don't ignore this warning!

python

```python
# WRONG - may not work as expected
subset = df[df['age'] > 25]
subset['new_col'] = values             # WARNING!

# CORRECT - create explicit copy
subset = df[df['age'] > 25].copy()
subset['new_col'] = values             # No warning
```

### Axis Parameter

**This is confusing but important!**

python

```python
# axis=0 or 'index' → operate DOWN rows (column-wise operation)
df.mean(axis=0)                        # mean of each column
df.drop('col', axis=0)                 # drop row

# axis=1 or 'columns' → operate ACROSS columns (row-wise operation)  
df.mean(axis=1)                        # mean of each row
df.drop('col', axis=1)                 # drop column

# Memory trick: axis=N "knocks out" dimension N
# axis=0 knocks out row dimension (left with column results)
# axis=1 knocks out column dimension (left with row results)
```

### inplace Parameter

python

```python
# Many pandas functions have inplace parameter
df.drop('col', axis=1)                 # returns new df (default)
df.drop('col', axis=1, inplace=True)   # modifies df in place

# Look out for this! Default is False
```

---

## IMPORTANT DIFFERENCES: PANDAS vs R

### Indexing Comparison

|Feature|Pandas|R|
|---|---|---|
|.loc|Label-based, INCLUDES endpoint|Not applicable|
|.iloc|Position-based, EXCLUDES endpoint|Similar to R's default|
|Default slicing|Excludes endpoint|Includes endpoint|

python

```python
# Pandas loc INCLUDES endpoint
df.loc[1:3]  # rows with labels 1, 2, AND 3

# Pandas iloc EXCLUDES endpoint  
df.iloc[1:3]  # rows at positions 1, 2 (NOT 3)

# R behavior for comparison
# df[1:3, ]  # rows 1, 2, 3 (includes 3)
```

**Lecture quote:** "Slice endpoint: excluded in standard Python, but INCLUDED in pandas .loc (inconsistency explicitly warned)"

### Index is Critical

python

```python
# Pandas uses index for fast lookups (unlike R row numbers)
df.set_index('id')                     # set column as index
df.reset_index()                       # convert index back to column
df.loc['index_value']                  # fast lookup by index
```

**Lecture quote:** "Index is critical in pandas (unlike R); used for fast retrieval"

### Attribute vs Method (IMPORTANT!)

python

```python
# Attribute (no parentheses)
df.shape                               # NOT df.shape()
df.columns
df.index
df.T                                   # transpose

# Method (needs parentheses)
df.head()                              # NOT df.head
df.mean()
df.sum()
df.copy()                              # ALWAYS use when subsetting!
```

**Lecture quote:** ".shape is attribute (no parentheses); .reshape() is method (needs parentheses)"

---

## COMMON MISTAKES TO AVOID

❌ **Forgetting copy()**

python

```python
# WRONG
subset = df[df['age'] > 25]
subset['new'] = values                 # May cause warning

# CORRECT
subset = df[df['age'] > 25].copy()
```

❌ **Using 'and'/'or' instead of &/|**

python

```python
# WRONG
df[(df['age'] > 25) and (df['gender'] == 'M')]

# CORRECT
df[(df['age'] > 25) & (df['gender'] == 'M')]
```

❌ **Forgetting to bracket conditions**

python

```python
# WRONG
df[df['age'] > 25 & df['gender'] == 'M']

# CORRECT  
df[(df['age'] > 25) & (df['gender'] == 'M')]
```

❌ **Modifying DataFrame during iteration**

python

```python
# WRONG - don't modify df while iterating
for i, row in df.iterrows():
    df.loc[i, 'new'] = value           # Slow and problematic

# CORRECT - use vectorized operation
df['new'] = df['col'].apply(lambda x: value)
```

❌ **Mixing loc and iloc**

python

```python
# WRONG
df.loc[0:5, 0:3]                       # loc uses labels, not positions!

# CORRECT
df.iloc[0:5, 0:3]                      # iloc for positions
df.loc[0:5, 'col1':'col3']             # loc for labels
```

---

## BEST PRACTICES

✅ **Use vectorized operations (avoid loops)**

python

```python
# SLOW
for i in range(len(df)):
    df.loc[i, 'new'] = df.loc[i, 'old'] * 2

# FAST
df['new'] = df['old'] * 2
```

✅ **Check data after reading**

python

```python
df = pd.read_csv('file.csv')
print(df.head())
print(df.info())
print(df.describe())
```

✅ **Use meaningful column names**

python

```python
# GOOD
df.rename(columns={'col1': 'student_age'}, inplace=True)

# BAD  
df.rename(columns={'col1': 'x1'}, inplace=True)
```

✅ **Handle missing data explicitly**

python

```python
df.dropna()                            # or
df.fillna(value)                       # or
df['col'].fillna(df['col'].mean())     # fill with mean
```

✅ **Use appropriate data types**

python

```python
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

---
## NOTES FROM LECTURES

**Key Points:**

- "Index is critical in pandas (unlike R); used for fast retrieval"
- "SettingWithCopyWarning: don't ignore; create explicit copy with .copy()"
- "Slice endpoint: excluded in standard Python, but INCLUDED in pandas .loc"
- ".shape is attribute (no parentheses); .reshape() is method (needs parentheses)"
- "split-apply-combine paradigm: key to data science"
- "axis=1 knocks out column dimension (row-wise operation); axis=0 knocks out row dimension"
- "Python histogram convention (left-closed) differs from R (right-closed)"
- "Chaining methods: wrap in parentheses and put each .method() on new line for readability"
- "%pip install inside Jupyter installs into virtual environment"
- "itables package: from itables import show — interactive table browsing in Jupyter"

