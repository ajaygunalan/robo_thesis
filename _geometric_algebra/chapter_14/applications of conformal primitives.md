This chapter isn't just "more primitives"; it's a pipeline for turning geometry problems into linear algebra and convexity problems by using conformal structure.

## Voronoi diagrams and Delaunay triangulations via lifting

Given Euclidean points $P,Q$ with lifts $p,q$ on the paraboloid, the perpendicular bisector between them is the set of points equidistant to both. In conformal algebra that bisector is dually represented by
$$
p - q,
$$
because probing with a point $x$ yields $x\cdot(p-q)=0 \iff x\cdot p = x\cdot q \iff d_E(x,P)^2 = d_E(x,Q)^2$.

In the paraboloid picture, this bisector line arises as the intersection of the **tangent planes** at $p$ and $q$. Extend that to triples: the intersection point of the three tangent planes at $p,q,r$ is dually represented by $p\wedge q\wedge r$, and it represents the circumcircle of the triangle (its projection gives the circumcenter). Voronoi vertices are these circumcenters.

The selection rule for what actually appears in the Voronoi diagram is "upper envelope in the $\infty$-direction": keep the bisector pieces that are highest above the base. Computational geometry literature packages this as the "paraboloid lifting trick." The conformal model tells you it's not a trick—it's the native representation.

By duality, the network dual to the Voronoi diagram in the conformal model is the convex hull of the lifted points, which projects down as the **Delaunay triangulation**. Practically: lift points, compute convex hull, project back; Voronoi is then obtained by duality.

## Sphere fitting becomes an SVD problem (if you accept a slightly biased metric)

Dual spheres are vectors $\sigma = c - \tfrac12\rho^2\infty$. Their inner product encodes a squared "tangential distance" relationship:
$$
\sigma_1\cdot\sigma_2 = \tfrac12\left(\rho_1^2 + \rho_2^2 - d_E(c_1,c_2)^2\right).
$$
Specialize $\sigma_2$ to be a point $p$ (a zero-radius sphere). Then $\sigma\cdot p$ becomes a signed measure of whether $p$ lies outside/inside the sphere, and for points close to the sphere it is approximately linear in the Euclidean distance-to-surface $\delta$:
$$
p\cdot\sigma \approx -\rho\,\delta \quad \text{(first order)}.
$$

If you try to minimize true squared distances you get a nonlinear optimization. The chapter instead proposes minimizing the sum of squares of $(\rho\delta)$, which leads to a quadratic objective in $\sigma$:
$$
\Gamma' = \sum_i (p_i\cdot\sigma)^2.
$$
Differentiating gives a *linear* condition in $\sigma$, which you solve in least-squares form by converting the conformal inner product to ordinary matrix algebra using the conformal metric matrix $M$ and assembling a data matrix of point coordinates. The nontrivial solution is obtained as the singular vector corresponding to the smallest singular value (SVD). Then decode center and radius using the parameter extraction rules.

Blunt assessment: this fit prefers smaller spheres (because it penalizes $\rho\delta$), but it's fast, linear, and gives a good seed if you later want a true nonlinear least-squares refinement.

## Kinematics: versor chains move *any* primitive, not just points

Forward kinematics is fundamentally "compose rigid motions." In the conformal model, you build those motions as versors:

* translations are exponentials of $t\,\infty$ (a translator),
* rotations are exponentials of bivectors (a rotor),
* rigid body motion is their product.

The important practical consequence is uniformity: once you have the motion versor, you apply it by sandwiching
$$
X \mapsto R X R^{-1}
$$
and it works for points, lines, circles, spheres, tangents—whatever blade you use to describe a limb or a feature you want to render.

Inverse kinematics then becomes "solve geometry with geometry" instead of "solve scalars with trigonometry." The chapter's humanoid-arm example sketches a conformal workflow:

* choose a tilt plane by rotating a reference plane about the shoulder–wrist line $L=o\wedge p\wedge \infty$,
* compute elbow candidates as a point pair from the intersection of two spheres (limb lengths) with that plane,
* choose one elbow point consistently,
* compute joint rotors as rotors mapping one conformal line to another using the same rotor-construction formulas you'd use in the vector model, but with lines substituted for direction vectors,
* only convert to angles at the very end (via rotor logarithms) if controllers demand scalars.

The point is not that this solves all IK problems magically—it doesn't—but that the conformal model keeps the computation in "meet/join/rotor" space for as long as possible, pushing trig and casework to the boundary where (sometimes) you actually need them.
