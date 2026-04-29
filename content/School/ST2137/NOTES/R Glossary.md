---
class: note
tags:
  - R
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 03:29:20
aliases:
---
> Quick reference: [[R]]
## QUICK REFERENCE CARD

### Most Used Functions (Memorize!)


```r
# Reading
read.table(), read.csv()

# Inspection  
head(), str(), summary(), dim(), names()

# Statistics
mean(), median(), sd(), min(), max(), summary()

# Subsetting
df[rows, cols], df$column, df[condition, ]

# Utilities
length(), nrow(), ncol(), is.na(), sum()

# Sequences
1:10, seq(), rep()

# Sorting
sort(), order()

# Data Structures
c(), matrix(), data.frame(), list()

# Tabulation
table(), aggregate()

# Plots
plot(), hist(), boxplot()

# Tests
chisq.test(), t.test(), lm()
```

---
## DATA STRUCTURES

### Vectors


```r
# Creating vectors
c(1, 2, 3, 4)                    # combine function
2:5                              # sequence: 2, 3, 4, 5
seq(2, 10, by=2)                 # 2, 4, 6, 8, 10
seq(2, 10, length=5)             # 5 evenly spaced numbers
rep(2, 3)                        # repeat: 2, 2, 2
rep(c(1,2), 3)                   # 1, 2, 1, 2, 1, 2
rep(c(1,2), c(3,2))              # 1, 1, 1, 2, 2
```

### Matrices


```r
# Create matrix
matrix(v, nrow=2, ncol=3)              # fills by COLUMN (default)
matrix(v, nrow=2, ncol=3, byrow=TRUE)  # fills by ROW

# Matrix operations
rbind(row1, row2)              # stack rows vertically
cbind(col1, col2)              # stack columns horizontally
t(matrix)                      # transpose
solve(matrix)                  # inverse of square matrix
matrixA %*% matrixB            # matrix multiplication
```

### Dataframes


```r
# Create dataframe
df <- data.frame(col1 = c(1,2,3), col2 = c("a","b","c"))
as.data.frame(matrix)          # convert matrix to dataframe

# Add columns
df$new_col <- values           # add by name
```

### Lists


```r
# Create list
my_list <- list(A = c(1,3,5), B = "text", C = df)

# Access elements
my_list$A                      # by name with $
my_list[[1]]                   # by position
my_list[["A"]]                 # by name with [[]]
```

---

## READING & WRITING DATA

### Reading Files


```r
# Text files
read.table("file.txt")                          # space/tab separated
read.table("file.txt", header=TRUE)             # with header row
read.table("file.txt", header=FALSE, col.names=names_vec)

# CSV files
read.csv("file.csv")                            # has header
read.csv("file.csv", header=FALSE)              # no header

# JSON files (requires jsonlite package)
library(jsonlite)
data <- fromJSON("file.json")                   # returns list
```

**Important:** Always open file in text editor FIRST to check:

- Header row presence
- Separator type (space, tab, comma, semicolon)
- Trailing empty rows
- Expected row count

### Writing Files


```r
write.csv(df, "output.csv", row.names=FALSE)    # save as CSV
write.table(df, "output.txt")                   # save as text
saveRDS(df, "data.rds")                         # save R object
df <- readRDS("data.rds")                       # load R object
```

---

## DATA INSPECTION

### Basic Info


```r
head(df)                       # first 6 rows
head(df, 10)                   # first 10 rows
tail(df)                       # last 6 rows
str(df)                        # structure of object
summary(df)                    # summary statistics
nrow(df)                       # number of rows (preferred)
NROW(df)                       # also works, more general
ncol(df)                       # number of columns (preferred)
NCOL(df)                       # also works
dim(df)                        # dimensions: c(rows, cols)
names(df)                      # column names
```

---

## SUBSETTING & INDEXING

### Using [] Brackets


```r
# Basic indexing
df[rows, columns]
df[1:3, ]                      # rows 1-3, all columns
df[, 2:4]                      # all rows, columns 2-4
df[1:3, 2:4]                   # rows 1-3, columns 2-4
df[c(1,3,5), ]                 # specific rows: 1, 3, 5

# Negative indexing (DROPS elements)
x[-1]                          # drops first element
x[-c(1,3)]                     # drops elements 1 and 3
```

### Using $ (Column Access)


```r
df$column_name                 # returns vector
df$age                         # get 'age' column
```

### Logical Subsetting


```r
# Single condition
df[df$Gender == "M", ]                    # males only
df[df$Age > 25, ]                         # age > 25
df[df$Score >= 80, ]                      # score >= 80

# Multiple conditions
df[df$Gender == "M" & df$Age > 25, ]      # AND: male AND over 25
df[df$Gender == "M" | df$Grade == "A", ]  # OR: male OR grade A

# Operators
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal
# <=  less than or equal
# &   AND (vectorized)
# |   OR (vectorized)
# &&  AND (non-vectorized, only first element)
# ||  OR (non-vectorized, only first element)
```

---

## SUMMARY STATISTICS

### Single Variable


```r
mean(x)                        # average
median(x)                      # median
sd(x)                          # standard deviation
var(x)                         # variance
min(x)                         # minimum
max(x)                         # maximum
range(x)                       # c(min, max)
sum(x)                         # sum
length(x)                      # number of elements
summary(x)                     # five-number summary + mean
quantile(x, probs)             # quantiles (default: 0, 0.25, 0.5, 0.75, 1)
IQR(x)                         # interquartile range
```

### Grouped Statistics


```r
# aggregate() - THE WORKHORSE for grouped summaries
aggregate(x ~ y, data=df, FUN=summary)    # x grouped by y
aggregate(score ~ gender, data=df, FUN=mean)
aggregate(cbind(x, y) ~ group, data=df, FUN=mean)  # multiple variables

# Formula syntax: outcome ~ predictor
# Can use custom functions
# FUN must return same-length output for each group
```

### Apply Family


```r
# apply() — apply FUN over rows (MARGIN=1) or columns (MARGIN=2) of a matrix
apply(matrix, MARGIN=1, FUN=mean)         # row means
apply(matrix, MARGIN=2, FUN=sd)           # column std deviations
apply(matrix, MARGIN=1, FUN=function(x) mean(x, trim=0.1))  # custom fn

# sapply() — simplified apply; returns vector or matrix (not a list)
sapply(1:5, function(i) i^2)              # [1, 4, 9, 16, 25]
sapply(groups, mean)                      # mean of each group

# tapply() — apply FUN to subsets of X defined by a factor INDEX
tapply(df$score, df$gender, mean)         # mean score by gender
tapply(df$score, df$gender, sd)           # SD by group
tapply(df$value, df$group, function(x) mean(Winsorize(x)))  # custom fn
```

### Correlation


```r
cor(x, y)                               # correlation (default: Pearson)
cor(x, y, method="pearson")             # Pearson correlation
cor(x, y, method="spearman")            # Spearman rank correlation  
cor(x, y, method="kendall")             # Kendall's tau
cor(df[, c("col1", "col2", "col3")])   # correlation matrix
```

---

## ROBUST STATISTICS


```r
# Trimmed mean — discard extreme proportions before averaging
mean(x, trim=0.1)                      # 10% trimmed: drops lowest/highest 10%

# Median absolute deviation (MAD) — robust spread measure
mad(x)                                 # median(|x - median(x)|) * 1.4826
# The 1.4826 scale factor makes it consistent with SD for normal data

# Winsorize — cap extreme values at given quantiles (requires DescTools)
library(DescTools)
Winsorize(x, quantile=c(0.05, 0.95))   # replace values outside [5th, 95th] pctile
# Winsorize returns modified vector; combine with tapply/aggregate for groups
aggregate(score ~ group, data=df,
          FUN=function(x) mean(Winsorize(x, quantile=c(0.05, 0.95))))
```

---

## MISSING VALUES


```r
is.na(x)                       # TRUE/FALSE for each element
sum(is.na(x))                  # count missing values
na.omit(df)                    # remove rows with ANY missing
complete.cases(df)             # logical vector: TRUE if row complete
```

---

## SORTING & ORDERING


```r
sort(x)                                  # sort vector ascending
sort(x, decreasing=TRUE)                 # sort descending
order(x)                                 # get indices for sorting

# Sort dataframe by column
df[order(df$Age), ]                      # ascending
df[order(df$Age, decreasing=TRUE), ]     # descending
df[order(df$Age, df$Score), ]            # sort by Age, then Score
```

---

## USEFUL UTILITY FUNCTIONS

### Finding & Matching


```r
which(condition)               # returns indices where TRUE
which.max(x)                   # index of maximum (FIRST if ties)
which.min(x)                   # index of minimum (FIRST if ties)
which(x == max(x))             # ALL indices with max value
match(x, table)                # returns positions of first matches
# match(c("A","B","C"), c("X","A","Y","C")) returns c(2, NA, 4)
```

### Tabulation


```r
table(x)                       # frequency table
table(x, y)                    # cross-tabulation (contingency table)
xtabs(~ x + y, data=df)        # alternative cross-tab using formula
```

### Date Handling


```r
as.Date("2020-01-15")                        # parse ISO date string to Date
as.Date("15/01/2020", format="%d/%m/%Y")     # parse with custom format
Sys.Date()                                   # today's date
as.numeric(date2 - date1)                    # difference in days
```

### Data Reshaping


```r
# stack() — reshape wide data to long format (selected columns → values + ind)
stack(df, select=c(col1, col2))    # returns data.frame with $values and $ind
stack(df[, c("before", "after")]) # use with wilcox.test/t.test on stacked data
# $values: all numeric values concatenated
# $ind   : factor indicating which original column each value came from
```

### Cutting (Binning)


```r
cut(x, breaks)                             # bin continuous variable
cut(score, breaks=c(-Inf, 10, 12, 15, 18, 20), 
    labels=c("F","D","C","B","A"))        # create grade categories
cut(x, breaks=5)                           # 5 equal-width bins
cut(x, breaks=c(0,10,20), include.lowest=TRUE)  # close left endpoint
```

### Combinations


```r
combn(n, k)                    # all combinations of k items from n
# combn(5, 2) returns all pairs from 1:5
# combn(c("A","B","C"), 2) returns all pairs from letters
```

### Set Operations


```r
union(x, y)                    # elements in x OR y
intersect(x, y)                # elements in BOTH x and y
setdiff(x, y)                  # elements in x but NOT in y
%in%                           # element-wise membership test
# c(1,2,3) %in% c(2,4,6) returns c(FALSE, TRUE, FALSE)
```

---

## STATISTICAL FUNCTIONS

### Distributions

**Pattern:** Every distribution has 4 functions: `d`, `p`, `q`, `r`


```r
# d = density/PMF/PDF
# p = cumulative probability (CDF)
# q = quantile function (inverse CDF)
# r = random generation

# Examples with normal distribution:
dnorm(x, mean=0, sd=1)         # density at x
pnorm(q, mean=0, sd=1)         # P(X <= q)
qnorm(p, mean=0, sd=1)         # value with cumulative prob p
rnorm(n, mean=0, sd=1)         # generate n random values

# Other distributions: binom, pois, unif, exp, chisq, t, f, etc.
# dhyper(w, m, n, k) - hypergeometric
## w: successes drawn
## m: no. of success states in popn 
## n: no. of failure states in popn 
## k: no. of draws 

# dpois(k, lambda) - Poisson
```

for a table:
(a, b)
(c, d)

**dhyper(a, a+c, b+d, a+b)**
### Hypothesis Tests


```r
# Chi-square test
chisq.test(table)              # returns list with test results
chisq_out <- chisq.test(table)
chisq_out$statistic            # test statistic
chisq_out$p.value              # p-value
chisq_out$expected             # expected frequencies

# Fisher's exact test (for 2x2 tables with small counts)
fisher.test(table)

# t-test
t.test(x, mu=0)                        # one-sample
t.test(x, y)                           # two-sample (Welch by default)
t.test(x, y, var.equal=TRUE)           # pooled variance (equal var assumed)
t.test(before, after, paired=TRUE)     # paired
t.test(x, y, conf.level=0.99)         # 99% CI instead of default 95%

# Extract t-test results
t_out <- t.test(x, y, var.equal=TRUE)
t_out$statistic                        # test statistic
t_out$p.value                          # p-value
t_out$conf.int                         # confidence interval

# Normality tests
shapiro.test(x)                        # Shapiro-Wilk, H0: data is Normal
ks.test(x, "pnorm")                    # Kolmogorov-Smirnov

# Q-Q plots
qqnorm(x)                              # theoretical normal quantiles vs data
qqline(x)                              # add reference line through quartiles

# Non-parametric two-sample tests
wilcox.test(x, y)                          # Wilcoxon Rank-Sum (independent)
wilcox.test(x, y, alternative="greater")  # one-sided: H₁: x > y
wilcox.test(before, after,
            paired=TRUE, exact=FALSE)      # Wilcoxon Signed-Rank (paired)
# exact=FALSE: use normal approximation (required when ties present)
# alternative: "two.sided" (default), "greater", "less"

# Linear models
lm(y ~ x, data=df)                # simple linear regression
lm(y ~ x1 + x2, data=df)          # multiple regression
lm(y ~ x1 + x2 + x3, data=df)     # add indicator variable for categorical
lm(y ~ x1 * x2, data=df)          # interaction (includes main effects too)
lm_out <- lm(y ~ x, data=df)

# Accessing lm results
coef(lm_out)                       # named vector of β estimates
lm_out$coefficients                # same
summary(lm_out)                    # coefficients + t-tests + R² + F-test
anova(lm_out)                      # SS decomposition table (SSReg, SSRes, F)
confint(lm_out)                    # 95% CI for all parameters
fitted(lm_out)                     # ŷ fitted values
residuals(lm_out)                  # raw residuals r_i = y_i - ŷ_i
rstandard(lm_out)                  # standardised residuals (use for diagnostics)
influence.measures(lm_out)         # leverage, Cook's D, DFFITS etc.

# Extracting scalars from summary()
s <- summary(lm_out)
s$r.squared                        # R²
s$adj.r.squared                    # adjusted R²
s$sigma                            # residual standard error σ̂
s$coefficients["x", "Pr(>|t|)"]   # p-value for specific coefficient
```

### ANOVA (L8)


```r
# One-way ANOVA via lm
heifers_lm <- lm(org ~ type, data=heifers)
anova(heifers_lm)                          # F-test table
summary(heifers_lm)                        # coefficient estimates

# Ordering factor levels (controls which group is reference)
heifers$type <- factor(heifers$type,
                       levels=c("Control", "Alfacyp", "Enro", ...))

# Residual checks
r1 <- residuals(heifers_lm)
hist(r1)
qqnorm(r1); qqline(r1)

# Confidence interval for contrast / pairwise comparison (manual)
qt(0.025, df=n-k, lower.tail=FALSE)        # critical t-value (positive)

# Tukey HSD — all pairwise CIs, valid post-hoc
TukeyHSD(aov(heifers_lm), ordered=TRUE)

# Kruskal-Wallis (non-parametric, requires n_i >= 5 per group)
kruskal.test(heifers$org, heifers$type)
```

### Prediction from Linear Model (L9)


```r
# Generate new data for prediction
new_df <- data.frame(Water = seq(160, 240, by=5))

# Confidence interval for mean response E(Y|X)
conf_intervals <- predict(lm_out, new_df, interval="conf")
# Returns matrix: columns = fit, lwr, upr

# Prediction interval for individual new observation
pred_intervals <- predict(lm_out, new_df, interval="pred")

# Plot fitted line with CI bands
plot(x, y)
abline(lm_out, col="red")
lines(new_df$Water, conf_intervals[, "lwr"], col="red", lty=2)
lines(new_df$Water, conf_intervals[, "upr"], col="red", lty=2)
```

---

## LOOPS & CONTROL FLOW

### For Loops


```r
# Basic structure
for(variable in sequence) {
  # do something
}

# Examples
for(i in 1:10) {
  print(i^2)
}

for(name in c("Alice", "Bob", "Charlie")) {
  print(paste("Hello", name))
}

# Loop over dataframe groups
for(group_name, group_df in groupby_output) {
  # process each group
}
```

### While Loops


```r
# Basic structure
while(condition) {
  # do something
  # MUST update condition!
}

# Example
x <- 0
while(x < 10) {
  print(x)
  x <- x + 1
}
```

### If-Else


```r
if(condition) {
  # do something
} else if(another_condition) {
  # do something else
} else {
  # default action
}
```

---

## USER-DEFINED FUNCTIONS


```r
# Basic structure
function_name <- function(arg1, arg2, default_arg=10) {
  # calculations
  result           # last line is returned automatically
}

# Or use explicit return
function_name <- function(arg1, arg2) {
  result <- arg1 + arg2
  return(result)
}

# Call function
function_name(5, 3)
```

---

## PLOTTING (BASE R)

### Basic Plots


```r
plot(x, y)                            # scatter plot
plot(x, y, col="red", pch=19, cex=1.5)  # with options
hist(x)                               # histogram
hist(x, breaks=20)                    # more bins
boxplot(x)                            # box plot
boxplot(y ~ group, data=df)           # box plot by group

# Plot returns object with stats
box_out <- boxplot(x)
box_out$out                           # outlier values
box_out$stats                         # five-number summary
```

### Plot Customization


```r
# Common arguments
col                             # color (e.g., "red", "#FF0000")
pch                             # plotting character (1-25)
cex                             # character expansion (size multiplier)
lty                             # line type (1=solid, 2=dashed, etc.)
lwd                             # line width
xlab, ylab                      # axis labels
main                            # title
xlim, ylim                      # axis limits c(min, max)

# Adding elements
abline(a, b)                    # line with intercept a, slope b
abline(h=5)                     # horizontal line at y=5
abline(v=3)                     # vertical line at x=3
abline(lm_model)                # add regression line
points(x, y)                    # add points
lines(x, y)                     # add lines
text(x, y, labels)              # add text
legend()                        # add legend

# Multiple plots in one figure
par(mfrow=c(2, 2))              # 2x2 grid of plots
par(mfrow=c(1, 1))              # reset to single plot
op <- par()                     # save old parameters
par(op)                         # restore old parameters

# Colors
colors()                        # 657 named colors
rgb(255, 0, 0, 64, maxColorValue=255)  # custom with transparency
# alpha controls transparency (0=transparent, 255=opaque)
```

### Advanced Plotting Techniques


```r
# Jittering (add random noise to avoid overplotting)
plot(x, y + runif(length(y), -0.2, 0.2))

# Transparency for overplotting
red_transparent <- rgb(255, 0, 0, alpha=64, maxColorValue=255)
plot(x, y, col=red_transparent, pch=20, cex=1.6)
```

---

## PLOTTING (LATTICE)


```r
library(lattice)

# Histograms
histogram(~ variable, data=df)
histogram(~ variable | factor, data=df)  # conditioned on factor

# Density plots
densityplot(~ variable, data=df)
densityplot(~ variable, data=df, bw=0.5)  # bandwidth control
densityplot(~ variable | factor, data=df)

# Box plots
bwplot(~ variable, data=df)
bwplot(variable ~ factor, data=df)        # by group

# Scatter plots
xyplot(y ~ x, data=df)
xyplot(y ~ x | factor, data=df)           # panels by factor
xyplot(y ~ x, groups=factor, data=df)     # overlay by group
xyplot(y ~ x, data=df, type="l")          # line plot

# Dot plots
dotplot(value ~ group, data=df)           # dot plot by group (good for means/CIs)

# Bar charts
barchart(table, horizontal=FALSE)

# Common arguments
layout = c(3, 1)                # 3 columns, 1 row
main = "title"                  # plot title
xlab, ylab                      # axis labels
col                             # color
pch                             # plotting character
```

---

## PLOTTING (GGPLOT2) - If Covered


```r
library(ggplot2)

# Basic template
ggplot(data=df, aes(x=var1, y=var2)) +
  geom_point() +
  labs(title="Title", x="X label", y="Y label")

# Common geoms
geom_point()                    # scatter plot
geom_line()                     # line plot
geom_histogram()                # histogram
geom_boxplot()                  # box plot
geom_bar()                      # bar chart
geom_density()                  # density plot
```

---

## CATEGORICAL DATA ANALYSIS PATTERNS

### Computing Expected Counts Under Independence


```r
# Given contingency table
tab <- table(df$rater_A, df$rater_B)
n <- sum(tab)                          # total count

# Marginal probabilities
row_margins <- rowSums(tab) / n        # row marginals
col_margins <- colSums(tab) / n        # column marginals

# Expected counts using outer product
expected <- n * outer(row_margins, col_margins)

# Pearson residuals
residuals <- (tab - expected) / sqrt(expected)
```

### Agreement Measures

**Cohen's Kappa:**


```r
# Measure of inter-rater agreement
# κ = (observed - expected) / (1 - expected)

# Joint probabilities
pi_ij <- tab / n

# Observed agreement (diagonal sum)
observed <- sum(diag(pi_ij))

# Expected agreement under independence  
expected <- sum(row_margins * col_margins)

# Cohen's Kappa
kappa <- (observed - expected) / (1 - expected)
```

**Weighted Kappa (for ordinal categories):**


```r
# Create weight matrix: w_ij = 1 - |i-j|/(I-1)
I <- 4  # number of categories
w <- matrix(0, nrow=I, ncol=I)

for(i in 1:I) {
  for(j in 1:I) {
    w[i, j] <- 1 - abs(i - j) / (I - 1)
  }
}

# Weighted observed agreement
weighted_obs <- sum(w * pi_ij)

# Weighted expected agreement
weighted_exp <- sum(w * outer(row_margins, col_margins))

# Weighted Kappa
kappa_w <- (weighted_obs - weighted_exp) / (1 - weighted_exp)
```

**Key functions:**

- `outer(x, y)` - outer product for expected counts
- `diag(matrix)` - extract diagonal (for agreement)
- `sum(diag(matrix))` - trace (sum of diagonal)

---

## CATEGORICAL DATA ANALYSIS

### Mosaic Plots


```r
# Mosaic plot (base R)
mosaicplot(table)
mosaicplot(table, shade=TRUE)              # color by residuals
mosaicplot(table, shade=TRUE, 
           xlab="X", ylab="Y")             # with labels

# Interpretation:
# - Area proportional to cell count
# - Blue = more than expected under independence
# - Red = less than expected
# - Solid = positive residual, dashed = negative
```

### Association Measures (Categorical)


```r
# Requires DescTools package
library(DescTools)

# Get all association measures
Desc(table, plotit=FALSE)
assoc_out <- Desc(table, plotit=FALSE)[[1]]$assocs

# Specific measures:
# - Kendall's tau-b: for ordinal variables
# - Goodman-Kruskal gamma: for ordinal variables
# - Cramér's V: for nominal variables
# - Odds Ratio: for 2x2 tables
```

### Skewness & Kurtosis (DescTools, L7)


```r
library(DescTools)

# Per-group skewness and kurtosis via aggregate
aggregate(viscera ~ gender, data=abl, Skew, method=1)
aggregate(viscera ~ gender, data=abl, Kurt, method=1)

# method=1: method-of-moments estimator (matches lecture formulas)
# Skew > 0: right-skewed; < 0: left-skewed
# Kurt > 0: fat tails (leptokurtic); < 0: thin tails (platykurtic)
# Note: Kurt() here is EXCESS kurtosis (Normal = 0)
```

### Odds Ratio & Relative Risk


```r
# Odds ratio for 2x2 table:
# OR = (a*d) / (b*c) where table is:
#      col1  col2
# row1   a     b
# row2   c     d

# Relative risk:
# RR = (a/(a+b)) / (c/(c+d))
# RR ≈ OR when probabilities are small
```

---

## SIMULATION (L10)

### Random Number Generation


```r
set.seed(2137)    # set seed — must call BEFORE generating; resets to same stream

rnorm(n, mean=0, sd=1)           # Normal
runif(n, min=0, max=1)           # Uniform
rgamma(n, shape=2, rate=3)       # Gamma (rate = 1/scale)
rpois(n, lambda=1.3)             # Poisson
rbinom(n, size=2, prob=0.3)      # Binomial
rexp(n, rate=1)                  # Exponential
```

### Simulation Loop Patterns


```r
# Basic simulation loop
set.seed(2139)
output_vec <- rep(0, length=100)     # pre-allocate
for(i in 1:length(output_vec)) {
  X <- rpois(20, 0.5)
  # ... compute statistic
  if(condition) output_vec[i] <- 1
}
mean(output_vec)                     # estimate of probability

# replicate() — cleaner alternative for repeating a function call
replicate(2000, some_function())

# vapply() — like sapply but type-safe (faster, safer)
vapply(1:2000,
       function(x) generate_one_test(),
       1L)                           # 1L specifies output type: integer scalar
```

### ifelse and floor


```r
ifelse(condition, value_if_true, value_if_false)   # vectorised if-else
# e.g. profit function:
hX <- ifelse(X >= 11000, 11000,
             floor(X) + (11000 - floor(X)) * (-0.25))

floor(x)     # round DOWN to nearest integer
ceiling(x)   # round UP
round(x, n)  # round to n decimal places
```

### Bootstrap (boot library)


```r
library(MASS)
library(boot)

# Define statistic function — must accept (data, indices)
stat_fn <- function(d, i) {
  mean(d[i], trim=0.1)     # i contains bootstrap sample indices
}

# Run bootstrap
boot_out <- boot(chem, stat_fn, R=1999, stype="i")

# Compute confidence intervals
boot.ci(boot.out=boot_out, type=c("perc", "bca"))
# perc: basic percentile interval
# bca:  bias-corrected and accelerated (more accurate, preferred)
```

### Monte Carlo Integration


```r
# To estimate ∫ h(x) f(x) dx = E[h(X)]:
# 1. Generate X ~ f
# 2. Compute mean(h(X))

set.seed(2138)
X <- runif(50000, 0, 1)     # X ~ Uniform(0,1)
hX <- exp(2*X)              # h(X)
mean(hX)                    # Monte Carlo estimate

# Confidence interval for the estimate (from CLT)
s <- sd(hX)
q1 <- qnorm(0.95)           # z-quantile
CI <- c(mean(hX) - q1*s/sqrt(n), mean(hX) + q1*s/sqrt(n))
```

---

## SPECIAL TECHNIQUES

### Poisson-ness Plot


```r
# Check if data follows Poisson distribution
# 1. Get counts of counts
Xk <- table(data)
k <- as.integer(names(Xk))
Xk <- as.vector(Xk)

# 2. Compute phi
N <- length(data)
phi <- lfactorial(k) + log(Xk/N)

# 3. Plot phi vs k (should be linear if Poisson)
plot(k, phi)

# 4. Estimate lambda from slope
lm_out <- lm(phi ~ k)
slope <- coef(lm_out)[2]
lambda_hat <- exp(slope)
```

### Theil-Sen Estimator (Robust Slope)


```r
# Compute slope from ALL pairwise combinations
# More robust to outliers than least squares

all_pairs <- combn(n, 2)
slopes <- numeric(ncol(all_pairs))

for(i in 1:ncol(all_pairs)) {
  idx <- all_pairs[, i]
  slopes[i] <- (y[idx[2]] - y[idx[1]]) / (x[idx[2]] - x[idx[1]])
}

robust_slope <- median(slopes)
```

---

## STRING OPERATIONS


```r
paste("Hello", "World")              # concatenate with space
paste0("Hello", "World")             # concatenate without space
sprintf("%.2f", 3.14159)             # formatted printing
substr("Hello", 1, 3)                # substring: "Hel"
nchar("Hello")                       # string length: 5
toupper("hello")                     # "HELLO"
tolower("HELLO")                     # "hello"
strsplit("a,b,c", ",")               # split string: list("a","b","c")
grep("pattern", vector)              # find pattern (returns indices)
grepl("pattern", vector)             # find pattern (returns T/F)
sub("old", "new", string)            # replace first occurrence
gsub("old", "new", string)           # replace all occurrences
```

---

## OUTPUT & PRINTING


```r
print(x)                             # print object
cat("text", x, "\n")                 # concatenate and print (no quotes)
cat("Value:", x, "\n", sep="")       # control separator

# format() — convert number to string with controlled precision
format(3.14159, digits=3)            # "3.14" (3 significant digits)
format(0.0001234, digits=3)          # "0.000123"
format(x, nsmall=2)                  # ensure at least 2 decimal places

# Formatted printing
sprintf("%.2f", 3.14159)             # "3.14" (2 decimals)
sprintf("%d", 42)                    # "42" (integer)
sprintf("%s", "text")                # "text" (string)

# Redirect output to file
sink("output.txt")                   # start saving to file
cat("Results:\n")
print(summary(data))
sink()                               # stop, close file
```

---

## PACKAGES


```r
# Install (once)
install.packages("package_name")
install.packages(c("pkg1", "pkg2"))  # multiple packages

# Load (every session)
library(package_name)
require(package_name)                # alternative, returns T/F

# Check if installed
"package_name" %in% installed.packages()

# Get help
help(package="package_name")
```

**Common Packages for This Course:**

- `MASS` - datasets and robust regression
- `lattice` - trellis graphics (conditioned plots, `histogram`, `xyplot`, etc.)
- `jsonlite` - JSON read/write
- `DescTools` - `Skew()`, `Kurt()`, `Desc()` for categorical association measures
- `psych` - correlation plots; `corPlot(r, cex=0.8, cex.axis=0.8, show.legend=TRUE)` where `r` is a correlation matrix
- `boot` - bootstrap resampling (`boot()`, `boot.ci()`)

---

## GETTING HELP


```r
?function_name                       # help for function
??search_term                        # search all help
help(function_name)                  # same as ?
help.search("search_term")           # same as ??
example(function_name)               # run examples from help
args(function_name)                  # show function arguments
apropos("text")                      # find functions with "text" in name
```

**Tip:** Examples at bottom of help pages are GUARANTEED to work!

---

## IMPORTANT CONCEPTS

### Recycling Rule

**Shorter vector repeats to match longer vector**


```r
c(1, 2, 3, 4) + c(10, 20)
# Returns: 11, 22, 13, 24
# Explanation: c(10,20) recycled to c(10,20,10,20)

# Used in matrix operations
matrix / vector  # vector recycles to match each column/row
```

### Indexing Differences from Python

- **Indexing starts at 1** (not 0)
- **Negative indexing DROPS elements** (not "from end")


```r
x <- c(10, 20, 30, 40, 50)
x[1]           # 10 (first element)
x[-1]          # 20, 30, 40, 50 (drops first)
x[-c(1,3)]     # 20, 40, 50 (drops 1st and 3rd)
```

### Formula Syntax

**Powerful notation used across many functions**


```r
# Basic: outcome ~ predictor
aggregate(score ~ gender, data=df, FUN=mean)
lm(y ~ x, data=df)
boxplot(score ~ group, data=df)

# Multiple predictors
lm(y ~ x1 + x2, data=df)

# Interactions
lm(y ~ x1 * x2, data=df)        # includes main effects + interaction
lm(y ~ x1 : x2, data=df)        # interaction only

# Conditioning in lattice
xyplot(y ~ x | factor, data=df)  # separate panels by factor
```

---

## DEBUGGING TIPS


```r
# Insert breakpoint
browser()                      # stop execution, enter debug mode

# Debug mode commands
# n - next line
# c - continue (exit debug mode)
# Q - quit
# help - show debug commands
# where - show call stack

# View objects
str(object)                    # structure
class(object)                  # object type
typeof(object)                 # storage mode
```

**General Debugging Strategy:**

1. Print intermediate values to understand structure
2. Test functions with small, known datasets first
3. Read error messages carefully - last line tells you where
4. Check for common mistakes (see below)

---

## COMMON MISTAKES TO AVOID

❌ **Forgetting c()**


```r
# WRONG
x <- 1, 2, 3
# CORRECT
x <- c(1, 2, 3)
```

❌ **Using = instead of == in logical tests**


```r
# WRONG
df[df$Gender = "M", ]
# CORRECT  
df[df$Gender == "M", ]
```

❌ **Forgetting comma in df[rows, cols]**


```r
# WRONG (treats as list indexing)
df[1:3]
# CORRECT
df[1:3, ]
```

❌ **Using && instead of & in vectors**


```r
# WRONG (only compares first elements)
df[df$Age > 25 && df$Gender == "M", ]
# CORRECT (vectorized)
df[df$Age > 25 & df$Gender == "M", ]
```

❌ **Accessing non-existent columns**


```r
# If column has spaces
df$col name      # WRONG
df$"col name"    # CORRECT
df[, "col name"] # ALSO CORRECT
```

---

## BEST PRACTICES

✅ **Use meaningful variable names**


```r
student_scores  # good
x               # bad (unless in math context)
```

✅ **Check data after reading**


```r
data <- read.csv("file.csv")
head(data)      # check first few rows
str(data)       # check structure
summary(data)   # check for oddities
```

✅ **Handle missing values explicitly**


```r
mean(x, na.rm=TRUE)           # remove NA before calculation
sum(is.na(x))                 # count missing
```

✅ **Factor variables when appropriate**


```r
df$category <- factor(df$category, 
                      levels=c("low","medium","high"),
                      ordered=TRUE)
```

✅ **Check assumptions before tests**


```r
# Chi-square: all expected counts >= 5
chisq_out$expected

# Normality: Q-Q plot, Shapiro-Wilk
qqnorm(x)
qqline(x)
shapiro.test(x)
```

---
## NOTES FROM LECTURES

**Instructor Quotes:**

- "Always open the data file in text editor before reading"
- "The roof is not going to fall down if the code doesn't work"
- "If you're not sure, just experiment with it"
- "The examples at bottom of help pages - guaranteed to work"
- "Try to use the recycling rule to your advantage"
- "Converting column to factor before summary() gives frequency table instead of five-number summary"
- "Small group sizes (n=3) make estimates unreliable — always check counts with table()"
- "Never automatically drop outliers; investigate WHY; run analysis twice (with/without) and compare"
