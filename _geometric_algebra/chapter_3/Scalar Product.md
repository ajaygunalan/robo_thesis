---
title: "scalar product (*)"
aliases: ["scalar product (*)"]
tags: [geometric-algebra, metric, blades]
---

The scalar product $A\ast B$ extends the vector inner product $a\cdot b$ to same-grade blades. It turns $k$-blades into measurable objects by assigning squared $k$-volume and supporting an “angle between subspaces” for equal grades.

For $k$-blades $A=a_1\wedge\cdots\wedge a_k$ and $B=b_1\wedge\cdots\wedge b_k$,
$$
A\ast B=\det\!\big[\,a_i\cdot b_{k+1-j}\,\big]_{i,j=1}^k,
$$
and $A\ast B=0$ when $\operatorname{grade}(A)\neq \operatorname{grade}(B)$.

The scalar product is symmetric and compatible with [[reversion]].
$$
A\ast B=B\ast A,\qquad A\ast B=\tilde A\ast \tilde B.
$$

The induced norm is
$$
\lVert A\rVert^2=A\ast \tilde A,
$$
and the angle between same-grade blades is defined by
$$
\cos\varphi=\frac{A\ast \tilde B}{\lVert A\rVert\,\lVert B\rVert}.
$$

Scalar-product calculations often factor out shared directions. Formalizing that cancellation leads to the [[contraction (⌋)|contraction]].
