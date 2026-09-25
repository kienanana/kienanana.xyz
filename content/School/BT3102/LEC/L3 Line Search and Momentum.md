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
updated: 2026-09-16
aliases:
  - BT3102 Lecture 3
---
Source: [[School/BT3102/LEC/PDFs/Lecture3_2026.pdf|Annotated lecture PDF]]. Page references use PDF page numbers.

## Overview
- Exact line search optimises distance along a chosen direction.
- Armijo and Wolfe conditions select useful steps without exact minimisation.
- Momentum combines gradient history; Nesterov evaluates the gradient at a look-ahead point.

## Exact line search

Define the one-dimensional function along the search direction:

$$
\phi_k(\alpha)=f(w_k+\alpha p_k),\qquad
\alpha_k\in\operatorname*{arg\,min}_{\alpha>0}\phi_k(\alpha),\qquad
w_{k+1}=w_k+\alpha_kp_k.
$$

For steepest descent, $p_k=-g_k$. Exact line search solves the problem along this ray, not the whole multivariable optimisation problem. It can be expensive or lack a closed-form solution. Source: [[Lecture3_2026.pdf#page=3|p. 3]].

**Global convergence means progress towards stationarity from general initial points under suitable assumptions; it does not mean finding a global minimum.** For steepest descent, standard sufficient conditions include a lower-bounded objective, a Lipschitz gradient on the relevant region, and well-defined exact line-search steps. Convergence of gradient norms to zero should not be confused with a guarantee that the iterates converge to one particular minimiser.

## Worked example: a quadratic objective

The lecture uses

$$
f(w_1,w_2)=w_1-w_2+2w_1w_2+2w_1^2+w_2^2,
$$
$$
g(w)=\begin{bmatrix}4w_1+2w_2+1\\2w_1+2w_2-1\end{bmatrix},\qquad
H=\begin{bmatrix}4&2\\2&2\end{bmatrix}.
$$

![[Lecture3_2026.pdf#page=8]]

**Key takeaway:** substituting $w_k-\alpha g_k$ gives a quadratic in $\alpha$. Keep the expanded coefficients in the PDF; a compact equivalent derivation is

$$
\phi_k(\alpha)=f(w_k)-\alpha g_k^Tg_k+\frac{\alpha^2}{2}g_k^THg_k,
\qquad
\alpha_k=\frac{g_k^Tg_k}{g_k^THg_k}\quad(g_k\ne0).
$$

Here $H\succ0$, so the denominator is positive. Solving $g(w)=0$ gives $w^*=(-1,3/2)^T$ and $f(w^*)=-5/4$. Stop when the gradient is small rather than evaluating the step formula at $g_k=0$.

The iteration table is on [[Lecture3_2026.pdf#page=10|p. 10]]; its useful result is convergence towards these values, not the individual rows.

### Why does the path zigzag?

![[Lecture3_2026.pdf#page=11]]

**Key takeaway:** at an interior exact line minimiser, $\phi_k'(\alpha_k)=g_{k+1}^Tp_k=0$. With $p_k=-g_k$, successive gradients are orthogonal. This explains the turns in the path; elongated contours can make progress slow despite an optimal step along each chosen direction. Starting on a principal axis is a special case in the diagram.

## Inexact line search and Armijo backtracking

Merely requiring $f(w_k+\alpha p_k)<f(w_k)$ can accept a step with negligible improvement. The examples on [[Lecture3_2026.pdf#page=13|pp. 13–14]] show why decreasing objective values alone need not get us to a stationary point.

**Armijo sufficient decrease** requires

$$
f(w_k+\alpha p_k)\le f(w_k)+c_1\alpha g_k^Tp_k,
\qquad 0<c_1<1.
$$

Since $g_k^Tp_k<0$, the right side lies below the current objective. Actual reduction must be at least the fraction $c_1$ of the linear model's predicted reduction.

Backtracking procedure:

1. Start with a positive trial step $\alpha_0$ and choose $0<\rho<1$.
2. While Armijo fails, replace $\alpha\leftarrow\rho\alpha$.
3. Accept the first tested step satisfying Armijo and update $w$.

Source: [[Lecture3_2026.pdf#page=18|annotated algorithm, p. 18]]. The useful handwritten qualification is that **Armijo alone does not reject unnecessarily small steps**. Backtracking from a sensible trial value controls how the accepted step is found.

## Wolfe conditions: sufficient decrease and curvature

Wolfe adds a curvature condition to Armijo:

$$
\underbrace{\phi_k(\alpha)\le\phi_k(0)+c_1\alpha\phi_k'(0)}_{\text{Armijo}},
\qquad
\underbrace{\phi_k'(\alpha)\ge c_2\phi_k'(0)}_{\text{curvature}},
\qquad 0<c_1<c_2<1.
$$

![[Lecture3_2026.pdf#page=20]]

**Key takeaway:** Armijo tests the function's **height** (enough decrease); curvature tests its **slope** (has the descent flattened enough?). If the initial slope is $-10$ and $c_2=0.9$, the new slope must be at least $-9$: $-9.99$ fails, while $-5$ passes the curvature test. Armijo must still hold.

The curvature test rules out very short steps that leave the slope almost unchanged. These are the ordinary Wolfe conditions, not the strong Wolfe variant. Suitable directions and regularity assumptions are still needed for convergence claims. The lecture highlights Wolfe's role in methods such as quasi-Newton; see [[Lecture3_2026.pdf#page=19|p. 19]].

## Momentum

With velocity $v_0=0$, fixed learning rate $\alpha$ and retention factor $0\le\tau<1$,

$$
v_{k+1}=-\alpha\nabla f(w_k)+\tau v_k,
\qquad w_{k+1}=w_k+v_{k+1}.
$$

Unrolling the recurrence gives

$$
v_{k+1}=-\alpha\sum_{i=0}^{k}\tau^{k-i}\nabla f(w_i).
$$

Recent gradients receive greater weight; older gradients fade exponentially. Persistent direction can build speed, while alternating gradient components can cancel. The full expansion is on [[Lecture3_2026.pdf#page=23|p. 23]], and the trajectory comparison is on [[Lecture3_2026.pdf#page=24|p. 24]]. Momentum does not guarantee improvement on every step or escape from every stationary point.

### Nesterov accelerated gradient: look ahead first

The lecture's look-ahead formulation is

$$
v_{k+1}=\tau v_k-\alpha\nabla f(w_k+\tau v_k),
\qquad w_{k+1}=w_k+v_{k+1}.
$$

Ordinary momentum measures the gradient at $w_k$; Nesterov measures it at the anticipated position $w_k+\tau v_k$. See [[Lecture3_2026.pdf#page=25|p. 25]] for the alternative implementation and its notation.

### Momentum versus random initialisation

[[Lecture3_2026.pdf#page=26|p. 26]] distinguishes using history within a run from changing its starting point. Multiple random starts explore different initial locations; momentum alters the trajectory using past updates. Neither supplies a general global-optimum guarantee.

## Important results

- Exact quadratic steepest-descent step: $\alpha_k=(g_k^Tg_k)/(g_k^THg_k)$ for $H\succ0$, $g_k\ne0$.
- Armijo asks for sufficient objective decrease; Wolfe also checks that the slope has flattened.
- Global convergence to stationarity is different from global optimality.
- Momentum retains past velocity; Nesterov uses a look-ahead gradient.
