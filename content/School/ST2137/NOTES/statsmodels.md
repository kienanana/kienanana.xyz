---
class: software
tags:
  - python
  - statsmodels
source:
related:
author:
date: 2026-04-22
updated: 2026-04-22 15:49:03
aliases:
---
## Statsmodels OLS - Useful Attributes & Methods
### Model Object
After fitting:
```python
lm = ols('y ~ x1 + x2', data=df).fit()
```
### Coefficients & Inference
```python
lm.params        # β estimates (Intercept, slopes)
lm.bse           # standard errors
lm.tvalues       # t-statistics
lm.pvalues       # p-values
lm.conf_int()    # confidence intervals for β
```
### Model Fit Metrics
```python
lm.rsquared
lm.rsquared_adj
lm.aic
lm.bic
lm.fvalue        # overall F-statistic
lm.f_pvalue      # p-value for overall F-test
```
### Residuals & Fitted Values
```python
lm.resid                     # raw residuals
lm.resid_pearson            # standardized residuals
lm.resid_studentized_internal
lm.fittedvalues             # predicted values
```
### Error Variance
```python
lm.mse_resid   # estimate of σ² (residual mean squared error)
lm.scale       # same as mse_resid
```
### Influence & Leverage
```python
influence = lm.get_influence()
influence.hat_matrix_diag              # leverage (h_ii)
influence.resid_studentized_external   # studentized residuals
influence.cooks_distance               # Cook’s distance
```
### ANOVA & Sums of Squares
```python
import statsmodels.api as sm
sm.stats.anova_lm(lm)
```
### Predictions
```python
pred = lm.get_prediction(new_data)
pred.predicted_mean
pred.conf_int()        # confidence intervals for mean response (2-col array)
pred.summary_frame()   # full table (mean, CI, etc.)
```

**Building a new_data frame for prediction (L9):**
```python
import statsmodels.api as sm
import numpy as np
import pandas as pd

# When formula API is used, just pass a DataFrame with the right column names:
new_df = pd.DataFrame({'Water': np.linspace(160, 240, 10)})
predictions_out = lm.get_prediction(new_df)

# Extract CI bounds (shape: n × 2)
lower = predictions_out.conf_int()[:, 0]
upper = predictions_out.conf_int()[:, 1]
fitted = predictions_out.predicted_mean
```
### Sample Information
```python
lm.nobs        # number of observations
lm.df_model    # number of predictors
lm.df_resid    # residual degrees of freedom
```
### Useful Inspection Trick
```python
dir(lm)
```
Scan for keywords like: resid, rsquared, mse, predict
### Mental Model
- Coefficients → `.params`
- Variance → `.mse_resid`
- Fit quality → `.rsquared`, `.aic`
- Diagnostics → `.get_influence()`
- Predictions → `.get_prediction()`

## Formula Syntax (L8, L9)
```python
from statsmodels.formula.api import ols

# ANOVA / one-way (categorical predictor)
lm = ols('org ~ type', data=heifers).fit()

# Multiple regression
lm = ols('Flow ~ Water + Slag', data=concrete).fit()

# Indicator variable (categorical covariate, separate intercepts)
lm = ols('registered ~ casual + workingday', bike2).fit()

# Interaction term (* includes both main effects + interaction)
lm = ols('registered ~ casual * workingday', bike2).fit()
# equivalent to: casual + workingday + casual:workingday
```

### Contrast Coding for Categorical Predictors
By default, statsmodels uses **treatment (reference-level) coding** — the first level alphabetically is dropped and becomes the baseline.

```python
# Explicit treatment contrast — set reference level manually
lm = ols('org ~ C(type, Treatment("Control"))', data=heifers).fit()

# Sum-to-zero contrast — coefficients are deviations from grand mean
lm = ols('org ~ C(type, Sum)', data=heifers).fit()
```

- **Treatment** (default): intercept = mean of reference group; each coefficient = difference from reference.
- **Sum**: intercept = grand mean; each coefficient = deviation of that group from grand mean. Matches the Σαᵢ = 0 constraint from L8.

## ANOVA Table (L8, L9)
```python
import statsmodels.api as sm

sm.stats.anova_lm(lm)         # type 1 (sequential)
sm.stats.anova_lm(lm, type=3) # type 3 (marginal) — use for unbalanced designs
```

## Q-Q Plot via statsmodels (L8)
```python
import statsmodels.api as sm

sm.qqplot(lm.resid, line="q", ax=ax)
# line="q": fits a line through the quartiles (equivalent to qqline in R)
```

## Multiple Comparisons — Tukey HSD (L8)
```python
import statsmodels.stats.multicomp as mc

cp = mc.MultiComparison(heifers.org, heifers.type)
tk = cp.tukeyhsd()
print(tk)
# Returns confidence intervals for all pairwise comparisons
# Adjusts for multiple testing — valid even when chosen after inspecting data

# Plot simultaneous confidence intervals
tk.plot_simultaneous()
# Each group gets a horizontal CI; groups whose CIs don't overlap differ significantly
```

## Manual Design Matrix (when not using formula API)
```python
import statsmodels.api as sm

# sm.add_constant() — prepend a column of 1s (the intercept) to X
X = sm.add_constant(x_array)     # adds 'const' column to DataFrame or array
lm = sm.OLS(y, X).fit()

# Useful when constructing X manually (e.g. custom polynomial or log transforms)
X = sm.add_constant(np.column_stack([x, x**2]))   # quadratic model
```

## Residual Diagnostics Pattern (L8, L9)
```python
import matplotlib.pyplot as plt

f, axs = plt.subplots(1, 2, figsize=(8, 4))
lm.resid.hist(ax=axs[0])
sm.qqplot(lm.resid, line="q", ax=axs[1])
plt.tight_layout()
```

