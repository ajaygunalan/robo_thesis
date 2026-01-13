---
title: "Examples"
tags: [examples, scaling, rotation, projection, reflection]
---

Outermorphism thinking is: apply $f$ to vectors, then wedge.

## Uniform scaling
If $S(x) = \alpha x$, then for $A = a_1 \wedge \ldots \wedge a_k$:
$$S(A) = \alpha^k A$$
So areas scale by $\alpha^2$, volumes by $\alpha^3$, and orientation flips when $k$ is odd and $\alpha < 0$.

## Parallel projection onto a line (the important surprise)
In a plane spanned by $a, b$, take $P(a) = a$, $P(b) = 0$. The plane's vector set maps onto the $a$-line, but the 2-blade maps to
$P(a \wedge b) = P(a) \wedge P(b) = a \wedge 0 = 0$.
Projection kills area elements, not just directions. This is why $\det = 0$ for projections.

## Rotation and an eigenblade
Rotate in the $u \wedge v$ plane. Vectors rotate, yet the plane blade is fixed:
$$R(u \wedge v) = R(u) \wedge R(v) = u \wedge v$$
A rotation may have no real eigenvectors in its plane, but it has a real eigen-2-blade: the plane itself.

## Point reflection
$f(x) = -x$ $\Rightarrow$ $f(A) = (-1)^{\text{grade}(A)} A$. In 3D that flips 3-blade handedness; the determinant is $(-1)^n$.

## Orthogonal projection (why outermorphisms are practical)
The vector projection $P_B(x) = ((x \lrcorner B) \lrcorner B^{-1})$ extends cleanly: you can project a blade directly without decomposing it into vectors.
