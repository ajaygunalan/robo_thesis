# 5 Intersection and Union of Subspaces

Geometric algebra contains operations to determine the union and intersection of subspaces, the **join** and **meet** products.

These products are of course important in geometry, and it is therefore disappointing to learn that they are not very tidy algebraically. In particular, they are not (bi-)linear: a small disturbance in their arguments may lead to major changes in their outcome as geometric degeneracies occur. This will give their treatment a different flavor than the products we introduced so far.

But meet and join are still very useful. Even when applied to the subspaces at the origin, meet and join generalize some specific formulas from 3-D linear algebra into a more unified framework and extend them to subspaces intersecting in n-dimensional space. Their full power will be unleashed later, in Part II, when we can use them to intersect offset subspaces and even spheres, circles, and the like. Yet it is good to understand their algebraic structure first, and we now have all the tools to do so.

---

## 5.1 The Phenomenology of Intersection

When we intersect two planes through the origin in 3-D, the outcome is usually a line. In terms of subspaces as blades, two grade-2 elements produce a grade-1 element.

However, if the two planes happen to coincide, we would want the geometric outcome of their intersection to be that plane of coincidence, which is of grade 2. None of the products we have seen so far can do this grade switching in the result as a consequence of the geometric relationship of their arguments, so there must be something new going on algebraically. In fact, an incidence product encoding this geometry cannot be linear, since even a small disturbance of one of the input planes can lead to this discontinuity in the result.

That nonlinearity prohibits extending the intersection and union easily from blades (which represent subspaces) to general multivectors (which do not). That we cannot do this makes sense for geometrical reasons as well, because any definition of geometrical union and intersection should be based on containment of the result in the arguments, or vice versa, and this is only well defined for subspaces. Algebraically, we will therefore have to *limit intersection and union to blades*. These are the first products that must be constrained to operate within the limited algebra of subspaces, not in the full Grassmann algebra of multivectors.

But even then, an algebraic problem that we can foresee geometrically is that the desired outcome does not have all the properties of a blade, because it is not meaningful to assign a unique magnitude and orientation (i.e., a sign) to the blade representing the subspace of intersection. This is illustrated in Figure 5.1(a) and (b) for two planes represented by 2-blades. Since those 2-blades may be reshaped without changing their value as blades, both depictions are permitted—but they each suggest a different intersection magnitude. It is equally easy to change the orientation of the possible intersection line. Therefore, the outcome of the intersection of two blades is a subspace, but one of which only the attitude matters.

> **Figure 5.1:** The ambiguity of the magnitude of the intersection of two planes, **A** and **B**. Both figures are acceptable solutions to the problem of finding blades representing the union **J** and intersection **M** of the subspaces represented by the same 2-blades **A** and **B**.

We are going to design two products between blades to compute with intersections. They will be called **meet** and **join**, and denoted by ∩ and ∪ to signify that they are meant to represent the geometric intersection and union of two blades. The setlike notation will not be confusing (we hardly use sets in this book), and in fact is a helpful reminder that the resulting elements are not fully quantified blades and that the products are nonlinear.¹

---

## 5.2 Intersection Through Outer Factorization

Consider two blades **A** and **B**, which happen to contain some common blade. To be precise, let **M** be the largest common divisor of **A** and **B** in the sense of the outer product. This is the algebraic formalization of their geometric intersection; we will call it their **meet** and denote it by **A** ∩ **B**.

Algebraically, we should be able to factor out **M** from both **A** and **B**, since it is contained in both. We do this in a particular order, writing

$$\mathbf{A} = \mathbf{A}' \wedge \mathbf{M} \quad \text{and} \quad \mathbf{B} = \mathbf{M} \wedge \mathbf{B}'$$
**(5.1)**

If **A** and **B** are disjoint, then **M** is a scalar (a 0-blade).

**A'** and **B'** together reside within a blade **J**, their smallest common multiple in terms of the outer product. This is a pseudoscalar of the subspace in which this meet intersection problem actually resides. We will call it their **join** and denote it by **A** ∪ **B**, for it is the geometric union of the subspaces. It is clear that join and meet are related through the factorization, for we can write

$$\mathbf{A} \cup \mathbf{B} = \mathbf{A}' \wedge \mathbf{M} \wedge \mathbf{B}' \quad \text{and} \quad \mathbf{A} \cap \mathbf{B} = \mathbf{M}$$
**(5.2)**

We already observed, when we discussed the geometry of Figure 5.1, that we should expect this factorization by **M** not to be unique. Indeed, in (5.1) we may multiply **M** by a scalar γ. Then **A'** must be multiplied by 1/γ to preserve **A**, and similar for **B'**. As a consequence, this would multiply the join result of (5.2) by 1/γ. So we can always trade off a scalar factor between the meet and the join, of any weight or sign. This ambiguity need not be a problem in geometrical usage of the outcome. For instance, a projection of a vector **x** to the meet subspace **M** is given by (**x**⌋**M**⁻¹)**M**, and this is invariant to the scalar ambiguity since it involves both **M** and **M**⁻¹.

The first use of meet and join in nonmetric projective geometry seems to have induced people to neglect the magnitude and sign completely. Yet this is a pity, for there are situations in which consistent use of relative magnitudes conveys useful geometric information (for instance, on the sines of intersection angles). To enable this, we will develop consistent formulas for meet and join based on the same factorization. We can then guarantee that meet and join of the same subspaces can be used consistently, and we will demonstrate how that can be applied. Of course you can always ignore this quantitative precision in any application where you do not need it—in that case, the order of the factors in (5.1) and (5.2) can be chosen arbitrarily.

---

## 5.3 Relationships Between Meet and Join

For practical use, we have to make the computational relationships between meet and join more explicit than merely relating them through their factorization. To do so, we first need formulas for **A'** and **B'**. Neither contain any factors also in **M**, so we can use the contraction to define them as the part of **A** not in **M** and the part of **B** not in **M**. But to be quantitative, we have to be careful about the order of the arguments and about their normalization:

$$\mathbf{B}' = \mathbf{M}^{-1} \rfloor \mathbf{B}, \quad \text{and} \quad \mathbf{A}' = \mathbf{A} \lfloor \mathbf{M}^{-1}$$
**(5.3)**

where we employed both contractions for simplicity of expression. If you are uncomfortable with using the contractions in this direct manner, you may derive the former more formally from the identity **B'** = **M**⁻¹⌋(**M** ∧ **B'**), which holds since a basis for **B'** can be chosen that is orthogonal to all of the factors of **M**⁻¹ and hence of **M**. The expression for **A'** can be derived in a similar manner. This shows why we need to use the inverse of **M** to achieve proper normalization.

But this means we can only proceed if **M** has an inverse. This may seem to restrict the kind of spaces in which we can do intersections, excluding those with null vectors, and that would be a serious limitation in practice. However, we will lift that apparent restriction in Section 5.7 (when we show that both join and meet are independent of the particular metric, as you may already suspect, since after all they are based on factorization by the nonmetric outer product). For now, assume that all blades are in the algebra of a Euclidean vector space.

Denoting the grades of the elements by the corresponding lowercase letters (where *j* is the grade of the join **J**), we have various simple relationships between them

$$a' = a - m, \quad b' = b - m, \quad j = a + b - m, \quad m + j = a + b$$
**(5.4)**

and these help in keeping track of the various quantitative relationships we are going to derive. Together with consideration of order and normalization, all can then be remembered easily.

With (5.3), the join in terms of the meet can be written in two ways:

$$\mathbf{J} = \mathbf{A} \cup \mathbf{B} = \mathbf{A} \wedge (\mathbf{M}^{-1} \rfloor \mathbf{B}) = (\mathbf{A} \lfloor \mathbf{M}^{-1}) \wedge \mathbf{B}$$
**(5.5)**

We can also solve for the meet in terms of the join. We first establish

$$1 = \mathbf{J} * \mathbf{J}^{-1} = (\mathbf{A} \wedge (\mathbf{M}^{-1} \rfloor \mathbf{B})) * \mathbf{J}^{-1} = \mathbf{A} * ((\mathbf{M}^{-1} \rfloor \mathbf{B}) \lfloor \mathbf{J}^{-1})$$

$$= (\mathbf{A}' \wedge \mathbf{M}) * (\mathbf{M}^{-1} \wedge (\mathbf{B} \lfloor \mathbf{J}^{-1})) = \mathbf{A}' * (\mathbf{B} \lfloor \mathbf{J}^{-1})$$

Then

$$1 = (\mathbf{B} \lfloor \mathbf{J}^{-1}) * (\mathbf{A} \lfloor \mathbf{M}^{-1}) = (\mathbf{M}^{-1} \wedge (\mathbf{B} \lfloor \mathbf{J}^{-1})) * \mathbf{A} = (\mathbf{M}^{-1} \wedge (\mathbf{B} \lfloor \mathbf{J}^{-1})) \rfloor \mathbf{A}$$

Now

$$\mathbf{M} = \mathbf{M} \wedge 1 = \mathbf{M} \wedge ((\mathbf{M}^{-1} \wedge (\mathbf{B} \lfloor \mathbf{J}^{-1})) \rfloor \mathbf{A}) = (\mathbf{M}(\mathbf{M}^{-1} \wedge (\mathbf{B} \lfloor \mathbf{J}^{-1}))) \rfloor \mathbf{A} = (\mathbf{B} \lfloor \mathbf{J}^{-1}) \rfloor \mathbf{A}$$

so that we obtain:

$$\mathbf{M} = \mathbf{A} \cap \mathbf{B} = (\mathbf{B} \lfloor \mathbf{J}^{-1}) \rfloor \mathbf{A}$$
**(5.6)**

This formula to compute **M** from **J** (given **A** and **B**) is often used in applications, since when subspaces **A** and **B** are in general position it is easy to specify a blade **J** for their join.

The dual of this relationship shows the structure of the meet more clearly: taking the inner product with **J**⁻¹ on both sides of (5.6), we obtain **M**⌋**J**⁻¹ = ((**B**⌊**J**⁻¹)⌋**A**)⌋**J**⁻¹ = (**B**⌊**J**⁻¹) ∧ (**A**⌊**J**⁻¹). So relative to the join, the dual meet is the outer product of the duals:

$$\mathbf{M} \lfloor \mathbf{J}^{-1} = (\mathbf{B} \lfloor \mathbf{J}^{-1}) \wedge (\mathbf{A} \lfloor \mathbf{J}^{-1})$$
**(5.7)**

This is often compactly denoted as

**dual meet:** $(\mathbf{A} \cap \mathbf{B})^* = \mathbf{B}^* \wedge \mathbf{A}^*$
**(5.8)**

but then you have to remember that this is not the dual relative to the pseudoscalar **I**ₙ of the total space, but only of the pseudoscalar of the subspace within which the intersection problem resides (i.e., of the join **J** = **A** ∪ **B**).

Some more expressions relating the four quantities **A**, **B**, **M**, and **J** are given in the structural exercises. It should be noted that such relationships between meet and join do not give us a formula or algorithm to compute either. In higher-dimensional subspaces, the search for a join of arbitrary blades requires care, for it can easily lead to an exponential algorithm. An O(n) algorithm will be given in Section 21.7, but we cannot explain that at this point since it uses the geometric product of Chapter 6.

---

## 5.4 Using Meet and Join

In practice, the join is often more easily determined than the meet, since the most interesting intersections and unions of subspaces tend to occur when they are in general position within some subspace with a known pseudoscalar (two planes in space, a line and a plane in space, etc.). Then the join is just the pseudoscalar of that common subspace, and (5.6) gives the meet. A numerical example conveys this most directly.

We intersect two planes represented by the 2-blades **A** = ½(**e**₁ + **e**₂) ∧ (**e**₂ + **e**₃) and **B** = **e**₁ ∧ **e**₂. Note that we have normalized them to facilitate interpreting the relative quantitative aspects. These are homogeneous planes in general position in 3-D space, so their join is proportional to **I**₃ ≡ **e**₁ ∧ **e**₂ ∧ **e**₃. It makes sense to orient **J** with **I**₃ so that we simply take **J** = **I**₃. This gives for the meet:

$$\mathbf{A} \cap \mathbf{B} = \frac{1}{\sqrt{3}} \left( (\mathbf{e}_1 \wedge \mathbf{e}_2) \lfloor (\mathbf{e}_3 \wedge \mathbf{e}_2 \wedge \mathbf{e}_1) \right) \rfloor \left( (\mathbf{e}_1 + \mathbf{e}_2) \wedge (\mathbf{e}_2 + \mathbf{e}_3) \right)$$

$$= \frac{1}{\sqrt{3}} \mathbf{e}_3 \rfloor \left( (\mathbf{e}_1 + \mathbf{e}_2) \wedge (\mathbf{e}_2 + \mathbf{e}_3) \right)$$

$$= -\frac{1}{\sqrt{3}} (\mathbf{e}_1 + \mathbf{e}_2) = -\sqrt{\frac{2}{3}} \left( \frac{\mathbf{e}_1 + \mathbf{e}_2}{\sqrt{2}} \right)$$
**(5.9)**

(the last step expresses the result in normalized form). Figure 5.2 shows the answer; the sign of **A** ∩ **B** is the right-hand rule applied to the turn required to make **A** coincide with **B**, in the correct orientation. We will show that the magnitude of the meet equals the sine of the smallest angle between them, so that in this example their angle is asin(−√(2/3)), measured from **A** to **B**.

> **Figure 5.2:** The meet of two oriented planes.

Classically, one would compute the intersection of two homogeneous planes in 3-space by first converting them to normal vectors and then taking the cross product. We can see that this gives the same answer in this nondegenerate case in 3-space, using the definition of the cross product (3.28) and our duality equations (3.20), (3.21), and remembering that the dual 2-blades are vectors:

$$\mathbf{A}^* \times \mathbf{B}^* = (\mathbf{A}^* \wedge \mathbf{B}^*)^* = -(\mathbf{B}^* \wedge \mathbf{A}^*)^* = (\mathbf{B}^* \wedge \mathbf{A}^*)^{-*} = \mathbf{B}^* \rfloor \mathbf{A} = \mathbf{A} \cap \mathbf{B}$$
**(5.10)**

So the classical result is a special case of (5.6) or (5.8). But formulas (5.6) and (5.8) are much more general: they apply to the intersection of subspaces of *any* grade, within a space of *any* dimension.

---

## 5.5 Join and Meet Are Mostly Linear

Once the join has been selected, the formula of (5.6) for the meet shows that the meet is linear in **A** and **B** since it can be expressed by contraction products, which are clearly linear. If we change **A** and/or **B** such that the join does not change, this remains true. In this sense, the meet is **mostly linear**. However, as soon as some degeneracy occurs or is resolved, the join changes in a nonlinear manner and the meet formula enters a new domain (within which it is again linear). You can tell that this happens when the meet with your selected join returns zero. That signals degeneracy and the need to pick another join.

As a geometric example, assume that in 3-D we have a homogeneous line **a** (a vector) and a homogeneous plane **B** (a 2-blade), as in Figure 5.3. As long as the line is not contained in the plane (so that they are in general position), the pseudoscalar **I**₃ can be used as the join **J**, and the meet varies nicely with both arguments.

$$\mathbf{M} = \mathbf{a} \cap \mathbf{B} = (\mathbf{B} \lfloor \mathbf{I}_3^{-1}) \rfloor \mathbf{a} = \mathbf{B}^* \cdot \mathbf{a} = \mathbf{b} \cdot \mathbf{a}$$

This is a scalar, geometrically denoting the common point at the origin, with a magnitude proportional to the cosine of angle between the line **a** and the normal vector **b** ≡ **B**⌊**I**₃⁻¹ of the plane; that is, proportional to the sine of the angle of line and plane (and weighted by their magnitudes). It changes sign as the line enters the plane from below rather than above, with above and below determined by the orientation of the plane **B** relative to the pseudoscalar chosen for the join (i.e., the orientation of the common space). This shows the use of the sign of the meet; it gives the sense of intersection and allows us to eliminate surface intersections of rays coming from inside an object (if we orient its boundary properly and consistently). It also shows why the sign of a scalar (i.e., the orientation of a point at the origin) can be important in the algebra of subspaces.

> **Figure 5.3:** A line meeting a plane in the origin in a point. If the join is taken to be the right-handed pseudoscalar, the intersection point is positive when the line pierces the oriented plane as shown. Other normal coordinates can be chosen to bear this out: Let **B** = **e**₁ ∧ **e**₂, **a** = a₁**e**₁ + a₂**e**₂ + a₃**e**₃, then with **J** = **e**₁ ∧ **e**₂ ∧ **e**₃ you find **M** = **a** ∩ **B** = **B**\*⌋**a** = a₃ = ‖**a**‖ sin φ, which is positive in the situation shown.

Precisely when the line becomes coincident with the plane, this expression for the meet becomes zero. This is the signal that it is actually no longer the proper meet, for the join must be changed to a normalized version **I**₂ of the plane **B**, which is now the smallest common subspace. The problem has essentially become 2-D. We then find that the meet is the line **a**, weighted:

$$\mathbf{M} = (\mathbf{B} \lfloor \mathbf{I}_2^{-1}) \rfloor \mathbf{a} = \beta \mathbf{a}$$

with β ≡ **B**⌊**I**₂⁻¹ the signed magnitude of the **B**-plane. This expression is also linear in both arguments **a** and **B**, as long as we vary them so that the join does not change (so we may only rotate and scale the line within the plane **I**₂, and only change weight or orientation of the plane **B**, not its attitude).

This example generalizes to k-spaces in n-dimensional space: the meet is linear as long as the join does not change, and it degrades gracefully to zero to denote that such a change of join becomes necessary.

---

## 5.6 Quantitative Properties of the Meet

If you normalize the join, you can interpret the value of the meet as proportional to the sine between **A** and its projection on **B** (or vice versa, depending on the relative grades). We encountered a particular instance of this in the example of Figure 5.2.

We can see that this holds in general, as follows. Focus on **A** relative to the space **B**. The join should be proportional to the blade **J** = **A** ∧ **B**. Let the pseudoscalar of this space be **I**, then normalizing the join to **I** implies division of **J** by the scalar **J**⌊**I**⁻¹ = **J**\*. This rescaling of the join implies that the meet should be rescaled to become **M** **J**\*, so proportional to the scalar **J**\*. Now inspect **J**\* = (**A** ∧ **B**)\*. This is proportional to the volume spanned by **A** and **B**—and we know from the previous chapters that the magnitude of a spanned volume involves the sine of the relative angle between the arguments. Alternatively, we can rewrite **J**\* = **A**⌊(**B**\*) = **A** \* **B**\*. This scalar product is proportional to the cosine of the angle between **A** and the orthogonal complement of **B**. That can be converted to the sine of the complementary angle, retrieving the same interpretation:

> **The magnitude of the meet A ∩ B of normalized blades A and B within a normalized join denotes the sine of the angle from A to B.**

The sine measure is quite natural as an indication of the relative attitudes of homogeneous spaces. In classical numerical analysis, the absolute value of the sine of the angle between subspaces is a well-known measure for the distance between subspaces in terms of their orthogonality: it is 1 if the spaces are orthogonal, and decays gracefully to 0 as the spaces get more parallel.

The sign of the sine is worth studying in more detail, for it indicates from which direction **A** approaches **B**. However, we have to be careful with this interpretation: there may be a sign change depending on whether we compute **A** ∩ **B** or **B** ∩ **A**. One should study this sign only relative to the choice of sign for the pseudoscalar for the space spanned by the join during normalization. Let us therefore compare **B** ∩ **A** with **A** ∩ **B** relative to the same join, by means of the dualization formula (5.8):

$$\mathbf{B} \cap \mathbf{A} = (\mathbf{A}^* \wedge \mathbf{B}^*)^{-*} = (-1)^{(j-a)(j-b)} (\mathbf{B}^* \wedge \mathbf{A}^*)^{-*} = (-1)^{(j-a)(j-b)} \mathbf{A} \cap \mathbf{B}$$

using (2.13) to swap the arguments of the outer product. Therefore, it depends on the grades of the elements whether the meet is symmetric or antisymmetric. Two lines through the origin in a plane (a = b = 1, j = 2) meet in antisymmetric fashion: **A** ∩ **B** = −**B** ∩ **A**. This makes sense, since if we swap the lines then we are measuring the sine of an opposite angle, and this is of opposite sign. On the other hand, a line and a plane through the origin in space (a = 1, b = 2, j = 3) meet symmetrically: **A** ∩ **B** = **B** ∩ **A**. There is still a sine involved, which changes sign as the relative orientation changes so that we can tell whether the line passes from the front or the back of the plane. But in the computation, it apparently does not matter whether the line meets the plane or vice versa.

This subtle interplay of signs of orientation of the join, the relative attitudes in space, and the order of arguments in the meet requires some experience to interpret properly. We give some examples of the ordering sign for common situations in Table 5.1.

---

## 5.7 Linear Transformation of Meet and Join

Even though the meet and join are not completely linear in their arguments, they do transform tidily under invertible linear transformations in a structure-preserving manner (by which we mean that the transform of the meet equals the meet of the transforms). This paradoxical result holds because such transformations cannot change the relative attitudes of the blades involved in any real way: if **A** was not contained in **B** before a linear transformation f, then f[**A**] will also not be contained in f[**B**] after the transformation. In that sense, the preservation of meet and join is a structural property of linear transformations. The proof of this fundamental property is not hard, since we know how the outer product and the contraction transform.

First, the join is made by a factorization in terms of the outer product. Since a linear transformation is an outermorphism, the linear mapping f preserves the outer product factorization, and we obtain trivially that

$$f[\mathbf{A} \cup \mathbf{B}] = f[\mathbf{A}] \cup f[\mathbf{B}]$$

The meet also transforms in a structure preserving manner:

$$f[\mathbf{A} \cap \mathbf{B}] = f[\mathbf{A}] \cap f[\mathbf{B}]$$

The reason is simply that the defining relationships of (5.1) and (5.2) between **A**, **B**, **J** = **A** ∪ **B** and **M** = **A** ∩ **B** only involve the outer product; therefore a linear transformation f, acting as an outermorphism, preserves all these relationships between the transformed entities.

When converting the expression f[**A**] ∩ f[**B**] to a computational form involving the contraction analogous to (5.6), these outermorphic correspondences imply that one should use duality relative to the transformed join f[**J**], not the original join **J**. So the transformation of (5.6) reads explicitly:

$$f[\mathbf{A} \cap \mathbf{B}] = f[\mathbf{B}] \lfloor f[\mathbf{J}]^{-1} \rfloor f[\mathbf{A}]$$

This is really different from f[**B**]⌊**J**⁻¹⌋f[**A**], since f[**J**] is in general not even proportional to **J**. This dependence on the join dualization is a good reason to use the explicit (5.7) rather than the overly compact (5.8).

Since a linear transformation usually changes the metric measures of elements (except when it is an orthogonal transformation), the preservation of meet and join under general linear transformations shows that these are actually **nonmetric products**. For the join, that is perhaps not too surprising (since it is like an outer product), but the occurrence of the two contractions in the computation of the meet makes it look decidedly metric. The nonmetric nature of the result must mean that these two contractions effectively cancel in their metric properties. In that sense, we have merely used the contraction to write things compactly. Mathematicians encoding union and intersection for the nonmetric projective spaces have devised a special and rather cumbersome notation for the nonmetric duality that is actually involved here. (It is called the Hodge dual, and its proper definition requires the introduction of the n-dimensional space of 1-forms.) We will not employ it, and just use our metric contraction instead.

But it is relevant to note that **the precise form of the metric does not matter**. If we ever need to compute meet and join in spaces with unusual metrics, we can always assume that we are in a Euclidean metric if that simplifies our computations. This is why we had no compunction about using the inverses **M**⁻¹ and **J**⁻¹ in our derivations; they can always be made to exist by embedding the whole computation temporarily in a Euclidean metric. We will apply this principle in the algorithm to compute meet and join in Chapter 21.

---

## 5.8 Offset Subspaces

So far we have only treated subspaces containing the origin, and although we have been able to do that case in general, it is of course not the most relevant case in applications. We postpone the treatment of the intersection of subspaces offset from the origin to their proper formalization as elements of the homogeneous model in Chapter 11. There we will show that parallel lines have a finite meet and that skew lines in space meet in a scalar proportional to their orthogonal Euclidean distance.

More surprisingly still, in Chapter 13 we will introduce an operational model of Euclidean geometry in which the meet of spheres, circles, lines, and planes can be computed by straightforward application of the subspace intersection formulas of the present chapter.

---

## 5.9 Further Reading

The meet and join are strangely positioned within the literature on algebras for subspaces: they are either neglected (presumably because they are algebraically not very tidy), or an attempt is made to take them as axiomatic products replacing the outer product and contraction.

- The meet and join are treated seriously and extensively in Stolfi's classical book on oriented projective geometry [60]. It is richly illustrated, and sharpens the intuition of working with oriented subspaces. It also gives an algorithm for meet and join in terms of the matrix representation of subspaces. Unfortunately, it does not treat metric geometry.

- When meet and join are taken as basic products, they are linearized: the join is redefined as the outer product of its arguments, and the meet is defined through duality (our (5.8)). It is then called the *regressive product*. This alternative algebra of subspaces tends to be nonmetric, with nonmetric duality, and is not easily extended to geometric algebra. Still, the work is mathematically interesting; a rather complete account is [3].

- We noted that the outcomes of meet and join are not fully qualified subspaces, since there is an ambiguity about their absolute weight and orientation. Within the context of geometric algebra, they are perhaps more properly represented as projection operators than as blades. This has been explored in [8]. An interesting subalgebra results, which forms the basis of algorithms to compute meet and join.

- The fundamental nature of meet and join for the treatment of linear algebra is displayed in [27]. When reading that and other literature founded in geometric algebra, beware that the use of an inner product that is not the contraction (see Appendix B) tends to create seemingly exceptional outcomes for meet and join when scalars or pseudoscalars are involved. The contractions avoids those exceptions; this issue is explained in [17] as one of the reasons to prefer them.

---

## 5.10 Exercises

### 5.10.1 Drills

Compute join **A** ∪ **B** and meet **A** ∩ **B** for the following blades:

1. **A** = **e**₁ and **B** = **e**₂.
2. **A** = **e**₂ and **B** = **e**₁.
3. **A** = **e**₁ and **B** = 2**e**₁.
4. **A** = **e**₁ and **B** = (**e**₁ + **e**₂)/√2.
5. **A** = **e**₁ and **B** = cos θ **e**₁ + sin θ **e**₂.
6. **A** = **e**₁ ∧ **e**₂ and **B** = cos θ **e**₁ + sin θ **e**₂.
7. **A** = **e**₁ ∧ **e**₂ and **B** = **e**₂.
8. **A** = **e**₁ ∧ **e**₂ and **B** = **e**₂ + 0.00001 **e**₃.

### 5.10.2 Structural Exercises

1. There is an interesting reciprocal relationship between **A**, **B**, **J**, and **M**.

   $$(\mathbf{B} \lfloor \mathbf{J}^{-1}) * (\mathbf{A} \lfloor \mathbf{M}^{-1}) = 1$$

   Verify the steps in the following proof: 1 = **M**⁻¹ \* **M** = **M**⁻¹ \* ((**B**⌊**J**⁻¹)⌋**A**) = (**M**⁻¹ ∧ (**B**⌊**J**⁻¹)) \* **A** = (**B**⌊**J**⁻¹) \* (**A**⌊**M**⁻¹). Then prove in a similar manner:

   $$(\mathbf{M}^{-1} \rfloor \mathbf{B}) * (\mathbf{J}^{-1} \rfloor \mathbf{A}) = 1$$

2. Find the error in this part of a 'proof' of the meet transformation formula of page 135 (from the first printing of this book):

   > Let us first establish how the inverse of the join transforms by transforming the join normalization equation **J**⁻¹ \* **J** = 1:
   >
   > 1 = f[1] = f[**J**⁻¹ \* **J**] = f⁻¹[**J**⁻¹] \* f[**J**],
   >
   > so that f⁻¹[**J**⁻¹] = f[**J**]⁻¹.

3. Compute meet and join of two vectors **a** and **b** in general position, and show that the magnitude of their meet (relative to their join) is the sine of their angle. Relate the sign of the sine to the order of intersection. In this case, the meet should be antisymmetric.

4. Compute the meet and join of two parallel vectors **u** and **v**. The meet should now be symmetric. (Hint: Use one of them as the join.)

5. As an exercise in symbolic manipulation of the products so far, let us consider the meet of **a** ∧ **B** and **a** ∧ **C**, where **a** is a vector and the blades **B** and **C** have no common factor. The answer should obviously be proportional to **a**, but what precisely is the proportionality factor? (Hint: If you get stuck, the next exercise derives the answer as (**a** ∧ **B** ∧ **C**)\*.)

6. Verify the steps in the following computation of the answer to the previous exercise. They are rather ingenious; note the third step especially, and the conversion to a scalar product (check the grades involved!). The join for dualization should be a blade proportional to **a** ∧ **B** ∧ **C** (if it is zero our suppositions are wrong, and vice versa). Here goes:

   $$(\mathbf{a} \wedge \mathbf{B}) \cap (\mathbf{a} \wedge \mathbf{C}) = \left( (\mathbf{a} \wedge \mathbf{C})^* \wedge (\mathbf{a} \wedge \mathbf{B})^* \right)^{-*} = \left( (\mathbf{a} \rfloor \mathbf{C}^*) \wedge (\mathbf{a} \rfloor \mathbf{B}^*) \right)^{-*}$$

   $$= \mathbf{a} \left( \mathbf{C}^* \wedge (\mathbf{a} \rfloor \mathbf{B}^*) \right)^{-*} = \left( \mathbf{a} \left( \mathbf{C}^* \wedge (\mathbf{a} \wedge \mathbf{B})^* \right) \right)^{-*}$$

   $$= \mathbf{a} \wedge \left( \mathbf{C}^* \rfloor (\mathbf{a} \wedge \mathbf{B}) \right) = \mathbf{a} \wedge \left( \mathbf{C}^* * (\mathbf{a} \wedge \mathbf{B}) \right)$$

   $$= \mathbf{a} \wedge \left( (\mathbf{a} \wedge \mathbf{B}) * \mathbf{C}^* \right) = \mathbf{a} \wedge \left( (\mathbf{a} \wedge \mathbf{B}) \lfloor \mathbf{C}^* \right)$$

   $$= \mathbf{a} \wedge (\mathbf{a} \wedge \mathbf{B} \wedge \mathbf{C})^*$$

7. Use the previous derivation to derive the general factorization of the meet:

   $$(\mathbf{A} \wedge \mathbf{B}) \cap (\mathbf{A} \wedge \mathbf{C}) = \mathbf{A} (\mathbf{A} \wedge \mathbf{B} \wedge \mathbf{C})^*$$
   **(5.11)**

   where **A**, **B**, and **C** have no common factors.

---

## 5.11 Programming Examples and Exercises

### 5.11.1 The Meet and Join

This example allows you to interactively select and manipulate two multivectors. The multivectors can be vector-valued or 2-blade-valued. Either the meet or the join of the multivectors are drawn:

```cpp
// M1 and M2 are the two multivectors
mv X;
if (g_draw == DRAW_MEET) X = meet(M1, M2);
else X = join(M1, M2);
// ... (set color, scale)
draw(X);
```

Note that we use multivectors (class `mv`) here because neither the input nor the output has a fixed multivector type. As demonstrated in the next example, working with the `mv` class in general and the `meet()` and `join()` functions in particular is much slower than the specialized classes and the ordinary products.

To make it easier to produce degenerate cases—such as two parallel vectors—we round the coordinates of multivectors `M1` and `M2` to multiples of 0.2. This causes them to move in a stepwise fashion.

### 5.11.2 Efficiency

In Gaigen 2, the implementation of the meet and join is very slow compared to the other products. This example performs a benchmark to demonstrate this. It creates 1,000,000 pairs of random vectors and bivectors. It then times how long it takes to compute the outer product of these pairs, and how long it takes to compute the join of these pairs. In our benchmark the join is about 100 times slower than outer product. There are several reasons for this:

- To compute the meet and join, a specialized (factorization) algorithm is used, whereas computing the outer product is as simple as multiplying and summing coordinates in the right way. See Section 21.7 for a description of the meet and join algorithm used in this example.

- The algorithm uses the `mv` class instead of the specialized types such as `vector` and `bivector`. The `mv` class uses coordinate compression, which is slow.

- The ordinary subspace products are just very efficient in Gaigen 2.

It may be possible to optimize the meet and join to a level where they are about 10 times slower than the regular products. But in general, you should try to avoid the meet and join in your programs if you care about efficiency. If you know the relative position of elements involved, just use the formula **B**\*⌋**A** in the appropriate subspace instead of **A** ∩ **B**.

### 5.11.3 Floating Point Issues

As stated above, the meet and join are computed by a factorization algorithm. Before the factorization starts, the algorithm computes what the grade of the output should be. This involves comparing a condition number (similar to that of a matrix) to a small threshold value. Hence, the algorithm will flip-flop between grades in degenerate cases (e.g., near-parallel vectors).

This example (see Figure 5.4) searches for the point where the join of two (near-)parallel vectors changes from a vector to a 2-blade. It starts with a very small probe epsilon of 10⁻¹⁰, and tests if **e**₁ ∪ (**e**₁ + 10⁻¹⁰ **e**₂) is a 2-blade. If not, it grows the probe epsilon, and loops. In the example, the flip-flop occurs when **b** = **e**₁ + 1.007748 × 10⁻⁷ **e**₂, which is to be expected, because the meet-join algorithm uses an epsilon of 10⁻⁷.

```cpp
// get two vectors, initialize 'a' to 'e1'
e3ga::vector a, b;
a = e1;
float probeEpsilon = 1e-10f;
while (true) {
    // the loop will be broken when the join is a bivector;
    // add a tiny bit of 'e2' to b:
    b = e1 + probeEpsilon * e2;
    
    // compute the join
    mv X = join(a, b);
    
    // get analysis of 'X'
    mvAnalysis AX(X);
    
    // check if blade, and if a blade, then is it a 2-blade or a vector?
    if (!AX.isBlade()) {
        // this should never happen
        printf("Error: the join of a and b is not a blade!\n");
        return -1;
    }
    else {
        // compute string "join(..., ...)"
        std::string str = "join(" + a.toString_e() + ", " + b.toString_e() + ")";
        if (AX.bladeSubclass() == mvAnalysis::BIVECTOR) {
            printf("%s is a 2-blade\n", str.c_str());
            return 0; // terminate
        }
        else printf("%s is a vector\n", str.c_str());
    }
    
    // Grow 'probeEpsilon' a little such that it won't take forever to reach
    // the point where join(a, b) is a 2-blade:
    probeEpsilon *= 1.01f;
}
```

> **Figure 5.4:** Searching for the point at which the join of two (near-)parallel vectors becomes a 2-blade (Example 3).

---

## Table 5.1: Order Sensitivity of Meet Arguments

The order of the arguments for a computed meet may affect the sign of the result. This table shows the signs for some common geometrical situations. A plus denotes no sign change, a minus a change. The vector space model in which all elements pass through the origin is denoted as **orig**. This is the algebra of the homogeneous subspaces in Part I.

For convenient referencing, we have also listed some results for the 4D homogeneous model (**hom**) and the 5D conformal model of 3-dimensional Euclidean space (**conf**), which will only be treated in Part II. In the bottom block, 'line' and 'plane' can always substituted for 'circle' and 'sphere'. The order sensitivity does not depend on the model used, since only the 'co-dimensions' (j − a) and (j − b) matter.

| Elements in meet | join | Space | a,b,j (orig) | a,b,j (hom) | a,b,j (conf) | Sign |
|------------------|------|-------|--------------|-------------|--------------|------|
| Two origin points | Point | | 0,0,0 | 1,1,1 | 2,2,2 | + |
| Origin point and origin line | Line | | 0,1,1 | 1,2,2 | 2,3,3 | + |
| Two origin lines | Plane | | 1,1,2 | 2,2,3 | 3,3,4 | − |
| Two origin lines | Line | | 1,1,1 | 2,2,2 | 3,3,3 | + |
| Two origin planes | Space | | 2,2,3 | 3,3,4 | 4,4,5 | − |
| Origin line and origin plane | Space | | 1,2,3 | 2,3,4 | 3,4,5 | + |
| Origin line and origin plane | Plane | | 1,2,2 | 2,3,3 | 3,4,4 | + |
| Two parallel lines | Plane | | | 2,2,3 | 3,3,4 | − |
| Two intersecting lines | Plane | | | 2,2,3 | 3,3,4 | − |
| Two skew lines | Space | | | 2,2,4 | 3,3,5 | + |
| Two intersecting planes | Space | | | 3,3,4 | 4,4,5 | − |
| Two parallel planes | Space | | | 3,3,4 | 4,4,5 | − |
| Line and plane | Space | | | 2,3,4 | 3,4,5 | + |
| Line and plane | Plane | | | 2,3,3 | 3,4,4 | + |
| Point and line | Plane | | | 1,2,3 | 2,3,4 | + |
| Point and plane | Space | | | 1,3,4 | 2,4,5 | − |
| Point and circle | Sphere | | | | 1,3,4 | + |
| Point and sphere | Space | | | | 1,4,5 | + |
| Point pair and circle | Sphere | | | | 2,3,4 | + |
| Point pair and sphere | Sphere | | | | 2,4,4 | + |
| Circle and sphere | Space | | | | 3,4,5 | + |
| Circle and sphere | Sphere | | | | 3,4,4 | + |
| Circle and circle | Space | | | | 3,3,5 | + |
| Circle and circle | Sphere | | | | 3,3,4 | − |
| Tangent vector and sphere | Sphere | | | | 2,4,4 | + |
| Sphere and sphere | Space | | | | 4,4,5 | − |

---

## Footnotes

¹ The reader should be warned that the terminology of "join" and "meet" is used in some literature in a different sense, directly corresponding to our outer product, and our operation of contraction with a dual, respectively. Those are then truly linear products, though they do not always compute the geometric union and intersection (they return zero in degenerate situations). To add to the confusion, that literature uses the notations ∨ for their "join" and ∧ for their "meet."
