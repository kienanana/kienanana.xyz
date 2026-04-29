---
class: note
tags:
  - dataset
  - R
  - python
  - pandas
  - numpy
  - scipy
  - SAS
  - quantitative
  - categorical
source:
related:
  - "[[L3 Exploring Quantitative Data]]"
  - "[[L6 Introduction to SAS]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L3 Exploring Quantitative Data]]

Portuguese secondary-school student performance records (UCI ML repo). The running example in [[L3 Exploring Quantitative Data]] focuses on `G3` (the final math grade). Other variables include:

- `Medu` — mother's education level (0–4, ordinal)
- `goout` — frequency of going out with friends (1–5)
- `Walc`, `Dalc` — weekend / weekday alcohol consumption
- `address`, `paid` — categorical (urban/rural, tuition yes/no)

File: `data/student/student-mat.csv` (semicolon-delimited).

## Numerical summaries
> From [[L3 Exploring Quantitative Data#Numerical Summaries]]

Basics: count, missing values, central tendency (mean/median), spread (sd, IQR, range).

##### R code
```R
stud_perf <- read.table("data/student/student-mat.csv", sep=";",
                        header=TRUE)
summary(stud_perf$G3)
sum(is.na(stud_perf$G3))
```

##### Python code
```python
import pandas as pd
stud_perf = pd.read_csv("data/student/student-mat.csv", delimiter=";")
stud_perf.G3.describe()
# stud_perf.G3.info()
```

**Conditioning on an explanatory variable** (mother's education):

```R
round(aggregate(G3 ~ Medu, data=stud_perf, FUN=summary), 2)
table(stud_perf$Medu)
```

```python
stud_perf[['Medu', 'G3']].groupby('Medu').describe()
```

**Interpretation notes:**
- mean ≈ median → roughly symmetric
- mean > median → likely right-skew (a few large values pulling mean up)
- mean < median → likely left-skew

## Histograms
> From [[L3 Exploring Quantitative Data#Histograms]]

What to look for: overall cluster pattern, suspected outliers, modality (uni-/bi-/multimodal), symmetry/skew.

##### R code
```R
hist(stud_perf$G3, main="G3 Histogram", xlab="G3 scores")

library(lattice)
histogram(~G3 | Medu, data=stud_perf, type="density",
          main="G3 scores, by Medu levels", as.table=TRUE)
```

##### Python code
```python
fig = stud_perf.G3.hist(grid=False)
fig.set_title('G3 histogram')
fig.set_xlabel('G3 scores');

stud_perf.G3.hist(by=stud_perf.Medu, figsize=(15,10),
                  density=True, layout=(2,3));
```

Conditioning on `Medu` gives a panel of histograms — useful to see whether `G3` shifts with the mother's education level.

## Density plots
> From [[L3 Exploring Quantitative Data#Density Plots]]

Kernel density estimate (KDE) — a smoothed alternative to a histogram:
$$
\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^n K \left( \frac{x - x_i}{h} \right)
$$
Bandwidth $h$ controls smoothness: too small → spiky; too large → over-smoothed.

##### R code
```R
densityplot(~G3, groups=Medu, data=stud_perf, auto.key=TRUE,
            main="G3 scores, by Medu", bw=1.5)
```

##### Python code
```python
import matplotlib.pyplot as plt

f, axs = plt.subplots(2, 3, squeeze=False, figsize=(15, 6))
out2 = stud_perf.groupby("Medu")

for y, df0 in enumerate(out2):
    tmp = plt.subplot(2, 3, y+1)
    df0[1].G3.plot(kind='kde')
    tmp.set_title(df0[0])
```

In R/lattice: `|` makes separate panels; `groups=` overlays on a single panel.

## Boxplots
> From [[L3 Exploring Quantitative Data#Boxplots]]

Boxplots skeletally summarise a distribution (Q1, median, Q3, whiskers, outliers) and are ideal for comparing across groups. Whisker reach: $Q_1 - 1.5 \cdot IQR$ to $Q_3 + 1.5 \cdot IQR$. Points outside are **suspected outliers**.

##### R code
```R
bwplot(G3 ~ goout, horizontal = FALSE, main="G3 scores, by goout",
       xlab="No. of times the student goes out per week",
       data=stud_perf)
```

##### Python code
```python
stud_perf.plot.box(column='G3', by='goout',
                   xlabel='No. of times student goes out per week');
```

## Kendall's tau (Walc and Dalc)
> From [[L6 Introduction to SAS#Example 6.10 (Kendall's Tau for Walc and Dalc)]]

Both `Walc` (weekend alcohol consumption) and `Dalc` (weekday alcohol consumption) are ordinal (1–5). Kendall's $\tau_b$ is the right measure of ordinal association (analogue of correlation for ordered categorical).

In SAS Studio: **Tasks > Tables > Table Analysis**, select the two variables, and check the Kendall's $\tau_b$ option. The output format is similar to R's `DescTools::Desc` — see the treatment under the [[Job satisfaction]] dataset.

See [[L4 Exploring Categorical Data#For Ordinal Variables]] and [[Gamma Tau]] for theory.

## Chi-squared test (address vs paid)
> From [[L6 Introduction to SAS#Example 6.9 (Chi-square Test for Independence)]]

Tests independence of `address` (urban/rural) and `paid` (took paid classes or not). In SAS Studio: **Tasks > Table Analysis**, select one as column, the other as row, and enable "Chi-square statistics" under OPTIONS.

See [[Chi-Square & Fisher]] for the formula and [[L4 Exploring Categorical Data#Chi-squared Test for Independence]] for the theory.

---
See also: [[L3 Exploring Quantitative Data]] · [[L6 Introduction to SAS]] · [[L4 Exploring Categorical Data]]
