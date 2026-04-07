---
class: note
tags:
  - python
  - R
  - SAS
  - pandas
  - numpy
  - scipy
  - statsmodels
  - matplotlib
source:
related:
author:
date: 2026-04-07
updated: 2026-04-07 17:16:26
aliases:
---
## Introduction 
In the [previous topic]([[L7 Two-sample Hypothesis Tests]]), we learned how to run two-sample t-tests. The objective of these procedures is to compare the means from two groups. Frequently, however, the means of more than two groups need to be compared. 

In this topic, we introduce the *one-way analysis of variance (ANOVA)*. It generalises the t-test methodology to more than 2 groups. Hypothesis tests in the ANOVA frameworkrequire the assumption of Normality. When this does not hold, we turn to the *Kruskal-Wallis test* - a non-parametric version of ANOVA, to compare distributions between groups. 

While the F-test in ANOVA provides a determination of whether or not the group means are different, in practice, we would always want to follow up with specific comparisons between groups as well. This chapter covers how we can construct confidence intervals in those cases. 

#### Example 8.1 (Effect of Antibiotics) 
An experiment to explore the influence of antibiotics on the decomposition of dung organic material. 36 heifers were randomly assigned into six groups. 
Antibiotics of different types added to the feed for heifers of 5 of the groups. The remaining group served as a control group. 

![[Screenshot 2026-04-07 at 5.30.02 PM.png | 450]]

Compared to the control group, it does appear that the median organic weight of the dung from the other heifer groups is higher. The following table displays the mean, standard deviation and count from each group: 

![[Screenshot 2026-04-07 at 5.33.27 PM.png | 300]]

Observe that the Spiramycin group only yielded 4 readings instead of 6. Our goal in this topic is to apply a technique for assessing if group means are statistically different from one another. Here are the specific analyses that we shall carry out: 
1. is there any significant difference, at 5% level, between the mean decomposition level of the groups? 
2. at 5% level, is the mean level for Enrofloxacin different from the control group? 
3. pharmacologically speaking, Ivermectin and Fenbendazole are similar to each other. Let us call this sub-group (A). They work differently than Enrofloxacin. At 5% level, is there a significant difference between the mean from sub-group A and Enrofloxacin? 

## One-Way Analysis of Variance 
### Formal Set-up 
Suppose there are k groups with $n_i$ observations in the i-th group. The j-th observation in the i-th group will be denoated by Y_ij. In the One-Way ANOVA, we assume the following model: 
$$
Y_{ij} = \mu\ + \alpha_{i}\ + e_{ij},\ i=1,\dots,k,\ j=1,\dots,n_{i} \tag{8.1}
$$
- $\mu$ is a constant, representing the underlying mean of all groups taken together 
- $\alpha_{i}$ is a constant specific to the i-th group. it represents the difference between the mean of the i-th group and the overall mean 
- $e_{ij}$ represents random error about the mean $\mu + \alpha_{i}$ for an individual observation from the i-th group 

In terms of distributions, we assume that the $e_{ij}$ are iid from a Normal distribution with mean 0 and variance $\sigma^2$ . This leads to the following model for each observation: 
$$
Y_{ij} \sim N(\mu + \alpha_{i},\ \sigma^2) \tag{8.2}
$$
It is not possible to estimate both $\mu$ and all the k different $\alpha_{i}$'s, since we only have k observed mean values for the k groups. For identifiability purposes, we need to constrain the parameters. There are two common constraints used, and note that different software have different defaults: 
1. Setting $\sum_{i=1}^k \alpha_{i} = 0$ , or 
2. Setting the reference level $\alpha_{1}=0$ 

Continuing on from Equation 8.2, let us denote the mean for the i-th group as $\bar{Y_{i}}$ , and the overall mean of all observations as $\overline{\overline{Y}}$ . We can then write the deviation of an individual observation from the overall mean as: 
$$
Y_{ij} - \overline{\overline{Y}}  
=  
\underbrace{(Y_{ij} - \overline{Y}_i)}_{\text{within}}  
+  
\underbrace{(\overline{Y}_i - \overline{\overline{Y}})}_{\text{between}}  
\tag{8.3}
$$
The first term on the right of the above equation is the source of *within-group variability*. The second term on the right gives rise to *between-group variability*. 
> The intuition behind the ANOVA procedure is that if the between-group variability is large and the within-group variability is small, then we have evidence that the group means are different. 

If we square both sides of Equation 8.3 and sum over all observations, we arrive at the following equation, the essence of ANOVA: 
$$
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (Y_{ij} - \overline{\overline{Y}})^2
=
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (Y_{ij} - \overline{Y}_i)^2
+
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (\overline{Y}_i - \overline{\overline{Y}})^2
$$
The squared sums above are referred to as: 
$$
SS_{T} = SS_{W} + SS_{B}
$$
- $SS_T$ : Sum of Squares Total 
- $SS_W$ : Sum of Squares Within
- $SS_B$ : Sum of Squares Between 

In addition the following definitions are important for understanding the ANOVA output: 
1. **The Between Mean Square** 
$$
MS_{B} = \frac{SS_{B}}{k-1}
$$
2. **The Within Mean Square**
$$
MS_{W} = \frac{SS_{W}}{n-k}
$$
The mean squares are estimates of the variability between and within groups. The ratio of these quantities is the test statistic. 

### F-Test in One-Way ANOVA 
The null and alternative hypotheses are: 
$$
\begin{array}{l}
H_{0} : \alpha_{i} = 0 \text{ for all i} \\
H_{1} : \alpha_{i} \neq 0 \text{ for at least one i}
\end{array}
$$
The test statistic is given by 
$$
F = \frac{MS_{B}}{MS_{W}}
$$
Under $H_0$ , the statistic F follows an F distribution with k-1 and n-k degrees of freedom. 

### Assumptions 
These are the assumptions that will need to be validated
1. *The observations are independent of each other*. This is usually a characteristic of the design of the experiment, and is not something we can always check from the data 
2. *The errors are Normally distributed*. Residuals can be calculated as follows:
$$
Y_{ij} - \overline{Y_{i}}
$$
	The distribution of these residuals should be checked for Normality. 
3. *The variance within each group is the same*. In ANOVA, the $MS_W$ is a pooled estimate (across the groups) that is used; in order for this to be valid, the variance within each group should be identical. Just as in the 2-sample situation, we shall avoid separate hypotheses tests and proceed with the rule-of-thumb that if the ratio of the largest to smallest standard deviation is less than 2, we can proceed with the analysis. 

#### Example 8.2 (F-test for Heifers Data) 
We begin by applying the overall F-test to assess if there is any significant difference between the means. 

##### R code 
```R
heifers <- read.csv("data/antibio.csv")
u_levels <- sort(unique(heifers$type))
heifers$type <- factor(heifers$type,
					levels=u_levels[c(2, 1, 3, 4, 5, 6)])
heifers_lm <- lm(org ~ type, data=heifers)
anova(heifers_lm)
```

![[Screenshot 2026-04-07 at 6.37.19 PM.png | 500]]

##### Python code 
```python
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

heifers = pd.read_csv("data/antibio.csv")
heifer_lm = ols('org ~ type', data=heifers).fit()
anova_tab = sm.stats.anova_lm(heifer_lm, type=3,)
print(anova_tab)
```

![[Screenshot 2026-04-07 at 6.38.19 PM.png | 500]]

##### SAS output 
![[Screenshot 2026-04-07 at 6.38.53 PM.png | 500]]

At the 5% significance level, we reject the null hypothesis to conclude that the group means are significantly different from one another. This answers question (1) from [[#Example 8.1 (Effect of Antibiotics)]]. 
To extract the estimated parameters, we can use the following code: 

##### R code 
```R
summary(heifers_lm)
```

![[Screenshot 2026-04-07 at 6.40.59 PM.png | 500]]

##### Python code 
```python
print(heifer_lm.summary())
```

![[Screenshot 2026-04-07 at 6.41.44 PM.png]]

##### SAS output 
![[Screenshot 2026-04-07 at 6.42.10 PM.png | 400]]

When estimating, both R and Python set one of the $\alpha_{i}$ to be equal to 0. In the case of R, it is the coefficient for $Control$, since we set it as the first level in the factor. For Python, we can tell from the output that the constraint has been placed on the coefficient for $Alfacyp$ (since it is missing). 

However, all estimates of group means are identical. From the R output, we can compute that the estimate of the mean for the $Alfacyp$ group is: 
$$
2.603 + 0.292 = 2.895
$$
From the Python output, we can read off (the Intercept term) that the estimate for $Alfacyp$ is 
$$
2.895 + 0 = 2.895
$$

To *check the assumptions*, we can use the following code:

##### R code 
```R
r1 <- residuals(heifers_lm)
hist(r1)
qqnorm(r1); qqline(r1)
```

![[Screenshot 2026-04-07 at 6.49.59 PM.png]]
##### Python code 
```python
import matplotlib.pyplot as plt 

f,axs = plt.subplots(1, 2, figsize(8,4))
tmp = plt.subplot(121) 
heifer_lm.resid.hist();
tmp = plt.subplot(122) 
sm.qqplot(heifer_lm.resid, line="q", ax=tmp);
```

![[Screenshot 2026-04-07 at 6.51.28 PM.png | 600]]

For SAS, we have to create a new column containing the residuals in a temporary dataset before creating these plots. 

## Comparing Specific Groups 






