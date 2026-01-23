Direct rounds are the same geometric objects as dual rounds, but represented in *direct* form: as blades made from finite points (or from a standard "round factor" times a Euclidean carrier blade). This is the representation that makes "incidence data" (points on the object) turn into an outer product.

## Rounds spanned by points

In 3D, four points determine a sphere. The direct conformal guess is exactly right:
$$
\Sigma = p \wedge q \wedge r \wedge s.
$$
Similarly, in a plane:

* a circle is $p\wedge q\wedge r$,
* a point pair is $p\wedge q$.

The chapter's core insight for *why* this works is the dualized form: when you dualize $\Sigma$, you can rewrite it as a point contracted with a meet of midplanes. The algebraic hinge is the geometric meaning of
$$
q-p,
$$
which turns out to be the **dual perpendicular bisector hyperplane** of the two points: probing with $x$ yields $x\cdot(q-p)=0 \iff d_E(x,p)^2=d_E(x,q)^2$.

Intersect three such bisector planes (in 3D) and you get the center point: that's the same classical construction, but done by pure meet/dual operations.

## Dual sphere "through a point" form

If you already know the center $c$ but want a dual sphere described "through a known point" $p$, the chapter packages the parameters into
$$
p\!\rfloor\!(c\wedge \infty),
$$
because $p\cdot c = -\tfrac12\rho^2$ and $p\cdot\infty=-1$ let you fold radius information into the same vector.

This is the bridge that makes the dual of $p\wedge q\wedge r\wedge s$ recognizable as a (weighted) dual sphere.

## A coordinate-free radius from four points

One clean quantitative payoff of the direct form is that the sphere radius can be extracted directly from the blade norms after normalization. The chapter gives a compact expression for the squared radius:
$$
\rho^2 = \frac{(p\wedge q\wedge r\wedge s)^2}{(p\wedge q\wedge r\wedge s\wedge \infty)^2}.
$$
This is exactly the kind of "no coordinates, no determinants" formula the conformal model is built to produce.

## Oriented rounds: standard direct form

Beyond existence, you care about **orientation**: circles have a direction of traversal; spheres have an oriented shell. The chapter chooses the orientation of a direct round by tying it to the orientation of its carrier flat $\Sigma\wedge\infty$.

A direct real round at the origin is represented as
$$
\Sigma = (o + \tfrac12 \rho^2 \infty)\,A_k,
$$
with $A_k$ a purely Euclidean $k$-blade encoding the carrier orientation. Dualizing this produces a dual round of the expected "$o - \tfrac12\rho^2\infty$ times Euclidean blade" type, with a dimension-dependent sign factor that tells you how to match orientations consistently.

Translation to an arbitrary center $c$ is done by applying the translation rotor (so the object moves covariantly). The chapter also gives explicit expanded formulas, but the conceptual takeaway is: **construct at the origin, then translate/rotate by versors**, and the correct conformal object comes along automatically.
