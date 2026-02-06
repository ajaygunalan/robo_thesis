---
title: "contraction (⌋)"
tags: [geometric-algebra, inner-product, blades]
---

Left contraction $A\lrcorner B$ (written $A⌋B$ in the book) is the grade-lowering product adjoint to $\wedge$ under the [[scalar product]]. Conceptually, it is the bilinear operation that lets you remove shared factors inside a scalar product.

In a nondegenerate metric it is characterized by
$$
(X\wedge A)\ast B = X\ast(A\lrcorner B),
$$
whenever the grades match. It follows that
$$
\operatorname{grade}(A\lrcorner B)=\operatorname{grade}(B)-\operatorname{grade}(A)
$$
(and $A\lrcorner B=0$ if the right-hand side is negative), and that for equal grades $A\lrcorner B=A\ast B$.

A computational definition that works directly on blades is given by the axioms
$$
\alpha\lrcorner B=\alpha B,\qquad B\lrcorner\alpha=0\ \text{if }\operatorname{grade}(B)>0,\qquad a\lrcorner b=a\cdot b,
$$
the Leibniz rule
$$
a\lrcorner(B\wedge C)=(a\lrcorner B)\wedge C+(-1)^{\operatorname{grade}(B)}B\wedge(a\lrcorner C),
$$
and the recursion rule
$$
(A\wedge B)\lrcorner C=A\lrcorner(B\lrcorner C).
$$

For computation, a vector $x$ acting on a factored blade expands as
$$
x\lrcorner(a_1\wedge\cdots\wedge a_k)=\sum_{i=1}^k(-1)^{i-1}(x\cdot a_i)\,a_1\wedge\cdots\wedge\widehat{a_i}\wedge\cdots\wedge a_k,
$$
with the bivector case
$$
x\lrcorner(a_1\wedge a_2)=(x\cdot a_1)a_2-(x\cdot a_2)a_1.
$$

Geometrically, $A\lrcorner B$ is a (possibly zero) subblade of $B$ that is perpendicular to $A$. In particular, $x\lrcorner A=0$ iff $x\perp A$.
