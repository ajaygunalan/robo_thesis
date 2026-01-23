# Chapter 10: The Vector Space Model: The Algebra of Directions

When we developed geometric algebra in the first part of this book, we illustrated the principles with pictures in which vectors are represented as arrows at the origin, bivectors as area elements at the origin, and so on. This is the purest way to show the geometric properties corresponding to the algebra.

The examples showed that you can already use this algebra of the mathematical vector space ℝⁿ to model useful aspects of Euclidean geometry, for it is the algebra of directions of n-dimensional Euclidean space. We explore some more properties of this model in this chapter, with special emphasis on computations with directions in 2-D and 3-D. Most topics are illustrated with programming exercises at the end of the chapter.

First we show how the vector space model can be used to derive fundamental results in the mathematics of angular relationships. We give the basic laws of trigonometry in the plane and in space, and show how rotors can be used to label and classify the crystallographic point groups.

Then we compute with 3-D rotations in their rotor representation, establishing some straightforward techniques to construct a rotor from a given geometrical situation, either deterministically or in an optimal estimation procedure. The logarithm of a 3-D rotor enables us to interpolate rotations.

Finally, we give an application to external camera calibration, to show how the vector space model can mix directional and locational aspects.

---

## 10.1 The Natural Model for Directions

There are n independent 1-D directions in an n-dimensional physical space, and they can conveniently be drawn as vectors at the origin. Mathematically, they form a vector space ℝⁿ, for they can be added and scaled with real numbers to produce other legitimate 1-D directions. The metric of the directions in the physical space (typically Euclidean) can be used to induce a metric in this mathematical representation. That gives a model of the directions in physical space in terms of the geometric algebra of a metric vector space ℝⁿ.

The vector space model thus constructed is indeed a good computational representation of spatial directions at the origin. We have used it in all our illustrations of the geometrical properties of geometric algebra in Part I. This already gave a list of powerful abilities, directly applicable to computations with directions. We list the main results.

- The k-dimensional directions in n-dimensional space can be composed as outer products of k 1-D directions (represented as vectors). These k-blades can be decomposed on an $\binom{n}{k}$-dimensional basis. Only for grades 0, 1, (n−1), and n can k-blades be constructed by arbitrary addition of basis elements.

- Directions have an attitude, a weight, and an orientation.

- Relative angles between k-dimensional directions can be computed using the contraction, even when they are of different grades. A k-direction can be represented by its dual, the direction of its orthogonal complement.

- Intersection and union of k-directions is defined by meet and join, which are a specific combination of outer product and duality. The orthogonal projection of k-directions is also well defined by the contraction.

- Directions can be used to reflect other directions using sandwiching products (where some care is required to process their orientation properly).

- Directions can be rotated using rotors and multiplied by the geometric product to produce such rotors.

Beyond these structural properties, true for the abstract directions of a general vector space ℝⁿ, we need specific techniques to use the blades of the vector space model to solve particular geometrical problems, notably in the Euclidean spaces ℝ² and ℝ³.

---

## 10.2 Angular Relationships

The vector space model is the natural model to treat angular relationships at a single location. To show this, we derive the elementary laws of sines and cosines in a planar triangle; some similar relationships in a spherical triangle; and the point groups of crystallography. The results are not new, but intended as examples of how you can now think about such problems in a purely directional manner using geometric algebra. Especially the ability to divide and multiply vectors will simplify both the computations and the definition of the oriented angular parameters in the configurations.

### 10.2.1 The Geometry of Planar Triangles

The combination of rotors in the same plane is sufficient to derive the various relationships between sides and angles in triangles. We repeat the derivation of these laws as given in [29], pp. 68–70, since this application shows the simplicity and power of geometric algebra nicely. Quantities that are required to characterize the properties are completely definable in terms of the original elements of the problem.

In Figure 10.1(a) we have indicated a triangle in the 2-D Euclidean I-plane, composed of three vectors **a**, **b**, **c** that have the relationship

$$\mathbf{a} + \mathbf{b} + \mathbf{c} = 0 \tag{10.1}$$

These vectors indicate weighted directions, and their weights can be drawn as their lengths. Although they have been drawn offset from the origin, there are no actual positional aspects to this triangle and its relationships. This is shown by redrawing all vectors involved as emanating from the origin, in a purist version of the triangle, as Figure 10.1(b). The relevant geometric algebra of both figures is the same.

> **Figure 10.1:** A triangle **a** + **b** + **c** = 0 in a directed plane I, and an equivalent configuration for treatment with the vector space model.

Solving this equation **a** + **b** + **c** = 0 for **c**, and squaring, we get

$$\mathbf{c}^2 = (\mathbf{a} + \mathbf{b})^2 = \mathbf{a}^2 + \mathbf{b}^2 + \mathbf{ab} + \mathbf{ba} = \mathbf{a}^2 + \mathbf{b}^2 + 2\mathbf{a} \cdot \mathbf{b} \tag{10.2}$$

We may introduce the angle α between **c** and −**b** (in that order), and similarly β and γ (see Figure 10.1), and we can introduce the lengths of the sides a, b, and c. The picture defines what is meant, but in geometric algebra we would rather define those elements unambiguously as properties of the geometric ratios of the original vectors. Section 6.1.6 gives the principle. Carefully observing the required angles and signs leads to the exact definitions:

$$-\mathbf{b}/\mathbf{a} \equiv \frac{b}{a} e^{I\gamma}, \quad -\mathbf{c}/\mathbf{b} \equiv \frac{c}{b} e^{I\alpha}, \quad -\mathbf{a}/\mathbf{c} \equiv \frac{a}{c} e^{I\beta} \tag{10.3}$$

Daring to make such definitions is a skill that you should master, for it is the transition from the classical methods of thinking about angles (with the associated headaches on the choice of signs) to the automated computations of geometric algebra. Make sure you understand the precise relationship between these definitions and the figure they represent!

When combined with the basic property (10.1), the angle definitions (10.3) fully define all relationships in the triangle. It just takes geometrically inspired algebraic manipulation to bring them out. For instance, we can multiply these equations. Remembering that exponentials of commuting arguments are additive, we obtain by (10.3)

$$e^{I(\alpha+\beta+\gamma)} = e^{I\alpha}e^{I\gamma}e^{I\beta} = (-\mathbf{c}/\mathbf{b})(-\mathbf{b}/\mathbf{a})(-\mathbf{a}/\mathbf{c}) = -1 = e^{I\pi} \tag{10.4}$$

This implies that

$$\alpha + \beta + \gamma = \pi \mod (2\pi) \tag{10.5}$$

which is a rather familiar result.

To obtain other classics, we split the geometric product in a contraction and an outer product, thereby separating the equations into their scalar and bivector parts. This automatically introduces the trigonometric functions as components of the rotors.

We multiply both sides of (10.3) by a², and so on, and obtain six equations:

$$-\mathbf{b} \cdot \mathbf{a} = ba \cos \gamma, \quad -\mathbf{b} \wedge \mathbf{a} = ba \, I \sin \gamma$$

$$-\mathbf{c} \cdot \mathbf{b} = cb \cos \alpha, \quad -\mathbf{c} \wedge \mathbf{b} = cb \, I \sin \alpha$$

$$-\mathbf{a} \cdot \mathbf{c} = ac \cos \beta, \quad -\mathbf{a} \wedge \mathbf{c} = ac \, I \sin \beta$$

Then the earlier results can be put into the classical form. Equation (10.2) is the **law of cosines**:

$$c^2 = a^2 + b^2 - 2ab \cos \gamma \tag{10.6}$$

Taking the outer product of (10.1) with **a**, **b**, and **c**, we obtain

$$\mathbf{a} \wedge \mathbf{b} = \mathbf{b} \wedge \mathbf{c} = \mathbf{c} \wedge \mathbf{a} \tag{10.7}$$

which leads to the **law of sines** in the I-plane:

$$\frac{\sin \alpha}{a} = \frac{\sin \beta}{b} = \frac{\sin \gamma}{c} \tag{10.8}$$

We have divided out the plane I in which this holds to achieve this classical form. But in fact, (10.7) is more specific and is valid in any plane I in n-dimensional space.

In the classical formulation, the area of the triangle is ½ab sin γ (or a similar expression). We see that in the directed plane I, we can define the **oriented area** Δ of the triangle naturally by the equivalent ratios

$$\Delta = \frac{\mathbf{a} \wedge \mathbf{b}}{2I} = \frac{\mathbf{b} \wedge \mathbf{c}}{2I} = \frac{\mathbf{c} \wedge \mathbf{a}}{2I} \tag{10.9}$$

This is a proper geometric quantity that relates the area to the orientation of the plane it is measured in.

### 10.2.2 Angular Relationships in 3-D

In a 3-D Euclidean space, geometrical directions can be indicated by vectors or bivectors (which are always 2-blades). The scalars and trivectors have trivial directional aspects and are mostly used for their orientations and magnitudes.

Relative angles between the directional elements are fully represented by their geometric ratios. Let us consider only unit elements, so that we can fully focus on the angles. Between two unit directional elements, there are three possibilities:

- **Two Vectors.** The geometric ratio of two unit vectors **u** and **v** is a rotor R = **v**/**u**. It contains in its components both the rotation plane I and the relative angle φ of the two vectors. These can be retrieved from the rotor as the bivector angle Iφ, using the logarithm function defined below in Section 10.3.3. Note that only the product of plane and angle is a well-defined geometric quantity, since each separately has an ambiguity of magnitude and orientation. In that sense, scalar angles are ungeometrical and should be avoided in computations, since they necessitate the nongeometrical choice of standard orientation for the I-plane. Since you probably only need the angles to use them in a rotation operator anyway, you may as well keep their bivector with their magnitude as a single bivector angle.

- **Two Bivectors (2-Blades).** The geometric ratio of two unit 2-blades U and V also defines a rotor R = V/U. This is most easily seen by introducing their normal vectors **u** ≡ U* = U/I₃ and **v** ≡ V* = V/I₃. Substituting gives R = V/U = **v**/**u**. Therefore, this reduces to the previous case. The bivector angle between two bivectors is automatically measured in a plane perpendicular to the common line of the two planes, and this plane and the angle are found as the bivector angle log(V/U).

- **Vector and Bivector (2-Blade).** When we have a unit bivector U and a unit vector **v**, we previously defined the cosine of their angle through the contraction, as in Figure 3.2(b). With the geometric product, we can proceed slightly differently, defining the full bivector angle. We try to determine a unit vector **w** in the plane U and perpendicular to **v**, such that it can rotate **v** into the plane over an angle α as **v**e^(**w**I₃α), after which that rotated version of **v** and **w** together span U. The sketch of Figure 10.2 shows that this mouthful is the algebraic demand

$$\mathbf{U} = \mathbf{v} e^{\mathbf{w}I_3\alpha} \mathbf{w}$$

This fully determines both **w** and α as aspects of the geometric product **v**U. It is simplest to make a rotor out of the element **v**U by undualization to show its bivector:

$$\mathbf{v}\mathbf{U}I_3 = e^{\mathbf{w}I_3\alpha} \mathbf{w}I_3 = e^{\mathbf{w}I_3 (\pi/2+\alpha)}$$

Taking the logarithm retrieves this bivector, which gives all parameters in one operation (though it is a pity not to get the actual bivector angle α**w**I₃).

> **Figure 10.2:** The angle between a vector and a bivector (see text).

Angular relationships between three directions can also be defined. They are much more involved, because there are various standard ways of characterizing the parameters of the spherical triangle, as depicted in Figure 10.3. These are its vertices (represented by three vectors), its sides (the angles between the vectors), its angles (the angles between the bivectors containing its sides), and its altitudes (angle between vector and plane bivector). The various combinations of these quantities provide the laws of spherical geometry. Geometric algebra again permits compact and computationally complete specification of the relationships.

> **Figure 10.3:** A spherical triangle and its characterizing parameters.

The bivectors containing the vertices can be defined through

$$\check{\mathbf{a}}/\check{\mathbf{b}} \equiv e^{\mathbf{C}}, \quad \check{\mathbf{b}}/\check{\mathbf{c}} \equiv e^{\mathbf{A}}, \quad \check{\mathbf{c}}/\check{\mathbf{a}} \equiv e^{\mathbf{B}} \tag{10.10}$$

where $\check{\mathbf{a}}$, $\check{\mathbf{b}}$, $\check{\mathbf{c}}$ are the unit vectors pointing at the vertices of the spherical triangle. The weights A, B, C of the bivectors **A**, **B**, **C** are the edge lengths, measured as angles on the unit sphere. The bivectors can be used to define the angles of the spherical triangle, through

$$\check{\mathbf{B}}/\check{\mathbf{A}} \equiv -e^{I_3 c}, \quad \check{\mathbf{C}}/\check{\mathbf{B}} \equiv -e^{I_3 a}, \quad \check{\mathbf{A}}/\check{\mathbf{C}} \equiv -e^{I_3 b} \tag{10.11}$$

with $\check{\mathbf{A}}$, $\check{\mathbf{B}}$, $\check{\mathbf{C}}$ now denoting the unit bivectors and I₃ the unit pseudoscalar of ℝ³·⁰. The weights of the vectors **a**, **b**, **c** thus defined are the internal angles a, b, c of the spherical triangle in Figure 10.3.

Multiplication of the unit vector expressions leads to

$$e^{\mathbf{A}} e^{\mathbf{B}} e^{\mathbf{C}} = 1$$

and multiplication of the unit bivector expressions gives

$$e^{I_3 c} e^{I_3 b} e^{I_3 a} = -1$$

We have met the former in the guise of the multiplication of rotors in Section 7.3.4. That should give you the confidence that these expressions can indeed lead to the correct expressions for sine and cosine formulas, when split in their different grades. To be specific, you can work out that the scalar part of the unit vector expression gives the identity

$$\cos C = \cos A \cos B + \sin A \sin B \cos c$$

known as the **cosine law for sides**. The minus sign in the bivector expression leads to subtle differences between the laws for the sides and for the angles. The scalar part is now

$$\cos c = -\cos a \cos b + \sin a \sin b \cos C$$

which is known as the **cosine law for angles**.

For the full details on these and other laws of spherical trigonometry, we refer to Appendix A of [29], highly recommended reading for anybody using spherical trigonometry. When we get more versed in geometric algebra, we should probably not reduce the geometry of these spherical triangles to the set of classical scalar relationships, learning instead to compute directly with the rotors, vectors, and bivectors involved.

### 10.2.3 Rotation Groups and Crystallography

A famous old puzzle in the mathematics of physics has been the classification of crystallographic groups: how many ways are there to make crystals in space? This is clearly a geometric problem, and one would hope that geometric algebra could help out. The vector space model, which provides the algebra of directions, can be used to solve a subproblem: how can one select the local symmetry of reflections and rotations to combine well, in the sense that multiple reflections and rotations generate only a finite number of elements? Such a set of operators is called a **point group**.

We use a unit vector **a** (with a² = 1) to denote a local plane of reflection. When used as the normal vector of this plane, it generates the reflection of a vector **x** as −**axa**. This transformation is insensitive to the sign of **a**. However, we can in principle distinguish the planes **a** and −**a** by their orientation, and for accurate classification of the point groups we should use such oriented planes.

In a 3-D crystal, there are several symmetry planes for reflection. In the algebra, they are each denoted by their vector versors. As the reflections combine as operators, new symmetries appear as the products of these versors. To form a crystal, the combined set of operators should form a finite set, so that a single point (atom) transformed by all operators of the crystal is only equivalent to a finite number of other atoms around the same point.

An even number of reflections generates a rotation, which is represented by the geometric product of the corresponding normal vectors to give an operator like R ≡ **ab**. A six-fold symmetry at the local point implies that applying the rotation operator **x** → R**x**R̃ six times gives back the original **x**. Two possible conditions would satisfy this demand: R⁶ = 1 and R⁶ = −1. The latter is more specific, and uses the possibility of geometric algebra to represent oriented rotations (see also Section 7.2.3). Since we need to reflect other operators (not just points), we use the −1. That gives the most accurate classification of the symmetries of the crystal. In general, R²ᵖ = 1 for a p-fold symmetry.

To use a particular example in 2-D, suppose we have two generating vectors **a** and **b** representing reflecting planes. These induce symmetries in the plane. To be a four-fold symmetry, we have the three demands:

$$\mathbf{a}^4 = 1, \quad \mathbf{b}^4 = 1, \quad (\mathbf{ab})^8 = 1$$

Clearly the generating vectors of this point group should be unit vectors with a relative angle of π/4 to satisfy these demands. The rotation and reflection operators that are possible by the combinations of these vectors are listed in Table 10.1. There are 16 symmetry operators, which together form the group ²H₄ of [30]. Each of these elements is a local symmetry Vᵢ of the crystal. If you start with a single location vector **x** and generate all elements **xᵢ** = Vᵢ**x**Vᵢ⁻¹, you find 8 equivalent locations for atoms in the symmetry group of this crystal. This is demonstrated in the programming example in Section 10.7.2.

**Table 10.1:** The operators of the point group ²H₄, with defining relations a⁴ = b⁴ = (ab)⁸ = 1. The terms positive and negative are relative (but consistent), and based on the ordering of **a** and **b**. These generate the symmetries of the crystal.

| Positive Rotations | Negative Rotations | Positive Reflections | Negative Reflections |
|---|---|---|---|
| 1 | −1 | **a** | −**a** |
| **ab** | −**ab** | **aba** | −**aba** |
| (**ab**)² | (**ba**)² | −**bab** | **bab** |
| −**ba** | **ba** | −**b** | **b** |

The defining relations on two vectors is sufficient to determine all points groups in 2-D. In 3-D, three generating vectors are required. If we have the demands in the form

$$(\mathbf{ab})^{2p} = (\mathbf{bc})^{2q} = (\mathbf{ca})^{2r} = 1$$

then the rotors generated by this can be written as

$$(\mathbf{ab}) = e^{I\mathbf{c}\pi/p}, \quad (\mathbf{bc}) = e^{I\mathbf{a}\pi/q}, \quad (\mathbf{ca}) = e^{I\mathbf{b}\pi/r}$$

in which I is the pseudoscalar of the 3-D space, and **a** and so on are the poles (unit axes) of the rotations. Careful analysis performed by Coxeter (in a different, non-GA representation) reveals that a necessary condition for finitely representable solutions is:

$$\frac{1}{p} + \frac{1}{q} + \frac{1}{r} > 1$$

The integer solutions to this equation then generate the point groups in 3-D space. The complete classification may be found in [30].

Geometric algebra thus classifies the groups by sets of vectors in relative positions; these not only represent the reflection planes (which is how more classical solutions also characterize the symmetry), but they can immediately be used to generate the operators that perform all the operations in the group simply by the geometric product.

The extension to crystallographic groups imposes the additional condition that the point groups should remain closed under translation. We cannot treat those with the same simplicity within the vector space model. Our reference [30] develops the crystallographic groups further, using the conformal model described in Chapter 13 to include translations with the same ease.

---

## 10.3 Computing with 3-D Rotors

The Euclidean space ℝ³·⁰ is a structural model of orientations in 3-D. In this model, rotations are represented by rotors. Those are structure-preserving and easily interpolated. We have already treated many of their structural properties when we introduced them in the general setting of n-dimensional algebras. Even though they did not then necessarily represent 3-D rotations, those provided a good and immediate illustration. We revisit and extend that material to provide the practical tools for 3-D rotors: how to find them from frames, how to determine their bivectors, and how to interpolate them.

### 10.3.1 Determining a Rotor from a Rotation Plane and an Angle

The most natural way to find a rotor in any geometrical problem is to know the rotation plane represented by the 2-blade I and the desired rotation angle φ (measured to be positive in the orientation of I). Their product gives the geometric quantity Iφ, which does not depend on the choice of the orientation of the plane. We called this the **bivector angle** in Section 7.2.2 (that is actually a misnomer in more than three dimensions, where it should then more properly be called a 2-blade angle, but that is rather a mouthful). The rotor in terms of the bivector angle is

$$R = e^{-I\phi/2}$$

We have seen how this is essentially a quaternion in Section 7.3.5, and in the programming exercise of Sections 7.10.3 and 7.10.4 showed how to convert between rotation matrices, quaternions, and rotors. In Section 7.3.4, we gave a pleasant visualization of the composition of rotations as the addition of half-angle arcs on a unit sphere.

If you have been able to determine the cosine c of the rotation angle in some way (for instance, through a scalar product), you can use this fairly directly to determine the rotor as

$$R = \sqrt{(1 + c)/2} - \sqrt{(1 - c)/2} \, I \tag{10.12}$$

The square roots are expressions of the cosine and sine of the half angle in terms of the cosine. When you take the standard positive values of the square roots, the orientation of I denotes the direction of rotation.

### 10.3.2 Determining a Rotor from a Frame Rotation in 3-D

A rotor can be found when you know how enough vectors rotate. In any number of dimensions, there is a cheap way to make the unique rotor turning unit vector **a** to unit vector **b** in their common plane. This of course involves the half angle between them, which may seem expensive to compute. However, a unit vector in that half-angle direction is easily found by adding the vectors **a** and **b** and normalizing. The rotor is then the geometric ratio of this vector with **a**. That gives

$$R = \frac{1 + \mathbf{ba}}{\sqrt{2(1 + \mathbf{a} \cdot \mathbf{b})}} \tag{10.13}$$

You should realize that this is one of many rotations that can turn **a** into **b**. It is the simplest in the sense that it only involves their common plane. The formula is unstable when **a** and **b** are close to opposite; when they are truly opposite, there is no unique rotation plane to turn one into the other.

In general, you would need to know the image of several vectors before you can determine the exact relative rotor. In 3-D Euclidean space, there is a compact formula to retrieve the rotor from the three vectors of a frame {**eᵢ**} (which does not even have to be orthogonal) and their images {**fᵢ**}. It is

$$R \sim 1 + \sum_{i=1}^{3} \mathbf{f}^i \mathbf{e}_i$$

which needs to be properly scaled to become a rotor (for which of course R R̃ = 1). Note that it uses the reciprocal frame of the vectors **fᵢ** (see Section 3.8). It does not give the correct result for rotations over π (returning zero instead), and is unstable near rotations close to π. These consequences were already explored in the programming exercise of Section 7.10.3.

We give a rather advanced derivation of this formula, invoking vector derivatives. The only reason for doing this is to show the general n-dimensional pattern, should you ever need it, before we home in on the 3-D-only case.

$$\mathbf{f}^i \mathbf{e}_i = R \mathbf{e}^i \tilde{R} \mathbf{e}_i$$
$$= R \partial_\mathbf{a} (\tilde{R} \mathbf{a})$$
$$= n - 2R \left( \langle \tilde{R} \rangle_0 + \langle \tilde{R} \rangle_2 + \langle \tilde{R} \rangle_4 + \cdots \right)$$
$$\stackrel{3D}{=} 3 - 4 R \langle \tilde{R} \rangle_2$$
$$= 3 - 4 R (R - \langle R \rangle_0)$$
$$= 4 \langle R \rangle_0 R - 1$$

and the result follows, since this shows that R is proportional to 1 + Σᵢ **fⁱeᵢ** in 3-D.

### 10.3.3 The Logarithm of a 3-D Rotor

As we saw in Section 7.4.3, general rotors are the exponentials of bivectors. In the 3-D vector space model of ℝ³·⁰, it is fairly straightforward to retrieve that bivector from the rotor. In such a 3-D space, the rotors are exponentials of 2-blades, since all bivectors are 2-blades in 3-D.

An explicit principal logarithm (as explained in Section 7.4.4) is easy to give for a rotor R = exp(−Iφ/2). It can be determined by writing out the expression for the rotor in its grades and reassembling those using standard trigonometric functions on the grade parts:

$$-I\phi/2 = \log(R)$$
$$= \log \exp(-I\phi/2)$$
$$= \log \left( \cos(\phi/2) - I \sin(\phi/2) \right)$$
$$= \frac{\langle R \rangle_2}{\|\langle R \rangle_2\|} \arctan \left( \frac{\|\langle R \rangle_2\|}{\langle R \rangle_0} \right) \tag{10.14}$$

There are some special cases that should be borne in mind. Obviously, when the scalar ⟨R⟩₀ equals zero, the division in the atan is ill-defined, even though there is still a well-defined rotation plane, and therefore a well-defined logarithm. In an implementation, you should use the `atan2` function to provide numerical stability and additionally make (10.14) valid for the second and third quadrant. In two other cases, namely when the rotor equals 1 or −1, the rotation plane is ambiguous. For the identity rotation, the small angle makes the behavior around R = 1 still numerically stable, and the logarithm is virtually zero. But the ambiguity at R = −1 cannot be resolved without making arbitrary choices. These cases are recognizable in the pseudocode of Figure 13.5 (where the rotation logarithm is presented as part of the logarithm of the general rigid body motion).

This formula (10.14) can be extended from a rotor to a nonunit versor; there is then an additional term of log(‖R‖).

### 10.3.4 Rotation Interpolation

When you want to interpolate between two known orientations, you can do this by dividing the rotor between the extreme poses in equal amounts. This requires being able to take the nth root of a rotor through using its logarithm. For the Euclidean rotors in the 3-D vector space model of ℝ³·⁰, this can be done explicitly.

Let us suppose we know the initial and final rotor in the interpolation sequence as R₁ and R₂, respectively. Then the total rotation that needs to be performed is characterized by the rotor R ≡ R₂/R₁. To perform this total rotation in n steps, one needs to apply the rotor r ≡ R^(1/n), n times. In the geometric algebra formulation, this is simply

$$R = R_2/R_1 = e^{-I\phi/2} \quad \Rightarrow \quad r = e^{-I\phi/(2n)} = e^{\log(R)/n}$$

This formula requires the bivector corresponding to the rotor, which we derived in (10.14) as its principal logarithm. The rotor that needs to be applied to the original element after k applications is rᵏR₁, and of course we should have rⁿR₁ = R₂. That gives the simple program of programming exercise 10.7.1. See also Figure 10.4.

> **Figure 10.4:** The interpolation of rotations illustrated on a bivector **X**. The poses R₁[**X**] and R₂[**X**] are interpolated by performing the rotor R₂/R₁ in eight equal steps.

An alternative is to give the resulting rotor not in multiplicative form, but to use the trigonometric functions to give a closed expression of the interpolation going on between R₁ and R₂. This is the way it is found in the quaternion literature, where this is known as **slerp interpolation** (for spherical-linear interpolation). To derive the formula, note that the requirement R₂/R₁ = cos(φ/2) − I sin(φ/2) gives IR₁ = (R₂ − R₁ cos(φ/2))/sin(φ/2). Then the linear interpolation is achieved by rotation over a fraction λφ/2 of the angle, from R₁ towards R₂. This is the rotor e^(−λIφ/2)R₁, which may be expressed as

$$R_\lambda = \cos(\lambda\phi/2) - I\sin(\lambda\phi/2) R_1$$
$$= \frac{R_1 \sin(\phi/2) \cos(\lambda\phi/2) - R_1 \cos(\phi/2) \sin(\lambda\phi/2) + R_2 \sin(\lambda\phi/2)}{\sin(\phi/2)}$$
$$= \frac{\sin((1 - \lambda)\phi/2)}{\sin(\phi/2)} R_1 + \frac{\sin(\lambda\phi/2)}{\sin(\phi/2)} R_2 \tag{10.15}$$

This is the linear interpolation formula for rotations (see [56]). It is valid in n-dimensional space.

In our software, we prefer not to use this explicit form, but instead the structurally simpler formulation in terms of the incremental rotor r. In the bivector formulation, one can easily design more sophisticated interpolation algorithms that interpolate between several rotors, such as bivector splines.

---

## 10.4 Application: Estimation in the Vector Space Model

For applications in synthetically generated computer graphics, the generative techniques for rotations suffice, but in the analytical fields of computer vision and robotics you need to determine rotations based on noisy data.

### 10.4.1 Noisy Rotor Estimation

If your data is noisy, you should of course not establish the rotation based on three frame vectors as in Section 10.3.2, but instead use a rotor estimation technique. You could try to use the frame estimation on triplets of rotors and average their bivectors, but it is better to do a proper estimation minimizing a well-defined cost function.

We encountered such a technique in Section 8.7.2, when we used the rotation estimation problem to give an example of multivector differentiation. Its outcome is a useful result that you can easily implement even without understanding the details of its derivation.

### 10.4.2 External Camera Calibration

When you have a set of cameras of unknown relative positions and attitudes observing one scene, you can only integrate their views if you have calibrated the setup (i.e., estimated the parameters of their relative geometry). You can collect the data for such a calibration by moving a spherical marker around in the scene and synchronizing the cameras to record their various views of it at the corresponding times, as illustrated in Figure 10.7. The observed data is of course inherently noisy, and you need to do some processing to determine the "best" estimate for their relative poses. We describe an algorithm for this, taken from [38], culminating in the programming exercise of Section 10.7.3. Our source assumes that the cameras have been calibrated internally. This involves a determination of the parameters of their optics and internal geometry, so that we can interpret a pixel in an image as coming from a well-determined spatial direction relative to its optical axis. Geometrically, it turns the camera into a measurement instrument for spatial directions.

Let us consider M + 1 cameras. We arbitrarily take one of them as our reference camera number 0, and characterize the location of the optical center of camera j relative to the center of camera 0 by the translation vector **tⱼ** and its orientation by the rotor Rⱼ. We mostly follow the notation of [38] for easy reference, which uses bold capitals for vectors in the world, and lowercase for vectors within the cameras. We will simplify the situation by assuming that the marker is visible in all cameras at all times (our reference deals with occlusions; this is not hard but leads to extra administration).

The marker is shown N times at different locations **Xᵢ** in the real world. Relative to camera j, it is seen at the location **Xᵢⱼ** given implicitly by

$$\mathbf{X}_i = \mathbf{t}_j + R_j \mathbf{X}_{ij} \tilde{R}_j$$

However, all that camera j can do is register that it sees the center of the marker in its image, and (using the internal calibration) know that it should be somewhere along the ray in direction **xᵢⱼ** from its optical center. The scaling factor along this ray is σᵢⱼ; if we would know its value, the camera would be a 3-D sensor that would measure σᵢⱼ**xᵢⱼ** = **Xᵢⱼ**, and then Rⱼ and **tⱼ** could be used to compute the true location of the measured points. But the only data we have are the **xᵢⱼ** for all the cameras. All other parameters must be estimated. This is the **external calibration problem**.

The estimation of all parameters is done well when the reconstructed 3-D points are not too different from their actual locations. When we measure this deviation as the sum of the squared differences, it implies that we want to minimize the scalar quantity

$$\Gamma = \sum_{j=1}^{M} \sum_{i=1}^{N} \left( \mathbf{X}_i - \mathbf{t}_j - R_j \sigma_{ij} \mathbf{x}_{ij} \tilde{R}_j \right)^2$$

Now partial differentiation with respect to the various parameters can be used to derive partial solutions, assuming other quantities are known. This employs the geometric differentiation techniques from Chapter 8. The results are simple to interpret geometrically and are the estimators you would probably have proposed even without being able to show that they are the optimal solutions.

- **Optimal translation tⱼ given Rⱼ, σᵢⱼ, Xᵢ, and the data xᵢⱼ.** This involves differentiation of the cost function relative to **tⱼ**. The zero derivative is attained at

$$\mathbf{t}_j = \frac{1}{N} \sum_{i=1}^{N} \left( \mathbf{X}_i - R_j \sigma_{ij} \mathbf{x}_{ij} \tilde{R}_j \right) \tag{10.16}$$

This is simply the average difference of where camera j would reconstruct the points based on its presumed rotations and their true average location.

- **Optimal rotation Rⱼ given Xᵢ and the data xᵢⱼ.** The differentiation with respect to a rotor was treated in Section 8.7.2 when optimizing (8.16). Here the result corresponding to (8.17) is that the optimal Rⱼ must satisfy

$$\sum_{i=1}^{N} \left( (\mathbf{X}_i - \mathbf{t}_j) \wedge (R_j \sigma_{ij} \mathbf{x}_{ij} \tilde{R}_j) \right) = 0$$

The geometrical interpretation is that the optimal rotor rotates to minimize the transverse components of all **Xᵢ** when reconstructed by camera j. Substituting the expression for the optimal **tⱼ** leads to

$$\sum_{i=1}^{N} \left( (\mathbf{X}_i - \bar{\mathbf{X}}) \wedge (R_j \sigma_{ij} \mathbf{x}_{ij} \tilde{R}_j) \right) = 0 \tag{10.17}$$

where $\bar{\mathbf{X}} \equiv \frac{1}{N} \sum_{k=1}^{N} \mathbf{X}_k$ is the centroid of the world points. As in Section 8.7.2, this optimal R can be found by a singular value decomposition of a linear function defined in terms of the other parameters.

- **Optimal scaling σᵢⱼ given Rⱼ, tⱼ, Xᵢ, and the data xᵢⱼ.** This requires scalar differentiation of Γ, and results in

$$\sigma_{ij} = (\mathbf{X}_i - \mathbf{t}_j) \cdot (R_j \mathbf{x}_{ij}^{-1} \tilde{R}_j) \tag{10.18}$$

This is almost a division of the estimated **Xᵢⱼ** by the rotated **xᵢⱼ**, except that the inner product makes only the parts along the ray contribute (so that a scalar results).

- **Optimal world points given tⱼ, Rⱼ, σᵢⱼ, and the data xᵢⱼ.** Setting the vector derivative of Γ with respect to **Xᵢ** to zero yields

$$\mathbf{X}_i = \frac{1}{M} \sum_{j=1}^{M} (\mathbf{t}_j + R_j \sigma_{ij} \mathbf{x}_{ij} \tilde{R}_j) \tag{10.19}$$

This is simply the average of the estimations of the location of world point i by each camera.

- **Optimal world points Xᵢ given tⱼ, Rⱼ, and the data xᵢⱼ.** The optimum for σᵢⱼ of (10.18) can be substituted in (10.19) to find a system of linear equations for **Xᵢ** using Rⱼ, **tⱼ**, and the data **xᵢⱼ**. That system can be solved optimally by a least squares technique.

- **Optimal translations tⱼ given Rⱼ and the data xᵢⱼ.** Another substitution of (10.18) and combination with the result for the **Xᵢ** leads to a system of homogeneous linear equations for the **tⱼ** using an estimate of the Rⱼ and the data **xᵢⱼ**. That system can be solved optimally using an SVD.

With these composite results, the following iterative scheme can be formulated:

1. Make an initial guess of the Rⱼ based on the data using a standard stereo vision algorithm (the geometrical basis for such algorithms will be explained in Section 12.2).
2. Estimate the **tⱼ** using the estimate of Rⱼ and the data **xᵢⱼ**.
3. Estimate the world points **Xᵢ** using Rⱼ, **tⱼ**, and the data **xᵢⱼ**.
4. Estimate the scaling σᵢⱼ using (10.18).
5. Obtain a new estimation for Rⱼ using (10.17) and iterate from step 2.

The authors of [38] report that a dozen or so iterations are required for convergence (depending on the number of cameras). The resulting calibration algorithm is fully linear. In modern calibration practice, it is customary to use the outcome of such linear algorithms as an initial estimate for a few steps of subsequent nonlinear optimization to improve the estimation.

This algorithm is the basis of the programming example of Section 10.7.3. The compact and direct derivation of the partial solution formulas (10.16) through (10.19) are an exemplary usage of geometric algebra for these kinds of geometrical optimization problems in the vector space model.

---

## 10.5 Convenient Abuse: Locations as Directions

The vector space model is the natural model to compute with directions and the ultimate tool for this purpose. It will remain clearly recognizable as a submodel providing the algebra of Euclidean directions, even as we move on to more sophisticated models in the next chapters.

In a purist point of view, the vector space model would not be used for other tasks. Yet we can, of course, model location in the vector space model, in the same way as it has always been done in elementary linear algebra. We just view a location as obtained by traveling in a certain direction denoted by a direction vector **p**, over a distance given by its norm. This treats a direction vector as a position vector, and particularly for problems only involving point objects, it is not bad practice. The calibration example of the previous section shows that it can be very effective, and since that is a problem in which locations are actually observed as directions, the vector space model is in fact its natural setting.

When you also have geometrical elements other than pure directions (such as line or plane offset from the origin), you run into the familiar problems that the use of classical linear algebra also entailed: translations of such elements require administration of object types and corresponding data structures. For instance, you can characterize a line by a position vector and a direction vector, but you should keep them clearly separate, for under a translation over a vector **t**, the position needs to change but the direction should not. Uniformity is only obtained by having a single algebraic element representing the line, with a representation of translation that can operate on it directly. The vector space model does not provide that in a structural manner. You need to encode this structure explicitly or use at least the homogeneous model.

Examples of the "convenient abuse" of directions as locations abound in all graphics and robotics literature, as well as in typical physics textbooks. Hestenes [29] shows how geometric algebra can be used effectively in the vector space model to do all of classical physics. The vector space model does not lack computational power, and its rotors help considerably in simplifying classical problems like the orbits of planets in a gravitational field (which involve locations, but viewed from the sun so that their directional treatment becomes natural). But this computational power can only be wielded by manually keeping track of what geometry is represented by each element and which operations are permitted to be performed on it. That is less a problem for physics (which tends to connect its equations by natural language anyway), but it is a major source of programming errors in computer graphics (as reported in [23, 44]). The models of the next chapters will provide alternatives in which a more extended algebra is used to perform simultaneously both the computations and the bookkeeping of geometrical elements.

---

## 10.6 Further Reading

The vector space model may seem prevalent in almost all linear algebra texts, since it is the most basic way to treat geometry with vectors. However, in geometric algebra, the full vector space model naturally includes blades and rotors. Not many texts incorporate those in their treatment of basic geometry.

Your best background material for advanced use of the vector space model of geometric algebra are texts in introductory physics (such as [29] and [15]). For current use in practical problems, the papers using geometric algebra in professional journals on computer vision and robotics are your best source, though these increasingly use the more powerful conformal model to address problems involving direction and location.

---

## 10.7 Programming Examples and Exercises

### 10.7.1 Interpolating Rotations

Interpolating rotations is an important problem with many applications. It is straightforward to implement once you are able to compute the logarithm of a rotor. This can be implemented as follows (see Section 10.3.3):

```cpp
bivector log(const rotor &R) {
    // get the bivector/2-blade part of R
    bivector B = _bivector(R);
    // compute the 'reverse norm' of the bivector part of R:
    mv::Float R2 = _Float(norm_r(B));
    // check to avoid divide-by-zero
    // (and also below zero due to FP roundoff):
    if (R2 <= 0.0){
        if (_Float(R) < 0) {
            // the user asks for log( — 1)
            // we return a 360 degree rotation in an arbitrary plane:
            return _bivector((float)M_PI * (e1 ^ e2));
        }
        else
            return bivector(); // return log(1) = 0
    }
    // return the log:
    return _bivector(B * ((float)atan2(R2, _Float(R)) / R2));
}
```

When you look for this function in the GA sandbox source code package, note that it resides in the file `e3ga_util.cpp` in the `libgasandbox` directory and not in the main source file of this example. The same is true for the `exp()` function listed below. This `exp()` is a specialization of the generic exponentiation algorithm, as described in Sections 7.4 and 21.3.

```cpp
rotor exp(const bivector &x) {
    // compute the square
    mv::Float x2 = _Float(x << x);
    // x2 must always be <= 0, but round off error can make it
    // positive:
    if (x2 > 0.0f) x2 = 0.0f;
    // compute half angle:
    mv::Float ha = sqrt( — x2);
    if (ha == (mv::Float)0.0) return _rotor((mv::Float)1.0);
    // return rotor:
    return _rotor((mv::Float)cos(ha) +
        ((mv::Float)sin(ha) / ha) * x);
}
```

Now that we can go back and forth between rotor and bivector representations of rotations, interpolating rotations becomes straightforward: given two rotors `src` and `dst`, we first compute their difference as the ratio `inverse(src) * dst`. Then we compute the `log()` of the difference, and scale by the interpolation parameter `alpha` (which will run from 0 to 1). The final step is reconstructing the rotor using `exp()`, and putting it back in the original frame by multiplying with `src`:

```cpp
rotor interpolateRotor(const rotor &src, const
    rotor &dst, mv::Float alpha) {
    // return src * exp(alpha * log(inverse(src) * dst));
    return _rotor(src * exp(_bivector(alpha *
        log(_rotor(inverse(src) * dst)))));
}
```

The example uses this code to display a rotating/translating frame with a trail following behind it, as seen in Figure 10.5. Interpolation of translations is done the classical way:

```cpp
e3ga::vector interpolateVector(
    const e3ga::vector &src, const e3ga::vector &dst,
    mv::Float alpha) {
    return _vector((1.0f — alpha) * src + alpha * dst);
}
```

> **Figure 10.5:** Interpolation of rotations (Example 1).

In later examples—when we gain the additional ability to represent translation and scalings as rotors—we will redo this example. Only the `log()` and `exp()` functions will change; the interpolation function remains essentially the same (see Sections 13.10.4 and 16.10.3).

### 10.7.2 Crystallography Implementation

We have made an implementation to play with the vectors generating symmetries of crystal lattices. An example of the output is Figure 10.6. The application works for the point groups in 3-D. It shows three input vectors **a**, **b**, **c** drawn as black line segments, which are the basic generators of the symmetry operators from Section 10.2.3. You can drag those around to investigate possible nearby symmetries.

> **Figure 10.6:** Crystallography (Example 2). This example shows the 24 symmetries of a hexagonal crystal generated from a single red point.

The operators are computed from the initial generators in a brute force manner, by repeatedly multiplying them with each other to make new versors until no new symmetry operators are found. To get a true point group, **a**, **b**, and **c** should be chosen in particular ways, and for some should be considered as composite operators like (**ac**). If the generators are not in the proper configuration to generate a point group, their combination may lead to an infinite number of versors, but we arbitrarily cut off the generation at 200 different versors. The largest true point group of cubic symmetry has 48 operators.

To draw the point groups, the code applies the operators to a single (draggable) input point. A popup menu can be used to initialize the vectors to preprogrammed configurations (cubic, hexagonal, tetragonal, orthorhombic, triclinic, monoclinic, and trigonal), corresponding to the seven main point groups. For more details on how to generate all the subgroups (32 in total), consult [30].

### 10.7.3 External Camera Calibration

This example implements the external calibration of [38], as summarized in Section 10.4.2. It assumes that the cameras have already been calibrated internally (we used the method of Zhang [63]), and that we have an initial external calibration (we used the 8-point algorithm, see e.g., [25]).

The data provided with the example is actual calibration data from a geometric-algebra-based motion capture system built by the authors. The data contains the initial 8-point calibration estimation, but we have deliberately decreased the quality of the initial estimation to make the effect of the refinement more pronounced. Figure 10.7 shows the reconstruction of the markers seen by the cameras after completion of the calibration.

> **Figure 10.7:** External camera calibration (Example 3). The cameras are drawn as red wireframe pyramids (view volume) with a line indicating their viewing direction. The marker points used for calibration are drawn as black dots. A line connects the marker points to show how the single marker was waved through the viewing volume of the cameras.

To implement (10.16) through (10.19), we first need some context. The data is kept in a class `State`. This state contains cameras in array `m_cam`, and 3-D world points in array `m_pt`:

```cpp
class State {
public:
    // ... (constructors, etc)
    // the cameras
    std::vector<Camera> m_cam;
    // the reconstructed markers, for each frame
    std::vector<e3ga::vector> m_pt;
    // is reconstruction of markers valid?
    std::vector<bool> m_ptValid;
};
```

The reconstruction of a marker is invalid when it is visible to only one camera.

Each camera carries its own 2-D marker measurements (`m_pt`), rotation (`m_R` and `m_Rom`), translation (`m_t`), scaling σᵢⱼ (`m_sigma`), and per-marker visibility (`m_visible`). (We ignored visibility issues when we explained the algorithm, but it is included in [38] and implemented in the code.)

```cpp
class Camera {
public:
    // ... (constructors, etc)
    // rotation
    rotor m_R;
    // rotation matrix
    om m_Rom;
    // translation
    e3ga::vector m_t;
    // for each frame, is a marker visible?
    std::vector<bool> m_visible;
    // for each frame, the '2D' point in the image plane
    // (normalized image coordinates, i.e., the e3 coordinate = — 1)
    std::vector<e3ga::vector> m_pt;
    // for each frame the estimated multiplication factor of m_pt
    std::vector<mv::Float> m_sigma;
};
```

Now each of the equations in Section 10.4.2 can be implemented and those functions combined in the total algorithm. As an example, (10.16) leads to the code:

```cpp
void State::updateTranslation() {
    // Iterate over all cameras
    // (start at '1' because translation of first camera is always 0)
    for (unsigned int c = 1; c < m_cam.size(); c++) {
        Camera &C = m_cam[c];
        vector sum;
        int nbVisible = 0;
        for (unsigned int i = 0; i < m_pt.size(); i++) {
            if ((C.m_visible[i]) && m_ptValid[i]) {
                sum += _vector(m_pt[i] - C.m_sigma[i] *
                    (apply_om(C.m_Rom, C.m_pt[i])));
                nbVisible++;
            }
        }
        C.m_t = sum * (1.0f / (mv::Float)nbVisible);
    }
}
```

Note that for efficiency we use the outermorphism matrix representation of the rotor to apply it to vectors by means of the function `apply_om()`. You can consult the rest of the code in the GA sandbox source code package.

We will encounter the motion capture system again in Section 12.5.3, when we reconstruct 3-D markers from the raw 2-D data.
