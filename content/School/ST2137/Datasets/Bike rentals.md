---
class: note
tags:
  - dataset
  - SAS
  - R
  - python
  - pandas
  - numpy
  - statsmodels
  - regression
source:
related:
  - "[[L6 Introduction to SAS]]"
  - "[[L9 Linear Regression]]"
  - "[[L3 Exploring Quantitative Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L6 Introduction to SAS#Example 6.3 (Bike Rentals)]]

Daily bike-rental records with columns for season, working-day indicator, weather variables (humidity etc.), and rental counts split into **casual**, **registered**, and total (`cnt`). Used as the running example through [[L6 Introduction to SAS]] and revisited in [[L9 Linear Regression]] to model the relationship between registered and casual users.

File: `data/bike2.csv`

## Numerical summaries
> From [[L6 Introduction to SAS#Example 6.4 (5-number summaries)]]

In SAS Studio: **Tasks > Statistics > Summary Statistics**. Analysis variable `cnt`, classification variable `season`. Under options, check lower/upper quartiles and comparative boxplots.

**Observations:** median count is highest in fall, then summer, winter, spring. IQRs are similar (~2000) across seasons; spring's middle 50% is the most right-skewed.

## Scatterplot
> From [[L6 Introduction to SAS#Example 6.5 (Casual vs Registered Scatterplot)]]

In SAS: **Tasks > Graphs > Scatter Plot**. x = `casual`, y = `registered`, group = `workingday`.

**Observation:** two distinct relationships appear between casual and registered counts — one for working days and one for non-working days. This motivates the interaction model fit in [[L9 Linear Regression]].

## Histograms
> From [[L6 Introduction to SAS#Example 6.6 (Casual Users Distribution)]]

In SAS: **Tasks > Graphs > Histogram**. Analysis variable `casual`, group `workingday`, with Normal density overlaid.

**Observation:** right-skewed in both cases; non-working-day counts extend further (to ~3500).

## Boxplots
> From [[L6 Introduction to SAS#Example 6.7 (Boxplots for Casual Users, by Season)]]

In SAS: **Tasks > Box Plot**. Analysis variable `casual`, category `season`, subcategory `workingday`. To force calendar ordering:

```SAS
proc sgplot data=ST2137.BIKE2;
    vbox casual / category=season group=workingday grouporder=ascending;
    xaxis values=('spring' 'summer' 'fall' 'winter');
    yaxis grid;
run;
```

Re-running on a log scale (APPEARANCE tab) tames the skew and reveals the seasonal pattern more clearly.

## QQ plots
> From [[L6 Introduction to SAS#Example 6.8 (Normality Check for Humidity)]]

In SAS: **Tasks > Statistics > Distribution Analysis**. Analysis variable `hum`; under options add the Normal curve, kernel density estimate, and the Normal QQ-plot.

**Observation:** humidity values are close to Normal except for a single low observation.

For the theory behind QQ-plots, see [[L3 Exploring Quantitative Data#QQ-plots]].

## Chi-squared test
> From [[L6 Introduction to SAS#Example 6.9 (Chi-square Test for Independence)]]

Shown in the bike-rentals chapter but applied to the [[Student performance]] dataset (variables `address` vs `paid`). The workflow is: **Tasks > Table Analysis**, select one variable as column and another as row, check "Chi-square statistics" under OPTIONS.

See [[Chi-Square & Fisher]] for the formula and the general test, and [[L4 Exploring Categorical Data#Chi-squared Test for Independence]] for theory.

## Regression F-test
> From [[L9 Linear Regression#Example 9.4 (Bike Data F-test)]]

Fitting a simple linear regression of `registered` on `casual`, restricted to non-working days:

##### R code
```R
bike2 <- read.csv("data/bike2.csv")
bike2_sub <- bike2[bike2$workingday == "no", ]
lm_reg_casual <- lm(registered ~ casual, data=bike2_sub)
anova(lm_reg_casual)
```

##### Python code
```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

bike2 = pd.read_csv("../data/bike2.csv")
bike2_sub = bike2[bike2.workingday == "no"]

lm_reg_casual = ols('registered ~ casual', bike2_sub).fit()
anova_tab = sm.stats.anova_lm(lm_reg_casual)
print(anova_tab)
```

From the ANOVA table: $SS_{\text{Reg}} = 237{,}654{,}556$, $SS_{\text{Res}} = 147{,}386{,}970$, giving $F_0 = 369.25$ with p-value $\approx 2\times 10^{-16}$. Strong evidence against $H_0: \beta_1 = 0$ — the casual count is a significant predictor of registered count on non-working days.

## Registered vs. casual, by workday
> From [[L9 Linear Regression#Example 9.7 (Bike Data Working Day)]]

Adding the categorical `workingday` indicator (dummy coded) allows separate intercepts for the two day types while sharing a slope:

##### R code
```R
lm_reg_casual2 <- lm(registered ~ casual + workingday, data=bike2)
summary(lm_reg_casual2)
```

##### Python code
```python
lm_reg_casual2 = ols('registered ~ casual + workingday', bike2).fit()
print(lm_reg_casual2.summary())
```

Fitted model: $Y = 605 + 1.72 X_1 + 2330 X_2$, where $X_2 = 1$ on working days. This splits into:
$$
Y =
\begin{cases}
605 + 1.72 X_1, & \text{non-working days} \\
2935 + 1.72 X_1, & \text{working days}
\end{cases}
$$
The benefit vs. fitting two separate regressions is that the entire dataset is used to estimate the common variability.

## Interaction term
> From [[L9 Linear Regression#Example 9.8 (Bike Data Working Day)]]

To fit separate slopes **and** intercepts, include an interaction between `casual` and `workingday`:

##### R code
```R
lm_reg_casual3 <- lm(registered ~ casual * workingday, data=bike2)
summary(lm_reg_casual3)
```

##### Python code
```python
lm_reg_casual3 = ols('registered ~ casual * workingday', bike2).fit()
print(lm_reg_casual3.summary())
```

Adjusted $R^2$ rises from 50.8% to 60.7%. The fitted models are:
$$
Y =
\begin{cases}
1362 + 1.16 X_1, & \text{non-working days} \\
2168 + 2.97 X_1, & \text{working days}
\end{cases}
$$
On working days each additional casual user is associated with a much larger bump in registered users (2.97 vs. 1.16).

---
See also: [[L6 Introduction to SAS]] · [[L9 Linear Regression]] · [[L3 Exploring Quantitative Data]]
