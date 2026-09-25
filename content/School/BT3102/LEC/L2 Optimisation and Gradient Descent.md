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
updated: 2026-09-16
aliases:
  - BT3102 Lecture 2
---
Source: [[School/BT3102/LEC/PDFs/Lecture2_2026.pdf|Annotated lecture PDF]]. Page references use PDF page numbers.

## Overview
- Positive definiteness describes the sign of quadratic forms.
- Optimisation seeks good parameters; stationarity alone does not certify a minimum.
- Least squares has a closed-form solution under a rank condition; logistic regression motivates iteration.
- Gradient descent combines a direction, a step size and a stopping rule.

## Positive definite and positive semidefinite matrices

For a real symmetric matrix $A$,

$$
A\succ0\iff x^TAx>0\quad\text{for every }x\ne0,
$$
$$
A\succeq0\iff x^TAx\ge0\quad\text{for every }x.
$$

This is a property of the **quadratic form**, not a requirement that every matrix entry be positive.

![[Lecture2_2026.pdf#page=3]]

**Key takeaway:** $x^TAx=x^T(Ax)$ is a dot product. For a positive definite matrix, $x$ and $Ax$ make an acute angle: this is the slide's “same side” intuition. In Taylor's quadratic term, the same expression describes curvature along a displacement.

## Optimisation setup

Unconstrained optimisation minimises $f(w)$ over $w\in\mathbb R^n$. Constrained optimisation restricts $w$ to a feasible region, for example using $c_i(w)=0$ and $c_i(w)\ge0$. The lecture assumes at least $f\in C^1$, sometimes $C^2$.

For model training, **the decision variables are the model parameters**, while the training data are fixed. An example objective is average squared prediction error:

$$
f(w)=\frac1m\sum_{i=1}^m\left[y^{(i)}-g(w\mid x^{(i)})\right]^2.
$$

Source: [[Lecture2_2026.pdf#page=4|pp. 4–5]].

## Stationary points and minima

- **Local minimum:** $f(w^*)\le f(w)$ for all $w$ in some neighbourhood of $w^*$.
- **Global minimum:** the inequality holds throughout the domain.
- **Stationary point:** $\nabla f(w^*)=0$.

**First-order necessary condition:** an unconstrained local minimiser of a differentiable function satisfies $\nabla f(w^*)=0$. This condition alone also admits maxima and stationary points that are not extrema. Do not apply it blindly to constrained boundary minima.

![[Lecture2_2026.pdf#page=7]]

**Key takeaway:** a zero slope cannot classify a point. The diagram groups several stationary behaviours; additional structure or curvature information is needed. For a differentiable convex objective on $\mathbb R^n$, a stationary point is a global minimiser.

## Worked example: least squares

With training examples as rows of $X$ and targets in $y$,

$$
f(w)=\frac1m\|Xw-y\|_2^2,\qquad
\nabla f(w)=\frac2mX^T(Xw-y).
$$

Setting the gradient to zero gives the **normal equations**:

$$
X^TXw=X^Ty.
$$

If $X$ has full column rank, $X^TX$ is invertible and

$$
w^*=(X^TX)^{-1}X^Ty.
$$

Include a column of ones in $X$ if fitting an intercept. The objective is convex because its Hessian is $2X^TX/m\succeq0$; full column rank makes it positive definite and the minimiser unique. If the rank condition fails, the inverse formula is unavailable and minimisers need not be unique.

Source: [[Lecture2_2026.pdf#page=10|scalar derivation, p. 10]] and [[Lecture2_2026.pdf#page=11|matrix formulation, p. 11]]. Remember the normal equations and rank assumption rather than every expanded scalar term.

## Logistic regression: from likelihood to loss

For binary targets $y_i\in\{0,1\}$, define

$$
p_i=\sigma(w^Tx_i),\qquad \sigma(z)=\frac1{1+e^{-z}}.
$$

The probability assigned to the observed label is $p_i^{y_i}(1-p_i)^{1-y_i}$. Under the lecture's independent-observation assumption, the likelihood is the product of these terms.

![[Lecture2_2026.pdf#page=15]]

**Key takeaway:** logarithms turn the product into a sum and preserve its maximiser because log is strictly increasing. Negating and averaging gives the **negative log-likelihood / binary cross-entropy**:

$$
f(w)=-\frac1m\sum_{i=1}^m\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right].
$$

This avoids directly multiplying many tiny probabilities. Unlike least squares, the stationarity equations generally have no simple closed-form solution, so we optimise iteratively. The gradient simplifies to

$$
\nabla f(w)=\frac1m\sum_{i=1}^m(p_i-y_i)x_i=\frac1mX^T(p-y).
$$

This is an equivalent form of [[Lecture2_2026.pdf#page=22|the gradient on p. 22]]: each example contributes prediction error multiplied by its features.

## Gradient descent

A **descent direction** $d$ decreases $f(w+\alpha d)$ for every sufficiently small positive $\alpha$. For differentiable $f$, $\nabla f(w)^Td<0$ is sufficient.

From [[L1 Course Introduction#Gradients and directional derivatives|the directional derivative]], the negative gradient is the Euclidean steepest descent direction. The standard update is

$$
w_{k+1}=w_k-\alpha_k\nabla f(w_k),\qquad \alpha_k>0.
$$

Even with fixed learning rate $\alpha$, the actual movement has length $\alpha\|\nabla f(w_k)\|_2$. A downhill direction guarantees improvement only for sufficiently small steps: an excessive step can overshoot.

Stop using a criterion such as $\|\nabla f(w_k)\|_2\le\varepsilon$ **and a hard iteration/computation limit**. A small gradient signals approximate stationarity, not proof of a global minimum. Initialisation can affect the outcome for nonconvex problems.

## Choosing the next iterate

[[Lecture2_2026.pdf#page=26|Line search versus trust region, p. 26]]:

- **Line search:** choose a direction first, then choose how far to move along it.
- **Trust region:** set a radius, then optimise a local model within that radius to choose the step.

The lecturer's practical emphasis on [[Lecture2_2026.pdf#page=24|pp. 24–25]] is to compare total computational cost. Fewer iterations may require more expensive information per iteration. The practical goal is a sufficiently good point within the available budget.

## Important results

- $\nabla f(w^*)=0$ is necessary for an unconstrained differentiable minimum, but generally insufficient.
- Least squares: $X^TXw=X^Ty$; the inverse formula requires full column rank.
- Logistic loss gradient: $X^T(p-y)/m$.
- Gradient descent: $w_{k+1}=w_k-\alpha_k\nabla f(w_k)$.
