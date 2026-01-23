## Direct flats: wedge points with $\infty$

The chapter switches from dual objects (vectors as dual spheres/planes) to *direct* objects built by outer products, because direct blades carry orientation naturally.

Take $k{+}1$ unit points $p_0,\dots,p_k$ and build
$$
X=\alpha\,(p_0\wedge p_1\wedge\cdots\wedge p_k\wedge \infty).
$$
This blade contains $\infty$ by construction, so it is already "improper" in the homogeneous-model sense. The chapter shows (by translating to the origin and using antisymmetry to subtract a common point) that, up to rewriting, this class collapses to the standard form
$$
X = o\wedge A_k\wedge \infty,
$$
with $A_k$ a purely Euclidean $k$-blade encoding the direction subspace (PDF pages 16–18).

To interpret $X$, probe with a point $x$ via the incidence equation
$$
x\wedge X=0.
$$
Because the $o$ and $\infty$ factors kill the non-Euclidean bookkeeping terms, the condition reduces to
$$
\mathbf{x}\wedge A_k=0,
$$
which is exactly the vector-space-model statement "$\mathbf{x}$ lies in the $k$-subspace spanned by $A_k$." So $o\wedge A_k\wedge\infty$ is a $k$-flat through the origin, and its Euclidean transforms represent general offset flats (PDF pages 17–18).

The general direct $k$-flat through point $p$ is therefore
$$
\text{direct flat} = p\wedge A_k\wedge \infty.
$$
That's the conformal model's "flat primitive."

Figure 13.2 (PDF page 19) shows concrete examples: a plane $p\wedge q\wedge r\wedge\infty$, a plane $s\wedge t\wedge\infty$, and the flat point $u\wedge\infty$ at their intersection.

## Directions as "free" flats

Inside $p\wedge A_k\wedge\infty$ you can read $p$ as location and $A_k\wedge\infty$ as the direction element. That suggests the pure direction object is
$$
\text{direct direction} = A_k\wedge \infty.
$$
The chapter verifies this behaves exactly as a direction should: rotation-covariant but translation-invariant (PDF page 22).

## The homogeneous model is literally the $\infty$-sector

This is the cleanest conceptual bridge in the chapter: the homogeneous model is embedded in the conformal model as the algebra of blades involving $\infty$.

* A homogeneous point corresponds to the *flat point* $p\wedge\infty$ (not the null vector $p$ itself).
* A line through points $p,q$ is $p\wedge q\wedge\infty$, which you can rewrite as $p\wedge(\mathbf{q}-\mathbf{p})\wedge\infty$ to expose "point + direction" just like homogeneous practice (PDF page 20).

The subtlety the chapter flags is worth taking seriously: a conformal point $p$ is a zero-radius (dual) sphere, while a flat point $p\wedge\infty$ is what you get as the meet of flats (it includes the finite intersection point *and* the shared point at infinity). They look the same if you only think in $E^n$, but the algebra distinguishes them—and that distinction is exactly what makes later computations cleaner.

## Dual flats without the homogeneous-model awkwardness

Dualization in the full conformal space uses the pseudoscalar
$$
I_{n+1,1}=o\wedge I_n\wedge \infty,
$$
and the chapter emphasizes a pleasant fact specific to having *two* extra dimensions: $(o\wedge\infty)^2=1$, so $o\wedge\infty$ is its own inverse and the inverse pseudoscalar takes the clean form
$$
I_{n+1,1}^{-1}=o\wedge I_n^{-1}\wedge \infty
$$
(PDF page 21).

Dual flats inherit the same Euclidean versor action as direct flats: you move them by the same translator/rotor sandwiches, without needing the special "dual translation" machinery that made the homogeneous model fussy (PDF page 21–22).
