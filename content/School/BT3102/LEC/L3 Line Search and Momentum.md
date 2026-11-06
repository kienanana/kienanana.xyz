---
class: lecture
tags:
  - y4s1
  - bt3102
  - math/optimisation/gradient-descent
  - math/optimisation/line-search
  - math/optimisation/momentum
source: "[[School/BT3102/LEC/PDFs/Lecture3_2026.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-09-11
updated: 2026-10-02
aliases:
  - BT3102 Lecture 3
---
Source: [[School/BT3102/LEC/PDFs/Lecture3_2026.pdf|Annotated lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

Notation: $g_k=\nabla f(w_k)$, search direction $p_k$, step size $\alpha_k>0$.

## Exact line search

Choose a direction first, then minimise along it:
$$
\phi_k(\alpha)=f(w_k+\alpha p_k),\qquad
\alpha_k\in\operatorname*{arg\,min}_{\alpha>0}\phi_k(\alpha),\qquad
w_{k+1}=w_k+\alpha_kp_k.
$$
For a quadratic objective with Hessian $Q\succ0$ and $p_k=-g_k$:
$$
\alpha_k=\frac{g_k^Tg_k}{g_k^TQg_k}\quad(g_k\ne0).
$$
At an interior line minimiser, $g_{k+1}^Tp_k=0$. For steepest descent, successive gradients are orthogonal; elongated contours can produce slow zigzagging.

**Global convergence** means convergence towards stationarity from general starting points under assumptions, not a guarantee of a global minimum. For exact-search steepest descent, relevant assumptions include a lower-bounded objective, a Lipschitz gradient and well-defined line-search steps. Gradient norms approaching zero does not itself guarantee convergence of the iterates to one point.

## Inexact line search and Armijo backtracking

For descent direction $g_k^Tp_k<0$, require **sufficient decrease**:
$$
f(w_k+\alpha p_k)\le f(w_k)+c_1\alpha g_k^Tp_k,\qquad 0<c_1<1.
$$
Actual decrease must be at least a fraction $c_1$ of the decrease predicted by first-order Taylor approximation.

Start with trial $\alpha_0>0$; while Armijo fails, shrink $\alpha\leftarrow\rho\alpha$, where $0<\rho<1$. Accept the first passing step.

Mere objective decrease may be negligible. Armijo alone allows unnecessarily small steps; backtracking from a sensible trial value helps control the chosen step.

## Wolfe conditions

Armijo **plus curvature**:
$$
\phi_k(\alpha)\le\phi_k(0)+c_1\alpha\phi_k'(0),\qquad
\phi_k'(\alpha)\ge c_2\phi_k'(0),\qquad 0<c_1<c_2<1.
$$
Here $\phi_k'(\alpha)=\nabla f(w_k+\alpha p_k)^Tp_k$.

- Armijo tests **height**: enough objective decrease.
- Curvature tests **slope**: descent has flattened enough, ruling out excessively short steps.

These are ordinary Wolfe conditions. Suitable search directions and regularity assumptions remain necessary for convergence claims.

**Connection to L5:** set $s_k=\alpha_kp_k$ and $y_k=g_{k+1}-g_k$. Wolfe gives
$$
s_k^Ty_k=\alpha_k(g_{k+1}^Tp_k-g_k^Tp_k)
\ge\alpha_k(c_2-1)g_k^Tp_k>0.
$$
This positive curvature condition supports BFGS preserving a positive definite inverse-Hessian approximation.

## Momentum

For $v_0=0$, fixed $\alpha>0$, $0\le\tau<1$:
$$
v_{k+1}=\tau v_k-\alpha\nabla f(w_k),\qquad w_{k+1}=w_k+v_{k+1}.
$$
Equivalently,
$$
v_{k+1}=-\alpha\sum_{i=0}^k\tau^{k-i}\nabla f(w_i).
$$
Older gradients fade exponentially. Consistent components build speed; alternating components can cancel. Momentum need not decrease the objective at every step or escape every stationary point.

## Nesterov accelerated gradient

Evaluate the gradient at the **look-ahead point**:
$$
v_{k+1}=\tau v_k-\alpha\nabla f(w_k+\tau v_k),\qquad w_{k+1}=w_k+v_{k+1}.
$$
The lecture/TUT2 alternative uses the look-ahead variable $z_k=w_k+\tau v_k$:
$$
v_{k+1}=\tau v_k-\alpha\nabla f(z_k),\qquad
z_{k+1}=z_k+(1+\tau)v_{k+1}-\tau v_k.
$$
These formulations track different position variables; keep their notation consistent.

**Random restarts** try independent runs from different starting points. **Momentum** changes a run's trajectory using its history. Neither guarantees a global optimum.

## Connections

- **[[L1 Course Introduction#Taylor approximations and the Hessian|L1]] → Armijo:** Taylor supplies the predicted decrease.
- **[[L2 Optimisation and Gradient Descent#Gradient descent|L2]] → this lecture:** separate choosing a direction from choosing its step size.
- **[[L4 Stochastic Gradient Descent and Newton Methods|L4]]:** SGD and Newton change how the direction is formed.
- **[[L5 Rescaling and Quasi-Newton Methods|L5]]:** combine Wolfe with curvature-aware BFGS directions.

For examples/algorithms: [[Lecture3_2026.pdf#page=8|exact search, pp. 8–11]] · [[Lecture3_2026.pdf#page=18|Armijo/Wolfe, pp. 18–20]] · [[Lecture3_2026.pdf#page=22|momentum/NAG, pp. 22–26]].
