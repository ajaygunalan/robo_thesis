# outermorphism

Linear transformations act on vectors, but geometry is organized around subspaces. A $k$-dimensional subspace is represented by a $k$-blade, so we want an action of a linear map $f$ on blades that matches the geometric rule “apply $f$ to the spanning vectors, then take the span”.

Start with bivectors. A 2-blade $A=x\wedge y$ is the oriented parallelogram spanned by $x$ and $y$. If $f$ preserves the parallelogram construction for addition and scaling, then the induced action on 2-blades (call it $f_2$) should preserve the same construction at the level of area elements, so the natural definition is
$$
f_2[x\wedge y] \equiv f[x]\wedge f[y].
$$
Consistency follows because $\wedge$ is bilinear. If $x\wedge y$ is rewritten using sums or scalars, both sides expand the same way. The same argument extends to $k$-blades by “transform each factor, then wedge”, and linearity then extends the map to all multivectors.

The outermorphism of $f$ is this unique linear extension that commutes with wedge.
$$
f[\alpha] = \alpha,\quad
f[A \wedge B] = f[A] \wedge f[B],\quad
f[A + B] = f[A] + f[B].
$$
Because every blade is a wedge of vectors, the wedge rule determines $f$ on blades, and linearity extends it to arbitrary multivectors.

Two consequences are worth keeping in mind. Grade is preserved, so a $k$-blade is always mapped to a $k$-blade, and the outermorphism never “turns a bivector into a vector”. Non-invertible maps can still collapse a nonzero blade to $0$, which is the algebraic way to say “$k$-volume disappears”. Factorization is preserved: if $A=A' \wedge C$ and $B=C \wedge B'$ share a common factor blade $C$, then $f[A]$ and $f[B]$ share the factor $f[C]$, which is the algebraic shadow of “intersections map to intersections”.

Uniform scaling $S[x] = \alpha x$ on a $k$-blade gives $S[A] = \alpha^k A$. Length scales as $\alpha$, area as $\alpha^2$, and volume as $\alpha^3$.

Projection exposes a subtlety that is easy to misread geometrically. In the plane spanned by $\{a,b\}$, define a projection $P$ by $P[a]=a$ and $P[b]=0$ (projection onto the $a$-line). As a map on vectors, $P$ sends the set of vectors in the plane $\{\alpha a+\beta b\}$ to the set of vectors on the line $\{\alpha a\}$. But the blade $a\wedge b$ is not “the set of vectors in the plane”. It represents an oriented area element carried by two independent directions. The outermorphism therefore gives
$$
P[a\wedge b] = P[a]\wedge P[b] = a\wedge 0 = 0,
$$
which says that all area in that plane collapses under the projection. The plane-as-vectors can map to a line-as-vectors while the plane-as-2-blade maps to the zero 2-blade, because these are different kinds of objects. The relationship between contraction and orthogonal projection in the metric algebra is developed in [[geometric operations]].

Rotation reveals why blades are natural eigen-objects. A rotation $R$ in the $u \wedge v$ plane moves every vector, yet $R[u \wedge v] = R[u] \wedge R[v] = u \wedge v$. The oriented plane is fixed even though no vector in it is. Blades are the natural datatype for eigenspaces.

Metric operations (scalar products, contractions, norms) do not transform by $f$ alone. They require the [[adjoint]]. The top-grade case is especially rigid. Because the [[pseudoscalar]] space $\bigwedge^n\mathbb{R}^n$ is one-dimensional, $f[I_n]$ must be a scalar multiple of $I_n$, which defines the [[determinant]]. Basis-dependent encodings of outermorphisms live in [[outermorphism matrices]].
