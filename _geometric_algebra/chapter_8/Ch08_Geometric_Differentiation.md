# Chapter 8: Geometric Differentiation

Differentiation is the process of computing with changes in quantities. When the changes are small, those computations can be linear to a good approximation, and it is not too hard to develop a calculus for geometry by analogy to classical analysis.

When formulated with geometric algebra, it becomes possible to differentiate not only with respect to a scalar (as in real calculus) or a vector (as in vector calculus), but also with respect to general multivectors and k-blades. The differentiation operators follow the rules of geometric algebra: they are themselves elements that must use the noncommutative geometric product in their multiplication when applied to other elements. As you might expect, this has precisely the right geometric consequences for the differentiation process to give geometrically significant results.

This chapter is a bit of a sideline to the main flow of thought in this book. Although the later chapters occasionally use differentiation in their examples, it is not essential. You can easily skip it at first reading, and move on to Part II on the modeling of geometries. We include the subject because it is important for geometric optimization and differential geometry. These techniques are beginning to appear in practical applications of geometric algebra.

---

## 8.1 Geometrical Changes by Orthogonal Transformations

The geometrical elements we have constructed are of various types, and within the context of the geometry they can change in different ways. Each of these kinds of changes should find their place in a suitably defined calculus for geometric elements.

**Orthogonal Transformations.** Elements of a geometry change when they are transformed, and the class of transformations that is permitted determines the kind of geometry one has. We are especially interested in Euclidean geometry and the accompanying transformations of rotation, reflection, and translation (and, by a stretch of the term Euclidean, scaling). We have already seen that rotations and reflections can be represented by versors, since they are orthogonal transformations. In Part II, we will show that it is possible to set up a model of Euclidean geometry so that translations and scaling are also representable by versors, which will unify the whole structure of operators.

Orthogonal transformations represented by versors thus become central to doing geometric algebra. Among these, we are especially interested in rotors, since they cause the smooth continuous changes that are typical of motions. In their representation as exponents of bivectors, the calculus of rotors is surprisingly easy to treat: all differentiation reduces to computing commutators with the bivectors of the transformations. This has a natural connection with the Lie algebras that are used classically to compute the calculus of continuous transformation groups.

**Parameterizations.** An element of the geometry is often parametrized in terms of other elements. A specific case is location-dependence, which is parameterization by the positional vector **x**, or time-dependence on a scalar time parameter τ. A more involved instance of parameterization is explicit geometric relational dependence, such as, for example, when an element X is reflected using a plane mirror **a** to make **a** X **a**⁻¹. As the parameter element changes (for instance because it is transformed, such as when the mirror **a** rotates), the parametrized element changes as well. Geometric algebra provides a calculus to compute with such changes.

This calculus consists of a scalar operator called the **directional derivative** to measure how the parametrized element reacts to a known change in the parameter (and the result is of the same type as the original), and of a **total geometric derivative** that specifies the change relative to any change in the parameter (and that returns an operator of a different type than its argument). The latter is more general (the directional derivative merely describes its components), and particularly useful in geometric integration theory (not treated in this book; see Section 8.8 for pointers).

In all of this, we have to be a bit careful about just copying the classical linear techniques, such as Taylor series definitions. Simply adding linear approximations of perturbations to a blade may not add up to a perturbed blade (but instead result in some nonfactorizable multivector), so we need to develop things in a structure-preserving manner. That is why we start with the calculus of versors, and develop the more classical derivatives in the remainder of the chapter.

---

## 8.2 Transformational Changes

First, let us consider an element X that has been changed by a rotor R. In the Euclidean and Minkowski spaces that interest us, the rotor can be written as the exponential of a bivector **R = exp(−B/2)**, and when we develop this in a power series in **B**, we get

> **e^(−B/2) X e^(B/2) = X + ½(XB − BX) + ···**  — (8.1)

The first-order term involves a combination that we will encounter a lot in our considerations, so it pays to define it as a new and useful product in geometric algebra. We briefly introduce it and its properties in Section 8.2.1. Then we play around with variations of changes to this basic transformation equation.

- We study what kind of changes small rotors can effect in an element X in Section 8.2.2. Once we have encoded motions as rotors (in Part II), those will be what we mean by "moving X slightly." Those motions together form a Lie algebra, which we connect to geometric algebra in Section 8.2.3.

- Those small changes in X can be propagated simply to other motions that X may undergo, as we show in Section 8.2.4.

- The most involved change is when the parameters of a motion themselves get moved—for instance, when a rotation plane translates or a mirror starts rotating. We study that in Section 8.2.5.

Each of these cases can be described by a well-chosen commutator product, some exactly, some to first order in the magnitude of the change.

### 8.2.1 The Commutator Product

The **commutator product** of two general elements of geometric algebra is defined as the product **×** : 𝒢ℝⁿ × 𝒢ℝⁿ → 𝒢ℝⁿ defined by

> **X × B ≡ ½(XB − BX)**

It is clearly bilinear and distributive, since it consists of a sum of geometric products, bilinear in the arguments. We have purposely not used the bold blade notation for its arguments, since its typical use involves more general multivectors.

This product is not associative. Instead of the identity **(A × B) × C = A × (B × C)**, so that **(A × B) × C − A × (B × C)** would be zero, we have

> **(A × B) × C − A × (B × C) = B × (C × A)**

which is more symmetrically expressed as the **Jacobi identity**:

> **(A × B) × C + (C × A) × B + (B × C) × A = 0**  — (8.2)

You can prove this easily yourself in structural exercise 1.

Even though the commutator product can be defined for general multivectors, we will not need it in completely general form: in our calculus of rotors, one of the two arguments (say the second argument B) is always a bivector. This has a property of grade-preservation (as we soon show):

> **grade(X × B) = grade(X)**  when **grade(B) = 2**

When used in this way, the commutator product is a grade-preserving product **× : ⋀ᵏℝⁿ × ⋀²ℝⁿ → ⋀ᵏℝⁿ**, extended to the whole space 𝒢ℝⁿ. This property of grade-preservation is important geometrically, for clearly we want all terms in a Taylor series like (8.1), showing the perturbation of X, to be of the same grade as X.

We prove this grade-preserving property in a slightly roundabout way. We first note that the terms **XB** and **BX** contain the grades **x − 2**, **x**, and **x + 2** (where **x = grade(X)**), since they are geometric products. The subtraction in the commutator product can kill some terms, so the whole range of grades may not be there. To investigate this, we take the reverse of the commutator to find

> **(X × B)̃ = ½(B̃X̃ − X̃B̃) = ½(X̃B̃ − B̃X̃) = X̃ × B̃**

We observe that the commutator product gets the same overall sign under reversion as X (namely **(−1)^(x(x−1)/2)**). Among the potential terms of grade **x − 2**, **x**, and **x + 2**, only the grade of **x** has precisely that same grade-dependent sign for all grades. (This is due to the sign pattern of the reversion over the grades, which is **+ + − − + + − − + + ···**, so that two grades up or two grades down may have opposite signs from grade x, for general x.) Therefore **X × B** must be of grade x, and the commutator product with a bivector is grade-preserving.

As an aside, having the commutator product permits listing a pleasing series of equations, expressing the geometric product in terms of other products when one of the arguments is a scalar α, a vector **a**, or a bivector A (not necessarily a 2-blade):

```
α X = α ∧ X
a X = a ∧ X + a⌋X
A X = A ∧ X + A⌋X + A × X
```

All equations hold for any multivector X.

You may have failed to notice the rather subtle difference between the commutator symbol **×** and the cross-product symbol **×**. Fortunately, there is little danger of confusing them in formulas, since we will use the commutator product only when one of the arguments is a bivector (which is an uppercase symbol, only bold if we know that it is a 2-blade), and the cross product only when both arguments are 3-D vectors (which are always lowercase bold).

### 8.2.2 Rotor-Induced Changes

After this introduction of the commutator product, we resume our treatment of the geometrical changes. Using the commutator notation, the transformation of X by the rotor **exp(−B/2)** can be developed in a Taylor series as

> **e^(−B/2) X e^(B/2) = X + X × B + ½(X × B) × B + (1/3!)((X × B) × B) × B + ···**  — (8.3)

You can prove this yourself, guided by structural exercise 2. The series continues the pattern as the generalization of the earlier (7.22) for vectors only. Since the commutator product with the bivector is grade-preserving, X remains of the same grade under this transformation (as it should, since the versor product is fully structure-preserving for all products).

Now suppose that the rotor is close to the identity. It is then the exponential of a small bivector **−δB/2**, with **δ ≈ 0**. We can write, in orders of δ:

> **e^(−δB/2) X e^(δB/2) = X + X × δB + O(δ²)**  — (8.4)

We read this as specifying the small change in an element X under a small orthogonal transformation. Such a small transformation must be represented by an even versor, which we can normalize to a rotor. The transformation caused by an odd versor cannot be continuously connected to the identity (i.e., done in small steps); you can perform a small amount of rotation, but not a small amount of reflection. We call small changes caused by small transformations **perturbations**.

To preserve the geometric meaning of X, we must demand that any small change δX to it must be writable as the application of a small rotor to it. These are the only kinds of small changes we should consider in our calculus. They are the proper generalization in geometric algebra of the additive change δX in a quantity X, beyond the scalars and vectors of the classical framework. Any small changes that cannot be written in this form may disrupt the algebraic structure of X, and with that its geometric interpretation.

> **Elements of geometric algebra should only be perturbed by rotors.**

We found in (8.4) that to first order, such a change can be written as **X × (δB)**, with **δB** a small bivector.

Remembering that rotors represent orthogonal transformations, you can see how even for a Euclidean vector **x** a general additive change **δx** is not permitted. Orthogonal transformations must preserve the norm, and this can only happen if the change **δx** is perpendicular to **x**. This must mean that **x · (δx) = 0**. The general element of grade 1 and linear in **x** with that property is **δx = x⌋δB**, with **δB** a small general bivector (for indeed **x · (x⌋δB) = x⌋(x⌋δB) = (x ∧ x)⌋δB = 0**). And for vectors,

> **δx = x⌋δB = ½(x δB − δB x) = x × δB**

so that it indeed has the desired form of a commutator product.

This limitation of the changes may appear unnecessarily restrictive, since it even forbids a simple translational change **δx** to a vector **x**. Indeed it does, for **x** denotes a 1-D direction, and that should only be turned by a rotor. But fortunately this limitation to rotors does not automatically mean that we cannot translate geometrical points in any direction. It merely necessitates us to find a way to represent that geometrical point in geometric algebra such that its translation is a rotor. In such a representation, any small translation would be permitted. We will present such a representation in Chapter 13. For now, please accept that the principle of allowing only rotor-type changes is not a geometrical limitation, but merely an algebraic structuring of the treatment of such changes.

### 8.2.3 Multiple Rotor-Induced Changes

When two small changes occur successively, by **exp(−δ₁A/2)** and **exp(−δ₂B/2)**, respectively, the resulting total change is

```
e^(−δ₂B/2) e^(−δ₁A/2) X e^(δ₁A/2) e^(δ₂B/2) =
= X + X × (δ₁A + δ₂B) +
  + ½((X × δ₁A) × δ₁A + 2(X × δ₁A) × δ₂B + (X × δ₂B) × δ₂B) + O(δ³)
```

To first order in the δs, the changes act independently and additively, but there is an interesting and asymmetrical structure in the second-order changes. This is most clearly seen when we attempt to undo the changes in opposite order. Many terms cancel (obviously those of first grade), and the Jacobi identity can be used to merge two terms, giving the result

```
e^(δ₂B/2) e^(δ₁A/2) e^(−δ₂B/2) e^(−δ₁A/2) X e^(δ₁A/2) e^(δ₂B/2) e^(−δ₁A/2) e^(−δ₂B/2) =
= X + X × (δ₁A × δ₂B) + O(δ³)
```

To the first relevant order, this changes X by an additive commutator with a bivector. Therefore, the commutator combination of two changes together acts like a new versor-type change, according to the bivector **(δ₁A × δ₂B)**:

```
e^(δ₂B/2) e^(δ₁A/2) e^(−δ₂B/2) e^(−δ₁A/2) X e^(δ₁A/2) e^(δ₂B/2) e^(−δ₁A/2) e^(−δ₂B/2)
≈ e^(−δ₁δ₂A×B/2) X e^(δ₁δ₂A×B/2)
```

The new versor is of a smaller order than the two original changes (**δ²** rather than **δ**).

Studying this combination of changes in transformations gets us into **Lie algebra**, classically used to analyze small continuous transformations. It can for instance be employed (in control theory) to prove that a few standard transformations suffice to achieve any transformation. In geometric algebra, the Lie algebra computations reduce to making a bivector basis for the space of transformations. That amounts to choosing a few bivectors as basic and trying to make the others by commutator products, commutators of commutators, and so on. This is possible because the algebra of bivectors is closed under the commutator product. If you can make a basis for the whole bivector space, this proves that any motion can be achieved by doing commutators of motions.

As an example, let us consider the combination of two rotations in Euclidean 3-space, in the **A=e₁ ∧ e₂** plane and the **B=e₂ ∧ e₃** plane, and investigate if we can make any rotation by a combination of these basic rotations. The commutator of the bivectors is **A × B = −e₃ ∧e₁**, so that performing a small rotation over angle φ in the A plane followed by a small rotation ψ in the B plane, and then reversing them, leads to a small rotation φψ in the **e₁ ∧ e₃** plane. That rotation was not among our basic transformations, but it clearly completes the set of bivectors for rotors. It shows that with the two rotations we can make the third independent rotation. Directions in 3-D space are controllable with only two basic rotations.

By contrast, translations in 3-D really need three independent components to reach an arbitrary position. The reason is that translations commute, so that any commutator is zero. Geometrically, this implies that no independent translation can be created from two translations in a plane. (We will meet the bivectors of translations only later, in Chapter 13, but the argument is simple enough not to require precise representation.)

As a third example, consider the maneuvering of a car. You can only steer and drive (forward or backward), yet you can reach any position in any orientation. The car is obviously controllable. The basic parallel parking maneuver that allows a car to move sideways is actually a (simplified) sequence of two commutators of the steer and drive actions. For more details, see [16].

### 8.2.4 Transformation of a Change

In Section 8.2.2, we showed the nature of small changes in elements like X caused by small rotors. Such changes can propagate through additional versors. For instance, if we have the transformation **X → V X/V**, and X is perturbed by a versor with characterizing bivector A, we can rewrite the result in terms of a perturbation of the original result:

> **V (e^(−δA/2) X e^(δA/2)) V⁻¹ = (V e^(−δA/2) V⁻¹) (VXV⁻¹) (V e^(δA/2) V⁻¹)**

Therefore, the result of the mapping gets perturbed by the mapped perturbation

> **V e^(−δA/2) V⁻¹ = e^(−VδAV⁻¹/2)**

by (7.21). You can simply substitute the error bivector **δA** by **V δA/V** to get the total error bivector of the perturbation on **V X/V**. No need for first-order approximations, the result is exact, and also holds for odd V.

### 8.2.5 Change of a Transformation

Things are somewhat more subtle when it is not X that is perturbed in the mapping **X → V X/V**, but the versor V (which may be odd or even, though we temporarily drop the sign to show the structure of the argument more clearly). This happens, for instance, when you reflect in a plane that has some uncertainty in its parameters. When the versor V becomes **e^(−δA/2) V e^(δA/2)**, the total perturbation is

> **(e^(−δA/2) V e^(δA/2)) X (e^(−δA/2) V⁻¹ e^(δA/2))**

We need to express this in terms of a versor operation on the transformation result **V X/V** to find out how that is perturbed. When we do so, the transformation versor on **V X/V** can be rewritten to first order as

> **e^(−δA/2) V e^(δA/2) V⁻¹ ≈ (V + V × δA) V⁻¹ = 1 + (V × δA)/V**  — (8.5)

These are the first few terms of the Taylor series of the exponential **exp((V × δA)/V)**, considered as a function of δA. So we find for the versor operator computing the perturbed result to first order:

> **e^(−δA/2) V e^(δA/2) V⁻¹ = e^((V×δA)/V)**

This should be written as the versor **e^(−δB/2)**, and that demand defines the bivector of the local perturbation **δB** as

> **δB = −2(V × δA)/V = δA − V δA/V**  — (8.6)

This method of computation of a versor using only a first-order Taylor series is fine, as long as you remember that this is only valid to first order. The resulting versor is not the exact result valid for a big change to V. We can imagine the local validity of this technique when we rotate a mirror around a general axis. To a good approximation, the reflection rotates around the projection of the rotation axis onto the mirror, and that is described by the first-order rotor so that the reflection describes a circular arc. However, as the mirror rotates more, this projected axis changes and higher-order effects kick in; the circular arc was just a local second-order approximation to what is actually a caustic. (We will treat this application in Section 8.5.2.)

---

## 8.3 Parametric Differentiation

After this treatment of the transformational changes of an element, we study the second type of change we mentioned in the introduction.

Parametric differentiation is concerned with changes in elements in their dependence on their defining constituents. As such, it generalizes both the usual scalar differentiation and the derivative from vector calculus. All differentiation is based on functional dependence of scalar functions. In the usual approach, when these scalar functions are coordinate functions of a parameterized spatial curve or a vector field, the derivatives themselves can be reassembled into a geometric quantity such as the tangent vector to the curve or the divergence of the vector field. Such elements are truly geometric in that they do not depend on the coordinate functions that were introduced, but this is not always clear from either their derivation, their form, or their use.

Geometric algebra offers a way of computing with derivatives without using coordinates in the first place, by developing a calculus to apply them to its elements constructed using its products. However, proper coordinate-free definitions of the geometrical derivatives along these lines would require us to view them as a ratio of integrals. This would lead us a bit too far astray—you are referred to [26] for such a treatment. Here we will follow a more direct coordinate-based route, starting from scalar differentiation, but we quickly rise above that to attain truly geometric differentiation, expressed in coordinate-free formulas and techniques.

We construct our differentiation operators from specific to general, in the order of scalar differentiation, directional vector differentiation, total vector differentiation, and multivector differentiation. The final concept is the most general and contains the others, but we prefer to build up to it gradually.

---

## 8.4 Scalar Differentiation

Scalar differentiation of a multivector-valued function F(τ) relative to its scalar parameter τ is defined in the usual manner:

> **d/dτ F(τ) ≡ lim(ε→0) [F(τ + ε) − F(τ)] / ε**

Geometric algebra has little to add to this form of differentiation, even though the function can now take values in the algebra. This type of differentiation is simply a scalar operator that commutes with all elements of the algebra. Therefore, it can be freely moved in a geometric product of multivector-valued functions, and obeys the product rule:

> **d/dτ [F(τ) G(τ)] = d/dτ [F(τ)] G(τ) + F(τ) d/dτ [G(τ)]**  — (8.7)

Yet we will see later that scalar differentiation is a particular instance of a more general multivector differentiation, and in preparation for that we denote it as **∂τ**.

Since the function F is typically defined using geometric algebra products, the differentiation result may also allow compact formulation using those products, so it is worth carrying out these differentiations symbolically. The following gives a simple example:

> Let a vector **x** follow a curve on an orbit parameterized as **x(τ)** by the time parameter τ. If we want to differentiate the scalar-valued vector function **x → x²** (involving the geometric product) along the curve, this is done in careful detail as follows:
>
> ```
> ∂τ x(τ)² = ∂τ[x(τ) x(τ)]
>          = ∂τ[x(τ)] x(τ) + x(τ) ∂τ[x(τ)]    (product rule)
>          = 2 ∂τ[x(τ)] · x(τ)                 (inner product definition)
>          = 2 ẋ(τ) · x(τ)                     (dot for time derivative)
> ```
>
> The result of the scalar operator ∂τ applied to the scalar-valued function **x(τ)²** is therefore a scalar, as you would expect. We will often leave the parameterization understood, and would then denote this in shorthand as **∂τx² = 2 ẋ · x**.

The scalar differentiation can easily be applied to the constructions of geometric algebra. As an example, we show the scalar differentiation of a time-dependent rotor equation. Let the rotor be **R = e^(−Iφ/2)**, where the bivector angle **Iφ** is a function of τ so that both rotation plane and rotation angle may vary. We use the rotor to produce a time-dependent, rotated version **X(τ) = R(τ) X₀ R(τ)⁻¹** of some constant blade **X₀**. For constant **I**, scalar differentiation with respect to time gives (using chain rule and commutation rules)

```
∂τ X(τ) = ∂τ[e^(−Iφ/2) X₀ e^(Iφ/2)]
        = −½ ∂τ[Iφ](e^(−Iφ/2) X₀ e^(Iφ/2)) + ½(e^(−Iφ/2) X₀ e^(Iφ/2)) ∂τ[Iφ]
        = ½(X ∂τ[Iφ] − ∂τ[Iφ] X)
        = X × ∂τ[Iφ]
```
— (8.8)

This retrieves the commutator form of the change in a rotor transformation: X changes in first order by its commutator with the derivative of the bivector of the change. This agrees with our analysis of changes in a rotor-based transformation as a commutator in (8.4). For the more general case of a variable **I**, see Structural Exercise 6.

The simple expression that results assumes a more familiar form when X is a vector **x** in 3-space, the attitude of the rotation plane is fixed so that **dI/dt = 0**, and we introduce a scalar angular velocity **ω ≡ dφ/dt**. It is then common practice to introduce the vector dual to the plane as the angular velocity vector **ω**, so **ω ≡ (ωI)* = ωI/I₃**. We obtain

> **dx/dt = x × d(Iφ)/dt = x × (ωI₃) = x⌋(ωI₃) = (x ∧ ω)⌋I₃ = ω × x**

where the final symbol **×** is the 3-D vector cross product. This shows the correspondence of our scalar differentiation with the classical way of expressing the change.

As before when we treated other operations, we find that an equally simple geometric algebra expression is much more general than the classical expression; here (8.8) describes the differential rotation of k-dimensional subspaces in n-dimensional space rather than merely of vectors in 3-D.

### 8.4.1 Application: Radius of Curvature of a Planar Curve

In the differential geometry of planar curves in the Euclidean plane ℝ²·⁰, you often want a local description of a parameterized curve **r(τ)** in terms of its local tangent circle. That characterizes the curve well to second order; the local curvature is the reciprocal of the radius of this tangent circle. The following derivation is a good example of a proper classical coordinate-free treatment, borrowed from [50], which we are then able to complete to a closed-form solution using geometric algebra.

Let the local tangent circle be characterized by its center **c** and its radius **ρ**. Then a point **r** lies on it if it satisfies **(c − r)² = ρ²**. Now we let **r** be the parameterized curve point **r(τ)**, which relative to its parameter τ has first derivative **ṙ(τ)** and second derivative **r̈(τ)**. (This handy overdot notation of these "fluxions" is common in physics texts.) Taking derivatives of the defining equation, we get the following list of requirements on **c** and **ρ**:

```
(c − r)² = ρ²
2(c − r) · ṙ = 0
−2 ṙ · ṙ + 2(c − r) · r̈ = 0
```

Our source [50] stops here, but we can continue because we have geometric algebra. The occurrence of **(c − r)** in an inner product with both **ṙ** and **r̈** makes us wonder what **(c−r)⌋(ṙ∧r̈)** might be, since that contains both terms by (3.17). Because of the equations above, it is fortunately independent of both **c** and **ρ**:

> **(c − r)⌋(ṙ ∧ r̈) = ((c − r) · ṙ)r̈ − ((c − r) · r̈)ṙ = −(ṙ · ṙ)ṙ = −‖ṙ‖³**  — (8.9)

Moreover, since in 2-D any trivector is zero, so is **(c−r)∧(ṙ∧r̈)**. Therefore, the contraction in (8.9) can be replaced by a geometric product. Since that is invertible, we can perform right division and obtain

> **c = r − ‖ṙ‖³ / (ṙ ∧ r̈)**

as the closed-form solution for **c**, and by substitution we obtain **ρ²**:

> **ρ² = (‖ṙ‖³ / (ṙ ∧ r̈))²**

In both expressions, we recognize the occurrence of the reciprocal of the rejection of **r̈** by **ṙ**—so only the component of **r̈** orthogonal to **ṙ** contributes to these geometric quantities (the other part is related to reparameterization, and is geometrically less interesting). The center of the tangent circle is clearly in the direction orthogonal to **ṙ**.

The ensuing expression for the curvature requires a square root of a square of a vector; its sign should be related to choosing a positive direction for vectors orthogonal to **ṙ**. Using the pseudoscalar **I₂** of the plane for dualization, we use **ṙ*** as the positive direction relative to **ṙ**. Then the curvature is

> **κ = 1/ρ = (ṙ ∧ r̈)* / ‖ṙ‖³**

This is easily converted to the familiar coordinate form by setting **r(τ) = x(τ) e₁ + y(τ) e₂**, with the parameter derivatives of the functions x and y denoted by overdots:

> **κ = (ẋ ÿ − ẏ ẍ) / (ẋ² + ẏ²)^(3/2)**

This expression takes considerably more work to derive when using coordinates from the start.

---

## 8.5 Directional Differentiation

Let F(**x**) be an element of geometric algebra dependent on a vector **x**. (If **x** is the position vector, this would be a position-dependent quantity, such as a vector field or a bivector field in the space ℝⁿ.) We may want to know how F(**x**) changes at a particular value of **x** if we would move in the direction **a**. It will clearly vary by an amount of the same grade type as F itself, so such a directional differentiation is a scalar operator on F(**x**). It is denoted by **(a ∗ ∂ₓ)**—we will explain why soon—and defined as

> **(a ∗ ∂ₓ) F(x) ≡ lim(ε→0) [F(x + εa) − F(x)] / ε**

Since it is a scalar operator, it commutes with all elements. You might expect that this implies that it acts very much like differentiation in real calculus, but that is incorrect: the geometric products in the functions it acts on make for rather different (but geometrically correct) results.

> **Example:** The function **x → x²** is defined everywhere, and gives a scalar field on the vector space ℝⁿ. Its directional derivative is
>
> ```
> (a ∗ ∂ₓ)[x²] = lim(ε→0) [(x + εa)² − x²] / ε     (definition)
>              = lim(ε→0) [ε x a + ε a x + ε²a²] / ε  (definition)
>              = x a + a x                            (limit process)
>              = 2 a · x                              (inner product definition)
> ```
>
> You see the familiar result: there is no variation when **a** is perpendicular to **x**, and maximum variation in the **x**-direction.

Since the differentiation is a scalar operator, it can be moved freely through expressions, and obeys a product rule like (8.7).

### 8.5.1 Table of Elementary Results

We do some basic derivations and collect them in Table 8.1, which contains other results that follow the same pattern. (In our derivations here, we assume that all vectors reside in the same space, but the table is slightly more general and requires projection of the parameter vectors to the space of **x**, hence the occurrence of **P[a]**. We explain this in Section 8.6.)

**The identity function F(x) = x** has the derivative you would expect:

> **(a ∗ ∂ₓ) x = lim(ε→0) [(x + εa) − x] / ε = a**

**Scalar differentiation of the inner product** leads to a substitution of **x** by its change **a**:

> **(a ∗ ∂ₓ) (x · b) = a · b**

**The inner product with a vector-valued linear function f** unexpectedly pulls in the adjoint function **f̄** of Section 4.3.2:

> **(a ∗ ∂ₓ) (f[x] · b) = (a ∗ ∂ₓ) (x · f̄[b]) = a · f̄[b]**

**The scalar derivative of the inverse 1/x = x⁻¹** gives a surprising result:

```
(a ∗ ∂ₓ) x⁻¹ = lim(ε→0) (1/ε)[1/(x + εa) − 1/x]
             = lim(ε→0) (1/ε)[(x + εa)/(x² + 2ε a·x) − 1/x]
             = lim(ε→0) (1/ε)[x(1 + ε x⁻¹a) / (x²(1 + 2ε a·x⁻¹)) − 1/x]
             = lim(ε→0) (1/ε)[x/(x²)(1 + ε x⁻¹a)(1 − 2ε a·x⁻¹) − 1/x]
             = x⁻¹(x⁻¹a − 2a·x⁻¹)
             = −x⁻¹ a x⁻¹
```

This clearly differs from the classical result in real analysis (ignoring all commutation restrictions, we would get the familiar **−a/x²**). The construction can be immediately interpreted geometrically, as in Figure 8.1. When you realize that **x⁻¹** is the inversion of **x** in the unit sphere, you see that a change **a** in **x** is a **1/x²**-scaled version of the reflection of **a** relative to the plane perpendicular to **x**, which is exactly what the differentiation result signifies.

*[Figure 8.1: Directional differentiation of a vector inversion. The small additive perturbation vector a is reflected in the plane with normal x to make −xax⁻¹, and the result scaled by 1/x² to produce −x⁻¹ax⁻¹ as the correct difference (to first order) between (x + a)⁻¹ and x⁻¹.]*

**For powers of the norm**, which are scalar functions, we retrieve a semblance of the usual calculus result:

```
(a ∗ ∂ₓ) ‖x‖ᵏ = lim(ε→0) (1/ε)(‖x + εa‖ᵏ − ‖x‖ᵏ)
              = lim(ε→0) (1/ε)(‖x‖ᵏ(√(1 + 2εx⁻¹·a))ᵏ − ‖x‖ᵏ)
              = lim(ε→0) (1/ε)(‖x‖ᵏ(1 + kεx⁻¹·a) − ‖x‖ᵏ)
              = k x·a ‖x‖ᵏ⁻²
```

The other entries of Table 8.1 can be demonstrated using similar techniques.

---

### Table 8.1: Directional derivatives and vector derivatives

Directional derivatives and vector derivatives of common functions in an m-dimensional vector manifold ℝᵐ within a larger vector manifold ℝⁿ. Here **x**, **a** are vectors, **A** is a blade, **P[ ]** is shorthand for the projection **P_Iₘ[ ] : ℝⁿ → ℝᵐ** locally mapping vectors onto the lower-dimensional manifold.

| Directional Derivatives | |
|---|---|
| **(a ∗ ∂ₓ) x** | **= P[a]** |
| **(a ∗ ∂ₓ) (x · b)** | **= P[a] · b** |
| **(a ∗ ∂ₓ) x⁻¹** | **= −x⁻¹ P[a] x⁻¹** |
| **(a ∗ ∂ₓ) ‖x‖ᵏ** | **= k (P[a] · x) ‖x‖ᵏ⁻²** |
| **(a ∗ ∂ₓ) x/‖x‖ᵏ** | **= [P[a] − k (P[a] · x)/x] / ‖x‖ᵏ** |

| Vector Derivatives | |
|---|---|
| **∂ₓ x** | **= m** |
| **∂ₓ · x** | **= m** |
| **∂ₓ ∧ x** | **= 0** |
| **∂ₓ(x · a)** | **= P[a]** |
| **∂ₓ(x ∧ a)** | **= (m − 1) P[a]** |
| **∂ₓ(x A)** | **= m P[A]** |
| **∂ₓ(x⌋A)** | **= grade(A) P[A]** |
| **∂ₓ(x ∧ A)** | **= (m − grade(A)) P[A]** |
| **∂ₓ(A⌋x)** | **= (m − 2 grade(A)) P[A]** |
| **∂ₓ ‖x‖** | **= x/‖x‖** |
| **∂ₓ ‖x‖ᵏ** | **= k ‖x‖ᵏ⁻² x** |
| **∂ₓ x/‖x‖ᵏ** | **= (m−k)/‖x‖ᵏ** |
| **∂ₓ (f[x] · y)** | **= P[f̄[y]]** |

---

### 8.5.2 Application: Tilting a Mirror

Consider the situation where we have a planar mirror in the origin with normal vector **n** (not necessarily a unit normal). The reflection of an element X in this mirror is given by (see Section 7.1):

> **X → n[X] ≡ n X n⁻¹**

We now perturb the mirror, for instance by a small rotation, and want to know what happens to the reflection result. Let us do this in two steps: first we see how any change in **n** affects the reflection result; then we relate the change in **n** to the parameters of the perturbing rotational action on the mirror.

**Step 1:** We apply the directional derivative for an **a**-change in **n**:

```
(a ∗ ∂ₙ)[n X n⁻¹] = a X n⁻¹ + n X (−n⁻¹ a n⁻¹)
                  = (a n⁻¹)(n X n⁻¹) − (n X n⁻¹)(a n⁻¹)
                  = 2(a n⁻¹) × (n X n⁻¹)
                  = (n X n⁻¹) × (2 n⁻¹ ∧ a)
```

The final simplification holds because the scalar part **n⁻¹ · a** of **n⁻¹ a** does not contribute to the commutator product result.

The result shows that it is the part of **a** perpendicular to **n** that causes changes to the reflection. This is, of course, just what we would have expected, since the magnitude of **n** does not affect the reflection **n[X]** at all. A small orthogonal change to a vector is effectively a rotation, so the directional derivative is eminently suited to process the rotational change. But there is more: to first order, the change in the reflection **n[X]** can be written as a commutator. Therefore, it can be represented (at least locally) as a rotor transformation. Comparing with (8.4), we see that the bivector **B** of the transforming rotor equals **B = 2n⁻¹ ∧ a**. So the reflected element **n[X]** describes a rotation as the mirror normal changes by **a**, in the plane **n⁻¹ ∧ a**, by a rotation angle **‖n⁻¹ ∧ a‖**. Recognizing this is in fact a local integration, since it reverses the differentiation process.

**Step 2:** We need to relate the change **a** in the mirror normal **n** to an actual transformation. Let us rotate the mirror using a rotor **exp(−Iφ/2)**, with **I** the unit 2-blade of the rotation plane and φ a small angle. Then, according to (8.3), the normal vector **n** changes to first order by the vector **n × Iφ**. This is therefore what we should use as our **a**.

**Combining the results:** The bivector of the total transformation in the reflected X is

> **B = 2 n⁻¹ ∧ a = 2φ n⁻¹ ∧ (n × I) = 2φ n⁻¹ ∧ (n⌋I)**  — (8.10)

That result is valid in any number of dimensions. It gives the bivector of the resulting rotation of **n[X]**, which specifies both the rotation plane and its angle.

To get a better feeling for the geometry of (8.10) in 3-D, introduce the unit rotational axis of the mirror motion **m = I***, normalize **n** to unity, and express the result as a rotational axis **b = B***. Some manipulation gives

> **b = 2φ n⌋(n ∧ m) = 2φ(m ∧ n)/n**

This axis is the rejection of **m** by **n**, or (if you prefer) the projection of the axis **m** onto the plane with normal vector **n**. That projection obtains a factor **sin ψ** of the angle ψ between **n** and **m**. The rotation angle β for the reflection **n[X]** of X under the rotation of φ around the **m** axis is the norm of **b**, which evaluates as

> **β = 2φ sin(ψ)**  — (8.11)

This is a rather powerful result acquired with fairly little effort, only at the very last moment requiring some trivial trigonometry. Figure 8.2 sketches the situation.

*[Figure 8.2: Changes in reflection of a rotating mirror. The yellow mirror with normal n rotates around the m axis over an angle φ, producing the green mirror plane. This changes the reflection −nxn⁻¹ of a vector x to the gray vector. That change is to first order described as the rotation of −nxn⁻¹ around an axis that is the projection of m on the n plane, over an angle 2φ sin ψ, where ψ is the angle between n and m.]*

Two special cases make perfect sense: if **ψ = 0**, then **n** and **m** are aligned, and indeed no rotation over **m** changes the reflection of X; and if **ψ = π/2**, then **n** and **m** are perpendicular, and any rotation φ of the rotation plane becomes a **2φ** rotation of the reflection **n[X]**.

We will get back to this rotated reflection in its full generality in Section 13.7.

---

## 8.6 Vector Differentiation

In scalar differentiation, we consider a vector function as a changing in time (or some such scalar parameter). We may also want to consider F(**x**) as a function of position as encoded by the vector variable **x**, and differentiate directly relative to that variable. This is most easily defined by developing it on a basis, doing a directional differentiation with respect to each of the components, and reassembling the result in one quantity. It is the **∇-operator** of vector analysis, but we will denote it as **∂ₓ**. This explicitly specifies the variable relative to which we differentiate and prepares for a generalization beyond vectors and toward differential geometry. On a basis **{eᵢ}ᵐᵢ₌₁** for the space ℝᵐ in which **x** resides, let **xⁱ** denote the coordinate functions of the vector **x** so that it can be written as

> **x = Σᵢ₌₁ᵐ xⁱ eᵢ**

We will be setting up this vector differentiation in a very general framework, in which the space ℝᵐ of **x** may reside on a manifold (curved subspace) within a larger space ℝⁿ (for instance, **x** may lie on a 2-D surface in 3-D space). The basis for ℝᵐ may then not be orthonormal, so we use the reciprocal basis of Section 3.8, and compute **xⁱ** as **xⁱ = eⁱ · x**. The directional derivative in the coordinate direction of **eᵢ** is simply the scalar derivative of the coordinate function:

> **(eᵢ ∗ ∂ₓ) = ∂/∂xⁱ = ∂ₓᵢ**

As their notation suggests, we can assemble the results of each of these directional operators and consider them as the components of a more general **vector derivative** operation defined on this basis as

> **∂ₓ ≡ Σᵢ₌₁ᵐ eⁱ (eᵢ ∗ ∂ₓ) = Σᵢ eⁱ ∂/∂xⁱ**  — (8.12)

(When you study reciprocal frames, expressions like these are actually coordinate-free when they contain the upper and lower indices that cancel; in physics, lower-index vectors are called *covariant* and upper-index vectors *contravariant*, but we will not follow that terminology here.)

The operator **∂ₓ** computes the total change in its argument when **x** changes in all possible ways, but it keeps track of those changes in a geometrical manner, registering the **eᵢ**-related scalar change in the magnitude of the **eⁱ** component of the total change. Preserving this geometrical information is surprisingly powerful, and in advanced geometric calculus it is shown that this operator can be inverted by integration (see [26]).

You should interpret the grade of the operator **∂ₓ** as a vector (i.e., as the grade of its subscript). As a geometrical vector operator, it should conform to the commutation rules for geometric products. We will not use the square application brackets here, for it is more productive to see this as a geometric element rather than as a linear operator, and to move it to other places in the sequence of symbols for computational purposes. The subscript **x** in **∂ₓ** denotes which vector variable is being differentiated (and this is necessary when there is more than one).

> **Example:** We apply the vector differentiation to the function **F(x) = x²**, relative to its vector parameter **x**:
>
> ```
> ∂ₓ x² = Σᵢ eⁱ ∂ₓᵢ [Σⱼ,ₖ xʲxᵏ eⱼ·eₖ]     (coordinate definition)
>       = Σᵢ eⁱ [Σₖ xᵏ eᵢ·eₖ + Σⱼ xʲ eⱼ·eᵢ]  (coordinate independence)
>       = 2 Σᵢ eⁱ (eᵢ·x)                      (linearity)
>       = 2x
> ```
> — (8.13)
>
> We obtain the result **2x**, which you might have expected from pattern matching with scalar differentiation (though that is a dangerous principle to apply). The result is not a vector, but a vector field that has the value **2x** at a location **x**. This vector field is in fact the **gradient** of the scalar function **x²** (i.e., the direction in which it varies most, with a magnitude that indicates the amount of variation).

The recognition of the multiplication in **∂ₓ F(x)** as the geometric product makes it quite natural to expand this in terms of the inner and outer product, simply applying (6.14):

> **∂ₓ F(x) = ∂ₓ⌋F(x) + ∂ₓ ∧ F(x)**

For a vector-valued function F, the first term corresponds to the usual **divergence** operator **div[F(x)] ≡ ∇·F(x)**, and the second term is related to the **curl** operator **rot[F(x)] ≡ ∇×F(x)**, written in terms of the 3-D cross product; it is actually its dual. As with the other uses of the cross product, replacing the curl by an outer-product-based construction ensures validity in arbitrary dimensionality. If F is scalar-valued, then only the **∂ₓ ∧ F(x)** term remains, and is identical to the **gradient** operator **grad[F(x)] = ∇F(x)**. For a symmetric vector function **F₊** (equal to its adjoint), the part **∂ₓ ∧ F₊[x]** equals zero, for a skew-symmetric vector function **F₋** (opposite to its adjoint), the part **∂ₓ · F₋[x]** equals zero.

### 8.6.1 Elementary Results of Vector Differentiation

We have introduced the vector differentiation as the geometric algebra equivalent of the ∇-operator from vector analysis. Although the definition as we have given it uses coordinates, the vector differentiation is a proper geometrical operation that is not dependent on any chosen coordinate system. When you apply it, you should avoid coordinates, and instead use results from a table of standard functions (combined with product rule and chain rule of differentiation). We give such a collection of useful elementary results in Table 8.1, and derive some of its more educational entries below.

**Identity Function x.** The identity function **F(x) = x** has a derivative that depends on the dimensionality of the space ℝᵐ in which **x** resides.

```
∂ₓ x = Σᵢ eⁱ ∂/∂xⁱ [Σⱼ xʲeⱼ]
     = Σᵢ,ⱼ δⁱⱼ eⁱ eⱼ = Σᵢ eⁱ eᵢ
     = Σᵢ eⁱ·eᵢ + Σᵢ eⁱ∧eᵢ = Σᵢ 1 + 0 = m
```

(Here we used **Σᵢ eⁱ ∧ eᵢ = 0**, given as (3.35).) This algebraic derivation gives a clue for the correct geometrical way to look at this: all changes in all directions are to be taken into account. In m-dimensional space, there are m directions, and each of these provide a unit change in coordinates with each unit step, for a total of m.

Since the vector differentiation applies as a geometric product, you can split the result in an inner and outer product part that the computation above has shown to obey **∂ₓ · x = m** and **∂ₓ ∧ x = 0**. The outer product result **∂ₓ ∧ x = 0** shows that you can think of **∂ₓ** as being like a vector in the **x** direction, and the inner product result then shows that it is like **m/x** (but view these as no more than mnemonics; **∂ₓ** is of course not a vector but an operator).

**Inner Product x · a.** When we study the change in the scalar quantity **F(x) = x · a** (geometrically the projected component of **x** onto a vector **a⁻¹**), we should in general allow for the variations of **x** to be in its m-dimensional manifold (curved subspace), whereas **a** may be a vector of the encompassing space ℝⁿ (for instance, **x** on a sphere, **a** a general vector in 3-D space; **x · a** is well defined everywhere on the sphere, so it has a derivative).

Two things happen to the measured changes caused by variations in **x**. First, even when **x** and **a** are in the same m-dimensional space, the quantity **x·a** can only pick up the changes in the direction **a**, so summing over all directions only this 1-D variation remains. Second, **x** cannot really vary in the **a**-direction, since it has to remain in its m-dimensional manifold, or more accurately, in the tangent space at **x** isomorphic to ℝᵐ, for which **{eᵢ}ᵐᵢ₌₁** is the basis. It is the projection of the **a**-direction onto this tangent space that must be the actual gradient.

The algebraic computation confirms this, with indices i and j ranging over coordinates for the space in which **x** resides, and k over the space of **a**, using a local coordinate basis for the total n-dimensional space in which the problem is defined:

```
∂ₓ (x · a) = Σᵢ eⁱ ∂/∂xⁱ [Σⱼ Σₖ xʲ aᵏ eⱼ·eₖ]
           = Σᵢ Σₖ aᵏ eⁱ (eᵢ·eₖ)
           = Σᵢ aⁱ eⁱ = P_Iₘ[a]
```

since the summation of the **a** components is only done for the elements in the basis of the tangent space at **x** with pseudoscalar **Iₘ**. In tables, we will use **P[a]** as shorthand.

**Outer Product x ∧ a.** When we compute the variation of the bivector **x ∧ a**, this can be rewritten as the variation of **x a − x · a**. The variation over **x** in the first term causes a factor m (the dimensionality of the space that **x** resides in), but of course it picks up only the part **P[a]** of **a**. The second term we have seen above, and the total variation is now **∂ₓ (x ∧ a) = (m − 1) P[a]**.

**Norm ‖x‖.** Geometrically, what would you expect the derivative of the norm to be? Since it is a scalar function, the vector derivative will be the gradient of the norm, i.e., the direction in which it increases most steeply weighted by the weight of increase. So the answer should be **x/‖x‖**, the unit vector in the **x** direction. The algebraic computation confirms that it is:

```
∂ₓ ‖x‖ = Σᵢ eⁱ ∂ₓᵢ [Σⱼ,ₖ xʲxᵏ eⱼ·eₖ]^(1/2)
       = Σᵢ eⁱ (Σₖ xᵏ eᵢ·eₖ + Σⱼ xʲ eⱼ·eᵢ)/(2‖x‖)
       = Σᵢ eⁱ (eᵢ·x)/‖x‖
       = x/‖x‖
```

This result depends on the metric through the norm **‖x‖**.

**Adjoint as Derivative.** When we introduced the adjoint **f̄** of a function f in Section 4.3.2, we only had an implicit definition through **x ∗ f[y] = f̄[x] ∗ y**. Using the vector derivative, we can define the adjoint explicitly as

> **f̄[x] ≡ ∂ᵧ (f[y] ∗ x)**  — (8.14)

where both **x** and **y** are in the same space ℝᵐ (to avoid the need for a projection). You can prove it immediately by rewriting the argument of the differentiation using the earlier definition. This definition can also be applied to nonlinear functions, and it then computes a local adjoint, which may be different at every location **x**.

### 8.6.2 Properties of Vector Differentiation

The vector differentiation operator is clearly linear. It also obeys a product rule, though we need to take care of its noncommutativity. Therefore, it becomes inconvenient to denote its application by square brackets; we need a more specific notation. Dropping the reference to **x** for readability, we express the product rule as

> **∂(FG) = ∂̇ F Ġ + ∂̇ FĠ**

where in each term the accent denotes on what factor the scalar differentiation part of the ∂ should act—the geometric vector part is not allowed to roam, so we cannot simply say that the operator acts on the element just to the right of it. To give an example:

```
∂ₓ(x x) = ∂̇ₓ x ẋ + ∂̇ₓ x ẋ = ∂̇ₓ x ẋ + ∂̇ₓ(2(ẋ·x) − x ẋ) = 2∂̇ₓ(ẋ·x) = 2x
```

Note that the subtle swap to get the elements into standard order precisely kills the term **∂̇ₓ x ẋ = m x**.

Because of the noncommutativity, there are other product rules, such as

> **F ∂G = Ḟ ∂̇ G + F ∂̇ Ġ**

with the accents again denoting how to match each differentiation with its argument.

There is also a **chain rule**, which looks a bit complicated. Let the coordinate **x** be hidden by a vector-valued function **y**, so that the dependence of F on **x** is **F(y(x))**. Then the chain rule of vector differentiation is

> **∂ₓ F(y(x)) = ∂̇ₓ(y(ẋ) ∗ ∂ᵧ) F(y)**

The two geometric products in this equation can be executed in either order due to associativity. If we start from the right, this states that we should first consider F as a function of **y** and do a directional differentiation in the **y(x)**-direction; that typically gives something involving both **y(x)** and **y**. We should not substitute **x** in the latter, but differentiate the **x**-dependence in the former. This can be confusing, so let us do an example.

> Let **G(y) = y²**, and **y(x) = (x · a)b**. If we would just evaluate G as a function of **x** by substitution, we would get **G(x) = (x · a)² b²**, so that **∂ₓ G(x) = 2(x · a) a b²**. The chain rule application should produce the same answer.
>
> We first evaluate from the right, so we start with the directional differentiation of **G(y) = y²**. For a general vector **z**, the directional derivative **(z ∗ ∂ᵧ) y² = 2 z · y**, so with **z = y(x)** the result is **2 y(x) · y = 2 (x · a) (b · y)**. Note that we kept **y**. In the second step, this expression needs to be differentiated to **x**, giving **∂ₓ[2(x · a) (b · y)] = 2 a (b · y)**. That is the answer, but we prefer it in terms of **x**, so we should substitute the expression for **y** in terms of **x**, giving the same result as before.
>
> If instead we had evaluated from the left, we would first need to evaluate **∂̇ₓ(y(ẋ) ∗ ∂ᵧ) = ∂ₓ[(x · a) b] ∗ ∂ᵧ = a (b ∗ ∂ᵧ)**. Do not be bothered by the presence of **∂ᵧ** in this derivation; since it is not differentiating anything, it behaves just like a vector. Now we apply the resulting operator to **G(y) = y²**, giving **2 a (b · y)** as in the other evaluation order. Here, too, you would need to substitute the expression **y(x)** to get the result in terms of **x**.
>
> The operator we just evaluated can be rewritten using the definition of the adjoint of the function **y(x) = (x · a) b**, which is **ȳ(x) = (x · b) a**. We then recognize **a (b ∗ ∂ᵧ)** as the adjoint of the y-function applied on **∂ᵧ**, i.e., **ȳ[∂ᵧ]**. We can also use the adjoint to write the actual answer for our differentiation of the squaring function G as **2 ȳ(y(x))**, which actually holds for any function **y** used to wrap the argument **x**.

The implicit understanding of how to deal with the substitutions in the equation is a bit cumbersome. A more proper notation for the process may be to keep the **x** in there at all steps:

> **∂ₓ G(y(x)) = ∂̇ₓ(y(ẋ) ∗ ∂ᵧ₍ₓ₎) G(y(x)) = ȳ[∂ᵧ₍ₓ₎]G(y(x))**  — (8.15)

The final rewriting uses the differential definition of the adjoint of (8.14) (which also holds for nonlinear vector functions **y**). This usage was motivated in the example. It means that we treat the differentiation operator **∂ᵧ₍ₓ₎** just as the vector it essentially is. Then the differentiation with respect to **y(x)** should be understood as above, but the lack of an accent denotes that that particular **x**-dependence should not be differentiated by **∂̇ₓ**.

So in the end, the chain rule is essentially a transformation of the differentiation operator: **when an argument gets wrapped into a function, the differentiation with respect to that argument gets wrapped into the adjoint of that function**.

---

## 8.7 Multivector Differentiation

We can extend these forms of differentiation beyond vectors to general multivectors, though for geometric algebra, the extension to differentiation with respect to blades and versors is most useful. Another extension is the differentiation with respect to a linear function of multivectors, which finds uses in optimization. We will not treat that here, but refer to Chapter 11 in [15].

### 8.7.1 Definition

The definition of **directional multivector differentiation** is a straightforward extension of the idea behind the directional vector differentiation. You simply vary the argument X of a function additively in its A-component, so that A should at least be of the same grade as X (as for instance when X is perturbed by a transformation, to first order). The definition reflects this grade-matching in its use of the scalar product:

> **(A ∗ ∂ₓ) F(X) ≡ lim(ε→0) [F(X + εA) − F(X)] / ε**

We emphasize that this is a scalar operator, since the grade of the result is the same as that of the original function.

As in the case of the vector derivative, we can see the directional multivector derivative as merely one component of a more general multivector derivative. We introduce coordinates now for the total **2ᵐ**-dimensional space of multivectors in the tangent space ℝᵐ at X. To distinguish it clearly from the m-dimensional vector basis, let us denote this multivector basis by a running capital index: **{eᵢ}²ᵐᵢ₌₁**. As with the vector basis in the vector derivative, this may not be orthonormal, so we also employ a reciprocal basis **{eᴵ}²ᵐᵢ₌₁**; see also Section 3.8. Then the multivector derivative is defined as

> **∂ₓ = Σᵢ eᴵ (eᵢ ∗ ∂ₓ)**

where **eᵢ** in principle runs over all **2ᵐ** elements **1, eᵢ, eᵢ ∧ eⱼ**, and so on, and the scalar product selects only the basis elements that are components of X.

This clearly contains vector differentiation as a special case. But also scalar differentiation is included: if we let X be a scalar **X = τ**, only the basis element **e = 1** is selected, so **∂τ = 1 (1 ∗ ∂τ) = (1 ∗ ∂τ) = d/dτ**, conforming to our earlier definition of this symbol. For scalars, directional differentiation and multivector differentiation coincide.

As with the vector derivative, the coordinate-based definition should be used to derive elementary coordinate-free results, which should then be the basis of all actual computations. We have collected some in Table 8.2, including results on scalar functions that often occur in optimization problems. The pattern of derivation of these equations is completely analogous to that for vector differentiation.

---

### Table 8.2: Elementary results of multivector differentiation

The multivector varies in the space ℝᵐ, contained in the larger space ℝⁿ. The map **P[]** projects from the latter to the former.

| Expression | Result |
|---|---|
| **(A ∗ ∂ₓ) X** | **= P[A]** |
| **(A ∗ ∂ₓ) X̃** | **= P[Ã]** |
| **(A ∗ ∂ₓ) Xᵏ** | **= P[A] Xᵏ⁻¹ + X P[A] Xᵏ⁻² + ··· + Xᵏ⁻¹ P[A]** |
| **∂ₓ X** | **= m** |
| **∂ₓ ‖X‖²** | **= 2X̃** |
| **∂ₓ (X ∗ A)** | **= P[Ã]** |
| **∂ₓ (X̃ ∗ A)** | **= P[A]** |
| **∂ₓ (X⁻¹ ∗ A)** | **= P[−X⁻¹ Ã X⁻¹]** |
| **∂ₓ ‖X‖ᵏ** | **= k ‖X‖ᵏ⁻² X̃** |

---

### 8.7.2 Application: Estimating Rotors Optimally

This example is taken from [36]. We are given k labeled vectors **uᵢ**, which have been rotated to become k correspondingly labeled vectors **vᵢ**. We want to try and retrieve that rotor from this data. If both sets of vectors are measured with some noise (as they usually are), we cannot exactly reconstruct the rotor R, but we have to estimate it. Let us use as our criterion for fit the minimization of the total squared distance between our estimated rotation vectors compared to where we measured them. This is an old problem, known in biometrics literature as the **Procrustes problem** and in astronautics as **Wahba's problem**.

So we need to find the rotor R that minimizes

> **Γ(R) = Σᵢ₌₁ᵏ (vᵢ − R uᵢ R̃)² = Σᵢ₌₁ᵏ (vᵢ² + uᵢ² − 2⟨vᵢ R uᵢ R̃⟩₀)**  — (8.16)

Preferably, we would like to differentiate this with respect to R and set the resulting derivative to zero to find the optimal solution. However, the rotor normalization condition **R R̃ = 1** makes this mathematically somewhat involved. It is easier to temporarily replace the rotor R by a versor V and consequently to replace R̃ by V⁻¹, and then to differentiate relative to the unconstrained V to compute the optimum V*. Clearly the terms without R (or V) do not affect the optimum, so

> **V* = argmax_V Σᵢ₌₁ᵏ ⟨vᵢ V uᵢ V⁻¹⟩₀**

Now we differentiate by **∂_V** and use the product rule. We can use some of the results from Table 8.2 once we realize that this is differentiation of a scalar product and use its symmetry and reordering properties (as (6.23)):

```
∂_V Γ(V) = Σᵢ₌₁ᵏ ∂_V ⟨vᵢ V uᵢ V⁻¹⟩₀
         = Σᵢ₌₁ᵏ [∂̇_V[V̇ ∗ (uᵢV⁻¹vᵢ)] + ∂̇_V[(V̇⁻¹) ∗ (vᵢVuᵢ)]]
         = Σᵢ₌₁ᵏ [uᵢV⁻¹vᵢ − V⁻¹(vᵢVuᵢ)V⁻¹]
         = 2V⁻¹ Σᵢ₌₁ᵏ (VuᵢV⁻¹) ∧ vᵢ
```

Therefore the rotor **R*** that minimizes **Γ(R)** must be the one that satisfies

> **Σᵢ₌₁ᵏ (R*uᵢR̃*) ∧ vᵢ = 0**  — (8.17)

This algebraic result makes geometric sense. For each **vᵢ**, it ignores the components that are just scalings of the corresponding rotated **uᵢ**; the rotation cannot affect those parts anyway. Only the perpendicular components matter, and those should cancel overall if the rotation is to be optimal—if not, a small extra twist could align the vectors better.

The result so far does not give us the optimal rotor **R*** explicitly; it has merely restated the optimization condition in a manner that shows what the essential components of the data are that determine the solution. Our reference [36] now cleverly uses vector differentiation to manipulate the equation to a form that can be solved by standard linear algebra. First, they observe that if we introduce the linear function

> **f[x] = Σᵢ₌₁ᵏ uᵢ (vᵢ · x)**

the condition (8.17) can be written as

```
∂ₓ ∧ (R* f[x] R̃*) = ½ Σᵢ₌₁ᵏ [∂ₓ(vᵢ·x)(R* uᵢ R̃*) − (R* uᵢ R̃*)(vᵢ·x)∂ₓ]
                   = −Σᵢ₌₁ᵏ (R*uᵢR̃*) ∧ vᵢ = 0
```

This kind of pulling out a differentiation operator is a good trick to remember. The resulting equation expresses the fact that **R* f[x] R̃*** is a symmetric function of **x**. The function **f** itself is therefore the **R***-rotated version of a symmetrical function.

We could proceed symbolically with geometric algebra to find the symmetric part of **R*[f]** (by adding the adjoint **f̄[R*]** and dividing by two), and its inverse (using (4.16)), and taking that out of the function; what remains is then the rotation by the desired rotor. However, [36] at this point switches over to using numerical linear algebra. In linear algebra, any linear function **f** has a **polar decomposition** in a symmetric function followed by an orthogonal transformation, and this can be computed using the **singular value decomposition (SVD)** of its matrix **[[f]]** as **f ≡ [[U]][[S]][[V]]ᵀ = ([[U]][[V]]ᵀ)([[V]][[S]][[V]]ᵀ)**. Using this result, the matrix of the optimal rotation **R*** is **[[V]][[U]]ᵀ**, where **[[U]]** and **[[V]]** are derived from the SVD of **[[f]] ≡ Σᵢ₌₁ᵏ [[uᵢ]][[vᵢ]]ᵀ**. This rotation matrix is easily converted back into the optimal rotor **R***, see Section 7.10.4.

This simple matrix computation algorithm is indeed the standard solution to the Procrustes problem. In the usual manner of its derivation, formulated in terms of involved matrix manipulations, one may have some doubts as to whether the SVD (with its inherent use of the Frobenius metric on matrices) is indeed the optimal solution to original optimization problem (which involved the Euclidean distance). In the formulation above, the intermediate result (8.17) shows that this is indeed correct, and that the SVD is merely used to compute the decomposition rather than to perform the actual optimization.

From a purist point of view, it is of course a pity that the last part of the solution had to revert temporarily to a matrix formulation to compute a rotor. We expect that appropriate numerical techniques will be developed soon completely within the framework of geometric algebra.

---

## 8.8 Further Reading

The main reference for further reading on geometric calculus is the classic book by Hestenes [33], which introduced much of it. It contains a wealth of material, including an indication of how geometric calculus could be used to rephrase differential geometry. His web site contains more material, including some new introductions such as [26].

The approach in Doran and Lasenby's book [15] is tailored towards physicists, and it has good and practical introductions to the techniques of geometric calculus. Read them for directed integration theory. They are practitioners who use it daily, and they give just the right amount of math to get applicable results.

---

## 8.9 Exercises

### 8.9.1 Drills

1. Compute the radius of the tangent circle for the circular motion **r(τ) = exp(−Iτ) e₁** in the plane **I = e₁ ∧ e₂**, at the general location **r(τ)**.

2. Compute the following derivatives:
   1. **(a ∗ ∂ₓ) x³**
   2. **∂ₓ x³**
   3. **(a ∗ ∂ₓ) (x b/x)**
   4. **∂ₓ (x b/x)**
   5. **ẋ ∂̇ₓ**
   6. **ẋ ∧ ∂̇ₓ**
   7. **ẋ · ∂̇ₓ**

3. Show that the coordinate vectors are related to differentiation through **eₖ = ∂/∂xᵏ x**.

4. Show that the reciprocal frame vectors are the gradients of coordinate functions: **eᵏ = ∂ₓ xᵏ**.

### 8.9.2 Structural Exercises

1. Prove the Jacobi identity (8.2) and relate it to nonassociativity of the bivector algebra.

2. Derive the Taylor expansion of a rotor transformation:
   > **e^(−B/2) X e^(B/2) = X + X × B + ½((X × B) × B) + ···**
   
   Do this by assuming that the first-order term is correct for small bivectors, it is easily derived by setting **exp(−B/2) ≈ 1 − B/2**. Now write a versor involving a finite B as versors involving **B/2**, **B/4**, **B/8**, and so on and build up the total form through repeated application of the smallest bivector forms. That should give the full expansion.

3. The **Baker-Campbell-Hausdorff formula** writes the product of two exponentials as a third, and gives a series expansion of its value:
   > **e^C = e^A e^B**
   
   with
   > **C = A + B + A × B + ⅓(A × (A × B) + B × (B × A)) + ···**
   
   Show that these first terms of the series are correct. This formula again shows the importance of the commutator **A × B** in quantifying the difference with fully commuting variables. We should warn you that the general terms of the series are more complicated than the first few suggest.

4. **Directional differentiation of spherical projection.**
   Suppose that we project a vector **x** on the unit sphere by the function **x → P[x] = x/‖x‖**. Compute its directional derivative in the **a** direction, as a standard differential quotient using Taylor series expansion. Use geometric algebra to write the result compactly, and give its geometric meaning. (Hint: See Figure 8.3.)

   *[Figure 8.3: The directional derivative of the spherical projection.]*

5. Justify the following form of Taylor's expansion formula of a function F around the location **x**:
   > **F(x + a) = e^(a∗∂ₓ) F(x)**
   
   where you can interpret the exponent in a natural manner as a symbolic expansion instruction.

6. For variable **I(τ)**, the resulting **∂τX(τ)** of (8.8) can still be written as a commutator **X × B** with a bivector B. Derive the explicit expression for B:
   > **B = I ∂τ[φ] + ∂τ[I] (e^(Iφ) − 1)/I**
   
   Hint: One way is to use the result **B = −2 ∂τ[R] R̃** from [15].
