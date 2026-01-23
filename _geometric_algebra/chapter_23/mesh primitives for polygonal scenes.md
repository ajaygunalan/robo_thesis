# mesh primitives for polygonal scenes

A polygon mesh is "just triangles," but a ray tracer forces you to interrogate those triangles constantly: positions for interpolation, surface attitude for shading, and edge/plane data for intersection logic. This chapter's mesh representation is a case study in using CGA where it buys clarity *without* choosing blade types that make the common queries expensive. (Figure 23.1 on page 4 shows the kind of triangular mesh being targeted: a solid rendering with a wireframe overlay.)

## Vertices: position, attitude, texture coordinates

A vertex needs a Euclidean position $x \in \mathbb{R}^3$. The chapter stores it as a **normalized conformal point**:

$$p(x) = o + x + \tfrac12 |x|^2 \infty.$$

This costs four stored coordinates (you don't store the implicit $o$). A tempting alternative is a flat point $(o+x)\wedge \infty$, which saves a coordinate, but the chapter rejects it because it's awkward in two places that happen constantly in mesh work:

* spanning operations (e.g., building the plane of a triangle cleanly), and
* barycentric interpolation (where normalized point behavior is convenient).

For shading, the mesh file supplies a classical normal vector $n$. The code converts this to a **surface attitude** stored as a free bivector (a 2-direction), by wedging with $\infty$ and dualizing:

$$A = \operatorname{dual}(n \wedge \infty).$$

This keeps the "tangent plane direction" as the primary object, with the normal being conceptually the dual view of the same geometric feature.

Texture coordinates are 2D and don't need heavy geometry. The chapter stores them as normalized flat points in a 2D texture carrier space, effectively homogeneous coordinates in that 2D world.

So a vertex is the bundle: conformal point (position), free bivector (attitude), and 2D texture point.

## A more elegant alternative they *don't* use: tangent 2-blades

CGA can fuse "position + direction" into a single primitive: a **tangent bivector**. You can combine a point $p$ and an attitude $A$ into something like

$$V = p \rfloor (p \wedge A \wedge \infty),$$

which has crisp semantics ("this 2-direction attached at this point"). The catch is that you can extract the attitude cheaply, but extracting the position is not a free coordinate grab; it needs an actual meet-style computation. The chapter cites an extraction approach of the form

$$p_{\text{flat}} = (\infty \rfloor V) \rfloor (V \wedge \infty),$$

which is conceptually clean (it's the meet of a perpendicular line with the plane containing the tangent element) but computationally heavier than what the tracer wants to pay for repeated interpolation. That's why the chapter keeps position and attitude as separate stored fields.

## Faces: precompute what you'll ask for later

A face is a triangle, stored by indices into the vertex list. The chapter precomputes two kinds of blades per face because they are repeatedly useful:

1. The **plane** containing the triangle, as

$$\Pi = p_0 \wedge p_1 \wedge p_2 \wedge \infty,$$

with a degeneracy check via its squared norm (zero implies no surface area).

2. The three **edge lines**, each as a conformal line through two vertices:

$$L_{01} = p_0 \wedge p_1 \wedge \infty,\quad L_{12} = p_1 \wedge p_2 \wedge \infty,\quad L_{20} = p_2 \wedge p_0 \wedge \infty.$$

These edges are useful both for geometric tests ("is an intersection inside the triangle?" style logic) and for extracting edge directions for shading or texture-space reasoning.
