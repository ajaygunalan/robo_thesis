# Clifford axioms and polarization identity

The chapter's "start over" move is philosophical but also engineering: don't define the geometric product in terms of other products; define it as the primitive operation tied to the metric, then re-derive the rest. The axioms are minimal: scalars commute with everything; a vector square $x^2 = xx$ is defined to be the scalar metric quantity $Q[x,x] = x \cdot x$; the product is bilinear (via distributivity/linearity); and it is associative. Crucially, it is **not** assumed commutative or anticommutative globally.

From these axioms you can recover the inner product as the symmetric part using polarization. Start from the standard bilinear identity

$$
x \cdot y = \tfrac{1}{2}\big((x+y) \cdot (x+y) - x \cdot x - y \cdot y\big),
$$

then replace dot-squares by geometric squares (since vector squares are defined as scalars). The cross terms isolate:

$$
x \cdot y = \tfrac{1}{2}(xy + yx).
$$

That single line matters: it shows the metric is already encoded in the symmetric part of the geometric product; the inner product doesn't need to be a separate primitive.

A neat application is the anticommutation of orthonormal basis vectors without "knowing" wedge products beforehand. If $i \neq j$, orthonormality gives $e_i \cdot e_j = 0$, hence $e_i e_j + e_j e_i = 0$, hence $e_i e_j = -e_j e_i$. With $e_i^2$ fixed by the metric, this is enough (with bilinearity and associativity) to expand arbitrary products in the algebra.

This is the chapter's quiet claim: once you tie "squares of vectors" to the metric and demand associativity, you get an algebra that reconstructs the same graded linear space you built earlier with wedge products—yet with a richer multiplication that can express operators and inverses cleanly.
