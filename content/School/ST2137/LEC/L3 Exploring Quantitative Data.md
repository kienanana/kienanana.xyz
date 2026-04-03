---
tags:
  - python
  - R
  - numpy
  - pandas
  - matplotlib
  - scipy
class: note
source:
related:
author:
date: 2026-02-27
updated: 2026-02-26 16:54:13
aliases:
---

*also referred to as numerical data*

![[Pasted image 20260226110336.png]]


### Numerical Summaries:
1. basic information about the data eg. number of observations and missing values
2. measures of central tendency eg. mean, median 
3. measures of speed eg. standard deviation, IQR, range

##### R Code:

```R 
stud_perf <- read.table("data/student/student-mat.csv", sep=";",
header=TRUE)
summary(stud_perf$G3)

sum(is.na(stud_perf$G3))
```

![[Screenshot 2026-02-26 at 11.44.12 AM.png]]
##### Python Code:
```python
import pandas as pd
import numpy as np

stud_perf = pd.read_csv("data/student/student-mat.csv", delimiter=";")
stud_perf.G3.describe()

# stud_perf.G3.info()
```

![[Screenshot 2026-02-26 at 11.44.45 AM.png]]

##### R code
```R
round(aggregate(G3 ~ Medu, data=stud_perf, FUN=summary), 2)
```

![[Screenshot 2026-02-26 at 11.49.37 AM.png]]

```R
table(stud_perf$Medu)
```

![[Screenshot 2026-02-26 at 11.49.50 AM.png]]

##### Python code
```python
stud_perf[['Medu', 'G3']].groupby('Medu').describe()
```

![[Screenshot 2026-02-26 at 11.51.34 AM.png]]

Some things to note about numerical summaries:
- if the mean and median are close to each other, it indicates that the distribution of the data is close to symmetric 
- the mean is sensitive to outliers but the median is not
- when the mean is much larger than the median, it suggests that there could be a few very large observations. it has resulted in a right-skewed distribution. 
	- conversely, if the mean is much smaller than the median, we probably have a left-skewed distribution 


### Graphical Summaries:
#### Histograms
when we create a histogram, here are some things that we look for:
1. what is the overall pattern? does the data cluster together, or is there a gap such that one or more observations deviate from the rest?
2. are there any suspected outliers?
![[Screenshot 2026-02-26 at 2.13.42 PM.png | 300]]
3. does the data have a single mound or peak? if yes, then we have what is known as a unimodal distribution. data with two peaks are referred to as bimodal, and data with many peaks are referred to as multimodal.
![[Screenshot 2026-02-26 at 2.15.18 PM.png | 300]]
4. is the distribution symmetric or skewed?
![[Screenshot 2026-02-26 at 2.17.04 PM.png]]


##### R Code
```R
hist(stud_perf$G3, main="G3 Histogram", xlab="G3 scores")
```

##### Python Code
```python
fig = stud_perf.G3.hist(grid=False)
fig.set_title('G3 histogram')
fig.set_xlabel('G3 scores');
```

it is not useful to inspect a histogram in a silo. condition on explanatory variable and create separate histograms for each group. 

```R
library(lattice)
histogram(~G3 | Medu, data=stud_perf, type="density",
main="G3 scores, by Medu levels", as.table=TRUE)
```

![[Screenshot 2026-02-26 at 2.53.54 PM.png]]

```python
stud_perf.G3.hist(by=stud_perf.Medu, figsize=(15,10), density=True,
layout=(2,3));
```

![[Screenshot 2026-02-26 at 2.54.36 PM.png]]


#### Density Plots
histograms are not perfect - when using them, we have to experiment with the bin size since this could mask details about the data. it is also easy to get distracted by the blockiness of histograms. an alternative to histograms is the kernel density plot. essentially, this is obtained by smoothing the heights of the rectangles in a histogram.

suppose we have observed an iid sample x1, x2 ... xn from a continuous pdf f(⋅). then the kernel density estimate at x is given by:
$$
\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^n K \left( \frac{x - x_{i}}{h} \right)
$$
where:
- K is a density function. a typical choice is the standard normal. the kernel places greater weights on nearby points (to x)
- h is a bandwidth, which determines which of the nearest points are used. the effect is similar to the number of bins in a histogram 

##### R code
```R
densityplot(~G3, groups=Medu, data=stud_perf, auto.key = TRUE,
main="G3 scores, by Medu", bw=1.5)
```

![[Screenshot 2026-02-26 at 3.13.30 PM.png]]

##### Python code
```python
import matplotlib.pyplot as plt
f, axs = plt.subplots(2, 3, squeeze=False, figsize=(15,6))
out2 = stud_perf.groupby("Medu")

for y,df0 in enumerate(out2):
	tmp = plt.subplot(2, 3, y+1)
	df0[1].G3.plot(kind='kde')
	tmp.set_title(df0[0])
```

![[Screenshot 2026-02-26 at 3.14.48 PM.png]]


#### Boxplots
a boxplot provides a skeletal representation of a distribution. boxplots are very well suited for comparing multiple groups. here are the steps for drawing a boxplot:
1. determine Q1, Q2 and Q3. the box is made from Q1 and Q3. the median is drawn as a line or a dot within the box 
2. determine the max-whisker reach: Q3 + 1.5 x IQR; the min-whisker reach by Q1 - 1.5 x IQR
3. any data point that is out of the range from the min to max whisker reach is classified as a *potential outlier*
4. excluding the potential outliers, the maximum point determines the *upper whisker* and the minimum point determines the *lower whisker* of a boxplot 
> a boxplot helps us to identify the median, lower and upper quantiles and outlier(s)

![[Screenshot 2026-02-26 at 3.30.59 PM.png | 300]]

##### R code

```R
bwplot(G3 ~ goout, horizontal = FALSE, main="G3 scores, by goout",
		xlab="No. of times the student goes out per week",
		data=stud_perf)
```

![[Screenshot 2026-02-26 at 4.02.13 PM.png]]
##### Python code

```python
stud_perf.plot.box(column='G3', by='goout',
				xlabel='No. of times student goes out per week');
```

![[Screenshot 2026-02-26 at 4.02.45 PM.png]]


#### QQ-plots
a QQ-plot plots the standardised sample quantiles against the theoretical quantiles of a N(0,1) distribution. if the points fall on a straight line, then we say there is evidence that the data comes from a Normal distribution.

especially for unimodal datasets, the points in the middle will typically fall close to the line. the value of a QQ-plot is in judging if the tails of the data are fatter or thinner than the tails of the Normal.

![[Screenshot 2026-02-26 at 4.22.36 PM.png]]

##### R code
```R
qqnorm(concrete$Comp.Strength)
qqline(concrete$Comp.Strength)
```

![[Screenshot 2026-02-26 at 4.29.35 PM.png]]

##### Python code
```python
from scipy import stats
import statsmodels.api as sm
sm.qqplot(concrete.Comp_Strength, line="q");
```

![[Screenshot 2026-02-26 at 4.30.03 PM.png]]


#### Correlation
when we are studying two quantitative variables, the most common numerical summary to quantify the relationship between them is the correlation coefficient. 
suppose that x1, x2, ... xn and y1, ... , yn are two variables from a set of n objects or people. the sample correlation between these two variables is computed as:

$$
r = \frac{1}{n-1} \sum_{i=1}^{n} \frac{(x_{i} - \bar{x}) (y_{i} - \bar{y})}{s_{x}s_{y}}
$$
where sx and sy are the sample standard deviations. r is an estimate of the correlation between random variables X and Y.

a few things to note about the value r, which is also referred to as the Pearson correlation:
- r is always between -1 and 1
- a positive value for r indicates a positive association and a negative value for r indicates a negative association 
- two variables have the same correlation, no matter which one is coded as X and which is coded as Y 

![[Screenshot 2026-02-26 at 4.36.26 PM.png]]


#### Scatterplot Matrices
when we have multiple quantitative variables in a dataset, it is common to create a matrix of scatterplots. this allows for simultaneous inspection of bivariate relationships.

##### R code 

```R
col_to_use <- c("Cement", "Slag", "Comp.Strength", "Water", "SLUMP.cm.", "FLOW.cm.")
pairs(concrete[, col_to_use], panel = panel.smooth)
```

![[Screenshot 2026-02-26 at 4.39.22 PM.png]]

##### Python code 
```python
pd.plotting.scatter_matrix(concrete[['Cement', 'Slag',  'Comp_Strength', 'Water', 'SLUMP(cm)', 'FLOW(cm)']],
figsize=(12,12));
```

![[Screenshot 2026-02-26 at 4.41.43 PM.png]]

> the scatterplots allow a visual understanding of the patterns, but it is usually also good to compute the correlation of all pairs of variables

### Correlation Plot
##### R code 
```R
library(psych)
corPlot(cor(concrete[, col_to_use]), cex=0.8, cex.axis=0.6,
	show.legend = FALSE)
```

![[Screenshot 2026-02-26 at 4.52.14 PM.png]]

##### Python code 
```python
corr = concrete[['Cement', 'Slag', 'Comp_Strength', 'Water',
				'SLUMP(cm)', 'FLOW(cm)']].corr()
corr.style.background_gradient(cmap='coolwarm_r')
```

![[Screenshot 2026-02-26 at 4.53.11 PM.png]]

> heatmaps enable us to pick out groups of variables that are similar to one another. 


## stuff not in lec notes:

### On Lattice Plots:
- Conditioning (|) vs Grouping (groups=):
	- **|** creates **separate** panels (small multiples)
	- **groups=** OVERLAYS on same panel 

### Box Plot Construction:
1. find Q1, median, Q3 -> draw box 
2. calculate IQR = Q3 - Q1
3. upper boundary = Q3 + 1.5 x IQR
4. lower boundary = Q1 - 1.5 x IQR
5. whiskers go to **LARGEST / SMALLEST** points **WITHIN boundaries**
6. plot individual points beyond boundaries as suspected outliers 

note: after log transform, should RECOMPUTE Q1, Q3, IQR, boundaries 

### QQ-Plot interpretation:
**How to Construct:**
1. standardise data: `x_i = (y_i - mean) / sd`
2. order data: ascending x_i
3. compute empirical quantiles: x_i is the (i/n)-quantile
4. get theoretical normal quantiles: qnorm(i/n)
5. plot: theoretical (x-axis) vs empirical (y-axis)

**Reading the Plot:**
![[Pasted image 20260309172302.png]]

 ![[Screenshot 2026-03-09 at 5.45.50 PM.png]]
- how i make sense of this:
	- less extreme tails: (highs are lower than norm, lows are higher than norm): thinner tails 
	- more extreme tails: (highs are higher than norm, lows are lower than norm): fatter tails 

### On Density Plots:
**Bandwidth Problem:**
- bandwidth too small: spiky / noisy
- bandwidth too large: over-smoothed 
- play around with the bw until it agrees with your intuition 
**Boundary Problem:**
- density estimates can extend beyond where your data actually exists
- FIX:
	1. identify boundary point (eg. 0)
	2. reflect data around boundary 
	3. estimate density on extended data 
	4. **discard** reflected portion
	5. results in density that levels off nicely at boundary 
---
See also: [[Numpy Glossary]] · [[Pandas Glossary]] · [[Matplotlib Glossary]]
