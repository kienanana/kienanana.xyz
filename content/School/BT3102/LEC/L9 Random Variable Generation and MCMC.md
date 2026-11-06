---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture9_2026_extend.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-28
updated: 2026-10-28
aliases:
  - BT3102 Lecture 9
---
Source: [[School/BT3102/LEC/PDFs/Lecture9_2026_extend.pdf|Lecture PDF]] · [[BT3102#Lecture study notes|Lecture index]]

## CDF: the distribution to reproduce

The **cumulative distribution function** is $F(x)=\Pr(X\le x)$. It determines the entire distribution, since
$$
\Pr(a<X\le b)=F(b)-F(a).
$$
For an absolutely continuous distribution, $F(x)=\int_{-\infty}^x f(z)\,dz$. Matching the support, mean or variance alone does not establish the correct distribution. A density value $f(x)$ is not the probability of the single point $x$.

## Inverse CDF sampling

Draw $U\sim\mathrm{Uniform}(0,1)$ and set
$$
X=F^{-1}(U),\qquad F^{-1}(u)=\inf\{x:F(x)\ge u\}.
$$
The **generalised inverse** handles jumps and flat portions of a CDF. An ordinary inverse requires stricter conditions than continuity alone.

For a continuous strictly increasing CDF, the proof is
$$
\Pr(F^{-1}(U)\le x)=\Pr(U\le F(x))=F(x).
$$
Thus the transformed variable has the desired CDF.

**Exponential example:** for rate $\lambda>0$,
$$
F(x)=1-e^{-\lambda x}\ (x\ge0)
\quad\Longrightarrow\quad X=-\frac{\log(1-U)}{\lambda}.
$$
Equivalently use $-\log U/\lambda$, since $1-U$ is also uniform. Mean is $1/\lambda$; do not confuse rate with scale. Avoid evaluating $\log0$ at numerical endpoints.

**Discrete example:** if $\Pr(X=x_k)=p_k$, form $c_k=\sum_{j\le k}p_j$ and return the first $x_k$ with $U\le c_k$. For probabilities $(0.2,0.5,0.3)$, the intervals are $(0,0.2]$, $(0.2,0.7]$, $(0.7,1)$.

**Normal example:** $X=\Phi^{-1}(U)$ has the standard normal distribution. Without a direct inverse routine, solve $\Phi(x)-U=0$ numerically. The lecture's implementation combines integration and root finding, making each draw expensive; theoretical applicability does not imply computational efficiency.

## Acceptance–rejection sampling

The lecture's geometric idea: generate candidate points uniformly in a rectangle and retain points **under the target density**. More points survive in regions of higher density.

For target density $f$ supported on $[a,b]$, choose $h\ge\sup_x f(x)$:

1. Draw independent $V\sim\mathrm{Uniform}(a,b)$ and $W\sim\mathrm{Uniform}(0,h)$.
2. If $W\le f(V)$, return $X=V$; otherwise redraw both.

The accepted horizontal coordinate has density proportional to $f$. When the rectangle encloses the entire normalised density, acceptance probability is $1/((b-a)h)$.

**Rectangle limitation:** a finite horizontal interval cannot cover the entire normal support. Restricting normal candidates to $[a,b]$ and filtering below $\phi$ produces a **truncated normal**, an approximation to the full normal if tail mass is small. Enlarging the rectangle reduces truncation but can waste more proposals.

The general density-envelope form makes the requirement explicit. Choose an easy proposal density $g$ and finite $c$ such that $f(x)\le cg(x)$ everywhere, then draw $V\sim g$, independent $U\sim\mathrm{Uniform}(0,1)$, and accept if
$$
U\le\frac{f(V)}{cg(V)}.
$$
For normalised $f,g$, acceptance rate is $1/c$ and expected proposals per accepted draw is $c$. The proposal must cover the target support; an invalid envelope gives an invalid sampler.

| Method | Main operation | Main computational issue |
| --- | --- | --- |
| Inverse CDF | Transform one uniform draw using a quantile | Inversion may be expensive; one output per input |
| Acceptance–rejection | Filter proposals using density values | A random number of proposals is needed; poor envelopes waste draws |

## Markov chain Monte Carlo

**Monte Carlo** estimates quantities using simulated draws. **MCMC** constructs a Markov chain with the desired target as its stationary distribution, then uses its trajectory for estimation. This builds on [[L8 Markov Chains and PageRank#Stationary, limiting and long-run distributions|L8]]; stationary distribution alone does not guarantee convergence from an arbitrary start.

For target $\pi$ and a **symmetric proposal** $q(y\mid x)=q(x\mid y)$, the Metropolis rule is:

1. From current state $x$, propose $y$.
2. Accept with probability $\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\}$.
3. If rejected, **remain at $x$**; record that repeated state in the chain.

Moves to larger target density are accepted; moves to smaller density can also be accepted. The normalising constant cancels in the ratio. The simple ratio requires proposal symmetry; asymmetric proposals need a proposal-probability correction.

After an initial transient, estimate expectations by averaging $h(X_t)$ along the chain. Consecutive MCMC draws are generally **dependent**. Discarding an initial burn-in can reduce initialisation effects but does not itself prove convergence. Unlike independent rejection sampling, an MCMC rejection still contributes an observation of the current state.

## Connections

- **[[L8 Markov Chains and PageRank#Computing and simulating|L8]]:** discrete inverse CDF sampling selects the next state from a transition column.
- **[[L7 Randomization Tests and Experimental Design#Monte Carlo randomization — HW2 extension|L7]]:** a simulated p-value is an average of tail indicators; the sampling mechanism must reproduce the intended distribution.
- **[[L4 Stochastic Gradient Descent and Newton Methods|L4]]:** numerical inverse-CDF sampling can become a root-finding problem.
- **[[L10 Markov Decision Processes and Value Iteration|L10]]:** simulation can evaluate a fixed policy; value iteration uses known transitions to optimise without enumerating simulated policies.

For lecture examples: [[Lecture9_2026_extend.pdf#page=4|CDF/inversion, pp. 4–15]] · [[Lecture9_2026_extend.pdf#page=16|acceptance–rejection, pp. 16–27]] · [[Lecture9_2026_extend.pdf#page=28|MCMC/Metropolis, pp. 28–30]].
