---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture6_2026_extended.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-02
updated: 2026-10-02
aliases:
  - BT3102 Lecture 6
---
Source: [[School/BT3102/LEC/PDFs/Lecture6_2026_extended.pdf|Lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

## Correlation versus causation

**Correlation:** variables are statistically related. **Causation:** intervening on one changes the other. A causal claim requires temporal precedence, covariation and ruling out plausible alternative explanations.

A **confounder** helps explain an observed treatment–outcome relationship without the proposed treatment effect. Controls and placebos address alternative explanations; they do not automatically make different people comparable. Before/after comparisons can reflect time, practice or environmental changes.

## Potential outcomes

For unit $i$ at a specified time:

- $D_i\in\{0,1\}$: received treatment indicator.
- $Y_i(1),Y_i(0)$: outcomes under treatment and control.
- $Y_i^{obs}$: the outcome actually observed.

$$
Y_i^{obs}=D_iY_i(1)+(1-D_i)Y_i(0),\qquad
\tau_i=Y_i(1)-Y_i(0).
$$
The individual causal effect compares **the same unit at the same time** under two alternatives. It is defined independently of which treatment was received.

**Fundamental problem of causal inference:** only one potential outcome is observed per unit; the counterfactual is missing. Individual effects cannot generally be identified without additional assumptions. Observing the same person later does not reveal the missing outcome at the original time.

## SUTVA

**Stable Unit Treatment Value Assumption** has two parts:

1. **No interference:** unit $i$'s potential outcomes do not depend on other units' assignments.
2. **No hidden treatment versions:** the defined treatment corresponds to one well-defined intervention.

Spillovers, contagion and competition can violate the first; varying treatment doses/versions can violate the second. Without no-interference, outcomes may need notation $Y_i(D_1,\ldots,D_N)$ rather than just $Y_i(D_i)$.

## Average causal effect and its estimator

For the fixed population of $N$ experimental units:
$$
\tau=\frac1N\sum_i[Y_i(1)-Y_i(0)].
$$
The observed difference in group means is
$$
\widehat\tau=\overline Y_1^{obs}-\overline Y_0^{obs}
=\frac{\sum_iD_iY_i^{obs}}{N_1}-\frac{\sum_i(1-D_i)Y_i^{obs}}{N_0},
$$
where $N_1=\sum_iD_i$ and $N_0=N-N_1$; both must be nonzero.

**Estimand** $\tau$: the effect we want, using potential outcomes. **Estimator** $\widehat\tau$: the quantity we calculate from observed data.

## Why assignment matters

Treatment groups selected according to potential outcomes need not represent comparable populations. Random assignment breaks this selection mechanism:
$$
D_i\ \perp\ (Y_i(1),Y_i(0)).
$$
For complete randomization with fixed nonempty group sizes,
$$
\mathbb E_D[\widehat\tau]=\tau.
$$
The expectation is over assignments, holding the units' potential outcomes fixed. Unbiasedness does not mean a single experiment gives the exact effect or perfectly balanced groups.

Equal treatment/control probabilities are not necessary for causal identification. The assignment probabilities and design still matter; differing probabilities across units can require a different estimator.

## Connections

- **[[L2 Optimisation and Gradient Descent#Logistic regression: from likelihood to loss|L2]] / TUT4:** a predictive model captures associations; intervention effects require a causal argument.
- **[[L7 Randomization Tests and Experimental Design#Fisher randomization test|L7]]:** random assignment provides the reference distribution for testing a causal hypothesis.
- **[[L7 Randomization Tests and Experimental Design#Random assignment versus random sampling|L7]]:** distinguish validity within the experiment from generalisation to a larger population.
- **HW2 P1(a–b):** evaluate SUTVA and before/after claims; these definitions also supply the setup for P2.

For examples: [[Lecture6_2026_extended.pdf#page=8|controls/confounding, pp. 8–21]] · [[Lecture6_2026_extended.pdf#page=22|potential outcomes/SUTVA, pp. 22–30]] · [[Lecture6_2026_extended.pdf#page=31|average effects/assignment, pp. 31–41]].
