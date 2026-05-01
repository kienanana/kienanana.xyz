---
class: note
tags:
  - y3s2
  - R
source:
related:
author:
date: 2026-03-10
updated: 2026-03-10 15:57:49
aliases:
---
## Useful Functions 
- `.cor(x,y,method="pearson")` 
	- default method = pearson
		- other methods: "spearman" and "kendall"
- `.aggregate(x~y, data=, FUN=summary)`
	- splits data into subsets, computes summary statistics for each, returns result in a convenient form
	- x grouped by y 
		- x: var you want to summarise
		- y: grouping var 
	- `summary` gives Min, Q1, Median, Mean, 3Q, Max
	- can also use FUN=sd, FUN=mean, FUN=Skew, etc.

## Hypothesis Tests (L7)
```r
# Independent two-sample t-test
t.test(x, y, var.equal=TRUE)     # pooled variance
t.test(x, y, var.equal=FALSE)    # Welch's (unequal variance)

# Paired t-test
t.test(before, after, paired=TRUE)

# Extract from result
t_out$statistic; t_out$p.value; t_out$conf.int

# Wilcoxon Rank-Sum (non-parametric, independent)
wilcox.test(x, y)

# Wilcoxon Signed-Rank (non-parametric, paired)
wilcox.test(before, after, paired=TRUE, exact=FALSE)

# Normality
shapiro.test(x)
qqnorm(x); qqline(x)
```

## Skewness & Kurtosis (L7, DescTools)
```r
library(DescTools)
aggregate(viscera ~ gender, data=abl, Skew, method=1)
aggregate(viscera ~ gender, data=abl, Kurt, method=1)
# method=1 → method-of-moments estimator (matches lectures)
```

## ANOVA (L8)
```r
# Fit model and get ANOVA table
heifers_lm <- lm(org ~ type, data=heifers)
anova(heifers_lm)      # SS breakdown + F-test
summary(heifers_lm)    # coefficient estimates + t-tests

# Factor levels matter — set them explicitly
heifers$type <- factor(heifers$type, levels=c("Control", "Alfacyp", ...))

# Residuals
r1 <- residuals(heifers_lm)
hist(r1); qqnorm(r1); qqline(r1)

# Tukey HSD (all pairwise, valid post-hoc)
TukeyHSD(aov(heifers_lm), ordered=TRUE)

# Kruskal-Wallis (non-parametric ANOVA)
kruskal.test(heifers$org, heifers$type)

# t-quantile for CI construction
qt(0.025, df, lower.tail=FALSE)   # returns positive critical value
```

## Linear Regression (L9)
```r
lm_out <- lm(Flow ~ Water, data=concrete)
lm_out <- lm(Flow ~ Water + Slag, data=concrete)         # multiple
lm_out <- lm(registered ~ casual + workingday, data=bike2)  # indicator var
lm_out <- lm(registered ~ casual * workingday, data=bike2)  # interaction

summary(lm_out)         # coefficients, R², F-test
anova(lm_out)           # SS decomposition
confint(lm_out)         # 95% CI for all β's

# Predictions with CI bands
new_df <- data.frame(Water = seq(160, 240, by=5))
conf_intervals <- predict(lm_out, new_df, interval="conf")
# Returns matrix with columns: fit, lwr, upr

# Residual diagnostics
r_s <- rstandard(lm_out)      # standardised residuals
fitted(lm_out)                  # fitted values
influence.measures(lm_out)      # leverage, Cook's distance etc.
```

## Simulation (L10)
```r
set.seed(2137)    # set seed for reproducibility

# Random variable generation
rnorm(n, mean=0, sd=1)
runif(n, min=0, max=1)
rgamma(n, shape=2, rate=3)       # or scale=1/rate
rpois(n, lambda=1.3)
rbinom(n, size=2, prob=0.3)

# Replicate a function call n times
replicate(2000, generate_one_test())

# Apply with type safety (faster than sapply for known output type)
vapply(1:2000, function(x) generate_one_test(), 1L)

# Vectorised if-else
ifelse(X >= 11000, 11000, floor(X) + (11000 - floor(X))*(-0.25))
```

## Bootstrap (L10, boot library)
```r
library(boot)

stat_fn <- function(d, i) {
  mean(d[i], trim=0.1)    # i = bootstrap indices
}
boot_out <- boot(data, stat_fn, R=1999, stype="i")
boot.ci(boot.out=boot_out, type=c("perc", "bca"))
# perc: percentile interval
# bca: bias-corrected and accelerated (more accurate)
```

---
Full reference: [[R Glossary]]
