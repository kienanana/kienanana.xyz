---
class: note
tags:
  - dataset
  - R
  - python
  - pandas
  - scipy
  - paired-test
  - wilcoxon
source:
related:
  - "[[L7 Two-sample Hypothesis Tests]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
  - Heart rate
  - Health promo
---
## Description
> From [[L7 Two-sample Hypothesis Tests#Example 7.4 (Heart Rate Before / After Treadmill)]]

Heart rate measurements for 12 subjects before and after a treadmill session (`baseline` vs `after5`). Because both measurements come from the *same* subject, observations are **paired**, not independent — the appropriate test is the paired-sample version of the t-test (or its non-parametric analogue).

File: `data/health_promo_hr.csv`. Columns: `baseline`, `after5`.

## Paired t-test
> From [[L7 Two-sample Hypothesis Tests#Example 7.4 (Heart Rate Before / After Treadmill)]]

Compute $D_i = X_i - Y_i$; test $H_0: \mu_D = 0$ via
$$
T_2 = \frac{\bar{D}}{s / \sqrt{n}} \sim t_{n-1} \text{ under } H_0
$$

##### R code
```R
hr_df <- read.csv("data/health_promo_hr.csv")
before <- hr_df$baseline
after  <- hr_df$after5
t.test(before, after, paired=TRUE)
```

##### Python code
```python
import pandas as pd
from scipy import stats

hr_df = pd.read_csv("data/health_promo_hr.csv")
paired_out = stats.ttest_rel(hr_df.baseline, hr_df.after5)
print(f"""
Test statistic: {paired_out.statistic:.3f}.
p-val: {paired_out.pvalue:.3f}.""")
```

**Assumption check caveat:** with only 12 subjects the case for Normality of the $D_i$ is weak. For small-sample paired data, a graphical check + the non-parametric analogue below is the safer route.

**Paired/agreement diagnostic plots:**
- **Paired-line plot** — one line per subject connecting baseline to after. Similar gradients (consistently up or consistently down) support a systematic effect; mixed signs weaken it.
- **Agreement plot** (after vs. before, with the $y = x$ reference line) — if points scatter around $y = x$, no mean shift.

## Non-parametric paired test
> From [[L7 Two-sample Hypothesis Tests#Example 7.6 (Heart Rate Before / After Treadmill)]]

**Wilcoxon Signed-Rank Test (WST)** — paired-sample analogue of Wilcoxon Rank-Sum. Tests whether the median of $D_i = X_i - Y_i$ is 0. No Normality assumption.

Procedure:
1. Drop $D_i = 0$.
2. Rank the remaining $|D_i|$ from 1 (smallest) to $m$ (largest).
3. $R_2$ = sum of ranks where $D_i > 0$.
4. Under $H_0$, $E(R_2) = m(m+1)/4$; the continuity-corrected test statistic $W_2 \sim N(0,1)$ approximately when the number of non-zero $D_i \geq 16$.

##### R code
```R
wilcox.test(before, after, paired=TRUE, exact=FALSE)
```

##### Python code
```python
wsr_out = stats.wilcoxon(hr_df.baseline, hr_df.after5,
                         correction=True, method='approx')
print(f"""Test statistic: {wsr_out.statistic:.3f}.
p-val: {wsr_out.pvalue:.3f}.""")
```

**Small-sample caveat:** with only 12 subjects here, we do not hit the $\geq 16$ threshold for the Normal approximation. The ideal is the **exact** version, but R/Python can't run exact when there are ties. SAS does use the exact version — which accounts for any difference in p-values between SAS and R/Python.

**Why test statistics look different across software:**
- R / Python report $R_2$ directly.
- SAS reports $R_2 - E(R_2)$.

For $n = 12$:
$$
0 - \frac{12(12+1)}{4} = -39
$$
reconciles a reported `0` in R with SAS's `-39`.

> If neither approximation is great and exact-with-ties is unavailable, fall back to the bootstrap or a permutation test (see [[L10 Simulation]]).

---
See also: [[L7 Two-sample Hypothesis Tests]] · [[L10 Simulation]]
