---
title: "Outermorphisms"
tags: [outermorphism, blades, grade]
---

A blade is built by wedging vectors, so the most conservative extension of a linear map is:

> the transformed blade is the wedge of the transformed generators.

That extension is the outermorphism of $f$: a linear map on the whole exterior algebra that commutes with $\wedge$.

## The rules
For scalar $\alpha$ and blades/multivectors $A,B$:
- $f(\alpha)=\alpha$
- $f(A \wedge B)=f(A) \wedge f(B)$
- $f(A+B)=f(A)+f(B)$ (so it extends to multivectors)

Equivalently:
$$
f(a_1 \wedge \ldots \wedge a_k)=f(a_1) \wedge \ldots \wedge f(a_k)
$$

## What this buys you
- Blades stay blades. Oriented subspaces map to oriented subspaces.
- Grade is preserved. A $k$-blade remains grade $k$ (dimension is not "retyped").
- Shared factors survive. If $A=A' \wedge C$ and $B=C \wedge B'$, then $f(A)$ and $f(B)$ share $f(C)$.

The catch is also the lesson: the image of a set of vectors can drop dimension, yet a blade can only keep its grade—so it may collapse to $0$ instead of becoming a lower-grade blade.

Everything here is metric-free; the metric re-enters when you ask about $\perp$, duals, and norms.
