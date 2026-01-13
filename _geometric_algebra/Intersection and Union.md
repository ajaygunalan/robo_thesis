# Chapter 5 — Intersection and Union of Subspaces

The outer product is great at **building** subspaces: it “adds dimensions” by spanning.  
But geometry also needs the opposite move: **given two subspaces, what do they have in common (intersection), and what is the smallest subspace containing both (union)?**

In 3D linear algebra you already know the vibe:

- Two planes through the origin usually intersect in a **line**.
- But if the planes *happen to coincide*, the “intersection” should suddenly jump to a **plane**.

That grade-switching is exactly why this chapter feels different: **intersection/union are inherently nonlinear**. A tiny perturbation of one plane can flip the answer’s grade. So geometric algebra introduces two new (blade-only) products:

- **Meet** $A \cap B$: the *intersection* subspace  
- **Join** $A \cup B$: the *union* (smallest containing) subspace

They’re incredibly useful — and algebraically a bit messy.

---

## What we’re building

By the end of the chapter, you should be comfortable with:

1. **Why** meet/join cannot be cleanly bilinear products.
2. The core **factorization picture**: “common part” vs “remainder.”
3. Practical **computational formulas**, especially “pick the join, then compute the meet.”
4. How the **sign and magnitude** of a meet can encode real geometry (like sines of angles).
5. Why meet/join are **nonmetric** even though contractions (metric-looking) appear in formulas.
6. What to watch for in code: **degeneracy, grade flip-flops, and efficiency**.

---

## 1. Why intersection is not a tidy product

### 1.1 Grade switching breaks linearity

Intersecting two 2D planes in 3D:

- “generic” case: plane ∩ plane → **line** (grade 1)
- “degenerate” case (coincident planes): plane ∩ plane → **plane** (grade 2)

No linear product can do that continuously. This is a *geometric discontinuity*, so the algebra has to accept **nonlinearity**.

### 1.2 These operations only make sense for blades

Meet/join depend on **containment** (“this subspace sits in that one”). Containment is well-defined for subspaces/blades, but not for arbitrary multivectors.

So:

- **Meet/join are defined for blades**, not general multivectors.

### 1.3 The result is not uniquely weighted

Even when the intersection subspace is clear, its **absolute scale and sign** are not.

Geometrically: you can “reshape” the blades representing the input planes without changing the planes, yet the *suggested* intersection line magnitude can change. So the meet is best thought of as:

- a **subspace attitude** (the carrier), with **relative** magnitudes/signs only becoming meaningful once you choose conventions (especially how you normalize the join).

---

## 2. The core definition: meet and join by outer factorization

Let $A$ and $B$ be blades that share a common factor (in the **outer product** sense).

### 2.1 Meet as “largest common outer divisor”

Define $M$ as the **largest blade** that divides both $A$ and $B$ via the wedge product. That is the algebraic version of “their intersection subspace.”

$$
M := A \cap B
$$

### 2.2 Factor out the meet

Write the factorization in an ordered way:

$$
A = A' \wedge M,\qquad B = M \wedge B'
\tag{5.1}
$$

- If $A$ and $B$ are disjoint (only meet at the origin), then $M$ is a **scalar** (a 0-blade).

### 2.3 Join as “smallest common outer multiple”

The **join** is the smallest blade containing both, i.e., the subspace spanned by “everything needed for $A$ and $B$ together”:

$$
J := A \cup B = A' \wedge M \wedge B'
\tag{5.2}
$$

This $J$ is the pseudoscalar of the *subspace in which the whole intersection problem lives*.

### 2.4 The unavoidable scalar ambiguity

If you rescale $M \mapsto \gamma M$, then to keep $A$ and $B$ the same you must rescale $A'$ and $B'$ accordingly — and **$J$** changes by $1/\gamma$.

So there is a built-in trade-off:

- you can push a scalar factor back and forth between meet and join.

This is not a disaster: many geometric constructions (like projection with $M$ and $M^{-1}$) are invariant under that scalar ambiguity.

---

## 3. Practical computation: how to actually get $A \cap B$ and $A \cup B$

This chapter’s main computational trick is:

> **Pick a sensible join $J$** (often obvious from the ambient geometry),  
> then compute the **meet** using contractions.

### 3.1 Grade bookkeeping (keeps you sane)

Let:

- $\mathrm{grade}(A)=a$, $\mathrm{grade}(B)=b$
- $\mathrm{grade}(M)=m$, $\mathrm{grade}(J)=j$

Then:

$$
j = a + b - m,\qquad m + j = a + b
\tag{5.4}
$$

These identities are just “dimension counting” for subspaces.

### 3.2 Extracting the “remainders” $A'$ and $B'$

Using contractions and the inverse $M^{-1}$ (assume Euclidean for now so inverses exist):

$$
B' = M^{-1}\,\rfloor\, B,\qquad A' = A \,\lfloor\, M^{-1}
\tag{5.3}
$$

(The book uses both left and right contractions; the point is: **strip out the common factor** with the right normalization.)

### 3.3 Join from meet

Once $M$ is known:

$$
J = A \cup B = A \wedge (M^{-1}\,\rfloor\, B) = (A \,\lfloor\, M^{-1}) \wedge B
\tag{5.5}
$$

### 3.4 Meet from join (the workhorse formula)

If you already know $J$, then:

$$
M = A \cap B = (B \,\rfloor\, J^{-1}) \,\rfloor\, A
\tag{5.6}
$$

This is the version you actually use most of the time: choose the join $J$ as “the pseudoscalar of the common space,” then contract twice.

### 3.5 Dual meet: intersection becomes an outer product (in the right space)

Relative to the join $J$, the **dual of the meet** factors cleanly:

$$
M \,\rfloor\, J^{-1} = (B \,\rfloor\, J^{-1}) \wedge (A \,\rfloor\, J^{-1})
\tag{5.7}
$$

This is often summarized as:

$$
(A \cap B)^{*} = B^{*} \wedge A^{*}
\tag{5.8}
$$

**Warning:** that dual $(\cdot)^*$ is not “dual in the full space,” but dual **inside the join subspace**. If you dualize against the wrong pseudoscalar, you’ll get nonsense.

---

## 4. Worked example: two planes through the origin in 3D

Take two planes (2-blades) in $\mathbb{R}^3$:

$$
A = \tfrac12 (e_1+e_2)\wedge(e_2+e_3),\qquad B = e_1\wedge e_2
$$

These planes are in general position in 3D, so their join is the 3D pseudoscalar:

$$
J = I_3 = e_1\wedge e_2\wedge e_3
$$

Then the meet is a **vector** (a line through the origin). The chapter computes:

$$
A\cap B
= -\frac{1}{\sqrt{3}}(e_1+e_2)
= -\sqrt{\frac{2}{3}}\,\frac{e_1+e_2}{\sqrt{2}}
\tag{5.9}
$$

Interpretation:

- The **direction** $(e_1+e_2)$ is the intersection line’s attitude.
- The **sign** encodes oriented incidence (right-hand rule relative to the chosen join orientation).
- The **magnitude** equals the **sine of the smallest angle** between the planes (once join is normalized), here $\sin(\theta)= -\sqrt{2/3}$.

### Connection to the classical cross product

In 3D, plane bivectors dualize to normal vectors, and the meet recovers the usual “cross the normals” construction as a special case.

---

## 5. “Mostly linear”: what breaks, and how to detect it

Once you’ve fixed a join $J$, formula (5.6) shows the meet is **linear in $A$ and $B$** (it’s built from contractions).

So meet/join are “piecewise linear”:

- **Linear as long as the join does not change.**
- **Nonlinear at degeneracies** where the correct join changes grade.

### The practical diagnostic

If your chosen join is wrong for the current configuration, the computed meet typically collapses to **0**, which is your signal:

> “We crossed into a different geometric regime. Pick a different join.”

### Example: line meets plane at the origin

In 3D, let:

- $a$ be a line (vector),
- $B$ be a plane (bivector).

If the line is **not contained** in the plane, you can take $J = I_3$. Then the meet is a **scalar** (a point at the origin) whose sign tells you whether the line pierces the oriented plane “from above” or “from below.”

When the line becomes **contained** in the plane, that scalar meet goes to **0** — correctly warning you that the join should drop to the plane’s pseudoscalar $I_2$. Then the meet becomes the line itself (up to scale).

---

## 6. Quantitative meaning: meet magnitude is a sine (distance between subspaces)

If you normalize the join $J$, the meet $M=A\cap B$ becomes a meaningful quantitative object:

- $|M|$ is proportional to a **sine of a relative angle** between the subspaces.

This is a standard “distance between subspaces” idea from numerical linear algebra:

- $=1$ when “as orthogonal as possible”
- smoothly decays to $0$ as subspaces become more parallel.

### Order matters: symmetric vs antisymmetric meets

Swapping arguments can flip the sign. The chapter derives:

$$
B\cap A = (-1)^{(j-a)(j-b)}\, (A\cap B)
$$

So:

- Two **lines in a plane** ($a=b=1,\ j=2$) meet **antisymmetrically**: $A\cap B = -(B\cap A)$  
  (makes sense: $\sin(\theta)$ changes sign when you reverse the angle).
- A **line and a plane in 3D** ($a=1,\ b=2,\ j=3$) meet **symmetrically**: $A\cap B = B\cap A$.

The full sign behavior across common geometric situations is summarized in the chapter’s Table 5.1.

---

## 7. Meet/join under linear transformations

Even though meet/join are not bilinear, they behave beautifully under **invertible linear maps** $f$:

$$
f[A\cup B] = f[A]\cup f[B],\qquad
f[A\cap B] = f[A]\cap f[B]
$$

Why? Because the defining relationships are built from **outer product factorization**, and $f$ acts as an outermorphism, preserving wedges.

### Subtle but important: dualize relative to the transformed join

If you compute meets via the contraction formula, you must use the **transformed join** $f[J]$, not the old one:

$$
f[A\cap B] = f[B]\,\rfloor\, f[J]^{-1} \,\rfloor\, f[A]
$$

This makes explicit that meet/join are fundamentally **nonmetric** objects, even if contractions make them look metric at first glance.

---

## 8. Offset subspaces: postponed (but that’s where the magic explodes)

So far, everything is “through the origin.” The chapter flags what’s coming:

- In the **homogeneous model** (later), you can meet **parallel** lines at a finite point and meet **skew** lines in a scalar proportional to their distance.
- In the **conformal model**, the same meet machinery intersects **spheres, circles, lines, planes**, etc., using essentially the same algebra.

---

## 9. Programming reality check

Meet/join are powerful — and expensive.

- Implementations often use a **factorization algorithm** (not just coordinate-level multiplication like the wedge).
- In Gaigen-style code, join can be **~100× slower** than the outer product in benchmarks.
- Near degeneracies (nearly parallel elements), the algorithm must decide the output grade using thresholds, so results can **flip-flop** between grades due to floating point issues.

**Rule of thumb:**  
If you know the configuration (i.e., you already know an appropriate join), prefer direct formulas like $M = (B\rfloor J^{-1})\rfloor A$ instead of calling a general-purpose meet/join routine.

---

## 10. Summary

- Meet/join are **incidence products**: they encode intersection and union of subspaces.
- They are **not bilinear** because geometry forces grade switches at degeneracies.
- They are defined for **blades**, not arbitrary multivectors.
- Core structure: factorization $A=A'\wedge M,\ B=M\wedge B'$, with $M=A\cap B$ and $J=A\cup B$.
- In practice: **choose a join** (often the ambient pseudoscalar), then compute meet via contractions.
- With join normalized, meet magnitude becomes a **sine-like angle measure** between subspaces.
- Meet/join are **nonmetric**, and transform cleanly under invertible linear maps.
- In code, beware: **cost** and **numerical degeneracy**.

