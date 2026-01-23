A "dual round" is the conformal model's way of representing a round object (sphere/circle/point pair, and their higher-dimensional analogs) in *dual form*, where the basic building block is a *vector* encoding a sphere. The key advantage is that center/radius data turns into a simple closed form, and intersections with flats become plain outer products.

## Dual sphere as a vector

In the conformal model, a real sphere of radius $\rho$ centered at the origin has the dual representation
$$
\sigma = o - \tfrac12 \rho^2 \,\infty.
$$
Translating the center to a Euclidean location vector $c$ gives the corresponding centered dual sphere
$$
\sigma = c - \tfrac12 \rho^2\,\infty.
$$
This is not a "parametric equation"; it is a single conformal vector whose inner products with conformal points encode the usual quadratic sphere condition.

A useful geometric reading is: the scalar condition "a point lies on the sphere" becomes a linear condition in the conformal algebra,
$$
x\cdot \sigma = 0.
$$

## Cutting dual spheres with dual planes

Let $\pi$ be a plane through the center of the sphere. In dual form, such a plane is represented by a Euclidean vector normal $n$ (at the origin), and the chapter emphasizes the perpendicularity/incidence relationship:
$$
\pi\cdot \sigma = 0
$$
for a plane through the center (checked at the origin and then extended everywhere by Euclidean covariance).

Now take the outer product of the duals. Because $(A\cap B)^* = B^* \wedge A^*$, the 2-blade
$$
\kappa = \sigma \wedge \pi
$$
is the **dual circle** obtained as the intersection of the sphere and that plane.

Probe logic (the "don't trust it, test it" move): if $x$ is a point on the circle, then $x$ must satisfy both sphere and plane conditions. Algebraically, the blade $\kappa$ enforces both simultaneously: from $x\!\rfloor(\sigma\wedge\pi)=0$ you can recover $x\cdot\sigma=0$ and $x\cdot\pi=0$ as independent constraints.

Cut again with another plane $\pi'$ perpendicular to both $\sigma$ and $\pi$ (in 3D), and you get a **dual point pair**:
$$
\sigma \wedge \pi \wedge \pi'.
$$
Geometrically, you're intersecting a sphere with two planes, leaving two points.

## General "dual round" pattern

Iterating this "sphere cut by flats" construction gives a uniform algebraic form. Centered at the origin, a real dual round looks like
$$
(o - \tfrac12 \rho^2 \infty)\,E_k,
$$
where $E_k$ is a purely Euclidean $k$-blade that (dually) encodes the carrier flat you are cutting with. (The chapter prefers the geometric product for these factored forms; you can replace it by an outer product if you want.)

Real vs imaginary: starting from an imaginary sphere flips the sign of $\rho^2$. In this framework that's normal—only squared distances appear, so "imaginary rounds" live perfectly well inside the same real algebra.
