---
class: lecture
tags:
  - y4s1
  - bt3102
source: "[[School/BT3102/LEC/PDFs/Lecture5_2026.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-10-02
updated: 2026-10-02
aliases:
  - BT3102 Lecture 5
---
Source: [[School/BT3102/LEC/PDFs/Lecture5_2026.pdf|Lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

Notation: $g_k=\nabla f(w_k)$, $Q_k=\nabla^2f(w_k)$; $B_k$ approximates the Hessian and $H_k$ its inverse.

## Conditioning and rescaling

For a positive definite quadratic Hessian $Q$, the condition number is $\kappa(Q)=\lambda_{\max}/\lambda_{\min}$. A large ratio gives elongated contours and can make steepest descent zigzag slowly.

For invertible $A$, set $w=Au$ and $\widetilde f(u)=f(Au)$:
$$
\nabla_u\widetilde f=A^T\nabla_w f,\qquad
\nabla_u^2\widetilde f=A^TQA.
$$
Choosing $A=Q^{-1/2}$ makes the transformed Hessian $I$. GD in the new coordinates maps back to
$$
w_{k+1}=w_k-\alpha Q^{-1}g_k.
$$
This is a scaled Newton step. For a general function, use $Q_k\succ0$ and recompute the local transformation each iteration. GD trajectories depend on coordinates; equivalent objectives need not be equally easy to optimise.

## Quasi-Newton and the secant equation

Use curvature learned from steps and gradient changes instead of computing an exact Hessian:
$$
p_k=-H_kg_k,\qquad w_{k+1}=w_k+\alpha_kp_k,
$$
$$
s_k=w_{k+1}-w_k,\qquad y_k=g_{k+1}-g_k.
$$
The gradient change suggests $y_k\approx Q_ks_k$. Enforce the **secant equation**:
$$
B_{k+1}s_k=y_k\quad\text{or}\quad H_{k+1}y_k=s_k.
$$
Symmetry and the secant equation do not uniquely determine the matrix. Quasi-Newton methods also choose an update close to the previous approximation; BFGS uses a weighted Frobenius-norm criterion.

## BFGS inverse-Hessian update

Start with $H_0=I$, choose $p_k=-H_kg_k$, select $\alpha_k$ using Wolfe, then update:
$$
\rho_k=\frac1{y_k^Ts_k},
$$
$$
H_{k+1}=(I-\rho_ks_ky_k^T)H_k(I-\rho_ky_ks_k^T)+\rho_ks_ks_k^T.
$$
If $H_k\succ0$ and $s_k^Ty_k>0$, the update preserves positive definiteness. Thus $g_k^Tp_k=-g_k^TH_kg_k<0$ for $g_k\ne0$.

**Wolfe supplies the positive curvature condition** for descent directions; Armijo alone does not. The denominator is the dot product $y_k^Ts_k$, not $\|y_k\|\|s_k\|$. A small final objective does not prove the update is correct.

## L-BFGS

Full BFGS stores a dense $n\times n$ matrix: $O(n^2)$ storage and update/direction cost. L-BFGS stores only the latest $m$ pairs $(s_i,y_i)$: $O(nm)$ storage and direction cost.

**Two-loop recursion** computes $H_kg_k$ implicitly. For retained indices $i=\ell,\ldots,k-1$, let $\rho_i=1/(y_i^Ts_i)$:

1. Set $q=g_k$. From newest to oldest: $a_i=\rho_i s_i^Tq$, then $q\leftarrow q-a_iy_i$.
2. Set $r=H_k^{(0)}q$, with a cheap positive definite base such as $I$.
3. From oldest to newest: $b_i=\rho_i y_i^Tr$, then $r\leftarrow r+s_i(a_i-b_i)$.
4. Use $p_k=-r$.

Limited history controls cost but discards older curvature information. Compare runtime, storage and achieved accuracy separately from iteration count.

## Connections

- **[[L1 Course Introduction#Bases, transformations and similarity|L1]] + [[L4 Stochastic Gradient Descent and Newton Methods#Quasi-Newton methods and rescaling|L4]]:** coordinate changes explain curvature scaling.
- **[[L3 Line Search and Momentum#Wolfe conditions|L3]]:** Wolfe links step selection to BFGS positive definiteness.
- **[[L2 Optimisation and Gradient Descent#Stationary points and minima|L2]]:** stopping at a small gradient establishes approximate stationarity, not global optimality.
- **TUT3 / HW1 P3–5:** BFGS implementation, curvature audit and limited-memory comparison.

For derivations/examples: [[Lecture5_2026.pdf#page=5|rescaling, pp. 5–11]] · [[Lecture5_2026.pdf#page=12|BFGS, pp. 12–18]] · [[Lecture5_2026.pdf#page=19|L-BFGS, pp. 19–21]].
