## Encode the camera as "pinhole + image plane"

Take the pinhole at the origin point $e_0$. The image plane is placed at distance $f$ along a unit direction $e$. Bundle those into a single **support vector**
$$
\mathbf f = f e.
$$
The image plane $\Pi$ is then most conveniently represented dually by
$$
\Pi^* \equiv \pi = e_0^{-1} - \mathbf f^{-1}.
$$
Check: a world point has homogeneous form $e_0 + x$, and $(e_0+x)\cdot \pi = 0$ reduces to the Euclidean plane equation $x\cdot \mathbf f = \mathbf f\cdot \mathbf f$.

Figure 12.2 (printed p.337) is literally this setup: a ray from the pinhole hits the plane.

## Projection is "meet the ray with the image plane"

A world point at direction/position vector $x$ defines the ray line
$$
L = e_0 \wedge x.
$$
Projecting is intersecting that ray with the image plane, i.e. taking a meet. With the plane in dual form, the meet is an inner-product contraction:
$$
\Pi \cap L \;=\; \pi \,\lrcorner\, L \;=\; e_0(\mathbf f^{-1}\cdot x) + x.
$$
Interpreted as homogeneous point coordinates, this corresponds to the Euclidean point
$$
x' = \frac{x}{\mathbf f^{-1}\cdot x},
$$
which is exactly the expected "scale until you hit the plane."

## The honest punchline: nonlinear in Euclidean space, linear in homogeneous space

The map $x \mapsto x'$ fails linear scaling in $\mathbb{R}^3$, so it's nonlinear if you insist on Euclidean coordinates. But the homogeneous representative map
$$
x \;\mapsto\; e_0(\mathbf f^{-1}\cdot x) + x
$$
*is linear*. That's the practical reason homogeneous coordinates exist.

The chapter also writes the corresponding $4\times 4$ matrix on the basis $\{e_1,e_2,e_3,e_0\}$:
$$
\begin{bmatrix}
I & 0\\
(\mathbf f^{-1})^T & 0
\end{bmatrix}.
$$

## Outermorphism matters: spans project covariantly

This isn't just "linear"; it's an outermorphism. So if an object $X$ is built by wedging points/lines/planes, its projection is obtained by one uniform expression:
$$
X \;\mapsto\; (e_0^{-1}-\mathbf f^{-1}) \,\lrcorner\, (e_0 \wedge X).
$$
That single formula replaces a bunch of special-case "project a point / project a line / project a plane" rules, because the wedge structure is preserved.

## Lines project with a clean Plücker-space matrix

On the Plücker line basis (direction block; moment block), the chapter gives the line-projection matrix:
$$
\begin{bmatrix}
0 & [\mathbf f^{-1}_\times]\\
0 & I
\end{bmatrix}.
$$
You can read this as a structural fact: from a pinhole, what you effectively observe for an image line is encoded in the **moment** part (because an observed image line corresponds to a *plane of rays*).

## Homogeneous coordinates are literally an imaging trick

Section 12.2.2 makes a slightly mind-bending but mathematically clean point: you can treat the vector $\mathbf f$ as the "homogeneous dimension" *inside the image plane itself*. Two image points at locations $x$ and $y$ correspond to world points $\mathbf f + x$ and $\mathbf f + y$, and their outer product
$$
(\mathbf f + x)\wedge(\mathbf f + y) = (\mathbf f + x)\wedge (y-x)
$$
has exactly the same structural form as a homogeneous line construction. The chapter's "Plato's cave" comment is cute, but the real use is concrete: the same outer-product algebra keeps working as you move between world geometry and image geometry.
