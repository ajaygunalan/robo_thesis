# tangents carriers surrounds and affine combinations

## Tangents without differentiating

A recurring need in geometry code is: "given an element and a point on it, what is the tangent object at that point?" The conformal model gives a purely algebraic answer.

If $p$ is a point on a flat or round $X$ (so $p \wedge X = 0$), then the tangent blade at $p$ is computed by contraction with a grade-involuted element:
$$\text{tangent to }X\text{ at }p:\quad p \rfloor \widehat{X}.$$
This works uniformly for flats and rounds and avoids any explicit differentiation (Figure 15.6, page 9). The chapter's proof strategy is "do it at the origin where the algebra is simplest, then invoke Euclidean covariance to move it anywhere."

A subtle point: for a round, the tangent blade naturally carries a factor proportional to the radius (not radius-squared). The chapter notes that imaginary rounds contain no real points, so real tangents are not expected there anyway.

## Carriers and tangent flats

Define the **carrier** of an element as the smallest flat that contains it. For a round $\Sigma$,
$$\text{carrier}(\Sigma) = \Sigma \wedge \infty.$$
That is: wedging with $\infty$ "forgets curvature" and produces the containing flat (e.g., circle $\to$ carrier plane).

Once you have the tangent blade $p \rfloor \widehat{X}$, its **tangent flat** is
$$(p \rfloor \widehat{X}) \wedge \infty.$$
This applies to rounds and flats; for a flat it returns the flat itself. Tangents themselves don't have tangent flats, but they do have carriers.

## Surrounding spheres and factorization of rounds

A round $\Sigma$ can be "surrounded" by the **smallest sphere containing it**. In dual form, the surrounding dual sphere is computed by a right division:
$$\text{surround}(\Sigma) = \Sigma / (\Sigma \wedge \infty).$$
Intuitively: $(\Sigma \wedge \infty)$ extracts the carrier information; dividing it out leaves the pure "sphere part" that encodes center and radius.

This motivates a clean factorization:
$$\Sigma = \big(\Sigma/(\Sigma \wedge \infty)\big) \cdot (\Sigma \wedge \infty).$$
Geometrically, this is a **perpendicular meet** of the carrier with the surrounding sphere (Figure 15.7, page 11): the carrier encodes direction/orientation/weight, while the surround encodes location (center) and size (radius-squared). Algebraically, having rounds split into orthogonal factors is a major simplifier in symbolic manipulation.

Special case (useful in practice): a point pair is also a round, so the same machinery returns the smallest sphere containing two points.

## Affine combinations: why "linear interpolation of points" isn't what you think

Take two normalized points $p$ and $q$. The affine-looking expression
$$\lambda p + (1-\lambda)q$$
does **not** produce a point family in CGA. It produces a 1-parameter family of **dual spheres** (in 2D: dual circles), whose centers move affinely but whose radii (and reality) vary with $\lambda$ (Figure 15.8, page 12). Their radius-squared becomes
$$-\lambda(1-\lambda) \cdot d_E^2(p,q),$$
so for $0<\lambda<1$ the spheres are imaginary even though the centers lie "between" $p$ and $q$.

If you actually want affine interpolation of *locations*, you should interpolate **flat points** instead of zero-radius dual spheres:
$$\lambda(p\wedge \infty) + (1-\lambda)(q\wedge \infty),$$
which yields the flat point at Euclidean location $\lambda p + (1-\lambda)q$.

The chapter notes you can extend affine combinations to flats and even circles/point pairs, but only when the objects form a true 1-parameter family (e.g., sharing a point pair). Even then, the parameter is usually geometrically awkward; rotor-based interpolation is typically the better tool (Figure 15.9, page 13).
