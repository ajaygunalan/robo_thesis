# ray representation and spawning

A ray tracer lives or dies on its ray representation. In CGA you have many "natural" options, but this chapter is explicit: the algebraically pure choice is not automatically the runtime-friendly one. The final representation is chosen by asking a blunt question: what do we do to rays *all the time* (spawn, transform, intersect, compare distances), and which representation makes those cheap?

## Representation trade study: elegance vs extraction cost

The chapter considers several candidates:

* **Classical**: Euclidean point + direction vector. Minimal storage, but you lose CGA semantics in operations unless you rebuild blades as needed.
* **Point + line (CGA)**: gives you an intersection-ready line, but is storage-heavy and awkward because common intersections (line with plane) yield flat points, forcing conversions back to regular points if you insist on regular points everywhere.
* **Tangent vector**: one blade encodes both position and direction, which fits the "one object → one blade" philosophy, but it is large (many coordinates) and extracting the position is not a free coordinate transfer.
* **Rotor**: compact storage, but you can't "meet" a rotor with primitives (not a blade), and extracting position/direction requires applying the rotor to probe blades, which is expensive.

The chapter settles on a deliberately "less elegant" but fast hybrid:

* **position** as a **flat point** (good under translation + rotation),
* **direction** as a **free vector** (rotation sensitive, translation invariant).

Storage is close to the classical minimal case, and transforms behave the way you want with minimal fuss.

The price you pay is conceptual: a ray is no longer a single algebraic object, so the programmer must keep the pairing consistent. Also, distance-to-ray-start comparisons become more classical: with a regular conformal point you could use an inner product; with flat points you typically compute Euclidean differences and norms explicitly.

## Turning (flat point, free vector) into a carrier line

Even though the ray is stored as two blades, you still often want the carrier line for intersection computations. The only subtlety is that both a flat point and a free vector contain an $\infty$ factor, so you can't wedge them directly; you first remove the $\infty$ factor from the free vector (in code, by contracting with $o$) and then wedge with the flat point.

## Spawning camera rays

Primary rays come from the camera through pixels of an image plane. The chapter constructs a direction in camera coordinates by treating the pixel grid as a rectangle in the $e_1$–$e_2$ plane and pointing "forward" along $e_3$. In Euclidean terms, before normalization, the direction is

$$u(x,y) = \left(x \Delta_x - \tfrac12 W\right)e_1 + \left(y \Delta_y - \tfrac12 H\right)e_2 + e_3,$$

then represented as a free vector by wedging with $\infty$ and normalized to unit length.

For antialiasing, the chapter perturbs $u$ by a small random offset inside the pixel square (Mersenne Twister) before normalizing, traces multiple samples, and accumulates color. This is one of the few places the chapter openly embraces raw coordinates: pixel grids are *already* coordinates, so forcing them into an artificial coordinate-free disguise would be pointless friction.

## Spawning shadow rays

Shadow checks need a ray from a surface intersection point to a light source.

* The surface point naturally arrives as a flat point (many intersections yield flat points directly).
* Light positions are stored in transforms (rotors). To get the light's flat point position, the chapter applies the light's transform to the flat point at the origin $(o \wedge \infty)$.

With two normalized flat points—surface and light—you can subtract them to get the Euclidean displacement and normalize to get the direction. This yields a shadow ray in the same (flat point, free vector) representation without conversions.
