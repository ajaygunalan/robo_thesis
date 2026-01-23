# Embedding and Points in the Homogeneous Model

The homogeneous model starts by separating "where" from "which way" without inventing separate point and vector types in the algebra. You do it by embedding the base space $\mathbb R^n$ into a representation space $\mathbb R^{n+1}$ with one extra basis direction $e_0$ that is orthogonal to every base vector. Any vector in the representation space splits cleanly as
$$x = \xi_0 e_0 + \mathbf{x},\qquad \mathbf{x}\in\mathbb R^n,$$
so computations can explicitly "see" what lives in the base subspace and what lives in the extra dimension.

The metric on $\mathbb R^{n+1}$ is only partially dictated by reality: on base-space vectors it must match the base metric, and it is convenient to enforce $e_0\cdot \mathbf{x}=0$ for all $\mathbf{x}\in\mathbb R^n$. The remaining freedom is $e_0\cdot e_0$: taking it as $0$ would make $e_0$ noninvertible (awkward for duality), so the chapter allows either $e_0^2=+1$ or $e_0^2=-1$ and keeps the inverse symbol $e_0^{-1}$ explicit to stay metric-agnostic. A central sanity rule emerges here: anything "geometrically real" should not depend on that choice.

## Finite Points as Weighted Vectors

Geometrically, interpret $e_0$ as the point at the origin of the base space. A base-space location $\mathbf{p}$ is represented by translating that origin-point by $\mathbf{p}$ inside the embedding space, i.e. a "unit point representative" is
$$p = e_0 + \mathbf{p}.$$
Scaling gives weighted points: $\alpha(e_0+\mathbf{p})$ is still "the same location" but with weight $\alpha$. Figure 11.1 (PDF p. 4–5) draws the mental picture: you can visualize the base space as a copy "sitting at the tip of $e_0$," and points are rays through that copy, with scaling changing only the weight.

From an arbitrary point representative $p\in\mathbb R^{n+1}$ you can recover two real quantities: weight and location. The chapter expresses this in a coordinate-free "selection operator" style:
$$
\text{weight } w = e_0^{-1}\cdot p,\qquad
\text{location vector } \mathbf{p} = \frac{p}{w}-e_0
= \frac{e_0^{-1}(e_0\wedge p)}{w}.
$$
In coordinates on the basis $\{e_0,e_1,\dots,e_n\}$ this is the classic homogeneous trick: $w=p_0$ and $\mathbf{p}=(p_1,\dots,p_n)/p_0$.

## Improper Points as Directions

If a representative has zero $e_0$-component, then $e_0^{-1}\cdot p=0$ and $p$ lies entirely in the base subspace. Such elements are naturally read as *directions* (the old vector space model) and, in the projective reading, as *points at infinity*. The chapter leans into the dual intuition: the same algebra supports both "it's a direction" and "it's an improper point," and that ambiguity is a feature because it lets incidence theorems become uniform ("two lines always meet").

## Addition Becomes Meaningful Because of Weights

Because points are vectors in the representation space, you can add them—but only if the sum has a coherent base-space meaning. The homogeneous model earns its keep by making that meaning physical: adding weighted points produces a center-of-mass construction. If $p = m_p(e_0+\mathbf{p})$ and $q=m_q(e_0+\mathbf{q})$, then
$$
p+q = (m_p+m_q)e_0 + (m_p\mathbf{p}+m_q\mathbf{q}),
$$
which is exactly "total mass" plus "mass-weighted position." Scaling a point just scales its weight, which later shows up as *significance* or *stability* factors in incidence results.

If you want to stay in unit points (weight $1$), you must constrain the coefficients. The homogeneous model packages this as the affine combination: for unit points $p_i$,
$$
p=\sum_{i=1}^k \alpha_i p_i,\qquad \sum_{i=1}^k \alpha_i=1,
$$
which guarantees the output remains a unit point. The centroid is the equal-weight case: $\frac1k\sum_i p_i$. This is later the algebraic reason affine geometry preserves "barycentric-style" constructions.
