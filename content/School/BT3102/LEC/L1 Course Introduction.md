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
updated: 2026-09-16
aliases:
  - BT3102 Lecture 1
---
Source: [[School/BT3102/LEC/PDFs/Lecture1_2026.pdf|Annotated lecture PDF]]. Page references use PDF page numbers.

## Overview
- Gradients describe local change; directional derivatives explain steepest ascent and descent.
- Convexity and Taylor approximations provide the language for optimisation.
- Matrices represent linear transformations relative to a chosen basis.

## Gradients and directional derivatives

For a differentiable scalar function $f:\mathbb R^n\to\mathbb R$,

$$
\nabla f(x)=\begin{bmatrix}\partial f/\partial x_1\\\vdots\\\partial f/\partial x_n\end{bmatrix},
\qquad D_u f(x)=\nabla f(x)^Tu.
$$

Each gradient component measures change along one coordinate axis. For a **unit** vector $u$, the directional derivative is the rate of change per unit distance in that direction. Without normalisation, the vector's length also scales the rate.

### Short derivation: why the dot product?

Define $g(h)=f(x+hu)$. The chain rule gives

$$
g'(0)=\sum_i\frac{\partial f(x)}{\partial x_i}u_i=\nabla f(x)^Tu.
$$

The annotated chain-rule calculation is on [[Lecture1_2026.pdf#page=9|p. 9]]. The useful idea is to turn movement through several coordinates into a function of one step parameter, $h$.

For $\nabla f(x)\ne0$ and $\|u\|_2=1$,

$$
-\|\nabla f(x)\|_2\le\nabla f(x)^Tu\le\|\nabla f(x)\|_2.
$$

Thus the unit steepest ascent/descent directions are $\pm\nabla f(x)/\|\nabla f(x)\|_2$. **The comparison assumes equal-length directions.**

### Geometry: gradient perpendicular to a level curve

![[Lecture1_2026.pdf#page=12]]

**Key takeaway:** along a level curve, $f$ stays constant, so its derivative along a tangent is zero. Consequently, a nonzero gradient is perpendicular to that tangent. The diagram and handwritten explanation preserve this geometry.

## Worked example: direction versus distance

From [[Lecture1_2026.pdf#page=10|p. 10]], let $f(x,y)=350-2x^2-1.5y^2$. Then

$$
\nabla f(1,1)=(-4,-3)^T,\qquad
D_{(-5,-2)}f(1,1)=(-4)(-5)+(-3)(-2)=26.
$$

This is the rate with respect to the step parameter. Per unit distance along the same direction it is $26/\sqrt{29}$. The greatest possible unit-direction increase is $5$, attained along $(-4,-3)^T/5$.

## Convexity

A set $S$ is **convex** if every segment between two of its points stays in $S$:

$$
tx+(1-t)y\in S\quad(x,y\in S,\;0\le t\le1).
$$

A function on a convex domain is **convex** if

$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y).
$$

Its graph lies below the chord joining two graph points. See [[Lecture1_2026.pdf#page=13|the diagrams on p. 13]]. This becomes useful in [[L2 Optimisation and Gradient Descent#Stationary points and minima|Lecture 2]]: convexity makes local minima global.

## Taylor approximations and the Hessian

For a small displacement $s$ from $w$, first-order and second-order approximations are

$$
f(w+s)\approx f(w)+\nabla f(w)^Ts,
$$
$$
f(w+s)\approx f(w)+\nabla f(w)^Ts+\frac12s^T\nabla^2f(w)s.
$$

The **Hessian** has entries $[\nabla^2f(w)]_{ij}=\partial^2f/\partial w_i\partial w_j$. The gradient supplies slope; the Hessian supplies curvature. $C^1$ means continuous first derivatives; $C^2$ means continuous second derivatives. These are local approximations, not exact descriptions of an arbitrary function far from $w$.

Source: [[Lecture1_2026.pdf#page=14|Taylor approximations, p. 14]] and [[Lecture1_2026.pdf#page=15|Hessian, p. 15]].

## Bases, transformations and similarity

A basis $B=(b_1,\ldots,b_n)$ lets us express each vector uniquely as $v=\sum_i x_i b_i$. Its coordinate column $[v]_B=(x_1,\ldots,x_n)^T$ depends on the basis and its ordering.

A transformation is linear when $T(ax+by)=aT(x)+bT(y)$. A matrix describes it once bases are chosen; matrix–vector multiplication applies it.

If $P$ contains the new basis vectors in old coordinates, then

$$
x_{\mathrm{old}}=Px_{\mathrm{new}},\qquad
A_{\mathrm{new}}=P^{-1}A_{\mathrm{old}}P.
$$

The similarity formula represents the **same transformation in different coordinates**: convert to old coordinates, apply the transformation, then convert back. $P$ must be invertible. See [[Lecture1_2026.pdf#page=22|p. 22]].

### Geometry: moving a point versus changing coordinates

![[Lecture1_2026.pdf#page=25]]

**Key takeaway:** $\operatorname{diag}(2,3)(1,1)^T=(2,3)^T$ can describe moving a point with fixed axes. The same numerical coordinate change can instead arise by keeping the point fixed and shrinking the coordinate units to $1/2$ and $1/3$. Keep the geometric object separate from its coordinates; [[Lecture1_2026.pdf#page=26|p. 26]] develops the basis interpretation.

## Important results

- Directional derivative: $D_u f=\nabla f^Tu$; use unit vectors when comparing slopes per unit distance.
- Negative gradient gives Euclidean steepest descent when the gradient is nonzero.
- Taylor's linear term predicts change; its quadratic term captures curvature.
- A matrix representation depends on the basis, while the underlying transformation need not change.
