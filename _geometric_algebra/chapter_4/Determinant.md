---
title: "Determinant"
tags: [determinant, pseudoscalar, volume]
---

The determinant becomes almost embarrassingly geometric once you remember: the space of $n$-blades in an $n$-D space is 1-dimensional. Any pseudoscalar is a scalar multiple of any other.

So when a linear map $f$ (extended as an outermorphism) acts on a pseudoscalar $I_n$, the result must be:
$$f(I_n) = \det(f) I_n$$

That's not a computational trick—it's the *definition* of $\det(f)$ as signed hypervolume scaling: magnitude change × orientation flip.

## Fast consequences
- Rotation: preserves the rotation plane's pseudoscalar, and leaves perpendicular directions fixed, so $\det=+1$.
- Point reflection: $\det = (-1)^n$.
- Projection onto a line: $\det=0$ for $n>1$.

## Composition law (falls out instantly)
For $g \circ f$:
$$(g \circ f)(I_n) = g(f(I_n)) = g(\det(f) I_n) = \det(f) g(I_n) = \det(g)\det(f) I_n$$
so $\det(g \circ f)=\det(g)\det(f)$.

This definition is coordinate-free; matrices enter later as one possible basis-bound implementation.
