# Metric Pitfalls of the Homogeneous Model

The homogeneous model is powerful precisely because it turns many geometric tasks into algebra on blades—*without needing a meaningful metric on the embedding space*. A major tell is that the chapter deliberately refuses to commit to $e_0^2=+1$ versus $e_0^2=-1$ for most of its development: if your result is genuinely about the base Euclidean geometry, it should not care. That's why the chapter leans so hard on outer product, duality, meet/join, and outermorphisms, and is cautious with the inner/geometric products in $\mathbb R^{n+1}$.

## Why the Embedding Metric is Not Euclidean Geometry

Euclidean geometry is translation-covariant: shifting the origin should not change the structure of metric facts. In the homogeneous model, shifting the "origin point" from $e_0$ to $e_0' = e_0 + t$ changes the square:
$$
(e_0')^2 = e_0^2 + t^2,
$$
so metric quantities in the embedding space depend on where you put the origin. That alone is enough to poison any attempt to interpret the embedding-space dot product as an intrinsic Euclidean measurement tool.

This shows up immediately in inverses. For a point representative $x=e_0+\mathbf{x}$,
$$
x^{-1} = (e_0+\mathbf{x})^{-1} = \frac{e_0+\mathbf{x}}{e_0^2+\mathbf{x}^2}
\neq e_0 + \mathbf{x}^{-1}.
$$
So "inverse of the representation" is not "representation of the inverse," which breaks the usual geometric-product intuition that drives versor-based Euclidean constructions.

## The Dot Product and Reflections Compute the "Wrong" Geometry

Even the inner product of two point representatives contains an origin-dependent constant:
$$
x\cdot y = e_0^2 + \mathbf{x}\cdot \mathbf{y}.
$$
Only the base-space term is Euclidean; the $e_0^2$ term is representational baggage. This is the classic warning from homogeneous coordinates, now expressed in GA form.

Reflections via sandwiching by point representatives become bizarre for the same reason. Reflecting about $e_0$ behaves like a point reflection, but reflecting about another point produces a nonlinear expression that depends explicitly on $e_0^2$ and the point's distance from the origin; the chapter notes that what you get is related to stereographic projection—not Euclidean reflection. The computation is "valid GA in $\mathbb R^{n+1}$," but it is not the Euclidean geometry you thought you were modeling.

## When "Metric-Looking" Operations Are Secretly Nonmetric

Some uses of inner products in the chapter are actually disguising nonmetric incidence relations because they pair a direct element with a dual element. For instance, probing a dual hyperplane with a point can be rewritten in terms of a meet: the meaningful content is "incidence," not an embedding-space dot product. This is why the hyperplane equation works cleanly even though point–point dot products don't.

## Projection: Salvaging Structure by Rewriting It as a Meet

In Euclidean GA, projection of $X$ onto $A$ is the metric construction
$$
P_A[X] = (X \cdot A)A^{-1}.
$$
In the homogeneous model, this produces a notion of "orthogonal" tied to the embedding metric (hence origin-dependent). The chapter's insight is that projection can be rewritten as an incidence operation involving dual inverses:
$$
P_A[X] = A \cap \big(X \wedge A^{-*}\big).
$$
So what looked metric can be reframed as "intersect $A$ with a flat built from $X$ and the dual inverse of $A$." Figure 11.12 (PDF p. 45) illustrates the geometry for projecting a point onto a line: the line joining the original point to its projected point intersects the dual line $L^{-*}$, producing a configuration that is coherent projectively but is emphatically not Euclidean "drop a perpendicular."

## The Practical Takeaway

Use the homogeneous model when you want:

* a closed algebra for *offset* flats (including "at infinity" elements),
* uniform meet/join incidence computations,
* clean affine/projective transformations applied to all grades.

Do **not** treat the embedding-space metric products as if they were Euclidean distance/angle machinery; that's structurally incompatible with translation covariance. The chapter explicitly frames this as the motivation for the conformal model that follows, which restores a metric interpretation while keeping the algebraic closure benefits.
