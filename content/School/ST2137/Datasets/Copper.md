---
class: note
tags:
  - dataset
  - R
  - python
  - pandas
  - numpy
  - scipy
  - DescTools
  - robust-statistics
  - bootstrap
source:
related:
  - "[[L5 Robust Statistics]]"
  - "[[L10 Simulation]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
  - Chem
  - Copper in wholemeal flour
---
## Description
> From [[L5 Robust Statistics#Copper in Wholemeal Flour Dataset (Chem)]]

24 measurements of copper content in wholemeal flour. 22 of the 24 points are below 4, but two large values (including 28.95) drag the mean up to 4.28. A canonical example for robust location/scale estimation — the mean is clearly being pulled by outliers.

Variable name in code: `chem`. File: `data/mass_chem.csv`.

## Histogram and outlier
> From [[L5 Robust Statistics#Copper in Wholemeal Flour Dataset (Chem)]]

A histogram reveals the strong right-skew: most mass concentrated below 4, with two isolated high values. The mean (4.28) exceeds the 3rd quartile — a red flag for outlier influence.

## Robust location
> From [[L5 Robust Statistics#Example 5.5]]

Compare the sample mean, 10%-trimmed mean, and Winsorized mean.

##### R code
```R
mean(chem)
## [1] 4.280417

mean(chem, trim=0.1)    # gamma = 0.1
## [1] 3.205

library(DescTools)
vals <- quantile(chem, probs=c(0.1, 0.9))
win_sample <- Winsorize(chem, vals)
mean(win_sample)
## [1] 3.182375
```

##### Python code
```python
import pandas as pd
from scipy import stats

chem = pd.read_csv("data/mass_chem.csv")

chem.chem.mean()
## 4.2804166666666665

stats.trim_mean(chem, proportiontocut=0.1)
## array([3.205])

stats.mstats.winsorize(chem.chem, limits=0.1).mean()
## 3.185
```

Trimmed and Winsorized means (~3.2) sit close to each other and near the median — they reflect the "typical" observation, unlike the sample mean which is distorted by the two outliers.

See [[L5 Robust Statistics]] for theory — trimmed mean drops tail observations; Winsorized mean replaces them with the boundary values (so large outliers have zero or bounded influence via $\psi$).

## Robust scale
> From [[L5 Robust Statistics#Example 5.6]]

Compare the sample SD, MAD, and IQR as scale estimates.

##### R code
```R
sd(chem)
mad(chem, constant=1)
IQR(chem)
```

##### Python code
```python
import numpy as np
# (on awareness data in lecture, but same pattern for chem:)
chem.chem.std()
stats.median_abs_deviation(chem.chem)
stats.iqr(chem.chem)
```

For Normal data, $\sigma \approx 1.4826 \cdot \text{MAD}$ and $\sigma \approx \text{IQR} / 1.35$. When data is non-Normal (as here), MAD and IQR just serve as robust spread measures rather than $\sigma$ estimates.

## Bootstrap CI
> From [[L10 Simulation#Example 10.9]]

Using the bootstrap to get a confidence interval for the **trimmed mean** (no closed-form distribution needed).

##### R code
```R
library(MASS)

mean(chem)
# [1] 4.280417

t.test(chem)
```
The classical t-based CI on the raw mean is very wide — because the sample SD is inflated by outliers.

```R
library(boot)

stat_fn <- function(d, i) {
  b <- mean(d[i], trim=0.1)
  b
}
boot_out <- boot(chem, stat_fn, R = 1999, stype="i")
boot.ci(boot.out = boot_out, type=c("perc", "bca"))
```

The bootstrap returns two interval types:
- **perc** — percentile method (simple but can be biased for skewed statistics)
- **bca** — bias-corrected & accelerated (accounts for skewness and bias; preferred when the statistic distribution is asymmetric)

Both intervals centre around ~3.2 (the trimmed mean from [[L5 Robust Statistics#Example 5.5]]) and are much narrower than the t-based interval. The asymmetry of the bootstrap intervals reflects the asymmetry of the distribution of the trimmed-mean statistic.

---
See also: [[L5 Robust Statistics]] · [[L10 Simulation]]
