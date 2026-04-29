---
class: note
tags:
  - statistics
  - revision
source:
related:
author:
date: 2026-04-27
updated: 2026-04-27
aliases:
---
## Step 1 — What kind of data do you have, and what do you want to know?

---

### Choosing a Plot

| Data type                                    | Question                   | Plot                             |
| -------------------------------------------- | -------------------------- | -------------------------------- |
| One quantitative variable                    | Shape, spread, modality    | Histogram or Density plot        |
| One quantitative variable                    | Outliers, quartiles, skew  | Boxplot                          |
| One quantitative variable                    | Is it Normal?              | QQ-plot                          |
| One quantitative + one group                 | Compare distributions      | Side-by-side boxplots            |
| Two quantitative variables                   | Linear relationship?       | Scatterplot                      |
| Many quantitative variables                  | All pairwise relationships | Scatterplot matrix               |
| One categorical variable                     | Frequency or proportion    | Bar chart                        |
| Two categorical variables                    | Association pattern        | Mosaic plot or grouped bar chart |
| Categorical outcome + quantitative predictor | How probability changes    | Conditional density plot         |

> **Histogram vs density plot:** histogram depends on bin width choice; density plot uses a bandwidth $h$. Too small $h$ → spiky; too large $h$ → over-smoothed. Use both to cross-check.

---

### Reading a Distribution

| Shape | Mean vs Median | What it looks like | Implication |
|---|---|---|---|
| Symmetric (Normal-like) | Mean ≈ Median | Bell, roughly equal tails | Parametric methods safe |
| Right-skewed | Mean > Median | Long tail to the right | Outliers inflate mean; use median or robust stats |
| Left-skewed | Mean < Median | Long tail to the left | Same; check for floor effects |
| Bimodal | N/A | Two peaks | May indicate two subgroups; split and analyse separately |
| Heavy-tailed | Mean ≈ Median, but wide | Symmetric but wide tails | SD unreliable; use IQR or MAD |

> **Five-number summary shortcut:** look at the gaps between Min–Q1, Q1–Median, Median–Q3, Q3–Max. Unequal gaps = skew in that direction.

---

## Step 2 — Checking Normality

**Use in order: visual first, formal test last.**

```
1. Histogram
   └─ Roughly bell-shaped, single peak? → possible Normal
   └─ Skewed, bimodal, or heavy-tailed? → likely NOT Normal

2. QQ-plot (quantile-quantile plot)
   └─ Points lie on straight diagonal line → Normal
   └─ S-curve → light tails (platykurtic)
   └─ Inverted S-curve → heavy tails (leptokurtic)
   └─ Points curve up at right end → right-skewed
   └─ Points curve down at left end → left-skewed

3. Formal test (use only for confirmation, not as sole evidence)
   └─ Shapiro-Wilk: preferred for small n
   └─ Kolmogorov-Smirnov: large n
   └─ Caution: large n almost always rejects — visual check matters more
```

> **Skewness and kurtosis numbers:** $g_1 \approx 0$ → symmetric; $g_2 > 0$ → fat tails (kurtosis > 3). These supplement plots; don't rely on them alone.

---

## Step 3 — Checking Association Between Two Quantitative Variables

| Measure | Formula | Range | Limitation |
|---|---|---|---|
| Pearson $r$ | $\frac{S_{XY}}{S_X S_Y}$ | $[-1, 1]$ | **Linear association only** |

> $r$ close to $\pm 1$ = strong linear association; $r \approx 0$ = no *linear* association (a curved relationship can exist and $r$ still be 0).

> Always plot a scatterplot before reporting $r$. Outliers can distort $r$ heavily.

**When to use scatterplot matrix:** when you have 3+ quantitative variables and want to scan all pairwise relationships simultaneously. Use a correlation heatmap alongside it to spot clusters.

---

## Step 4 — Outlier Detection via Boxplot Rule

$$\text{Outlier if } x < Q_1 - 1.5 \times \text{IQR} \quad \text{or} \quad x > Q_3 + 1.5 \times \text{IQR}$$

> This is a *flag*, not a deletion rule. Investigate outliers — they may be data errors or genuinely extreme observations. Do not remove without justification.

---

See also: [[L3 Exploring Quantitative Data]] · [[L4 Exploring Categorical Data]] · [[L1 Introduction to R]] · [[Robust Statistics Guide]]
