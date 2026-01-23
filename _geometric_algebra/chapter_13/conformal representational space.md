## The design constraint: make distance an inner product

The conformal model is engineered around a single interface requirement: the representational inner product should encode *Euclidean squared distance*. Instead of treating Euclidean distance as something you compute "after" transforming points, you define the metric so that distance is already sitting inside the algebra. Concretely, for Euclidean points $P,Q\in E^n$ represented by vectors $p,q$ in an $(n+2)$-dimensional space, the model is defined by the normalization-aware rule
$$
\frac{p}{-\infty\cdot p}\cdot \frac{q}{-\infty\cdot q}
\;\equiv\;
-\frac12\, d_E^2(P,Q).
$$
This is the chapter's definition of the conformal model; almost everything else is forced by it.

Squared distance being linear-friendly is not cosmetic: it's what makes this metric "compute" well (Pythagoras is naturally about squares), and it is what lets isometries become orthogonal transformations later.

## Why points must be null, and why that forces a Minkowski metric

If $d_E(P,P)=0$ for every point $P$, then the defining rule forces
$$
p\cdot p = 0
$$
for every *finite* point representative $p$. So point representatives can't live in a Euclidean-signature space where the only null vector is $0$. You need an indefinite metric so nonzero null vectors exist.

The chapter constructs the representational space as $\mathbb{R}^{n+1,1}$ (Minkowski signature): $n$ Euclidean dimensions plus a $1{+}1$ subspace that can generate null vectors. A convenient "physics" basis for that $\mathbb{R}^{1,1}$ part is $\{e,\bar e\}$ with $e^2=+1$, $\bar e^2=-1$, and $e\cdot \bar e=0$, because then $(e+\bar e)$ and $(\bar e-e)$ are automatically null.

Geometrically, the conformal model prefers a *null* basis for those extra dimensions:

* $o$: an arbitrary finite "origin" point (not geometrically special—just a chosen unit point)
* $\infty$: the point at infinity (a geometrically special element that closes Euclidean space)

They satisfy the inner products shown in Table 13.1 (PDF page 7): $o^2=\infty^2=0$, $o\cdot\infty=-1$, and both are orthogonal to the Euclidean basis vectors.

The change of basis between the orthonormal $(e,\bar e)$ and null $(o,\infty)$ bases is (PDF page 7):
$$
o=\tfrac12(e+\bar e),\qquad \infty=\bar e-e,
$$
and conversely
$$
e=o-\tfrac12\infty,\qquad \bar e=o+\tfrac12\infty.
$$
This is just a coordinate change in the $\mathbb{R}^{1,1}$ part, but it's the one that makes the geometry legible.

## The point embedding and weight

A conformal point representative has one extra degree of freedom beyond the Euclidean $n$ coordinates because it is a *null* vector up to scale. That scale is interpreted as a *weight* (as in homogeneous coordinates). In this model, weight is extracted by the inner product with $-\infty$:
$$
\text{weight}(p)= -\infty\cdot p.
$$
A unit (normalized) point satisfies $-\infty\cdot p = 1$.

With a chosen unit point $o$ as "origin," a Euclidean location vector $\mathbf{p}\in E^n$ embeds as the unit conformal point (PDF page 6):
$$
p \;=\; o + \mathbf{p} + \tfrac12 |\mathbf{p}|^2\,\infty.
$$
A weighted point is $\alpha$ times that expression.

The embedding is consistent with the distance metric: for two unit points $p,q$ at Euclidean locations $\mathbf{p},\mathbf{q}$,
$$
p\cdot q = -\tfrac12|\mathbf{p}-\mathbf{q}|^2,
$$
so the inner product reproduces squared Euclidean distance with the planned $-\tfrac12$ factor.

## What general vectors mean: dual planes and dual spheres

Once points are settled, you still have "extra" vectors in $\mathbb{R}^{n+1,1}$ that are not null. The chapter's key interpretive move is: treat an arbitrary vector $v$ as a *dual* object by probing it with points. A unit point $x$ lies on the object dual to $v$ exactly when
$$
x\cdot v = 0.
$$
Running this probe classifies the geometric meaning of various vector forms (Table 13.2, PDF page 9).

### Dual planes

A vector with no $o$-component has the form
$$
\pi = \mathbf{n} + \delta\,\infty.
$$
Probing with a unit point $x$ yields $x\cdot\pi = x\cdot\mathbf{n} - \delta$, so $x\cdot\pi=0$ is the familiar plane equation with normal $\mathbf{n}$ and offset $\delta$. This is why $\pi$ is read as a *dual plane*.

A defining hallmark is $\infty\cdot\pi=0$: the point at infinity lies on every plane, which is exactly the "plane is a sphere through infinity" intuition made algebraic.

### Dual spheres (real and imaginary)

A general vector can be written as a scaled unit point plus an $\infty$-shift:
$$
\sigma = \alpha\left(c + \beta\,\infty\right),
$$
with $c$ a unit point. Probing gives $x\cdot\sigma=0 \iff |x-c|^2 = -2\beta$. Setting $\beta=-\tfrac12\rho^2$ makes this the real sphere equation:
$$
\sigma = \alpha\left(c - \tfrac12\rho^2\,\infty\right)
\quad\Longleftrightarrow\quad
|x-c|^2=\rho^2.
$$
If $\beta=+\tfrac12\rho^2$, you get $|x-c|^2=-\rho^2$, an *imaginary sphere* (negative squared radius). The chapter treats these as necessary "closed algebra" objects: they arise naturally from intersections and duality even if you never draw them.

Points are now seen as the $\rho=0$ special case of spheres; planes are the "radius $\to\infty$ / passes through $\infty$" limiting case. That's the conceptual reason the conformal model is simultaneously about Euclidean geometry and "the algebra of spheres."
