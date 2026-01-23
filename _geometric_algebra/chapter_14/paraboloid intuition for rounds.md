The "why" behind rounds-as-blades is easiest to see in 2D, where you can visualize the conformal lift as a paraboloid in one extra dimension.

## Points live on a null paraboloid

A Euclidean point at location vector $x$ is represented by the conformal null vector
$$
x = o + x + \tfrac12 x^2\,\infty.
$$
In 2D, you can picture the Euclidean plane as the $e_1\wedge e_2$ base, and the extra $\infty$-direction as "vertical." Then the map $x \mapsto x + \tfrac12 x^2\infty$ traces a **paraboloid** of null vectors above the base plane.

The extra $o$-dimension functions like a homogeneous coordinate, letting you represent offset subspaces without forcing them through the origin.

## Dual of a point is the tangent plane at its lift

A direct plane $\Pi$ contains a point $y$ exactly when $y\wedge \Pi=0$. In dual form, with $\pi=\Pi^*$, incidence becomes $y\cdot \pi=0$.

Now use the null property: $x\cdot x = 0$. The lifted point $x$ lies on the plane dually represented by $x$ itself. In the paraboloid picture, that plane is exactly the **tangent plane** to the paraboloid at $x$. This is not a metaphor: it is the geometric meaning of the null construction.

## Dual circles/spheres are points off the paraboloid; their duals are cutting planes

Pick a Euclidean center $c$ and consider the vertical line $c\wedge \infty$ in the homogeneous picture. Intersect that line with the tangent plane at a lifted point $x$; the intersection point $\sigma$ lies off the paraboloid and represents a **dual circle** through $x$ centered at $c$.

The key duality flip is:

* a dual circle/sphere is represented as a *point* (in the lifted picture) off the paraboloid,
* its dual is an actual **plane** in the lifted space,
* that plane intersects the paraboloid in an ellipse whose projection down is the Euclidean circle.

This is the classic "polar plane of a quadric" construction from projective geometry, now wearing conformal metric clothing.

It also explains imaginary circles cleanly: the representative point moves above the paraboloid and the dual plane moves below, but everything remains real in the lifted space.

## Circle intersection becomes plane intersection

Two Euclidean circles become two planes in the lifted space. Their intersection is a line. Where that line hits the paraboloid are the two lifted intersection points—i.e., a Euclidean point pair.

So in the conformal model of a 2D Euclidean space:

* intersecting circles is literally intersecting offset planes one dimension up (the $\infty$-dimension),
* and with the homogeneous $o$-dimension, that becomes intersecting linear subspaces through the origin.

That's the reason outer products of conformal points (origin blades) can represent curved Euclidean objects: the "curvature" is outsourced to the embedding.
