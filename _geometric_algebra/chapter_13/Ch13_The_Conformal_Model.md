# Chapter 13: The Conformal Model: Operational Euclidean Geometry

In the previous chapters, we studied the geometric algebra version of the homogeneous model. The homogeneous model of Euclidean geometry is reasonably effective since it linearizes Euclidean transformations, and geometric algebra extends the classical homogeneous coordinate techniques nicely through its outermorphisms. However, we remarked that we were not able to use the full metric products of geometric algebra, since the metric of the model was only indirectly related to the metric of the Euclidean space we had wanted to model.

Fortunately, we can do better. In the next few chapters, we present the new conformal model for Euclidean geometry, which can represent Euclidean transformations as orthogonal transformations. Encoding those as versors, we get the full power of geometric algebra, including the structure preservation of all constructions.

In this chapter, we start the exposition by defining the new representational space (which has two extra dimensions and an indefinite metric) and showing what its vectors represent. The two extra dimensions are geometrically interpretable as the point at the origin (as in the homogeneous model) and the point at infinity (which nicely closes Euclidean geometry, making translations into rotations around infinity).

We then focus on how to represent the familiar flats and directions already present in the homogeneous model and how to move them around. As first applications, we use the versor representation to provide straightforward closed-form interpolation of rigid body motions and universally valid constructions for the reflection of arbitrary elements.

The natural coordinate-free specification of elements and operations in the conformal model is best appreciated using the interactive illustrations. Even more than in the previous chapters, we encourage you to play around with the interactive software provided with this book.

---

## 13.1 The Conformal Model

The conformal model is especially designed for Euclidean geometry, which is the geometry of transformations preserving the Euclidean distances of and within objects. These Euclidean transformations are sometimes called isometries, and they include translations, rotations, reflections, and their compositions.

We will occasionally limit ourselves to Euclidean motions, which are the Euclidean transformations that can be performed a little at a time. These are also known as rigid body motions, and they consist of compositions of translations and rotations. They are proper isometries, i.e., they preserve the Euclidean distances and handedness.

To emphasize that the conformal model involves the representation of Euclidean geometry, we will denote the base space by Eⁿ rather than ℝⁿ·⁰. This notation is meant to suggest that the group of Euclidean transformations is to be represented in the model as well.

### 13.1.1 Representational Space and Metric

We start with some observations on points in a Euclidean space.

- A Euclidean space Eⁿ has points at a well-defined distance from each other. If two points P and Q were created by a translation over the Euclidean direction vectors **p** and **q** from some origin O, then their squared distance is $d^2_E(P, Q) = \|\mathbf{p} - \mathbf{q}\|^2 = (\mathbf{p} - \mathbf{q}) \cdot (\mathbf{p} - \mathbf{q})$. In many respects, these squared distances are more convenient to compute with than the actual distances; for instance, Pythagoras' theorem states that squared distances can be added under certain conditions.

- Euclidean spaces do not really have an origin: there is no special finite point that can be distinguished from other points. If an origin is used, it is for convenience, as a point to relate other points to. Similarly, there are no preferential directions, though it may be convenient to define an arbitrary standard frame at the equally arbitrary origin.

- Mathematicians have long known that it is convenient to close a Euclidean space by augmenting it with a point at infinity. (They call this compactification.) That point at infinity is a point in common to all lines and planes, and invariant under the Euclidean transformations. Having it explicit makes the algebraic patterns in geometrical statement more universal.¹

When constructing a model for Euclidean geometry, we take these properties as central. The arbitrariness of the origin was something we wanted in the homogeneous model, and it was partly achieved by assigning an extra dimension to it in a representational space. So we need at least need an (n+1)-dimensional representational space. We are now also going to assign an extra dimension to the special point at infinity. In our model, we represent it as a vector denoted as ∞, to remind us of what it is. (There will be no confusion with the number infinity.) This turns our representational space for the n-dimensional Euclidean space Eⁿ from (n + 1)-dimensional to (n + 2)-dimensional.

The interface between geometry and algebraic representation is that we represent Euclidean points in Eⁿ by representative vectors in the (n + 2)-dimensional representational vector space. The infinite point is represented by the vector ∞. A finite point P is represented by a vector p, with certain additional properties that we specify below. Now we still have the freedom to choose the metric of this representational space (and we must specify it if we want to endow it with a geometric algebra). We use this metric to encode the Euclidean distance in Eⁿ. In view of the observed linear behavior of square distances we do so as follows:

$$\mathbf{p} \cdot \mathbf{q} \sim d^2_E(P, Q) \tag{13.1}$$

On the left you see the inner product of two vectors of the representational space; on the right you see the squared distance of two points in the Euclidean space Eⁿ. They are directly proportional! (There are some scaling factors that we introduce below for backwards compatibility, but those are irrelevant to the principle of the setup.)

One immediate consequence of this definition of the metric is that a vector p representing a finite point must obey p · p = 0, since the Euclidean distance of a point to itself is zero: $d^2_E(P, P) = 0$. Therefore, Euclidean points are represented by **null vectors** in the representational model. A null vector is a vector with norm zero; in a Euclidean space, such a vector would have to be the zero vector, and we could not use that to denote a great variety of points. So the (n + 2)-dimensional representational space must be non-Euclidean.

Null vectors may seem strange, but it is fairly easy to make them in a manner that feels only moderately irregular. We may alternatively construct the (n + 2)-dimensional representational space by augmenting the regular n Euclidean dimensions with two special dimensions, for which a basis is formed by two vectors **e** and **ē** that square to +1 and −1, respectively, and that are orthogonal (so that **e**·**ē** = 0). Having these, it is easy to make null vectors out of them: the vectors (**e**+**ē**) and (**ē**−**e**) are both null without being zero, as you can check easily by squaring them. In this construction, the representational space has an orthonormal basis consisting of (n + 1) positive dimensions (with basis vectors squaring to +1) and 1 negative dimension (with basis vector squaring to −1). We therefore denote it by ℝⁿ⁺¹·¹. Such a space is called a Minkowski space in physics, where it has been well studied to represent space-time in relativity; the negative dimension is then employed to represent time. We will find a geometrically more natural basis than **e** and **ē** for the conformal model, but the representational space is still the metric space ℝⁿ⁺¹·¹.

This (n + 2)-dimensional space requires n + 2 coefficients to specify a vector. We should require only n coefficients to specify a point in Euclidean space, so there is more in this space than we appear to need. Since points are represented by null vectors, their representatives must obey p · p = 0, and this is a condition on their coefficients that removes one degree of freedom, leaving n + 1. The remaining degree of freedom we use to denote the weight of the point, as in the homogeneous model. In that model, we retrieved the weight as $e_0^{-1} \cdot p$, since it was the coefficient of e₀; in the present model we extract it by the operation −∞ · p. The relationship of inner product to distance of (13.1) should of course be defined on properly normalized points, since it is independent of the weight, so in that formula we should divide p by its weight, and q as well. We introduce an extra scaling factor of −½ for convenience later on, and actually define the inner product of vectors representing points through

$$\frac{\mathbf{p}}{-\infty \cdot \mathbf{p}} \cdot \frac{\mathbf{q}}{-\infty \cdot \mathbf{q}} \equiv -\frac{1}{2} d^2_E(P, Q) \tag{13.2}$$

(The two minus signs on the left of course cancel each other, but we would like to get you used to viewing −∞ · p as a weight-computing expression.) Equation (13.2) is in fact the definition of the representational model; all the rest of the correspondence between elements of its geometric algebra and Euclidean geometry follows from it without additional assumptions.

The model thus constructed was called the **conformal model** in the literature, for the mathematical reason that it is capable of representing conformal transformations by versors. We will demonstrate that in Chapter 16, but prefer to focus on its use for Euclidean transformations first. We will show that it is an operational model for Euclidean geometry in the double sense that Euclidean transformations are represented as structure-preserving operators, which are moreover easy to put to operational use. In view of that, we would prefer to call it the operational model for Euclidean computations. This is too much of a mouthful, so we might as well conform to the term conformal model, despite its arcane origins.

Even though the conformal model hit computer science only a few years ago, when it was introduced by Hestenes et al. in 1999 [31], we are beginning to find that we could have had the pleasure of its use all along. Considerable elements of it are found in much older work, and it appears to have been reinvented several times. We do not know the whole story yet, but markers on the way are Wachter (a student of Gauss), Cox [9] and Forder 1941 [22] (who used Grassmann algebra to treat circles and their properties), Anglès 1980 [2] (who showed the crucial versor form of the conformal transformations) and Hestenes (who had already presented it in his 1984 book [33] but only later realized its true importance for Euclidean geometry). We are convinced that its time of general adaptation has finally arrived, since the conformal model is much more clearly useful to actually programming geometrical applications than it is to theorizing about geometry on paper.

---

¹ The homogeneous model has location-independent directions, which we identified as being characterized by improper points on the heavenly sphere, but this has a different flavor than a single point at infinity, which is a location that one can approach from any direction. We will not lose those extra elements representing directions for they are also found as elements in the new model.

### 13.1.2 Points as Null Vectors

Let us be more precise about the point representation. As we realized before, the relationship of the metric to the Euclidean distance implies that finite points are represented by null vectors. What about the point at infinity?

The point at infinity is represented by ∞, and it should have infinite distance to all finite points. Substituting q = ∞ in (13.2), we find that an infinite result is reached only if we set ∞·∞ = 0. This implies that the point at infinity is also represented by a null vector.

> **Null vectors in the conformal model ℝⁿ⁺¹·¹ represent Euclidean points of Eⁿ (both finite and infinite).**

After you have gotten used to this correspondence, it becomes natural to identify representative null vectors with points and talk about the null vector p as "the point p" rather than as "representing the point P." We will gradually slip into that convenient usage as this chapter evolves.

We call a point p **normalized** or a **unit point** when its weight equals 1:

$$-\infty \cdot \mathbf{p} = 1$$

We may be tempted to select one special unit point O as the origin of our space and represent it by a vector denoted o. It would then be a special vector in the conformal model with the property o · ∞ = −1, as well as o · o = 0, by virtue of being a point. It therefore appears to bear a special relationship to the vector ∞ representing the point at infinity: though both are null vectors, they are (minus) each other's reciprocals in the sense that o · ∞ = −1. That simplifies the math of computing with them, and it reveals that the weight of a point is the coefficient of o of its representative vector (for a coefficient of a vector is retrieved by an inner product with its reciprocal, as we saw in Section 3.8—so the o coefficient is retrieved by an inner product with −∞). The strong parallel with e₀ and $e_0^{-1}$ in the homogeneous model suggests that an arbitrary unit point might be writable as o + **p**, but this is not a null vector (it squares to **p**²). We should use the extra dimension to represent a unit point as p = o + **p** + α∞, with an α that should be determined by the null vector condition p · p = 0. You can easily verify that this gives

$$\mathbf{p} = o + \mathbf{p} + \frac{1}{2}\mathbf{p}^2 \infty \tag{13.3}$$

as the representative null vector for a unit point relative to the origin o.²

Equation (13.3) resembles a coordinate representation of the vector p in terms of a purely Euclidean location vector **p** and two extra terms in a {o, ∞}-basis for the extra two dimensions of the conformal model. It is somewhat misleading: although ∞ indeed has special significance, the origin point o does not. Any unit point could have been used as origin; it would have had the same relationships with ∞ (since any finite point p obeys −∞·p = 1), and would merely have changed the value of the location vector **p** for the particular point P we are considering. So (13.3) is deceptive in that it is too specific. Still, it is convenient to have, since it gives a connection to the homogeneous representation (o is like e₀), and even to the vector space model (in exhibiting the Euclidean location vector **p**). You can use it when you begin to work with the conformal model—as you advance, you will dare to work coordinate-free, merely using the algebraic properties of the point p, and that will make your formulas and algorithms more generally applicable.

But while we have this specific representation, let us use it to verify the consistency with the original definition of the metric:

$$\mathbf{p} \cdot \mathbf{q} = (o + \mathbf{p} + \frac{1}{2}\mathbf{p}^2\infty) \cdot (o + \mathbf{q} + \frac{1}{2}\mathbf{q}^2\infty)$$
$$= -\frac{1}{2}\mathbf{q}^2 + \mathbf{p} \cdot \mathbf{q} - \frac{1}{2}\mathbf{p}^2$$
$$= -\frac{1}{2}(\mathbf{q} - \mathbf{p})^2 \tag{13.4}$$

Note how the metric of the conformal model plays precisely the right role to compose the correct terms in the squared difference required to express the Euclidean distance. So the conformal model indeed does what it was designed to do.

Letting **p** become large in (13.3), the dominant term is proportional to +∞. This shows the reason for our choosing the normalization such that ∞ · p is negative: now +∞ is positively proportional to (the vector representing) the point at infinity.

We are especially interested in the Euclidean space E³, and when required, we use an orthonormal basis {**e₁**,**e₂**,**e₃**} for that part of the representation. That leaves the other two elements in the basis of ℝⁿ⁺¹·¹. Earlier, we briefly introduced the basis {**e**,**ē**} with their squares of +1 and −1, and that would work as basis for the part ℝ¹·¹. But it is often geometrically more significant to make a change of basis to the two null vectors o and ∞, representing our arbitrary origin and the point at infinity. These null vectors can be defined in terms of **e** and **ē** as

$$o = \frac{1}{2}(\mathbf{e} + \bar{\mathbf{e}}), \quad \infty = \bar{\mathbf{e}} - \mathbf{e} \tag{13.5}$$

giving conversely

$$\mathbf{e} = o - \frac{1}{2}\infty; \quad \bar{\mathbf{e}} = o + \frac{1}{2}\infty \tag{13.6}$$

So in terms of a basis, this is just a simple coordinate change in the representational subspace with pseudoscalar **e** ∧ **ē** = o ∧ ∞. We reiterate that any finite unit point could have been used instead of o without changing these defining equations (picking another point as origin merely changes where we attach the Euclidean part Eⁿ to the basis for ℝ¹·¹, and therefore just changes the Euclidean vectors by an offset). For E³, the basis elements have the inner product multiplication tables of Table 13.1. We can define the pseudoscalar by I₃ = **e₁** ∧ **e₂** ∧ **e₃**.

But throughout the remainder, we will avoid the use of the basis to specify elements. We shall hardly need it, for the Euclidean covariance properties of the conformal model will make computations in it delightfully coordinate-free.

---

² We should mention that the standards in this new model have not quite been established yet, and you may find other authors with different definitions and notations of the elements we have denoted ∞ and o, differing by a factor of ±1 or ±2 with our definition. For instance, in [15] our ∞ is their −n, and our o is their −½n̄, so that their point representation reads p = p²n + 2**p** − n̄, with normalization p · n = 2. Any rescaling of ∞ is a trivial change to the conformal model, not affecting its structure in any way, though it is a bit annoying in cross-referencing texts from various sources. Always check the local definitions! We will give our reasons for our choices.

**Table 13.1:** Multiplication table for the inner product of the conformal model of 3-D Euclidean geometry E³, for two choices of basis.

| | **e** | **e₁** | **e₂** | **e₃** | **ē** |
|---|---|---|---|---|---|
| **e** | 1 | 0 | 0 | 0 | 0 |
| **e₁** | 0 | 1 | 0 | 0 | 0 |
| **e₂** | 0 | 0 | 1 | 0 | 0 |
| **e₃** | 0 | 0 | 0 | 1 | 0 |
| **ē** | 0 | 0 | 0 | 0 | −1 |

| | o | **e₁** | **e₂** | **e₃** | ∞ |
|---|---|---|---|---|---|
| o | 0 | 0 | 0 | 0 | −1 |
| **e₁** | 0 | 1 | 0 | 0 | 0 |
| **e₂** | 0 | 0 | 1 | 0 | 0 |
| **e₃** | 0 | 0 | 0 | 1 | 0 |
| ∞ | −1 | 0 | 0 | 0 | 0 |

### 13.1.3 General Vectors Represent Dual Planes and Spheres

By construction, some of the vectors in the representational space ℝⁿ⁺¹·¹ represent weighted points of the Euclidean space; namely all null vectors, which must satisfy p · p = 0. Yet there are many more vectors in ℝⁿ⁺¹·¹. We should investigate whether those are also useful to represent elements of Euclidean geometry. And indeed they are: we will find that they are generally dual spheres (with points and dual planes included as special cases for radius zero and infinity, respectively).

To determine what such a nonnull vector v signifies, we should somehow use our fundamental definition of (13.2), since that is all that we have up to this point. Therefore we probe the vector v with a unit point x, solving the equation x · v = 0 to find out what v is when considered as defining a Euclidean point set in this manner. Note that this already implies that we interpret a vector v as the dual representation of some Euclidean element.

It is perhaps a bit surprising that we meet these dual representations of elements before the direct interpretations. (Actually, something similar happened with the vectors of the homogeneous model. There, a vector of the form e₀ + **p** represented a point, a vector of the form **u** was a direction, and a vector **n** − δe₀⁻¹ = **n** ∓ δe₀ represented a dual plane).

- **Null Vector p = α(o + p + ½p²∞): Point.** We may as well first verify that this probing procedure gives the right interpretation for a general null vector of the form we saw before. Our earlier computation (13.4) gives x · p = −½α(**p** − **x**)², so that this is zero if and only if **x** = **p**. Therefore x must be a point at the same location as p, albeit possibly with a different weight.³

  As we have seen, a vector p representing a point satisfies p² = 0, and ∞ · p = −α. These properties define this class of vector of ℝⁿ⁺¹·¹ representing a point of Eⁿ. The prototype of this class is the vector o representing the point O at the arbitrary origin.

- **Vector without o Component: π = n + δ∞: Dual Plane.** A vector π without an o component has the general form π = **n** + δ∞. It clearly does not represent a Euclidean point. We probe it to find out what it is in the Euclidean space:

  $$\mathbf{x} \cdot \pi = (o + \mathbf{x} + \frac{1}{2}\mathbf{x}^2\infty) \cdot (\mathbf{n} + \delta\infty) = \mathbf{x} \cdot \mathbf{n} - \delta$$

  and demanding this to be zero retrieves the familiar dual plane equation for a plane with normal vector **n** at a distance δ/‖**n**‖ from the origin. Therefore, the vector π dually represents a Euclidean plane. We will denote dual planes by π-based symbols (and direct planes by symbols based on Π).

  Such a dual plane vector satisfies ∞ · π = 0 and π² = **n**², defining the type. The equation ∞·π = 0 can be interpreted as: ∞ lies on the dual plane π. The prototypical member of this class is the vector **n** of ℝⁿ⁺¹·¹ that lies completely in its subspace Eⁿ (and hence is denoted in bold font).

- **General Vector σ± = α(c ∓ ½ρ²∞): Dual Sphere.** A general vector can be made as a scaled version of a null vector with an additional amount of ∞-component to make it nonnull. Let us write it as σ = α(c + β∞), with c a unit point representative (so that c² = 0, and −∞ · c = 1). Then we find

  $$\mathbf{x} \cdot \sigma = \alpha(\mathbf{x} \cdot c + \beta \mathbf{x} \cdot \infty) = \alpha\left(-\frac{1}{2}d^2_E(\mathbf{x}, c) - \beta\right)$$

  Requiring this to be zero gives the equation ‖**x** − **c**‖² = −2β, where we substituted the Euclidean distance between x and c as ‖**x** − **c**‖. If β is negative, we redefine it as β = −½ρ², and obtain

  $$\|\mathbf{x} - \mathbf{c}\|^2 = \rho^2$$

  We recognize the equation of a sphere with center at the location **c**, and radius ρ.

  > A general vector of the form σ = α(c − ½ρ²∞) dually represents a Euclidean sphere with center c and radius ρ, and weight α.

  If β is positive, we can set it equal to ½ρ², and we obtain the equation

  $$\|\mathbf{x} - \mathbf{c}\|^2 = -\rho^2$$

  By analogy, this represents an **imaginary sphere** whose squared radius is negative. We do not need complex numbers to define it as long as we only represent squares of distances (which is indeed all that entered our model by its definition).

  > A general vector of the form σ = α(c + ½ρ²∞) dually represents an imaginary sphere with center c and squared radius −ρ², and weight α.

  These imaginary spheres may appear useless, but they occur naturally as solutions to intersections and in duality computations. They keep our algebra consistent and closed, and we will try to develop a feeling for them (yes, you can learn to see imaginary spheres, in Section 15.1.3).

  The dual sphere vectors satisfy σ² = ±α²ρ² and −∞ · σ = α, so that a unit-weight sphere has the same square as its radius. The null vectors representing points can now be viewed as (dual) spheres of zero radius, which makes good geometric sense. Prototypical examples of this class are the vectors **e** = o − ∞/2 and **ē** = o + ∞/2, which represent the real and imaginary unit spheres at the origin.

This completes the Euclidean interpretation of the representational vectors in the conformal model; the results are collected in Table 13.2. The extension of the homogeneous model by the extra dimension ∞, and the modification of the metric, have already given us (dual) spheres as typical Euclidean elements (with a point as a zero-radius sphere and a plane as an improper sphere that passes through infinity). This carries it beyond the homogeneous model, which could only represent flats. Clearly the set of transformations preserving properties of spheres are more limited than those preserving properties of flats, so the conformal model will be more specifically tailored to Euclidean geometry than the homogeneous model. The affine transformations in particular, which preserved the flats of the homogeneous model, are no longer all admissible since they may not preserve spheres. This loss is in fact a gain: the added precision makes the conformal model much more powerful for the treatment of Euclidean transformations than the homogeneous model.

We are obviously going to invoke the geometric algebra structure of the conformal model to make more involved elements from the dual planes and dual spheres at our disposal, but this will have to wait until the next chapter. In this chapter, we explore how the Euclidean transformations can be represented in the new model, and how that improves and extends the capabilities of the homogeneous model.

---

³ Note however that there is something slightly uncomfortable going on: strictly speaking, if x is a point, then p must be the dual representation of a point (since it is the solution of x·p = 0), rather than the direct representation (which would be the solution of x∧p = 0). Strangely enough, p is both, due to the special nature of null vectors. For x∧p = 0 is certainly valid for x = p, and computing: x∧p = (o+**x**+½**x**²∞)∧α(o+**p**+½**p**²∞) = α o∧(**p**−**x**)+···, and already the first term shows that we can only make this zero by having **x** = **p**, so that x = p is indeed the unique solution. We get back to the dual nature of the point representation when we treat the plunge in Section 15.1.

**Table 13.2:** The interpretation of vectors in the conformal model.

| Element | Form | Characteristics |
|---------|------|-----------------|
| Point | p = α(o + **p** + ½**p**²∞) | p² = 0, −∞ · p ≠ 0 |
| Dual plane | π = **n** + δ∞ | π² ≠ 0, −∞ · π = 0 |
| Dual real sphere | σ = α(p − ½ρ²∞) | σ² = ρ² > 0, −∞ · σ ≠ 0 |
| Dual imaginary sphere | σ = α(p + ½ρ²∞) | σ² = ρ² < 0, −∞ · σ ≠ 0 |

---

## 13.2 Euclidean Transformations as Versors

The crucial Euclidean property of point distance was embedded in terms of the inner product of the representational space ℝⁿ⁺¹·¹ by (13.2). Euclidean transformations in Eⁿ are isometries: they preserve distances of points, so they should be represented by transformations of ℝⁿ⁺¹·¹ that preserve the inner product. Such transformations are therefore orthogonal transformations of the representational space. We know from Section 7.6 that geometric algebra can represent orthogonal transformations as versors. Therefore:

> **Euclidean transformations are representable by versors in the conformal model.**

Since versors have structure-preserving properties, all constructions that we make using the geometric algebra of ℝⁿ⁺¹·¹ will transform nicely (i.e., covariantly) in that algebra—which implies that they move properly with the Euclidean transformations. We never need to enforce that; it is intrinsically true due to the versor structure. This kind of operational model is very intuitive to use (for you can make a construction somewhere, and it will hold anywhere). The conformal model is the smallest known algebra that can model Euclidean transformations in this structure-preserving manner.

### 13.2.1 Euclidean Versors

Representing Euclidean transformations by versors is the plan, but when we put it into action we have to be bit more precise. Not just any versor in the algebra of ℝⁿ⁺¹·¹ is a Euclidean motion: it also needs to preserve the vector ∞, since that is an essential part of the modeling interface between the inner product and its interpretation as Euclidean distance in (13.2). Such a versor induces an operation in the Euclidean base space that preserves the point at infinity, which is indeed a property of Euclidean transformations.

So in the conformal model, a Euclidean transformation is represented by a versor V that preserves ∞. Using the versor product formula of (7.17), this gives

$$V \infty V^{-1} = \infty$$

It follows that ∞V − V∞ = 0, so that ∞ ⌋ V = 0 is the condition on a versor V to be a Euclidean versor.

The simplest versor is a vector; and the most general vector that satisfies ∞ ⌋ V = 0 is π = **n** + δ∞. This represents a dual plane. All other Euclidean transformation versors should be products of such vectors; in the base space, we would phrase that as

> **All Euclidean transformations can be made by multiple reflections in well-chosen planes.**

This well-known fact from Euclidean geometry is the key to designing the Euclidean transformation versors in ℝⁿ⁺¹·¹.

### 13.2.2 Proper Euclidean Motions as Even Versors

We showed in Part I that an odd number of reflections will produce a transformation with determinant −1 (Section 7.6.2). The resulting versor represents an improper motion: it changes handedness, and therefore cannot be performed as a continuous motion. Proper, continuous Euclidean motions preserve handedness and are represented by even versors, which we can normalize to be rotors. There are two elementary proper motions: pure translations and pure rotations. They can of course be composed to make general proper motions. We construct their versors, and illustrate this in Figure 13.1.

> **Figure 13.1:** The versors for the Euclidean transformations can be constructed as multiple reflections in well-chosen planes. (a) Two parallel planes make a translation, and (b) two intersecting planes make a rotation.

- **Translations.** As a special case of versor composition, we compute the product of two reflecting parallel planes with the same direction but at a differing location, as in Figure 13.1(a). Let **n** be their unit normal vector, then we compute

  $$(\mathbf{n} + \delta_2\infty)(\mathbf{n} + \delta_1\infty) = 1 - (\delta_2 - \delta_1)\mathbf{n}\infty \equiv 1 - \mathbf{t}\infty/2 \equiv T_\mathbf{t}$$

  where we define the Euclidean translation vector **t** ≡ 2(δ₂ − δ₁)**n**. Geometrically, we would expect this double reflection to represent a translation in the direction **n**, over twice the distance of the reflecting planes (i.e., over **t**).

  For a point at the (arbitrary) origin o, this behavior is easily checked:

  $$T_\mathbf{t} \, o \, T_\mathbf{t}^{-1} = (1 - \mathbf{t}\infty/2) \, o \, (1 + \mathbf{t}\infty/2)$$
  $$= o - \frac{1}{2}(\mathbf{t}\infty o - o\mathbf{t}\infty) - \mathbf{t}\infty o\mathbf{t}\infty/4$$
  $$= o - \mathbf{t}(\infty \cdot o) - \infty(2o \cdot \infty - \infty o)\mathbf{t}^2/4$$
  $$= o + \mathbf{t} + \frac{1}{2}\mathbf{t}^2\infty \equiv \mathbf{t}$$

  (Verify this computation carefully, as it contains techniques you will frequently use.) This is the representative of the point **t** at location **t** relative to the origin o, so we have indeed found the translation versor. This versor is even a rotor, for $T_\mathbf{t} \tilde{T}_\mathbf{t} = (1 - \mathbf{t}\infty/2)(1 + \mathbf{t}\infty/2) = 1 - \mathbf{t}\infty\mathbf{t}\infty/4 = 1 + \mathbf{t}^2\infty^2/4 = 1$.

  Like all rotors in ℝⁿ⁺¹·¹, the translation rotor has an exponential representation. This is easy to construct from the fact that ∞ squares to 0:

  $$T_\mathbf{t} = 1 - \mathbf{t}\infty/2 = 1 + (-\mathbf{t}\infty/2) + \frac{1}{2!}(-\mathbf{t}\infty/2)^2 + \cdots = e^{-\mathbf{t}\infty/2}$$

  The Taylor expansion of the exponential truncates by itself, after the first-order term. We foresaw such unusual rotors when discussing the exponential in Section 7.4.2.

- **Rotations in the Origin.** If we consider two planes in the origin as in Figure 13.1(b), these are dually represented as the purely Euclidean vectors π₁ = **n₁** and π₂ = **n₂**. Viewed as reflection versors, we may take these as unit vectors without loss of generality. Their product is the versor

  $$\pi_2 \pi_1 = \mathbf{n}_2 \mathbf{n}_1$$

  in which we recognize the purely Euclidean rotor R. Let us check what it does on a point, represented as a vector of ℝⁿ⁺¹·¹:

  $$R(o + \mathbf{p} + \frac{1}{2}\mathbf{p}^2\infty)\tilde{R} = Ro\tilde{R} + R\mathbf{p}\tilde{R} + \frac{1}{2}\mathbf{p}^2(R\infty\tilde{R})$$
  $$= o + (R\mathbf{p}\tilde{R}) + \frac{1}{2}\mathbf{p}^2\infty$$
  $$= o + (R\mathbf{p}\tilde{R}) + \frac{1}{2}(R\mathbf{p}\tilde{R})^2\infty$$

  which holds simply because the elements o and ∞ commute with the purely Euclidean elements. This is indeed the representation of the point at location R**p**R̃, so successive reflections in planes through the origin are a rotation in a plane through the origin. This was also the case in the vector space model when we introduced its rotors in Chapter 7 (and therefore also in the homogeneous model). This rotor representation of rotations is therefore nicely backwards compatible: it is literally the same as in the vector space model contained in the space ℝⁿ⁺¹·¹, and it merely acts on the whole space now.

  Since this rotor is completely Euclidean, the earlier results of Chapter 7 and the vector space model in Chapter 10 apply, and we can write it as

  $$R = e^{-\mathbf{I}\phi/2} = \cos(\phi/2) - \sin(\phi/2)\mathbf{I}$$

  in terms of its rotation plane **I** and rotation angle φ.

- **General Rigid Body Motions.** A general rigid body motion can be constructed by first doing a rotation in the origin and following it by a translation. That gives a rotor of the form

  $$(1 - \mathbf{t}\infty/2)R$$

  This generally contains terms of grades 0, 2, and 4. Being a rotor, the general rigid body motion can also be written in exponential form, but this is a bit involved: it requires viewing it as a screw motion (i.e., a rotation around a general axis combined with a translation along that axis). We will get back to analyzing and interpreting such motions in Section 13.5.2.

The above shows how the Euclidean proper motions are represented as rotors (i.e., as even unit versors). Improper Euclidean motions can be represented by odd unit versors (just multiply by a vector representing a dual reflection plane).

As a shorthand of the linear transformation produced by the application of T_t in a versor product, we will use T_t[·] (note the sans serif font). For the linear transformation of the rotor R_I, we may use the notation R_I[·] (though we may conveniently drop the reference to the bivector angle).

### 13.2.3 Covariant Preservation of Structure

By representing Euclidean transformations as versors, we have achieved an important algebraic milestone in computing with Euclidean spaces, with far-reaching geometric consequences: automatic structure-preservation of all our constructions, in the sense of Section 7.6.3. By this we mean that a construction made anywhere, in any orientation, will automatically transform properly under a Euclidean motion.

As an example, we have just seen how we make a rotation by reflection in two planes passing through a point o as the product R = π₂π₁. If we now would want to have a similar rotation at a point p, we could define that new rotation by moving both planes to p by a translation versor T_p and making the computation π₁ₚπ₂ₚ for the moved planes π₁ₚ ≡ T_p π₁ T_p⁻¹ and π₂ₚ ≡ T_p π₂ T_p⁻¹. But when we do this, we find that this is the same as applying the translation T_p to the original rotor R, for π₁ₚπ₂ₚ = T_p π₁ T_p⁻¹ T_p π₂ T_p⁻¹ = T_p π₁π₂ T_p⁻¹ = T_p R T_p⁻¹. The rotor of the moved planes is the moved rotor of the planes!

This is of course what we want for our original construction to be geometrically meaningful: it should transfer to another location in precisely this covariant manner (co-variant, implying: varying with the change) under the transformations of Euclidean geometry. We have effectively used similarity under Euclidean transformations as a generative principle rather than as a property to check afterwards.

It should be clear from this example that it is precisely the versor representation that makes this covariant structure preservation work so automatically, and that it should therefore work for any Euclidean transformation (since they are all represented by versors in the conformal model). We discuss the abstract principle involved in some detail, so that we can apply it throughout the remainder of this chapter. The most important structure-preservation properties of the versor product are easily proved.

- **The versor product preserves the structure of a geometric product:**

  $$\mathsf{V}[XY] = \mathsf{V}[X]\mathsf{V}[Y]$$

  *Proof:*⁴ Use associativity: V(XY)V⁻¹ = VXYV⁻¹ = VXV⁻¹VYV⁻¹ = (VXV⁻¹)(VYV⁻¹).

- **The versor product is linear:**

  $$\mathsf{V}[\alpha X + \beta Y] = \alpha\mathsf{V}[X] + \beta\mathsf{V}[Y]$$

  *Proof:* V(αX + βY)V⁻¹ = αVXV⁻¹ + βVYV⁻¹.

- **The versor product is grade-preserving:**

  $$\langle\mathsf{V}[X]\rangle_k = \mathsf{V}[\langle X\rangle_k]$$

  *Proof:* Grades are defined in terms of the number of factors in an outer product. An outer product can be written as a sum of geometric products, and under transformation each of its terms transforms in a structure-preserving manner. The factorization of the transform is the transform of the factorization, and therefore the number of (transformed) vector factors in the outer product is preserved.

In Part I, we saw that we construct all objects and operators in geometric algebra using only these constructive elements (either as linear combinations of geometric products or by grade selection). Therefore the versors preserve all constructions, even including meet and join, inverses, and duality. So the universal structure preservation of constructions can be denoted compactly as

$$V(A \circ B)V^{-1} = (VAV^{-1}) \circ (VBV^{-1})$$

where ∘ may be substituted by any of the products ∧, ⌋, ·, *, ∩, ∪.

This leads to the **operational model principle**, of which the conformal model is merely one manifestation:

> If we have managed to construct a geometric algebra in which useful transformations (motions) in the base space are represented as versors, then all constructions in the model transform covariantly (i.e., with preservation of their structure).

We implicitly used this principle for rotations in the vector space model, which is why that is the operational model for directions in space. The homogeneous model augmented it with translations as linear transformations, but not as versors, which is why it had some problems preserving the structure of constructions (notably the metric properties). In the conformal model we finally have the Euclidean transformations as versors, so all constructions should be covariant under Euclidean transformations. It is the smallest known model that can do this. Operational models for other important geometries (such as projective geometry) have yet to be developed.

---

⁴ For structural clarity, we suppressed the signs in (7.18), which really should be there. You can easily verify that the result still holds when these are included.

### 13.2.4 The Invariance of Properties

Structure preservation is useful in analyzing and constructing all elements in the conformal model: it saves work. Since we have the Euclidean transformations available, we need to focus only on standardized elements at the origin (which is arbitrary anyway) to determine their form and defining equations. We can always move them to their desired location and orientation later. But are we guaranteed that their defining properties are preserved under such a transformation? For instance, could a point become a dual sphere or a dual plane? They are all represented as vectors, and could these not change into each other?

This brings us to how the characteristic properties change, that determine the interpretation of a representative element. For vectors, these properties were given in Table 13.2. They express that some combination of products is equal to a scalar. That algebraic form already guarantees that they are structurally preserved. To take an example, we have seen above how a unit point **t** at location **t** can be made by translation of a unit point at the origin: **t** = T_t o T_t⁻¹. But how do we know that it is still a unit point and not a dual sphere or dual plane? Of the original point o, we knew that o² = 0 and −∞ · o = 1. Since these conditions are completely expressed in terms of the products of geometric algebra, they transform covariantly under the Euclidean transformation of translation, so we can relate the properties of **t** to those of o:

$$\mathbf{t}\mathbf{t} = T_\mathbf{t} o T_\mathbf{t}^{-1} T_\mathbf{t} o T_\mathbf{t}^{-1} = T_\mathbf{t} oo T_\mathbf{t}^{-1} = T_\mathbf{t} \cdot 0 \cdot T_\mathbf{t}^{-1} = 0$$

so indeed, **t** is also a point. Moreover,

$$-\infty \cdot \mathbf{t} = -\infty \cdot (T_\mathbf{t} o T_\mathbf{t}^{-1}) = -(T_\mathbf{t}\infty T_\mathbf{t}^{-1}) \cdot (T_\mathbf{t} o T_\mathbf{t}^{-1}) = -T_\mathbf{t}(\infty \cdot o)T_\mathbf{t}^{-1} = 1$$

so **t** also has unit weight. Note that in the derivation of weight preservation, it is essential that ∞ is an invariant of the translation: it does not change, so the normalization equation preserves its form after transformation.

> Characteristic properties expressed as scalar conditions in terms of the products and ∞ are automatically invariants of the Euclidean transformations.

In summary, as long as we construct elements and their defining properties in terms of the products of the geometric algebra of the operational model ℝⁿ⁺¹·¹, we are automatically guaranteed of their covariance (for the elements) and invariance (for their properties) under Euclidean transformations. So we can construct everything around the origin, and yet get a full inventory of the general possibilities. With that labor-saving capability, we are ready to construct and interpret general blades of ℝⁿ⁺¹·¹ effectively.

---

## 13.3 Flats and Directions

Let us embed the geometrical elements of the homogeneous model into the conformal model, and investigate how the versor properties empower our geometric representation.

We originally started our exploration of the conformal model in Section 13.1.3 by interpreting vectors, which turned out to be the dual representations of spheres (real, imaginary, or zero radius), hyperplanes, and the point at infinity. To establish the correspondence with the vector space model and the homogeneous model, we now prefer instead to construct the direct representations of elements. The two representations are of course related by duality, so none is more fundamental than the other, but it is more natural to assign orientations to flats (and spheres) in the direct representation—and then dualization automatically introduces some grade-dependent orientation signs in their corresponding duals, which are good to get straight once and for all.

Constructing direct representations implies that we use the outer product ∧, both for constructing the elements (as blades A) and for testing what Euclidean point set it represents (by solving x ∧ A = 0).

### 13.3.1 The Direct Representation of Flats

We start constructing an element of the form

$$X = \alpha(p_0 \wedge p_1 \wedge \cdots \wedge p_k \wedge \infty)$$

by which we mean the weighted outer product of k+1 unit points and the point at infinity ∞. This clearly contains the point at infinity (since ∞ ∧ X = 0), and we will find out that such a blade is the direct representation of a k-flat in the conformal model (i.e., an offset k-dimensional linear subspace of Eⁿ). We do so by rewriting the blade to a form that we mostly recognize from the homogeneous model. This is done in three steps: standardization, interpretation, and generalization.

**Standardization**

By the structure preservation principle, we still have the general form if we take p₀ to be the arbitrary origin o (and we can view this either as moving the whole blade X back to the origin to make p₀ coincide with o, or as choosing p₀ as the origin of our representation). Note that the invariance of ∞ is essential (if it changed under translation, the form of the expression would not be the same at the origin). So we have reduced the element X to

$$X = \alpha(o \wedge p_1 \wedge \cdots \wedge p_k \wedge \infty)$$

Now because the outer product is antisymmetric, we can subtract one of the factors from each of the others without changing the value of the product (the extra terms would produce zero, a∧b = a∧(b−a) being the prime example). We subtract o, and get the element X into the form:

$$X = \alpha\left(o \wedge (p_1 - o) \wedge \cdots \wedge (p_k - o) \wedge \infty\right)$$

We substitute the general form of the point representation of (13.3), setting pᵢ = o + **pᵢ** + ½**pᵢ**²∞, to obtain:

$$X = \alpha\left(o \wedge (\mathbf{p}_1 + \frac{1}{2}\mathbf{p}_1^2\infty) \wedge \cdots \wedge (\mathbf{p}_k + \frac{1}{2}\mathbf{p}_k^2\infty) \wedge \infty\right)$$

The outer product with ∞ eliminates the extra terms ½**pᵢ**²∞. So we have:

$$X = \alpha(o \wedge \mathbf{p}_1 \wedge \cdots \wedge \mathbf{p}_k \wedge \infty)$$

We can now reduce the part involving the vectors **pᵢ** to a purely Euclidean k-blade **Aₖ**, into which we also absorb the weight α, defining **Aₖ** = α**p₁** ∧ ··· ∧ **pₖ**. We therefore ultimately find that this class of blade is equivalent to:

$$X = o \wedge \mathbf{A}_k \wedge \infty$$

a much simplified form.

**Interpretation**

To find the Euclidean interpretation of X = o ∧ **Aₖ** ∧ ∞ as a direct blade, we probe it with a point x and solve x ∧ (o ∧ **Aₖ** ∧ ∞) = 0; that should give the set of Euclidean points it represents. Let us bring this into a more familiar form by expanding x as o + **x** + ½**x**²∞. We immediately realize that the outer products with o and ∞ eliminate the first and last term of this point representation, so we effectively can substitute x = **x** without changing the solution:

$$0 = x \wedge o \wedge \mathbf{A}_k \wedge \infty = \mathbf{x} \wedge o \wedge \mathbf{A}_k \wedge \infty$$

Therefore we need to solve **x** ∧ o ∧ **Aₖ** ∧ ∞ = 0. This equation contains a purely Euclidean part (**x** ∧ **Aₖ**) and a non-Euclidean part (o ∧ ∞). These are orthogonal, so that their outer product is a geometric product, and we have (o ∧ ∞)(**x** ∧ **Aₖ**) = 0 (absorbing a sign into the zero). The model bivector o∧∞ is not zero, so we must have **x**∧**Aₖ** = 0 (if you do not trust this reasoning, take the contraction of the original equation with o ∧ ∞ to eliminate the non-Euclidean part, and use (o ∧ ∞)⌋(o ∧ ∞) = (∞ · o)² = 1). But the result

$$\mathbf{x} \wedge \mathbf{A}_k = 0$$

is a simple equation from the vector space model. It involves purely Euclidean vectors and implies that **x** is in the blade spanned by **Aₖ**. Therefore the blade X = o∧**Aₖ**∧∞ represents a flat k-dimensional subspace through the origin o.

**Generalization**

We have found that flats through the origin are part of the conformal model, and since the Euclidean transformations are structure-preserving, all their translations and rotations should be in the model as well.

To find the general form of a k-dimensional flat through a point p, we need to translate o ∧ **Aₖ** ∧ ∞ using the versor T_p. Since this is a versor, we can distribute it over the terms o, **Aₖ**, and ∞. The first and the last are easy: T_p applied to o is p, and ∞ is invariant, so the translation of X is p ∧ T_p[**Aₖ**] ∧ ∞. The translation of the Euclidean k-blade **Aₖ** requires some care:

$$\mathsf{T}_\mathbf{p}[\mathbf{A}_k] = (1 - \mathbf{p}\infty/2)\mathbf{A}_k(1 + \mathbf{p}\infty/2)$$
$$= \mathbf{A}_k - \frac{1}{2}(\mathbf{p}\infty\mathbf{A}_k - \mathbf{A}_k\mathbf{p}\infty) - \mathbf{p}\infty\mathbf{A}_k\mathbf{p}\infty/4$$
$$= \mathbf{A}_k + \frac{1}{2}\infty(\mathbf{p}\mathbf{A}_k - \mathbf{A}_k\mathbf{p}) + 0$$
$$= \mathbf{A}_k + \infty(\mathbf{p} \rfloor \mathbf{A}_k) = -\mathbf{p} \rfloor (\infty\mathbf{A}_k) \tag{13.7}$$

where p = T_p[o]. The final form is a multiplicative rewriting convenient for later computations. For our present purpose, the penultimate form is more convenient. Substituting it in p ∧ T_t[**Aₖ**] ∧ ∞, we find that its ∞-component is killed by the outer product with ∞, so that the general form of a flat k-dimensional offset subspace passing through p is

$$\text{direct } \mathbf{A}_k\text{-flat through } p: \quad p \wedge \mathbf{A}_k \wedge \infty \tag{13.8}$$

Elements of this kind are depicted in Figure 13.2.

> **Figure 13.2:** Flat elements in the conformal model: the plane p∧q∧r∧∞ (with its orientation denoted by the circle), the line s ∧ t ∧ ∞, and the flat point u ∧ ∞ at their intersection.

We see that a directly represented flat X in the conformal model always contains the point at infinity, so it satisfies ∞ ∧ X = 0. In the origin, you can easily verify that X² = X̃X = −**Aₖ**² ≠ 0, and since that is an invariant property, this holds anywhere. These two conditions characterize the blades representing a direct flat.

### 13.3.2 Correspondence with the Homogeneous Model

This expression p ∧ **Aₖ** ∧ ∞ for a general direct flat in the conformal model is nicely backwards compatible with the homogeneous model. We can see this most clearly by trying to determine its meaning directly (without using the versor properties to bring things to the origin, as we did above). So we need to solve 0 = x ∧ (p ∧ **Aₖ** ∧ ∞); it simplifies by the following steps:

$$0 = x \wedge (p \wedge \mathbf{A}_k \wedge \infty)$$
$$= (o + \mathbf{x} + \frac{1}{2}\mathbf{x}^2\infty) \wedge (o + \mathbf{p} + \frac{1}{2}\mathbf{p}^2\infty) \wedge \mathbf{A}_k \wedge \infty$$
$$= (o + \mathbf{x}) \wedge (o + \mathbf{p}) \wedge \mathbf{A}_k \wedge \infty$$
$$= \left(o \wedge (\mathbf{p} - \mathbf{x}) + \mathbf{x} \wedge \mathbf{p}\right) \wedge \mathbf{A}_k \wedge \infty$$
$$= o \wedge (\mathbf{p} - \mathbf{x}) \wedge \mathbf{A}_k \wedge \infty + \mathbf{x} \wedge (\mathbf{p} - \mathbf{x}) \wedge \mathbf{A}_k \wedge \infty$$

The linear independence of the two terms implies that they should each be zero to make the total zero. The orthogonality of o ∧ ∞ to the Euclidean parts makes setting the first term equal to zero equivalent to solving the single equation (**p** − **x**) ∧ **Aₖ** = 0. The second term is then also zero, so this is the general solution. We indeed have an offset flat with direction element **Aₖ** passing through the point at **p**.

After the first two steps, this derivation is completely analogous to the computation in the homogeneous model:

$$0 = (e_0 + \mathbf{x}) \wedge (e_0 + \mathbf{p}) \wedge \mathbf{A}_k$$
$$= \left(e_0 \wedge (\mathbf{p} - \mathbf{x}) + \mathbf{x} \wedge \mathbf{p}\right) \wedge \mathbf{A}_k$$
$$= \left(e_0 \wedge (\mathbf{p} - \mathbf{x}) + \mathbf{x} \wedge (\mathbf{p} - \mathbf{x})\right) \wedge \mathbf{A}_k$$

The metric properties of o or e₀ (which are very different: o² = 0 while e₀² = ±1) do not enter the solution process, they only serve as bookkeeping devices for the outer product.

This equivalence of the derivations worked because the outer product with ∞ removed the terms involving the squared vectors from the point representation. We have demonstrated an important relationship between the two models:

> **The homogeneous model is embedded in the conformal model as governing the behavior of the blades involving a factor ∞. These represent offset flat subspaces.**

Pushing this equivalence, a homogeneous point p is found in the conformal model as the element p∧∞, which must be a flat point. It contains both the conformal point representative p and the point at infinity ∞. Such flat points occur as the result of the intersection of a line and a plane, which actually contains two common points: the finite intersection point and the point at infinity. An example is the point u ∧ ∞ in Figure 13.2. In containing this infinite aspect, they are subtly different from the point p itself, which is a dual sphere with zero radius, as we saw in Section 13.1.3. Separating these algebraically is natural in the conformal model and cleans up computational aspects. But we readily admit that these two conceptions of what still looks like a point in the Euclidean space Eⁿ do take some getting used to.

Anyway, if you want the line through the points p and q, this is the 2-blade p_H ∧ q_H in the homogeneous model (where p_H and q_H are the homogeneous representatives), and the 3-blade Λ = p∧q∧∞ in the conformal model. It can be re-expressed as p∧(q−p)∧∞ = p∧(**q**−**p**)∧∞ ≡ p∧**a**∧∞, so the line passing through p with direction vector **a** is p∧**a**∧∞, just as it would have been p_H ∧ **a** in the homogeneous model. Our flexible computational rerepresentation techniques from the homogeneous model therefore still apply without essential change. In the conformal model, too, lines and planes can be represented by a mixture of locations and/or directions, with the outer product as universal construction operation.

### 13.3.3 Dual Representation of Flats

The dual representation of flats is simply found by dualization. As a pseudoscalar for the representational space ℝⁿ⁺¹·¹ we use the blade representing the full Euclidean space as a flat, so

$$\text{pseudoscalar of conformal model: } I_{n+1,1} \equiv o \wedge I_n \wedge \infty$$

where Iₙ is the Euclidean unit pseudoscalar. As in the homogeneous model, we will denote the dualization in the full representational space by a six-pointed star (as X*) and the dualization in its Euclidean part by a five-pointed star (as X⋆, typically done on a purely Euclidean element).

Dualization in geometric algebra involves the inverse of the unit pseudoscalar. In the strange metric of the representational space ℝⁿ⁺¹·¹, this is not equal to the reverse of I_{n+1,1}. The reason boils down to a property of the 2-blade o ∧ ∞. For we have

$$(o \wedge \infty)(o \wedge \infty) = (o\infty + 1)(o\infty + 1) = o\infty o\infty + 2o\infty + 1 = 1$$

so that the o ∧ ∞ is its own inverse. (The final step involves a computation highlighted in structural exercise 2.) The inverse of the pseudoscalar is then easily verified to be

$$I_{n+1,1}^{-1} = o \wedge I_n^{-1} \wedge \infty$$

so this is what we should use for dualization. It is satisfactory that the embedding of the Euclidean model is such that the inverse of the representation of the Euclidean pseudoscalar is the representation of the inverse. This is of course related to the general structure preserving properties of the conformal model. We did not have this property in the homogeneous model, where $(e_0 I_n)^{-1} = I_n^{-1} e_0^{-1} = (-1)^n e_0^{-1} I_n^{-1}$, involving an extra sign in odd dimensions. Because we have two extra representational dimensions in the conformal model (rather than just one), we can avoid those extraneous signs.

The structure-preserving property of the duality implies that we can make the dual of the standard flat through the origin and then translate it to the location of the desired flat to obtain its dual. This is permitted, for the structure preservation

$$\mathsf{V}[X]^* = \mathsf{V}[X^*]$$

holds for any even versor, especially for Euclidean motions. In the conformal model, we do not need to know whether an element is a direct or a dual representation to move it in a Euclidean manner by an even versor. This is an improvement over the homogeneous model. (However, in structural exercise 4, we ask you to show that there is an additional minus sign for an odd versor. So there is a small difference between reflections and motions.)

Dualizing the origin blade o ∧ **Aₖ** ∧ ∞, we find

$$(o \wedge \mathbf{A}_k \wedge \infty)^* = (o \wedge \mathbf{A}_k \wedge \infty) \rfloor (o \wedge I_n^{-1} \wedge \infty)$$
$$= -(o \wedge \mathbf{A}_k) \rfloor (I_n^{-1} \wedge \infty)$$
$$= -o \rfloor (\mathbf{A}_k^\star \wedge \infty)$$
$$= \bar{\mathbf{A}}_k^\star$$

Note that the grade inversion extends over the Euclidean dual, so it gives a sign of (−1)^{n−k}. The dual of a blade in the homogeneous model involved a similar sign change, so we are still backwards compatible in the dualization.

But in contrast to the homogeneous model (see Section 11.8.2), translations on dual blades are performed by the same operation as translations on direct blades: simply apply the translation versor. We have already computed the translation of a purely Euclidean element in (13.7), so the result is immediate:

$$\text{dual flat: } \mathsf{T}_\mathbf{p}[\bar{\mathbf{A}}_k^\star] = \bar{\mathbf{A}}_k^\star + \infty(\mathbf{p} \rfloor \bar{\mathbf{A}}_k^\star) = -\mathbf{p} \rfloor (\mathbf{A}_k^\star\infty) \tag{13.9}$$

This makes it particularly easy to construct, say, the dual representation of a hyperplane with 2-blade **I** and associated normal **n** = **I**⋆, passing through p: it is Π* = −p⌋(**n**∞) = −**n** − (**p** · **n**)∞. This confirms our earlier result of Table 13.2, though the sign is now properly related to a properly oriented plane Π and a well-defined pseudoscalar in the dualization process.

Direct representations of flats contain a factor ∞ and are therefore characterized by ∞ ∧ X = 0. Dualization of this condition yields that a blade X* representing a dual flat is characterized by ∞ ⌋ X* = 0. This is of course interpreted to mean that the point at infinity is contained in the element dually represented by X. The condition itself is invariant under Euclidean transformations, because ∞ is. The other property of a direct flat, X² < 0, dualizes to X*² > 0 for the dual representation.

### 13.3.4 Directions

In the construction of the direct flat p∧**Aₖ**∧∞, we recognize the location p and the blade **Aₖ** ∧ ∞. Bearing in mind how the conformal flats correspond to their representations in the homogeneous model, such an element **Aₖ** ∧ ∞ must be the conformal representation of a k-dimensional direction:

$$\text{directly represented direction: } \mathbf{A}_k \wedge \infty$$

To be a pure direction, it should only have directional properties and no locational aspects. It is easy to verify how it transforms under a general Euclidean motion consisting of a rotation R and a translation T:

$$\mathsf{T}_\mathbf{t}[\mathsf{R}[\mathbf{A}_k \wedge \infty]] = \left(\mathsf{R}[\mathbf{A}_k] - (\mathbf{t} \rfloor \mathsf{R}[\mathbf{A}_k])\infty\right) \wedge \infty = \mathsf{R}[\mathbf{A}_k] \wedge \infty$$

So these elements of the form **Aₖ** ∧ ∞ are rotation covariant, but translation invariant. That is precisely what you would expect from directions. The dual directions are simply their duals:

$$\text{dual direction: } (\mathbf{A}_k \wedge \infty)^* = (\mathbf{A}_k \wedge \infty) \rfloor (o \wedge I_n^{-1} \wedge \infty) = -\bar{\mathbf{A}}_k^\star \wedge \infty$$

again involving signs that should be observed if you want to use them in consistently oriented computations. They are clearly also translation invariant.

You can make a flat by attaching a direction element to a point p using an outer product, as in p ∧ (**Aₖ** ∧ ∞). The corresponding dual flat is made by attaching the dual direction to the point p using the contraction, giving p⌋(−**Āₖ**⋆∞) in agreement with (13.9).

A direction element X is characterized by containing ∞, so that ∞ ∧ X = 0, and moreover by having a zero norm: X² = 0, as you can easily verify. A dual direction X* has ∞⌋X* = 0 and X*² = 0.

---

## 13.4 Application: General Planar Reflection

In classical texts on subjects like computer graphics, many crucial formulas are given in a Euclidean or homogeneous-coordinate form. How are we to integrate those into the new conformal model? This is often surprisingly straightforward, since the more familiar vector space model and the homogeneous model are both naturally contained in the conformal model. All that is required is recasting of standard formulas into a geometric algebra format before you perform the embedding. You then find that the conformal model gives you the freedom to generalize the formulas, in a manner that the other models did not allow. The reason, as always, is the versor form of the Euclidean transformations and its associated structure-preserving properties.

As an application, let us consider the reflection of a general line Λ in a general plane π. See Figure 13.3.

> **Figure 13.3:** Reflection of a line Λ in a (dual) plane π in the conformal model. This is derived from the reflection of a vector **u** in a normal vector **n** in the origin, according to the vector space model (also depicted).

- **Classical Linear Algebra.** In the classical way of doing this, you would have to treat positions and orientations separately. The intersection point q of Λ and π determines a point on the outgoing line. For its direction vector, you would reflect the direction **u** of Λ relative to the normal vector **n** of the plane. This would refer to a Euclidean formula such as

  $$\mathbf{u} \to \mathbf{u}' = \mathbf{u} - 2(\mathbf{u} \cdot \mathbf{n})\mathbf{n}$$

  You would then reassemble the position q and the transformed direction **u'** and return that as the transformed line, in some data format.

- **Vector Space Model.** In the vector space model of geometric algebra, we can start from the same formula, since all quantities belong to it. We have seen in Section 7.1 how this can be reformulated to geometric algebra by introducing the geometric product, giving

  $$\mathbf{u} \to -\mathbf{n}\mathbf{u}\mathbf{n} = -\mathbf{n}\mathbf{u}/\mathbf{n} \tag{13.10}$$

  (we introduced the division to waive normalization of **n**.) This is clearly a versor product, and the embedding in the geometric algebra of the vector space model gives us the automatic extension to the reflection of any blade in the Euclidean model, not just a direction vector **u**.

- **Homogeneous Model.** In the homogeneous model we can combine the directional and locational aspects of the line in one data structure, a 2-blade. We can use that blade to compute the intersection point, but we still need to isolate the direction vector to perform the reflection (by the same formula as the vector space model). We can then compose the resulting line from the intersection point and the new reflected direction as a resulting 2-blade in the homogeneous model.

- **Conformal Model.** In the conformal model, we can completely skip determining the intersection point. Instead, we extend the reflection formula (13.10) from the vector space model directly from merely working on directions to acting on the whole line, in the following manner.

  We first note that the formula also holds in the conformal model, since the vector space model is contained in it. The direction vector **n** is now recognized as a dual plane through the origin, and this is the plane Π of the original problem, as long as we accept for the moment that it passes through the origin. We write this special plane as Π_o, dually represented by π_o = **n**. We want the vector **u** to represent the direction of the line Λ_o also passing through the origin. This implies that the line should be represented as Λ_o = o ∧ **u** ∧ ∞.

  Let us now extend the reflection formula of (13.10) to this element Λ_o. This is straightforward, since o and ∞ are invariants of the reflection in π_o, and the versor structure of the conformal model does the rest.

  $$o \wedge (-\mathbf{n}\mathbf{u}/\mathbf{n}) \wedge \infty = (-\mathbf{n}o/\mathbf{n}) \wedge (-\mathbf{n}\mathbf{u}/\mathbf{n}) \wedge (-\mathbf{n}\infty/\mathbf{n})$$
  $$= \hat{\mathbf{n}}(o \wedge \mathbf{u} \wedge \infty)/\mathbf{n}$$

  (We wrote the formula using the grade involution ^, since there are obviously as many signs as the grade of Λ_o and this will help the further generalization below.) So we now have a formula that reflects a line Λ_o through the origin in a dual plane π_o through the origin:

  $$\Lambda_o \to \hat{\pi}_o \Lambda_o / \pi_o$$

  Since this formula consists only of geometric products, it is clearly translation covariant. So moving both to a general position using the Euclidean rigid body motion V (first a rotation then a translation), we get a formula for a general line Λ = V[Λ_o] and a general dual plane π = V[π_o]

  $$\Lambda = \mathsf{V}[\Lambda_o] \to \mathsf{V}[\hat{\pi}_o\Lambda_o/\pi_o] = \mathsf{V}[\pi_o]\widehat{\mathsf{V}[\Lambda_o]}/\mathsf{V}[\pi_o] = \hat{\pi}\Lambda/\pi$$

  Under this motion, the original intersection point o moves to V[o], but the final result holds whether we know the intersection point explicitly or not. So the reflection of a line Λ in a dual plane π in general is

  $$\Lambda \to \hat{\pi}\Lambda/\pi$$

  in all its aspects of location and direction. It can do this without actually computing the intersection point, and that is an improvement over both the vector space model and the homogeneous model. (If you really want to compute the intersection point, the meet of the plane Π and the line Λ is the flat point Λ ∩ Π = π⌋Λ.)

The result is clearly only the special case for a line of the general reflection formula that reflects any directly represented flat space in an arbitrary plane:

$$X \to \hat{\pi}X/\pi \tag{13.11}$$

You see how much work the nice algebraic structure saves to transfer formulas, as well as providing clear insights in why they hold, and how to extend them. Classical geometrical results, typically formulated in the vector space model, are naturally embeddable within the conformal model. Moreover, we don't have to spell them all out: with a bit of practice and confidence, such transfers become one-liners. In the example above, you know that o is never special, so that (13.11) is the only actual computation to get to the general case. You may even learn to guess the result (which was clearly possible in the example above based on the pattern in reflection formulas in Table 7.1), and merely verify the correctness with interactive software (moving its constituents around to check its structure preservation, and the correctness of weights). That is how we ourselves typically design formulas for specific tasks, and the method is justified by virtue of the structure preservation properties of the conformal model.

Incidentally, (13.11) is the reflection formula used in the motivating example of Section 1.1.

---

## 13.5 Rigid Body Motions

We have seen in Section 13.2 how the conformal model represents the Euclidean transformations as versors. Of special interest are the Euclidean rigid body motions, represented by even versors that can be normalized to rotors. We explore their structure, culminating in a closed-form logarithm useful for interpolation of rigid body motions.

### 13.5.1 Algebraic Properties of Translations and Rotations

The rotor T_t = exp(−**t**∞/2) = (1−**t**∞/2) has all the desirable properties of a translation versor. The occurrence of the null vector ∞ makes translation versors combine in an additive manner in terms of its vector parameter **t**, since it kills any terms that might contain the combination of translations:

$$T_\mathbf{s} T_\mathbf{t} = (1 - \mathbf{s}\infty/2)(1 - \mathbf{t}\infty/2) = 1 - \mathbf{s}\infty/2 - \mathbf{t}\infty/2 + \mathbf{s}\infty\mathbf{t}\infty/4 = 1 - (\mathbf{s} + \mathbf{t})\infty/2 = T_{\mathbf{s}+\mathbf{t}}$$

You may contrast this with the much more complicated composition of rotations, which we saw in Section 7.3. That was essentially the geometric algebra version of the quaternion product (in 3-D), extended to n-D. It, too, is automatic from the rotor representation of the rotation, but the result was in essence an addition of arcs on the rotation sphere, involving severe trigonometry in a coordinate representation.

The algebraic nature of the bivector in the exponent of these rotors is the crucial difference that makes us experience them so differently geometrically: when it has a negative square, it generates rotations, which do not commute and involve trigonometry, and when it has a zero square, it generates translations, which do commute and remain additive. We will meet the remaining possibility of a positive square later (in Section 16.3, where we show that they are scalings and involve hyperbolic functions).

The versor structure of the conformal model means that not only elements like flats and directions transform easily, but so do the versors themselves. A consequence of the properties of translations is that translations are translation invariant: a translated translation rotor acts in the same manner as the original rotor, for

$$\mathsf{T}_\mathbf{s}[T_\mathbf{t}] = T_\mathbf{s} T_\mathbf{t} T_\mathbf{s}^{-1} = T_\mathbf{s} T_\mathbf{t} T_{-\mathbf{s}} = T_{\mathbf{s}+\mathbf{t}-\mathbf{s}} = T_\mathbf{t}$$

(Note that T denotes the translation rotor, whereas T[ ] denotes the translation operator!) This invariance property is why we feel so free to draw the translation vector anywhere, attached to any point we like in the same manner. By contrast, rotations are not rotation invariant:

$$\mathsf{R}_{\mathbf{J}\psi}[R_\mathbf{I}] = R_{\mathsf{R}_{\mathbf{J}\psi}[\mathbf{I}]}$$

and therefore the total rotation rotates in the R_{Jψ}-rotated plane **I**, not in the original plane **I**. (Again, R denotes the rotation rotor, while R[ ] denotes the rotation operator.)

When we translate a rotation rotor R_I = exp(−**I**π/2), by a translation rotor T_t, this has the same effect as shifting the rotation 2-blade by the translation T_t:

$$\mathsf{T}_\mathbf{t}[R_\mathbf{I}] = R_{\mathsf{T}_\mathbf{t}[\mathbf{I}]}$$

In 3-D space, this is particularly striking. The rotation 2-blade is the inverse dual of the rotation axis Λ_o also passing through the origin, since Λ_o = **I**⋆. Originally, the axis passes through the origin; after the translation the new axis Λ has become T_t[Λ_o]. But the property that the rotation rotor is the exponent of the dual line is covariant, so the new rotation rotor is simply the exponent of the new dual axis Λ:

$$\text{3-D rotation around line } \Lambda \text{ over angle } \phi: \quad R = e^{-\Lambda^{-*}\phi/2} = e^{\Lambda^*\phi/2}$$

(Make sure you normalize the axis Λ so that the angle φ has the intended meaning.)

In Chapter 7, we showed that the 3-D rotation rotors around the origin were the geometric algebra way of doing quaternions, in what we now recognize was the vector space model. That had the advantage of embedding quaternions in a real computational framework, but did not add any computational power. In the conformal model, the concept of a quaternion is greatly extended. In 3-D, the extension encompasses the general rotation axis for an arbitrary rotation to encode the rotation. (In n-D, it still signifies the 2-blade of the rotational bivector, though this does then not dualize to a single axis.) This relationship to the rotation axis is very compact and convenient in applications. You have met it first in our motivating example in Section 1.1.

### 13.5.2 Screw Motions

A translated rotation is not yet the general rigid body motion, for it lacks a translation component along the rotation axis. So we would have to supply that separately, to obtain the general rigid body motion as

$$T_\mathbf{w} \mathsf{T}_\mathbf{v}[R_\mathbf{I}]$$

where **v** is a vector in the plane **I** (so that **v** ∧ **I** = 0), and **w** is vector perpendicular to it (so that **w**⌋**I** = 0).

Such a decomposition of a rigid body motion gives us a better understanding of what it does, and we can execute the two parts (translation along the axis and rotation around the axis) in any order or simultaneously. When we do them in similar amounts to reach a total resulting rigid body motion, we obtain a **screw motion**, as depicted in Figure 13.4. The simultaneous rotation and translation (around and along the spatial axis) are then related through the pitch of the screw. According to **Chasles' theorem**, an arbitrary rigid body motion can be represented in this manner. Given a general rigid body motion, we can compute the location and magnitude of the elements of the screw using the conformal model. Perhaps surprisingly, it completely avoids the rather involved trigonometry.

> **Figure 13.4:** The computation of the screw corresponding to a rotor R followed by a translation over **t**. The rotor plane and angle are indicated by the blue disk. The translation **w** along the screw axis is the rejection of **t** by the rotation plane. The location vector **v** of the axis is found as the unique vector in the rotation plane whose chord under rotation is parallel to **w** − **t** (indicated by a thin blue line). The resulting screw motion around the axis (in black) is shown applied to a tangent bivector (in fading shades of green).

First, assume that we have a general rigid body motion T_t R_I composed of a standard rotation in a plane **I** at the origin, followed by a translation. This is the usual way to decompose rigid body motions, which we already encountered in the homogeneous model (in Section 11.8.5). It corresponds well to the homogeneous coordinate matrices for rigid body motions. Following Chasles, we attempt to rewrite this rigid body motion as a displaced rotation around a displaced axis parallel to **I**⋆, with its location characterized by a vector **v** (which we can take to be in the **I**-plane without loss of generality), followed by a translation **w** in the direction of that axis. We saw this form of the motion above, and therefore find that we need to solve

$$T_\mathbf{t} R_\mathbf{I} = T_\mathbf{w} \mathsf{T}_\mathbf{v}[R_\mathbf{I}]$$

for **v** and **w**, where **v** ∧ **I** = 0 and **w**⌋**I** = 0. The two factors on the right-hand side should commute, since we can do the translation along the displaced axis before or after a rotation around it. Actually, that demand on commutation is an equivalent, more algebraic way of phrasing the problem, from which the conditions on **v** and **w** relative to **I** follow.

The Euclidean blade **I** characterizing the direction of the rotation plane can be computed as the normalization of ⟨R⟩₂. Since the only translation perpendicular to **I** is performed by **w**, we must have that **w** is the rejection of the translation vector **t** by **I**:

$$\mathbf{w} = (\mathbf{t} \wedge \mathbf{I})/\mathbf{I}$$

That leaves the other part of the translation (**t**⌋**I**)/**I**. Call it **u** for the moment. The problem is now reduced to a 2-D problem in the **I**-plane, namely that of solving for **v** in

$$T_\mathbf{u} R_\mathbf{I} = T_\mathbf{v} R_\mathbf{I} T_{-\mathbf{v}}$$

We would like to swap the rightmost translation with R_I. We derive the following swapping rule (abbreviating R_I to R for convenience):

$$RT_{-\mathbf{v}} = R(1 + \mathbf{v}\infty/2) = (1 + R\mathbf{v}\infty\tilde{R}/2)R = (1 + R\mathbf{v}\tilde{R}\infty/2)R = T_{-R\mathbf{v}\tilde{R}}R \tag{13.12}$$

We also observe that since **v** is a vector in the R-plane, we have

$$\mathbf{v}R = \mathbf{v}(\langle R\rangle_0 + \langle R\rangle_2) = (\langle R\rangle_0 - \langle R\rangle_2)\mathbf{v} = (\langle \tilde{R}\rangle_0 + \langle \tilde{R}\rangle_2)\mathbf{v} = \tilde{R}\mathbf{v}$$

Therefore,

$$T_\mathbf{u} R = T_\mathbf{v} R T_\mathbf{v} = T_\mathbf{v} T_{-R\mathbf{v}\tilde{R}} R = T_{\mathbf{v}-R\mathbf{v}\tilde{R}} R = T_{(1-R^2)\mathbf{v}} R$$

It follows that

$$\mathbf{v} = (1 - R^2)^{-1}\mathbf{u} = (1 - R^2)^{-1}(\mathbf{t} \rfloor \mathbf{I})/\mathbf{I} \tag{13.13}$$

Graphically, the vector **v** − R**v**R̃ = 2(**v**⌋R)/R occurring in this computation is the chord connecting the rotated **v** to the original **v**. We should find **v** such that this equals **u**, which gives the construction in Figure 13.4 as the geometric interpretation of this algebraic computation. To pull it all together, the final result giving the screw parameters is:

$$\text{screw decomposition: } T_\mathbf{t} R_\mathbf{I} = T_{(\mathbf{t}\wedge\mathbf{I})/\mathbf{I}} \mathsf{T}_{(1-R_\mathbf{I}^2)^{-1}(\mathbf{t}\rfloor\mathbf{I})/\mathbf{I}}[R_\mathbf{I}]$$

Realize again that T denotes a translation rotor, whereas T[ ] denotes a translation operator!

### 13.5.3 Logarithm of a Rigid Body Motion

Using Chasles' theorem, we can determine the logarithm of a rigid body motion rotor V, which means that we can determine the bivector when we have been given the rotor. For such a rotor is, on the one hand,

$$V = T_\mathbf{t} R_\mathbf{I} = (1 - \mathbf{t}\infty/2)R_\mathbf{I} = R_\mathbf{I} - \frac{1}{2}\mathbf{t}R_\mathbf{I}\infty \tag{13.14}$$

and on the other hand,

$$V = T_\mathbf{w} R_{\mathsf{T}_\mathbf{v}[\mathbf{I}]} = e^{-\mathbf{w}\infty/2}e^{-\mathsf{T}_\mathbf{v}[\mathbf{I}]\phi/2} = e^{-\mathbf{w}\infty/2 - \mathsf{T}_\mathbf{v}[\mathbf{I}]\phi/2}$$

in which the addition of the exponents is only permitted because the rotors commute. They were designed that way by Chasles' theorem, and it is the algebraic consequence of the possibility to execute the screw as one smooth motion. Substituting the values of **w** and **v** we found above, the requested rigid body motion logarithm is

$$\log(T_\mathbf{t} R_\mathbf{I}) = -((\mathbf{t} \wedge \mathbf{I})/\mathbf{I})\infty/2 + \mathsf{T}_{(1-R^2)^{-1}(\mathbf{t}\rfloor\mathbf{I})/\mathbf{I}}[-\mathbf{I}\phi/2]$$
$$= -((\mathbf{t} \wedge \mathbf{I})/\mathbf{I})\infty/2 + (1 - R^2)^{-1}(\mathbf{t} \rfloor \mathbf{I})\infty/2 - \mathbf{I}\phi/2 \tag{13.15}$$

The value of this expression can be determined via the computation of the screw parameters, provided that we can retrieve both R_I (which gives **I** by the logarithm of (10.14)) and **t** from the overall rotor V. But this retrieval is simple in (13.14):

$$R_\mathbf{I} = -o \rfloor (V\infty), \quad \mathbf{t} = -2(o \rfloor V)/R_\mathbf{I}$$

Putting all formulas together, we get the pseudocode of Figure 13.5. Special cases happen when R equals +1 or −1. When R equals +1, the motion is a pure translation versor and we just return the logarithm of that (which is −**t**∞/2). When R equals −1, there is no unambiguous logarithm, since a rotation of π within any plane could generate the −1. To prevent spurious terms in the product with the translation versor, one must choose a plane perpendicular to **t**. In 2-D, this is impossible, and the logarithm does not exist (as we intimated in Section 7.4.4). Having the logarithm of a rigid body motion is a powerful result. It permits us to interpolate these motions in a total analogy to the rotation interpolation procedure that we had in the vector space model. See Section 13.10.4 for an implementation.

```
log(V){
    R = −o ⌋ (V∞)
    t = −2(o ⌋ V)/R
    if (R == −1) return ("no unique logarithm")
    if (R == 1)
        log = −t∞/2
    else
        I = ⟨R⟩₂ / √(−⟨R⟩₂²)
        φ = −2 atan2(‖⟨R⟩₂‖/I, ⟨R⟩₀)
        log = (−(t ∧ I)/I + 1/(1 − R²)(t ⌋ I))∞/2 − Iφ/2
    endif
}
```

> **Figure 13.5:** Computation of the logarithm of a normalized rigid body motion rotor V. One may improve subsequent numerics by making sure to return a bivector by taking the grade-2 element by ⟨log⟩₂.

---

## 13.6 Application: Interpolation of Rigid Body Motions

According to Chasles' theorem, a rigid body motion can be viewed as a screw motion. It is then natural to interpolate the original motion by performing this screw gradually. Figure 13.6 shows how simple this has become: the ratio of two unit lines L₂ and L₁ defines the square of the versor that transforms one into the other (see structural exercise 9). Performing this motion in N steps implies using the versor

$$V^{1/N} = e^{\log(L_2/L_1)/(2N)}$$

Applying this versor repeatedly to the line L₁ gives the figure. It interpolates the transformation of L₁ into L₂ and extrapolates naturally. Note how all can be defined completely, and simply, in terms of the geometric elements involved. You do not need coordinates to specify how things move around. The same rotor V^{1/N} can of course be applied to any element that should move similarly to L₁.

> **Figure 13.6:** The interpolation and extrapolation of the rigid body motion transforming a spatial line L₁ into a line L₂ is done by repeated application of the versor exp(log(L₂/L₁)/(2N)). The screw nature of the motion is apparent.

Since the resulting logarithms are bivectors, they can be interpolated naturally themselves. This allows one to estimate how various points on a rigid body move, establish their motion bivectors, and average those to get an improved estimate of the motion. Such numerical estimation techniques for motions are now being developed.

---

## 13.7 Application: Differential Planar Reflections

Now that we have general planar reflections available in (13.11), we can redo the example of Section 8.5.2, in which we studied a rotating mirror and its reflected image using geometric differentiation. Before, we used what was effectively the vector space model and therefore could only work in the origin. Now we can treat the fully general planar rotation.

To restate the problem, we consider the reflection of an element X in the dual plane π (i.e., X → πX̂π⁻¹) in 3-D Euclidean space. We rotate the plane slightly around line Λ, and need to find out what this does to the reflection of X.

In Section 8.2.5, we performed the differential computation of such perturbed versors in completely general form, with as a result (8.6) for the bivector of the perturbation versor, given an original versor and a motion. We can apply this immediately, since the conformal model gives us these versors: the original versor is the reflection versor π, and the motion is exp(−Λ⁻*/2) with bivector Λ⁻*. Then according to application of (8.6), the versor displacing the reflection should have bivector

$$-2(\pi \times \Lambda^{-*})/\pi = -2(\pi \rfloor \Lambda^{-*})\pi = -2(\pi \rfloor \Lambda^{-*}) \wedge \pi = 2(\pi \wedge \Lambda)^* \wedge \pi \tag{13.16}$$

The geometric interpretation of π ∧ Λ is the plane perpendicular to π and containing the line Λ; then the interpretation of the total formula is that it is dual of the meet of this plane with the dual plane π (i.e., it is dual of the orthogonal projection of the line Λ onto the mirror π). This line is indicated in Figure 13.7(a). Since the bivector of the resulting perturbing versor is this dual line, that versor is a rotation around this projected line when the reflection plane changes. This is clear geometry, easily verified. When it rotates around this line, the perturbed element follows a curved path: first-order perturbations in versors can lead to element paths of second order.

We would have to do a second-order Taylor series on the position to achieve a similar effect, so not only are the versor perturbations structure-preserving but they also give us a much better approximation for the same effort. You can work out the angle of rotation of the perturbation in a similar way as in the origin-based treatment, again resulting in (8.11).

Note that this computation is not valid for large perturbations: doing the same construction on a perturbed mirror shows that the projected line changes (since it now needs to be on the perturbed mirror), and therefore the arc changes as well. In fact, it becomes a caustic, of which the above effectively computes the local osculating cylinder.

Because we have done the whole computation in the conformal model, we can substitute any of its other elements for X. Figure 13.7(b) shows the whole computation applied to a reflected line. After the next chapter you will not even hesitate to apply it to the reflection of a sphere, circle, or tangent blade.

> **Figure 13.7:** (a) The yellow planar mirror π reflects a point X to the point Xᵣ. The green line Λ rotates the mirror; the red curve shows the orbit of the reflection in 100 steps. In black is the first-order perturbation description of the orbit around Xᵣ. It is a rotation of Xᵣ around the blue line, which is the projection of the line Λ onto the mirror π, which follows the tangent circle to the true orbit. The first few black points keep pace with the red points, showing that the velocity is correct. Note that a first-order perturbation of the versor generates a second-order curve. Both the black and red curves are on the sphere X ∧ π* ∧ Λ* (perpendicular to both Λ and π), which has also been depicted, to make the spatial nature of the curves more obvious. (b) The same setup, merely replacing X by a line, to show the universality of constructions in geometric algebra. The black lines are again good first-order approximations to the exact results.

---

## 13.8 Further Reading

The conformal model was first introduced to the engineering community in 1999 [31], but its roots can be traced to the 19th century. We will give more specific references in the following chapters, when we have more a complete view of its contents and capabilities.

Commercial applications of conformal geometric algebra to model statics, kinematics and dynamics of particles and linked rigid bodies are protected by U.S. Patent 6,853,964, "System for encoding and manipulating models of objects" [32]. Anyone contemplating such applications should contact Alyn Rockwood or David Hestenes. The patent does not restrict use of conformal geometric algebra for academic research and education or other worthy purposes that are not commercial.

---

## 13.9 Exercises

### 13.9.1 Drills

These drills intend to familiarize you with the form of common geometric elements and their parameters in the conformal model. We recommend doing them by hand first, and check them with interactive software later.

1. Give the representation of a point p₁ with weight 2 at location **e₁** + **e₂**.
2. Give the representation of a point p₂ with weight −1 at location **e₁** + **e₃**, and compute its distance to p₁.
3. Give the representation of the line L through p₁ and p₂.
4. Compute weight and direction of the line L.
5. Compute the support point on the line L.
6. Give the direct representation of the plane Π through L and the unit point at the origin.
7. Compute the direction and support of the plane Π.
8. Give the representation of the translation over −**e₁** of the plane Π.
9. Compute the dual π of the plane Π. Compute its dual direction and its moment.
10. Compute the dual of the line L.

### 13.9.2 Structural Exercises

1. Show that on the {**e**,**ē**}-basis, the point p of (13.3) is represented as:

   $$\mathbf{p} = \mathbf{p} + \frac{1}{2}(1 - \mathbf{p}^2)\mathbf{e} + \frac{1}{2}(1 + \mathbf{p}^2)\bar{\mathbf{e}}$$

   In [33] and [15], you find the close relationship of this formula with stereographic projection spelled out as a way of visualizing of the conformal model. Unfortunately, it needs the two extra dimensions, so you can only visualize the model for a 1-D Euclidean space. We will provide a better visualization in Section 14.3.

2. Show that ∞o∞ = −2∞ and o∞o = −2o.

3. In structural exercise 5 of Section 11.12.2, we introduced barycentric coordinates using the homogeneous model. Using the correspondence between homogeneous model and conformal model, give expressions for the barycentric coordinates in terms of conformal points.

4. When studying dualization in combination with versors in the main text, we were mostly interested in the even versors, for which V[X]* = V[X*]. For odd versors, you should use V[X]* = −V[X*]. Derive both simultaneously by using the general versor transformation of (7.18), which is V[X] = (−1)^{xv}VXV⁻¹, to show that V[X]* = (−1)^v V[X*]. (Hint: What is the sign involved in swapping V⁻¹I_{n+1,1}⁻¹ to I_{n+1,1}⁻¹V⁻¹?)

5. For a pure translation versor T, the logarithm is easy to determine. Show that

   $$\log(T) = \frac{1}{2}(T - \tilde{T})$$

6. Write the logarithm of the rigid body motion of (13.15) in terms of the logarithm of the rotor R introduced in (10.14). Your goal is to eliminate all **I** or φ from the formula.

7. Show that the ratio of two flat points p ∧ ∞ and q ∧ ∞ is a translation rotor. What is the corresponding translation vector?

8. Show that the ratio of two general planes passing through a common point p is a rotation versor. Do this in 3-D; you can represent the plane with normal **n** dually as p⌋(**n** ∧ ∞). The ratio of two elements is of course identical to the ratio of their duals. What is the bivector angle of the rotation?

9. Show that the ratio of two lines p ∧ **n** ∧ ∞ and q ∧ **m** ∧ ∞ is a general rigid body motion. What are the screw parameters?

10. To get back to an issue raised in Section 8.2.2, with translation represented as a rotor you can indeed change the position of a point x arbitrarily within a multiplicative framework. Show that the transformation by a translation rotor T_t = exp(−**t**∞/2), when developed in the Taylor series expansion (8.3), generates an arbitrary additive change in the position of a point x.

---

## 13.10 Programming Examples and Exercises

The implementation of the conformal model of 3-D space is called `c3ga`. The basis of the representation space in this implementation is spanned by basis vectors `no`, `e1`, `e2`, `e3`, and `ni`, with the metric as in Table 13.1. As you notice, we write o and ∞ as `no` and `ni` in our code (short for null vector representing the origin and null vector representing infinity, respectively).⁵ This, finally, is the implementation of geometric algebra that is behind the code of Figure 1.2 in the introductory example of Section 1.1.

The implementation contains a large number of specialized multivector types. Table 13.3 lists the most important ones. We have so far only treated the flats, the directions (labeled "free" in the table), and the rigid body motion operators (the table uses "rotor" exclusively for a rotation versor, calling a translation rotor a "translator"). The other elements will be introduced in the next chapter.

The specialized multivector types are complemented by the matrix representation of outermorphisms (`om`) and a specialized matrix representation that works well with OpenGL (`omFlatPoint`).

In addition to the basis vectors, which are present as constants by default, `c3ga` also contains some extra constants (see Table 13.4).

A 2-D version of the conformal model implementation is also provided. It is named `c2ga` and has most of the same specialized multivector types as its 3-D counterpart, but of course lacks spheres, freeTrivectors, and so on. We use `c2ga` in Sections 14.9.1 and 15.8.2.

---

⁵ When pronounced in a sentence, `ni` should be emphatic and slightly higher than the other words, whereas `no` should sound like a man imitating a woman imitating a man's voice.

**Table 13.3:** A list of the most important specialized multivector types in `c3ga`.

| Name | Sum of Basis Blades |
|------|---------------------|
| `vector` | e1, e2, e3 |
| `point` | no, e1, e2, e3, ni |
| `normalizedPoint` | no = 1, e1, e2, e3, ni |
| `flatPoint` | e1∧ni, e2∧ni, e3∧ni, no∧ni |
| `pointPair` | no∧e1, no∧e2, no∧e3, e1∧e2, e2∧e3, e3∧e1, e1∧ni, e2∧ni, e3∧ni, no∧ni |
| `line` | e1∧e2∧ni, e1∧e3∧ni, e2∧e3∧ni, e1∧no∧ni, e2∧no∧ni, e3∧no∧ni |
| `dualLine` | e1∧e2, e1∧e3, e2∧e3, e1∧ni, e2∧ni, e3∧ni |
| `plane` | e1∧e2∧e3∧ni, e1∧e2∧no∧ni, e1∧e3∧no∧ni, e2∧e3∧no∧ni |
| `dualPlane` | e1, e2, e3, ni |
| `circle` | e2∧e3∧ni, e3∧e1∧ni, e1∧e2∧ni, no∧e3∧ni, no∧e1∧ni, no∧e2∧ni, no∧e2∧e3, no∧e1∧e3, no∧e1∧e2, e1∧e2∧e3 |
| `sphere` | e1∧e2∧e3∧ni, e1∧e2∧no∧ni, e1∧e3∧no∧ni, e2∧e3∧no∧ni, e1∧e2∧e3∧no |
| `dualSphere` | no, e1, e2, e3, ni |
| `freeVector` | e1∧ni, e2∧ni, e3∧ni |
| `freeBivector` | e1∧e2∧ni, e2∧e3∧ni, e3∧e1∧ni |
| `freeTrivector` | e1∧e2∧e3∧ni |
| `tangentVector` | no∧e1, no∧e2, no∧e3, e1∧e2, e2∧e3, e3∧e1, e1∧ni, e2∧ni, e3∧ni, no∧ni |
| `tangentBivector` | e1∧e2∧e3, e2∧e3∧ni, e3∧e1∧ni, e1∧e2∧ni, no∧e3∧ni, no∧e1∧ni, no∧e2∧ni, no∧e2∧e3, no∧e1∧e3, no∧e1∧e2 |
| `vectorE2GA` | e1, e2 |
| `vectorE3GA` | e1, e2, e3 |
| `bivectorE3GA` | e1∧e2, e2∧e3, e3∧e1 |
| `translator` | scalar, e1∧ni, e2∧ni, e3∧ni |
| `normalizedTranslator` | scalar=1, e1∧ni, e2∧ni, e3∧ni |
| `rotor` | scalar, e1∧e2, e2∧e3, e3∧e1 |
| `scalor` | scalar, no∧ni |

**Table 13.4:** Constants in `c3ga`.

| Name | Value |
|------|-------|
| `e1ni` | e1 ∧ ∞ |
| `e2ni` | e2 ∧ ∞ |
| `e3ni` | e3 ∧ ∞ |
| `noni` | o ∧ ∞ |
| `I3` | e1 ∧ e2 ∧ e3 |
| `I5` | o ∧ e1 ∧ e2 ∧ e3 ∧ ∞ |
| `I5i` | (o ∧ e1 ∧ e2 ∧ e3 ∧ ∞)⁻¹ |

### 13.10.1 Metric Matters

As a first experiment to confirm that `c3ga` uses the strange metric of the conformal model, we print out the metric of the five basis vectors:

```cpp
// get the basis vectors:
mv bv[5] = {no, e1, e2, e3, ni};
// ... (omitted)
for (int i = 0; i < 5; i++) {
    // ... (omitted)
    for (int j = 0; j < 5; j++) {
        printf(" % 1.1f", _Float(bv[i] << bv[j]));
    }
    printf("\n");
}
```

The output of this part of the example agrees with Table 13.1:

```
         no    e1    e2    e3    ni
no      0.0   0.0   0.0   0.0  -1.0
e1      0.0   1.0   0.0   0.0   0.0
e2      0.0   0.0   1.0   0.0   0.0
e3      0.0   0.0   0.0   1.0   0.0
ni     -1.0   0.0   0.0   0.0   0.0
```

The example also creates vectors **e** (denoted as `ep`) and **ē** (denoted as `em`) from `no` and `ni`, according to (13.6):

```cpp
// create 'e+' and 'e-'
dualSphere ep = _dualSphere(no - 0.5f * ni);
dualSphere em = _dualSphere(no + 0.5f * ni);
```

Note that `dualSphere` is now the specialized vector type that holds arbitrary 5-D vectors. The example continues to print out some information about **e** and **ē**. The output is

```
e+ = 1.00*no - 0.50*ni
e- = 1.00*no + 0.50*ni

The metric of e+ and e-:
e+ . e+ = 1.000000
e- . e- = -1.000000
e+ . e- = 0.000000
```

### 13.10.2 Exercise: The Distance Between Points

This example draws five (draggable) points, connected by lines, and prints distance labels halfway between each pair of points. The exercise is to complete the following code:

```cpp
const normalizedPoint &pt1 = g_points[i];
const normalizedPoint &pt2 = g_points[j];

// compute distance
// EXERCISE: fill in the code to compute the distance between pt1
// and pt2
float distance = 0.0;
```

> **Figure 13.8:** The output of the solution to Example 2.

Figure 13.8 shows sample output of the correct solution. If you want to write a robust solution, keep in mind that floating point roundoff error may cause values that should always be less than or equal to zero to turn up as a very small positive number. This may cause trouble when you hand this value (negated) to `sqrt()`.

### 13.10.3 Loading Transformations into OpenGL, Again

In this exercise we repeat the example from Section 12.5.1, but this time we use the conformal model. The goal is to build up the matrix representation of any outermorphism (in this case, a simple combination of translation and rotation) and to load that matrix into OpenGL.

> **Figure 13.9:** Example 4 in action. A trail of circles is drawn to visualize the interpolation of rigid body motions.

In the homogeneous version, we transformed the basis vectors **e₁**, **e₂**, **e₃**, and e₀, and used their images to initialize the matrix representation of the transform. We then loaded this matrix directly into OpenGL.

In the conformal model, the blades **e₁** ∧ ∞, **e₂** ∧ ∞, **e₃** ∧ ∞, and o ∧ ∞ are the closest equivalent to the aforementioned basis vectors of the homogeneous model, since that is how the two models relate to each other. Geometrically, these are the blades representing the basis directions, just as **e₁**, **e₂**, **e₃**, and e₀ were in the homogeneous model. Using this, the code to load our conformal outermorphism into OpenGL is

```cpp
// get translator and rotor
vectorE3GA t = _vectorE3GA(distance * e3);
normalizedTranslator T = exp(_freeVector(-0.5f * (t ^ ni)));
rotor &R = g_modelRotor;

// combine 'T' and 'R' to form translation-rotation versor:
TRversor TR = _TRversor(T * R);
TRversor TRi = _TRversor(inverse(TR)); // compute inverse

// compute images of basis blades e1^ni, e2^ni, e3^ni, no^ni:
flatPoint imageOfE1NI = _flatPoint(TR * e1ni * TRi);
flatPoint imageOfE2NI = _flatPoint(TR * e2ni * TRi);
flatPoint imageOfE3NI = _flatPoint(TR * e3ni * TRi);
flatPoint imageOfNONI = _flatPoint(TR * noni * TRi);

// create matrix representation:
omFlatPoint M(imageOfE1NI, imageOfE2NI, imageOfE3NI, imageOfNONI);

// load matrix representation into GL:
glLoadMatrixf(M.m_c);
```

In Section 16.10.1, we will perform the opposite operation of converting OpenGL matrices to conformal versors. We postpone this subject until we can properly handle (uniform) scaling, which is first introduced in Chapter 16.

### 13.10.4 Interpolation of Rigid Body Motions

Since we can now represent translation and rotation as exponentials of bivectors and have their logarithm available (see Section 13.5.3), we can interpolate them with ease. The example presented here is similar to the interpolation example treated in the context of the vector space model (Section 10.7.1), but the conformal model now allows us to do it properly.

First of all, we need an implementation of the logarithm of (normalized) translation-rotation versors. This is easily done given the pseudocode in Figure 13.5:

```cpp
dualLine log(const TRversor &V) {
    // isolate rotation & translation part:
    rotor R = _rotor(-no << (V * ni));
    vectorE3GA t = _vectorE3GA(-2.0f * (no << V) * inverse(R));

    const float EPSILON = 1e-6f;
    if (_Float(norm_e2(_bivectorE3GA(R))) < EPSILON * EPSILON) {
        // special cases:
        if (_Float(R) < 0.0f)
        {// R = -1
            // Get a rotation plane 'I', perpendicular to 't'
            bivectorE3GA I;
            if (_Float(norm_e2(t)) > EPSILON * EPSILON)
                I = _bivectorE3GA(unit_e(t << I3));
            else {
                // when t = 0, any plane will do
                I = _bivectorE3GA(e1^e2);
            }
            // return translation plus 360 degree rotation:
            return _dualLine(0.5f *(I * 2.0f * (float)M_PI - (t^ni)));
        }
        else
        { // R = 1;
            // return translation:
            return _dualLine(-0.5f *(t^ni));
        }
    }
    else { // regular case
        // compute logarithm of rotation part
        bivectorE3GA Iphi = _bivectorE3GA(-2.0f * log(R));
        // determine rotation plane:
        rotor I = _rotor(unit_e(Iphi));
        // compose log of V:
        return _dualLine(
            0.5f * (
                -(t ^ I) * inverse(I) * ni +
                inverse(1.0f - R * R) * (t << Iphi) * ni -
                Iphi));
    }
}
```

Note the slight misuse of the type system: the function returns a `dualLine`, which is officially a 2-blade. In general, the logarithm of a rigid body motion is not a 2-blade but a bivector. It just so happens that this bivector can be represented employing the same basis blades as for dual lines, so we can (ab-)use `dualLine` as the return type. That is a consequence of the additive decomposition. But if you would pass the output of this `log()` function to `draw()`, which can only draw blade, it will only draw a line if the screw happens to be a pure rotation.

The example interpolates from one random versor to the next. These versors are computed as the product of a random translation and a random translated rotation:

```cpp
void initRandomDest() {
    normalizedTranslator T1 = exp(_freeVector(randomBlade(2, 3.0f)));
    normalizedTranslator T2 = exp(_freeVector(randomBlade(2, 3.0f)));
    rotor R = exp(_bivectorE3GA(randomBlade(2, 100.0f)));
    g_destVersor = _TRversor(T1 * T2 * R * inverse(T2));
}
```

Interpolation between the versors is done using the following function, which is almost identical to the one used in Section 10.7.1:

```cpp
// interpolate between 'src' and 'dst', as determined by 'alpha'
TRversor interpolateTRversor(const TRversor &src,
    const TRversor &dst, mv::Float alpha) {
    // return src * exp(alpha * log(inverse(src) * dst));
    return _TRversor(src * exp(_dualLine(alpha *
        log(_TRversor(inverse(src) * dst)))));
}
```
