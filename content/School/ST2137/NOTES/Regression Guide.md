---
class: note
tags:
  - statistics
  - revision
source:
related:
author:
date: 2026-04-27
updated: 2026-04-27
aliases:
---
## Step 1 — When to use regression

| Situation | Use |
|---|---|
| Continuous $Y$, one continuous $X$ | Simple linear regression |
| Continuous $Y$, multiple $X$s (continuous or categorical) | Multiple linear regression |
| Want to quantify the relationship / make predictions | Regression |
| Want to test if a group difference exists | t-test or ANOVA (regression with only dummy predictors is equivalent) |

> **Regression vs ANOVA:** ANOVA is a special case of regression where all predictors are categorical indicator variables. They give identical results.

---

## Step 2 — Interpreting Outputs

| Output | What it means |
|---|---|
| $\hat{\beta}_0$ (intercept) | Predicted $Y$ when all $X = 0$; often not directly meaningful |
| $\hat{\beta}_1$ (slope) | Change in predicted $Y$ for a 1-unit increase in $X$, holding others fixed |
| $R^2$ | Proportion of variance in $Y$ explained by the model; range $[0, 1]$ |
| Adjusted $R^2$ | $R^2$ penalised for number of predictors; use this to compare models of different sizes |
| F-test p-value | Tests if *at least one* predictor is useful; overall model significance |
| t-test p-value (per coefficient) | Tests if *that specific* $\hat{\beta}_j \neq 0$ |

> **$R^2$ vs Adjusted $R^2$:** $R^2$ always increases when you add a variable (even a useless one). Adjusted $R^2$ decreases if the new variable doesn't help enough. Use adjusted $R^2$ when comparing models.

---

## Step 3 — Categorical Predictors (Indicator Variables)

| Rule | Detail |
|---|---|
| A categorical variable with $a$ levels needs $a - 1$ dummy variables | One level is the *reference category* (absorbed into intercept) |
| Dummy coefficient interpretation | Difference in mean $Y$ between that level and the reference, holding other predictors fixed |
| Interaction term $X_2 \times X_3$ | Allows slope of $X_2$ to differ across levels of $X_3$ (or vice versa) |

> **Why $a - 1$ and not $a$?** Using all $a$ dummies causes perfect collinearity with the intercept — the model matrix becomes singular and $\hat{\beta}$ cannot be computed.

**Example — gender with reference = Female:**
$$\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \hat{\beta}_2 \cdot \mathbf{1}[\text{Male}]$$
- $\hat{\beta}_2 > 0$: males have higher predicted $Y$ than females on average

**Adding an interaction:**
$$\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \hat{\beta}_2 \cdot \mathbf{1}[\text{Male}] + \hat{\beta}_3 (X_1 \times \mathbf{1}[\text{Male}])$$
- Now the slope of $X_1$ is $\hat{\beta}_1$ for females, $\hat{\beta}_1 + \hat{\beta}_3$ for males

---

## Step 4 — Residual Diagnostics

**Always run these after fitting. The model is only valid if assumptions hold.**

```
Residuals vs Fitted values plot
│
├─ Random scatter around zero, no pattern → assumptions OK ✓
├─ Curved / U-shape → non-linearity; add polynomial term (X²)
├─ Funnel / wedge (variance increases with fitted values) → heteroscedasticity
│   └─ Fix: log-transform Y, or use weighted least squares
└─ Systematic trend remaining → missing variable; add it to the model

QQ-plot of standardised residuals
├─ Points on diagonal → Normality OK ✓
└─ Deviations → Normality violated; consider transformation or robust regression

Residuals vs each X variable
└─ Pattern remaining → that variable needs a non-linear term
```

> **Standardised residuals:** $r_{i,\text{std}} = r_i \,/\, (\hat{\sigma}\sqrt{1 - h_{ii}})$ where $h_{ii}$ is the leverage. Points with $|r_{i,\text{std}}| > 2$ or $3$ are potential outliers.

> **Leverage:** $h_{ii} > 2p/n$ flags a high-leverage point — extreme in $X$-space. High leverage alone is not a problem; high leverage *plus* large residual = influential point.

> **Cook's distance $> 1$:** the point is likely influential — removing it would substantially change $\hat{\beta}$. Investigate, but don't automatically delete.

---

## Step 5 — Assumption Summary

| Assumption | How to check |
|---|---|
| Linearity | Residuals vs fitted / residuals vs $X$ — no pattern |
| Normality of errors | QQ-plot of standardised residuals; Shapiro-Wilk |
| Homoscedasticity (equal variance) | Residuals vs fitted — no funnel shape |
| Independence of observations | Study design (not checkable from residual plots) |

---

## Step 6 — Quick Flowchart

```
Fit model → plot residuals vs fitted
│
├─ Random scatter → check QQ-plot of residuals
│   ├─ On diagonal → model OK; report R²_adj, coefficients, p-values
│   └─ Deviations → Normality violated; consider transformation
│
├─ Curved pattern → add X² term; refit
├─ Funnel pattern → transform Y (try log); refit
└─ Trend → add missing variable; refit

After refit → repeat diagnostics until residuals are clean
```

---

See also: [[L9 Linear Regression]] · [[Test Selection Guide]] · [[EDA Guide]]
