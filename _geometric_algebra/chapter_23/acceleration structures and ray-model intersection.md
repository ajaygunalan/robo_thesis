# acceleration structures and ray-model intersection

Most ray tracers spend the bulk of their runtime asking one question: does this ray hit anything, and if so, what's the closest hit? This chapter's answer is a two-stage acceleration pipeline expressed in CGA terms: first a coarse bounding test to avoid detailed work, then a binary space partition (BSP) descent to restrict triangle testing to a small subset. The interesting CGA part is not that these are new ideas—they're not—but that each step stays "geometric" while still choosing representations that avoid repeated expensive decompositions.

## Precompute a bounding sphere

For each mesh, the chapter computes a bounding sphere that encloses all vertices. It does *not* try to find the tightest sphere; it builds a decent one cheaply.

The center is computed from axis-aligned extents:

1. Create three orthogonal dual planes through the origin (coordinate-aligned).
2. For every vertex point, compute its signed distance to each plane.
3. Track min/max signed distances per axis.
4. The center is placed at the midpoint of these extents, expressed as a conformal point.

Then compute the needed radius parameter by scanning vertices relative to this center. In conformal terms, the inner product of two normalized points encodes (minus half) squared Euclidean distance, so a min-scan of that quantity yields the parameter the chapter wants. The chapter notes explicitly that the stored value is effectively $-\tfrac12 R^2$, not $R$.

Finally, the sphere is stored in **dual sphere** form:

$$S^* = c + r \infty,$$

with $c$ the conformal center point and $r$ the (negative) radius-squared parameter.

## Build a BSP tree by splitting with translated coordinate planes

The BSP tree recursively partitions space so that each leaf contains a manageable set of geometry.

For the splitting planes, the chapter cycles (mod 3) through the three coordinate-aligned base planes (orthogonal directions), but translates each chosen base plane so that it approximately halves the current vertex set in that direction.

The translation distance is computed in a very "computer graphics" way:

1. compute each vertex's signed distance to the chosen dual base plane,
2. quicksort vertices by that signed distance,
3. take the midpoint distance $d$ between the two central vertices after sorting,
4. translate the dual plane by subtracting $d \infty$,
5. dualize and store it as the node's partition plane.

All of this is standard BSP construction; the only novelty is that it's expressed in conformal primitives (dual planes, translations in the $\infty$ direction) rather than matrices and dot products.

## Bounding sphere intersection test

During ray tracing, the first intersection filter is: does the ray's carrier line intersect the mesh's bounding sphere?

In the chapter's CGA code, intersecting the (dual of the) line with the stored dual sphere yields a **point pair** representing the entry/exit points. The chapter then checks whether this point pair represents a real intersection by evaluating its squared magnitude; a positive value indicates a real point pair rather than an "imaginary" one, which corresponds to "no hit."

## Clip the ray and represent line segments as endpoint flat points

To descend the BSP tree efficiently, the chapter represents a clipped ray segment as **two flat points**: start and end.

Bootstrapping this requires dissecting the point pair from the bounding sphere intersection into two flat points. The chapter uses the earlier book's point-pair dissection recipe (its equation (14.13)), implemented as a short sequence:

* compute a scalar magnitude from $pp \cdot pp$,
* construct auxiliary dual objects by contracting with $\infty$ and with the point pair itself,
* scale appropriately,
* produce two endpoint flat points via outer products with $\infty$.

The key idea is that the algebra gives you the endpoints directly, but you pay a real cost to do it—so you want to do it once (at the top), not repeatedly deeper in the BSP descent.

This choice also explains why the chapter does *not* represent segments as point pairs throughout the descent: splitting a segment at each BSP plane would force you to dissect point pairs repeatedly, which is too expensive. With endpoints stored explicitly, splitting is cheap.

## BSP descent: split segments by signed distance to the partition plane

At each BSP node, the algorithm checks which side(s) of the partition plane the current segment occupies.

For each endpoint flat point $p_i$, compute a signed distance scalar to the plane. If both distances have the same sign, the whole segment lies on one side, so you descend only into that child.

If the signs differ (product < 0), the segment crosses the plane. Then:

1. compute the intersection point of the ray's carrier line with the partition plane via a meet-like operation,
2. normalize it (the chapter uses a reverse-norm unitization),
3. split the segment at that point and recurse into both children with the two subsegments.

A degenerate case occurs when the segment lies in the partition plane; then the safe choice is to descend into both children.

The chapter also notes a useful pruning heuristic: because the end goal is the *closest* hit, you visit the BSP side containing the ray start first (by evaluating the ray start's sign relative to the partition plane), and you can stop early if you find a nearer intersection that makes farther branches irrelevant.
