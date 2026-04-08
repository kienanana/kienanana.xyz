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
The F-test in a One-Way ANOVA indicates if all means are equal, but does not provide further insight into which particular groups differ. If we had specified beforehand that we wished to *test if two particular groups $i_1$ and $i_2$ had different means*, we could do so with a t-test. Here are the details to compute a Confidence Interval in this case: 
1. Compute the estimate of the difference between the two means: 
$$
\overline{Y_{i_{1}}}\ - \overline{Y_{i_{2}}}
$$
2. Compute the standard error of the above estimator: 
$$
\sqrt{ MS_{W}\ \left( \frac{1}{n_{i_{1}}} + \frac{1}{n_{i_{2}}} \right)  }
$$
3. Compute the 100(1 - $\alpha$) confidence interval as: 
$$
\overline{Y}_{i_1} - \overline{Y}_{i_2}
\;\pm\;
t_{n-k,\alpha/2}
\;\sqrt{
MS_W \left( \frac{1}{n_{i_1}} + \frac{1}{n_{i_2}} \right)
}
$$
> ! Important:
If you notice from the output in [[#Example 8.1 (Effect of Antibiotics)]], the rule-of-thumb regarding standard deviations has not been satisfied. The ratio of the largest to smallest standard deviations is slightly more than 2. Hence we should in fact switch to the non-parametric version of the test; the pooled estimate of the variance may not be valid. However, we shall proceed with
this dataset just to demonstrate the next few techniques, instead of introducing a new dataset.

#### Example 8.3 (Enrofloxacin vs Control) 
Let us attempt to answer question (2) from the earlier set of questinos in example 8.1 

##### R code 
```R
summary_out <- anova(heifers_lm)
est_coef <- coef(heifers_lm)
est1 <- unname(est_coef[3]) # coefficient for Enrofloxacin
MSW <- summary_out$`Mean Sq`[2]
df <- summary_out$Df[2]
q1 <- qt(0.025, df, 0, lower.tail = FALSE)

lower_ci <- est1 - q1*sqrt(MSW * (1/6 + 1/6))
upper_ci <- est1 + q1*sqrt(MSW * (1/6 + 1/6))
	cat("The 95% CI for the diff. between Enrofloxacin and Control is (",
		format(lower_ci, digits = 3), ",",
	format(upper_ci, digits = 3), ").", sep="")
```

![[Screenshot 2026-04-08 at 12.31.48 PM.png]]

##### Python code 
```python
est1  = heifer_lm.params.iloc[2] - heifer_lm.params.iloc[1]
MSW = heifer_lm.mse_resid
df = heifer_lm.df_resid
q1 = -stats.t.ppf(0.025, df)

lower_ci = est1 - q1*np.sqrt(MSW * (1/6 + 1/6))
upper_ci = est1 + q1*np.sqrt(MSW * (1/6 + 1/6))
print(f"""The 95% CI for the diff. between Enrofloxacin and control is
({lower_ci:.3f}, {upper_ci:.3f}).""") 
```

![[Screenshot 2026-04-08 at 12.36.38 PM.png | 600]]

##### SAS code 
In order to get SAS to generate the estimate, modify the default ANOVA code to include *clparm* in the *model* statement, and include the *estimate* statement. 

```SAS
proc glm data=ST2137.HEIFERS;
	class type;
	model org=type / clparm;
	means type / hovtest=levene welch plots=none;
	lsmeans type / adjust=tukey pdiff alpha=.05;
	estimate 'enro_vs_control' type 0 -1 1 0 0 0;
	output out=work.Oneway_stats r=residual;
	run;
quit;
```

![[Screenshot 2026-04-08 at 12.40.00 PM.png]]

As the confidence interval contains the value 0, the binary conclusion would be to not reject the null hypothesis at the 5% level. 

## Contrast Estimation 
A more **general** comparison, such as the *comparison of a collection of $l_1$ groups with another collection of $l_2$ groups*, is also possible. 

First, note that a **linear contrast** is any *linear combination of the individual group means* such that the *linear coefficients add up to 0*. In other words, consider L such that: 
$$
L = \sum_{i=1}^k c_{i} \overline{Y_{i}}, \text{ where } \sum_{i=1}^k c_{i} = 0
$$
Note that the comparison of two groups in [[#Comparing Specific Groups]] is a special case of this linear contrast: 
1. Compute the estimate of the contrast: 
$$
L = \sum_{i=1}^k c_{i} \overline{Y_{i}}
$$
2. Compute the standard error of the above estimator: 
$$
\sqrt{ MS_{W} \sum_{i=1}^k \frac{c^2_{i}}{n_{i}} }
$$
3. Compute the 100(1 - $\alpha$) confidence interval as: 
$$
L\ \pm\ t_{n-k,\ \alpha /2 }\ \times \sqrt{ MS_{W} \sum_{i=1}^k \frac{c^2_{i}}{n_{i}} }
$$

#### Example 8.4 (Comparing collection of groups) 
Let sub-group (A) consist of Ivermectin and Fenbendazole. Here is how we can compute a confidence interval for the difference between this sub-group and Enrofloxacin. 

##### R code 
```R
c1 <- c(-1, 0.5, 0.5)
n_vals <- c(6, 6, 6)
L <- sum(c1*est_coef[3:5])

#MSW <- summary_out[[1]]$`Mean Sq`[2]
#df <- summary_out[[1]]$Df[2]
se1 <- sqrt(MSW * sum( c1^2 / n_vals ) )

q1 <- qt(0.025, df, 0, lower.tail = FALSE)

lower_ci <- L - q1*se1
upper_ci <- L + q1*se1
cat("The 95% CI for the diff. between the two groups is (",
    format(lower_ci, digits = 2), ",", 
    format(upper_ci, digits = 2), ").", sep="")
```

![[Screenshot 2026-04-08 at 12.53.24 PM.png | 500]]

##### Python code 
```python
c1 = np.array([-1, 0.5, 0.5])
n_vals = np.array([6, 6, 6,])
L = np.sum(c1 * heifer_lm.params.iloc[2:5])

MSW = heifer_lm.mse_resid
df = heifer_lm.df_resid
q1 = -stats.t.ppf(0.025, df)
se1 = np.sqrt(MSW*np.sum(c1**2 / n_vals))

lower_ci = L - q1*se1
upper_ci = L + q1*se1
print(f"""The 95% CI for the diff. between the two groups is 
({lower_ci:.3f}, {upper_ci:.3f}).""") 
```

![[Screenshot 2026-04-08 at 12.55.21 PM.png | 500]]

##### SAS code 
```SAS
proc glm data=ST2137.HEIFERS;
	class type;
	model org=type / clparm;
	means type / hovtest=levene welch plots=none;
	lsmeans type / adjust=tukey pdiff alpha=.05;
	estimate 'group_A_vs_enro' type 0 0 -1 0.5 0.5 0;
	output out=work.Oneway_stats r=residual;
	run;
quit;
```

![[Screenshot 2026-04-08 at 12.55.56 PM.png | 600]]

## Multiple Comparisons 
The procedures in the previous two subsections correspond to contrasts that we had specified before collecting or studying the data. If instead, we wished to perform **particular comparisons after studying the group means**, or if we wish to **compute all pairwise contrasts**, then we need to *adjust for the fact that we are conducting multiple tests*. If we do not do so, the chance of making at least one false positive increases greatly. 

### Bonferroni 
The simplest method for correcting for multiple comparisons is to use the Bonferroni correction. Suppose we wish to perform m pairwise comparisons, either as a test or by computing confidence intervals. If we wish to *maintain the significance level of each test at $\alpha$,* then we should *perform each of the m tests or confidence intervals at* $\alpha /m$ . 

### TukeyHSD 
This procedure is known as Tukey's Honestly Significant Difference. It is designed to construct confidence intervals for **all** pairwise comparisons. For the same $\alpha$-level, Tuley's HSD method provides *shorter confidence intervals* than a Bonferroni correction for all pairwise comparisons. 

##### R code 
```R
TukeyHSD(aov(heifers_lm)), ordered = TRUE) 
```

![[Screenshot 2026-04-08 at 1.10.09 PM.png | 500]]

##### Python code 
```python
import statsmodels.stats.multicomp as mc 

cp = mc.MultiComparison(heifers.org, heifers.type)
tk = cp.tukeyhsd()
print(tk)
```

![[Screenshot 2026-04-08 at 1.11.07 PM.png | 500]]

##### SAS output 
![[Screenshot 2026-04-08 at 1.11.29 PM.png | 450]]

## Kruskal-Wallis Procedure 
If the *assumptions of the ANOVA procedure are not met*, we can turn to a *non-parametric version* - the Kruskal Wallis test. This latter procedure is a generalisation of the Wilcoxon Rank-Sum test for 2 independent samples. 

### Formal Set-up 
The test statistic compares the *average ranks in the individual groups*. If these are *close together*, we would be inclined to conclude the *treatments are equally effective*. 

The null hypothesis is that all groups follow the same distribution. The alternative hypothesis is that at least one of the groups' distribution differs from another by a location shift. We then proceed with: 

1. Pool the observations over all samples, thus constructing a combined sample of size N = $\sum n_{i}$. Assign ranks to individual observations, using average rank in the case of tied observations. Compute the rank sum $R_{i}$ for each of the k samples. 
2. If there are no ties, compute the test statistic as
$$
H = \frac{12}{N(N+1)} \sum_{i=1}^k \frac{R^2_{i}}{n_{i}} - 3(N+1)
$$
3. If there *are* ties, compute the test statistic as
$$
H^* = \frac{H}{1 - \frac{\sum_{j=1}^{g} (t_j^3 - t_j)}{N^3 - N}}
$$
	where $t_j$ refers to the number of observations with the same value in the j-th cluster of tied observations and g is the number of tied groups. 

Under $H_0$, the test statistic follows a $\chi^2$ distribution with k-1 degrees of freedom. 

> ! Important: 
> This test should only be used if $n_{1} \geq 5$ for all groups 

#### Example 8.5 (Kruskal-Wallis Test)
##### R code 
```R
kruskal.test(heifers$org, heifers$type)
```

![[Screenshot 2026-04-08 at 1.23.45 PM.png | 600]]

##### Python code 
```python
out = [x[1] for x in heifers.org.groupby(heifers.type)]
kw_out = stats.kruskal(*out)
print(f"""The test statistic is {kw_out.statistic:.3f},
the p-value is {kw_out.pvalue:.3f}.""")
```

![[Screenshot 2026-04-08 at 1.24.27 PM.png | 400]]

##### SAS output 
![[Screenshot 2026-04-08 at 1.24.49 PM.png | 500]]

## Summary 
This topic has introduced the one-way ANOVA model. While there are restrictive distributional assumptions, try to focus on the information the method conveys - it attempts to compare the *within-group variance* to the *between-group variance*. 

Try to avoid viewing statistical procedures as flowcharts. If an assumption does not hold, or a p-value is borderline significant, try to identify which points lead to the result being significant (or not). 

Even after reporting the p-value from the F-test, try to dig deeper to uncover which groups are the ones that are different from the rest. 

Finally, take note that we should specify the contrasts we wish to test / estimate upfront, even before collecting the data. Only the Tukey comparison method (HSD) is valid if we perform multiple comparisons after inspecting the data. 




