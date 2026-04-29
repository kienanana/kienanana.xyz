---
class: note
tags:
  - dataset
  - R
  - python
  - pandas
  - numpy
  - scipy
  - statsmodels
  - ANOVA
  - kruskal-wallis
source:
related:
  - "[[L8 ANOVA]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
  - Antibiotics
  - Dung decomposition
---
## Description
> From [[L8 ANOVA#Example 8.1 (Effect of Antibiotics)]]

An experiment on the influence of antibiotics on decomposition of dung organic material. 36 heifers were randomly assigned into **six groups**: five antibiotic types plus a control. The response is organic-material level (`org`).

File: `data/antibio.csv`. Categorical variable: `type`. Note that the *Spiramycin* group contains 4 readings (not 6).

Three research questions:
1. Are there any significant differences between group means at 5%?
2. Is the Enrofloxacin mean different from Control?
3. Is the mean of sub-group $A$ = {Ivermectin, Fenbendazole} different from Enrofloxacin?

## F-test
> From [[L8 ANOVA#Example 8.2 (F-test for Heifers Data)]]

One-way ANOVA decomposes the total sum of squares into between-group and within-group. The F-statistic $F = MS_B / MS_W$ tests whether any $\alpha_i \neq 0$.

##### R code
```R
heifers <- read.csv("data/antibio.csv")
u_levels <- sort(unique(heifers$type))
heifers$type <- factor(heifers$type,
                       levels=u_levels[c(2, 1, 3, 4, 5, 6)])   # Control first
heifers_lm <- lm(org ~ type, data=heifers)
anova(heifers_lm)
```

##### Python code
```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

heifers = pd.read_csv("data/antibio.csv")
heifer_lm = ols('org ~ type', data=heifers).fit()
anova_tab = sm.stats.anova_lm(heifer_lm, type=3)
print(anova_tab)
```

**Conclusion (Q1):** reject $H_0$ at 5% — group means are significantly different.

**Assumption caveat:** the prof's rule-of-thumb on equal variances (largest sd < 2× smallest) is not quite satisfied — strictly we should use the non-parametric Kruskal-Wallis. The chapter proceeds with ANOVA for pedagogical continuity.

### Residual Normality checks
```R
r1 <- residuals(heifers_lm)
hist(r1)
qqnorm(r1); qqline(r1)
```

### Parameter estimates (identifiability constraint)
```R
summary(heifers_lm)
```
R and Python differ in which level they set as the reference (coefficient = 0). R drops *Control* (because it was set as the first factor level); Python drops *Alfacyp* by default. All group-mean estimates are identical once you add back the reference's intercept, e.g., in R `2.603 + 0.292 = 2.895` gives the *Alfacyp* mean.

## Comparing two groups
> From [[L8 ANOVA#Example 8.3 (Enrofloxacin vs Control)]]

For a **pre-specified** comparison of two groups, build a CI using the pooled MSE from ANOVA:
$$
\bar{Y}_{i_1} - \bar{Y}_{i_2}
\pm t_{n-k,\alpha/2} \sqrt{MS_W \left( \frac{1}{n_{i_1}} + \frac{1}{n_{i_2}} \right)}
$$

##### R code
```R
summary_out <- anova(heifers_lm)
est_coef <- coef(heifers_lm)
est1 <- unname(est_coef[3])           # coefficient for Enrofloxacin
MSW  <- summary_out$`Mean Sq`[2]
df   <- summary_out$Df[2]
q1   <- qt(0.025, df, 0, lower.tail = FALSE)

lower_ci <- est1 - q1*sqrt(MSW * (1/6 + 1/6))
upper_ci <- est1 + q1*sqrt(MSW * (1/6 + 1/6))
cat("95% CI for Enrofloxacin - Control: (",
    format(lower_ci, digits=3), ",", format(upper_ci, digits=3), ").", sep="")
```

##### Python code
```python
from scipy import stats
import numpy as np

est1 = heifer_lm.params.iloc[2] - heifer_lm.params.iloc[1]
MSW  = heifer_lm.mse_resid
df   = heifer_lm.df_resid
q1   = -stats.t.ppf(0.025, df)

lower_ci = est1 - q1*np.sqrt(MSW * (1/6 + 1/6))
upper_ci = est1 + q1*np.sqrt(MSW * (1/6 + 1/6))
print(f"95% CI: ({lower_ci:.3f}, {upper_ci:.3f}).")
```

**Conclusion (Q2):** CI contains 0 → do not reject $H_0$; no significant difference between Enrofloxacin and Control at 5%.

## Contrasts
> From [[L8 ANOVA#Example 8.4 (Comparing collection of groups)]]

A linear contrast $L = \sum c_i \bar{Y}_i$ with $\sum c_i = 0$ generalises two-group comparisons to comparing one *collection* of groups against another. For sub-group $A$ = {Ivermectin, Fenbendazole} vs. Enrofloxacin, use $c = (-1, 0.5, 0.5)$.

$$
L \pm t_{n-k, \alpha/2} \sqrt{MS_W \sum_i \frac{c_i^2}{n_i}}
$$

##### R code
```R
c1 <- c(-1, 0.5, 0.5)
n_vals <- c(6, 6, 6)
L <- sum(c1 * est_coef[3:5])

se1 <- sqrt(MSW * sum(c1^2 / n_vals))
q1  <- qt(0.025, df, 0, lower.tail = FALSE)

lower_ci <- L - q1*se1
upper_ci <- L + q1*se1
cat("95% CI between group A and Enrofloxacin: (",
    format(lower_ci, digits=2), ",", format(upper_ci, digits=2), ").", sep="")
```

##### Python code
```python
c1 = np.array([-1, 0.5, 0.5])
n_vals = np.array([6, 6, 6])
L = np.sum(c1 * heifer_lm.params.iloc[2:5])

MSW = heifer_lm.mse_resid
df  = heifer_lm.df_resid
q1  = -stats.t.ppf(0.025, df)
se1 = np.sqrt(MSW * np.sum(c1**2 / n_vals))

lower_ci = L - q1*se1
upper_ci = L + q1*se1
print(f"95% CI between group A and Enrofloxacin: ({lower_ci:.3f}, {upper_ci:.3f}).")
```

> The contrast method is only valid for comparisons **pre-specified** before looking at the data. For post-hoc / all-pairwise comparisons, use Tukey's HSD (see [[L8 ANOVA#TukeyHSD]]).

## Kruskal-Wallis test
> From [[L8 ANOVA#Example 8.5 (Kruskal-Wallis Test)]]

Non-parametric analogue of one-way ANOVA; generalises the Wilcoxon Rank-Sum test to $k$ groups. Since the equal-variance rule of thumb was borderline here, Kruskal-Wallis is arguably the better analysis.

Requires $n_i \geq 5$ per group.

##### R code
```R
kruskal.test(heifers$org, heifers$type)
```

##### Python code
```python
out = [x[1] for x in heifers.org.groupby(heifers.type)]
kw_out = stats.kruskal(*out)
print(f"Statistic: {kw_out.statistic:.3f}, p-value: {kw_out.pvalue:.3f}.")
```

Under $H_0$, the test statistic follows $\chi^2_{k-1}$.

---
See also: [[L8 ANOVA]] · [[L7 Two-sample Hypothesis Tests]]
