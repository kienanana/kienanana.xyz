---
class: note
tags:
  - dataset
  - R
  - python
  - numpy
  - scipy
  - robust-statistics
source:
related:
  - "[[L5 Robust Statistics]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
  - Awareness
---
## Description
> From [[L5 Robust Statistics#Self-Awareness Dataset]]

19 observations of a self-awareness measurement, highly right-skewed. The mean of the full dataset exceeds the 3rd quartile — another classic case where the sample mean/SD are contaminated by a few very large values.

Values (sorted):
```
77, 87, 88, 114, 151, 210, 219, 246, 253, 262, 296,
299, 306, 376, 428, 515, 666, 1310, 2611
```

Variable in code: `awareness`.

## Histogram and outlier
> From [[L5 Robust Statistics#Self-Awareness Dataset]]

A histogram reveals the strong right-skew and the two large values (1310, 2611) far separated from the body of the data. This pattern motivates [[L5 Robust Statistics|robust]] measures of location and scale.

## Scale estimates (robust vs. classical)
> From [[L5 Robust Statistics#Example 5.6]]

Compare sample SD, MAD, and IQR.

##### R code
```R
sd(awareness)
## [1] 594.6295

mad(awareness, constant=1)
## [1] 114

IQR(awareness)
## [1] 221.5
```

##### Python code
```python
import numpy as np
from scipy import stats

awareness = np.array([77, 87, 88, 114, 151, 210, 219, 246, 253, 262, 296,
                      299, 306, 376, 428, 515, 666, 1310, 2611])

awareness.std()
## 578.7698292373723

stats.median_abs_deviation(awareness)
## 114.0

stats.iqr(awareness)
## 221.5
```

The classical sample SD ($\approx 579$–$595$) is dominated by the two extreme values. MAD (114) and IQR (221.5) — both based on quantiles of absolute deviations, not squared deviations — are resistant.

For Normal data, $\sigma \approx 1.4826 \cdot \text{MAD}$ and $\sigma \approx \text{IQR} / 1.35$. On this skewed dataset those identities don't hold; we treat MAD and IQR as robust *spread* summaries, not $\sigma$ estimates. See [[L5 Robust Statistics#Proposition 5.1 (MAD for Normal).]] and [[L5 Robust Statistics#Proposition 5.2 (IQR for Normal).]] for the Normal case.

---
See also: [[L5 Robust Statistics]] · [[Copper]]
