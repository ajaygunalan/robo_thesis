## Affine maps are outermorphisms, so blades transform consistently

An affine transformation is
$$
A[x] = f[x] + t,
$$
with the "affine constraint" $A[e_0]=e_0$ enforced by the homogeneous embedding. The chapter's key structural fact is that the induced action on blades is an **outermorphism**:
$$
A[X] = f[X] + t \wedge \big(e_0^{-1}\,\lrcorner\, f[X]\big),
$$
with the convenient convention that $f[e_0]=e_0$ so $f$ extends grade-wise.

Once you accept this, the different-looking transformation rules for points, lines, and planes are not different theories—they're the same outermorphism, restricted to different grades and written in different coordinate bases.

## Point, line, plane matrices (Table 12.2, printed p.335)

Write $f$ as a $3\times 3$ matrix acting on Euclidean vectors, and $t$ as a translation vector. Let $[t_\times]$ be the cross-product matrix such that $[t_\times]x = t \times x$.

### Points (standard homogeneous coordinates)

$$
\begin{bmatrix}
f & t\\
0^T & 1
\end{bmatrix}.
$$

### Lines (Plücker coordinates as a 6-vector)

With the Plücker split into direction-like and moment-like blocks, the induced $6\times 6$ matrix for a general affine $f$ is block-structured:
$$
\begin{bmatrix}
f & 0\\
-[t_\times]\,f & \det(f)\,f^{-T}
\end{bmatrix}.
$$
Intuition, without handwaving: directions transform by $f$, moments transform like pseudovectors ($\det(f)f^{-T}$), and translation couples direction into moment via the cross-product term.

### Planes

Planes transform by the inverse-transpose rule on normals, plus the induced offset update. In the chapter's plane-coordinate basis this becomes:
$$
\begin{bmatrix}
\det(f)\,f^{-T} & 0\\
-\,t^T\det(f)\,f^{-T} & \det(f)
\end{bmatrix}.
$$

### Sanity checks: translation and rotation

For pure translation ($f=I$), the line matrix collapses to
$$
\begin{bmatrix}
I & 0\\
-[t_\times] & I
\end{bmatrix},
$$
and the plane matrix to
$$
\begin{bmatrix}
I & 0\\
-\,t^T & 1
\end{bmatrix}.
$$
For pure rotation ($f=R$, $\det(R)=1$, $R^{-T}=R$), lines rotate by $\mathrm{diag}(R,R)$ and planes rotate like points (normals rotate, offsets unchanged).

## Dual lines: a swap matrix, not a new theory

Dualizing a line swaps the two 3-vector blocks (up to a metric-dependent sign). In matrix terms, dualization is implemented by
$$
D = \begin{bmatrix}
0 & \pm I\\
I & 0
\end{bmatrix}.
$$
So if you already have a matrix $A$ that acts on direct line coordinates, you can get the corresponding action on dual-line coordinates by conjugating with $D$ (the chapter writes the resulting block-swap rule explicitly). This is exactly what you'd hope for: "dual line" is not a separate data type with separate physics—just a different coordinate face.

## Sparsity: why this matters for implementation

A full multivector in a 4D Clifford algebra has $2^4=16$ components. If you insisted on transforming arbitrary multivectors with dense $16\times 16$ matrices, you'd be doing work you don't need.

But geometric objects in the homogeneous model live in fixed grades with dimensions:
$$
1,\;4,\;6,\;4,\;1 \quad (\text{grades }0\text{ through }4),
$$
so you transform only the grade you actually have. Even if you're computing all induced grade transforms, the chapter notes the dramatic reduction compared to "transform everything as a generic 16D object," and then points out an extra practical win: *affine* transforms produce inherently sparse block matrices on these subspaces. That structure is what enables fast code paths and even automatic code generation later in the book.
