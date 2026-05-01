---
class: note
tags:
  - y3s2
  - R
  - python
  - statistics
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 10:31:08
aliases:
---
## The Core Question

**Are two categorical variables related, or independent?**

- Independent = knowing one variable tells you nothing about the other
- Related = knowing one helps predict the other

---

## Chi-Square Test (χ²)

### Key Idea

> Compare what you **OBSERVE** vs what you'd **EXPECT** if there were no relationship. Bigger difference = more evidence of a relationship.

### Expected Count Formula

```
Expected = (Row Total × Column Total) / Grand Total
```

### Chi-Square Statistic

```
χ² = Σ (Observed - Expected)² / Expected
```

Sum this over **every cell** in the table.

### Degrees of Freedom

```
df = (rows - 1) × (columns - 1)
```

### Interpretation

- **Small p-value (< 0.05)** → reject independence → variables ARE related
- **Large p-value (≥ 0.05)** → no evidence of a relationship

### ⚠️ Key Assumption

**All expected counts must be ≥ 5.** If any are < 5, use Fisher's Exact Test instead.

### Python

```python
from scipy.stats import chi2_contingency

observed = [[60, 20, 20],
            [30, 40, 30]]

chi2, p_value, df, expected = chi2_contingency(observed)
print(f"χ² = {chi2:.2f}, p = {p_value:.4f}, df = {df}")
print(f"Min expected count: {expected.min():.2f}")
```

---

## Fisher's Exact Test

### Key Idea

> Used for **2×2 tables with small counts**. Calculates the **exact** probability of seeing a table this extreme (or more), given fixed row/column totals.

Uses the **hypergeometric distribution** — no approximation needed.

### When to Use

| Situation                        | Test               |
| -------------------------------- | ------------------ |
| Any size table, all expected ≥ 5 | Chi-Square         |
| 2×2 table, any expected < 5      | **Fisher's Exact** |
| 2×2 table, want exact p-value    | **Fisher's Exact** |
| Larger than 2×2                  | Chi-Square only    |

### Python

```python
from scipy.stats import fisher_exact

table = [[7, 3],
         [2, 8]]

odds_ratio, p_value = fisher_exact(table)
print(f"Odds Ratio = {odds_ratio:.2f}, p = {p_value:.4f}")
```

---

## What to Report

**Chi-Square:**

> "A chi-square test showed a significant association between age and ice cream preference (χ² = 18.66, df = 2, p < 0.001)."

**Fisher's Exact:**

> "Fisher's exact test showed a significant association between drug treatment and side effects (p = 0.011, OR = 9.33)."