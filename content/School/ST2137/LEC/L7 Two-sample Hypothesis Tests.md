---
class: note
tags:
source:
related:
author:
date: 2026-03-31
updated: 2026-03-31 13:41:12
aliases:
---
## Introduction 
In this topic, we introduce the routines for a common class of hypothesis tests: the scenario of comparing the location parameter of two groups. This technique is commonly used in A/B testing to assess if an intervention has resulted in a significant difference between two groups.  

Hypothesis tests are routinely abused in many ways by investigators. Such tests typically require strong assumptions to hold, and can result in false positives or negatives. As such, it may be preferred to use confidence intervals to make an assessment of the significance of a result. In this topic, we introduce how the p-values can be obtained for these hypothesis tests. 

## Procedure for Significance Tests 
### Step 1: Assumptions 
In this step, we verify that the assumptions required for the test are valid. In some tests, this step is carried out at the end of the others, but it is always essential to perform. Some tests are very sensitive to the assumptions - this is the main reason that the class of [[L5 Robust Statistics|Robust Statistics]] was invented. 

### Step 2: State the hypotheses and significance level 
The purpose of hypothesis testing is to make an inferential statement about the population from which the data arose. This inferential statement is what we refer to as the hypothesis regarding the population. 

> NOTE: 
> A hypothesis is a statement about population, usually claiming that a parameter takes a particular numerical value or falls in a certain range of values. 

The hypothesis will be stated as a pair: The null hypothesis H0 and the alternative hypothesis H1. Both statements will involve the **population parameter** (not the data summary) of interest. 

For example, if we have a sample of observations from two groups A and B and we wish to assess if the mean of the populations is different, the hypotheses would be: 
$$
H_{0} : \mu_{A} = \mu_{B}
$$
$$
H_{1} : \mu_{A} \neq \mu_{B} 
$$
H0 is usually a statement that indicates "no difference", and H1 is *usually* the complement of H0. 

At this stage, it is also crucial to state the significance level of the test. The significance level corresponds to the Type I error of the test - the probability of rejecting H0 when in fact it was true. This level is usually denoted as 𝛼, and is usually taken to be 5%, but there is no reason to adopt this blindly. Think of the choice of 5% as corresponding to accepting an error rate of 1 in 20 - that's how it was originally decided upon by Fisher. 

> WARNING: 
> It is important to state the significance level at this stage because if it is chosen after inspecting the data, the test is no longer valid. This is because, after knowing the p-value, one could always choose the significance level such that it yields the desired decision. 

Example of one-tailed test: 
$$
H_{0} : \mu_{A} = \mu_{B}
$$
$$
H_{1} : \mu_{A} > \mu_{B} 
$$

### Step 3: Compute the Test Statistic 
The test statistic is usually a measure of how far the observed data deviates from the scenario defined by H0. Usually, the larger it is, the more evidence we have against H0. 

The construction of a hypothesis test involves the derivation of the exact or approximate distribution of the test statistic under H0. Deviations under the assumption could render this distribution incorrect. 

### Step 4: Compute the p-value 
The p-value quantifies the chance of observing such a test statistic, or one that is more extreme in the direction of H1, under H0. The distribution of the test statistic under H0 is used to compute this value between 0 and 1. A value closer to 0 indicates stronger evidence against H0. 

### Step 5: State your conclusion
If the p-value is less than the stated significance level, we conclude that we reject H0. Otherwise, we say that we do not reject H0. It is conventional to use this terminology (instead of saying "accept H1") since our p-value is obtained with respect to H0. 

## Confidence Intervals
Confidence intervals are an alternative method of inference for population parameters. Instead of yielding a binary reject / do-not-reject result, they return a confidence interval that contains the plausible values for the population parameter. Many confidence intervals are derived by inverting hypothesis tests, and almost all confidence intervals are of the form:
$$
\text{Sample estimate}\ \pm \text{margin of error} 
$$
For instance, if we observe x1, ... , xn from a Normal distribution, and wish to estimate the mean of the distribution, the 95% confidence interval based on the t distribution is 
$$
\bar{x}\ \pm\ t_{0.025,n-1} \times \frac{s}{\sqrt{n}}
$$
where:
- s is the sample standard deviation, and 
- t_0.025,n-1 is the 0.025-quantile from the t distribution with n-1 degrees of freedom

The formulae for many confidence intervals rely on asymptotic Normality of the estimator. However, this is an assumption that can be overcome with the technique of bootstrapping. 

Bootstrapping can also be used to sidestep the distributional assumptions in hypothesis tests, but the professor prefers confidence intervals to tests because they yield an interval, providing much more information than a binary outcome. 

## Parametric Tests 
Parametric tests are hypothesis tests that assume some form of distribution for the sample (or population) to follow. An example of such a test is the t-test, which assumes that the data originates from a Normal distribution. 

Conversely, nonparametric tests are hypothesis tests that do not assume any form of distribution for the sample. Unfortunately, since nonparametric tests are so general, they do not have a high discriminative ability - they have low power. In other words, if a dataset truly comes from a Normal distribution, using the t-test would be able to detect smaller differences between the groups better than a non-parametric test. 

In this section, we cover parametric tests for comparing the difference in mean between *two groups*. 

