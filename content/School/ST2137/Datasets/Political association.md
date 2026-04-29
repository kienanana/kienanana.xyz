---
class: note
tags:
  - dataset
  - R
  - python
  - numpy
  - matplotlib
  - statsmodels
  - categorical
  - chi-square
source:
related:
  - "[[L4 Exploring Categorical Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L4 Exploring Categorical Data#example 4.2]]

A 2×3 contingency table of political party association (Democrat / Independent / Republican) by gender (female / male). Used to illustrate bar charts, mosaic plots, and the chi-squared test for $r \times c$ tables.

|            | Dem | Ind | Rep |
|------------|:---:|:---:|:---:|
| **female** | 762 | 327 | 468 |
| **male**   | 484 | 239 | 477 |

## Bar chart
> From [[L4 Exploring Categorical Data#Bar charts]]

A row-proportion bar chart shows the political-party mix within each gender. The key step is dividing each cell by its row total so we compare distributions (not raw counts).

##### R code
```R
library(lattice)

x <- matrix(c(762, 327, 468,
              484, 239, 477), ncol=3, byrow=TRUE)
dimnames(x) <- list(c("female", "male"),
                    c("Dem", "Ind", "Rep"))
political_tab <- as.table(x)

barchart(political_tab / rowSums(political_tab),
         main="Political association by gender",
         horizontal = FALSE, auto.key=TRUE)
```

## Mosaic plot
> From [[L4 Exploring Categorical Data#Mosaic Plots]]

Unlike a bar chart, a mosaic plot encodes **both** the count (tile area) and the conditional proportions. With `shade=TRUE`, cells are coloured by their standardised residual under the independence model:
- **Blue** — more observations than expected under independence
- **Red** — fewer observations than expected

This makes it a visual partner to the chi-squared test: coloured cells *are* the cells driving the test's significance.

##### R code
```R
mosaicplot(political_tab, shade=TRUE,
           main="Political association by gender")
```

##### Python code
```python
from statsmodels.graphics.mosaicplot import mosaic
import numpy as np

political_tab = np.asarray([[762, 327, 468],
                            [484, 239, 477]])
mosaic(political_tab, statistic=True, gap=0.05);
```

## Chi-squared test (r × c)
> From [[L4 Exploring Categorical Data#Chi-squared Test for r x c Tables]]

For an $r \times c$ table the test is identical in form to the 2×2 case; under $H_0$ the statistic follows $\chi^2_{(r-1)(c-1)}$. Here $df = (2-1)(3-1) = 2$.

##### R code
```R
chisq.test(political_tab)

# Standardised residuals — tell us which cells drive the (non-)fit
chisq.test(political_tab)$stdres
```

Standardised residuals
$$
r_{ij} = \frac{n_{ij} - \mu_{ij}}{\sqrt{\mu_{ij} (1 - p_{i+})(1 - p_{+j})}}
$$
should be roughly $N(0,1)$ under $H_0$. Large $|r_{ij}|$ flags where the data deviates from independence — the colours in the mosaic plot above correspond to the sign of these residuals.

See [[Chi-Square & Fisher]] for the general procedure and interpretation tips.

---
See also: [[L4 Exploring Categorical Data]] · [[Chi-Square & Fisher]]
