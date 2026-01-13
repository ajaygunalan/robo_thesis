---
title: "Geometric Operations"
tags: [geometric-algebra, projection, coordinates]
---

## Orthogonal projection (vectors and blades)
A projection should keep what lies in $B$ and kill what's perpendicular to $B$. The contraction already manufactures the "in $B$, perpendicular to $x$" piece; dualizing within $B$ turns that into the actual projected component.

For a vector:
$$
P_B[x] = (x \lrcorner B) \lrcorner B^{-1}
$$
For a blade $X$ of any grade:
$$
P_B[X] = (X \lrcorner B) \lrcorner B^{-1}
$$
It's idempotent: applying it twice doesn't change anything.

A practical variant that makes "the result lies in $B$" visually obvious is
$$
P_B[X] = (X \lrcorner B^{-1}) \lrcorner B
$$
This matters most when inverses misbehave (e.g., null blades in degenerate metrics).

A useful perspective flip: contraction is the "dual-by-$B$" of a projection:
$$
X \lrcorner B = P_B[X] \lrcorner B
$$
So if projection feels intuitive and contraction feels alien, you can *bootstrap* your intuition that way.

The deeper point: contraction is bilinear in both arguments (like the outer product), while projection needs $B^{-1}$, making it nonlinear in $B$. That's why the chapter treats contraction as primitive and defines projection from it—not the other way around.

### Why $B^{-1}$ acts as "dual within $B$"

"Dual" always means "contract with the inverse pseudoscalar of the space you're dualizing in."

- **Global dual**: $A^* = A \lrcorner I_n^{-1}$ (complement in the full $n$-space).
- **Local dual within $B$**: A nonnull $b$-blade $B$ is itself the pseudoscalar of its own $b$-dimensional subspace. So the dual *inside* $B$ of any $Y \subseteq B$ is
$$
Y^{*_B} := Y \lrcorner B^{-1} \qquad (\text{maps grade } k \to b-k \text{ inside } B).
$$

That's exactly what the second contraction in projection does:
$$
P_B[X] = \underbrace{(X \lrcorner B)}_{\text{in } B,\;\perp X} \lrcorner B^{-1}
$$
The first contraction produces a $(b-x)$-blade lying in $B$ and perpendicular to $X$. The second contraction $B$-dualizes it back to grade $x$—the projected copy of $X$ that lies in $B$.

The $1/B^2$ inside $B^{-1} = \tilde{B}/B^2$ removes $B$'s scale, so "within $B$" depends only on the *attitude* of the subspace, not its volume.

## Reciprocal frames (coordinates without orthonormality)
With a skew basis $\{b_i\}$, dotting with $b_i$ doesn't isolate coordinates. The fix is to build a *reciprocal basis* $\{b^i\}$ that is mutually orthonormal with $\{b_i\}$.

Let $I_n = b_1 \wedge \dots \wedge b_n$. Define
$$
b^i = (-1)^{i-1}(b_1 \wedge \dots \wedge \widehat{b_i} \wedge \dots \wedge b_n) \lrcorner I_n^{-1}
$$
Then
$$
b_i \cdot b^j = \delta_i^j
$$
and any vector $x = \sum_i x^i b_i$ has coefficients
$$
x^i = x \cdot b^i
$$
So "take coordinates" becomes an inner product again—just with the right vectors.

The geometry hiding in the formula: $b^i$ is the (oriented) orthogonal complement of the span of all basis vectors except $b_i$. In a truly orthonormal basis this collapses to $b^i = \pm b_i$, so you recover the usual shortcut.

### Why this replaces "minors of determinants"

In standard linear algebra, the reciprocal basis is $(G^{-1})^T$ times the original basis, where $G$ is the Gram matrix. Writing out the inverse explicitly uses cofactors/minors—bookkeeping that hides the geometry.

The formula above makes the geometry visible: the $(n-1)$-blade $(b_1 \wedge \dots \wedge \widehat{b_i} \wedge \dots \wedge b_n)$ is the hyperplane spanned by all basis vectors *except* $b_i$. Dualizing it produces the 1-vector perpendicular to that hyperplane—hence perpendicular to every $b_j$ with $j \neq i$.

So "cofactor/minor" bookkeeping becomes a direct geometric construction: $b^i$ is the orthogonal complement of "the others."

These two operations—projection and reciprocal frames—are the workhorses that make later chapters feel coordinate-free without being coefficient-illiterate.
