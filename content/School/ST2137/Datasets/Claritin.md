---
class: note
tags:
  - dataset
  - R
  - python
  - numpy
  - pandas
  - matplotlib
  - scipy
  - categorical
  - fishers-exact
source:
related:
  - "[[L4 Exploring Categorical Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L4 Exploring Categorical Data#Example 4.3]]

A 2×2 contingency table for a clinical trial comparing Claritin (active drug) vs. placebo, cross-tabulated against whether patients reported nervousness as a side effect.

| | nervous | not nervous |
|---|---|---|
| **claritin** | 4 | 184 |
| **placebo** | 2 | 260 |

Small counts in the "nervous" column make this dataset a canonical example for [[Chi-Square & Fisher|Fisher's exact test]] — the chi-squared expected-count assumption (all cells > 5) is violated.

## Bar chart
> From [[L4 Exploring Categorical Data#Bar charts]]

A side-by-side bar chart of proportions highlights the relative difference in nervousness rates between the two arms.

##### Python code
```python
import numpy as np
import pandas as pd

claritin_tab = np.array([[4, 184], [2, 260]])
claritin_prop = claritin_tab / claritin_tab.sum(axis=1).reshape((2,1))

xx = pd.DataFrame(claritin_prop,
                  columns=['nervous', 'not_nervous'],
                  index=['claritin', 'placebo'])

ax = xx.plot(kind='bar', stacked=False, rot=1.0, figsize=(10,4),
             title='Nervousness by drug')
ax.legend(loc='upper left');
```

Proportions are small in absolute terms (~2% vs ~1%) but the relative difference looks noteworthy — hence the need for a formal test.

## Fisher's exact test
> From [[L4 Exploring Categorical Data#Fisher's Exact Test]]

Used when expected cell counts are < 5 (chi-squared's approximation fails). Models the top-left cell count as hypergeometric under fixed marginals.

##### R code
```R
y <- matrix(c(4, 2, 184, 260), nrow=2)
dimnames(y) <- list(c("claritin", "placebo"), c("nervous", "not nervous"))
claritin_tab <- as.table(y)
fisher.test(claritin_tab)
```

##### Python code
```python
from scipy import stats

fe_output = stats.fisher_exact(claritin_tab)
print(f"The p-value for the test is {fe_output.pvalue:.4f}.")
# The p-value for the test is 0.2412.
```

**Conclusion:** p-value = 0.2412. Do not reject $H_0$; no significant association between drug group and nervousness.

Verifying the chi-squared test was not appropriate:
```R
chisq.test(claritin_tab)$expected
```
confirms at least one expected count is below 5.

---
See also: [[L4 Exploring Categorical Data]] · [[Chi-Square & Fisher]]
