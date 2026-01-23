# dual representations

Duality turns a $k$-blade into an $(n-k)$-blade that represents the orthogonal complement subspace. Fix an oriented unit [[pseudoscalar]] $I_n$ and let $X^*$ denote the dual of a blade $X$ as defined in [[duality and orthogonality]]. Then $X$ and $X^*$ encode complementary subspaces.

A direct blade transforms by the [[outermorphism]], $X \mapsto f[X]$. A dual blade is defined by a metric operation, so it cannot be pushed through $f$ by wedge alone. Define the induced action on duals as the map $f^*$ that preserves duality.
$$
f^*[X^*] \equiv (f[X])^*.
$$
If $f$ is invertible, this requirement forces
$$
f^*[D] = \det(f)\,\bar f^{-1}[D],
$$
where $\bar f$ is the [[adjoint]] and $\det(f)$ is defined by the image of the pseudoscalar in [[determinant]]. In orthonormal coordinates this becomes the inverse-transpose rule. Dual objects (such as normals) transform by $(\det M)\,M^{-T}$ rather than by $M$.

The 3D cross product $a \times b = (a \wedge b)^*$ exemplifies the issue. It transforms by $\det(f)\, \bar{f}^{-1}$ rather than by $f$, which is why graphics code patches normals with inverse-transpose. The conceptual fix is to represent the plane as the bivector $a \wedge b$, which transforms directly as $f[a] \wedge f[b]$, and dualize only at the end if a normal is needed [[the 3-d cross product]].
