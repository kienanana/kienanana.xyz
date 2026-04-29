---
class: note
tags:
  - python
  - scipy
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 03:37:59
aliases:
---
# SciPy.stats Comprehensive Reference

SciPy's statistics module provides a large number of probability distributions, summary statistics, and statistical tests. This is THE go-to library for statistical analysis in Python.

## IMPORTING


```python
from scipy import stats
import numpy as np
```

---

## PROBABILITY DISTRIBUTIONS

### The Four-Function Pattern

**Every distribution has 4 functions:**

- **`d`** → PDF/PMF (density/probability mass)
- **`p`** → CDF (cumulative probability)
- **`q`** → PPF (quantile/inverse CDF)
- **`r`** → Random sampling

**In scipy.stats, these are methods:**

- `.pdf()` or `.pmf()` → density/probability
- `.cdf()` → cumulative probability
- `.ppf()` → percent point function (quantile)
- `.rvs()` → random variates (samples)

### Normal Distribution


```python
from scipy.stats import norm

# PDF: probability density at x
norm.pdf(0, loc=0, scale=1)            # density at 0 for N(0,1)
norm.pdf(x, loc=mu, scale=sigma)       # density for N(μ,σ²)

# CDF: P(X ≤ x)
norm.cdf(1.96, loc=0, scale=1)         # P(Z ≤ 1.96) ≈ 0.975
norm.cdf(x, loc=mu, scale=sigma)       # P(X ≤ x) for N(μ,σ²)

# PPF: inverse CDF (quantiles)
norm.ppf(0.975, loc=0, scale=1)        # 97.5th percentile ≈ 1.96
norm.ppf(0.5, loc=0, scale=1)          # median = 0

# Random samples
norm.rvs(loc=0, scale=1, size=100)     # 100 random N(0,1) values
```

**Common shortcuts:**


```python
# Standard normal N(0,1) - can omit parameters
norm.pdf(0)                            # same as norm.pdf(0, 0, 1)
norm.cdf(1.96)                         # same as norm.cdf(1.96, 0, 1)
```

### Other Continuous Distributions


```python
from scipy.stats import uniform, expon, t, chi2, f

# Uniform [a, b]
uniform.pdf(x, loc=a, scale=b-a)
uniform.rvs(loc=0, scale=1, size=100)  # 100 values in [0,1]

# Exponential
expon.pdf(x, scale=1/lambda)           # rate = 1/scale
expon.rvs(scale=2, size=100)

# Student's t
t.pdf(x, df=10)                        # df = degrees of freedom
t.ppf(0.975, df=10)                    # 97.5th percentile

# Chi-square
chi2.pdf(x, df=5)
chi2.cdf(x, df=5)

# F-distribution
f.pdf(x, dfn=5, dfd=10)                # dfn, dfd = degrees of freedom
```

### Discrete Distributions


```python
from scipy.stats import binom, poisson, hypergeom

# Binomial
binom.pmf(k, n, p)                     # P(X = k) for Binomial(n, p)
binom.cdf(k, n, p)                     # P(X ≤ k)
binom.rvs(n, p, size=100)              # random samples

# Poisson
poisson.pmf(k, mu)                     # P(X = k) for Poisson(μ)
poisson.cdf(k, mu)                     # P(X ≤ k)

# Hypergeometric
hypergeom.pmf(k, M, n, N)              # pmf at k
# M = population size
# n = number of success states in population
# N = number of draws
```

**From lectures:** Hypergeometric for Fisher's exact test


```python
# Drawing without replacement
# M+N total balls (M of type 1, N of type 2)
# Drawing k balls
# X = number of type 1 balls drawn
hypergeom.pmf(w, M+N, M, k)
```

---

## DESCRIPTIVE STATISTICS

### Central Tendency & Spread


```python
stats.tmean(data)                      # trimmed mean
stats.gmean(data)                      # geometric mean
stats.hmean(data)                      # harmonic mean
stats.mode(data)                       # mode (most common value)
stats.variation(data)                  # coefficient of variation
```

### Robust Statistics


```python
# Trimmed mean — drop proportiontocut fraction from each tail before averaging
stats.trim_mean(data, proportiontocut=0.1)   # 10% trimmed mean (drops lowest/highest 10%)

# Interquartile range
stats.iqr(data)                              # IQR = Q3 - Q1

# Median absolute deviation (MAD)
stats.median_abs_deviation(data)             # MAD (scaled to be consistent with SD)
stats.median_abs_deviation(data, scale=1)    # raw MAD without scaling

# Winsorize — replace extremes with quantile values (from scipy.stats.mstats)
from scipy.stats.mstats import winsorize
winsorize(data, limits=[0.05, 0.05])         # clip bottom 5% and top 5%
# Returns a masked array; convert with .data or np.array()
```

**Usually just use NumPy:**


```python
np.mean(data), np.median(data), np.std(data)
```

### Distribution Shape


```python
stats.skew(data)                       # skewness
stats.kurtosis(data)                   # kurtosis (excess)
stats.moment(data, moment=3)           # 3rd moment
```

### Percentiles & Quantiles


```python
np.percentile(data, 50)                # 50th percentile (median)
np.percentile(data, [25, 75])          # Q1, Q3
np.quantile(data, 0.95)                # 95th quantile
```

---

## HYPOTHESIS TESTS

### One-Sample Tests

**One-Sample t-test:**


```python
# H₀: μ = μ₀
stats.ttest_1samp(data, popmean=0)
# Returns: TtestResult(statistic=..., pvalue=...)

result = stats.ttest_1samp(data, popmean=5)
print(f"t = {result.statistic:.4f}, p = {result.pvalue:.4f}")
```

**Shapiro-Wilk Test (Normality):**


```python
# H₀: data comes from normal distribution
stats.shapiro(data)
# Returns: ShapiroResult(statistic=..., pvalue=...)

# Small p-value → reject normality
```

### Two-Sample Tests

**Independent Samples t-test:**


```python
# H₀: μ₁ = μ₂
t_out = stats.ttest_ind(group1, group2)            # equal variance (pooled)
t_out = stats.ttest_ind(group1, group2, equal_var=False)  # Welch's (unequal var)

# Access results
t_out.statistic
t_out.pvalue
ci_95 = t_out.confidence_interval()   # returns (low, high) — newer API (L7)
```

**Paired t-test:**


```python
# H₀: μ_diff = 0 (for paired data)
stats.ttest_rel(before, after)
```

**Mann-Whitney U Test (Non-parametric, independent):**


```python
# H₀: distributions are same (Wilcoxon Rank-Sum / Mann-Whitney)
stats.mannwhitneyu(group1, group2)
```

**Wilcoxon Signed-Rank Test (Non-parametric, paired):**


```python
# H₀: median of differences is 0
# Non-parametric analogue of paired t-test
wsr_out = stats.wilcoxon(before, after,
                         correction=True,           # continuity correction
                         method='approx')           # normal approximation
print(f"statistic={wsr_out.statistic:.3f}, p={wsr_out.pvalue:.3f}")

# One-sided test
wsr_out = stats.wilcoxon(before, after, alternative='greater')  # H₁: before > after
# alternative: 'two-sided' (default), 'greater', 'less'

# Exact method (no ties, n < 16)
wsr_out = stats.wilcoxon(before, after, method='exact')
# Use method='approx' (normal approximation) when ties are present
```

**Kruskal-Wallis Test (Non-parametric, k groups):**


```python
# H₀: all groups follow the same distribution
# Non-parametric analogue of one-way ANOVA
# Requires n_i >= 5 for all groups

groups = [x[1] for x in df['value'].groupby(df['group'])]
kw_out = stats.kruskal(*groups)   # unpack list of arrays
print(f"statistic={kw_out.statistic:.3f}, p={kw_out.pvalue:.3f}")
```

**Levene's Test (Equal Variance):**


```python
# H₀: all groups have equal variance
stat, p = stats.levene(group1, group2, group3)
# Rule of thumb from lectures: if largest SD > 2× smallest SD → use Welch/non-parametric
```

### Categorical Data Tests

**Chi-Square Test of Independence:**


```python
from scipy.stats import chi2_contingency

# For contingency table
table = pd.crosstab(df['var1'], df['var2'])
chi2, p_value, dof, expected = chi2_contingency(table)

print(f"χ² = {chi2:.4f}")
print(f"p-value = {p_value:.4f}")
print(f"degrees of freedom = {dof}")
print(f"Expected frequencies:\n{expected}")
```

**From Exercise 4:**


```python
# Extract standardized residuals
observed = table.values
chi2, p, dof, expected = chi2_contingency(table)

# Calculate residuals
n = observed.sum()
row_margins = observed.sum(axis=1) / n
col_margins = observed.sum(axis=0) / n

# Standardized residuals formula from textbook:
# r_ij = (n_ij - μ_ij) / sqrt(μ_ij * (1 - p_i+) * (1 - p_+j))
std_residuals = (observed - expected) / np.sqrt(
    expected * (1 - row_margins[:, None]) * (1 - col_margins)
)
```

**Fisher's Exact Test (2×2 tables):**


```python
from scipy.stats import fisher_exact

# For 2×2 contingency table
table_2x2 = [[a, b], [c, d]]
oddsratio, p_value = fisher_exact(table_2x2)

print(f"Odds Ratio = {oddsratio:.4f}")
print(f"p-value = {p_value:.4f}")
```

**From Exercise 5:**


```python
# Fisher's test on political data (reduced to 2×2)
table_dem_rep = political_tab[['Dem', 'Rep']]
oddsratio, p_value = fisher_exact(table_dem_rep.values)

# Interpretation:
# OR > 1: first group has higher odds
# OR < 1: first group has lower odds
# OR = 1: no association (independence)
```

### Correlation Tests

**Pearson Correlation:**


```python
# H₀: ρ = 0 (no linear correlation)
r, p_value = stats.pearsonr(x, y)
print(f"Pearson r = {r:.4f}, p = {p_value:.4f}")
```

**Spearman Rank Correlation:**


```python
# H₀: ρ_s = 0 (no monotonic correlation)
rho, p_value = stats.spearmanr(x, y)
print(f"Spearman ρ = {rho:.4f}, p = {p_value:.4f}")
```

**Kendall's Tau:**


```python
# H₀: τ = 0 (no association)
tau, p_value = stats.kendalltau(x, y)
print(f"Kendall τ = {tau:.4f}, p = {p_value:.4f}")
```

**From lectures & Exercise 3:**


```python
# For categorical data (ordinal)
# Kendall's tau requires long format data
tau, p = stats.kendalltau(df['var1'], df['var2'])

# Kendall vs Goodman-Kruskal gamma:
# - Tau includes ties in denominator
# - Gamma ignores ties completely
# - Therefore |τ| ≤ |γ|
```

---

## NORMALITY TESTS & Q-Q PLOTS

### Normality Tests


```python
# Shapiro-Wilk (best for small samples, n < 50)
stat, p = stats.shapiro(data)

# Kolmogorov-Smirnov (for larger samples)
stat, p = stats.kstest(data, 'norm')                        # legacy interface

# 1-sample K-S test (preferred newer interface)
# Tests whether data comes from a specified distribution
result = stats.ks_1samp(data, stats.norm.cdf)               # vs standard normal
result = stats.ks_1samp(data, stats.norm(loc=mu, scale=sigma).cdf)  # vs N(μ,σ)
result.statistic; result.pvalue

# Anderson-Darling
result = stats.anderson(data, dist='norm')
```

### Q-Q Plot


```python
from scipy import stats
import matplotlib.pyplot as plt

# Basic Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()
```

**From Exercise 4:** Customized Q-Q plot


```python
fig, ax = plt.subplots(figsize=(10, 8))

# Create Q-Q plot
stats.probplot(residuals, dist="norm", plot=ax)

# Access and customize the plot elements
# ax.get_lines()[0] = data points
# ax.get_lines()[1] = reference line

ax.get_lines()[0].set_markerfacecolor('#e74c3c')
ax.get_lines()[0].set_markeredgecolor('black')
ax.get_lines()[0].set_markersize(12)

ax.get_lines()[1].set_color('#2c3e50')
ax.get_lines()[1].set_linewidth(2)
ax.get_lines()[1].set_linestyle('--')

ax.set_title('Q-Q Plot of Residuals')
ax.grid(True, alpha=0.3)
```

**Interpretation:**

- Points on line → data follows theoretical distribution
- S-shaped curve → skewness
- Curve up at ends → fat tails (heavier than normal)
- Curve down at ends → thin tails (lighter than normal)

---

## LINEAR REGRESSION


```python
from scipy.stats import linregress

# Simple linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Standard error: {std_err:.4f}")

# Make predictions
y_pred = slope * x + intercept
```

**From Tutorial 3:** Poisson-ness plot


```python
# Fit line to Poisson-ness plot
slope, intercept, _, _, _ = linregress(k, phi)
lambda_hat = np.exp(slope)
```

---

## NUMERICAL INTEGRATION


```python
from scipy import integrate

# integrate.quad — integrate a 1D function from a to b
result, error = integrate.quad(func, a, b)

# Examples:
result, _ = integrate.quad(lambda x: np.exp(2*x), 0, 1)   # ∫₀¹ e^(2x) dx
result, _ = integrate.quad(lambda x: x**2, 0, 3)           # ∫₀³ x² dx

# Monte Carlo alternative (E[h(X)] where X ~ Uniform(a,b)):
# mean(h(rng.uniform(a, b, n))) * (b - a)
```

---

## CONFIDENCE INTERVALS

### t-Confidence Interval for Mean


```python
# Manual calculation
from scipy.stats import t

mean = np.mean(data)
std = np.std(data, ddof=1)             # sample std (n-1)
n = len(data)
se = std / np.sqrt(n)

# 95% CI
alpha = 0.05
df = n - 1
t_crit = t.ppf(1 - alpha/2, df)
ci_lower = mean - t_crit * se
ci_upper = mean + t_crit * se

print(f"95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
```

### Bootstrap Confidence Intervals


```python
from scipy.stats import bootstrap

# Bootstrap CI for any statistic
def my_statistic(data):
    return np.median(data)

rng = np.random.default_rng()
res = bootstrap((data,), my_statistic, n_resamples=10000,
                random_state=rng, method='percentile')
print(f"95% CI: {res.confidence_interval}")
```

---

## WORKING WITH CONTINGENCY TABLES

### Complete Chi-Square Analysis


```python
from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np

# 1. Create contingency table
table = pd.crosstab(df['A'], df['B'])
print("Observed frequencies:")
print(table)

# 2. Perform chi-square test
chi2, p, dof, expected = chi2_contingency(table)

print(f"\nChi-square test:")
print(f"χ² = {chi2:.4f}")
print(f"p-value = {p:.6f}")
print(f"df = {dof}")

print(f"\nExpected frequencies:")
print(pd.DataFrame(expected, index=table.index, columns=table.columns))

# 3. Check assumptions
min_expected = expected.min()
print(f"\nMinimum expected count: {min_expected:.2f}")
if min_expected >= 5:
    print("✓ Chi-square assumption met (all expected ≥ 5)")
else:
    print("✗ Use Fisher's exact test instead")

# 4. Calculate Pearson residuals
residuals = (table.values - expected) / np.sqrt(expected)
print(f"\nPearson residuals:")
print(pd.DataFrame(residuals, index=table.index, columns=table.columns))

# 5. Interpret
print("\nInterpretation:")
print("Residuals > 2 or < -2 indicate significant deviation")
```

### Odds Ratio and Relative Risk (2×2 tables)


```python
# For 2×2 table:
#       B=0  B=1
# A=0    a    b
# A=1    c    d

a, b, c, d = table.iloc[0,0], table.iloc[0,1], table.iloc[1,0], table.iloc[1,1]

# Odds Ratio
OR = (a * d) / (b * c)
print(f"Odds Ratio = {OR:.4f}")

# Relative Risk (row-wise)
RR = (a / (a+b)) / (c / (c+d))
print(f"Relative Risk = {RR:.4f}")

# Log odds ratio CI (approximate)
se_log_or = np.sqrt(1/a + 1/b + 1/c + 1/d)
log_or = np.log(OR)
ci_lower = np.exp(log_or - 1.96 * se_log_or)
ci_upper = np.exp(log_or + 1.96 * se_log_or)
print(f"95% CI for OR: [{ci_lower:.4f}, {ci_upper:.4f}]")
```

**Interpretation:**

- OR = 1, RR = 1: No association
- OR > 1, RR > 1: Positive association (first group has higher odds/risk)
- OR < 1, RR < 1: Negative association (first group has lower odds/risk)
- OR ≈ RR when probabilities are small (rare events)

---

## SPECIAL FUNCTIONS

### Gamma Function & Factorials


```python
from scipy.special import gammaln, factorial

# Log of factorial (for large n)
gammaln(n + 1)                         # ln(n!)
# More stable than np.log(factorial(n))

# Exact factorial (small n only)
factorial(5)                           # 120
```

**From Tutorial 3:** Poisson-ness plot


```python
# Computing φ_k = ln(k! * X_k / N)
phi = gammaln(k + 1) + np.log(Xk / N)
```

---

## COMMON STATISTICAL WORKFLOWS

### Workflow 1: Testing for Group Differences


```python
# 1. Check normality within groups
for group in [group1, group2]:
    stat, p = stats.shapiro(group)
    print(f"Shapiro-Wilk p-value: {p:.4f}")

# 2. Check equal variances
stat, p = stats.levene(group1, group2)
print(f"Levene's test p-value: {p:.4f}")

# 3. Choose appropriate test
if normality_ok and equal_var:
    result = stats.ttest_ind(group1, group2)
elif normality_ok and not equal_var:
    result = stats.ttest_ind(group1, group2, equal_var=False)
else:
    result = stats.mannwhitneyu(group1, group2)

print(f"Test p-value: {result.pvalue:.4f}")
```

### Workflow 2: Checking Model Assumptions


```python
# For linear regression residuals

# 1. Normality
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("Q-Q Plot of Residuals")
plt.show()

# 2. Shapiro-Wilk test
stat, p = stats.shapiro(residuals)
print(f"Normality test p-value: {p:.4f}")

# 3. Plot residuals vs fitted
plt.scatter(fitted, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
```

### Workflow 3: Categorical Association


```python
# 1. Create table
table = pd.crosstab(df['var1'], df['var2'])

# 2. Chi-square test
chi2, p, dof, expected = chi2_contingency(table)

# 3. Check assumptions
if expected.min() < 5:
    print("Use Fisher's exact test (for 2×2)")
    if table.shape == (2, 2):
        or_val, p_fisher = fisher_exact(table.values)
else:
    print("Chi-square test is valid")

# 4. Compute association measure
if ordinal_data:
    tau, p_tau = stats.kendalltau(df['var1'], df['var2'])
    print(f"Kendall's τ = {tau:.4f}, p = {p_tau:.4f}")
```

---

## IMPORTANT NOTES FROM LECTURES

### Distribution Differences: Python vs R

**Family of functions:**

- **R:** `dnorm`, `pnorm`, `qnorm`, `rnorm`
- **Python:** `norm.pdf`, `norm.cdf`, `norm.ppf`, `norm.rvs`

**Parameters:**

- **R:** `mean`, `sd` (standard deviation)
- **Python:** `loc`, `scale` (also standard deviation for normal)

### Test Output Format


```python
# Most scipy.stats tests return named tuples
result = stats.ttest_ind(group1, group2)

# Access by attribute name (recommended)
result.statistic
result.pvalue

# Or unpack (but less clear)
t_stat, p_val = stats.ttest_ind(group1, group2)
```

### Multiple Testing Correction


```python
from scipy.stats import false_discovery_control

# Benjamini-Hochberg procedure
p_values = [0.01, 0.04, 0.03, 0.002, 0.5]
rejected = false_discovery_control(p_values, method='bh')
# Returns boolean array: which tests to reject
```

---

## QUICK REFERENCE

### Most Used Functions


```python
# Distributions
norm.pdf(), norm.cdf(), norm.ppf(), norm.rvs()
binom.pmf(), poisson.pmf(), hypergeom.pmf()

# Hypothesis Tests
stats.ttest_1samp(), stats.ttest_ind(), stats.ttest_rel()
stats.chi2_contingency(), stats.fisher_exact()
stats.pearsonr(), stats.spearmanr(), stats.kendalltau()

# Normality
stats.shapiro(), stats.probplot()

# Regression
stats.linregress()

# Categorical
chi2_contingency(), fisher_exact()
```

### Test Selection Guide

|Data Type|Test|
|---|---|
|One group, test mean|`ttest_1samp()`|
|Two independent groups|`ttest_ind()`|
|Two paired groups|`ttest_rel()`|
|Two groups, non-normal|`mannwhitneyu()`|
|Two paired groups, non-normal|`wilcoxon()` (signed-rank)|
|Multiple groups (parametric)|`ols` + `sm.stats.anova_lm()` in statsmodels|
|Multiple groups (non-parametric)|`kruskal()`|
|Categorical 2×2|`fisher_exact()` or `chi2_contingency()`|
|Categorical r×c|`chi2_contingency()`|
|Correlation (linear)|`pearsonr()`|
|Correlation (monotonic)|`spearmanr()` or `kendalltau()`|
|Normality|`shapiro()` or Q-Q plot|

---

## COMMON MISTAKES

❌ **Forgetting degrees of freedom**


```python
t.ppf(0.975, 10)  # Need df!
```

❌ **Using wrong tail for p-value**


```python
# Two-tailed test (most common)
stats.ttest_ind(group1, group2)  # Already two-tailed

# One-tailed: need to divide p-value by 2
# But check direction first!
```

❌ **Confusing pmf and pdf**


```python
binom.pdf(k, n, p)   # WRONG! Use pmf for discrete
binom.pmf(k, n, p)   # Correct

norm.pmf(x)          # WRONG! Use pdf for continuous
norm.pdf(x)          # Correct
```

❌ **Not checking assumptions**


```python
# Always check expected counts for chi-square!
chi2, p, dof, expected = chi2_contingency(table)
if expected.min() < 5:
    print("Warning: chi-square may not be valid")
```