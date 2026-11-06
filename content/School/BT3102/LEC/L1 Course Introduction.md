---
class: lecture
tags:
  - y4s1
  - bt3102
  - math/multivariable-calculus
  - math/linear-algebra
  - math/convexity
source: "[[School/BT3102/LEC/PDFs/Lecture1_2026.pdf]]"
related:
  - "[[BT3102]]"
date: 2026-08-13
updated: 2026-10-06
aliases:
  - BT3102 Lecture 1
---
Source: [[School/BT3102/LEC/PDFs/Lecture1_2026.pdf|Annotated lecture PDF]] · [[BT3102#Review roadmap — Lectures 1–7|Review roadmap]]

## Gradients and directional derivatives

For differentiable $f:\mathbb R^n\to\mathbb R$,
$$
\nabla f(x)=\begin{bmatrix}\partial f/\partial x_1\\\vdots\\\partial f/\partial x_n\end{bmatrix}.
$$
The lecture writes the **directional derivative** at $(x_0,y_0)$ in direction $\mathbf w$ as
$$
\nabla_{\mathbf w}f(x_0,y_0)=\nabla f(x_0,y_0)\cdot\mathbf w.
$$
This is a **scalar**, whereas the gradient $\nabla f$ is a **vector**. Equivalent notation, using a general point $x$ and direction $u$, is
$$
\nabla_u f(x)=D_u f(x)=\nabla f(x)\cdot u=\nabla f(x)^Tu.
$$
The dot denotes a dot product. With column vectors, the transpose turns the gradient into a row so matrix multiplication gives the same scalar; no transpose is needed when using $\cdot$.

For $\|u\|_2=1$, this is change **per unit distance**. If $\nabla f(x)\ne0$:
$$
u_{\mathrm{ascent}}=\frac{\nabla f(x)}{\|\nabla f(x)\|_2},\qquad
u_{\mathrm{descent}}=-\frac{\nabla f(x)}{\|\nabla f(x)\|_2}.
$$
The nonzero gradient is perpendicular to a level curve/surface. Steepest direction depends on the norm; these formulas use the Euclidean norm.

## Convexity

A **convex set** contains the segment between any two of its points:
$$
tx+(1-t)y\in S\quad(x,y\in S,\ t\in[0,1]).
$$
A **convex function** on a convex domain satisfies
$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y).
$$
Every local minimum of a convex function is global. Strict convexity gives at most one minimiser.

## Taylor approximations and the Hessian

$C^1$: continuous first derivatives. $C^2$: continuous second derivatives.
$$
[\nabla^2f(w)]_{ij}=\frac{\partial^2f}{\partial w_i\partial w_j}.
$$
For small displacement $s$:
$$
f(w+s)\approx f(w)+\nabla f(w)^Ts,
$$
$$
f(w+s)\approx f(w)+\nabla f(w)^Ts+\frac12s^T\nabla^2f(w)s.
$$
Gradient = slope; Hessian = curvature. For $C^2$ functions the Hessian is symmetric. These approximations are local; the second-order expression is exact for quadratic functions.

## Bases, transformations and similarity

A basis represents each vector uniquely as $v=\sum_i x_i b_i$. Coordinates depend on the chosen basis and its ordering. A linear transformation satisfies $T(ax+by)=aT(x)+bT(y)$.

If invertible $P$ contains new basis vectors in old coordinates:
$$
x_{\mathrm{old}}=Px_{\mathrm{new}},\qquad A_{\mathrm{new}}=P^{-1}A_{\mathrm{old}}P.
$$
Similar matrices describe the same transformation in different coordinates. Distinguish moving an object from changing its coordinate representation.

## Connections

- **[[L2 Optimisation and Gradient Descent#Gradient descent|L2: gradient descent]]:** directional derivatives justify choosing $p=-\nabla f$.
- **[[L3 Line Search and Momentum#Inexact line search and Armijo backtracking|L3: Armijo]]:** first-order Taylor change becomes the sufficient-decrease benchmark.
- **[[L4 Stochastic Gradient Descent and Newton Methods#Newton optimisation|L4: Newton]]:** minimise a second-order Taylor model to obtain the Newton step.
- **[[L5 Rescaling and Quasi-Newton Methods|L5]]: rescaling:** coordinate transformations explain why matrix-scaled gradients can improve conditioning.

For diagrams and derivations: [[Lecture1_2026.pdf#page=9|directional derivative, pp. 9–12]] · [[Lecture1_2026.pdf#page=13|convexity/Taylor, pp. 13–15]] · [[Lecture1_2026.pdf#page=22|coordinates, pp. 22–26]].
