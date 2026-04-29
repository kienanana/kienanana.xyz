---
class: note
tags:
  - dataset
  - R
  - python
  - pandas
  - numpy
  - statsmodels
  - regression
  - residual-diagnostics
source:
related:
  - "[[L3 Exploring Quantitative Data]]"
  - "[[L9 Linear Regression]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L3 Exploring Quantitative Data]] (QQ-plots, scatterplot matrices) and [[L9 Linear Regression]]

Physical / compositional measurements on concrete mixtures. Columns include `Cement`, `Slag`, `Water`, `Comp.Strength`, `SLUMP.cm.`, and `FLOW.cm.` (the flow-test output). Used in [[L3 Exploring Quantitative Data]] for QQ-plots, scatterplot matrices, and correlation plots; used in [[L9 Linear Regression]] for simple and multiple regression modelling of flow.

Files: `data/concrete+slump+test/slump_test.data`

## QQ plots
> From [[L3 Exploring Quantitative Data#QQ-plots]]

QQ-plot of compressive strength against the standard Normal. Points on the line indicate Normality; systematic deviations at the tails indicate heavier/lighter tails than Normal.

##### R code
```R
qqnorm(concrete$Comp.Strength)
qqline(concrete$Comp.Strength)
```

##### Python code
```python
from scipy import stats
import statsmodels.api as sm

sm.qqplot(concrete.Comp_Strength, line="q");
```

## Scatterplots and correlation
> From [[L3 Exploring Quantitative Data#Scatterplot Matrices]]

A scatterplot matrix enables simultaneous inspection of all bivariate relationships among numeric variables. Pair it with a correlation heatmap to quantify what the eye sees.

##### R code
```R
col_to_use <- c("Cement", "Slag", "Comp.Strength", "Water", "SLUMP.cm.", "FLOW.cm.")
pairs(concrete[, col_to_use], panel = panel.smooth)

library(psych)
corPlot(cor(concrete[, col_to_use]), cex=0.8, cex.axis=0.6, show.legend = FALSE)
```

##### Python code
```python
pd.plotting.scatter_matrix(concrete[['Cement', 'Slag', 'Comp_Strength',
                                     'Water', 'SLUMP(cm)', 'FLOW(cm)']],
                           figsize=(12,12));

corr = concrete[['Cement', 'Slag', 'Comp_Strength', 'Water',
                 'SLUMP(cm)', 'FLOW(cm)']].corr()
corr.style.background_gradient(cmap='coolwarm_r')
```

The scatterplot panel uses a smoothed curve to detect non-linear patterns; the heatmap reveals clusters of highly-correlated inputs.

## Flow vs. Water (simple regression)
> From [[L9 Linear Regression#Example 9.3 (Concrete Data Model)]]

Model: $\text{Flow} = \beta_0 + \beta_1 \cdot \text{Water} + e$.

##### R code
```R
concrete <- read.csv("data/concrete+slump+test/slump_test.data")
names(concrete)[c(1,11)] <- c("id", "Comp.Strength")
lm_flow_water <- lm(FLOW.cm. ~ Water, data=concrete)
summary(lm_flow_water)

confint(lm_flow_water)
```

##### Python code
```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

concrete = pd.read_csv("../data/concrete+slump+test/slump_test.data")
concrete.rename(columns={'No':'id',
                         'Compressive Strength (28-day)(Mpa)':'Comp_Strength',
                         'FLOW(cm)': 'Flow'},
                inplace=True)
lm_flow_water = ols('Flow ~ Water', data=concrete).fit()
print(lm_flow_water.summary())
```

Fitted model: $\hat{Y} = -58.73 + 0.55 X$, with $R^2 = 0.3995$ (water explains ~40% of flow's variability). 95% CIs:
- $\beta_0$: (−85.08, −32.37)
- $\beta_1$: (0.42, 0.68)

**Interpretation:** each additional unit of Water is associated with an average increase of 0.55 units in Flow.

## Predicted means (confidence bands)
> From [[L9 Linear Regression#Example 9.5]]

Plotting $\widehat{E(Y|X)}$ with a confidence envelope over a grid of Water values shows how uncertainty in the fitted line widens away from $\bar{X}$.

##### R code
```R
new_df <- data.frame(Water = seq(160, 240, by = 5))
conf_intervals <- predict(lm_flow_water, new_df, interval="conf")

plot(concrete$Water, concrete$FLOW.cm., ylim=c(0, 100),
     xlab="Water", ylab="Flow", main="Confidence Bands for Flow vs. Water")
abline(lm_flow_water, col="red")
lines(new_df$Water, conf_intervals[,"lwr"], col="red", lty=2)
lines(new_df$Water, conf_intervals[,"upr"], col="red", lty=2)
legend("bottomright", legend=c("Fitted line", "Lower/Upper CI"),
       lty=c(1,2), col="red")
```

##### Python code
```python
import numpy as np

new_df = sm.add_constant(pd.DataFrame({'Water': np.linspace(160, 240, 10)}))
predictions_out = lm_flow_water.get_prediction(new_df)

ax = concrete.plot(x='Water', y='Flow', kind='scatter', alpha=0.5)
ax.set_title('Confidence Bands for Flow vs. Water');
ax.plot(new_df.Water, predictions_out.conf_int()[:, 0].reshape(-1),
        color='blue', linestyle='dashed');
ax.plot(new_df.Water, predictions_out.conf_int()[:, 1].reshape(-1),
        color='blue', linestyle='dashed');
ax.plot(new_df.Water, predictions_out.predicted, color='blue');
```

The bands are narrowest near $\bar{X} \approx 200$ and fan out toward the edges of the observed Water range.

## Flow vs. Water + Slag (multiple regression)
> From [[L9 Linear Regression#Example 9.6 (Concrete Data Multiple Linear Regression).]]

Adding a second predictor, Slag: $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + e$.

##### R code
```R
lm_flow_water_slag <- lm(FLOW.cm. ~ Water + Slag, data=concrete)
summary(lm_flow_water_slag)
```

##### Python code
```python
lm_flow_water_slag = ols('Flow ~ Water + Slag', data=concrete).fit()
print(lm_flow_water_slag.summary())
```

Fitted model: $\hat{Y} = -50.27 + 0.54 X_1 - 0.09 X_2$. Overall $F_1 = 49.17$, p ≈ $1.3 \times 10^{-15}$; individual $t$-tests are all significant. $R^2 = 0.50$; adjusted $R^2 = 0.49$ (which is the right statistic to watch when adding predictors).

## Residual Normality
> From [[L9 Linear Regression#Example 9.9 (Concrete Data Normality Check)]]

Check standardised residuals against Normal via histogram, QQ-plot, and formal tests.

##### R code
```R
r_s <- rstandard(lm_flow_water_slag)
hist(r_s)
qqnorm(r_s); qqline(r_s)

shapiro.test(r_s)
## W = 0.97223, p-value = 0.02882
ks.test(r_s, "pnorm")
## D = 0.08211, p-value = 0.491
```

##### Python code
```python
r_s = pd.Series(lm_flow_water_slag.resid_pearson)
r_s.hist()
```

There is mild left-skew (mostly from a thinner right tail). Shapiro rejects at 5%, KS does not — disagreement is normal for borderline cases. The model's *point estimates* remain valid (OLS is still least-squares optimal); only the hypothesis-test inferences lean on Normality.

## Residual plots
> From [[L9 Linear Regression#Example 9.10 (Concrete Data Residual Plots)]]

Plot standardised residuals against:
1. fitted values
2. each explanatory variable

Patterns we watch for: random scatter (good), trend vs. a new variable (include it), curvature (add a quadratic), funnel shape (heteroscedasticity — transform $Y$ or use WLS).

##### R code
```R
opar <- par(mfrow=c(1,3))
plot(x=fitted(lm_flow_water_slag), r_s, main="Fitted")
plot(x=concrete$Water, r_s, main="X1")
plot(x=concrete$Slag, r_s, main="X2")
par(opar)
```

Residuals vs. Water / Slag look OK, but residuals vs. fitted values show a slight funnel shape. Combined with the left-skew in the residual distribution, this suggests trying a square-transform of the response.

## Influential points
> From [[L9 Linear Regression#Example 9.11 (Concrete Data Influential Points)]]

Influence = how much a parameter estimate (or fitted value) changes when observation $i$ is deleted. Cook's distance > 1 flags potentially influential points.

##### R code
```R
infl <- influence.measures(lm_flow_water_slag)
summary(infl)
```

Six points appear to affect the covariance matrix of the parameter estimates noticeably. Standard practice is to refit with each flagged point removed and check whether the conclusions change.

---
See also: [[L3 Exploring Quantitative Data]] · [[L9 Linear Regression]]
