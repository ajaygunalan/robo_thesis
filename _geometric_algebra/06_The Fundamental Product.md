# Chapter 6 — The Fundamental Product of Geometric Algebra

By Chapter 5 you’ve built a useful “subspace algebra”: the **outer product** tells you *what subspace you span*, and the **contraction** tells you *how much* (projections, measures, etc.). The catch is brutal and unavoidable:

- The inner product / contraction is **not invertible**.
- The outer product is **not invertible**.

So you can’t reliably solve even simple geometric equations by “dividing” through them.

Clifford’s move (1872) is to stop treating “spanning” and “measuring” as separate worlds and **fuse them into one product** that contains *both* kinds of information at once. That product is the **geometric product**. Once you have it, you can manipulate geometric relationships almost like ordinary algebra, because you can actually **invert** things and do **division**.

**What we’ll build in this chapter:**

- A single product $ab$ on vectors (and later multivectors) whose
  - symmetric part is the inner product,
  - antisymmetric part is the outer product,
  - and which is **associative** and often **invertible**.
- A clean “operator” viewpoint: ratios like $b/a$ act as transformations (rotation + scaling in 2D).
- A way to recover the old subspace products (wedge, contractions, scalar product) from the geometric product.
- Practical geometric division: projection, rejection, and reflection become one-liners.

---

## 1. Why dot and wedge don’t let you solve equations

Take a fixed nonzero vector $a$ and an unknown vector $x$.

### 1.1 Knowing only $x\cdot a$ is not enough

If all you know is the scalar
$$
x\cdot a = \alpha,
$$
then the endpoint of $x$ lies on a **hyperplane orthogonal to $a$**. Many $x$ satisfy this. There is no unique “inner division.”

### 1.2 Knowing only $x\wedge a$ is not enough

If all you know is the bivector
$$
x\wedge a = B,
$$
then $x$ must lie on a **line** (offset from the origin) parallel to $a$. Still not unique. There is no “outer division.”

### 1.3 But together they *do* determine $x$

Geometrically, the plane from $x\cdot a$ and the line from $x\wedge a$ intersect in a single point: that’s $x$. Figure 6.1 in the PDF literally sketches this intersection idea (yellow plane + blue line).

**Conclusion:** we want one product $xa$ that carries *both* pieces of information.

---

## 2. The geometric product of vectors

### 2.1 Symmetry vs antisymmetry

- The inner product is **symmetric**: $x\cdot a = a\cdot x$.
- The outer product is **antisymmetric**: $x\wedge a = -(a\wedge x)$.

So define a new product $xa$ whose

$$
x\cdot a = \tfrac12(xa + ax), \qquad
x\wedge a = \tfrac12(xa - ax).
$$

Add them and you get the defining formula:

$$
\boxed{\,xa \;\equiv\; x\cdot a \;+\; x\wedge a\,}
$$

This is the **geometric product** (aka Clifford product).

### 2.2 Why this is “weird” but powerful

- $x\cdot a$ is grade 0 (scalar).
- $x\wedge a$ is grade 2 (bivector).

So $xa$ is a **mixed-grade multivector** (scalar + bivector). That’s exactly why it can be invertible: the two grades don’t “confuse” each other under addition.

---

## 3. Core algebraic properties you must not forget

From the chapter:

| Property | Status | What it means in practice |
|---|---|---|
| Commutative? | **No** (in general) | Order matters. $ab\neq ba$ unless $a\wedge b=0$ (parallel). |
| Anticommutative? | Also **no** (in general) | $ab=-ba$ would force $a\cdot b=0$ (orthogonal), a special case. |
| Linear + distributive | Yes | Inherits from dot + wedge. |
| **Associative** | Defined to be | This is what makes division sane and inverses unique. |

If you keep one thing in your head: **the geometric product is associative but not commutative**. That single fact drives almost everything later.

---

## 4. Computing with a basis (and why $e_{12}^2=-1$ shows up)

Let $\{e_i\}$ be an orthonormal basis in a metric space.

### 4.1 Basis vector squares encode the metric

$$
e_i e_i = e_i\cdot e_i = Q[e_i,e_i]
$$
So in Euclidean space $e_i^2 = 1$. In other signatures, $e_i^2$ can be $-1$.

### 4.2 Different basis vectors anticommute

For $i\neq j$:
$$
e_i e_j = e_i\wedge e_j = - e_j e_i.
$$

### 4.3 The “complex unit” is hiding as a bivector in 2D

Define $e_{12}:=e_1e_2$. Then in Euclidean $R^{2,0}$:

$$
e_{12}^2 = (e_1e_2)(e_1e_2) = -1.
$$

So the algebra contains an element that squares to $-1$, but it’s **not imaginary**—it’s a real oriented plane element.

### 4.4 A concrete 2D product formula

For $a=a_1e_1+a_2e_2$ and $b=b_1e_1+b_2e_2$:

$$
ab = (a_1b_1+a_2b_2) + (a_1b_2-a_2b_1)e_{12}.
$$

Scalar part = dot product, bivector part = oriented area.

---

## 5. Division by a vector (finally!)

### 5.1 Inverse of a vector

If $a\cdot a\neq 0$ (not a null vector), then

$$
\boxed{\,a^{-1} = \frac{a}{a\cdot a} = \frac{a}{\|a\|^2}\,}
$$

and indeed $a^{-1}a=1$. Null vectors don’t have inverses.

### 5.2 Right division vs left division

Because $ab\neq ba$, division is also noncommutative:

- $(xa)/a$ means **right division**: $(xa)a^{-1}$.
- $a^{-1}(xa)$ is a different beast (and will become reflection).

---

## 6. Ratios of vectors are operators

This is one of the chapter’s “stop and appreciate this” moments.

### 6.1 Similarity problem in 2D

Solve: “$x$ is to $c$ as $b$ is to $a$” i.e. $x:c=b:a$.

Read it as a geometric-product ratio:
$$
x c^{-1} = b a^{-1}
\quad\Rightarrow\quad
\boxed{\,x = (b a^{-1})c\,}.
$$

### 6.2 Why that’s more than a trick

The multivector $b a^{-1}$ acts like a **combined scaling + rotation operator** on vectors in the plane. If you express it in polar form, it reproduces the usual 2×2 rotation-scaling matrix — but without ever introducing coordinates as the *conceptual* starting point. The chapter even calls the matrix form “assembly code” compared to the coordinate-free expression.

---

## 7. The geometric product for multivectors

Up to now we defined $ab$ using dot+wedge. The chapter then flips the story: the geometric product is actually more fundamental, so it should be definable *without* mentioning the other products.

### 7.1 Axioms (the algebraic definition)

The geometric product is defined by:

1. **Scalars behave like scalars**: $\alpha A = A\alpha$.
2. **Vector squares are scalars**: $x^2 = x\cdot x = Q[x,x]$.
3. **Distributive/linear** in both arguments.
4. **Associative**: $A(BC)=(AB)C$.
5. Not required to be commutative or anticommutative.

### 7.2 Polarization gives the inner product back

From bilinearity:
$$
x\cdot y = \tfrac12\big((x+y)^2 - x^2 - y^2\big)
= \tfrac12(xy+yx).
$$

So the inner product is the **symmetric part** of the geometric product.

### 7.3 Grades get mixed (and that’s expected)

If $A_k$ is grade $k$ and $B_\ell$ is grade $\ell$, then

$$
A_k B_\ell \;\text{can contain grades}\;
|k-\ell|,\ |k-\ell|+2,\ \ldots,\ k+\ell.
$$

Common vector factors “collapse” to scalars and drop the grade by 2 each time.

This is the price (and the benefit) of having a product that captures *everything* about relative geometry.

---

## 8. Getting the old subspace products back

You don’t lose wedge and contraction. You just stop treating them as “primitive.”

The chapter gives two complementary routes.

### 8.1 Symmetry formulas (vector with a blade)

Let $a$ be a vector and $B$ a blade. With grade involution $\hat{B}=(-1)^{\mathrm{grade}(B)}B$:

$$
a\wedge B = \tfrac12\big(aB + \hat{B}a\big),
\qquad
a\!\rfloor B = \tfrac12\big(aB - \hat{B}a\big),
$$

and similarly on the right:
$$
B\wedge a = \tfrac12\big(Ba + a\hat{B}\big),
\qquad
B\!\lfloor a = \tfrac12\big(Ba - a\hat{B}\big).
$$

A key decomposition falls straight out:

$$
\boxed{\,aB = a\!\rfloor B \;+\; a\wedge B\,}
$$
which generalizes $ab = a\cdot b + a\wedge b$.

### 8.2 Grade-selection definitions (works for all blades)

Use grade selection $\langle\ \rangle_k$. For vectors:

$$
a\cdot b = \langle ab\rangle_0,
\qquad
a\wedge b = \langle ab\rangle_2.
$$

For blades $A_k, B_\ell$:

$$
A_k\wedge B_\ell := \langle A_k B_\ell\rangle_{k+\ell},
$$
$$
A_k\!\rfloor B_\ell := \langle A_k B_\ell\rangle_{\ell-k},
\qquad
A_k\!\lfloor B_\ell := \langle A_k B_\ell\rangle_{k-\ell},
$$
$$
A_k * B_\ell := \langle A_k B_\ell\rangle_{0}.
$$

This is the “single-product implementation” viewpoint: implement $AB$ once, and derive everything else by selecting grades.

---

## 9. Geometric division: projection, rejection, reflection

This is where invertibility pays rent.

### 9.1 Inverse of a blade

If a blade $A$ is non-null, then it has an inverse:

$$
\boxed{\,A^{-1} = \frac{\tilde{A}}{A * \tilde{A}} = \frac{\tilde{A}}{\|A\|^2}\,}
$$

where $\tilde{A}$ is the reverse (reversion).

Versors (products of invertible vectors) are also invertible; that’s Chapter 7’s whole game.

### 9.2 Projection and rejection via division

For a vector $x$ relative to a vector $a$:

$$
x = (xa)a^{-1} = (x\cdot a)a^{-1} + (x\wedge a)a^{-1}.
$$

So:

- **Projection onto $a$**:
  $$
  \mathrm{proj}_a(x) = (x\cdot a)a^{-1} = \frac{x\!\rfloor a}{a}.
  $$
- **Rejection by $a$** (the perpendicular leftover):
  $$
  \mathrm{rej}_a(x) = (x\wedge a)a^{-1} = \frac{x\wedge a}{a}.
  $$

Figure 6.3 illustrates this decomposition as “component along the line” plus “component orthogonal to it.”

For a general blade $A$:

$$
x = (xA)A^{-1} = (x\!\rfloor A)A^{-1} + (x\wedge A)A^{-1},
$$
so
$$
\mathrm{proj}_A(x)=\frac{x\!\rfloor A}{A},\qquad
\mathrm{rej}_A(x)=\frac{x\wedge A}{A}.
$$

Projection extends nicely to blades (outermorphism):
$$
X \mapsto (X\!\rfloor A)A^{-1}.
$$
The rejection does **not** extend as cleanly if you want to stay within blades; the chapter is explicit about this disappointment.

### 9.3 The “other” division is reflection

Left-division gives a different result:

$$
a^{-1}xa = (x\cdot a)a^{-1} - (x\wedge a)a^{-1}.
$$

So the parallel component stays, the perpendicular component flips: that’s exactly a **reflection of $x$ in the line of $a$**. The PDF shows this as Figure 6.4.

This sandwiching pattern $a^{-1}xa$ (or $axa^{-1}$) is the seed of the **versor** machinery for orthogonal transformations in the next chapter.

---

## 10. Bonus: Gram–Schmidt as repeated rejections

Once division exists, orthogonalization becomes a geometric one-liner.

Given vectors $v_1, v_2, v_3$ in Euclidean space:

$$
b_1 := v_1,
\qquad
b_2 := \frac{v_2\wedge b_1}{b_1},
\qquad
b_3 := \frac{v_3\wedge b_1\wedge b_2}{b_1\wedge b_2}.
$$

Figure 6.5 visualizes this as “keep rejecting the next vector from what you’ve already built.”

---

## 11. Summary

This chapter’s message is simple:

1. **Dot and wedge are incomplete** on their own because they’re not invertible.
2. The **geometric product** $ab = a\cdot b + a\wedge b$ merges measurement + spanning and becomes invertible.
3. With associativity + inverses, you get **division**, which turns geometry into solvable algebra.
4. Wedge, contractions, and scalar products are still there — now as **derived views** of the one fundamental product.
5. The “sandwich” $a^{-1}xa$ is reflection, and generalizes to the versor/rotor machinery next.

The geometric product is the point where geometric algebra stops being “a nicer Grassmann algebra” and becomes a full-blown computational engine.
