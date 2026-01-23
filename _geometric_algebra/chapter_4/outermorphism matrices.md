# outermorphism matrices

Matrices are basis-dependent encodings of a linear map. Given a basis $\{b_i\}$ with reciprocal $\{b^j\}$ satisfying $b_i * b^j = \delta_i^j$, the vector-level matrix elements are
$$
[f]^j{}_i = f[b_i] * b^j,
$$
so the $i$-th column is the transformed basis vector $f[b_i]$ expressed in the reciprocal frame.

In a Euclidean orthonormal basis, $b^j=b_j$ and $*$ reduces to the dot product, so this becomes the familiar entry $[f]^j{}_i = f[b_i]\cdot b_j$.

Higher grades follow from the [[outermorphism]] rule $f[A\wedge B]=f[A]\wedge f[B]$. For bivectors with basis $b_{ij} = b_i \wedge b_j$, the induced matrix entries are $2\times 2$ minors of the vector-level matrix.
$$
[f]^{j_1 j_2}{}_{i_1 i_2} = [f]^{j_1}{}_{i_1}[f]^{j_2}{}_{i_2} - [f]^{j_1}{}_{i_2}[f]^{j_2}{}_{i_1}.
$$
The subtraction is wedge antisymmetry, and the product structure is wedge multilinearity. The same expansion in grade $k$ produces $k\times k$ minors. The $k$-vector matrix is the $k$-th exterior power of the vector-level matrix.
