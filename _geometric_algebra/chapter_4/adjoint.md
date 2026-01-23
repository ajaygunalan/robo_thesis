# adjoint

Outermorphisms handle wedge products without reference to the metric, but contractions and norms are metric-dependent. The adjoint $\bar f$ is the linear map that lets $f$ move across the scalar product.

Write the scalar product as $A * B$ (grade-$0$ part). For vectors this is $a*b=a\cdot b$. The adjoint is defined on vectors by
$$
f[a] * b = a * \bar f[b]\qquad \text{for all vectors }a,b.
$$
In an orthonormal basis this is the transpose map. The definition above is basis-free.

The adjoint extends to blades as an [[outermorphism]], so for blades the scalar product satisfies
$$
\bar f[A] * B = A * f[B].
$$
Two identities follow directly from this defining relation. Taking the adjoint twice returns the original map: $\overline{\bar f}=f$. If $f$ is invertible, then taking adjoints commutes with inversion: $\overline{f^{-1}}=(\bar f)^{-1}$.

Define the left contraction $A \lrcorner B$ by the adjointness relation $(X \wedge A) * B = X * (A \lrcorner B)$. If $f$ is invertible, combining the scalar-product identity with that relation yields the contraction transformation law
$$
f[A \lrcorner B] = \bar f^{-1}[A] \lrcorner f[B].
$$
The forward transform $f[B]$ is the object being kept. The inverse-adjoint $\bar f^{-1}[A]$ appears because contraction depends on orthogonality, and orthogonality depends on the metric. This asymmetry is the geometric source of the inverse-transpose rule.

Orthogonal transformations collapse the asymmetry. Preserving inner products ($f[a] * f[b] = a * b$ for all vectors $a,b$) is equivalent to $\bar{f} = f^{-1}$, so contraction becomes structure-preserving: $f[A \lrcorner B] = f[A] \lrcorner f[B]$. Orthogonal maps preserve the full subspace algebra.

The adjoint also governs norms:
$$
(f[A]) * (f[A]) = A * (\bar f \circ f)[A].
$$
The composite $\bar f \circ f$ measures how $f$ distorts the metric. For orthogonal maps it is the identity, which is exactly the statement that lengths and angles are preserved.

The implicit definition of the adjoint relies on the metric being able to distinguish vectors. In a nondegenerate metric, $u*b=0$ for all vectors $b$ forces $u=0$, so the equation $f[a]*b=a*\bar f[b]$ uniquely determines $\bar f$. In a degenerate metric there are nonzero “invisible” vectors $u\neq 0$ with $u*b=0$ for all $b$, so the same implicit equation cannot pin down $\bar f$ uniquely. A parallel nondegeneracy caveat appears in [[contraction (⌋)]].
