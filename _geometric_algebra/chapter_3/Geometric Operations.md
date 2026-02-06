---
title: "geometric operations"
tags: [geometric-algebra, projection, coordinates]
---

Orthogonal projection becomes a blade-level operation once contraction and inverses are available. For a [[null and nonnull blades|nonnull]] blade $B$, the projection of a vector or blade $X$ onto $B$ is
$$
P_B[X]=(X\lrcorner B)\lrcorner B^{-1}=(X\lrcorner B^{-1})\lrcorner B,
$$
so the result lies in $B$ and $P_B$ is idempotent. It satisfies $P_B[P_B[X]]=P_B[X]$. Contraction is the $B$-dual of projection.
$$
X\lrcorner B=P_B[X]\lrcorner B.
$$

If $B$ is a [[null and nonnull blades|nonnull]] $b$-blade, it behaves as a [[pseudoscalar]] for its own subspace. For any $Y\subseteq B$, define the dual inside $B$ by
$$
Y^{*_B}:=Y\lrcorner B^{-1}\qquad(\text{grade }k\mapsto b-k\text{ inside }B).
$$
Then projection is contraction followed by $B$-duality.
$$
P_B[X]=(X\lrcorner B)\lrcorner B^{-1}=(X\lrcorner B)^{*_B}.
$$

Reciprocal frames make coordinate extraction work without orthonormality. Given a (skew) basis $\{b_i\}_{i=1}^n$ and pseudoscalar $I_n=b_1\wedge\cdots\wedge b_n$, define
$$
b^i:=(-1)^{i-1}(b_1\wedge\cdots\wedge\widehat{b_i}\wedge\cdots\wedge b_n)\lrcorner I_n^{-1}.
$$
Then $b_i\cdot b^j=\delta_i^j$, and for $x=\sum_i x^i b_i$ the coefficients are recovered by an inner product again:
$$
x^i=x\cdot b^i.
$$
Geometrically, $b^i$ is the orthogonal complement of $\operatorname{span}\{b_j:j\neq i\}$.
