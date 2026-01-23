# voronoi edge from four points

## Goal and setup

Given four planar points $p,q,r,s$ (assumed normalized conformal points), the chapter analyzes the Voronoi edge across the shared edge $pr$ of triangles $pqr$ and $prs$. The point is not the specific geometry; it's the technique: derive carrier, endpoint(s), and signed length **directly from the four points** without introducing an army of trigonometric helper variables (Figure 15.12, page 20).

## Edge lines as dual perpendicular bisectors

A point $x$ is on the perpendicular bisector of segment $pq$ iff $x\cdot p = x\cdot q$, i.e.
$$x\cdot (q-p)=0.$$
So the **dual perpendicular bisector** is simply the dual element
$$q-p.$$
Its squared norm is proportional to the squared Euclidean distance:
$$(q-p)\cdot(q-p)\sim d_E^2(p,q)=-2 \, p\cdot q,$$
which tells you it carries the right quantitative "strength," but also highlights a sign/square-root nuisance if you insist on extracting lengths too early. The chapter's workaround is to keep oriented linear quantities (built via consistent planar duality) rather than taking square roots mid-derivation.

## Edge endpoint as a circumcenter (intersection of midlines)

Intersect the dual midlines for $pq$ and $qr$:
$$(q-p)\wedge(r-q) = p\wedge q + q\wedge r + r\wedge p.$$
This is a **dual flat point** (you can confirm it's "flat" by contracting with $\infty$). It is not normalized; the chapter gives a normalization trick that allows choosing a convenient reference point to keep expressions short.

After normalization, the flat point becomes the circumcenter (as a flat point) of triangle $pqr$:
$$M = \frac{p\wedge q + q\wedge r + r\wedge p}{p\wedge q\wedge r\wedge \infty}.$$
This is already a strong example of "coordinate-free but still explicit": a symmetric wedge expression, no angles, no coordinates.

## Signed edge length via the weight of the connecting line

Compute the corresponding circumcenter $N$ for triangle $prs$ analogously. The Voronoi edge segment length could be obtained by point-point distance, but that reintroduces square roots and sign conventions.

Instead, the chapter computes the **line connecting the two centers** and reads the segment length from its weight. The key practical trick is how to get a Euclidean point $m$ from a dual flat point $M^*$: use a contraction with a chosen reference point and note that any extra $\infty$ term will die when you wedge with $\infty$ to form a line.

After rearranging wedge products to expose meet structure, the connecting line (and therefore the signed edge length factor) collapses to:
$$m\wedge n \wedge \infty = \frac{(r-p)^* \cdot (p\wedge q\wedge r\wedge s)^*}{(p\wedge q\wedge r\wedge \infty)^* \cdot (p\wedge r\wedge s\wedge \infty)^*}.$$
Interpretation the chapter emphasizes:

* The segment length becomes **zero** when $p\wedge q\wedge r\wedge s=0$, i.e., when the four points are concyclic (here: when $q$ lies on the circle through $p,r,s$). Crossing that circle flips the sign, signaling a change in Voronoi adjacency.
* Each denominator term is a dual oriented plane of a triangle; numerically it corresponds to twice the signed area of that triangle.
* The factor $(r-p)^*$ contributes the expected dependence on the Euclidean distance $d_E(r,p)$.

## Why this beats the classical derivation

The chapter then converts the result into a traditional trigonometric formula (introducing lengths like $\kappa,\rho,\sigma$ and angles like $\phi,\psi$) and shows how quickly symmetry disappears and bookkeeping explodes (equations (15.9)–(15.10), pages 23–24). The conformal expression encodes the same geometry using only the original points and standard operations; the "circle test" that controls the sign appears automatically rather than being bolted on by insight after the fact.
