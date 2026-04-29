---
class: note
tags:
  - dataset
  - R
  - python
  - scipy
  - statistics
  - two-sample-test
  - non-parametric
  - permutation-test
source:
related:
  - "[[L7 Two-sample Hypothesis Tests]]"
  - "[[L10 Simulation]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
Measurements of physical characteristics (viscera weight, etc.) of abalone, along with gender status. A sample of 50 male and 50 female records is used in [[L7 Two-sample Hypothesis Tests]] to compare viscera weight between males and females. Also revisited in [[L10 Simulation]] for a permutation test.

File: `data/abalone_sub.csv`

## 2-sample t-test
> From [[L7 Two-sample Hypothesis Tests#Example 7.1 (Abalone Measurements)]]

We want to test whether mean viscera weight differs between male and female abalones. Since the two groups are unrelated units, this is the independent 2-sample t-test. We assume Normality and equal variance within each group.

##### R code
```R
abl <- read.csv("data/abalone_sub.csv")
x <- abl$viscera[abl$gender == "M"]
y <- abl$viscera[abl$gender == "F"]

t.test(x, y, var.equal=TRUE)
```

##### Python code
```python
import pandas as pd
from scipy import stats

abl = pd.read_csv("data/abalone_sub.csv")
x = abl.viscera[abl.gender == "M"]
y = abl.viscera[abl.gender == "F"]

t_out = stats.ttest_ind(x, y)
ci_95 = t_out.confidence_interval()

print(f"""
* The p-value for the test is {t_out.pvalue:.3f}.
* The actual value of the test statistic is {t_out.statistic:.3f}.
* The CI is ({ci_95[0]:.3f}, {ci_95[1]:.3f}).
""")
```

**Equal variance check** — prof's rule of thumb: if the larger sd is more than twice the smaller, do not use the equal-variance form.

```R
aggregate(viscera ~ gender, data=abl, sd)
```

**Conclusion:** the p-value is not small enough to reject $H_0$; we do not have evidence of a significant difference between male and female mean viscera weights.

## Normality checks
> From [[L7 Two-sample Hypothesis Tests#Example 7.2 (Abalone Measurements)]]

To assess the Normality assumption we use histograms, [[L3 Exploring Quantitative Data#QQ-plots|QQ-plots]], skewness, kurtosis, and formal Normality tests (Shapiro-Wilk).

##### R code
```R
library(lattice)
histogram(~viscera | gender, data=abl, type="count")
qqnorm(y, main="Female Abalones"); qqline(y)
qqnorm(x, main="Male Abalones"); qqline(x)

library(DescTools)
aggregate(viscera ~ gender, data=abl, Skew, method=1)
## gender viscera
## 1 F 0.4060918
## 2 M 0.2482997

aggregate(viscera ~ gender, data=abl, Kurt, method=1)
## gender viscera
## 1 F -0.2431501
## 2 M 1.1660593

shapiro.test(x)
## W = 0.96779, p-value = 0.1878
```

##### Python code
```python
abl.groupby("gender").skew()
## viscera
## gender
## F 0.418761
## M 0.256046

for i, df in abl.groupby('gender'):
    print(f"{df.gender.iloc[0]}: {df.viscera.kurt():.4f}")
## F: -0.1390
## M: 1.4220

stats.shapiro(x)
## statistic=0.9677..., pvalue=0.1878...
```

Skewness is near 0 (symmetric-ish), kurtosis for males is moderately positive (slightly fatter-tailed). Shapiro-Wilk on the male group does not reject Normality ($p=0.19$). The female group's skewness is larger, but the formal tests also fail to reject $H_0$.

> Prof advocates graphical assessment over formal Normality tests — large samples reject almost always, and the bootstrap ([[L10 Simulation#Bootstrapping]]) sidesteps Normality anyway.

## Non-parametric two-sample test
> From [[L7 Two-sample Hypothesis Tests#Example 7.5 (Abalone Measurements)]]

Non-parametric analogue of the independent 2-sample t-test: the Wilcoxon Rank Sum (WRS) test, equivalent to the Mann-Whitney U test. No Normality required; only needs $n_1, n_2 \geq 10$ and continuous underlying distributions.

##### R code
```R
wilcox.test(x, y)
```

##### Python code
```python
wrs_out = stats.mannwhitneyu(x, y)

print(f"""Test statistic: {wrs_out.statistic:.3f}.
p-val: {wrs_out.pvalue:.3f}.""")
```

Conclusion is consistent with the t-test: no significant difference between the two groups.

Note: SAS reports a different-looking test statistic because it does not subtract the smallest possible rank sum from group 1. For $n_1 = 50$:
$$
1415.5 + \frac{50(50+1)}{2} = 2690.5
$$
p-values match across all three.

## Permutation test
> From [[L10 Simulation#Example 10.8 (Abalone Data)]]

Permutation tests make **no distributional assumptions** — useful when both Normality and the WRS sample-size requirement are questionable.

Procedure:
1. Compute the observed difference in group means as the test statistic.
2. Pool the observations, permute, re-split into groups of sizes $n_1, n_2$.
3. Compute the difference under the permutation.
4. Repeat ~1000+ times.
5. p-value = proportion of permuted differences at least as extreme (in absolute value) as the observed one.

##### R code
```R
d1 <- mean(x) - mean(y)
print(d1)
# [1] 0.01979

generate_one_perm <- function(x, y) {
  n1 <- length(x); n2 <- length(y)
  xy <- c(x, y)
  xy_sample <- sample(xy)
  mean(xy_sample[1:n1]) - mean(xy_sample[-(1:n1)])
}
sampled_diff <- replicate(2000, generate_one_perm(x, y))
hist(sampled_diff)

(p_val <- 2 * mean(sampled_diff > d1))
# [1] 0.369
```

The permutation p-value (~0.37) is consistent with both the t-test and WRS conclusions: no significant difference in viscera weight between male and female abalones.

---
See also: [[L7 Two-sample Hypothesis Tests]] · [[L10 Simulation]] · [[L3 Exploring Quantitative Data]]
