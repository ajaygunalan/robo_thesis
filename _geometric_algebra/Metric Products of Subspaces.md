# Chapter 3 — Metric Products of Subspaces

Chapter 2 gave us *spanning*: subspaces as blades, built with the outer product. That was intentionally **non-metric**: no lengths, no angles, no perpendicularity. It was clean — and also limited.

Here’s the blunt limitation: the outer product can compare **lengths along the same line**, **areas in the same plane**, and **volumes in the same space**. But it cannot compare lengths on *different* lines, or areas in *different* planes. For that you need a metric. This chapter bolts that missing piece onto the subspace algebra: a **real-valued metric product** that works on blades.

**What we’ll build:** a metric-aware toolbox for subspaces:
- a scalar product `∗` between **same-grade blades** (norms + angles),
- a grade-reducing inner product called the **contraction** (the workhorse),
- **duality / orthogonal complements** as blades,
- **orthogonal projection** of subspaces,
- **reciprocal frames** for non-orthonormal coordinates,
- and a clean explanation of why the **3D cross product** is a special-case hack we can avoid.

---

## 1. The Metric Upgrade: From “Spanning” to “Measuring”

A *metric space* is just a vector space with a bilinear form (equivalently, an inner/dot product) that lets you compute norms and angles. In Euclidean intuition:

- length: $\|a\|^2 = a\cdot a$
- angle: $\cos\theta = \dfrac{a\cdot b}{\|a\|\|b\|}$

The book is careful about the bigger picture:
- In general you can have signatures $R^{p,q}$ (some “negative” directions), and even **degenerate** metrics where nonzero “null vectors” satisfy $a\cdot a = 0$.  
- But you can safely build intuition in the positive-definite Euclidean case first.

The goal of the chapter is simple: **extend the dot product from vectors to blades** in a way that produces sensible geometric measurements (length/area/volume) and sensible notions of relative attitude (angles).

---

## 2. Scalar Product `∗`: A Dot Product for Blades of the Same Grade

### 2.1 Definition (same grade only)

The scalar product is a mapping

$$
\ast : \bigwedge^k\mathbb{R}^n \times \bigwedge^k\mathbb{R}^n \to \mathbb{R},
$$

and it’s defined on two factored $k$-blades

$$
A = a_1\wedge\cdots\wedge a_k,\qquad B = b_1\wedge\cdots\wedge b_k
$$

as the determinant of the matrix of pairwise dot products:

$$
A \ast B \;=\; \det\!\big[\,a_i\cdot b_j\,\big]_{i,j=1}^k.
$$

It is **zero between unequal grades**.

**Why a determinant?** Because it’s the only natural way to combine dot products so that:
- the result is **multilinear**,
- swapping two vectors flips sign (so it respects the antisymmetry “flavor” of wedges),
- and (crucially) it becomes independent of *how* you factor the blade (it depends on the subspace, not your chosen spanning vectors).

There are useful symmetries (the book uses reversion $\tilde{\;}$):

$$
B\ast A = A\ast B = \tilde A \ast \tilde B.
$$



### 2.2 Norms of blades = metric sizes of subspaces

The squared norm of a blade is defined as:

$$
\|A\|^2 \equiv A^2 = A \ast \tilde A.
$$



This lines up with geometry exactly:

- **Vectors:** $a\ast a = a\cdot a$ gives squared length.  
- **Bivectors:** for $A=a_1\wedge a_2$,

  $$
  \|A\|^2 = (a_1\cdot a_1)(a_2\cdot a_2) - (a_1\cdot a_2)^2
          = (\|a_1\|\|a_2\|\sin\psi)^2,
  $$

  i.e. the squared area of the parallelogram.  
- **$k$-blades:** $\|A\|^2$ becomes the Gram determinant, i.e. the squared $k$-dimensional volume.

So the scalar product gives an *absolute* size (within the metric), not merely a “relative weight within the same attitude” like in Chapter 2.

### 2.3 Angles between subspaces (same grade)

Once you can measure, you can compare. The chapter defines the cosine of the angle $\theta$ between same-grade blades by the direct analogue of the vector formula:

$$
\cos\theta = \frac{A \ast \tilde B}{\|A\|\|B\|}.
$$



For 2-blades, the book explains this by factoring out a common direction and reducing the problem to an angle between two vectors in the shared plane.

**Important nuance:** in higher dimensions, “the angle between two $k$-subspaces” can involve multiple independent rotations (principal angles). The scalar-product cosine effectively becomes the **product of cosines** of those orthogonal rotations; it hits zero as soon as one of them is a right angle, which is the correct generalization of “perpendicular”.

---

## 3. The Contraction: The Metric Inner Product That Actually Does Work

The scalar product only works between blades of the **same** grade. But geometry constantly needs “mixed-grade interaction”:

- a vector with a plane,
- a line with a volume,
- a plane with a 4D bivector, etc.

This chapter derives (almost inevitably) a grade-reducing inner product between blades of different grades: the **contraction**.

### 3.1 Implicit motivation: “factor out the common part”

Suppose $B$ and $Y$ are blades of the same grade and share a factor $A$. If $Y=X\wedge A$, then we want to “remove” the shared $A$ from the scalar product:

$$
(X\wedge A)\ast B \;=\; X \ast (A \!\rfloor\! B).
$$

That implicitly defines a new object $A\!\rfloor\!B$: **the contraction of $A$ onto $B**.

From grade bookkeeping, you immediately get:

$$
\operatorname{grade}(A\!\rfloor\!B) = \operatorname{grade}(B) - \operatorname{grade}(A),
$$

(with the convention that negative grades mean “zero”).

When the grades match, the contraction reduces to the scalar product (so it’s a genuine generalization).

### 3.2 Explicit definition: computation rules (the practical version)

The implicit definition is conceptually clean but not computationally convenient (and it can fail to uniquely determine results in degenerate metrics). The book therefore gives axioms that define the contraction constructively.

For scalars $\alpha$, vectors $a,b$, and blades $A,B,C$:

1. Scalars pull out:
   $$
   \alpha \!\rfloor\! B = \alpha B
   $$
2. Contracting a blade into a scalar gives zero (if the blade has positive grade):
   $$
   B \!\rfloor\! \alpha = 0 \quad\text{if }\operatorname{grade}(B)>0
   $$
3. For vectors, contraction is the dot product:
   $$
   a\!\rfloor\! b = a\cdot b
   $$
4. Derivation rule over wedges:
   $$
   a\!\rfloor\!(B\wedge C)
   = (a\!\rfloor\!B)\wedge C + (-1)^{\operatorname{grade}(B)}\,B\wedge (a\!\rfloor\!C)
   $$
5. Associative “peeling”:
   $$
   (A\wedge B)\!\rfloor\!C = A\!\rfloor\!(B\!\rfloor\!C)
   $$



These rules make contraction:
- bilinear,
- distributive over addition,
- and algorithmically computable by repeatedly contracting one vector at a time.

### 3.3 The one formula you actually use

A big payoff is the expansion for contracting a vector $x$ into a factored blade:

$$
x\!\rfloor\!(a_1\wedge\cdots\wedge a_k)
=\sum_{i=1}^k (-1)^{i-1}\,(x\cdot a_i)\;
a_1\wedge\cdots\wedge \widehat{a_i}\wedge\cdots\wedge a_k
$$

(where $\widehat{a_i}$ means “omit $a_i$”).

For a bivector, this collapses to the classic-looking identity:

$$
x\!\rfloor\!(a_1\wedge a_2) = (x\cdot a_1)\,a_2 - (x\cdot a_2)\,a_1.
$$



This is the contraction doing exactly what you want: take a vector and a plane element and return a vector *in that plane*.

---

## 4. What the Contraction Means Geometrically

The book gives several properties that together pin down the geometry:

1. $A\!\rfloor\!B$ is a **blade** (if $A$ and $B$ are blades), so it denotes an oriented subspace.  
2. It is **contained in $B$**. (Repeatedly expand the contraction; you never introduce vectors outside $B$.)  
3. For a vector $x$, $x\!\rfloor\!A=0$ iff $x$ is perpendicular to every vector in $A$.  
4. The result $A\!\rfloor\!B$ is **perpendicular to $A$** (in the metric sense).  
5. The grade drop is exactly “remove dimensions”:  
   $\operatorname{grade}(A\!\rfloor\!B)=\operatorname{grade}(B)-\operatorname{grade}(A)$.

So the contraction is best summarized as:

> **$A\!\rfloor\!B$ picks out the part of $B$ that is (i) still inside $B$, (ii) perpendicular to $A$, and (iii) has the right reduced grade.**

In 3D intuition: for a vector $x$ and a plane (bivector) $B$, the contraction $x\!\rfloor\!B$ is the **vector in the plane** that is **perpendicular to $x$** (and its magnitude encodes how well $x$ “fits into” the plane).

---

## 5. The “Other” Contraction (Right Contraction)

Because “removing” is asymmetric, you can define a right contraction by swapping the role of the wedge factor in the scalar product:

$$
B \ast (A\wedge X) = (B \!\lfloor\! A)\ast X.
$$



It’s not a new geometric concept; it differs from the left contraction only by a grade-dependent sign (via reversion).

Practical rule of thumb: pick one convention and stick with it. Most of the book uses the **left** contraction.

---

## 6. Orthogonality, Duality, and the Orthogonal Complement

### 6.1 Contraction is nonassociative — and that’s fine

In general, $A\!\rfloor\!(B\!\rfloor\!C)\neq (A\!\rfloor\!B)\!\rfloor\!C$ (their grades don’t even match).

But there *are* two key “duality formulas” involving wedges + contractions (one universal, one conditional).

### 6.2 Inverse of a blade (relative to contraction)

A blade doesn’t have a unique inverse in a naive sense, but you can define a **canonical** inverse using its norm:

$$
A^{-1} \equiv \frac{\tilde A}{\|A\|^2}.
$$

(Up to a grade-dependent sign, depending on conventions.)

It satisfies the expected contraction identity:

$$
A\!\rfloor\!A^{-1}=1.
$$



**Caveat:** if $A$ is *null* ($\|A\|=0$), this inverse doesn’t exist. The book notes you then need the more subtle **reciprocal** concept.

### 6.3 Dualization = “orthogonal complement as a blade”

Given a unit pseudoscalar $I_n$ of the space, define dualization:

$$
A^\ast = A\!\rfloor\! I_n^{-1}.
$$



This maps a $k$-blade to an $(n-k)$-blade and represents the **orthogonal complement** subspace with a consistent orientation convention.

Double dual gives a dimension-dependent sign (pattern $++--++--\dots$ over $n$).  
To “undo” dualization without worrying about that sign, define undualization:

$$
A^{-\ast} \equiv A\!\rfloor\! I_n.
$$



### 6.4 Dual representation of a subspace

Chapter 2 gave **direct representation**: $x\in A \iff x\wedge A=0$.  
With duality, you also get:

- Let $D = A^\ast$. Then

  $$
  x\in A \iff x\!\rfloor\! D = 0.
  $$



This generalizes the “normal-vector equation” $n\cdot x=0$ to arbitrary dimensions and grades — and it does it inside the same algebra.

---

## 7. Orthogonal Projection of Subspaces

With contraction + inverse, projection becomes a one-line formula.

### 7.1 Vector projection onto a blade

For a vector $x$ and a blade $B$ with inverse $B^{-1}$, define:

$$
P_B[x] \equiv (x\!\rfloor\! B)\!\rfloor\! B^{-1}.
$$



Geometric intuition in 3D:
- $x\!\rfloor\!B$ gives a vector **in the plane of $B$** perpendicular to $x$.
- Contract again by $B^{-1}$ acts like “dual inside the $B$-plane”, rotating that perpendicular vector into the actual projection direction.

The mapping is linear in $x$, depends only on the *attitude* of $B$ (weight/orientation cancel out), and is idempotent: $P_B[P_B[x]]=P_B[x]$.

### 7.2 Projecting a blade

Same idea works for a general blade $X$:

$$
P_B[X] \equiv (X\!\rfloor\! B)\!\rfloor\! B^{-1}.
$$



The book also recommends an equivalent form that makes it obvious the result lies in $B$:

$$
P_B[X] = (X\!\rfloor\! B^{-1})\!\rfloor\! B.
$$



---

## 8. The 3D Cross Product: Included, then (politely) Fired

The cross product is a 3D convenience. It’s not a fundamental geometric object; it’s a **dualized bivector**.

In Euclidean $\mathbb{R}^3$,

$$
a\times b = (a\wedge b)^\ast = (a\wedge b)\!\rfloor\! I_3^{-1}.
$$



So “cross product” really means:
1) span the plane with $a\wedge b$, then  
2) take its orthogonal complement via duality.

That’s why it:
- depends on the ambient metric,
- has awkward transformation laws under general linear maps,
- doesn’t generalize cleanly beyond 3D.

The chapter walks through the standard cross-product use cases and replaces them:

- **Normals:** represent the plane directly as $a\wedge b$ instead of its normal vector.  
- **Rotational velocity:** rewrite

  $$
  a\times x = (a\wedge x)^\ast = x\!\rfloor\!A,
  $$

  where $A$ is the dual plane of the axis vector $a$. This generalizes to any dimension (rotations are planes, not axes).  
- **Plane intersections:** the “trick” $a\times b$ becomes a contraction expression that later generalizes to the meet operation.

Bottom line: keep $a\wedge b$ and contractions; only dualize to a vector if you absolutely must interface with legacy 3D vector formulas.

---

## 9. Application: Reciprocal Frames (Non-Orthonormal Coordinates Done Right)

If $\{b_i\}_{i=1}^n$ is any basis (not necessarily orthonormal), you still want a simple way to recover coordinates of a vector $x$ from dot products.

Define the pseudoscalar of the basis:

$$
I_n = b_1\wedge\cdots\wedge b_n,
$$

and define the **reciprocal basis vectors** $\{b^i\}$ by:

$$
b^i \equiv (-1)^{i-1}\,(b_1\wedge\cdots\wedge \widehat{b_i}\wedge\cdots\wedge b_n)\!\rfloor\! I_n^{-1}.
$$



They satisfy the killer property:

$$
b_i\cdot b^j = \delta_i^j.
$$



So if

$$
x = \sum_i x^i b_i,
$$

then the coordinates are still given by a dot product:

$$
x^i = x\cdot b^i.
$$



This is standard linear algebra in disguise — but geometric algebra packages it into a clean geometric construction: each $b^i$ is (up to sign) the dual of the span of “all basis vectors except $b_i$”.

---

## 10. Programmer’s Takeaways (because you’ll implement this)

This chapter isn’t just theory; it’s setting up computational primitives.

- **Orthonormalization idea:** build blades with wedges, then “remove” components with contractions to get orthogonal vectors (a contraction-based Gram–Schmidt style).  
- **Cross product implementation:** compute $(a\wedge b)^\ast$ using dualization (requires pseudoscalar $I_3$ or its inverse).  
- **Reciprocal frames in code:** compute pseudoscalar $I$, invert it, and contract the “all-but-one” wedge products with $I^{-1}$.  
- **Color space conversion:** reciprocal frames aren’t abstract — they’re a practical way to project measurements (RGB samples) onto a non-orthonormal frame.

---

## 11. Operations Reference

Here’s the compact “mental API” you should carry forward.

| Operation | Formula | What it means |
|---|---|---|
| Scalar product | $A\ast B=\det[a_i\cdot b_j]$ | metric measurement + alignment (same grade only) |
| Blade norm | $\|A\|^2 = A\ast\tilde A$ | squared length/area/volume |
| Angle | $\cos\theta=\dfrac{A\ast\tilde B}{\|A\|\|B\|}$ | relative attitude (same grade) |
| Left contraction | $A\!\rfloor\!B$ | grade-reducing inner product; “part of $B$ perpendicular to $A$” |
| Dual | $A^\ast = A\!\rfloor\!I_n^{-1}$ | orthogonal complement as a blade |
| Projection | $P_B[X]=(X\!\rfloor\!B)\!\rfloor\!B^{-1}$ | orthogonal projection of a blade onto a subspace |
| Reciprocal basis | $b^i = (-1)^{i-1}(\widehat{b_i})\!\rfloor\!I_n^{-1}$ | compute coordinates via $x^i=x\cdot b^i$ |

Everything else in the chapter is basically a consequence of these.

---

## 12. Summary

Chapter 2 made subspaces computable via the outer product. Chapter 3 makes them **measurable**:

1. **Scalar product** extends the dot product to blades of equal grade, giving norms and angles.  
2. The interaction between scalar product and outer product forces a mixed-grade inner product: the **contraction**, which becomes the real workhorse.  
3. Contraction naturally produces **orthogonal complements** and **dual representations** via pseudoscalars.  
4. With inverses, you get clean formulas for **projection** and **reciprocal frames**.  
5. The 3D cross product is revealed as “dual of a bivector”, and you’re given better, dimension-independent replacements.  

If Chapter 2 was “subspaces exist”, Chapter 3 is “subspaces have metric relationships — and we can compute them without crawling back to coordinates.”
