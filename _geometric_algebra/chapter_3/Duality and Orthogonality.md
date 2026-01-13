---
title: "Duality and Orthogonality"
tags: [geometric-algebra, duality, orthogonality]
---

Orthogonality is usually a yes/no relation. In this chapter it becomes a *construction*: contraction produces the part of a subspace that's forced to be perpendicular to another. Duality is the cleanest version of that idea—orthogonality relative to the whole space.

## Blade inverse
A blade doesn't have a unique inverse under contraction (you can always add something perpendicular and keep $A \lrcorner A^{-1} = 1$). But there *is* a canonical one:
$$
A^{-1} = \frac{\tilde{A}}{A^2}
$$
(up to the grade-dependent sign coming from reversion conventions). It satisfies $A \lrcorner A^{-1} = 1$ when $A^2 \neq 0$. Null blades (zero norm) are the warning label: the inverse doesn't exist there.

## Dualization via contraction
Let $I_n$ be the unit pseudoscalar of the ambient space. The dual of a *k*-blade is
$$
A^* = A \lrcorner I_n^{-1}
$$
Geometrically: $A^*$ represents the orthogonal complement of the subspace of $A$, with a consistent orientation (Figures 3.4 and 3.5 are the 2-D and 3-D intuition pumps).

Dualizing twice flips a dimension-dependent sign:
$$
(A^*)^* = (-1)^{n(n-1)/2} A
$$
So if you need a true "undo," use undualization:
$$
A^{-*} = A \lrcorner I_n
$$

## Duality identities
With $I_n$ as the "everything blade," both subspaces are automatically contained in it, so duality identities become powerful simplifiers:
$$
(A \wedge B)^* = A \lrcorner (B^*)
$$
and, when containment is satisfied,
$$
(A \lrcorner B)^* = A \wedge (B^*)
$$

## Dual representation of a subspace
Direct representation: $A$ represents a subspace via $x \in A \iff x \wedge A = 0$.

Dual representation: let $D = A^*$. Then
$$
x \in A \iff x \lrcorner D = 0
$$
That $D$ is also a direct representation of the orthogonal complement of $A$. This is the general-blade version of the "normal vector defines a hyperplane by $x \cdot n = 0$" habit—now upgraded to arbitrary dimension.

With duality in place, "do geometry" becomes "apply a product, maybe dualize to swap wedge/contract, then undualize."

## Duality vs orthogonalization

Both are about orthogonality; both depend on the metric; both can be expressed using contraction. But they are not the same operation.

**Duality**
- Is a single *linear* map: $k$-blade $\mapsto$ $(n-k)$-blade.
- Changes *representation* (span to complement), not the underlying vectors.
- Output is uniquely determined by the input (once $I_n$ is fixed).

**Orthogonalization** (Gram–Schmidt style)
- Is an *algorithm* on a set of vectors.
- Is *nonlinear* (division by norms, order-dependent).
- Produces a new set of mutually orthogonal vectors—a construction, not just a re-representation.

The bridge: Gram–Schmidt's "remove the component along $u$" step is a contraction-with-wedge:
$$
u \lrcorner (u \wedge v) = v - (u \cdot v)u \quad\text{(assuming $u$ is unit)}
$$
So GA packages "orthogonalization step" into the same contraction primitive that powers duality—but orthogonalization chains many such steps with normalization, which is what makes it nonlinear.
