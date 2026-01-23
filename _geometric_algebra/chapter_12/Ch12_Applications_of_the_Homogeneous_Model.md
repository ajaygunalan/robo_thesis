# Chapter 12: Applications of the Homogeneous Model

The homogeneous model is well suited to applications in which incidences of offset flat subspaces are central, but less so when metric properties are also important. In this, it plays a role similar to Grassmann-Cayley algebra. This chapter gives details on its direct use in applications.

In the first part, we discuss the coordinate representations of the homogeneous elements. This naturally embeds the powerful Plücker coordinates for line computations, which are seen to be a natural extension of homogeneous point coordinates (using the outer product). We show how you can master them and derive new application formulas simply. Those coordinates for lines, as well as points and planes, permit compact formulation of the affine transformations as matrices.

In the second part, we give an advanced application of the homogeneous model. It is well suited to encode the projective geometry involved in the imaging of the world by one or more pinhole cameras. The homogeneous model permits easy specification of how observations in the various cameras are connected, which permits using observations by one camera to guide the search for corresponding features in another camera. We treat the fairly advanced subjects of stereo-vision based on point and line matches in 2 or 3 cameras.

Both subjects of this chapter are incidental to the main flow of the book, though the section on Plücker coordinates prepares you for the implementation of geometric algebra in Part III.

---

## 12.1 Homogeneous Plücker Coordinates in 3-D

In the previous chapter, we saw how the homogeneous model permits direct and dual representation of flats. This extends the commonly used homogeneous coordinates for points and hyperplanes used throughout computer graphics and robotics literature. In some more specialized texts, you may also find a representation of lines by Plücker coordinates. These are coordinates tailored to the description of lines, and they permit direct computation with lines as basic elements. That provides for faster and simpler code than if you described lines by a direction vector and a position vector, or as two plane equations, or by two points. Repeated attempts have been made to introduce them into mainstream computer graphics, where line computations are obviously important, but with limited success.

It is clear why Plücker coordinates are less well known than they deserve to be. In the usual texts, they are presented as a strange mathematical trick, not clearly related to the homogeneous coordinates. They require 6-D vectors and corresponding matrices, which appear extraneous to the usual 4-D data structures in homogeneous coordinate software. So most people continue to encode lines as composite elements in a data structure consisting of two vectors. This denies lines the status of being convenient elements of computation, and that in turn affects solutions to practical problems; if there is a natural way of describing and solving some problem using lines, it is less likely to be found. An example is visual self-localization by a robot in an office environment; a typical solution looks to match point features, neglecting the numerous straight lines usually present in such an environment. Reducing everything to point-based or plane-based computations may be suboptimal and neglects the perfectly useful and stably measurable straight edges. But to actually use them in your estimation processes, you need the ability to compute with them.

In this chapter, we show how to look at the Plücker coordinates in a manner that makes them natural and convenient to use. There are no new concepts here; this is an application of the structure of the previous chapter, but is good to relate the algebra to the specific coordinate techniques that the proponents of Plücker coordinates (such as [57]) suggest.

### 12.1.1 Line Representation

Let us again look at the representation of lines, and focus specifically on a 3-D base space. The line representation **p** ∧ **q** of (11.3) as

$$\mathbf{p} \wedge \mathbf{q} = e_0 \wedge (\mathbf{q} - \mathbf{p}) + \mathbf{p} \wedge \mathbf{q} \tag{12.1}$$

involves six coordinates: three for the 2-blade e₀ ∧ (**q** − **p**) and three for the 2-blade **p** ∧ **q**. There is one dependency relationship (since e₀ ∧ (**q** − **p**) ∧ (**p** ∧ **q**) = 0), and that reduces the degrees of freedom of the line to five. Geometrically, you can interpret the first term of (12.1) as the direction vector and the second term as the moment.

We can group the six coordinates of a line in 3-D as two vectors of three components, by employing the cross product:

$$\mathbf{p} \wedge \mathbf{q} = e_0 \wedge (\mathbf{q} - \mathbf{p}) + \mathbf{p} \wedge \mathbf{q} = (\mathbf{p} - \mathbf{q})e_0 + (\mathbf{p} \times \mathbf{q}) I_3 \tag{12.2}$$

We recognize (minus) the direction vector and the dual of the moment 2-blade (which is the properly weighted normal vector of the plane through the line and the origin). Together, these form the **Plücker coordinates** of the 3-D line, denoted by

$$-\{\mathbf{p} - \mathbf{q}; \mathbf{p} \times \mathbf{q}\} \tag{12.3}$$

(see [57]). Classically, these are often treated as six slots for storing numbers, without much algebraic structure, and manipulations with these numbers may seem rather arbitrary, especially when combined with the homogeneous coordinate representations of points and planes. Table 12.1 gives some examples. The operations are simple and fast and that explains the interest of the Plücker coordinates, but the structure between these "magic formulas" is lost, so that implementations are hard to extend to cases not covered in such tables (or to higher dimensions). The usual nonalgebraic encoding of the type of element represented by different kinds of brackets around the coordinates does little to clarify the structure of the table.

**Table 12.1: Common Plücker coordinate computations** with a line {**a**, **m**}, a plane [**n**, δ], and a point (**p** : 1). The type of bracket denotes the type of object nonalgebraically. (Expanded from [57].) Note that **a** is minus the usual direction vector.

| Expression | Description |
|------------|-------------|
| (**p** : 1) | Point at location **p** |
| [**n**, −δ] | Plane with normal **n** and offset δ |
| **n** · **p** − δ | Distance from point to plane |
| {**a**, **m**} = {**p** − **q**, **p** × **q**} | Line through two points, from Q to P |
| (**m** · **m**)/(**a** · **a**) | Squared distance of line to origin |
| (**m** × **a** : **a** · **a**) | Point on line closest to origin |
| [**a** × **m** : **m** · **m**] | Plane through line, perpendicular to origin plane |
| (**m** × **n** + δ**a** : **a** · **n**) | Point in line and plane |
| [**a** × **p** − **m** : **m** · **p**] | Plane through line and point |
| [**a** × **n** : **m** · **n**] | Plane through line, additional direction **n** |

In the geometric algebra point of view, we see that the six numbers are coefficients on a specific basis, in (12.2) demonstrated by the extra symbols e₀ and I₃. This gives the full algebraic meaning to the Plücker coordinates, and endows them automatically with relationships to the other elements through their membership in geometric algebra. Their actual construction in (12.2) is a clear instance of this: by taking the outer product of two homogeneous points, we get the line representation, providing the straightforward connection between point coordinates and line coordinates through the standard operation of outer product. The same standard operation should connect the table entries for point, line, and plane through line and point. This obvious geometrical fact is not at all clear from the corresponding entries in Table 12.1. Only by translating the bracket notation back into its actual geometric basis and applying the standard constructions of geometric algebra can we understand and extend such tables.

### 12.1.2 The Elements in Coordinate Form

In the homogeneous model of 3-D space, the representation of the quantities in terms of coordinates is easily computed. We give a complete inventory of the repertoire of geometric elements in the homogeneous model. We study the coordinate representation of the offset flat subspaces of various grades (points, lines, and planes) in both their direct and in their dual representations.

**1. Point.** We have seen that the 1-D homogeneous subspace representing a 0-D point in the homogeneous model is of the form e₀ + **p** (or a multiple). In a homogeneous model of 3-space with basis {e₁, e₂, e₃, e₀}, it therefore has the coordinates (p₁, p₂, p₃, 1) (or a multiple), with (p₁, p₂, p₃) the Euclidean coordinates of its position vector. In Table 12.1 this is written as (**p** : 1), following [57].

**2. Hyperplane.** If we have a plane characterized as all points **x** such that **x** · **n** = δ, this can be written as (e₀ + **x**) · (−**n** + δe₀⁻¹) = 0, so as **x** · (−**n** + δe₀⁻¹) = 0. Therefore −**n** + δe₀⁻¹ (or any multiple of it) is the dual of the blade representing the hyperplane. It is represented on a basis {e₁, e₂, e₃, e₀⁻¹}, which appears different from the basis for points until you realize that e₀⁻¹ = ±e₀, depending on the metric chosen. Therefore the bases are the same, and you cannot tell these elements apart as vectors.

If −**n** + δe₀⁻¹ is the dual of a blade, then the blade itself must be

$$(−\mathbf{n} + δe_0^{-1})(e_0 I_3) = −\mathbf{n}e_0I_3 + δI_3$$

(where we take the undualization in the (n + 1)-dimensional homogeneous model, so relative to the pseudoscalar e₀I₃). This has the Plücker coefficients [n₁, n₂, n₃ : −δ] used in Table 12.1, but on the trivector basis

{e₂e₃e₀, e₃e₁e₀, e₁e₂e₀, −e₁e₂e₃},

which is clearly different from the vector basis for points. In standard literature on Plücker coordinates, this difference in basis is denoted nonalgebraically by square brackets: [**n** : −δ]. Others consider planes as row vectors, and points as column vectors, so then their brackets could be interpreted as specifying this difference.

If you want a consistent representation of the direct and dual-oriented planes, you should be very explicit in your choice of basis. The dual plane also has a representation [**n** : −δ], but the basis is {−e₁, −e₂, −e₃, −e₀⁻¹ = ∓e₀} (the sign of the last element related to the sign in e₀⁻¹ = ±e₀). Such headaches are the consequences of splitting up a single geometric element (the dual plane) in its coordinates and basis, each of which separately have no objective geometric meaning.

**3. Lines.** We have seen above in (12.2) that a line is represented by minus the usual direction vector **a** = **p** − **q** and a moment vector **m** = **p** × **q** = −**p** × **a** as

$$L = \mathbf{a} e_0 + \mathbf{m} I_3 \tag{12.4}$$

The six coefficients {a₁, a₂, a₃, m₁, m₂, m₃} of this line are on the bivector basis

$$\{e_1 e_0, e_2 e_0, e_3 e_0, e_2 e_3, e_3 e_1, e_1 e_2\} \tag{12.5}$$

In Table 12.1, we follow [57] in using curly brackets for this data type. In derivations with lines, we obviously need to revert to the fully expressed form.

The dual representation of such a line is

$$L^* = L I_3^{-1} e_0^{-1} = \mathbf{a} I_3 + \mathbf{m} e_0^{-1} \tag{12.6}$$

so it has the coefficients {±m₁, ±m₂, ±m₃, a₁, a₂, a₃} on the bivector basis, the ± signs are again determined by the metric chosen. Such a dual line is not in the usual Plücker coordinate tables, though we will soon see that it is convenient to have.

It should be clear that a mere coefficient-based representation is dangerous and needs to be accompanied by some bookkeeping, at the very least by maintaining separate data structures (and this is presumably what the brackets are intended to remind us of). We would be in favor of letting that bookkeeping be done by the algebraic tags on the coefficients; it is unambiguous, nonarbitrary, and computational. It is not necessarily more expensive, for the multiplications of the basis blades used as tags are essentially Boolean operations. We will expand on this in Chapter 19 for general geometric algebras.

### 12.1.3 Combining Elements

In interactions of elements, the explicit basis specification takes care of the computational rules for the Plücker formula table. We give some examples to explain entries in the table, and some that go beyond it, to show how the algebra empowers you to extend it if your application so requires.

**1. Plane through Point and Line.** The formula for augmenting a point **p** by a line L to make a plane is of course simply the outer product of point and the direct line representation. Rewriting the result in terms of a 3-D cross product, we get

$$\mathbf{p} \wedge L = (e_0 + \mathbf{p}) \wedge (\mathbf{a} e_0 + \mathbf{m} I_3) = e_0 \wedge (\mathbf{m} I_3 + \mathbf{p} \wedge \mathbf{a}) + \mathbf{p} \wedge (\mathbf{m} I_3)$$
$$= −(\mathbf{m} + \mathbf{p} × \mathbf{a})e_0 I_3 + (\mathbf{p} \cdot \mathbf{m}) I_3$$

So this is indeed the plane [**a** × **p** − **m** : **m** · **p**] listed in Table 12.1. That this should be the natural extension of the construction of a line from two points is hard to guess from the Plücker table—yet it is a straightforward computation when one remembers their embedding in the full algebra.

**2. Point and Plane.** To compute the meet of a hyperplane Π and a point **p** in general position, we need to compute by (5.8)

$$Π ∩ \mathbf{p} = −\mathbf{p} ∩ Π = −Π^*\mathbf{p} = (\mathbf{n} − δe_0^{-1})(e_0 + \mathbf{p}) = \mathbf{n} \cdot \mathbf{p} − δ$$

We recognize a scalar outcome, of which the geometry is the oriented distance between point and hyperplane. This imbues scalars (grade 0 blades) with a geometrical meaning: they are distances, and distances are apparently legitimate outcomes of a coincidence operation.

This is of course the standard formula in the homogeneous model (calling this a Plücker coordinate formula is overdoing it), but is nice to see it as a standard *meet* rather than a special (albeit trivial) construct.

**3. Line and Plane.** The meet of a plane dually represented as Π* = −**n** + δe₀⁻¹ and a line L, in general position, is computed as

$$−Π ∩ L = −L ∩ Π = −Π^*L = (\mathbf{n} − δe_0^{-1})(\mathbf{a}e_0 + \mathbf{m}I_3)$$
$$= (\mathbf{n} \cdot \mathbf{a})e_0 + \mathbf{n}(\mathbf{m}I_3) + δ\mathbf{a} + 0 = (\mathbf{n} \cdot \mathbf{a})e_0 + (\mathbf{n} \wedge \mathbf{m})I_3 + δ\mathbf{a}$$
$$= (\mathbf{n} \cdot \mathbf{a})e_0 + (\mathbf{m} × \mathbf{n} + δ\mathbf{a})$$

Note how the orthogonality relationships between the basis elements automatically kill the potential term involving δ and **m**.

This is the correct result, representing a point at the location (**m** × **n** + δ**a**)/(**n** · **a**) in its homogeneous coordinates. It corresponds to the result in Table 12.1.

**4. Skew Lines.** The meet of two lines L₁ and L₂ in general position (skew) is a measure of their signed distance. We have seen this in algebraic form in (11.9). Here we redo the computation compactly using the specific Plücker coordinates with their algebraic tags:

$$L_1 ∩ L_2 = L_2^* L_1 = (\mathbf{a}_2 I_3 + \mathbf{m}_2 e_0^{-1})(\mathbf{a}_1 e_0 + \mathbf{m}_1 I_3) = −\mathbf{m}_1 \cdot \mathbf{a}_2 − \mathbf{m}_2 \cdot \mathbf{a}_1$$

Note that we used the dual line representation for one of the lines to derive this compact expression quickly. Again, the basis orthogonality relationships have prevented terms containing **m**₁ · **m**₂ or **a**₁ · **a**₂ from appearing (as they should!). If you had any problems evaluating the expression (**a**₂I₃)(**m**₁I₃), use duality (twice) and the commutation of the outer product of a vector and a bivector: (**a**₂I₃)(**m**₁I₃) = ((**a**₂I₃) ∧ **m**₁)I₃ = (**m**₁ ∧ (**a**₂I₃))I₃ = (**m**₁**a**₂)I₃I₃ = −**m**₁ · **a**₂.

The scalar result above retrieves the well-known compact Plücker-based method of determining how lines pass each other in space; three tests on the signs of such quantities representing the edges of a triangle determine efficiently whether a ray hits the inside of the triangle.

**5. Intersecting Lines.** When the parameters of the two lines L₁ = **p**₁ ∧ **a**₁ and L₂ = **p**₂ ∧ **a**₂ satisfy **a**₁ ∧ **a**₂ ≠ 0 but (**p**₁ ∧ **a**₁) ∧ (**p**₂ ∧ **a**₂) = 0, then lines are not skew but intersect (the latter condition implies (**p**₁ − **p**₂) ∧ **a**₁ ∧ **a**₂ = 0). The resulting meet was given in (11.20); this is easily translated into Plücker format as

$$L_1 ∩ L_2 = \|\mathbf{a}_1 × \mathbf{a}_2\|^2 e_0 + \mathbf{a}_1 \mathbf{m}_2 \cdot (\mathbf{a}_1 × \mathbf{a}_2) + \mathbf{a}_2 \mathbf{m}_1 \cdot (\mathbf{a}_2 × \mathbf{a}_1)$$
$$+ \frac{1}{2} (\mathbf{a}_2 \cdot \mathbf{m}_1 − \mathbf{a}_1 \cdot \mathbf{m}_2) (\mathbf{a}_1 × \mathbf{a}_2)$$

This outcome is immediately interpretable as a point; it is not one of the formulas one usually finds in the Plücker tables.

The other relationships of the table can be derived in a similar manner. If you need one that is not in the table, you can now derive it yourself.

### 12.1.4 Matrices of Motions in Plücker Coordinates

An affine transformation A transforms a vector **x** to

$$A[\mathbf{x}] = f[\mathbf{x}] + \mathbf{t}$$

and it has to satisfy A[e₀] = e₀ to be affine. We found in (11.16) that a general affine transformation of the base space ℝⁿ transforms a blade in the representation space ℝⁿ⁺¹ as

$$A[X] = f[X] + \mathbf{t} \wedge (e_0^{-1} \rfloor f[X])$$

where we conveniently define f[e₀] = e₀ so that f can be extended to any blade.

We can now spell out the effects on the different elements of their Plücker bases and write the result again on that basis. If we then represent the elements by Plücker coordinates, the affine transformation is representable as a matrix. By this transference principle, we can easily compute the affine matrices of some common transformations. We explain the derivations, which you can relate to the result given in Table 12.2.

The point transformation is familiar, and a direct consequence of the definition. You can compute its columns simply:

$$A[e_0] = f[e_0] + \mathbf{t} = e_0 + \mathbf{t}, \text{ and } A[e_i] = f[e_i]$$

The line transformation follows from the transformation of the elements of the line basis, and is more involved:

$$A[e_i \wedge e_0] = A[e_i] \wedge A[e_0] = f[e_i] \wedge (e_0 + \mathbf{t})$$
$$= f[e_i \wedge e_0] − \mathbf{t} \wedge f[e_i]$$
$$= f[e_i \wedge e_0] − (\mathbf{t} × f[e_i]) I_3$$

which in its matrix form involves the cross product matrix [[**t**×]]. The other part of the line transformation follows from results such as

$$A[e_2e_3] = f[e_2e_3] = f[e_1I_3] = f^{-1}[e_1]f[I_3] = \det(f)f^{-1}[e_1]I_3$$

The transformations for a dual line have not been specified in the table, but they are easily made. Comparing (12.4) and (12.6), line dualization is achieved by the matrix

$$\begin{pmatrix} [[0]] & ±[[1]] \\ [[1]] & [[0]] \end{pmatrix}$$

the sign choice again depending on the metric of the representation space. Using this dualization matrix, any matrix for an operation on a dual line can be obtained from the operation A on a direct line by undualization, performing A, and dualization. This transforms a matrix from acting on a direct line to acting on a dual line, according to

$$\begin{pmatrix} [[A_{11}]] & [[A_{12}]] \\ [[A_{21}]] & [[A_{22}]] \end{pmatrix} \mapsto \begin{pmatrix} ±[[A_{22}]] & [[A_{21}]] \\ [[A_{12}]] & ±[[A_{11}]] \end{pmatrix}$$

In the plane transformation matrix acting on elements of the form [**n**, −δ], you may recognize the 3×3 upper left submatrix as the transformation of the normal vector from (4.15). This also occurs in the direct representation of the plane, for the resulting coordinates should undergo the same transformation whether they represent a direct plane or a dual plane. You may derive it in the same manner as in its occurrence for line transformations, above.

**Table 12.2: Transformation of the flats in the homogeneous model** through matrices constructed from the outermorphisms acting on their Plücker coordinates. The same algebraic formula leads to quite different matrices. [[**t**×]] is the matrix of a cross product, defined through [[**t**×]][[**x**]] = [[**t** × **x**]]. [[1]] is an identity matrix of appropriate size, [[0]] a zero matrix.

| Element | Point | Line | Plane |
|---------|-------|------|-------|
| **Basis** | (e₁, e₂, e₃, e₀) | (e₁e₀, e₂e₀, e₃e₀, e₂e₃, e₃e₁, e₁e₂) | (e₂e₃e₀, e₃e₁e₀, e₁e₂e₀, −e₁e₂e₃) |
| **Affine** | [[f]] [[t]]; [[0]]ᵀ 1 | [[f]] [[0]]; −[[t×]][[f]] det(f)[[f]]⁻ᵀ | det(f)[[f]]⁻ᵀ [[0]]; −[[t]]ᵀdet(f)[[f]]⁻ᵀ det(f) |
| **Translation t** | [[1]] [[t]]; [[0]]ᵀ 1 | [[1]] [[0]]; −[[t×]] [[1]] | [[1]] [[0]]; −[[t]]ᵀ 1 |
| **Rotation R** | [[R]] [[0]]; [[0]]ᵀ 1 | [[R]] [[0]]; [[0]] [[R]] | [[R]] [[0]]; [[0]]ᵀ 1 |

### 12.1.5 Sparse Usage of the 24 Dimensions

The Plücker coordinate representation and its associated matrices begin to show how an implementation of geometric algebra can make use of the sparseness of the geometrically significant structures. In principle, the Clifford algebra of the 4-D representation space has 2⁴ = 16 dimensions, and arbitrary linear transformations on this algebra would therefore require 16×16 matrices, to be applied to a 16×1 vector, for some 2×16² = 512 operations per transformation.

We have seen how the basic elements of 4-D geometry form subspaces of specific grades 1, 4, 6, 4, and 1. A linear transformation of the representation vector space (which is 4-D) leads to smaller matrices on each of those. This is already a reduction from 4,096 operations to 1³+4³+6³+4³+1³ = 346, saving a factor of 12. Of course, one invokes only the transformation for the element at hand rather than transforming the whole ladder of subspaces—the worst case among these are the middle grades, which require some 216 operations for a general linear transformation.

Even among those linear transformations on the representational spaces, not all are equal, for the extra dimension and the base space ℝ³ have different semantics. Therefore, the useful transformations on the base space often have a special form. In the affine matrices above, this is reflected by their sparseness; one block is always zero. This leads to some additional reduction of the computational load.

We will go into the implementational issues in detail in Part III, after we have a more complete view of how geometric algebra performs its Euclidean computations. The matrices above will be found to play a role in fast implementations, and the consistent structure of geometric algebra permits them to be constructed implicitly by an automatic code generator rather than having to be coded by hand.

---

## 12.2 Imaging by Multiple Cameras

When you have multiple cameras observing the geometry of the world, the same points or lines may be visible from several of them. If you know the relative positions and orientations of the cameras, this allows a reconstruction of the 3-D event; alternatively, the observed consistency can be used to estimate the camera parameters.

This geometrical situation is well suited to analysis by the homogeneous model, since it involves general points, lines, and planes. We do so in this section, retrieving classical results in a coordinate-free and highly geometrical manner. (Some indices on symbols are unavoidable, but they refer to the different cameras rather than to coordinates.)

As is usual when treating these issues, we simplify the situation geometrically by considering only ideal pinhole cameras, which perform an ideal central projection.

### 12.2.1 The Pinhole Camera

Let us derive the formulas for the projection in a pinhole camera model using the homogeneous model. We choose to denote the vectors from the pinhole, so the pinhole itself is e₀, the point at the origin.¹

The imaging plane of the pinhole is in a direction **e**, at a distance f. We can merge these parameters f and **e** by saying that the support vector of the imaging plane is the vector **f** = f**e**. The imaging plane Π itself is then dually denoted by Π* ≡ π = e₀⁻¹ − **f**⁻¹. Verify this: the equation **x** · π = 0 for a probe point x = e₀ + **x** should lead to the Euclidean equation **x** · **f** = **f** · **f**, showing that the **f**-component of the vector **x** has the correct magnitude to be in the image plane.

If we now take an arbitrary unit point x in 3-D, the light ray from the pinhole to that point is

$$L = e_0 \wedge x = e_0 \wedge \mathbf{x} \tag{12.7}$$

This defines **x** fully as the Euclidean coordinate of x relative to **x**, since the equation can be solved as **x** = e₀⁻¹(e₀ ∧ x). (This solution holds even when x has been given in homogeneous coordinates relative to a different origin; see structural exercise 2.) This shows clearly that the point at x plays the role of the Euclidean direction **x** of the ray line. To find the projection formula of the vector **x**, we need to intersect this line with the imaging plane. This is an instance of the meet formula, and since we have the plane given dually, it is easiest to use the inner product form of the meet:

$$Π ∩ L = L ∩ Π = Π^* \rfloor L = π \rfloor L = (e_0^{-1} − \mathbf{f}^{-1}) \rfloor (e_0 \wedge \mathbf{x}) = e_0 (\mathbf{f}^{-1} \cdot \mathbf{x}) + \mathbf{x} \tag{12.8}$$

> ¹ The usual texts on imaging prevent awkward signs by imagining the imaging plane to be in front of the pinhole, at a distance f in the direction denoted by a unit vector **e**. We do not need to do so in our formulas, since the intrinsic treatment of oriented elements in geometric algebra takes care of the signs automatically. You can take f positive or negative, and the formulas still work to produce the projection onto the corresponding image plane.

This is a point at the 3-D location

$$\mathbf{x}' \equiv P[\mathbf{x}] = \frac{\mathbf{x}}{\mathbf{f}^{-1} \cdot \mathbf{x}} \tag{12.9}$$

that is precisely the rescaling of **x** you would expect: the magnitude guarantees that **x**' · **f** = **f** · **f**, so that **x**' indeed ends on the imaging plane. An interesting way of rewriting this is explored in structural exercise 3.

The mapping that we have produced is nonlinear—already, the test of the linear scaling property (which requires that α**x** should be mapped onto α**x**') fails. However, if we stay within the homogeneous domain and do not do the rescaling, the mapping is linear:

$$x \mapsto e_0 (\mathbf{f}^{-1} \cdot \mathbf{x}) + \mathbf{x}$$

To get the mapping in terms of points rather than vectors, we substitute **x** = e₀⁻¹(e₀ ∧ x), and obtain

$$x \mapsto e_0 \left( (\mathbf{f}^{-1} − e_0^{-1}) \cdot x \right) + x \tag{12.10}$$

Alternatively, you can derive this by using L = e₀ ∧ x instead of L = e₀ ∧ **x** in (12.8). The matrix of this linear transformation on the basis {e₁, e₂, e₃, e₀} is obtained by determining the action on each of the basis vectors. For instance, e₀ ↦ e₀ − e₀ = 0; and e₁ ↦ e₀(**f**⁻¹ · e₁) + e₁, so that the e₀ coordinate of the image of e₁ is **f**⁻¹ · e₁. The other components are similar, and the full matrix becomes

$$\begin{pmatrix} [[1]] & [[0]] \\ [[\mathbf{f}^{-1}]]^T & 0 \end{pmatrix}$$

familiar from the classical treatment (although that usually gives the matrix multiplied by f, with e₃ as axis direction). In implementations, this is what you would use to act on the homogeneous vectors, but the explicit algebraic form is more convenient for symbolic simplifications.

In the classical way of using homogeneous coordinates, the linearity of the mapping is already an advantage, certainly combined with the representation of rigid body motions as linear transformations in the homogeneous coordinate representation. But the geometric algebra treatment goes beyond this: not only is the transformation linear, it is also an outermorphism. Therefore, combinations of the original objects using outer products transform nicely (i.e., covariantly). In particular, spanning behaves well under the central projection. The general projection of a homogeneously represented object X to the imaging plane is simply always the meet of e₀ ∧ X with the image plane Π:

$$X \mapsto (e_0^{-1} − \mathbf{f}^{-1}) \rfloor (e_0 \wedge X) = e_0 \wedge \left( (\mathbf{f}^{-1} − e_0^{-1}) \rfloor X \right) + X$$

You can show, by analogy to the above, that this results in a flat with direction D = e₀⁻¹(e₀ ∧ (**f**⁻¹ ⌋ X)) and support point (e₀⁻¹ ⌊ e₀ ∧ X)/D.

Lines can now be projected immediately. On the Plücker line basis of (12.5), the projection is represented by the matrix

$$\begin{pmatrix} [[0]] & [[\mathbf{f}^{-1}×]] \\ [[0]] & [[1]] \end{pmatrix} \tag{12.11}$$

which is derived by techniques similar to our derivation of the matrices in Table 12.2. The projection of a general plane is not very interesting, since all planes project to the image plane by the matrix

$$\begin{pmatrix} [[0]] & −[[\mathbf{f}^{-1}]] \\ [[0]]^T & [[1]] \end{pmatrix}$$

Of course, in the homogeneous model of geometric algebra, we also have the rigid body motions present as linear transformations and their outermorphisms, so the whole framework now contains everything of interest in a consistent manner.

### 12.2.2 Homogeneous Coordinates as Imaging

Two points spanning a line in the world generate a projected line in the image plane spanned by two projected points. It is an amusing (but rather confusing) property of the homogeneous model that homogeneous coordinates can be introduced in the image plane using the support vector **f** as the extra homogeneous embedding dimension. Let us consider a camera of focal length equal to 1, and focal vector **f**. We will denote points in the image plane relative to the optical center (the location **f**) by an underscore. Then a point at image location **x̲** is seen from the pinhole as **f** + **x̲**. It generates a ray of possible real-world positions e₀ ∧ (**f** + **x̲**). The line spanned by two image points could be constructed in two ways, which are indeed consistent:

- The two rays e₀ ∧ (**f** + **x̲**) and e₀ ∧ (**f** + **y̲**) together span a world plane e₀ ∧ (**f** + **x̲**) ∧ (**f** + **y̲**), and this plane cuts the image plane in the world line:
  
  $$(e_0^{-1} − \mathbf{f}^{-1}) \rfloor (e_0 \wedge (\mathbf{f} + \mathbf{\underline{x}}) \wedge (\mathbf{f} + \mathbf{\underline{y}})) = e_0 \wedge (\mathbf{\underline{y}} − \mathbf{\underline{x}}) + (\mathbf{f} + \mathbf{\underline{x}}) \wedge (\mathbf{f} + \mathbf{\underline{y}}) = (e_0 + \mathbf{f} + \mathbf{\underline{x}}) \wedge (\mathbf{\underline{y}} − \mathbf{\underline{x}})$$
  
  We see from the final form (compare (11.3)) that this is a line in the direction (**y̲** − **x̲**) passing through the point **f** + **x̲** of the world (which is the point **x̲** on the image plane). This is of course what we would expect.

- Directly taking the outer product of the two points in the image plane gives:
  
  $$(\mathbf{f} + \mathbf{\underline{x}}) \wedge (\mathbf{f} + \mathbf{\underline{y}}) = (\mathbf{f} + \mathbf{\underline{x}}) \wedge (\mathbf{\underline{y}} − \mathbf{\underline{x}})$$
  
  If we are to interpret this as the line through the image points at **x̲** and **y̲**, then clearly **f** plays the role of the homogeneous coordinate in (11.3).

The similarity of the two approaches is apparent and generalizes to higher dimensions. Taking a slightly philosophical excursion, working in homogeneous coordinates is like viewing the 3-D world through a pinhole in a 4-D camera. Homogeneous coordinates are a useful version of Plato's cave metaphor, where the 3-D shadows of a 4-D higher reality are what we experience, but in which there is a clear mathematical advantage to use the 4-D "ideal world" as our spatial representation. With homogeneous coordinates, this metaphor can be taken literally as a projection from 4-D to 3-D.

### 12.2.3 Cameras and Stereo Vision

When working with cameras, one often measures positions in the local coordinate system of the camera. In that case, the use of coordinates is essential for the conversions to objective world coordinates for comparison with other camera measurements. So even though geometric algebra is coordinate-free in a way that linear algebra is not, we still need coordinate transformations for common geometrical tasks.

Let us look at a single camera. Its position and orientation can be characterized relative to a standard position and orientation, at the origin e₀ looking in the f**e₃**-direction (where f is the focal length). Any general rigid body transformation can be performed as a pure rotation around the origin, followed by a translation. Let us denote the composite transformation by A[·]. In the homogeneous coordinate representation, it is linear and an outermorphism.

To be specific, consider a camera oriented by R_A (so that R_A[f**e₃**] = **f**) and its pinhole at the point a = e₀ + **a**. This defines A as

$$X \mapsto A[X] = R_A[X] + \mathbf{a} \wedge (e_0^{-1} \rfloor R_A[X]) \tag{12.12}$$

If we measure a point in the image of camera A at location **x̲** (which for now we take to be converted to millimeters on the image plane after processing using the internal camera parameters), then this is a vector having the direction **x** = f**e₃** + **x̲** in the local coordinate system. Also in that system, it determines the line e₀ ∧ **x** emanating from the pinhole. This line can be converted to world coordinates by applying A, which you may either see as a coordinate transformation or as moving the camera to its actual configuration:

$$A[e_0 \wedge \mathbf{x}] = A[e_0] \wedge A[\mathbf{x}] = (e_0 + \mathbf{a}) \wedge R_A[\mathbf{x}]$$

Here we applied the outermorphism A to each of the factors in the outer product. We wrote the result on e₀ as a translation characterized by the position vector **a** and its effect on the purely directional element **x** as a rotation R_A. Both are easy consequences of (12.12).

Introducing a second camera B, we have a similar equation generating a line B[e₀ ∧ **x_B**] from the observation **x_B** (or **x̲_B**) and the rigid body motion B. If those two cameras are looking at the same point x and we know their relative positions and attitudes, then the measurements **x_A** and **x_B** (or rather **x̲_A** and **x̲_B**) are not geometrically independent. There is a linear constraint relating them, known as the **epipolar constraint**, which arises from the fact that the two 3-D lines we have constructed should intersect in the point x.

For this to happen, the meet of the two lines should be degenerate, which happens when their naïve join (computed as an outer product) is zero:

$$0 = A[e_0 \wedge \mathbf{x}_A] \wedge B[e_0 \wedge \mathbf{x}_B]$$

Because A and B are outermorphisms, we can manipulate this equation to a more familiar form. First distribute the mappings over the outer products:

$$0 = A[e_0] \wedge A[\mathbf{x}_A] \wedge B[e_0] \wedge B[\mathbf{x}_B] = (e_0 + \mathbf{a}) \wedge R_A[\mathbf{x}_A] \wedge (e_0 + \mathbf{b}) \wedge R_B[\mathbf{x}_B]$$

Taking the inner product of this equation with e₀⁻¹, and noting that the second and fourth factor are purely Euclidean (so that they do not contribute), we get

$$0 = R_A[\mathbf{x}_A] \wedge (e_0 + \mathbf{b}) \wedge R_B[\mathbf{x}_B] + (e_0 + \mathbf{a}) \wedge R_A[\mathbf{x}_A] \wedge R_B[\mathbf{x}_B]$$
$$= R_A[\mathbf{x}_A] \wedge (\mathbf{b} − \mathbf{a}) \wedge R_B[\mathbf{x}_B]$$

The meaning of the resulting equation is sketched in Figure 12.3: the observed vectors and the relative camera position are in one plane. (If in the derivation the idea of taking the inner product with e₀⁻¹ strikes you as unnatural, you can also write out the above equation in its Euclidean and non-Euclidean components, and focus on the non-Euclidean part being zero—that is, the same. The Euclidean part is then automatically zero, so we have not lost generality.)

The equation above is often rewritten in terms of the relative rotation of B relative to A, which is R_A^B ≡ R_A⁻¹R_B. This gives, applying R_A⁻¹ to the whole blade equation:

$$0 = \mathbf{x}_A \wedge R_A^{-1}[\mathbf{b} − \mathbf{a}] \wedge R_A^B[\mathbf{x}_B]$$

We recognize in R_A⁻¹[**b** − **a**] the position of the pinhole of B measured in the A-frame. Denoting that as the translation vector **t_A**, we get

$$0 = \mathbf{x}_A \wedge \mathbf{t}_A \wedge R_A^B[\mathbf{x}_B] \tag{12.13}$$

This is the epipolar constraint on the point **x_A** given the point **x_B** (in B coordinates) and the relative poses of the cameras.

Note that this equation states that the measured **x_A** should lie on the 2-blade **t_A** ∧ R_A^B[**x_B**] parameterized by **x_B**. In the image plane, this implies that the point **x̲_A**/f_A lies on the line **t_A** ∧ R_A^B[**e₃** + **x̲_B**/f_B]—note how **e₃** plays the role of a homogeneous model dimension for the image plane, just as we showed before.

In the classical treatment of the epipolar constraint, there are of course no trivector equations. We get to a scalar equation by taking the Euclidean dual of (12.13), which gives

$$0 = \mathbf{x}_A \cdot (\mathbf{t}_A × R_A^B[\mathbf{x}_B])$$

This is the form in which you find the epipolar constraint in texts on stereo vision, although it is often formulated in matrix form

$$0 = [[\mathbf{x}_A]]^T[[\mathbf{t}_A^×]][[R_A^B]][[\mathbf{x}_B]]$$

by introducing the matrix [[**t_A**×]] that performs the cross product with **t_A**. The combination [[E_A^B]] = [[**t_A**×]][[R_A^B]] is known as the **essential matrix** of the stereo vision problem.

### 12.2.4 Line-Based Stereo Vision

In more advanced stereo vision, one does not use only potential point matches to reconstruct the depth image of reality, but also line matches. In the usual formulation, the representation of such lines and the matches that are their consequences is not always straightforward. The reason is that you require Plücker coordinates to represent lines, and this is an extra representational step in the classical approaches. In the geometric algebra approach, lines are natural elements of the algebra, just like points are, and the formulation of the line-based stereo matching is more clearly analogous to that for points. We investigate that briefly in this section.

Consider a camera A as above, with rigid body motion A[·], but now look at the interpretation of an observed line in the image plane. First, place a camera in the origin, in standard orientation. A line in the image plane at location **x̲** in the image and direction **u̲** (parallel to the image plane) is

$$L = (e_0 + \mathbf{f} + \mathbf{\underline{x}}) \wedge \mathbf{\underline{u}} = e_0 \mathbf{\underline{u}} + M$$

so it is characterized by a direction vector **u̲** and a 3-D moment 2-blade M = (**f** + **x̲**) ∧ **u̲**. This line generates the plane of rays from the pinhole e₀:

$$e_0 \wedge L = e_0 \wedge M \tag{12.14}$$

which only depends on the moment of the line. The 3-D Euclidean 2-blade M thus completely characterizes the observed line (obviously, you can retrieve the direction by intersection with the image plane), and we will denote the observed line by this 2-blade. (This is also shown by the matrix of the line projection in (12.11), which only involves the coordinates of the moment.) Note the subtle difference between the effectively observed line M and the real-world 3-D line L, and how (12.14) expresses that they are geometrically and algebraically identical when seen from the pinhole.

Moving the camera to its general position and orientation by its rigid body motion A, we find that an observed line L_A in the image corresponds to a potential plane

$$A[e_0 \wedge L_A] = A[e_0 \wedge M_A] = (e_0 + \mathbf{a}) \wedge R_A[M_A]$$

Now consider three cameras A, B, C, each observing the same line L as L_A, L_B, and L_C, respectively, in their own local frames of reference. The world planes of the observed lines should intersect in line L. Algebraically, we can express this by stating that their meet naïvely computed with the pseudoscalar e₀I₃ as a join is zero (since they are not in general position). This gives the equation

$$0 = (A[e_0 \wedge L_A])^* \wedge (B[e_0 \wedge L_B])^* \wedge (C[e_0 \wedge L_C])^*$$

To get more specific in the consequences, we expand the rigid body motion in its translational and rotational parts and write the full dual in terms of the Euclidean dual (since I₄ = e₀I₃, we have X* = X ⌊ e₀⁻¹). As shorthand, we define Euclidean dual moment vectors **m_A** ≡ M_A*, and so on, in local camera coordinates, and their rotated versions **m'_A**, **m'_B**, **m'_C** to world coordinates:

$$\mathbf{m}'_A ≡ R_A[\mathbf{m}_A] = R_A[M_A]^*$$
$$\mathbf{m}'_B ≡ R_B[\mathbf{m}_B] = R_B[M_B]^*$$
$$\mathbf{m}'_C ≡ R_C[\mathbf{m}_C] = R_C[M_C]^*$$

The **m_A**, **m_B**, **m_C** are dual representations of the planes of the rays for each of the lines and therefore simply dual representations of the observed lines in all their projective essence. You may think of them as the observed lines. The **m'_A**, and so on, are those directions transferred to world coordinates. Then we obtain

$$0 = ((e_0 + \mathbf{a}) \wedge R_A[M_A])^* \wedge ((e_0 + \mathbf{b}) \wedge R_B[M_B])^* \wedge ((e_0 + \mathbf{c}) \wedge R_C[M_C])^*$$
$$= ((e_0 + \mathbf{a})(\mathbf{m}'_A e_0^{-1})) \wedge ((e_0 + \mathbf{b})(\mathbf{m}'_B e_0^{-1})) \wedge ((e_0 + \mathbf{c})(\mathbf{m}'_C e_0^{-1}))$$
$$= ((\mathbf{a} \cdot \mathbf{m}'_A)e_0^{-1} − \mathbf{m}'_A) \wedge ((\mathbf{b} \cdot \mathbf{m}'_B)e_0^{-1} − \mathbf{m}'_B) \wedge ((\mathbf{c} \cdot \mathbf{m}'_C)e_0^{-1} − \mathbf{m}'_C)$$
$$= −\mathbf{m}'_A \wedge \mathbf{m}'_B \wedge \mathbf{m}'_C$$
$$+ ((\mathbf{a} \cdot \mathbf{m}'_A) \wedge \mathbf{m}'_B \wedge \mathbf{m}'_C − \mathbf{m}'_A \wedge (\mathbf{b} \cdot \mathbf{m}'_B) \wedge \mathbf{m}'_C + \mathbf{m}'_A \wedge \mathbf{m}'_B \wedge (\mathbf{c} \cdot \mathbf{m}'_C)) e_0^{-1}$$

Therefore, there are two equations that follow from the triviality of the meet:

$$0 = \mathbf{m}'_A \wedge \mathbf{m}'_B \wedge \mathbf{m}'_C$$

and

$$0 = (\mathbf{a} \cdot \mathbf{m}'_A) \mathbf{m}'_B \wedge \mathbf{m}'_C − (\mathbf{b} \cdot \mathbf{m}'_B) \mathbf{m}'_A \wedge \mathbf{m}'_C + (\mathbf{c} \cdot \mathbf{m}'_C) \mathbf{m}'_A \wedge \mathbf{m}'_B$$

The first equation has a simple geometrical interpretation: the **m'_i** are the normal vectors of planes through a common line L, and these are of course coplanar. The second involves the positional aspects, and is more quantitative.

We can interpret these equations as a condition on any of the observed lines, given the other two lines. Let us develop this for **m'_A**. To factorize **m'_A** out of the second equation (in terms of the outer product), we need to get rid of the first term. We can do so by taking the inner product with **a** of the first equation, which gives

$$0 = (\mathbf{a} \cdot \mathbf{m}'_A) \wedge \mathbf{m}'_B \wedge \mathbf{m}'_C − (\mathbf{a} \cdot \mathbf{m}'_B) \wedge \mathbf{m}'_A \wedge \mathbf{m}'_C + (\mathbf{a} \cdot \mathbf{m}'_C)\mathbf{m}'_A \wedge \mathbf{m}'_B$$

Inserting this into the second equation yields

$$0 = \mathbf{m}'_A \wedge \left( ((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) \mathbf{m}'_B − ((\mathbf{b} − \mathbf{a}) \cdot \mathbf{m}'_B) \mathbf{m}'_C \right) \tag{12.15}$$

Given the observed lines **m_B** and **m_C** in their local coordinates, plus the relative poses of the cameras as given by A, B, C, this specifies what **m_A** should be (modulo the usual homogeneous scale factor). This is a linear relationship of two variables **m'_B** and **m'_C** to provide a third: it is a tensor, and we can rewrite it symbolically as a mapping T with two arguments:

$$0 = \mathbf{m}_A \wedge T(\mathbf{m}_B, \mathbf{m}_C)$$

T is called the **trifocal tensor**. One can derive similar trifocal tensors by factoring out **m_B** or **m_C**, so there are three of them in this situation.

Converting this into the more classical coordinate form, we consider everything relative to camera A. This means that we should apply A⁻¹ to the tensor equation. All elements involved are Euclidean direction elements, so they simply transform by R_A⁻¹. Let us abbreviate R_A^B ≡ R_A⁻¹R_B and R_A^C ≡ R_A⁻¹R_C, and the relative position of the cameras B and C in terms of A as **t_B** ≡ R_A⁻¹[**b** − **a**] and **t_C** ≡ R_A⁻¹[**c** − **a**].²

$$0 = \mathbf{m}_A \wedge \left( R_A^B[\mathbf{m}_B] (\mathbf{t}_C \cdot R_A^C[\mathbf{m}_C]) − (R_A^B[\mathbf{m}_B] \cdot \mathbf{t}_B) R_A^C[\mathbf{m}_C] \right)$$

The result is then written in terms of matrix operations on vectors (since that is all you have classically), or in tensor notation. The i-th coordinate of the line **m_A** is proportional to

$$[[\mathbf{m}_A]]_i \propto [[\mathbf{m}_B]]_j \left( [[R_A^B]]_i^j [[\mathbf{t}_C]]_l [[R_A^C]]_l^k − [[R_A^B]]_m^j [[\mathbf{t}_B]]^m [[R_A^C]]_i^k \right) [[\mathbf{m}_C]]_k = [[T]]_i^{jk} [[\mathbf{m}_B]]_j [[\mathbf{m}_C]]_k$$

so that gives the trifocal tensor in tensorial notation (including the usual summation convention over repeated upper and lower index pairs).

> ² In the other literature on multicamera treatments, it is customary to parameterize the rigid body motion inversely (not where the camera frame is in the world frame, but vice versa). Replace our rotations like R with R⁻¹ and **t** with −R⁻¹**t** to get that parameterization. It simplifies the appearance of the final results somewhat, since an R gets absorbed into the new **t** twice.

The trifocal constraint of (12.15) can be used to derive constraints on points as well as lines. For example, if we know the two observed lines **m_B** and **m_C**, and wonder what the constraint might be for a point **x_A** to be the projection of the line Λ, then this follows immediately from the demand that it should lie on the line L_A, which is **x_A** ∧ e₀ ∧ M_A = 0, so **x_A** ∧ M_A = 0. Introducing **x'_A** = A[**x_A**] = **a** + R_A[**x_A**] as the same point in world coordinates, we have **x'_A** · **m_A** = 0, so that the constraint on the point is obtained by taking the inner product of the trifocal constraint with **x'_A**:

$$0 = (\mathbf{x}'_A \cdot \mathbf{m}'_B)((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) − (\mathbf{m}'_B \cdot (\mathbf{b} − \mathbf{a}))(\mathbf{x}'_A \cdot \mathbf{m}'_C)$$

Therefore, **x'_A** lies on the dual line

$$\mathbf{m}'_B ((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) − (\mathbf{m}'_B \cdot (\mathbf{b} − \mathbf{a})) \mathbf{m}'_C$$

Another way of looking at the trifocal tensor is as a line-parameterized homography (i.e., a projective mapping between spaces). Suppose we fix **m_C**; then this determines a spatial plane, which can be used to transfer points in B that are observations from the same world line to points in A (project the ray of observation **x_B** to meet the plane in a point, then observe this point as **x_A**). This mapping can be extended uniquely to the whole image plane as a homography. We can give an explicit formula for this homography between the planes A and B: it should be proportional to the inverse adjoint of the mapping for lines **m_A** and **m_B**, given **m_C**. The adjoint of

$$\mathbf{m} \mapsto ((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) R_B[\mathbf{m}] − ((\mathbf{b} − \mathbf{a}) \cdot R_B[\mathbf{m}]) \mathbf{m}'_C$$

is easily found as

$$\mathbf{x} \mapsto ((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) R_B^{-1}[\mathbf{x}] − (\mathbf{m}'_C \cdot \mathbf{x}) R_B^{-1}[\mathbf{b} − \mathbf{a}]$$

and we take the inverse by simply considering this not as a mapping from **x_B** to **x_A**, but from **x_A** to **x_B**. Therefore the homography between image A and image B is

$$\mathbf{x}_B \propto ((\mathbf{c} − \mathbf{a}) \cdot \mathbf{m}'_C) R_B^A[\mathbf{x}_A] − (\mathbf{m}'_C \cdot \mathbf{x}_A) R_B^A[\mathbf{b} − \mathbf{a}]$$

Similarly, you can derive where a point should be in image A once you have observed it in image B and C, just using the trifocal tensor.

If you therefore have a robotic environment in which you see enough lines for which you are able to do the correspondence in the three images, then you can estimate the trifocal tensor (using techniques from [25]), and employ this to compute other correspondences between the images as well.

---

## 12.3 Further Reading

The impressive book by Faugeras and Luong [21] deals with the geometry of multiple cameras. Like [60], it uses the Grassmann-Cayley algebra of the outer product (which they call join) and its adjoint (which they call meet). This provides a concept of duality, but no metric. The book contains a compact mathematical explanation of this structure, illustrated with geometrical usage. Unfortunately, the authors quickly revert to a matrix-based notation in the chapters that put the structure to practical use, and what could have been explicitly defined algebraic products become tricks in matrix manipulation.

Another modern reference on the geometry of imaging is [25], which dextrously avoids using even Grassmann algebra. All operations are expressed in terms of matrices or tensors defined in terms of Plücker coordinates. The powerful results can therefore be implemented directly, but the geometrical structure of the techniques is often hard to grasp.

We find that both these books have become much more accessible now that geometric algebra offers a structural, representation-independent insight to help one understand what is essentially going on. They can then be browsed quickly for useful techniques.

---

## 12.4 Exercises

### 12.4.1 Structural Exercises

1. Table 12.1 contains the case in which a line {**a**, **m**} is extended to a plane by an additional direction **n** to form the plane [**a** × **n** : **n** · **m**]. Demonstrate the correctness of this formula by representing the spanning L ∧ **n** in terms of the Plücker coordinates.

2. Show that the solution of **x** from the relationship e₀ ∧ **x** = e₀ ∧ x of (12.7) is indeed **x** = e₀⁻¹(e₀ ∧ x), and understand to your satisfaction that this still gives the correct vector **x** for the point x, even when the latter would have been given relative to another origin e'₀ for the homogeneous coordinates.

3. Knowing some of the standard formulas in geometric algebra, you may recognize that the central projection formula (12.9) is not unlike the usual orthogonal projection formula onto a line with direction **a**, which maps **x** to (**x** · **a**)**a**⁻¹. Demonstrate that we can consider the central projection **x** ↦ **x**/(**f**⁻¹ · **x**) as the fixed vector **f** gets inverted, projected onto the variable vector **x**, and then reinverted, to produce **x'**. This interpretation of the formula generalizes to substituting **x** by a line or plane (just replace the inner product with the contraction); it then produces the support vector of the projected line or plane. (Hint: Show that **x'** satisfies: **x'**⁻¹ = (**f**⁻¹ · **x**)**x**⁻¹ = (**f**⁻¹ · **x**⁻¹)**x** and interpret.)

4. Show that the images of all **x** under the construction of the previous exercise before the final inversion (that is, (**f**⁻¹ · **x**)/**x**) lie on a sphere through the pinhole and the end of the vector **f**⁻¹. This is sketched in Figure 12.5 for f = |**f**| = 1. It bears uncanny resemblance to an eyeball!

5. Equation (12.9) gives the projection of a unit 3-D point at location **x** to become a point at location **x'**, which is on the image plane, but it is not expressed yet in image plane coordinates **x̲**. Show that the mapping from the 3-D point at **x** to the image point at **x̲** = **x'** − **f** can be written as:

   $$\mathbf{x} \mapsto \frac{\mathbf{f} (\mathbf{f}^{-1} \wedge \mathbf{x})}{\mathbf{f}^{-1} \cdot \mathbf{x}}$$
   
   Interpret this expression geometrically, especially the numerator.

6. Represent the result of the previous problem in homogeneous coordinates, using the center of the image at **f** as origin. Before you do so, guess the answer!

---

## 12.5 Programming Examples and Exercises

### 12.5.1 Loading Transformations into OpenGL

This example illustrates the good interoperability between homogeneous coordinates-based software (such as OpenGL) and the homogeneous model.

Any outermorphism can be straightforwardly loaded into OpenGL. First, the images of the four basis vectors under the outermorphism are computed, and then the matrix representation of the outermorphism is constructed, whose coordinates are then loaded onto the modelview matrix of OpenGL.

We use a translation-rotation as a simple example. In our OpenGL examples so far, loading this transformation to the modelview matrix would be implemented as:

```cpp
glTranslatef(0.0f, 0.0f, distance); // translate
rotor R = g_modelRotor;
rotorGLMult(R); // rotate (implemented in h3ga_util.cpp)
```

Using the matrix representation of the outermorphism, this becomes:

```cpp
// get the translation vector & the rotor
h3ga::vector T = _vector(distance * e3);
rotor R = g_modelRotor;
rotor Ri = _rotor(inverse(R));

// compute images of basis vectors:
point imageOfE1 = _point(R * e1 * Ri + (T ^ (e0 << (R * e1 * Ri))));
point imageOfE2 = _point(R * e2 * Ri + (T ^ (e0 << (R * e2 * Ri))));
point imageOfE3 = _point(R * e3 * Ri + (T ^ (e0 << (R * e3 * Ri))));
point imageOfE0 = _point(R * e0 * Ri + (T ^ (e0 << (R * e0 * Ri))));

// create matrix representation:
omPoint M(imageOfE1, imageOfE2, imageOfE3, imageOfE0);

// load matrix representation into GL modelview matrix:
glLoadMatrixf(M.m_c);
```

For this simple example, it is of course counterproductive to replace the short OpenGL code with its geometric algebra equivalent: the example is intended to demonstrate the principles only.

### 12.5.2 Transforming Primitives with OpenGL Matrices

This example performs the opposite of the previous example. Instead of setting the OpenGL modelview matrix using the matrix representation of an outermorphism, it reads out the modelview matrix and turns it into a matrix representation of an outermorphism. The actions are as follows:

- The code reads the OpenGL transformation matrix;
- It loads this into a matrix representation of an outermorphism;
- It resets the OpenGL modelview matrix;
- It applies the transform to the primitives, and then draws them.

We can then transform not only points, but also lines and planes, as this example is just the example from Section 11.13.2 with some modifications.

To initialize the matrix representation of the outermorphism, we use:

```cpp
// extract OpenGL modelview matrix
float MVM[16];
glMatrixMode(GL_MODELVIEW);
glGetFloatv(GL_MODELVIEW_MATRIX, MVM);

// reset OpenGL modelview matrix (we will apply the transform ourselves)
glLoadIdentity();

// initialize the images of the basis vectors:
point images[4];
for (int i = 0; i < 4; i++) {
    images[i].set(point_e1_e2_e3_e0, &(MVM[i * 4]));
    /* or:
    images[i].set(point_e1_e2_e3_e0,
        MVM[i * 4 + 0],
        MVM[i * 4 + 1],
        MVM[i * 4 + 2],
        MVM[i * 4 + 3]);
    */
}

// initialized matrix representation of outer morphism
om M(images);
```

To draw any primitive (point, lines, plane):

```cpp
void applyTransformAndDraw(const om &M, const mv &X) {
    // apply the outermorphism:
    mv MX = apply_om(M, X);
    draw(MX);
}
```

The actual code is slightly more complicated due to the use of a custom probing point; see the GA sandbox source code package.

In the graphics, there is a somewhat undesirable side effect due to the explicit use of a basis in a factorization algorithm that is used to draw the plane. It is best observed by starting the example and rotating the scene (drag the left mouse button along the edges of the viewport). You will notice that edges of the depicted plane stay in place while the rest of the scene rotates. This feels counterintuitive (compare this to Example 11.13.2 where the edges do rotate).

The cause of this is the following. To draw the plane, we need two vectors that span it. We obtain these by factorization, using the (basis-dependent) algorithm described in Section 21.6. In the original example (Section 11.13.2), we factor the plane, transform the factors, and then draw the plane using the rotated factors. Then the plane rotates visibly, because its vector factors do. In the present example, we first rotate the plane, then factor it, and then draw the rotated plane using its factors. When the rotation plane is the same as the plane itself, the rendering of the plane will not change at all. Intuitively, the former is better, but algebraically, the latter result is more correct, for it shows the true behavior of a plane under rotation.

### 12.5.3 Marker Reconstruction in Optical Motion Capture

In Section 10.7.3 we implemented an algorithm for external camera calibration. That algorithm computed the position and orientation of any number of cameras. The current example builds upon that earlier example by using the calibrated cameras to perform measurements of the position of markers. We use the homogeneous model to reconstruct 3-D markers from actual capture data.

The markers are little spheres (size from 0.5–3.0 cm) wrapped in retroreflective tape. Every time the camera records an image (between 20 to 500 times per second), an LED ring around the camera lens illuminates the scene, and the markers reflect this light back to the camera sensor. With proper exposure time (our system typically uses between 0.2 and 1ms), the result is that the markers are visible as bright blobs in the otherwise black images. The centers of the 2-D markers are easily retrieved from the images, since the center of a projected sphere is a good approximation to the projection of the center of that sphere when the markers are sufficiently far away.

When a marker is visible from multiple calibrated cameras, its position can be reconstructed by computing the intersection point of rays from the camera centers through the marker center. Markers can of course be occluded by the subject to which they are attached, so not all cameras can see every marker all the time. The more cameras that actually see a particular marker, the more precise the reconstruction can be. The simplistic marker reconstruction algorithm used in this example reconstructs the markers as follows: we iterate over every pair of 2-D markers from two different cameras. For each pair, we perform the following actions:

- First, we construct a plane through the two camera centers and the 2-D marker in the image plane of one camera. This plane is then intersected with the image plane of the other camera to compute the epipolar line:

```cpp
// normalizedPoints P1, P2 are the camera positions.
// normalizedPoint M1 is the marker position, on image plane of
// camera 1.
// plane IP2 is the image plane of camera 2.
// compute the epipolar line in the image plane of camera 2:
line L2 = _line(unit_r(dual(P1 ^ M1 ^ P2) << IP2));
```

- Once we have the epipolar line, we search for 2-D markers sufficiently close to it (as the data is inherently noisy, we will rarely have a precise intersection of the epipolar line with a marker). We compute the distance of each candidate marker as (M2*)⌋L2:

```cpp
// normalizedPoint M2 is the marker position, on image plane of
// camera 2
// compute distance in image plane:
mv::Float distance = fabs(_Float((M2 << IP2) << L2));
```

The dual is of course taken relative to the image plane of the second camera.

- If the distance is less than some epsilon value, we reconstruct a 3-D marker by computing the average of the closest points on the two lines P1 ∧ M1 and P2 ∧ M2. We collect all reconstructed points in an array. How these points are computed is described below.

After this loop, we iterate over all pairs of reconstructed 3-D markers to find the ones that are sufficiently close in 3-D space (where close is typically defined as within the distance of the radius of the marker). We merge close markers by summing them. We do not normalize the points, as we use the e₀ coordinates as rough counters for how many cameras contributed to a particular reconstruction. We return only those markers that have been seen by a sufficient number of cameras:

```cpp
/*
R is the array of reconstructed 3D markers (candidates).
'reconstructedMarkers' is the final array of 3D markers
(normalizedPoints) that is returned to the caller.
*/
if ((int)R[i].e0() >= minNbCameras) {
    reconstructedMarkers.push_back(_normalizedPoint(R[i] /
        R[i].e0()));
}
```

When you read the full source code of the example in the GA sandbox source code package, you may encounter some use of the conformal model of the later chapters. Our actual motion capture system is based primarily on the conformal model, hence this example (which was derived from it to illustrate homogeneous model techniques) stores the camera transformations as conformal versors.

A more refined reconstruction algorithm would use some kind of data structure to quickly look up points close to particular epipolar lines. For each successful match in two cameras, an initial 3-D marker is then reconstructed. These 3-D markers can subsequently be projected onto the image planes of the other cameras, after which another data structure (e.g., a spatial hashing table) can be used to quickly find markers in the vicinity of the projected points. A least-squares-based solution (see Section 10.4.2) would then be used to find the optimal reconstruction of the 3-D marker given the 2-D measurements in each camera.

#### Computing Closest Points on Lines

Computing the closest points on two skew lines is an important operation that is performed in the inner loop of by the reconstruction algorithm. We provide an efficient geometric algebra implementation below. The two lines are passed in factored form (i.e., as points and directions such that the actual lines are P1 ∧ D1 and P2 ∧ D2).

```cpp
bool closestPointsOnCrossingLines(
    const normalizedPoint &P1, const h3ga::vector &D1,
    const normalizedPoint &P2, const h3ga::vector &D2,
    mv::Float &d1, mv::Float &d2) {
    // Compute difference between starting points
    h3ga::vector dif = _vector(P2 - P1);
    
    // compute inverse pseudoscalar of space spanned by D1 and D2
    bivector I = _bivector(D1 ^ D2);
    if (_Float(norm_e2(I)) == 0.0f) // check parallel
        return true; // returning true means 'lines are parallel'
    bivector Ii = _bivector(inverse(I));
    
    // compute reciprocals:
    h3ga::vector rD1 = _vector(D2 << Ii);
    h3ga::vector rD2 = _vector(D1 << Ii);
    
    // solution:
    d1 = _Float(rD1 << dif);
    d2 = _Float(rD2 << dif);
    
    return false;
}
```

The function returns scalars d1 and d2 such that P1 + d1 * D1 and P2 + d2 * D2 are the closest points on the two lines.

The function works by projecting the vector P2 — P1 onto the bivector D1 ∧ D2. The geometric intuition behind this is that we are trying to minimize the distance P2 — P1 between the two points by moving along the lines. d1 and d2 are the coordinates of the projected vector relative to the basis spanned by D1 and D2. Because D1 and D2 are not orthonormal, we need to compute their reciprocals (rD1 and rD2) first.
