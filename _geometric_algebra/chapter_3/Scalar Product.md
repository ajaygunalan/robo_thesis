---
title: "Scalar Product (*)"
aliases: ["Scalar Product (*)"]
tags: [geometric-algebra, metric, blades]
---

You introduce the outer product to *name* a subspace: a line, a plane, a volume element. But geometry immediately asks for more than naming: *How big is it?* and *How tilted is it relative to another one?* The usual dot product answers that for vectors; the scalar product extends that same capability to blades of the same grade.

## Why a new product?
A bivector $a \wedge b$ already encodes a plane and its oriented area, but only up to the plane it lives in. Comparing areas across *different* planes needs a metric: some way to say what "length" means in the ambient space.

That ambient metric is still the ordinary vector inner product $a \cdot b$. The point of the scalar product is: if the vectors have a dot product, then blades inherit a size and an angle measure automatically.

## Definition
For two *k*-blades $A = a_1 \wedge \dots \wedge a_k$ and $B = b_1 \wedge \dots \wedge b_k$,
$$
A \ast B = \det\big[ a_i \cdot b_j \big]
$$
(up to the book's specific column order). Blades of unequal grade have scalar product 0.

This determinant is the "antisymmetry tax": it makes the result independent of how you happened to factor $A$ and $B$.

Symmetry you get for free:
- $A \ast B = B \ast A$
- $A \ast B = \tilde{A} \ast \tilde{B}$ (reversion $\tilde{\cdot}$ behaves nicely here)

## Size and angle
Once you accept $\ast$, two classic geometric numbers reappear for blades.

Squared norm (weight):
$$
A^2 = A \ast \tilde{A}
$$
- For vectors this is $a \cdot a$.
- For a bivector $A = a_1 \wedge a_2$: $A^2 = (\lVert a_1 \rVert \, \lVert a_2 \rVert \sin\psi)^2$, the parallelogram area squared.
- For a general *k*-blade you get squared *k*-volume (determinant geometry in disguise).

Angle between subspaces (same grade):
$$
\cos\theta = \frac{A \ast \tilde{B}}{\lVert A \rVert \, \lVert B \rVert}
$$
In 3-D, the diagram of "share a common direction, compare the leftover vectors" is exactly what Figure 3.1 is doing conceptually: factor common parts, and the cosine becomes a familiar vector cosine.

