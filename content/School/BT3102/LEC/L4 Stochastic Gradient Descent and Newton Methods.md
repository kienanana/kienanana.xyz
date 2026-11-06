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
updated: 2026-10-02
aliases:
  - BT3102 Lecture 4
---
Source: [[School/BT3102/LEC/PDFs/Lecture4_2026_extended.pdf|Lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

Notation: $g_k=\nabla f(w_k)$, $Q_k=\nabla^2f(w_k)$.

## Stochastic and mini-batch gradient descent

For an average loss over $m$ examples:
$$
f(w)=\frac1m\sum_i h_i(w),\qquad \nabla f(w)=\frac1m\sum_i\nabla h_i(w).
$$
Full GD evaluates all $m$ component gradients per update. SGD uses one example or a mini-batch $B_k$:
$$
\widehat g_k=\nabla h_{i_k}(w_k)
\quad\text{or}\quad
\widehat g_k=\frac1{|B_k|}\sum_{i\in B_k}\nabla h_i(w_k),
\qquad w_{k+1}=w_k-\alpha_k\widehat g_k.
$$
With fresh uniform sampling from the full fixed dataset, conditional on the current iterate/history:
$$
\mathbb E[\widehat g_k\mid\text{history}]=\nabla f(w_k).
$$
Thus the estimate is full gradient + zero-mean noise. This per-step statement does not generally apply unchanged to shuffling through the remaining examples without replacement.

**Tradeoff:** cheaper updates, often more iterations and a noisier trajectory. A sampled step need not decrease the full objective. Larger batches generally reduce sampling noise but cost more per update. Learning-rate schedules can avoid full-objective line search.

**Stopping:** one tiny mini-batch gradient is unreliable. Use a larger gradient estimate, sustained lack of progress and an iteration/computation cap. Tiny parameter updates may simply reflect a tiny learning rate.

## Logistic regression: label convention

L4 uses $y_i\in\{-1,+1\}$:
$$
h_i(w)=\log(1+e^{-y_iw^Tx_i}),\qquad
\nabla h_i(w)=-\frac{y_ix_i}{1+e^{y_iw^Tx_i}}.
$$
The margin $y_iw^Tx_i$ measures agreement between score and label. This equals [[L2 Optimisation and Gradient Descent#Logistic regression: from likelihood to loss|L2's logistic loss]] after recoding $y_{\pm}=2y_{01}-1$.

## Newton root finding

For scalar equation $r(w)=0$:
$$
w_{k+1}=w_k-\frac{r(w_k)}{r'(w_k)}.
$$
Each step finds the root of the tangent approximation. Requires a nonzero derivative. Root finding for $f=0$ is different from minimising $f$; optimisation applies root finding to $f'=0$.

## Newton optimisation

Minimise the local quadratic Taylor model:
$$
q_k(p)=f(w_k)+g_k^Tp+\frac12p^TQ_kp.
$$
Its stationarity equation gives
$$
Q_kp_k=-g_k,\qquad p_k=-Q_k^{-1}g_k,\qquad w_{k+1}=w_k+p_k.
$$
Pure Newton uses step size $\alpha_k=1$. In computation, solve the linear system rather than explicitly forming the inverse. For scalar $f$, the update is $w_{k+1}=w_k-f'(w_k)/f''(w_k)$.

If $Q_k\succ0$, the quadratic model has a unique minimiser and, for $g_k\ne0$,
$$
g_k^Tp_k=-g_k^TQ_k^{-1}g_k<0.
$$
Newton's direction is then descent; the full step still need not decrease the true objective far from the solution.

**Local quadratic convergence:** with a sufficiently close start, positive definite Hessian at the minimiser and suitable smoothness (e.g. locally Lipschitz Hessian),
$$
\|w_{k+1}-w^*\|\le C\|w_k-w^*\|^2.
$$
This is a local rate, not a global convergence guarantee.

**Limitations:** singular Hessian → undefined standard step; indefinite Hessian → possible ascent; poor starting point → bad steps/cycling. General dense Hessian storage is $O(n^2)$ and factorisation costs $O(n^3)$; structure can reduce costs.

A $C^2$ local minimum only requires a **semidefinite** Hessian. Positive definiteness is an extra assumption: $f(w)=w^4$ has $f''(0)=0$ at its minimum.

## Quasi-Newton methods and rescaling

Quasi-Newton uses an inverse-Hessian approximation $H_k$:
$$
p_k=-H_kg_k,\qquad w_{k+1}=w_k+\alpha_kp_k.
$$
If $H_k\succ0$ and $g_k\ne0$, the direction is descent. L5 develops BFGS and L-BFGS to learn curvature without computing the exact Hessian each iteration.

For invertible coordinate change $w=Au$, define $\widetilde f(u)=f(Au)$:
$$
\nabla_u\widetilde f(u)=A^T\nabla_w f(w).
$$
GD in $u$, mapped back to $w$, becomes
$$
w_{k+1}=w_k-\alpha AA^T\nabla f(w_k).
$$
Rescaling changes GD trajectories and can improve conditioning. The underlying objective and corresponding minimisers remain equivalent.

## Connections

- **[[L1 Course Introduction#Taylor approximations and the Hessian|L1]] → Newton:** second-order Taylor supplies the local model; bases explain rescaling.
- **[[L2 Optimisation and Gradient Descent#Stationary points and minima|L2]] → interpretation:** a small gradient alone does not establish a minimum.
- **[[L3 Line Search and Momentum|L3]] → step selection:** separate the Newton/quasi-Newton direction from its step size.
- **[[L5 Rescaling and Quasi-Newton Methods|L5]]:** BFGS approximates curvature; L-BFGS limits storage. SGD reduces data-evaluation cost, while these methods address curvature computation/storage.
- **TUT4:** apply full/mini/single-sample updates to the same logistic loss and compare total computation.

For examples: [[Lecture4_2026_extended.pdf#page=12|SGD, pp. 12–15]] · [[Lecture4_2026_extended.pdf#page=17|Newton, pp. 17–27]] · [[Lecture4_2026_extended.pdf#page=28|quasi-Newton/rescaling, pp. 28–30]].
