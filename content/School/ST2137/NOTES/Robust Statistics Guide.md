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
## Step 1 — Should you use robust methods?

**Check these triggers:**

| Trigger | Why it matters |
|---|---|
| Clear outliers in histogram or boxplot | Mean and SD are pulled toward outliers; unreliable |
| Distribution is heavily right- or left-skewed | Mean no longer represents the "centre" |
| Small $n$ with fat-tailed or unknown distribution | Normal-based methods break down |
| Max SD / Min SD > 2 across groups | Equal variance assumption fails for t-test / ANOVA |

> **Breakdown point:** the fraction of contaminated data an estimator can tolerate before it becomes arbitrarily bad. Mean has breakdown point = 0 (one extreme outlier destroys it). Median has breakdown point = 50%.

---

## Step 2 — Choosing a Location Estimator

| Estimator | Formula | Breakdown point | When to use |
|---|---|---|---|
| **Mean** | $\bar{X} = \frac{1}{n}\sum X_i$ | 0% | Data is Normal with no outliers |
| **Median** | Middle value | 50% | Heavy skew or many outliers |
| **$\gamma$-Trimmed mean** | Drop smallest and largest $g = \lfloor \gamma n \rfloor$ values, average the rest | $\gamma$ | Moderate outliers; recommended $\gamma \in (0, 0.2]$ |
| **Winsorised mean** | Replace smallest $g$ with $X_{(g+1)}$, largest $g$ with $X_{(n-g)}$, then average | $\gamma$ | Same situations as trimmed mean; keeps sample size intact |

> **Trimmed vs Winsorised:** trimmed mean *removes* extreme values; Winsorised *replaces* them with the nearest kept value. Winsorised variance is used to compute the SE of the trimmed mean — they go together.

> Use $\gamma = 0.2$ (20% trim) as a sensible default when you suspect outlier contamination but don't know the exact fraction.

---

## Step 3 — Choosing a Scale Estimator

| Estimator | Formula | For Normal, converts to $\hat{\sigma}$ by | Breakdown point |
|---|---|---|---|
| **SD** | $\sqrt{\frac{1}{n-1}\sum(X_i - \bar{X})^2}$ | already $\hat{\sigma}$ | 0% |
| **IQR** | $Q_3 - Q_1$ | $\hat{\sigma} \approx \text{IQR} / 1.35$ | 25% |
| **MAD** | $\text{median}(|X_i - \text{median}(X)|)$ | $\hat{\sigma} \approx 1.4826 \times \text{MAD}$ | 50% |

> **Rule of thumb:** if you're using a robust location estimator, use a robust scale estimator too. Pair trimmed/Winsorised mean with IQR or MAD.

---

## Step 4 — Quick Flowchart

```
Is your data approximately Normal with no obvious outliers?
│
├─ Yes → Mean + SD
│
└─ No
    ├─ Moderate outliers or mild skew
    │   └─ γ-Trimmed mean (γ ≤ 0.2) + IQR or MAD
    │
    ├─ Heavy skew or many outliers
    │   └─ Median + MAD
    │
    └─ Unknown distribution / can't tell
        └─ Median + MAD (safest default)
            or Bootstrap CI (see Simulation & Bootstrap Guide)
```

---

## Step 5 — Asymptotic Relative Efficiency (ARE)

> **ARE** tells you how many extra observations the non-robust method needs to match the robust one.

- $\text{ARE}(\tilde{\theta}; \hat{\theta}) = \lim_{n \to \infty} \frac{\text{Var}(\hat{\theta})}{\text{Var}(\tilde{\theta})}$
- Trimmed mean vs mean on pure Normal: ARE ≈ 88% (you "lose" 12% efficiency for robustness)
- Trimmed mean vs mean on 10%-contaminated Normal: ARE > 100% (robust estimator is *better*)

> The ARE trade-off: robust estimators are slightly less efficient on clean Normal data, but dramatically better once contamination exists. For real data where the distribution is unknown, robustness is usually worth the cost.

---

See also: [[L5 Robust Statistics]] · [[EDA Guide]] · [[Simulation & Bootstrap Guide]]
