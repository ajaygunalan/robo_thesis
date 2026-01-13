# Geometric Algebra for Computer Science — Chapter Learning Outcomes

**Total: 566 pages (Chapters 1-23)**

---

## Part I: Geometric Algebra (236 pages | 42% of book)
*Focus: The mathematical syntax and grammar of the algebra.*

| Ch  | Topic                            | Pages | Done | Learning Outcome                                                                                                                                                 |
| --- | -------------------------------- | ----- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Why Geometric Algebra?           | 19    | 3%   | Understand geometric algebra as a unified language for geometry that treats objects (lines, circles) and operators (rotations, reflections) with the same syntax |
| 2   | [[Spanning Oriented Subspaces]]  | 42    | 11%  | Use the outer product to represent and manipulate oriented subspaces as blades.                                                                                  |
| 3   | [[Metric Products of Subspaces]] | 34    | 17%  | Use scalar product and contraction to measure subspaces, compute projections, duals, and reciprocal frames.                                                      |
| 4   | [[Linear Transformations]]       | 25    | 21%  | Extend linear maps to subspaces via outermorphisms; compute adjoint, determinant, and inverse.                                                                   |
| 5   | [[Intersection and Union]]       | 16    | 24%  | Compute subspace intersections and unions using meet and join, handling degeneracies consistently.                                                               |
| 6   | [[The Fundamental Product]]      | 25    | 28%  | Use geometric product to unify inner/outer products, enabling division, projection, and reflection.                                                              |
| 7   | [[Orthogonal Transformations]]   | 46    | 37%  | Use versors and rotors to compute reflections, rotations, and orthogonal transformations                                                                         |
| 8   | [[Geometric Differentiation]]    | 29    | 42%  | Use rotors, commutators, and geometric derivatives to compute structure-preserving multivector changes.                                                          |

---

## Part II: Models of Geometry (251 pages | 44% of book)
*Focus: Applying the algebra to describe specific geometries (Euclidean, Projective).*

| Ch | Topic | Pages | Done | Learning Outcome |
|----|-------|-------|------|------------------|
| 9 | Modeling Geometries | 2 | 42% | Understand the strategy of using higher-dimensional vector spaces (models) to represent more complex geometric entities (like offset lines or spheres) |
| 10 | The Vector Space Model | 24 | 46% | Use the algebra of directions to handle rotational problems, angular relationships, and interpolation of rotations using rotors |
| 11 | The Homogeneous Model | 56 | 56% | Implement Projective Geometry by embedding 3D space in 4D. Represent points as vectors and offset lines/planes as blades to linearize affine transformations |
| 12 | Applications of Homogeneous | 28 | 61% | Apply the homogeneous model to computer vision (cameras). Understand Plücker coordinates for lines as a natural consequence of the algebra |
| 13 | The Conformal Model | 42 | 69% | (Core Topic) Master the 5D Conformal model (R⁴˒¹). Represent Euclidean transformations (translation, rotation) universally as versors (rotors) |
| 14 | New Primitives | 40 | 76% | Represent spheres, circles, point pairs, and tangents directly as blades. Learn to switch between direct (spanning) and dual (constraint) representations |
| 15 | Constructions | 28 | 81% | Solve complex geometric problems using Meet (intersection) and Plunge (orthogonal intersection). Compute distances and tangents without coordinates |
| 16 | Conformal Operators | 31 | 86% | Implement advanced conformal transformations like spherical inversion and scaling using versors. Understand how translation is just rotation around infinity |

---

## Part III: Implementation of Geometric Algebra (79 pages | 14% of book)
*Focus: Algorithms, data structures, and software engineering for GA.*

| Ch | Topic | Pages | Done | Learning Outcome |
|----|-------|-------|------|------------------|
| 17 | Operational Models | 3 | 87% | Review how different geometries (Euclidean, Projective, Conformal) are defined by their symmetries and metrics within the algebraic framework |
| 18 | Implementation Issues | 7 | 88% | Understand the trade-offs between different software implementation strategies (matrix-based vs. basis-blade-based) for geometric algebra |
| 19 | Basis Blades and Operations | 9 | 89% | Implement low-level operations using bitmaps to represent basis blades. Efficiently compute products using logical operations on these bitmaps |
| 20 | Linear Products | 7 | 91% | Implement linear products (outer, contraction, geometric) efficiently, exploiting linearity to distribute computations over basis blades |
| 21 | Nonlinear Products | 12 | 93% | Implement complex nonlinear operations like inversion, exponentiation, and the meet/join algorithms for general multivectors |
| 22 | Specializing Structure | 16 | 96% | Optimize geometric algebra code using generative programming. Learn to automatically generate efficient code for specific geometric tasks |
| 23 | Ray-Tracing Application | 25 | 100% | Apply the full conformal model to build a functional ray tracer. Handle rays, intersections, and shading using the algebraic primitives derived in previous chapters |
