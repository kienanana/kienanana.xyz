---
class: note
tags:
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 11:55:07
aliases:
---
# ST2137 — Exam & Tutorial Takeaways

---

## Part 1: Practice Paper Takeaways

### Indexing & Slicing

**Python** — `[start:stop:step]`, stop is **exclusive**:

```python
my_list[2:8:2]    # indices 2, 4, 6 → length 3
x['col'][1::2]    # every other element starting at index 1 (odd positions)
```

**R** — 1-based, inclusive on both ends. Negative index **removes** elements (opposite to Python):

```r
vec1[2:8][-2]     # 2:8 gives 7 elements, [-2] removes the 2nd → length 6
```

**NumPy column binding:**

- `np.hstack()` joins arrays horizontally (column-wise). Adding shape (2,1) to (2,2) → (2,3).
- `np.concatenate()` also works but requires `axis=1` explicitly.

---

### Know Your Data Type Before Indexing

A common trap: `json.load()` returns a Python **dictionary**, not a DataFrame. So `.iloc`, `.col_name` attribute access, and `.corrected_calls` all fail — use `x['key']` bracket access instead.

In R, know the difference between `[[1]]`, `$name`, and `[1:3]` for nested list access:

```r
hawker_ctr_raw[[1]][[2]]$STREETNAME   # nested list indexing
```

---

### Histograms & Density Plots

|Task|Python|R|
|---|---|---|
|Switch to density y-axis|`density=True`|`freq=FALSE`|
|Change KDE bandwidth|—|`bw=` in `density()`|
|Bin closure default|Left-closed `[a,b)`|Right-closed `(a,b]`|

The bin closure difference between Python and R produces visually different histograms from the same data — this has been tested directly. R closes on the right; Python closes on the left.

---

### Boxplots & Outliers — The IQR Rule

Log transforms **do not automatically remove outliers**. You must recompute the fence after transforming:

```
Upper fence = Q3_transformed + 1.5 × IQR_transformed
```

Since log is monotone, `log(Q1)`, `log(Q3)`, `log(max)` preserve order — but still check against the fence arithmetically.

Extract outlier rows in R using the `$out` element of the `boxplot()` return object:

```r
box_out <- boxplot(x)
outlier_rows <- df[df$col >= min(box_out$out), ]
```

---

### Robust Statistics

- **Winsorised mean** — extreme values are **replaced** with the γ-quantile boundary (not removed). Graph (b) ≠ graph (c).
- **Trimmed mean** — for a symmetric distribution (e.g. Normal), trimmed mean = μ. ✓
- `σ̂ = IQR/1.35` is only valid as a σ estimator **for Normal data** — False for arbitrary distributions.

```python
# Winsorised mean in Python
lower, upper = np.quantile(x, [0.1, 0.9])
x[x <= lower] = lower
x[x >= upper] = upper
x.mean()
```

---

### sapply vs lapply

- `lapply` → returns a **list**
- `sapply` → returns a **vector/matrix**

To repeat a no-argument function N times, use an anonymous wrapper:

```r
sapply(1:50, function(x) generate_compute())   # ✓ correct
sapply(1:50, generate_compute)                  # ✗ passes x as argument → error
sapply(1:50, generate_compute())                # ✗ generate_compute() is a call, not a function object
```

---

### Chi-Square & Fisher's Exact

Fisher's exact p-value uses `dhyper()`:

```r
dhyper(3, 4, 4, 4)   # P(top-left cell = 3) given fixed margins
```

Expected probability under H₀:

```r
chisq.test(tab)$expected[i, j] / N
# or equivalently: (row_total/N) * (col_total/N)
```

Always check `chisq_output.expected_freq` (Python) or `chisq.test()$expected` (R) — test is invalid if any expected count < 5.

---

### Odds Ratio in R

`OddsRatio()` from `DescTools` returns a vector: `[1]` is the OR, `[-1]` is the CI. Build nested list output by hand when required:

```r
output <- list(
  rural = list(or = or_rural[1], ci = or_rural[-1]),
  urban = list(or = or_urban[1], ci = or_urban[-1])
)
```

CI not containing 1 → significant association. Direction of OR can reverse between subgroups — always report and interpret both.

---

### pd.cut() for Binning

Standard pattern:

```python
df['age_cut'] = pd.cut(df.age, bins=np.arange(40, 96, 5))
df.groupby('age_cut')['outcome'].mean()
```

In R:

```r
stud_perf$letter_grade <- cut(stud_perf$G3,
  breaks = c(-Inf, 10, 12, 15, 18, 20),
  labels = c("F", "D", "C", "B", "A"))
```

---

### Common Errors to Avoid

|Error|Cause|Fix|
|---|---|---|
|`NameError: name 'pd' is not defined`|pandas not imported|`import pandas as pd`|
|`could not find function "corPlot"`|package loaded but not attached|`library(psych)`|
|`KeyError: '0'` in `.loc`|using string `'0'` on integer index|match the index type|
|`unused argument (X[[i]])` in sapply|passed function object that takes no args|wrap in anonymous function|

---

---

## Part 2: Tutorial Takeaways

### Tutorial 1 — R Basics & Matrix Operations

**Useful query patterns on a dataframe:**

```r
NROW(df); NCOL(df); dim(df)               # dimensions
sum(df$y > 100 & df$y < 200)              # count rows meeting condition
head(sort(df$y), n=3)                      # smallest 3
df$x[which.max(df$y)]                      # year of max value
```

**Matrix operations in R:**

```r
X <- cbind(1, df$x)                        # design matrix: column of 1s + x
y <- matrix(df$y, ncol=1)
beta_hat <- solve(t(X) %*% X) %*% t(X) %*% y   # OLS estimate: (X'X)^{-1} X'y
y_hat <- X %*% beta_hat                    # fitted values
```

`lm()` does this automatically — use `lm_output$coefficients` and fitted values from `lm_output$fitted.values`.

**Theil-Sen robust slope (median of pairwise gradients):**

```r
all_combn <- combn(n, 2)
# For each pair, compute (y2-y1)/(x2-x1), then take median
fit_slope <- median(all_slopes)
fit_intercept <- median(y) - median(x) * fit_slope
```

More robust than OLS when data has outliers.

**Replacing values by matching keys — `match()`:**

```r
matched_rows <- match(corrected_data$x, df1$x)
df1$y[matched_rows] <- corrected_data$y
```

`match(a, b)` returns the positions in `b` where each element of `a` is found.

---

### Tutorial 2 — Python Pandas & MLE

**Adding computed columns with a for loop using `iterrows()`:**

```python
for _, row in liv.iterrows():
    if row.GF > row.GA:
        result.append('W')
```

**Groupby iteration pattern:**

```python
for name, group in df.groupby('Opponent'):
    print(name, group['pts'].sum())
```

**Cumulative sum + np.where to find first threshold crossing:**

```python
liv['cumul_pts'] = liv.pts.cumsum()
id = np.where(liv.cumul_pts >= 40)
liv.iloc[id[0]].head(1)
```

**Slice operator summary (iloc):**

```python
liv.iloc[0:10, ]        # first 10 rows
liv.iloc[0:10:2, ]      # alternate rows from first 10
liv.iloc[0::2, [0,2,3]] # every alternate row, specific columns
liv.iloc[-5:, :]        # last 5 rows
liv.iloc[::-1, ]        # all rows reversed
```

**Grid search for MLE (when no closed form):**

```python
lam_range = np.arange(0.5, 2, 0.01)
ll_vals = y_bar - lam_range / (1.0 - np.exp(-lam_range))
lam_hat = lam_range[np.argmin(np.abs(ll_vals))]
```

**Iterative (fixed-point) MLE algorithm:**

```python
def trunc_pois(y, tol=1e-6):
    y_bar = y.mean()
    lam_old = y_bar
    while True:
        lam_new = y_bar * (1 - np.exp(-lam_old))
        if np.abs(lam_new - lam_old) < tol:
            break
        lam_old = lam_new
    return lam_new
```

---

### Tutorial 3 — Exploratory Data Analysis

**Correlation matrix:**

```python
df[['G1','G2','G3']].corr()
# Style with heatmap:
cor.style.background_gradient(cmap='coolwarm_r', axis=None, vmin=-1, vmax=1)
```

```r
library(psych)
corPlot(cor(df[, c('G1','G2','G3')]))
```

**Wide to long reshape (stacking multiple columns):**

```r
grade_score <- c(stud_perf$G1, stud_perf$G2, stud_perf$G3)
grade_type  <- rep(c("first","second","final"), each=395)
df2 <- data.frame(grade_type=grade_type, grade_score=grade_score)
```

```python
grade_type  = pd.Series(np.repeat(['first','second','final'], repeats=395))
grade_score = pd.Series(stud_perf.G1.to_list() + stud_perf.G2.to_list() + stud_perf.G3.to_list())
df2 = pd.DataFrame({'grade_score': grade_score, 'grade_type': grade_type})
```

**Overplotting solutions for scatter plots:**

```r
# Jitter: add small random noise
plot(x=df$G1, y=df$G3 + runif(n, -0.2, 0.2))

# Transparency:
red_new <- rgb(255, 0, 0, 64, maxColorValue=255)
plot(x=df$G1, y=df$G3, col=red_new, cex=1.6, pch=20)
```

**Computing IQR fences manually in Python:**

```python
iqr = np.quantile(df.col, 0.75) - np.quantile(df.col, 0.25)
upper_fence = np.quantile(df.col, 0.75) + 1.5 * iqr
outliers = df[df.col > upper_fence]
```

**Poisson-ness plot** — tests whether count data follows a Poisson distribution. Plot φ_k = log(k! × X_k / N) vs k. A straight line = consistent with Poisson. Slope = log(λ̂). In Python, `gammaln(k+1)` computes log(k!) efficiently. `lfactorial(k)` in R.

---

### Tutorial 4 — Categorical Data Analysis

**Full chi-square hypothesis test workflow (5 steps):**

1. State H₀: no association between the two variables
2. Significance level (usually 5%)
3. Compute χ² statistic
4. Compute p-value
5. Decision: reject/not reject H₀, state conclusion in context

```r
chisq.test(table(df$var1, df$var2))
```

```python
stats.chi2_contingency(pd.crosstab(df.var1, df.var2).to_numpy())
# Check: chisq_output.expected_freq — all must be ≥ 5
```

**Row-wise proportions from a contingency table:**

```r
prop_table <- table / rowSums(table)     # R: recycling fills column-wise, so this works
```

```python
prop_table = table / table.sum(axis=1).reshape((2,1))  # reshape to (2,1) for broadcasting
```

The R recycling rule and numpy broadcasting rule are tested here — R fills matrices **column-wise**, numpy repeats the dimension with fewer axes.

**Relative Risk vs Odds Ratio:**

- RR = p̂₁/p̂₂, range (0, ∞), value of 1 = no association
- When the outcome is rare (a << b and c << d), RR ≈ OR
- OR is symmetric — doesn't change whether you compute row-wise or column-wise. RR does change.

**Kendall's Tau-b to find strongest ordinal association:**

```r
for (i in 24:29) {
  tmp <- table(stud_perf[, c(i, 34)])
  assocs <- Desc(tmp, plotit=FALSE)[[1]]$assocs
  cat(names(stud_perf)[i], round(assocs[3,1], 3), "\n")
}
```

```python
for var in df.columns[23:29]:
    kt = stats.kendalltau(df.letter_grade, df[var])
    print(var, kt.statistic)
```

**Mosaic plot** — rectangle width = marginal distribution of X, height within each column = conditional distribution of Y|X. Shading indicates standardised residuals (blue = more than expected, red = less than expected).

```r
mosaicplot(table(df$Dalc, df$Walc), shade=TRUE)
```

**Mutual Information (MI):**

```
I(X,Y) = Σ P(X=i, Y=j) × log( P(X=i,Y=j) / (P(X=i)×P(Y=j)) )
```

- MI = 0 if X and Y are independent
- MI > 0: variables are associated; larger = stronger association
- Estimate probabilities using sample proportions from a contingency table
- Skip cells where P(X=i, Y=j) = 0 (log(0) is undefined)

Common mistakes to watch for when implementing MI (from tutorial):

- Using `ln()` which doesn't exist in R — use `log()` instead
- Computing joint probability as `pX * pY` (that assumes independence)
- Iterating over all rows instead of unique levels of each variable
- Dividing by `i + j` instead of `i * j` in the log ratio

---

### General Patterns Across All Tutorials

**`match()` in R** — finds positions of elements from one vector in another. Useful for update-by-key operations.

**`combn(n, 2)`** — generates all pairwise combinations. Returns a 2×C(n,2) matrix where each column is one pair. Used in Theil-Sen slope and similar combinatorial calculations.

**`sprintf()` for formatted output in R:**

```r
cat("Value is", sprintf("%.3f", x), "\n")
```

**`unname(coef(lm1)[2])`** — strips the name from a named vector element so it prints cleanly.

**`factor()` with explicit `levels=`** — controls display order in lattice/ggplot2 plots. Without it, R defaults to alphabetical order which may not match the intended sequence.

**Date parsing:**

```r
df$date <- as.Date(df$date)
```

```python
df['date'] = pd.to_datetime(df['date'])
```