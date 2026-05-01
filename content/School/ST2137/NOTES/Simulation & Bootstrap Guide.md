---
class: note
tags:
  - y3s2
  - statistics
  - revision
source:
related:
author:
date: 2026-04-27
updated: 2026-04-27
aliases:
---
## Step 1 — When to simulate instead of calculate

| Situation | Method |
|---|---|
| Need a confidence interval but distribution is unknown or non-Normal | Bootstrap CI |
| Distributional assumptions for a test are violated | Permutation test |
| Need to evaluate $\int h(x) f(x) \, dx$ analytically intractable | Monte Carlo integration |
| Want to validate whether a test/CI procedure actually works at the claimed level | Simulation study |

> **Core justification:** the Strong Law of Large Numbers guarantees that $\bar{X} \to E(X)$ as $n \to \infty$, regardless of the distribution. This is why averaging simulated values gives valid estimates.

---

## Step 2 — Monte Carlo Integration

**Goal:** estimate $\int h(x) f(x) \, dx = E[h(X)]$ where $X \sim f$.

```
1. Express the integral as an expectation E[h(X)] under some pdf f
2. Generate X₁, X₂, ..., Xₙ ~ f  (use rnorm / np.random.normal / scipy.stats etc.)
3. Estimate: (1/n) Σ h(Xᵢ)
4. Precision improves as n increases (CLT gives SE ≈ s/√n)
```

> **Example:** $\int_0^1 e^{2x} \, dx$ — let $X \sim \text{Unif}(0,1)$ and $h(X) = e^{2X}$. Then the integral $= E[e^{2X}]$, estimated by averaging $e^{2X_i}$ over many draws.

> **Always set a seed** for reproducibility: `set.seed(42)` in R, `np.random.seed(42)` or `random_state=42` in Python.

---

## Step 3 — Bootstrap vs Permutation Test

| | Bootstrap CI | Permutation test |
|---|---|---|
| **Question** | What is the uncertainty around my statistic? | Could this observed difference have arisen by chance if $H_0$ is true? |
| **When to use** | Distribution unknown; robust alternative to t-based CI | Distributional assumptions fail; exact $p$-value needed |
| **How it works** | Resample *with replacement* from original data | Randomly shuffle group labels, recompute test statistic |
| **Output** | Confidence interval | $p$-value |
| **$H_0$ required?** | No | Yes ($H_0$: groups are exchangeable) |

---

## Step 4 — Bootstrap CI Recipe

```
Given: data x₁, x₂, ..., xₙ; statistic of interest θ̂ (e.g. trimmed mean)

1. Resample with replacement: draw n values from x₁..xₙ → bootstrap sample x*
2. Compute θ̂* on x*
3. Repeat B times (B = 1000–10,000)
4. Percentile CI: [2.5th percentile of θ̂*, 97.5th percentile of θ̂*]
```

> **Why resample *with* replacement?** Each bootstrap sample mimics drawing a new sample from the population. The variability across bootstrap samples estimates the variability of $\hat{\theta}$ across real samples.

> **Bootstrap CI vs t-based CI:** bootstrap CIs are asymmetric when the sampling distribution is skewed, which makes them more accurate. t-based CIs are symmetric by construction and can be badly wrong for skewed distributions or small $n$.

---

## Step 5 — Permutation Test Recipe

```
Given: group 1 values x₁..xₙ₁ and group 2 values y₁..yₙ₂

1. Compute observed statistic: d_obs = mean(x) - mean(y)
2. Pool all n₁ + n₂ values together
3. Randomly assign n₁ values to "group 1", remaining to "group 2"
4. Compute permuted statistic d*
5. Repeat B times (B ≥ 1000)
6. p-value = proportion of |d*| ≥ |d_obs|
```

> **Two-sided vs one-sided:** for a two-sided test use $|d^*| \geq |d_{\text{obs}}|$; for one-sided use the raw sign.

> **Permutation test vs Wilcoxon Rank-Sum:** both are non-parametric. Permutation test is more flexible (works for any statistic, not just rank sums); Wilcoxon has published exact tables and is faster for standard location tests.

---

## Step 6 — Simulation Study Structure (for validation questions)

```
To check if a procedure achieves its claimed level (e.g. 95% CI coverage):

1. Set the true parameter value (e.g. μ = 0)
2. Generate a dataset from a known distribution
3. Apply the procedure (compute CI, run test)
4. Record whether it succeeded (CI contains μ; test gives correct decision)
5. Repeat 1000–5000 times
6. Empirical rate = count of successes / total replications
   → Compare to claimed level (e.g. should be ≈ 0.95 for 95% CI)
```

> **Type I error check:** generate data under $H_0$ (equal means), run the test, count how often you reject. Should equal $\alpha$. If it's much higher, the test is liberal; much lower, it's conservative.

---

See also: [[L10 Simulation]] · [[Robust Statistics Guide]] · [[Test Selection Guide]]
