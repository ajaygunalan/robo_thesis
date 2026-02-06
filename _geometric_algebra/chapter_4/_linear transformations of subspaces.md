# linear transformations of subspaces

Geometry is organized around subspaces, not just vectors. A $k$-blade $A=a_1\wedge\cdots\wedge a_k$ represents the subspace spanned by the vectors $a_i$, so a linear map $f$ should send that subspace to the one spanned by $f[a_i]$. The [[outermorphism]] is the blade-level extension of $f$ that enforces this "transform the spanning vectors, then take the span" principle, characterized by
$$
f[A \wedge B] = f[A] \wedge f[B].
$$

Wedge is metric-free, but most geometry is not. Angles, lengths, and orthogonality enter through metric products, so they require extra structure. The [[adjoint]] $\bar f$ is the map that moves $f$ across the scalar product,
$$
f[a] * b = a * \bar f[b],
$$
and it is the object that appears whenever a transformation law depends on the metric (in particular, for contraction).

Two recurring tasks then become transparent. Oriented $n$-volume is carried by a [[pseudoscalar]], and its image under an outermorphism defines the [[determinant]],
$$
f[I_n] = \det(f)\, I_n.
$$
The same pseudoscalar also implements duality, and combining duality with the adjoint yields the coordinate-free [[inverse via pseudoscalar|inverse formula]]
$$
(f^{-1}[A])^* = \frac{\bar{f}[A^*]}{\det(f)}.
$$

A blade can represent a subspace directly (as its span) or as a dual representative of its orthogonal complement. Those two representations transform differently: direct blades transform by $f$, while dual blades transform by
$$
f^*[D] = \det(f)\,\bar f^{-1}[D],
$$
which is the content of [[dual representations]] and explains the inverse-transpose rule for normals.

If you choose a basis, all of these maps become matrices. The outermorphism on $k$-blades is encoded by $k\times k$ minors of the vector-level matrix, as shown in [[outermorphism matrices]].
