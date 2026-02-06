---
title: "duality and orthogonality"
tags: [geometric-algebra, duality, orthogonality]
---

Duality is orthogonal complementation expressed inside the algebra of blades, implemented by contracting with the [[pseudoscalar|inverse pseudoscalar]] and relying on the metric structure carried by the [[contraction (⌋)|contraction]]. When a formula uses $A^{-1}$, it assumes $A$ is [[null and nonnull blades|nonnull]]. See [[blade inverse]].

Let $I_n$ be the unit pseudoscalar of the ambient space. The dual of a $k$-blade is
$$
A^*=A\lrcorner I_n^{-1},
$$
an $(n-k)$-blade representing the orthogonal complement subspace (with orientation fixed by $I_n$). Dualizing twice gives a dimension-dependent sign:
$$
(A^*)^*=(-1)^{n(n-1)/2}A,
$$
and undualization is contraction with $I_n$:
$$
A^{-*}=A\lrcorner I_n.
$$

Duality swaps $\wedge$ and $\lrcorner$:
$$
(A\wedge B)^*=A\lrcorner(B^*),\qquad (A\lrcorner B)^*=A\wedge(B^*).
$$

A subspace blade $A$ can be used directly via $x\in A\iff x\wedge A=0$, or dually via $D=A^*$ as $x\in A\iff x\lrcorner D=0$.
