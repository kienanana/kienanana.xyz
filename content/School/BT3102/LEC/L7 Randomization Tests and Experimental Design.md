---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture7_2026_extended.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-02
updated: 2026-10-02
aliases:
  - BT3102 Lecture 7
---
Source: [[School/BT3102/LEC/PDFs/Lecture7_2026_extended.pdf|Lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

Notation follows [[L6 Potential Outcomes and Causal Effects]]: $D_i$, $Y_i(1)$, $Y_i(0)$, $Y_i^{obs}$ and $\widehat\tau$.

## Sharp null hypotheses

Fisher's **sharp null of no effect** specifies each unit's effect:
$$
H_0:Y_i(1)=Y_i(0)\quad\text{for every }i.
$$
It imputes every missing potential outcome: $Y_i(1)=Y_i(0)=Y_i^{obs}$.

A **zero average-effect null**, $N^{-1}\sum_i\tau_i=0$, permits nonzero effects that cancel. It is not sharp and does not generally impute missing outcomes.

**HW2 extension — constant-effect sharp null:**
$$
H_0^{(\tau_0)}:Y_i(1)=Y_i(0)+\tau_0\quad\forall i,
$$
$$
Y_i(0)=Y_i^{obs}-D_i\tau_0,\qquad
Y_i(1)=Y_i^{obs}+(1-D_i)\tau_0.
$$
Imputed values follow from the hypothesis; they are not additional measurements.

## Fisher randomization test

Let $\Omega$ be the assignment vectors allowed by the actual design. For each hypothetical assignment $d\in\Omega$, reconstruct outcomes under the null:
$$
Y_i(d_i)=d_iY_i(1)+(1-d_i)Y_i(0).
$$
A common statistic is $T(d)=\overline Y_1(d)-\overline Y_0(d)$. Calculate $t_{obs}$ from the original observed data.

For a prespecified **upper-tail** test:
$$
p=\Pr_{H_0,D}(T\ge t_{obs})
=\sum_{d\in\Omega}\Pr(D=d)\,\mathbf1\{T(d)\ge t_{obs}\}.
$$
With equally likely assignments, this is the fraction meeting the tail condition. Include ties and retain multiplicities when different assignments give the same statistic.

**Test sequence:** sharp null → impute outcomes → choose statistic/tail → reproduce assignment design → calculate reference distribution and p-value. Reject when $p\le\alpha$ at the chosen significance level.

The p-value is a probability of an equally/more extreme statistic under the null and design, not the probability that the null is true. Non-rejection does not prove the null. For a nonzero effect null, shuffling labels while holding raw outcomes fixed generally gives the wrong distribution.

## Randomized assignment designs

| Design | Allowed assignments and probability | Main idea |
| --- | --- | --- |
| Bernoulli | Independent $D_i\sim\mathrm{Bernoulli}(p_i)$; $\Pr(D=d)=\prod_i p_i^{d_i}(1-p_i)^{1-d_i}$ | Random group sizes; convenient when participants arrive over time |
| Complete | Fix $N_1$ treated; $\binom N{N_1}$ vectors, each with probability $1/\binom N{N_1}$ | Fix nonempty group sizes |
| Stratified/block | Complete randomization within each pre-treatment block; with independent blocks, $\prod_b\binom{N_b}{N_{1b}}$ vectors | Balance important observed covariates; can improve precision |
| Paired | One treated per pair, independent fair coin per pair; $2^{N/2}$ vectors, each with probability $2^{-N/2}$ | Block size two; match on pre-treatment characteristics |

Equal individual treatment probabilities do not imply equal joint assignment distributions. A paired test cannot use arbitrary fixed-size treatment subsets.

Ordinary Bernoulli assignment allows empty groups, where difference in means is undefined. If conditioning on both groups being nonempty, use the **conditional** assignment distribution; with fair coins it has $2^N-2$ equally likely vectors. This is a different reference design from complete randomization.

## Random assignment versus random sampling

- **Assignment:** who receives treatment; supports causal inference for experimental units.
- **Sampling:** who enters the experiment; supports generalisation to a super-population and introduces additional uncertainty.

The super-population average treatment effect is
$$
\mathrm{ATE}=\mathbb E[Y(1)-Y(0)].
$$
Random assignment alone does not ensure that volunteers represent the wider target population.

## Selection bias decomposition

Using population conditional means:
$$
\mathbb E[Y^{obs}\mid D=1]-\mathbb E[Y^{obs}\mid D=0]
=\underbrace{\mathbb E[Y(1)-Y(0)\mid D=1]}_{\mathrm{ATT}}
+\underbrace{\mathbb E[Y(0)\mid D=1]-\mathbb E[Y(0)\mid D=0]}_{\text{selection bias}}.
$$
**ATT** is average treatment effect on the treated. If $D\perp(Y(1),Y(0))$, selection bias vanishes and ATT equals ATE.

## Monte Carlo randomization — HW2 extension

Sample $M$ assignments from the same design instead of enumerating all:
$$
\widehat p=\frac1M\sum_{j=1}^M\mathbf1\{T_j\ge t_{obs}\}.
$$
This is the simulated tail proportion requested in HW2. It has Monte Carlo error; a fixed seed makes it reproducible, not exact. Sampling treated units without replacement within a repetition does not prevent an assignment recurring across repetitions.

## Connections

- **[[L6 Potential Outcomes and Causal Effects#Average causal effect and its estimator|L6]]:** distinguishes the causal estimand from the random observed estimator; a sharp null makes missing outcomes computable.
- **HW2 P1(c–d), P2:** sharp versus average nulls, design-specific tests, interpretation and simulation audits.
- **[[L9 Random Variable Generation and MCMC|L9 — simulation and sampling]]:** Monte Carlo approximates a distribution by repeated random draws; its randomness here reproduces treatment assignment.

For lecture examples: [[Lecture7_2026_extended.pdf#page=6|Fisher test, pp. 6–18]] · [[Lecture7_2026_extended.pdf#page=19|designs, pp. 19–28]] · [[Lecture7_2026_extended.pdf#page=29|sampling/selection bias, pp. 29–35]].
