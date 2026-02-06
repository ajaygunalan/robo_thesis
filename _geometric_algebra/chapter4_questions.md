# Chapter 4: Linear Transformations of Subspaces - Conceptual Questions

## 4.1 Linear Transformations of Vectors

A linear transformation $\mathsf{f} : \mathbb{R}^n \to \mathbb{R}^n$ satisfies $\mathsf{f}[\alpha \mathbf{x} + \beta \mathbf{y}] = \alpha \mathsf{f}[\mathbf{x}] + \beta \mathsf{f}[\mathbf{y}]$. Explain why this means lines through the origin stay lines through the origin with preserved ratios, and why the parallelogram law of addition is preserved. Why does this include scaling, rotation, and reflection (through origin) but exclude translation?


## 4.2 Outermorphisms: Linear Transformations of Blades

The outermorphism extension of $\mathsf{f}$ to blades is defined by $\mathsf{f}[\alpha] = \alpha$ and $\mathsf{f}[A \wedge B] = \mathsf{f}[A] \wedge \mathsf{f}[B]$. Explain why this guarantees that blades remain blades, grades are preserved, and the meet (intersection) of subspaces is preserved. How does the determinant emerge naturally as $\mathsf{f}[I_n] = \det(\mathsf{f}) I_n$, and why does a rotation in a plane have the plane itself as an eigenblade even though no vector in that plane is an eigenvector?


## 4.3 Linear Transformation of the Metric Products

The scalar product transforms trivially as $\mathsf{f}[A * B] = A * B$ since it returns a scalar, but the contraction requires the adjoint $\bar{\mathsf{f}}$ (defined by $\bar{\mathsf{f}}[\mathbf{a}] * \mathbf{b} = \mathbf{a} * \mathsf{f}[\mathbf{b}]$) and transforms as $\mathsf{f}[A \rfloor B] = \bar{\mathsf{f}}^{-1}[A] \rfloor \mathsf{f}[B]$. Why do orthogonal transformations simplify this to $\mathsf{f}[A \rfloor B] = \mathsf{f}[A] \rfloor \mathsf{f}[B]$, and why does the dual representation transform as $\mathsf{f}^*[D] = \det(\mathsf{f}) \bar{\mathsf{f}}^{-1}[D]$ rather than simply $\mathsf{f}[D]$?


## 4.4 Inverses of Outermorphisms

The inverse of an outermorphism has the coordinate-free formula $\mathsf{f}^{-1}[A] = \frac{\bar{\mathsf{f}}[A \rfloor I_n^{-1}] \rfloor I_n}{\det \mathsf{f}}$. Explain why this formula involves two dualizations (which cancel metrically) and how it generalizes the classical minor-based matrix inverse construction to work directly on blades of any grade.


## 4.5 Matrix Representations

The matrix element $[[\mathsf{f}]]^j_i = \mathsf{f}[\mathbf{b}_i] \cdot \mathbf{b}^j$ represents the $j$-coordinate of the transformed $i$th basis vector. Explain why the outermorphism on $k$-blades can be represented by a $\binom{n}{k} \times \binom{n}{k}$ matrix constructed from the vector transformation matrix, and why precomputing this outermorphism matrix is more efficient than repeatedly applying the definition $\mathsf{f}[A \wedge B] = \mathsf{f}[A] \wedge \mathsf{f}[B]$.
