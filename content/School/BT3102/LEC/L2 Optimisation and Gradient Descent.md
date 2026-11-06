---
class: lecture
tags:
  - y4s1
  - bt3102
  - math/linear-algebra
  - math/optimisation/gradient-descent
  - math/statistics/regression
source: "[[School/BT3102/LEC/PDFs/Lecture2_2026.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-09-11
updated: 2026-10-02
aliases:
  - BT3102 Lecture 2
---
Source: [[School/BT3102/LEC/PDFs/Lecture2_2026.pdf|Annotated lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

## Positive definite and positive semidefinite matrices

For real symmetric $A$:
$$
A\succ0\iff x^TAx>0\ \text{for every }x\ne0,\qquad
A\succeq0\iff x^TAx\ge0\ \text{for every }x.
$$
Equivalently, eigenvalues are all positive / all nonnegative. This concerns a quadratic form, not the signs of individual entries. If $A\succ0$, its inverse exists and is positive definite.

## Stationary points and minima

Unconstrained optimisation: $\min_{w\in\mathbb R^n}f(w)$. Constraints restrict the feasible region. In model training, parameters are decision variables; training data are fixed.

- **Local minimum:** $f(w^*)\le f(w)$ in a neighbourhood of $w^*$.
- **Global minimum:** this holds throughout the domain.
- **Stationary point:** $\nabla f(w^*)=0$.

For a differentiable unconstrained local minimum, stationarity is **necessary**, not sufficient. For differentiable convex $f$ on $\mathbb R^n$, stationarity is sufficient for a global minimum.

**HW1 supplement — second-order classification:** for $C^2$ functions, evaluate $Q=\nabla^2f(w^*)$ at a stationary point:

| Hessian | Conclusion |
| --- | --- |
| Positive definite | Strict local minimum |
| Negative definite | Strict local maximum |
| Indefinite (positive and negative eigenvalues) | Saddle point |
| Semidefinite with zero eigenvalues | Test may be inconclusive |

A local minimum necessarily has a positive semidefinite Hessian. Local curvature alone does not establish global optimality.

## Least squares

Rows of $X$ are feature vectors; include a column of ones for an intercept.
$$
f(w)=\frac1m\|Xw-y\|_2^2,\qquad
\nabla f(w)=\frac2mX^T(Xw-y),\qquad
\nabla^2f(w)=\frac2mX^TX\succeq0.
$$
Normal equations and solution:
$$
X^TXw=X^Ty,\qquad w^*=(X^TX)^{-1}X^Ty.
$$
The inverse formula and uniqueness require **full column rank**. Without it, the objective remains convex but minimisers need not be unique.

## Logistic regression: from likelihood to loss

For $y_i\in\{0,1\}$:
$$
p_i=\sigma(w^Tx_i),\qquad \sigma(z)=\frac1{1+e^{-z}},\qquad
L(w)=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}.
$$
Independent observations justify the product. Maximising $L$ is equivalent to maximising $\log L$ and minimising negative average log-likelihood:
$$
f(w)=-\frac1m\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)],
$$
$$
\nabla f(w)=\frac1mX^T(p-y).
$$
Log turns products into sums, avoiding multiplication of tiny probabilities. Unlike least squares, the stationarity equations generally need an iterative solution.

## Gradient descent

A **descent direction** decreases the objective for every sufficiently small positive step. A sufficient condition is $\nabla f(w)^Tp<0$.
$$
p_k=-\nabla f(w_k),\qquad w_{k+1}=w_k+\alpha_kp_k,\quad\alpha_k>0.
$$
With fixed $\alpha$, movement length is $\alpha\|\nabla f(w_k)\|_2$. A downhill direction still needs a suitable step size.

Stop when $\|\nabla f(w_k)\|_2\le\varepsilon$ **or** a computation/iteration limit is reached. A small gradient indicates approximate stationarity. Initialisation matters for nonconvex problems; compare total runtime as well as iteration count.

- **Line search:** choose direction, then distance.
- **Trust region:** choose a radius, then optimise a local model within it.

## Connections

- **[[L1 Course Introduction#Taylor approximations and the Hessian|L1]]** supplies slope and curvature for optimisation.
- **[[L3 Line Search and Momentum|L3]]** chooses the step size and adds history to GD.
- **[[L4 Stochastic Gradient Descent and Newton Methods|L4]]** replaces full gradients with noisy estimates or uses Hessian information.
- **[[L6 Potential Outcomes and Causal Effects|L6]]: prediction versus causation:** fitting a predictive relationship does not establish an intervention effect.

For examples: [[Lecture2_2026.pdf#page=7|stationary points, pp. 7–8]] · [[Lecture2_2026.pdf#page=9|regression, pp. 9–15]] · [[Lecture2_2026.pdf#page=17|GD and frameworks, pp. 17–26]].
