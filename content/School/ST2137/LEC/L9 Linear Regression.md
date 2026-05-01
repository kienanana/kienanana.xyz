---
class: note
tags:
  - y3s2
  - python
  - R
  - pandas
  - numpy
  - statsmodels
source:
related:
author:
date: 2026-04-15
updated: 2026-04-15 13:20:22
aliases:
---
## Introduction
Regression analysis is a technique for investigating and modelling the relationship between variables like X and Y, using X to estimate Y. In these cases, we refer to X as the *explanatory* or *independent variable*. It is also sometimes referred to as a predictor. Y is referred to as the *response* or *dependent variable*. 

Regression models are used for two primary purposes: 
1. to understand how certain explanatory variables affect the response variable. This aim is typically known as estimation, since the primary focus is on estimating the unknown parameters of the model. 
2. to predict the response variable for new values of the explanatory variables. this is referred to as prediction 

This course focuses on the estimation aim. 

#### Example 9.1 (Concrete Data: Flow on Water)
Recall that we first saw this dataset in [[L3 Exploring Quantitative Data]] 

![[Screenshot 2026-04-15 at 1.30.20 PM.png | 500]]

The fitted regression model here estimates the relationship between the output of the flow test, and the amount of water used to create the concrete. Note that trend in the scatterplot. In this topic, we will figure out how to estimate this line. 

#### Example 9.2 (Bike Rental Data)
In [[L6 Introduction to SAS]] we encountered data on bike rentals. Here we attempt to model the number of registered users on the number of casual users. 

![[Screenshot 2026-04-15 at 2.32.12 PM.png | 500]]

Contingent on whether the day is a working one or not, it does appear that the trendline is different. 

## Simple Linear Regression
### Formal Set-up 
The simple linear regression model is applicable when we have observations $(X_{i},Y_{i})$ for n individuals. For now, let's assume both the X and Y variables are quantitative. 

#### Equation 9.1
The simple linear regression model is given by
$$
Y_{i} = \beta_{0} + \beta_{1} X_{i} + e_{i} \tag{9.1}
$$
where:
- $\beta_{0}$ is the intercept term
- $\beta_{1}$ is the slope, and 
- $e_{i}$ is an error term, specific to each individual in the dataset 

#### Equation 9.2
$\beta_{0}$ and $\beta_{1}$ are unknown constants that need to be estimated from the data. There is an implicit assumption in the formulation of the model that there is a linear relationship between $Y_{i}$ and $X_i$ . In terms of distributions, we assume that the $e_{i}$ are iid Normal. 
$$
e_{i} \sim N(0,\sigma^2),\ i=1,\dots,n \tag{9.2}
$$
The constant variance assumption is also referred to as *homoscedasticity*. The validity of the above assumptions will have to be checked after the model is fitted. All in all, the assumptions imply that: 
1. $E(Y_{i}|X_{i})=\beta_{0}+\beta_{1}X_{i},\ for\ i=1,\dots,n$
2. $Var(Y_{i}|X_{i})=Var(e_{i})=\sigma^2,\ for\ i=1,\dots,n$
3. The $Y_{i}$'s are independent 
4. The $Y_i$'s are Normally distributed 

### Estimation
#### Equation 9.3
Before deploying or using the model, we need to estimate optimal values to use for the unknown $\beta_{0}$ and $\beta_{1}$ . We shall introduce the method of Ordinary Least Squares (OLS) for the estimation. Let us define the *error Sum of Squares* to be:
$$
SS_{E} = S(\beta_{0},\beta_{1}) = \sum_{i=1}^n (Y_{i}-\beta_{0}-\beta_{1}X_{i})^2 \tag{9.3}
$$
Then the OLS estimates of $\beta_{0}$ and $\beta_{1}$ are given by
$$
\operatorname*{arg\,min}_{\beta_0, \beta_1} \sum_{i=1}^{n} (Y_i - \beta_0 - \beta_1 X_i)^2
$$
The minimisation above can be carried out analytically, by taking partial derivative with respect to the two parameters and setting them to 0. 
$$
\begin{align}
\frac{\partial S}{\partial \beta_0}  
= -2 \sum_{i=1}^{n} (Y_i - \beta_0 - \beta_1 X_i) = 0  \\
\frac{\partial S}{\partial \beta_1}  
= -2 \sum_{i=1}^{n} X_i (Y_i - \beta_0 - \beta_1 X_i) = 0
\end{align}
$$
Solving and simplifying, we arrive at the following:
$$
\begin{aligned}
\hat{\beta}_1  
&= \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}  
{\sum_{i=1}^{n} (X_i - \bar{X})^2} \\
\hat{\beta}_0 &= \bar{Y} - \hat{\beta}_1 \bar{X}
\end{aligned}
$$
where $\bar{Y} = (1 / n) \sum_{i=1}^{n} Y_{i} \text{and}\bar{X} = (1 / n) \sum_{i=1}^{n} X_{i}$ 

If we define the following sums:
$$
\begin{aligned}  
S_{XY}  
&= \sum_{i=1}^{n} X_i Y_i  
- \frac{\left(\sum_{i=1}^{n} X_i\right)\left(\sum_{i=1}^{n} Y_i\right)}{n} \\
S_{XX}  
&= \sum_{i=1}^{n} X_i^2  
- \frac{\left(\sum_{i=1}^{n} X_i\right)^2}{n}
\end{aligned}
$$
then a form convenient for computation of $\hat{\beta_{1}}$ is 
$$
\hat{\beta_{1}} = \frac{S_{XY}}{S_{XX}}
$$
Once we have the estimates, we can use [[#Equation 9.1]] to compute fitted values for each observation. These correspond to our best guess of the mean of the distributions from which the observations arose: 
$$
\hat{Y_{i}} = \hat{\beta_{0}} + \hat{\beta_{1}}X_{i}\ ,\ i=1,\dots,n
$$
#### Equation 9.4
As always, we can form residuals as the deviations from fitted values. 
$$
\begin{align}
r_{i} = Y_{i}\ -\ \hat{Y_{i}} \tag{9.4}
\end{align}
$$
Residuals are our best guess at the unobserved error terms $e_{i}$ . Squaring the residuals and summing over all observations, we can arrive at the following decomposition, which is very similar to the one in the ANOVA model:
$$
\begin{aligned}  
\underbrace{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}_{SS_T}  
&=  
\underbrace{\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}_{SS_{Res}}  
+  
\underbrace{\sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2}_{SS_{Reg}}  
\end{aligned}
$$
where:
- $SS_T$ is known as the total sum of squares 
- $SS_{Res}$ is known as the residual sum of squares
- $SS_{Reg}$ is known as the regression sum of squares 

In our model, recall from [[#Equation 9.2]] that we had assumed equal variance for all our observations. We can estimate $\sigma^2$ with 
$$
\hat{\sigma^2} = \frac{SS_{Res}}{n-2}
$$
#### Equation 9.5 & 9.6
Our distributional assumptions lead to the following for our estimates $\hat{\beta_{0}}$ and $\hat{\beta_{1}}$ :
$$
\begin{align}
\hat{\beta_{0}} &\sim N(\beta_{0},\ \sigma^2(1 /n\ +\ \bar{X^2} /S_{XX})) \tag{9.5}  \\
\hat{\beta_{1}} &\sim N(\beta_{1},\ \sigma^2 / S_{XX}) \tag{9.6}
\end{align}
$$
The above are used to construct confidence intervals for $\beta_{0}$ and $\beta_{1}$ , based on t-distributions. 

## Hypothesis Test for Model Significance 
This is to test if the coefficient $\beta_{1}$ is significantly different from 0. It is essentially a test of whether it was worthwhile to use a regression model of the form in [[#Equation 9.1]] instead of a simple mean to represent the data. 
The null and alternative hypotheses are: 
$$
\begin{align}
H_{0} : \beta_{1} = 0 \\
H_{1} : \beta_{1} \neq 0
\end{align}
$$
#### Equation 9.7
The test statistic is 
$$
\begin{align}
F_{0} = \frac{SS_{Reg} /1}{SS_{Res} /(n-2)} \tag{9.7}
\end{align}
$$
#### Equation 9.8
Under the null hypothesis, $F_{0} \sim F_{1,n-2}$
It is also possible to perform this same test as a t-test, using the result earlier. The statement of the hypotheses is equivalent to the F-test. The test statistic:  
$$
T_{0} = \frac{\hat{\beta_{1}}}{\sqrt{ \hat{\sigma^2} /S_{XX} }} \tag{9.8}
$$
Under $H_{0}$, the distribution of $T_0$ is $t_{n-2}$. This t-test and the earlier F-test in this section are *identical*. It can be proved that $F_{0} = T^2_{0}$ ; the obtained *p-values will be identical*.

### Coefficient of Determination, $R^2$
The coefficient of determination $R^2$ is defined as  
$$
R^2 = 1 - \frac{SS_{Res}}{SS_{T}} = \frac{SS_{Reg}}{SS_{T}}
$$
It can be interpreted as the proportion of variation in $Y_i$, explained by the inclusion of $X_i$ . Since $0 \leq SS_{Res} \leq SS_{T}$ , we can easily prove that $0 \leq R^2 \leq 1$ . The larger the value of $R^2$ is, the better the model is.

When we get to the case of multiple linear regression, take note that simply including more variables in the model can increase $R^2$ . This is undesirable, it is preferable to have a parsimonious model (uses the minimum number of parameters necessary to explain a given phenomenon) that explains the response variable well. 

#### Example 9.3 (Concrete Data Model) 
In this example, we focus on the estimation of the model parameters for the two variables we introduced in [[#Example 9.1 (Concrete Data Flow on Water)]] 

##### R code 
```R
concrete <- read.csv("data/concrete+slump+test/slump_test.data")
names(concrete)[c(1,11)] <- c("id", "Comp.Strength")
lm_flow_water <- lm(FLOW.cm. ~ Water, data=concrete)
summary(lm_flow_water)
```

![[Screenshot 2026-04-15 at 6.13.21 PM.png | 600]] 

##### Python code 
```python
import pandas as pd
import numpy as np
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

![[Screenshot 2026-04-15 at 6.14.29 PM.png | 600]]

##### SAS output 
![[Screenshot 2026-04-15 at 6.14.56 PM.png | 500]]

From the output, we note that the *estimated model* for Flow (Y) against Water (X) is: 
$$
Y = -58.73\ +\ 0.55X
$$
The estimates are $\hat{\beta_{0}} = -58.73$ and $\hat{\beta_{1}} = 0.55$ . This is the precise equation that was plotted in Figure 9.1. The $R^2$ was labelled as "Multiple R-squared" in the R output. The value is 0.3995, which means that about 40% of the variation in Y is explained by X. 

A simple interpretation of the model is as follows: 
> For every 1 unit increase in Water, there is an average associated increase in Flow rate of 0.55 units.

To obtain confidence intervals for the parameters, we can use the following code in R. The Python summary already contains the confidence intervals. 

##### R code 
```R
confint(lm_flow_water)
```

![[Screenshot 2026-04-15 at 6.21.22 PM.png | 400]]

We can read off that the 95% Confidence Intervals are: 
- for $\beta_{0}$ : (-85.08, -32.37)
- for $\beta_{1}$: (0.42, 0.68) 

#### Example 9.4 (Bike Data F-test)
We shall fit a simple linear regression model to the bike data, *constrained to the non-working days*. 
Take note that in this example, in the R and Python output, we print an analysis of variance table instead of using the summary() methods. The latter provides coefficient estimates, but the former output only returns a sum-of-squares breakdown. 

##### R code 
```R
bike2 <- read.csv("data/bike2.csv")
bike2_sub <- bike2[bike2$workingday == "no", ]
lm_reg_casual <- lm(registered ~ casual, data=bike2_sub)
anova(lm_reg_casual)
```

![[Screenshot 2026-04-15 at 6.24.24 PM.png]]

##### Python code 
```python
bike2 = pd.read_csv("../data/bike2.csv")
bike2_sub = bike2[bike2.workingday == "no"]

lm_reg_casual = ols('registered ~ casual', bike2_sub).fit()
anova_tab = sm.stats.anova_lm(lm_reg_casual,)
anova_tab
```

![[Screenshot 2026-04-15 at 6.25.02 PM.png]]

##### SAS output 
![[Screenshot 2026-04-15 at 6.25.22 PM.png | 450]]

The output above includes the sum-of-squares that we need to perform the F-test outlined in [[#Hypothesis Test for Model Significance]]. From the output table, we can see that $SS_{Reg}$ = 237654556 and $SS_{Res}$ = 147386970. The value of $F_0$ for this dataset is 369.25. The p-value is extremely small (2 x 10^-16), indicating strong evidence against H_0, ie. that $\beta_{1} = 0$

If you observe carefully in [[#Example 9.3 (Concrete Data Model)]] , the output from R contains both the t-test for significance of $\beta_{1}$ and the F-test statistic based on sum-of-squares. The p-value in both cases is 8.10 x 10^-13.

In linear regression, we almost always wish to use the model to understand what the mean of future observations would be. In the concrete case, we may wish to use the model to understand how the Flow test output values change as the amount of Water in the mixture changes. This is because, based on our formulation 
$$
E(Y | X) = \beta_{0} + \beta_{1} X
$$
After estimating the parameters, we would have: 
$$
\widehat{E(Y|X)} = \hat{\beta_{0}} + \hat{\beta_{1}} X
$$
Thus we can vary the values of X to study how much the mean of Y changes. Here is how we can do so in the concrete model for data. 

#### Example 9.5 
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

![[Screenshot 2026-04-15 at 6.33.08 PM.png | 500]]

##### Python code 
```python
new_df = sm.add_constant(pd.DataFrame({'Water' : np.linspace(160,240, 10)}))

predictions_out = lm_flow_water.get_prediction(new_df)

ax = concrete.plot(x='Water', y='Flow', kind='scatter', alpha=0.5 )
ax.set_title('Confidence Bands for Flow vs. Water');
ax.plot(new_df.Water, predictions_out.conf_int()[:, 0].reshape(-1), 
        color='blue', linestyle='dashed');
ax.plot(new_df.Water, predictions_out.conf_int()[:, 1].reshape(-1), 
        color='blue', linestyle='dashed');
ax.plot(new_df.Water, predictions_out.predicted, color='blue');
```

![[Screenshot 2026-04-15 at 6.33.48 PM.png | 500]]

##### SAS output 
![[Screenshot 2026-04-15 at 6.34.13 PM.png | 550]]

The fitted line is the straight line formed using $\hat{\beta_{0}}$ and $\hat{\beta_{1}}$ . The dashed lines are 95% Confidence Intervals for E(Y|X), for varying values of X. They are formed by joining up the lower bounds and upper bounds separately. Notice how the limits get wider the further away we are from $\bar{X} \approx 200$.

## Multiple Linear Regression 
### Formal Setup 
When we have more than 1 explanatory variable, we turn to multiple linear regression - generalised version of what we have been dealing with so far. We would still have observed information from n individuals, but for each one, we now observe a vector of values:
$$
Y_{i},\ X_{1,i},\ X_{2,i},\dots,\ X_{p-1,i},\ X_{p,i} 
$$
#### Equation 9.9
In other words, we observe p independent variables and 1 response variable for each individual in our dataset. The analogous equation to [[#Equation 9.1]] is
$$
Y_{i} = \beta_{0} + \beta_{1} X_{1,i} + \dots + \beta_{p}X_{p,i} + e_{i} \tag{9.9}
$$
It is easier to write things with matrices for multiple linear regression: 
$$
\begin{aligned}  
\mathbf{Y} &=  
\begin{bmatrix}  
Y_1 \\  
Y_2 \\  
\vdots \\  
Y_n  
\end{bmatrix},  
\quad  
\mathbf{X} =  
\begin{bmatrix}  
1 & X_{1,1} & X_{2,1} & \cdots & X_{p,1} \\  
1 & X_{1,2} & X_{2,2} & \cdots & X_{p,2} \\  
\vdots & \vdots & \vdots & \ddots & \vdots \\  
1 & X_{1,n} & X_{2,n} & \cdots & X_{p,n}  
\end{bmatrix}, \\  
\\  
\boldsymbol{\beta} &=  
\begin{bmatrix}  
\beta_0 \\  
\beta_1 \\  
\vdots \\  
\beta_p  
\end{bmatrix},  
\quad  
\mathbf{e} =  
\begin{bmatrix}  
e_1 \\  
e_2 \\  
\vdots \\  
e_n  
\end{bmatrix}  
\end{aligned}
$$
With the above matrices, we can re-write [[#Equation 9.9]] as 
$$
\mathbf{Y} = \mathbf{X}\beta + \mathbf{e}
$$
We retain the same distributional assumptions as in [[#Formal Set-up]]

### Estimation 
Similar to [[#Estimation]], we can define $SS_{E}$ to be 
$$
SS_E = S(\beta_0, \beta_1, \ldots, \beta_p)  
= \sum_{i=1}^{n}  
\left( Y_i - \beta_0 - \beta_1 X_{1,i} - \cdots - \beta_p X_{p,i} \right)^2  
\tag{9.10}
$$
Minimising the above cost function leads to the OLS estimates:
$$
\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}
$$
The fitted values can be computed with
$$
\hat{\mathbf{Y}} = \mathbf{X}\hat{\boldsymbol{\beta}} 
= \mathbf{X}(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}
$$
Residuals are obtained as
$$
\mathbf{r} = \mathbf{Y} - \hat{\mathbf{Y}}
$$
Finally, we estimate $\sigma^2$ using
$$
\hat{\sigma}^2 
= \frac{SS_{\text{Res}}}{n - p}
= \frac{\mathbf{r}'\mathbf{r}}{n - p}
$$
### Coefficient of Determination
In the case of multiple linear regression, $R^2$ is calculated exactly as in simple linear regression, and its interpretation remains the same: 
$$
R^2 = 1 - \frac{SS_{Res}}{SS_{T}}
$$
However, note that $R^2$ can be inflated simply by adding more terms to the model (even insignificant terms). Thus, we use the adjusted $R^2$, which penalises the model for adding more and more terms to the model: 
$$
R^2_{adj} = 1 - \frac{SS_{Res} / (n-p)}{SS_{T} / (n-1)}
$$
### Hypothesis Tests 
The F-test in the multiple linear regression helps determine if our regression model provides any advantage over the simple mean model. The null and alternative hypotheses are: 
$$  
\begin{aligned}  
H_0 &: \beta_1 = \beta_2 = \cdots = \beta_p = 0 \\  
H_1 &: \beta_j \neq 0 \text{ for at least one } j \in \{1,2,\ldots,p\}  
\end{aligned}  
$$  
#### Equation 9.11
The test statistic is  
$$  
F_1 = \frac{SS_{\text{Reg}}/p}{SS_{\text{Res}}/(n - p - 1)} \tag{9.11}  
$$  
Under the null hypothesis, $F_0 \sim F_{p,n-p-1}$.  
It is also possible to test for the significance of individual $\beta$ terms, using a $t$-test. The output is typically given for all the coefficients in a table. The statement of the hypotheses pertaining to these tests is:  
$$  
\begin{aligned}  
H_0 &: \beta_j = 0 \\  
H_1 &: \beta_j \neq 0  
\end{aligned}  
$$  
However, note that these $t$-tests are partial because it should be interpreted as a test of the contribution of $\beta_j$, given that all other terms are already in the model.  
#### Example 9.6 (Concrete Data Multiple Linear Regression). 
In this second model for concrete, we add a second predictor variable, Slag. The updated model is  
$$  
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + e  
$$  
where $X_1$ corresponds to Water, and $X_2$ corresponds to Slag.

##### R code 
```R
lm_flow_water_slag <- lm(FLOW.cm. ~ Water + Slag, data=concrete)
summary(lm_flow_water_slag)
```

![[Screenshot 2026-04-21 at 4.23.49 PM.png | 450]]

##### Python code 
```python
lm_flow_water_slag = ols('Flow ~ Water + Slag', data=concrete).fit()
print(lm_flow_water_slag.summary())
```

![[Screenshot 2026-04-21 at 4.25.50 PM.png]]

##### SAS output 
![[Screenshot 2026-04-21 at 4.26.25 PM.png | 400]]

The F-test is now concerned with the hypotheses: 
$$
\begin{align}
H_{0} &: \beta_{1} = \beta_{2} = 0 \\
H_{1} &: \beta_{1} \neq 0 \text{ or } \beta_{2} \neq 0
\end{align}
$$
From the output above, we can see that $F_{1} = 49.17$, with a corresponding p-value of $1.3 \times 10^{-15}$ . The individual t-tests for the coefficients all indicate significant differences from 0. The final estimated model can be written as 
$$
Y = -50.27\ +\ 0.54X_{1}\ - 0.09X_{2}
$$
Notice that the coefficients have changed slightly from the model in [[#Example 9.3 (Concrete Data Model)]]. Notice also that we have an improved $R^2$ of 0.50. However, as we pointed out earlier, we should be using the adjusted $R^2$, which adjusts for the additional variable included. This value is 0.49. 

While we seem to have found a better model than before, we still have to assess if all the assumptions listed in [[#Formal Set-up]] have been met. We shall do so in the subsequent sections. 

## Indicator Variables 
### Including a Categorical Variable 
The explanatory variables in a linear regression model do not need to be continuous. Categorical variables can also be included in the model. In order to include them, they have to be coded using dummy variables.  

For instance, suppose that we wish to include gender in a model as $X_3$. There are only two possible genders in our dataset: Female and Male. We can represent $X_3$ as an indicator variable, with  
$$  
X_{3,i} =  
\begin{cases}  
1 & \text{individual } i \text{ is male} \\  
0 & \text{individual } i \text{ is female}  
\end{cases}  
$$  
The model (without subscripts for the $n$ individuals) is then:  
$$  
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + e  
$$  
For females, the value of $X_3$ is 0. Hence the model reduces to  
$$  
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + e  
$$  
On the other hand, for males, the model reduces to  
$$  
Y = (\beta_0 + \beta_3) + \beta_1 X_1 + \beta_2 X_2 + e  
$$  
The difference between the two models is in the intercept. The other coefficients remain the same.  

In general, if the categorical variable has $a$ levels, we will need $a - 1$ columns of indicator variables to represent it. This is in contrast to machine learning models which use one-hot encoding. The latter encoding results in columns that are linearly dependent if we include an intercept term in the model.

#### Example 9.7 (Bike Data Working Day) 
In this example, we shall improve on the simple linear regression model from [[#Example 9.4 (Bike Data F-test)]]. 

##### R code 
```R
lm_reg_casual2 <- lm(registered ~ casual + workingday, data=bike2)
summary(lm_reg_casual2)
```

![[Screenshot 2026-04-21 at 5.03.07 PM.png | 500]]

##### Python code 
```python
lm_reg_casual2 = ols('registered ~ casual + workingday', bike2).fit()
print(lm_reg_casual2.summary())
```

![[Screenshot 2026-04-21 at 5.04.21 PM.png]]

##### SAS output 
![[Screenshot 2026-04-21 at 5.05.05 PM.png | 500]]

The estimated model is now  
$$  
Y = 605 + 1.72X_1 + 2330X_2  
$$  
But $X_2 = 1$ for working days and $X_2 = 0$ for non-working days. This results in two separate models for the two types of days:  
$$  
Y =  
\begin{cases}  
605 + 1.72X_1, & \text{for non-working days} \\  
2935 + 1.72X_1, & \text{for working days}  
\end{cases}  
$$  
We can plot the two models on the scatterplot to see how they work better than the original model.

![[Screenshot 2026-04-21 at 5.06.52 PM.png]]

The dashed line corresponds to the earlier model, from [[#Example 9.7 (Bike Data Working Day)]]. With the new model, we have fitted separate intercepts to the two days, but the same slope. The benefit of fitting the model in this way, instead of breaking up the data into two portions and a different model on each one is that we use the entire dataset to estimate the variability. 

If we wish to fit separate intercepts *and* slopes, we need to include an *interaction term*. 

## Interaction Term 
A more complex model arises from an interaction between two terms. Here, we shall consider an interaction between a continuous variable and a categorical explanatory variable. Suppose that we have three predictors: height ($X_1$), weight ($X_2$) and gender ($X_3$). As spelt out in Section 9.5.1, we should use indicator variables to represent $X_3$ in the model.  
If we were to include an interaction between gender and weight, we would be allowing for males and females to have separate coefficients for $X_2$. Here is what the model would appear as:  
$$  
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 X_2 X_3 + e  
$$  
Remember that $X_3$ will be 1 for males and 0 for females. The simplified equation for males would be:  
$$  
Y = (\beta_0 + \beta_3) + \beta_1 X_1 + (\beta_2 + \beta_4) X_2 + e  
$$  
For females, it would be:  
$$  
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + e  
$$  
Both the intercept and coefficient of $X_2$ are different now. Recall that in [[#Including a Categorical Variable]], only the intercept term was different.

#### Example 9.8 (Bike Data Working Day)
Finally, we include an interaction in the model, resulting in separate intercepts and slopes. 

##### R code 
```R
lm_reg_casual3 <- lm(registered ~ casual * workingday, data=bike2)
summary(lm_reg_casual3)
```

![[Screenshot 2026-04-21 at 6.07.31 PM.png | 450]]

##### Python code 
```python
lm_reg_casual3 = ols('registered ~ casual * workingday', bike2).fit()
print(lm_reg_casual3.summary())
```

![[Screenshot 2026-04-21 at 6.08.05 PM.png]]

##### SAS output 
![[Screenshot 2026-04-21 at 6.08.29 PM.png | 500]]

Notice that $R^2_{adj}$ has increased from 50.8% to 60.7%. The estimated models for each type of day are:  
$$  
Y =  
\begin{cases}  
1362 + 1.16X_1, & \text{for non-working days} \\  
2168 + 2.97X_1, & \text{for working days}  
\end{cases}  
$$  
Here is visualisation of the lines that have been estimated for each sub-group of day. This is the image that we had earlier on in [[#Example 9.2 (Bike Rental Data)]]. 

![[Screenshot 2026-04-21 at 6.10.20 PM.png | 500]]

## Residual Diagnostics 
Recall from [[#Equation 9.4]] that residuals are computed as 
$$
r_{i} = Y_{i}\ -\ \hat{Y_{i}}
$$
Residual analysis is a standard approach for identifying how we can improve a model. In the case of linear regression, we can use the residuals to asses if the distributional assumptions hold. We can also use residuals to identify influential points that are masking the general trend of other points. Finally, residuals can provide direction on how to improve the model. 

### Standardised Residuals 
It can be shown that the variance of the residuals is in fact not constant. Let us define the hat-matrix as  
$$  
\mathbf{H} = \mathbf{X}(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'  
$$  
The diagonal values of $\mathbf{H}$ will be denoted $h_{ii}$, for $i = 1, \ldots, n$. It can then be shown that  
$$  
\mathrm{Var}(r_i) = \sigma^2 (1 - h_{ii}), \quad \mathrm{Cov}(r_i, r_j) = -\sigma^2 h_{ij}  
$$  
As such, we use the standardised residuals when checking if the assumption of Normality has been met.  
$$  
r_{i,\text{std}} = \frac{r_i}{\hat{\sigma}\sqrt{1 - h_{ii}}}  
$$  
If the model fits well, standardised residuals should look similar to a $N(0,1)$ distribution. In addition, large values of the standardised residual indicate potential outlier points.

By the way, $h_{ii}$ is also referred to as the *leverage* of a point. It is a measure of the potential influence of a point (on the parameters, and future predictions). $h_{ii}$ is a value between 0 and 1. For a model with p parameters, the average $h_{ii}$ should be $p /n$ . We consider points for whom $h_{ii} > 2 \times p /n$ to be **high leverage points**.

### Normality 
#### Example 9.9 (Concrete Data Normality Check) 

##### R code 
```R
r_s <- rstandard(lm_flow_water_slag)
hist(r_s)
qqnorm(r_s)
qqline(r_s)
```

![[Screenshot 2026-04-21 at 6.27.41 PM.png]]

##### Python code 
```python
r_s = pd.Series(lm_flow_water_slag.resid_pearson)
r_s.hist()
```

![[Screenshot 2026-04-21 at 6.28.09 PM.png | 500]]

While it does appear that we have slightly left-skewed data, the departure from Normality seems to arise mostly from a thinner tail on the right. 

```R
shapiro.test(r_s)
##
## Shapiro-Wilk normality test
##
## data: r_s
## W = 0.97223, p-value = 0.02882
ks.test(r_s, "pnorm")
##
## Asymptotic one-sample Kolmogorov-Smirnov test
##
## data: r_s
## D = 0.08211, p-value = 0.491
## alternative hypothesis: two-sided
```

At the 5% level, the two Normality tests do not agree on the result either. In any case, we should keep in mind where Normality is needed most: in the hypothesis tests. The estimated model is still valid - it is still the best fitting line according to the least-squares criteria. 

### Scatterplots 
To understand the model fit better, a set of scatterplots are typically made. These are plots of standardised residuals (on the y-axis) against:
- fitted values 
- explanatory variables, one at a time 
- potential variables 

Residuals are meant to contain only the information that our model cannot explain. Hence, if the model is good, the residuals should only contain random noise. There should be no apparent pattern to them. If we find such a pattern in one of the above plots, we would have some clue as to how we could improve the model. 

We typically inspect the plots for the following patterns: 

![[Screenshot 2026-04-21 at 6.32.44 PM.png]]

*(left to right)*
1. A pattern lie this is ideal. Residuals are randomly distributed around zero; there is no pattern or trend in the plot. 
2. The second plot is something rarely seen. It would probably appear if we were to plot residuals against a *new* variable that is not currently in the model. If we observe this plot, we should then include this variable in the model. 
3. This plot indicates we should include a quadratic term in the model. 
4. The *wedge* (or *funnel*) shape indicates that we do not have *homoscedasticity*. The solution to this is either a transformation of the response or weighted least squares. 

#### Example 9.10 (Concrete Data Residual Plots) 
##### R code 
```R
opar <- par(mfrow=c(1,3))
plot(x=fitted(lm_flow_water_slag), r_s, main="Fitted")
plot(x=concrete$Water, r_s, main="X1")
plot(x=concrete$Slag, r_s, main="X2")
par(opar)
```

![[Screenshot 2026-04-21 at 6.36.24 PM.png]]

##### SAS Plots 
![[Screenshot 2026-04-21 at 6.36.41 PM.png]]

While the plots of residuals versus explanatory variables look satisfactory, the plot of the residual versus fitted values appears to have funnel shape. Coupled with the observations about the deviations from Normality of the residuals in [[#Example 9.6 (Concrete Data Multiple Linear Regression).]], we might want to try a square transform of the response. 

### Influential Points 
The influence of a point on the inference can be judged by how much the inference changes with and without the point. For instance to assess if point i is influential on coefficient j: 
1. Estimate the model coefficients with all the data points 
2. Leave out the observations $(Y_{i},X_{i})$ one at a time and re-estimate the model coefficients. 
3. Compare the $\beta$'s from step 2 with the original estimate from step 1. 

While the above method assesses influence on parameter estimates, Cook's distance performs a similar iteration to assess the influence on the fitted values. *Cook's distance values greater than 1*  indicate *possibly influential points*. 

#### Example 9.11 (Concrete Data Influential Points) 
##### R code 
```R
infl <- influence.measures(lm_flow_water_slag)
summary(infl)
```

![[Screenshot 2026-04-21 at 6.42.08 PM.png | 500]]

The set of 6 points above appear to be influencing the covariance matrix of the parameter estimates greatly. To proceed, we would typically leave these observations out one-at-a-time to study the impact on our eventual decision.

##### SAS Output
![[Screenshot 2026-04-21 at 6.44.57 PM.png]]




