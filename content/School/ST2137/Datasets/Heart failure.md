---
class: note
tags:
  - dataset
  - R
  - categorical
source:
related:
  - "[[L4 Exploring Categorical Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L4 Exploring Categorical Data#Conditional Density Plots]]

Heart-failure clinical records. Primary outcome is `DEATH_EVENT` (binary: died during follow-up or not). Explanatory variables include `age` (quantitative) and other clinical measures.

File: `data/heart+failure+clinical+records/heart_failure_clinical_records_dataset.csv`

## Conditional density plot
> From [[L4 Exploring Categorical Data#Conditional Density Plots]]

When the **response is categorical** and the explanatory variable is quantitative, it is not useful to make boxplots or histograms of the response. Instead, show how the probability of the event varies across the quantitative variable via a conditional density plot (or its discrete sibling, a spineplot).

##### R code
```R
data_path <- file.path("data", "heart+failure+clinical+records",
                       "heart_failure_clinical_records_dataset.csv")
heart_failure <- read.csv(data_path)

# Spineplot: widths proportional to the density of `age`,
# heights proportional to P(DEATH_EVENT | age-bin).
spineplot(as.factor(DEATH_EVENT) ~ age, data=heart_failure,
          ylab = "Death", xlab="Age", main="Proportion dying, by age")

# Conditional density plot: a smoothed version of the spineplot,
# showing P(DEATH_EVENT | age) as a continuous function of age.
cdplot(as.factor(DEATH_EVENT) ~ age, data=heart_failure,
       ylab = "Death", xlab="Age", main="Proportion dying, by age")
```

**What to read from the plot:** at each age, the vertical split gives the conditional probability of death — as age increases, the shaded region (death) grows, indicating a higher chance of death for older patients. The spineplot makes this discrete (per age-bin); `cdplot` renders it as a smooth curve.

Unlike a boxplot (which suits quantitative response / categorical predictor), or a histogram-by-group layout, the conditional density plot is the correct choice when **categorical is the response**.

---
See also: [[L4 Exploring Categorical Data]]
