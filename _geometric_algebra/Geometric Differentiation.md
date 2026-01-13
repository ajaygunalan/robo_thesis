# Chapter 8 — Geometric Differentiation

Classical calculus is built for **numbers** (and later, for **vectors**). Geometry, unfortunately, doesn’t just “change by adding a little bit.” A line should stay a line, a plane should stay a plane, and a rotated object should stay the *same kind* of object.

Geometric algebra forces you to respect that. Differentiation here is not just “take a limit”—it’s **compute with infinitesimal geometric change without destroying geometric meaning**.

This chapter is a detour (the book says you can skip it on a first pass), but it’s the detour that matters if you care about:

- **geometric optimization** (estimating rotors from noisy data),
- **differential geometry** (curvature, local motion),
- and “vector calculus”-style operators (gradient/divergence/curl) without coordinate worship.

**What we’ll build:** a calculus where we can differentiate not only with respect to a scalar or a vector, but with respect to **general multivectors and blades**, and where the main algebraic workhorse is a geometric cousin of the Lie bracket: the **commutator product**.

---

## 1. Two kinds of geometric change

The chapter splits “change” into two very different mechanisms.

### A) Transformational change (move the thing)
An element $X$ changes because you **transform it**—rotate, reflect, etc.

In geometric algebra, orthogonal transformations are done by **versors**; smooth continuous ones are done by **rotors**. The basic action is

$$
X \mapsto R X R^{-1}.
$$

This is the right kind of change for geometry: it preserves grade and structure.

### B) Parametric change (change what it depends on)
An element $F$ changes because it depends on parameters: time $\tau$, position $x$, or even other geometric objects (like a mirror normal $n$ inside the expression $nXn^{-1}$).

This is the domain of derivatives like:

- scalar derivative $\partial_\tau$,
- directional derivative $(a * \partial_x)$,
- vector derivative $\partial_x$ (the geometric $\nabla$),
- multivector derivative $\partial_X$.

### The big warning
You *cannot* casually do “$X + \delta X$” for blades the way you do for scalars. A generic additive perturbation of a blade may stop being a blade.

So the book takes a hard line:

> **Elements of geometric algebra should only be perturbed by rotors.**

That single sentence is the spine of the chapter.

---

## 2. Rotor calculus: the commutator product shows up everywhere

A rotor in the spaces the book cares about can be written as an exponential of a bivector:

$$
R = e^{-B/2}.
$$

Expanding the sandwich product as a series gives

$$
e^{-B/2} X e^{B/2} = X + \tfrac12(XB - BX) + \cdots
$$

That first-order term is so important it gets its own name.

### 2.1 The commutator product
Define (for general multivectors $X, B$)

$$
X \times B \;\;\equiv\;\; \tfrac12(XB - BX).
$$

- Bilinear, distributive.
- **Not associative**, but it satisfies the **Jacobi identity**:

$$
(A\times B)\times C + (C\times A)\times B + (B\times C)\times A = 0.
$$

### 2.2 Why the commutator is geometrically “correct”
When the second argument is a **bivector** ($\mathrm{grade}(B)=2$), the commutator is **grade-preserving**:

$$
\mathrm{grade}(X \times B) = \mathrm{grade}(X).
$$

That’s exactly what you need for rotor Taylor series: every term in the perturbation of $X$ stays the same grade as $X$.

### 2.3 Rotor Taylor series in commutator form
With this notation, the rotor action expands cleanly:

$$
e^{-B/2} X e^{B/2}
= X + (X\times B) + \tfrac12((X\times B)\times B) + \tfrac1{3!}(((X\times B)\times B)\times B)+\cdots
$$

This is “Lie algebra calculus” written in geometric algebra clothing.

---

## 3. Small changes and the “only rotors” rule

If the rotor is near the identity, write it as $e^{-\delta B/2}$ with $\delta \approx 0$. Then

$$
e^{-\delta B/2} X e^{\delta B/2}
= X + X\times (\delta B) + O(\delta^2).
$$

So the **allowed** first-order perturbations of $X$ are exactly commutators with a small bivector.

### A sanity check: vectors
For a vector $x$, an orthogonal perturbation must preserve $\|x\|$. That forces the change $\delta x$ to be perpendicular to $x$, i.e. $x\cdot\delta x = 0$.

In GA, that condition is automatically enforced by writing

$$
\delta x = x \times \delta B,
$$

because commutating with a bivector produces the right “infinitesimal rotation” behavior.

### What about translations?
A raw vector $x$ represents a **direction**, not a **point**. Translating it doesn’t make geometric sense in this model—so the rotor-only restriction forbids it.

That’s not a geometric limitation; it’s a representation issue. Later chapters build models where **translations are versor operations too** (e.g., homogeneous / conformal models), so “rotor-only perturbations” remains compatible with real Euclidean motion.

---

## 4. Combining changes: where Lie algebra sneaks in

### 4.1 Two small rotor changes
Do two small changes successively: $e^{-\delta_1 A/2}$ and $e^{-\delta_2 B/2}$.

- To **first order**, the effects add: $\delta_1 A + \delta_2 B$.
- At **second order**, noncommutativity matters.

If you do the two changes and undo them in the opposite order, the net effect is (to the first nontrivial order)

$$
X \mapsto X + X \times (\delta_1 A \times \delta_2 B) + O(\delta^3).
$$

So the commutator of two motions produces a *new* motion—exactly the hallmark of Lie algebras.

### 4.2 Example: rotations in 3D
Let

- $A = e_1\wedge e_2$ (rotation in the $e_1e_2$ plane),
- $B = e_2\wedge e_3$ (rotation in the $e_2e_3$ plane).

Then the commutator gives a third bivector:

$$
A\times B = -\,e_3\wedge e_1.
$$

Translation: two “basic” rotations can generate the third.

### 4.3 Why translations behave differently
Translations commute. Their commutator is zero. So you can’t “manufacture” a missing translation direction by commutating the ones you have. (This shows up later once translations are represented as bivectors in the right model.)

---

## 5. Propagating perturbations through other transformations

### 5.1 Transforming a perturbed object
If $X$ is perturbed by a small rotor with bivector $\delta A$, and then you apply a versor $V$,

$$
X \mapsto VXV^{-1},
$$

then the perturbation bivector transforms cleanly:

$$
\delta A \mapsto V\,\delta A\,V^{-1}.
$$

This part is exact (no approximation needed).

### 5.2 Perturbing the *transformation* itself
Now the subtle case: the versor $V$ is uncertain, not $X$.

If

$$
V \mapsto e^{-\delta A/2} V e^{\delta A/2},
$$

then (to first order) the induced perturbation on the transformed result is still a rotor perturbation, but with an **effective** bivector

$$
\delta B = \delta A - V\,\delta A\,V^{-1}.
$$

This is a *local* first-order statement: it’s good for “small uncertainty,” not for finite changes.

---

## 6. Parametric differentiation: scalar → directional → vector → multivector

The second half of the chapter is a construction ladder: start with ordinary derivatives and climb to fully geometric derivatives.

### Cheat sheet: the four derivative operators

| Operator | Acts on $F$ that depends on… | Output “type” | Core idea |
|---|---|---|---|
| $\partial_\tau$ | scalar $\tau$ | same grade as $F$ | ordinary time derivative |
| $(a * \partial_x)$ | vector $x$ in direction $a$ | same grade as $F$ | directional rate of change |
| $\partial_x$ | vector $x$ (all directions) | multivector via geometric product | geometric $\nabla$ operator |
| $\partial_X$ | multivector $X$ | multivector via geometric product | derivative w.r.t. blades/multivectors |

The moment you move past $\partial_\tau$, **noncommutativity matters**. You cannot blindly reuse scalar-calculus pattern matching.

---

## 7. Scalar differentiation $\partial_\tau$

Defined as usual:

$$
\frac{d}{d\tau}F(\tau) = \lim_{\varepsilon\to 0}\frac{F(\tau+\varepsilon)-F(\tau)}{\varepsilon}.
$$

It commutes with everything and obeys the usual product rule.

### 7.1 Example: differentiating $x^2$ along a curve
If $x(\tau)$ is a vector curve, then

$$
\partial_\tau(x^2) = 2\,\dot x\cdot x.
$$

Nothing shocking—yet.

### 7.2 Rotor time derivative becomes a commutator
Let $X(\tau) = R(\tau)X_0R(\tau)^{-1}$, and $R(\tau)=e^{-I(\tau)/2}$. Under the assumptions used in the chapter’s worked derivation, you get

$$
\partial_\tau X = X \times \partial_\tau I.
$$

In 3D, when you dualize the bivector rate into an angular velocity vector, this collapses to the familiar

$$
\dot x = \omega \times x.
$$

Same physics, cleaner geometry.

---

## 8. Application: curvature of a planar curve (done properly)

For a planar curve $r(\tau)$, define the tangent circle by center $c$ and radius $\rho$:

$$
(c-r)^2 = \rho^2.
$$

Differentiate twice, eliminate $c$ using a geometric-algebra trick, and you get a **closed form** for the circle center:

$$
c = r - \frac{\dot r^{\,3}}{\dot r \wedge \ddot r},
\qquad\text{where }\dot r^{\,3} \equiv (\dot r\cdot \dot r)\,\dot r.
$$

Then curvature $\kappa = 1/\rho$ becomes

$$
\kappa = \frac{(\dot r \wedge \ddot r)^{*}}{\|\dot r\|^3}.
$$

Key point: only the component of $\ddot r$ **orthogonal** to $\dot r$ contributes (the tangential component is reparameterization noise).

---

## 9. Directional differentiation $(a * \partial_x)$

Directional derivative of a multivector-valued function $F(x)$:

$$
(a * \partial_x)F(x)
\equiv
\lim_{\varepsilon\to0}\frac{F(x+\varepsilon a)-F(x)}{\varepsilon}.
$$

It’s a **scalar operator**, so it commutes with everything and obeys a product rule. But the values you get depend on the geometric product structure inside $F$.

### 9.1 Example: $(a * \partial_x)(x^2)$
$$
(a * \partial_x)(x^2) = 2\,a\cdot x.
$$

### 9.2 The “surprising” one: derivative of inversion
$$
(a * \partial_x)(x^{-1}) = -x^{-1} a x^{-1}.
$$

Geometric meaning (as emphasized by Figure 8.1 in the chapter): the change is a **reflection of $a$** in the plane normal to $x$, scaled by $1/\|x\|^2$. That’s why the result is not the scalar-looking $-a/x^2$ you might expect from commutative algebra.

### 9.3 A mini reference (subset of Table 8.1)
The chapter collects many standard derivatives. A few that show the pattern:

- $(a * \partial_x) x = P[a]$
- $(a * \partial_x)(x\cdot b) = P[a]\cdot b$
- $(a * \partial_x) \|x\|^k = k(P[a]\cdot x)\,\|x\|^{k-2}$

Here $P[\cdot]$ is a projection onto the local $m$-dimensional manifold in which $x$ lives (the book is careful to allow $x$ to lie on a submanifold inside a larger space).

---

## 10. Application: tilting a mirror

Reflection in a plane through the origin with normal $n$ (not necessarily unit) is

$$
n[X] \equiv nXn^{-1}.
$$

Differentiate with respect to the normal, in direction $a$:

$$
(a * \partial_n)[nXn^{-1}]
= n[X] \times \bigl(2n^{-1}\wedge a\bigr).
$$

So: **a small change in the mirror normal produces a rotor-like change of the reflection result**.

Now relate $a$ to an actual small rotation of the mirror. If the mirror rotates by a small rotor with unit plane $I$, then the normal changes as

$$
a = n \times I.
$$

Plugging that in yields the bivector of the induced rotation of the reflected object:

$$
B = 2\,n^{-1}\wedge (n\times I).
$$

In 3D, this simplifies to a clean geometric statement (illustrated by Figure 8.2):

- The reflection rotates around the **projection** of the rotation axis onto the mirror plane.
- The reflection rotation angle is

$$
\beta = 2\sin\psi,
$$

where $\psi$ is the angle between the mirror normal and the rotation axis.

That “$2\sin\psi$” factor is the kind of result that is painful in coordinates and trivial in GA.

---

## 11. Vector differentiation $\partial_x$: the geometric $\nabla$

Define a basis $\{e_i\}_{i=1}^m$ for the manifold where $x$ lives, and assemble the directional derivatives:

$$
\partial_x \equiv \sum_{i=1}^{m} e_i (e_i * \partial_x)
= \sum_i e_i \frac{\partial}{\partial x_i}.
$$

Interpretation: this is a **vector-valued differential operator**. It keeps track of change in all directions.

### 11.1 Example: $\partial_x(x^2)$
$$
\partial_x(x^2)=2x.
$$

### 11.2 Divergence and curl fall out automatically
Because multiplication is the **geometric product**,

$$
\partial_x F = \partial_x \cdot F + \partial_x \wedge F.
$$

- $\partial_x\cdot F$ corresponds to divergence.
- $\partial_x\wedge F$ corresponds to curl (more precisely, its bivector form; the 3D cross-product curl is a dual).

### 11.3 A few anchor identities (from Table 8.1)
- $\partial_x x = m$
- $\partial_x \cdot x = m$
- $\partial_x \wedge x = 0$
- $\partial_x \|x\| = x/\|x\|$

That “$\partial_x x = m$” looks weird until you interpret it as: “there are $m$ independent coordinate directions, and each contributes 1.”

### 11.4 Product rule and chain rule are noncommutative
Unlike $\partial_\tau$, $\partial_x$ does **not** commute with everything. The chapter introduces a bookkeeping notation (accents) to say which factor the derivative applies to.

The chain rule also needs the **adjoint** of the wrapping function $y(x)$. The punchline is:

> wrapping the argument by $y(x)$ wraps the derivative by the **adjoint** of $y$.

---

## 12. Multivector differentiation $\partial_X$

Directional multivector derivative:

$$
(A * \partial_X)F(X)
=
\lim_{\varepsilon\to0}\frac{F(X+\varepsilon A)-F(X)}{\varepsilon}.
$$

Again: scalar operator, grade-matched via the scalar product.

Then the full multivector derivative is built by expanding on a basis of the multivector space:

$$
\partial_X = \sum_I e^I (e_I * \partial_X).
$$

This includes scalar and vector differentiation as special cases.

### 12.1 A few useful identities (subset of Table 8.2)
- $\partial_X \|X\|^2 = 2\tilde X$
- $\partial_X (X * A) = P[A]$
- $\partial_X (X^{-1} * A) = P[-X^{-1}AX^{-1}]$
- $\partial_X \|X\|^k = k\|X\|^{k-2}\tilde X$

($\tilde X$ is reversion; it shows up naturally because $\|X\|^2$ is built from $X\tilde X$.)

---

## 13. Application: estimating a rotor optimally (Wahba / Procrustes)

You’re given vector correspondences $(u_i, v_i)$. They’re related by a rotation, but noisy. Find the rotor $R$ that best fits.

A common squared-error cost is

$$
\Gamma(R)=\sum_{i=1}^k (v_i - Ru_i\tilde R)^2.
$$

The chapter’s trick: temporarily replace rotor $R$ by an unconstrained versor $V$ and differentiate with respect to $V$. After some algebra, the optimal rotor $R^*$ must satisfy

$$
\sum_{i=1}^k (R^*u_i\tilde R^*)\wedge v_i = 0.
$$

Interpretation: if the fit is optimal, there’s no leftover “systematic perpendicular mismatch” that a small extra twist could reduce.

Then the chapter connects this to a linear map

$$
f[x]=\sum_{i=1}^k u_i (v_i\cdot x),
$$

and shows the condition is equivalent to a symmetry property of the rotated map. In practice, you compute the optimal rotation using the **polar decomposition / SVD** of the matrix built from the data, then convert the optimal rotation matrix back into a rotor.

This is the standard Procrustes solution—but GA makes it clear what geometry is being optimized, and why SVD is merely a computational tool, not the meaning.

---

## 14. Takeaways

1. **Rotor differentiation = commutators.** If something changes by a rotor, its derivative naturally lives in the commutator algebra.
2. **Preserve structure.** If you perturb a blade in an arbitrary additive way, you can destroy what it represents.
3. **Directional derivatives are scalar operators.** They behave “calculus-like,” but their results are geometrically richer because the underlying products are noncommutative.
4. **$\partial_x$ is $\nabla$, but better behaved.** Divergence/curl/gradient are just grade parts of one operator.
5. **$\partial_X$ is where optimization lives.** Once you can differentiate w.r.t. rotors/versors, you can do serious estimation problems cleanly.

If Chapter 2 taught you how to *build* geometric objects, Chapter 8 teaches you how to make them **move**—without losing their meaning.
