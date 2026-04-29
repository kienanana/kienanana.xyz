---
class: note
tags:
  - dataset
  - R
  - python
  - scipy
  - DescTools
  - categorical
  - chi-square
  - odds-ratio
source:
related:
  - "[[L4 Exploring Categorical Data]]"
author:
date: 2026-04-22
updated: 2026-04-22
aliases:
---
## Description
> From [[L4 Exploring Categorical Data#Example 4.6]]

A 2×2 contingency table cross-classifying chest-pain status (pain / no pain) against gender (male / female) for 1073 patients. Used to illustrate the chi-squared test for independence and odds-ratio computation.

| | pain | no pain |
|---|---|---|
| **male** | 46 | 474 |
| **female** | 37 | 516 |

Total: 1073 patients. Marginal proportions: $\widehat{P}(X=\text{male}) = 0.485$, $\widehat{P}(Y=\text{pain}) = 0.077$.

## Expected counts
> From [[L4 Exploring Categorical Data#Example 4.6]]

Under $H_0$ (independence), the joint probability factors:
$$
\widehat{P}(X=\text{male}, Y=\text{pain}) = 0.485 \times 0.077 \approx 0.04
$$
Expected count for the male-pain cell: $0.04 \times 1073 = 42.92$.

General formula:
$$
\text{Expected count} = \frac{\text{Row total} \times \text{Column total}}{\text{Total sample size}}
$$

##### R code
```R
chisq_output <- chisq.test(chest_tab)
chisq_output$expected
```

##### Python code
```python
chisq_output.expected_freq
```

All expected counts exceed 5, so the chi-squared test is valid.

## Chi-squared test
> From [[L4 Exploring Categorical Data#Example 4.6]]

Formula (with continuity correction):
$$
\chi^2 = \sum \frac{(|\text{observed} - \text{expected}| - 0.5)^2}{\text{expected}}
$$

##### R code
```R
x <- matrix(c(46, 37, 474, 516), nrow=2)
dimnames(x) <- list(c("male", "female"), c("pain", "no pain"))
chest_tab <- as.table(x)

chisq_output <- chisq.test(chest_tab)
chisq_output
```

##### Python code
```python
from scipy import stats
import numpy as np

chest_array = np.array([[46, 474], [37, 516]])
chisq_output = stats.chi2_contingency(chest_array)

print(f"The p-value is {chisq_output.pvalue:.3f}.")
## The p-value is 0.228.
print(f"The test-statistic value is {chisq_output.statistic:.3f}.")
## The test-statistic value is 1.456.
```

**Conclusion:** p-value = 0.228, do not reject $H_0$ at the 5% level. Not enough evidence to conclude gender and chest pain are associated.

## Odds ratio
> From [[L4 Exploring Categorical Data#Example 4.10 (Chest Pain and Gender Odds Ratio)]]

Sample odds ratio:
$$
\widehat{OR} = \frac{n_{11} \cdot n_{22}}{n_{12} \cdot n_{21}} = \frac{46 \times 516}{474 \times 37}
$$

95% CI via log-OR + Normal approx:
$$
\log \widehat{OR} \pm z_{0.025} \times \text{ASE}(\log \widehat{OR})
$$
where $\text{ASE} = \sqrt{1/n_{11} + 1/n_{12} + 1/n_{21} + 1/n_{22}}$, then exponentiate the endpoints.

##### R code
```R
library(DescTools)
OddsRatio(chest_tab, conf.level = .95)
```

##### Python code
```python
import statsmodels.api as sm
chest_tab2 = sm.stats.Table2x2(chest_array)
print(chest_tab2.summary())
```

The CI for the OR includes 1 — consistent with the chi-squared test, no evidence of association.

See [[Odds Ratio & Relative Risk]] for further interpretation notes, and [[Chi-Square & Fisher]] for the independence test in general.

---
See also: [[L4 Exploring Categorical Data]] · [[Chi-Square & Fisher]] · [[Odds Ratio & Relative Risk]]
