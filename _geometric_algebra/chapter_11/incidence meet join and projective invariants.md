# Incidence, Meet, Join, and Projective Invariants

The homogeneous model becomes most compelling when you stop thinking of points/lines/planes as separate cases and start thinking of them as *flats* that can be combined by a closed algebra of incidence. Join (span) comes from outer products, meet (intersection) is built from duality plus outer products, and the presence of improper elements guarantees "sensible" outputs even when Euclidean intuition says "they don't intersect."

## Meet as a Uniform Intersection Operator

The chapter emphasizes closure: you can wedge, dualize, and meet and you never fall out of the algebra. Programmatically, that means you don't branch for "parallel" or "skew" until you decide how to *interpret* the final blade. That's why the book treats explicit hand derivations as learning exercises, not as what you should implement.

## Two Lines in a Plane: Finite Intersection vs. Point at Infinity

In a plane through the origin with pseudoscalar $I$, write two lines as
$$
L = e_0\,\mathbf{u} + U,\qquad M=e_0\,\mathbf{v}+V,
$$
where $\mathbf{u},\mathbf{v}$ are direction vectors in the plane and $U,V$ are their (scalar) moments in that plane. The meet computation yields
$$
L\cap M = e_0(\mathbf{u}\wedge \mathbf{v})^\star + V\mathbf{u} - U\mathbf{v}.
$$
This single expression covers:

* **Generic intersection**: if $(\mathbf{u}\wedge\mathbf{v})^\star\neq 0$, the result is a weighted finite point, and its weight acts like an "intersection strength" (large for near-perpendicular, small for near-parallel).
* **Parallel lines**: if $(\mathbf{u}\wedge\mathbf{v})^\star=0$, the meet reduces to an improper point proportional to the common direction, weighted by relative offset (for unit lines, proportional to their distance).
* **Coincident lines**: the meet becomes zero, which is the algebra's way of saying "your chosen join is wrong; the true meet is the line itself."

Figure 11.5 (PDF p. 23) visualizes the finite intersection case and explains the ratio-like structure (Cramer's rule) hiding in the meet.

## Two Skew Lines in 3D: Meet as a Scalar Dissimilarity

For skew lines in space,
$$
L = p\wedge \mathbf{u},\qquad M=q\wedge \mathbf{v},
$$
their meet in the full space becomes a scalar:
$$
L\cap M = \big((p-q)\wedge \mathbf{u}\wedge \mathbf{v}\big)^\star.
$$
Geometrically this encodes two "how different are they?" aspects at once: directional mismatch (via $\sin$ of the angle between $\mathbf{u},\mathbf{v}$) and locational mismatch (via the weighted perpendicular separation). Figure 11.6 (PDF p. 25) depicts the meet as a difference of oriented volumes and shows how a rejection operation can expose the separation vector.

## Relative Orientation as a Signed Measure

When the meet of two flats is scalar, it becomes a signed "relative orientation / sidedness" measure relative to the orientation of their join space. The chapter walks through standard 3D Euclidean intuitions (Figure 11.7, PDF p. 26):

* two points on an oriented line (sign changes with order),
* a point vs. an oriented line in an oriented plane (left/right),
* a point vs. an oriented plane in oriented space (which side),
* two oriented skew lines in space (a less intuitive but well-defined signed relation).

The critical modeling punchline is that these sidedness tests come out of the same meet machinery that computes intersections; no new ad hoc predicates are required.

## Ratios That Survive Transformations: Affine Ratio and Cross Ratio

The chapter then turns incidence weights into *invariants*. For colinear points $p,q,r$ with arbitrary normalizations (so $p=p_0(e_0+\mathbf{p})$ etc.), the ratio
$$
\frac{p\wedge q}{q\wedge r}
= \frac{p_0}{r_0}\,\frac{\mathbf{p}-\mathbf{q}}{\mathbf{q}-\mathbf{r}}
$$
is scalar because the direction vectors are proportional on a line. If points are identically normalized, the normalization factors cancel and you get an oriented distance ratio—an *affine* invariant (unchanged by affine maps).

To get a quantity invariant under *all* projective transformations (i.e., all linear maps of $\mathbb R^{n+1}$), you must eliminate normalization entirely, which requires four points. The projective cross ratio is
$$
\frac{(p\wedge q)(r\wedge s)}{(q\wedge r)(s\wedge p)}
= \frac{(\mathbf{p}-\mathbf{q})(\mathbf{r}-\mathbf{s})}{(\mathbf{q}-\mathbf{r})(\mathbf{s}-\mathbf{p})}.
$$
Figure 11.8 (PDF p. 30) shows the numerator/denominator pairing along the line. The chapter also extends the idea from colinear points to pencils of lines via area elements (Figure 11.9, PDF p. 31), where the same cancellation logic makes the cross ratio projectively invariant.
