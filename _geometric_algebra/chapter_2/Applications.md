---
title: "Applications"
tags: [cramers-rule, line-intersection, incidence, computation]
---

The wedge turns "solve/intersect/test" into computations with oriented subspaces.

## Decomposing vectors (Cramer's rule, without coordinates)
In $\mathbb{R}^2$, solve $x = \alpha a + \beta b$ by wedging with $a$ and $b$:
- $x \wedge a = \beta(b \wedge a)$
- $x \wedge b = \alpha(a \wedge b)$

So the coefficients are ratios of oriented areas:
$$\alpha = \frac{x \wedge b}{a \wedge b}, \quad \beta = \frac{x \wedge a}{b \wedge a}$$

and
$$x = \frac{x \wedge b}{a \wedge b} a + \frac{x \wedge a}{b \wedge a} b$$

Determinants appear only if you choose to expand wedges in a basis.

## Intersecting planar lines via reshapeability
For $L: p + t u$ and $M: q + s v$, at intersection $x$ you can replace unknown bivectors by anchored ones in the same attitude:
- $x \wedge u = p \wedge u$, $x \wedge v = q \wedge v$.

Then the same ratio logic yields:
$$x = \frac{q \wedge v}{u \wedge v} u + \frac{p \wedge u}{v \wedge u} v$$

## Incidence as equations
Quick reference: parallel test is $a \wedge b = 0$.

## Programmer-grade uses
- Triangle orientation in 2D: sign of $(b-a) \wedge (c-a)$ drives back-face culling.
- Vector-field singularities in 3D: normalize samples on a cube to the unit sphere, sum small spherical triangle contributions $v(p_1) \wedge v(p_2) \wedge v(p_3)$; near-unit total suggests a singularity inside, near-zero suggests none.

Everything above is the same move: compute with blades instead of re-deriving geometry from coordinates.
