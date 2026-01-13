# Chapter 4 — Linear Transformations of Subspaces

Linear algebra courses love matrices. The problem is: matrices are *not* the thing doing the work. The real object is a **linear transformation**—and once you start thinking that way, Chapter 4 becomes almost inevitable.

In Chapter 2, we upgraded “subspaces” from *sets you describe* to **blades you compute with**. This chapter does the next upgrade: if a linear map transforms vectors, it should also transform the *subspaces spanned by those vectors*—directly, without decomposing anything back into coordinates.

That extension is called an **outermorphism**. It’s the cleanest “lift” of a linear map from vectors to blades, because it preserves the one product that *defines* blades: the outer product.

**What we’ll build:**
- A principled extension of a linear map $f:\mathbb{R}^n\to\mathbb{R}^n$ to *all blades* (and then all multivectors).
- Transformation laws for the core products: $\wedge$, scalar product, contraction.
- The **adjoint** map $f^\dagger$ (transpose-in-disguise).
- A surprisingly compact **coordinate-free inverse** formula.
- Why **orthogonal** maps are special (they’re the only ones that preserve contraction structure).
- Why “normal vectors” are a trap under general transforms (and why bivectors win).

---

## 1. Linear maps: what they really guarantee

A linear transformation $f$ is defined by:

$$
f[\alpha x + \beta y] = \alpha f[x] + \beta f[y]
$$

Equivalently:

$$
f[\alpha x]=\alpha f[x],\qquad f[x+y]=f[x]+f[y]
$$

Geometric meaning (no fluff):
- Lines through the origin stay lines through the origin.
- Parallelogram addition is preserved.
- Translations are **not** linear (they don’t keep the origin fixed).

So far: standard linear algebra.

---

## 2. The key move: extend $f$ to blades (outermorphism)

A blade is built by wedging vectors. So the transformation rule should respect that construction.

### 2.1 The outermorphism rules

The **outermorphism** extension of $f$ is defined by:

$$
\boxed{
\begin{aligned}
f[\alpha] &= \alpha \\
f[A\wedge B] &= f[A]\wedge f[B] \\
f[A+B] &= f[A]+f[B]
\end{aligned}}
$$

That’s it. Everything else follows.

This is *not* an arbitrary choice. It’s forced by “span-of-transforms = transform-of-span”:
$$
f[a_1\wedge\cdots\wedge a_k] = f[a_1]\wedge\cdots\wedge f[a_k]
$$

### 2.2 Immediate consequences

Outermorphisms give you three high-value invariants:

- **Blades remain blades.**  
  Subspaces map to subspaces (still representable by a single blade).

- **Grade is preserved.**  
  If $A$ is a $k$-blade, then $f[A]$ is also a $k$-blade. Dimensions don’t magically change.

- **Common factors survive.**  
  If $A=A'\wedge C$ and $B=C\wedge B'$, then $f[A]$ and $f[B]$ share $f[C]$.  
  In geometric terms: intersections (meets) are structurally respected.

### 2.3 A warning you should actually remember

Outermorphisms preserve **grade**, not “the image of a set”.

So a projection that maps a *vector plane* to a *vector line* does **not** map the plane-blade to a line-blade. It maps it to a **zero 2-blade**.

If you expect “plane becomes line,” you’re mixing:
- the image of a *set of vectors*, versus
- the image of a *2D oriented area element*.

Those are different objects. The algebra is the one that stays consistent.

---

## 3. Examples that show what outermorphisms do (and don’t do)

### 3.1 Uniform scaling

If $S[x]=\alpha x$, then for an $n$-blade $A$,
$$
S[A]=\alpha^n A
$$

Areas scale like $\alpha^2$, volumes like $\alpha^3$, and so on. Orientation flips when $\alpha<0$ and the grade is odd.

### 3.2 Projection onto a line: “area disappears”

If $P[a]=a$ and $P[b]=0$ (projection in the $b$-direction onto the $a$-line), then:
$$
P[a\wedge b] = P[a]\wedge P[b] = a\wedge 0 = 0
$$

That’s correct: a 2-blade is an **area element**. Projection collapses area to zero.

### 3.3 Planar rotation has an eigenblade

A rotation $R$ in the plane of $u\wedge v$ satisfies:
$$
R[u\wedge v] = u\wedge v
$$

Vectors rotate (no real eigenvectors in that plane), but the **plane itself** is invariant: a real eigenblade of grade 2.

### 3.4 Point reflection: parity shows up cleanly

Point reflection is $x\mapsto -x$. For an $n$-blade:
$$
A \mapsto (-1)^n A
$$

Even-grade blades stay the same; odd grades flip orientation.

### 3.5 Orthogonal projection onto a blade extends cleanly

If the orthogonal projection of a vector $x$ onto a blade $B$ is
$$
P_B[x] = (x\;\!\!\lrcorner\;\! B)\;\!\!\lrcorner\;\! B^{-1},
$$
then outermorphism means:
$$
P_B[x\wedge y] = P_B[x]\wedge P_B[y]
$$
and in fact you can often rewrite it so you can apply the same projection formula directly to higher-grade blades.

The point: **you can project subspaces directly**.

---

## 4. Determinant, defined without matrices

A pseudoscalar $I_n$ represents an oriented unit $n$-volume element. Under $f$, it must map to another pseudoscalar, so:
$$
f[I_n] = \delta I_n
$$
and we define:
$$
\boxed{f[I_n] \equiv \det(f)\,I_n}
$$

So the determinant is literally “signed volume scaling.”

### 4.1 Easy determinant sanity checks

- Rotation: $\det(f)=1$.
- Projection onto a proper subspace (in $n>1$): $\det(f)=0$.
- Point reflection: $\det(f)=(-1)^n$.

### 4.2 Composition rule (no surprise, but clean)

For $g\circ f$:
$$
\det(g\circ f)=\det(g)\det(f)
$$

---

## 5. Metric products: scalar product and contraction under transforms

Outermorphisms preserve the **outer** product automatically. But the contraction and “inner-ish” products involve the **metric**, so you need more machinery.

### 5.1 Scalars stay scalars

Because the scalar product returns a scalar,
$$
f[A * B] = A * B
$$
This does **not** mean norms and angles are preserved. It just means “if the result is a scalar, applying $f$ doesn’t change it.”

The real question is: what is $(f[A])*(f[B])$? That’s where the adjoint enters.

### 5.2 The adjoint $f^\dagger$

The **adjoint** is defined implicitly by:
$$
\boxed{(f[a]) * b = a * (f^\dagger[b]) \quad \text{for all vectors }a,b}
$$

In Euclidean orthonormal coordinates, $f^\dagger$ is the transpose map. But this definition is coordinate-free.

Key properties:
- $(f^\dagger)^\dagger = f$
- $(f^{-1})^\dagger = (f^\dagger)^{-1}$

### 5.3 The contraction transformation law

This is the big one:

$$
\boxed{f[A\;\!\!\lrcorner\;\! B] = (f^\dagger)^{-1}[A]\;\!\!\lrcorner\;\! f[B]}
$$

You can remember it like this:
- the result is “a part of $B$,” so $B$ transforms with $f$,
- but “taking $A$ out orthogonally” drags in the inverse-adjoint.

---

## 6. Orthogonal transformations are the only ones that preserve contraction structure

A transformation is **orthogonal** if it preserves inner products of vectors:
$$
f[a]\cdot f[b] = a\cdot b \quad \forall a,b
$$

Then:
$$
\boxed{f^\dagger = f^{-1}}
$$

Plug that into the contraction law and it collapses to:
$$
\boxed{f[A\;\!\!\lrcorner\;\! B] = f[A]\;\!\!\lrcorner\;\! f[B]}
$$

So:
- every linear map is an **outermorphism** (preserves $\wedge$),
- but only orthogonal maps are also “innermorphisms” (structure-preserving for contraction).

That’s why rotations/reflections get special treatment later.

---

## 7. Duals, “normal vectors,” and why the cross product is brittle

The dual of a blade $X$ is:
$$
X^* \equiv X\;\!\!\lrcorner\;\! I_n^{-1}
$$

Here’s the catch: duality depends on the pseudoscalar (and therefore on the metric structure), so dual objects do **not** transform like direct objects.

### 7.1 Dual transformation law

If you want the transformed dual to equal the dual of the transformed blade:
$$
f_*(X^*) \equiv (f[X])^*
$$
then the required map is:
$$
\boxed{f_*[D] = \det(f)\,(f^\dagger)^{-1}[D]}
$$

So duals need $\det(f)$ and the inverse-adjoint.

### 7.2 The cross product is just a dual bivector… and that’s the problem

In 3D,
$$
a\times b = (a\wedge b)^*
$$

Therefore under a general linear $f$,
$$
\boxed{a\times b \;\mapsto\; \det(f)\,(f^\dagger)^{-1}[a\times b]}
$$

That is *not* the same as $f[a]\times f[b]$.

This is exactly the practical “normal vector bug” in graphics:
- points/directions transform with $f$,
- normals transform with $f^{-T}$ (and a determinant factor depending on conventions).

Geometric algebra’s fix is brutally simple: stop pretending a normal is a regular vector. Use the **bivector** $a\wedge b$ to represent the plane directly. It transforms cleanly:
$$
f[a\wedge b] = f[a]\wedge f[b]
$$

---

## 8. A coordinate-free inverse formula (yes, really)

Once you have the contraction transform rule, you can derive an explicit inverse formula in terms of pseudoscalars:

$$
\boxed{
f^{-1}[A] = \frac{\,f^\dagger\!\left[A\;\!\!\lrcorner\;\! I_n^{-1}\right]\;\!\!\lrcorner\;\! I_n\,}{\det(f)}
}
$$

In dual language:
$$
(f^{-1}[A])^* = \frac{f^\dagger[A^*]}{\det(f)}
$$

This looks “metric” because of the duals, but the duals cancel in a way that makes the result effectively non-metric (you can compute it in any convenient metric if needed).

---

## 9. Matrices: what they are (and what they aren’t)

A matrix is just a coordinate representation of a linear map relative to a basis $\{b_i\}$ and its reciprocal basis $\{b^j\}$.

The matrix element is:
$$
[f]^j{}_i \equiv f[b_i]\cdot b^j
$$

This chapter pushes a useful viewpoint:
- **Transformations are primary.**
- Matrices are implementation details.

### 9.1 Outermorphism matrices are “minors by design”

Once you know the matrix for vectors, the induced action on bivectors, trivectors, etc. is built from determinants of submatrices (minors). For bivectors, the matrix elements look like 2×2 minors:

$$
[f]^{j_1 j_2}{}_{i_1 i_2} =
[f]^{j_2}{}_{i_2}[f]^{j_1}{}_{i_1} - [f]^{j_1}{}_{i_2}[f]^{j_2}{}_{i_1}
$$

This is exactly what you’d expect: a bivector is an oriented area element, so it transforms by the area scaling induced by $f$.

### 9.2 Practical note: why implementations like matrices

If you apply the same linear map many times, precomputing the outermorphism matrices per grade is often faster than recomputing products each time. The chapter’s programming examples show this explicitly for projection.

---

## 10. Summary

Here are the load-bearing facts:

1. **Every linear map extends to blades as an outermorphism**
   $$
   f[A\wedge B]=f[A]\wedge f[B]
   $$

2. **Determinant is pseudoscalar scaling**
   $$
   f[I_n]=\det(f)I_n
   $$

3. **Adjoint is defined by scalar-product symmetry**
   $$
   (f[a])*b = a*(f^\dagger[b])
   $$

4. **Contraction transforms via inverse-adjoint**
   $$
   f[A\;\!\!\lrcorner\;\! B]=(f^\dagger)^{-1}[A]\;\!\!\lrcorner\;\! f[B]
   $$

5. **Orthogonal maps are exactly the ones that preserve contraction structure**
   $$
   f^\dagger=f^{-1}\quad\Rightarrow\quad f[A\;\!\!\lrcorner\;\! B]=f[A]\;\!\!\lrcorner\;\! f[B]
   $$

6. **Dual objects (like normals/cross products) transform differently**
   $$
   f_* = \det(f)\,(f^\dagger)^{-1}
   $$

7. **There’s a compact, coordinate-free inverse formula**
   $$
   f^{-1}[A] = \frac{\,f^\dagger[A\;\!\!\lrcorner\;\! I_n^{-1}]\;\!\!\lrcorner\;\! I_n\,}{\det(f)}
   $$

If Chapter 2 made subspaces computable, Chapter 4 makes them **movable**—correctly, cleanly, and without constantly dropping back to coordinates.
