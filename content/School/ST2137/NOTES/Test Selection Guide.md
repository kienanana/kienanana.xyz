---
class: note
tags:
  - y3s2
  - statistics
  - revision
source:
related:
author:
date: 2026-04-26
updated: 2026-04-26
aliases:
---
## Step 1 — What kind of variables do you have?

---

### Both Categorical → L4

**First: can you use chi-square?**
> Chi-square requires all *expected* cell counts ≥ 5. If any are < 5, use Fisher's Exact instead (2×2 only).

| Variables                     | Test                         | What it answers               |
| ----------------------------- | ---------------------------- | ----------------------------- |
| 2 nominal, large sample       | Chi-square                   | Is there an association?      |
| 2 nominal, small sample (2×2) | Fisher's Exact               | Same, exact p-value           |
| 2 ordinal                     | Chi-square **+** Gamma/Tau-b | Exists + direction + strength |

> Chi-square and Fisher only tell you **if** an association exists. To say how strong, add:

| Measure           | Use when                    | Interpretation                  |
| ----------------- | --------------------------- | ------------------------------- |
| **Odds Ratio**    | Any 2×2 (esp. case-control) | OR = 1 → no association         |
| **Relative Risk** | Cohort studies              | RR = 2 → twice as likely        |
| **Gamma (γ)**     | Ordinal, want simple number | Ignores ties; larger magnitude  |
| **Tau-b (τ_b)**   | Ordinal, want conservative  | Penalises ties; \|τ_b\| ≤ \|γ\| |

> OR vs RR: if outcome is rare (< 10%), they're approximately equal. Can't compute RR from case-control data.

---

### Continuous outcome, comparing groups → L7, L8
*is there a difference between groups?*

**Check assumptions first:**
1. **Normality** — histogram + QQ-plot of data (L7) or residuals (L8)
2. **Equal variance** — if larger SD > 2× smaller SD, do NOT assume equal variance

| Situation               | Parametric             | Non-parametric fallback (no normality assumption) |
| ----------------------- | ---------------------- | ------------------------------------------------- |
| 2 independent groups    | Independent t-test     | Wilcoxon Rank-Sum (WRS)                           |
| 2 paired/related groups | Paired t-test          | Wilcoxon Sign Test (WST)                          |
| 3+ groups               | One-way ANOVA (F-test) | Kruskal-Wallis                                    |

> **Paired vs independent:** paired = same subject in both groups (e.g. before/after), or matched observations. Compute $D_i = X_i - Y_i$ and test if median/mean of D is 0.

> **Unpooled t-test (Welch):** use when equal variance assumption fails in the 2-group case.

**After ANOVA — which groups differ?**

| When                                         | Method                                         |
| -------------------------------------------- | ---------------------------------------------- |
| Contrast specified *before* seeing data      | Manual contrast / t-test using $MS_W$          |
| All pairwise comparisons *after* seeing data | **TukeyHSD**                                   |
| Subset of comparisons *after* seeing data    | **Bonferroni** (divide α by number of tests m) |

---

## Step 2 — Quick flowchart

```
What type of variables?
│
├─ Both categorical
│   ├─ Expected counts < 5?  Yes → Fisher's Exact (2×2 only)
│   │                        No  → Chi-square
│   ├─ Both nominal? → Chi-square (+OR/RR for strength)
│   └─ Both ordinal? → Chi-square + Gamma/Tau-b
│
└─ Continuous outcome, comparing groups
    ├─ 2 groups, paired?    Yes → Paired t-test / WST
    │                       No  → Independent t-test / WRS
    └─ 3+ groups?               → ANOVA / Kruskal-Wallis
                                  → Follow up: contrasts or TukeyHSD
```

---

## Step 3 — Assumption check summary

| Test | Key assumptions |
|---|---|
| Independent t-test | Normality in each group; equal variance (or use Welch) |
| Paired t-test | Normality of *differences* $D_i$ |
| ANOVA | Normality of *residuals*; equal variance across groups |
| WRS | Both $n_1, n_2 \geq 10$; continuous underlying distribution |
| WST | ≥ 16 non-zero differences (else use exact version) |
| Kruskal-Wallis | $n_i \geq 5$ for all groups |
| Chi-square | All expected counts ≥ 5 |

---

See also: [[Chi-Square & Fisher]] · [[Odds Ratio & Relative Risk]] · [[Gamma Tau]] · [[L7 Two-sample Hypothesis Tests]] · [[L8 ANOVA]]
