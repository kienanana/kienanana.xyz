---
class:
tags:
source:
related:
author:
date: 2026-03-11
updated: 2026-03-11 10:54:25
aliases:
---
# Goodman-Kruskal Gamma & Kendall's Tau-b

_Measuring association strength and direction in **ordinal** data_

---

## Why Not Just Chi-Square?

Chi-square tests IF variables are related, but ignores **order**. Gamma and Tau-b use the natural ordering of categories to tell you **how strong** and **in what direction** the association is.

---

## Core Concept: Concordant, Discordant & Tied Pairs

For any two observations (Person A vs Person B):

| Type               | Condition                        | Meaning                   |
| ------------------ | -------------------------------- | ------------------------- |
| **Concordant (C)** | Both variables go same direction | Consistent pattern        |
| **Discordant (D)** | Variables go opposite directions | Inconsistent pattern      |
| **Tied**           | At least one variable is equal   | Can't determine direction |

```
CONCORDANT:  X: A > B  and  Y: A > B   (or both lower)
DISCORDANT:  X: A > B  and  Y: A < B   (or vice versa)
TIED:        X: A = B  (or Y: A = B)
```

---

## Goodman-Kruskal Gamma (γ)

### Key Idea

> Out of all pairs where we CAN determine direction (ignoring ties), what proportion are concordant?

### Formula

```
γ = (C - D) / (C + D)
```

Ties are **completely ignored**.

### Interpretation

|γ|Meaning|
|---|---|
|+1|Perfect positive association|
|0|No association|
|−1|Perfect negative association|

**PRE interpretation:** |γ| = how much knowing X reduces your errors in predicting the order of Y.

---

## Kendall's Tau-b (τ_b)

### Key Idea

> Like gamma, but **penalises for ties** — gives a more conservative estimate.

### Formula

```
τ_b = (C - D) / √[(C + D + T_x)(C + D + T_y)]
```

Where T_x = pairs tied on X only, T_y = pairs tied on Y only.

### Key property

```
|τ_b| ≤ |γ|   (tau is always ≤ gamma in magnitude)
```

---

## Gamma vs Tau-b

|Feature|Gamma (γ)|Tau-b (τ_b)|
|---|---|---|
|Treats ties|Ignores|Penalises|
|Magnitude|Larger|Smaller|
|Best when|Many ties, want simple interpretation|Want conservative/correlation-like measure|

**Rule of thumb:** If gamma and tau-b are very different, there are many ties in your data.

---

## Python

```python
from scipy.stats import kendalltau

# Convert contingency table to long format first
tau, p_value = kendalltau(rater_A, rater_B)
print(f"Kendall's τ_b = {tau:.4f}, p = {p_value:.4f}")
```

For gamma, count C and D manually from the table:

```python
gamma = (C - D) / (C + D)
```

---

## When to Use Each Measure

|Goal|Use|
|---|---|
|Test IF association exists|Chi-square|
|Measure direction + strength (ordinal, simple)|**Gamma**|
|Measure direction + strength (conservative)|**Tau-b**|

Use chi-square **and** gamma/tau-b together — they answer different questions.

---

## What to Report

> "A chi-square test indicated a significant association (χ² = 89.3, p < 0.001). Ordinal measures confirmed strong positive concordance: γ = 0.85, τ_b = 0.75."