---
title: "Metric Products"
tags: [adjoint, contraction, orthogonal, duals, normals]
---

$\wedge$ is "span," so it doesn't care about the metric. $\lrcorner$ and duality do: they encode perpendicularity and complements, so linear maps won't preserve them unless they have extra structure.

## Scalars don't transform; norms can
Because scalars are fixed by the extension, if a product outputs a scalar:
$f(A \cdot B) = A \cdot B$.
But the norm of a transformed blade is $f(A) \cdot f(A)$, which generally changes—nothing forces $f$ to preserve angles or lengths.

## The adjoint $f^\dagger$
To control metric behavior, define $f^\dagger$ by
$\langle f(a), b \rangle = \langle a, f^\dagger(b) \rangle$ for all vectors $a, b$.
In Euclidean orthonormal coordinates, $f^\dagger$ is the transpose map. Extend it to blades as an outermorphism, so $f^\dagger(A) \cdot B = A \cdot f(B)$.

## Contraction transforms with the adjoint
The compact law is:
$$f(A \lrcorner B) = (f^\dagger)^{-1}(A) \lrcorner f(B)$$

## Orthogonal transformations are exactly the nice ones
If $\langle f(a), f(b) \rangle = \langle a, b \rangle$, then $f^\dagger = f^{-1}$ and contraction becomes structure-preserving:
$f(A \lrcorner B) = f(A) \lrcorner f(B)$.

## Duals (and "normal vectors") transform differently
With $X^* = X \lrcorner I_n^{-1}$, duals inherit both the adjoint and determinant:
$$f^\star(X^*) = (f(X))^* = \det(f) \, (f^\dagger)^{-1}(X^*)$$
That's why a 3D normal $a \times b$ (a dual of $a \wedge b$) does not generally transform as $f(a) \times f(b)$; using the bivector $a \wedge b$ avoids that trap.
