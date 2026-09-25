---
class: lecture
tags:
  - y4s1
  - bt3102
  - math/optimisation/gradient-descent
  - math/optimisation/stochastic-gradient-descent
  - math/optimisation/newton-method
  - math/optimisation/quasi-newton
  - math/linear-algebra
source: "[[School/BT3102/LEC/PDFs/Lecture4_2026_extended.pdf]]"
related:
  - "[[BT3102]]"
  - "[[L3 Line Search and Momentum]]"
date: 2026-09-16
updated: 2026-09-16
aliases:
  - BT3102 Lecture 4
---
Source: [[School/BT3102/LEC/PDFs/Lecture4_2026_extended.pdf|Lecture PDF]]. Page references use PDF page numbers.

## Overview
- Stochastic gradient descent (SGD) trades exact gradients for cheaper, noisy updates.
- Newton's method uses curvature to choose a step, with fast local convergence but greater cost and weaker guarantees far from a minimum.
- Quasi-Newton methods and coordinate rescaling aim to improve the geometry without computing an exact inverse Hessian each iteration.

The opening recap builds on [[L3 Line Search and Momentum]]. On [[Lecture4_2026_extended.pdf#page=5|p. 5]], **random restarts** change the starting point of independent runs; **momentum** uses history within a run. Accumulated velocity may carry a trajectory through flat regions or shallow minima, but escape is not guaranteed. [[Lecture4_2026_extended.pdf#page=6|p. 6]] motivates looking beyond local minima to saddle points in high-dimensional landscapes.

## Why full gradients become expensive

Many training objectives average losses over $m$ examples:

$$
f(w)=\frac1m\sum_{i=1}^m h_i(w),\qquad
\nabla f(w)=\frac1m\sum_{i=1}^m\nabla h_i(w).
$$

Every full-gradient update requires all $m$ component gradients. When $m$ is large, this can dominate the cost. See [[Lecture4_2026_extended.pdf#page=9|p. 9]].

### Logistic regression: the label convention changes

Unlike [[L2 Optimisation and Gradient Descent#Logistic regression: from likelihood to loss|L2's binary labels]], L4 uses $y_i\in\{-1,+1\}$:

$$
h_i(w)=\log\left(1+e^{-y_iw^Tx_i}\right),\qquad
\nabla h_i(w)=-\frac{y_ix_i}{1+e^{y_iw^Tx_i}}.
$$

The margin $y_iw^Tx_i$ is positive when the score agrees with the label; increasing it reduces the loss. This is the same binary logistic loss after recoding $y_{\pm}=2y_{01}-1$. Source: [[Lecture4_2026_extended.pdf#page=7|loss, p. 7]] and [[Lecture4_2026_extended.pdf#page=8|gradient, p. 8]].

## Stochastic and mini-batch gradient descent

At iteration $k$, sample a uniform random index $i_k$, or a random mini-batch $B_k$:

$$
\widehat g_k=\nabla h_{i_k}(w_k)
\quad\text{or}\quad
\widehat g_k=\frac1{|B_k|}\sum_{i\in B_k}\nabla h_i(w_k),
\qquad
w_{k+1}=w_k-\alpha_k\widehat g_k.
$$

For uniform sampling from the fixed dataset, conditional on the current iterate,

$$
\mathbb E[\widehat g_k\mid w_k]=\nabla f(w_k).
$$

Thus $\widehat g_k=\nabla f(w_k)+\xi_k$, with zero-mean sampling noise. The equality is exact for this sampling scheme; the lecture also discusses the population intuition of independent training examples. An individual sampled direction need not decrease the full objective. Source: [[Lecture4_2026_extended.pdf#page=12|mini-batches, p. 12]] and [[Lecture4_2026_extended.pdf#page=13|average-direction intuition, p. 13]].

![[Lecture4_2026_extended.pdf#page=14]]

**Key takeaway:** the noisy path may need more iterations, but each costs much less. Randomness can help move through some difficult regions, and a chosen learning-rate schedule avoids an expensive full-objective line search at every update. Compare total computation, not iteration counts alone.

### Stopping with noisy gradients

A tiny gradient from one small batch does not reliably establish stationarity. [[Lecture4_2026_extended.pdf#page=15|p. 15]] suggests estimating the gradient using a much larger sample and considering changes in parameters or objective values:

$$
\left\|\frac1R\sum_{i\in S_R}\nabla h_i(w_k)\right\|\le\varepsilon,
\qquad
\|w_{k+1}-w_k\|\le\varepsilon,
\qquad
|f(w_{k+1})-f(w_k)|\le\varepsilon.
$$

These are diagnostics rather than interchangeable guarantees: tiny learning rates also produce tiny updates, and evaluating the full loss can be costly. Combine sustained evidence of little progress with a computational limit.

## Newton's method: root finding versus optimisation

For a scalar equation $r(w)=0$, replace $r$ by its tangent line and solve that line for its root:

$$
0\approx r(w_k)+r'(w_k)(w_{k+1}-w_k)
\quad\Longrightarrow\quad
w_{k+1}=w_k-\frac{r(w_k)}{r'(w_k)}.
$$

![[Lecture4_2026_extended.pdf#page=19]]

**Key takeaway:** the tangent's horizontal-axis intercept becomes the next iterate. To optimise $f$, apply root finding to **$r=f'$**, giving $w_{k+1}=w_k-f'(w_k)/f''(w_k)$. Solving $f(w)=0$ and minimising $f(w)$ are different tasks.

### Worked example: computing $\sqrt3$

For the example introduced on [[Lecture4_2026_extended.pdf#page=17|p. 17]], set $r(w)=w^2-3$. Then

$$
w_{k+1}=\frac12\left(w_k+\frac3{w_k}\right).
$$

Starting from $w_0=2$ gives $w_1=1.75$ and $w_2\approx1.732143$. Each step solves a local linear approximation to $r$, without needing a symbolic square-root formula.

## Newton optimisation: minimise a local quadratic model

Let $g_k=\nabla f(w_k)$ and $Q_k=\nabla^2f(w_k)$. Taylor's approximation gives

$$
q_k(p)=f(w_k)+g_k^Tp+\frac12p^TQ_kp.
$$

Setting its gradient to zero yields

$$
Q_kp_k=-g_k,\qquad
p_k=-Q_k^{-1}g_k,\qquad
w_{k+1}=w_k+p_k.
$$

When $Q_k\succ0$, this stationary point is the quadratic model's unique minimiser. The **pure Newton step uses $\alpha_k=1$** along $p_k$. In computation, solve the linear system rather than explicitly forming the inverse.

![[Lecture4_2026_extended.pdf#page=22]]

**Key takeaway:** the Hessian adjusts movement for curvature in different directions. Newton minimises a local quadratic model, which need not match the true function well far from the current point. This extends [[L1 Course Introduction#Taylor approximations and the Hessian|L1's Taylor approximation]].

### Fast convergence is local

Near a minimiser $w^*$ with positive definite Hessian, Newton can converge **quadratically** under suitable smoothness assumptions (including a locally Lipschitz Hessian) and a sufficiently close starting point:

$$
\|w_{k+1}-w^*\|\le C\|w_k-w^*\|^2.
$$

This describes how quickly a small error shrinks; it is not a guarantee of reaching a minimum from any initial point.

## Why Newton can fail

- **Cost:** a dense $n\times n$ Hessian requires $O(n^2)$ storage; a general dense factorisation/solve costs $O(n^3)$. See [[Lecture4_2026_extended.pdf#page=24|p. 24]].
- **Undefined step:** the required second derivatives may not exist, or the Hessian may be singular.
- **Wrong direction:** an indefinite Hessian can produce an ascent direction.
- **Poor initialisation:** the local model may give unhelpful steps or cycling.

![[Lecture4_2026_extended.pdf#page=25]]

**Key takeaway:** the left example concerns root finding for $r(w)=w^3-2w+2$. Starting at $0$, Newton cycles $0\to1\to0$. The right diagram shows an optimisation step following an unsuitable quadratic model. Both illustrate why fast local behaviour does not imply global convergence.

### When is Newton's direction descent?

For $g_k\ne0$ and $Q_k\succ0$,

$$
g_k^Tp_k=-g_k^TQ_k^{-1}g_k<0.
$$

Positive definiteness makes the inverse positive definite too. Without it, the sign is not assured. Source: [[Lecture4_2026_extended.pdf#page=26|p. 26]].

**Qualification to the slide:** a twice-differentiable local minimum need only have a positive **semidefinite** Hessian. Positive definiteness is an additional condition, not automatic; $f(w)=w^4$ at $0$ is a simple counterexample.

## Quasi-Newton methods and rescaling

[[Lecture4_2026_extended.pdf#page=28|p. 28]] motivates an intermediate update:

$$
w_{k+1}=w_k-\alpha_kH_kg_k.
$$

Here $H_k$ approximates the **inverse Hessian**. The goal is a more useful direction than $-g_k$ at lower cost than an exact Newton step. If $H_k\succ0$ and $g_k\ne0$, then $-H_kg_k$ is descent. This lecture introduces the motivation; it does not yet derive a quasi-Newton update rule.

![[Lecture4_2026_extended.pdf#page=29]]

**Key takeaway:** elongated contours can make steepest descent zigzag. Rescaling coordinates can make the contours rounder and the optimisation easier, even though the underlying minimum is unchanged.

On [[Lecture4_2026_extended.pdf#page=30|p. 30]], set $w=Au$ with invertible $A$ and define $g(u)=f(Au)$. Then $w^*=Au^*$ and $g(u^*)=f(w^*)$.

**Short derivation of the connection:** the chain rule gives $\nabla_u g(u)=A^T\nabla_w f(w)$. A gradient step in $u$, converted back to $w$, becomes

$$
u_{k+1}=u_k-\alpha A^T\nabla f(w_k)
\quad\Longrightarrow\quad
w_{k+1}=w_k-\alpha AA^T\nabla f(w_k).
$$

So rescaling induces a matrix-scaled gradient step. Equivalent optimisation problems can have very different steepest-descent trajectories.

## Important results

- Uniformly sampled component/mini-batch gradients are unbiased estimates of the full empirical gradient.
- SGD makes each update cheaper; a noisy gradient changes how we assess convergence.
- Newton root finding uses $r/r'$; Newton optimisation uses $f'/f''$ or solves $Q_kp_k=-g_k$.
- Positive definite curvature ensures Newton's direction is descent; quadratic convergence needs local assumptions.
- Quasi-Newton methods seek useful curvature scaling at lower cost; rescaling explains why the geometry matters.
