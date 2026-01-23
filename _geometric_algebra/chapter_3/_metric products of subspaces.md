---
title: "metric products of subspaces"
chapter: 3
tags:
  - geometric-algebra
  - blades
  - metric
---
# metric products of subspaces

Subspaces are easy to span and hard to compare. The outer product $A\wedge B$ builds the subspace you want, but it is metric-free and cannot say whether two lines have the same length scale, whether two planes have the same area scale, or what an angle between planes should mean. The metric enters through the vector inner product $a\cdot b$, and the chapter’s first step is to extend it to blades as the [[scalar product]], so same-grade blades acquire norms and angles.

For $k$-blades $A=a_1\wedge\cdots\wedge a_k$ and $B=b_1\wedge\cdots\wedge b_k$, the scalar product is
$$
A\ast B=\det\!\big[\,a_i\cdot b_{k+1-j}\,\big]_{i,j=1}^k,
$$
and it vanishes when the grades differ.

The norm and the angle are then defined by
$$
\lVert A\rVert^2 = A\ast \tilde A,
\qquad
\cos\varphi = \frac{A\ast \tilde B}{\lVert A\rVert\,\lVert B\rVert}.
$$

Once you can take scalar products of blades, you immediately want to simplify them by extracting shared factors. Requiring a bilinear operation that “removes $A$ from $B$ inside a scalar product” leads to the [[contraction (⌋)|contraction]]. It produces a grade-lowering blade that stays inside $B$ while being orthogonal to $A$, and it is the basic metric interaction between unequal grades.

The contraction is characterized by the adjointness relation
$$
(X\wedge A)\ast B = X\ast(A\lrcorner B),
$$
and computed in practice by expanding a vector contraction through a factored blade
$$
x\lrcorner(a_1\wedge\cdots\wedge a_k)
=\sum_{i=1}^k(-1)^{i-1}(x\cdot a_i)\,a_1\wedge\cdots\wedge\widehat{a_i}\wedge\cdots\wedge a_k.
$$

Contraction then becomes the engine behind “metric geometry in the algebra”. When blades are [[null and nonnull blades|nonnull]], they admit a canonical [[blade inverse]], and contracting with the [[pseudoscalar|inverse pseudoscalar]] packages orthogonal complementation as [[duality and orthogonality|duality]]. This replaces the ad hoc “normal vector” viewpoint with a uniform blade-level dual representation.

The same construction reappears inside a subspace. A [[null and nonnull blades|nonnull]] blade $B$ serves as a [[pseudoscalar]] for its span. Contracting with $B^{-1}$ implements duality within $B$, and this local duality makes [[geometric operations|orthogonal projection]] and [[geometric operations|reciprocal frames]] drop out as direct constructions rather than coordinate tricks.

Define the projection by
$$
P_B[X] = (X\lrcorner B)\lrcorner B^{-1},
$$
and use the equivalent form $P_B[X] = (X\lrcorner B^{-1})\lrcorner B$ when you want the result to visibly lie in $B$.

Finally, the 3-d cross product is not primitive. It equals the dual of a bivector (a plane). Keeping planes as bivectors and dualizing only when a normal is genuinely required avoids a 3-d-only operator and clarifies how normals should transform [[the 3-d cross product]].

In $\mathbb{R}^{3,0}$ this reads
$$
a\times b = (a\wedge b)^* = (a\wedge b)\lrcorner I_3^{-1}.
$$

Reciprocal frames close the loop back to coordinates. Given a basis $\{b_i\}_{i=1}^n$ and $I_n=b_1\wedge\cdots\wedge b_n$, define
$$
b^i = (-1)^{i-1}(b_1\wedge\cdots\wedge\widehat{b_i}\wedge\cdots\wedge b_n)\lrcorner I_n^{-1},
$$
so coordinates become inner products again, $x=\sum_i x^i b_i$ with $x^i=x\cdot b^i$.
