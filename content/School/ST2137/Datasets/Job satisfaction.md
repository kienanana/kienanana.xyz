---
class: note
tags:
  - dataset
  - R
  - python
  - numpy
  - scipy
  - DescTools
  - categorical
  - ordinal
source:
related:
  - "[[L4 Exploring Categorical Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
  - US job satisfaction survey
---
## Description
> From [[L4 Exploring Categorical Data#For Ordinal Variables]]

A 4×4 cross-classification of income level (ordinal) against job-satisfaction level (ordinal) from a US survey. Used to illustrate ordinal-association measures (Kendall's $\tau_b$, Goodman-Kruskal $\gamma$) — the analogues of Pearson's correlation for ordered categorical data.

|               | Very Dissat. | Little Dissat. | Mod. Sat. | Very Sat. |
|---------------|:------------:|:--------------:|:---------:|:---------:|
| <15,000       | 1            | 3              | 10        | 6         |
| 15,000–25,000 | 2            | 3              | 10        | 7         |
| 25,000–40,000 | 1            | 6              | 14        | 12        |
| >40,000       | 0            | 1              | 9         | 11        |

## Ordinal association
> From [[L4 Exploring Categorical Data#For Ordinal Variables]] and [[L4 Exploring Categorical Data#Definition 4.1]]

A **pair of subjects** is:
- *concordant* — subject ranked higher on $X$ is also ranked higher on $Y$
- *discordant* — subject ranked higher on $X$ is ranked lower on $Y$
- *tied* — same rank on $X$ and/or $Y$

Let $C$ = # concordant pairs, $D$ = # discordant pairs.

**Goodman-Kruskal $\gamma$:** $(C - D) / (C + D)$ — easy to interpret; ignores ties.
**Kendall's $\tau_b$:** similar numerator, with a normalising denominator that handles ties; less sensitive to cut-points defining the categories.

Both measures lie in $[-1, 1]$:
- $\approx 0$ → weak trend
- near $\pm 1$ → strong monotone (positive / negative) association

See [[Gamma Tau]] for a longer reference on these measures.

##### R code
```R
x <- matrix(c(1, 3, 10, 6,
              2, 3, 10, 7,
              1, 6, 14, 12,
              0, 1, 9, 11), ncol=4, byrow=TRUE)
dimnames(x) <- list(c("<15,000", "15,000-25,000",
                      "25,000-40,000", ">40,000"),
                    c("Very Dissat.", "Little Dissat.",
                      "Mod. Sat.", "Very Sat."))
us_svy_tab <- as.table(x)

library(DescTools)
output <- Desc(x, plotit = FALSE, verbose = 3)
output[[1]]$assocs
```

##### Python code
```python
import numpy as np
from scipy import stats

us_svy_tab = np.array([[1, 3, 10, 6],
                       [2, 3, 10, 7],
                       [1, 6, 14, 12],
                       [0, 1, 9, 11]])
dim1 = us_svy_tab.shape
x, y = [], []
for i in range(dim1[0]):
    for j in range(dim1[1]):
        for _ in range(us_svy_tab[i, j]):
            x.append(i); y.append(j)

kt_output = stats.kendalltau(x, y)
print(f"Estimate of tau-b: {kt_output.statistic:.4f}.")
# The estimate of tau-b is 0.1524.
```

**Results:** Goodman-Kruskal $\gamma \approx 0.22$, Kendall's $\tau_b \approx 0.15$. Both point to a weak positive association: higher-income respondents tend to report higher job satisfaction, though the effect is modest and the lower confidence limit is close to zero — borderline significant.

> Note that in Python, `scipy.stats.kendalltau` expects two rank vectors, so we reconstruct them by "unrolling" the contingency table. R's `DescTools::Desc` works directly on the table.

---
See also: [[L4 Exploring Categorical Data]] · [[Gamma Tau]]
