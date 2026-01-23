# 6 The Fundamental Product of Geometric Algebra

We have seen how the outer product and the contraction characterize rather different properties of subspaces: qualitative spanning and quantitative measurements. Together, they have given us an enriched view of the linear algebra of subspaces. This much has been known for some time, and is part of the branch of applied mathematics that is called Grassmann-Cayley algebra.

In this chapter we will start afresh and introduce the basics of Clifford algebra to develop a powerful geometric algebra. This geometric algebra will incorporate operators on subspaces into our framework, and permit us to displace the constructions of the subspace algebra in a structure-preserving manner. The crucial construction is to unify the qualitative and quantitative subspace products into a single **geometric product**, more fundamental than either. The geometric product is invertible, and it allows us to manipulate and solve equations about geometrical quantities almost as if they were regular arithmetical expressions. The true power of this geometric product will become clear in the next chapter, when we use it to define the versor product construction for operators. This chapter defines the geometric product, first for vectors and then for general multivectors. Subsequently, we show how the geometric product indeed subsumes the earlier products (which is a bit of tedious but necessary algebra), and we end with the use of its invertibility to define general projection and rejection operations through geometric division.

---

## 6.1 The Geometric Product for Vectors

### 6.1.1 An Invertible Product for Geometry

Consider a fixed and known vector **a** and an unknown vector **x**, both in a Euclidean vector space ℝⁿ. Let us assume that all we know about **x** is the scalar value α of its inner product with **a**. Then **x** must satisfy **x** · **a** = α. This implies that the endpoint of **x** lies on a hyperplane perpendicular to the direction of **a**. In Figure 6.1, this is sketched in ℝ³'⁰ as the yellow plane. Geometrically, it is clear that we cannot retrieve **x** from α and **a**. Algebraically, this means that there is no unique "inner division". If there were, we could invert the inner product and retrieve **x** from its product with **a** by means of some formula like (**x** · **a**)/**a** = **x**.

The outer product is not much better in this respect. Suppose that we were told the value of the outer product of **a** and **x** is to be the bivector **B**. That bivector must of course be an area element of the plane shared by **a** and **x**. The equation **x** ∧ **a** = **B** defines a line in space, offset from the origin. (You can see this as follows: let **p** be a solution of **p** ∧ **a** = **B**. Then **x** satisfies **x** ∧ **a** = **p** ∧ **a**, so that (**x** − **p**) ∧ **a** = 0. We saw in Section 2.8.1 that this implies (**x** − **p**) = λ**a**. Therefore **x** = **p** + λ**a**, a general point on the line through **p** in the direction **a**.) This line has been sketched in blue in Figure 6.1. The endpoint of **x** must be on this line; but knowing the line does not specify **x**. This is the geometrical reason why we cannot algebraically retrieve **x** from knowing the outer product **B** and **a**; there is no "outer division", and no formula such that (**x** ∧ **a**)/**a** = **x** for all **x**.

We thus see that, when taken separately, the two products with **a** are insufficient to retrieve **x**; yet they are somehow complementary. Indeed, combining the two pieces of information is obviously enough to fully determine **x**, with its endpoint at the intersection of the hyperplane and the line, as illustrated in Figure 6.1 for 3-D space. Therefore a product of **x** and **a** that contains both the inner product and outer product information should be invertible.

> **Figure 6.1:** Combination of the noninvertible subspace products leads to the invertible geometric product (see text).

### 6.1.2 Symmetry and Antisymmetry

There is a clean way to construct a composite product from the inner product **x** · **a** and the outer product **x** ∧ **a**. It is based on their symmetries. The inner product **x** · **a** is symmetric in **x** and **a**, for it retains its value when **x** and **a** are interchanged. The outer product **x** ∧ **a** is antisymmetric; it changes sign under exchange of **x** and **a**.

We can now make a new product between **x** and **a** such that the inner product is its symmetric part and the outer product its antisymmetric part. That defines it uniquely. This product is called the **geometric product** (though some call it the Clifford product after its 1872 inventor William Kingdon Clifford). It is so central that we use the empty symbol ' ' to denote it, writing **x a** for the geometric product of **x** and **a**.

The demands on its symmetric and antisymmetric parts give the equations

$$\mathbf{x} \cdot \mathbf{a} = \frac{1}{2}(\mathbf{x}\,\mathbf{a} + \mathbf{a}\,\mathbf{x})$$
**(6.1)**

and

$$\mathbf{x} \wedge \mathbf{a} = \frac{1}{2}(\mathbf{x}\,\mathbf{a} - \mathbf{a}\,\mathbf{x})$$
**(6.2)**

By adding these equations, we find that the geometric product of the vectors **x** and **a** must be

**geometric product for vectors:**
$$\mathbf{x}\,\mathbf{a} \equiv \mathbf{x} \cdot \mathbf{a} + \mathbf{x} \wedge \mathbf{a}$$
**(6.3)**

This product of two vectors produces a multivector that consists of a scalar part and a 2-blade part. That is unusual; our previous products always produced outcomes of a single grade. But it is precisely because the parts of different grades do not mix in an addition that they can be retrieved separately. That makes the geometric product invertible.

### 6.1.3 Properties of the Geometric Product

Let us check the algebraic properties of this new product between vectors:

- **Commutativity.** The geometric product of two general vectors is not commutative, for the equation **x a** = **a x** would imply that **x** ∧ **a** = 0. This means that commutativity only happens when **x** and **a** are parallel. On the other hand, the product is also not anticommutative, for that would imply **x** · **a** = 0, which is also a special relationship of **x** and **a**. As a consequence of this lack of general commutativity, we should be very careful about the order of the factors in the product **x a**.

- **Linearity and Distributivity.** The geometric product is linear and distributive, since both the inner and the outer product are, and these properties inherit under addition.

- **Associativity.** Definition 6.3 does not specify how to compute the geometric product of more than two vector factors. We have motivated our definition because we wanted an invertible product so that (**x a**)/**a** would be equal to **x** (with division defined in terms of the geometric product). This suggests that we should define the product to be associative. The desired equation then holds, since we could rewrite it to (**x a**)/**a** = **x** (**a**/**a**) = **x**. Moreover, in an associative algebra, each invertible element has a unique inverse, so the division would be uniquely defined. (We clarify that point later, in Section 6.1.5.)

We give the fully general algebraic definition of the geometric product in Section 6.2.1. But first, we would like to familiarize you with the use of having such a product for vectors, to aid your intuition and acceptance of this new construction.

### 6.1.4 The Geometric Product for Vectors on a Basis

When asked to evaluate the geometric product of two vectors **a** and **b** given in a coordinate basis, we can simply evaluate their inner and outer products and add them. However, it is more direct to expand the geometric product in terms of a sum of geometric products of the coordinate vectors. We then need to establish what those basis products are.

Let us take an orthonormal basis {**e**ᵢ} in a metric space ℝⁿ. The geometric product of a basis vector with itself evaluates to a scalar derived from the metric:

$$\mathbf{e}_i\,\mathbf{e}_i = \mathbf{e}_i \cdot \mathbf{e}_i = Q[\mathbf{e}_i, \mathbf{e}_i]$$

where we used either the inner product or the bilinear form Q of the metric space (see Appendix A). In a Euclidean space ℝⁿ'⁰, this is of course simply equal to 1 for all orthonormal basis vectors.

For two different vectors from the orthonormal basis, we get

$$\mathbf{e}_i\,\mathbf{e}_j = \mathbf{e}_i \cdot \mathbf{e}_j + \mathbf{e}_i \wedge \mathbf{e}_j = \mathbf{e}_i \wedge \mathbf{e}_j$$

This does not simplify further, but it does show that **e**ᵢ **e**ⱼ = −**e**ⱼ **e**ᵢ when i ≠ j. We sometimes denote **e**ᵢ **e**ⱼ as **e**ᵢⱼ to show more clearly that it is a single element of the algebra. This element has an unusual property:

$$\mathbf{e}_{ij}^2 = (\mathbf{e}_i\,\mathbf{e}_j)(\mathbf{e}_i\,\mathbf{e}_j) = \mathbf{e}_i(\mathbf{e}_j\,\mathbf{e}_i)\mathbf{e}_j = -\mathbf{e}_i(\mathbf{e}_i\,\mathbf{e}_j)\mathbf{e}_j = -(\mathbf{e}_i\,\mathbf{e}_i)(\mathbf{e}_j\,\mathbf{e}_j) = -1$$
**(6.4)**

Therefore the algebra of the real Euclidean vector space ℝ²'⁰ contains an element **e**₁₂ that squares to −1 under the geometric product! It is not the imaginary unit from complex numbers, but a real 2-blade, representing a unit plane.

In a 2-D vector space, the element **e**₁₂ completes the algebra. Multiplying **e**₁₂ with **e**₁ reverts to something we already had:

$$\mathbf{e}_{12}\,\mathbf{e}_1 = \mathbf{e}_1\,\mathbf{e}_2\,\mathbf{e}_1 = -\mathbf{e}_2\,\mathbf{e}_1\,\mathbf{e}_1 = -\mathbf{e}_2(\mathbf{e}_1 \cdot \mathbf{e}_1)$$

so this is simply a multiple of **e**₂. For the 2-D Euclidean space ℝ²'⁰ with orthonormal basis, the full multiplication table is:

|       | 1     | **e**₁  | **e**₂  | **e**₁₂ |
|-------|-------|---------|---------|---------|
| **1** | 1     | **e**₁  | **e**₂  | **e**₁₂ |
| **e**₁| **e**₁| 1       | **e**₁₂ | **e**₂  |
| **e**₂| **e**₂| −**e**₁₂| 1       | −**e**₁ |
| **e**₁₂| **e**₁₂| −**e**₂ | **e**₁  | −1      |

Now we can use the linearity and distributivity to compute the geometric product of any two vectors. For **a** = a₁**e**₁ + a₂**e**₂ and **b** = b₁**e**₁ + b₂**e**₂:

$$\mathbf{a}\,\mathbf{b} = (a_1\mathbf{e}_1 + a_2\mathbf{e}_2)(b_1\mathbf{e}_1 + b_2\mathbf{e}_2)$$
$$= a_1b_1(\mathbf{e}_1\,\mathbf{e}_1) + a_2b_2(\mathbf{e}_2\,\mathbf{e}_2) + a_1b_2(\mathbf{e}_1\,\mathbf{e}_2) + a_2b_1(\mathbf{e}_2\,\mathbf{e}_1)$$
$$= (a_1b_1 + a_2b_2) + (a_1b_2 - a_2b_1)\mathbf{e}_{12}$$

By the extension of these techniques, the geometric product can be computed for vectors in n-dimensional space.

### 6.1.5 Dividing by a Vector

Since the geometric product on vectors is invertible, a vector **a** should have an inverse. This inverse **a**⁻¹ is easy to find:

**inverse of a vector:**
$$\mathbf{a}^{-1} = \frac{\mathbf{a}}{\mathbf{a} \cdot \mathbf{a}} = \frac{\mathbf{a}}{\mathbf{a}^2}$$
**(6.5)**

This indeed works, for

$$\mathbf{a}^{-1}\,\mathbf{a} = \frac{1}{\mathbf{a} \cdot \mathbf{a}}\mathbf{a}\,\mathbf{a} = \frac{1}{\mathbf{a} \cdot \mathbf{a}}(\mathbf{a} \cdot \mathbf{a} + \mathbf{a} \wedge \mathbf{a}) = \frac{1}{\mathbf{a} \cdot \mathbf{a}}(\mathbf{a} \cdot \mathbf{a} + 0) = 1$$

Vectors with zero norms (the null vectors of Appendix A) do not have inverses.

The associativity of the geometric product makes the inverse of a vector unique. If **ã** would also be an inverse of **a**, then **ã a** = 1. Now right-multiply both sides by **a**⁻¹, regroup by associativity, and you get **ã** = **a**⁻¹. Therefore, there is only one inverse.¹

Having the inverse allows us to divide by vectors, so that we indeed can retrieve **x** from knowing the value of (**x a**) and **a**, as was our goal:

$$(\mathbf{x}\,\mathbf{a})\,\mathbf{a}^{-1} = \mathbf{x}\,(\mathbf{a}\,\mathbf{a}^{-1}) = \mathbf{x}$$

This shows the necessity of the associativity property. We often prefer to denote this by a division sign as (**x a**)/**a**, but note that the noncommutativity of the geometric product implies that division is also noncommutative. So using the notation /**a** is permitted as long as we remember that this means "division *on the right* by **a**."

Geometrically, the inverse of a vector **a** is a vector in the same direction as **a**, and properly rescaled.

### 6.1.6 Ratios of Vectors as Operators

Having an algebraic definition of the division of vectors already helps to solve geometric problems. In a 2-D Euclidean space ℝ²'⁰, we can pose the similarity problem illustrated in Figure 6.2:

> Given two vectors **a** and **b**, and a third vector **c** (in the plane of **a** and **b**), determine **x** so that **x** is to **c** as **b** is to **a** (i.e., solve **x** : **c** = **b** : **a**).

It is geometrically intuitive what we would want: a proportionality involving both the relative length and angle of **b** and **a** should be transferred to **x** and **c**.

We take a leap of faith, and read this ratio in terms of the geometric product. So we guess that the solution to this might be the solution to the equation

$$\mathbf{x}\,\mathbf{c}^{-1} = \mathbf{b}\,\mathbf{a}^{-1}$$

The solution is immediate through right-multiplication of both sides by **c**:

$$\mathbf{x} = (\mathbf{b}\,\mathbf{a}^{-1})\,\mathbf{c}$$
**(6.6)**

> **Figure 6.2:** Ratios of vectors.

This is a fully computable expression. For instance, with **a** = **e**₁ (so that **a**⁻¹ = **e**₁), **b** = **e**₁ + **e**₂, and **c** = 2**e**₂ in the standard orthonormal basis, we obtain **x** = ((**e**₁ + **e**₂) **e**₁⁻¹) 2**e**₂ = 2(1 − **e**₁ **e**₂) **e**₂ = 2(**e**₂ − **e**₁). Draw a picture like Figure 6.2 to convince yourself of the correctness of this outcome.

In fact, we might see (**b a**⁻¹) in (6.6) as an operator that acts on **c** to produce **x**. The operator is parametrized by **a** and **b**, and it should be capable of both rotation and scaling to produce **x** from **c**. From the construction above, we would suspect that it only depends on the relative angle and size of the vectors **a** and **b**. If that is so, we may as well take **a** to be the unit vector **e**₁ and **b** = ρ (cos θ **e**₁ + sin θ **e**₂), with ρ the relative length and θ the relative angle (from **a** to **b**). Then we compute that the rotation/scaling operator is

$$\mathbf{b}\,\mathbf{a}^{-1} = \rho(\cos\theta\,\mathbf{e}_1 + \sin\theta\,\mathbf{e}_2)\,\mathbf{e}_1 = \rho(\cos\theta - \sin\theta\,\mathbf{e}_{12})$$

You may verify that **b a**⁻¹ acts on the basis vector **e**₁ to produce ρ (cos θ **e**₁ + sin θ **e**₂), and on **e**₂ it yields ρ (cos θ **e**₂ − sin θ **e**₁). Moreover, since the geometric product is linear, these results can be used to produce the result on a general vector **c** = c₁ **e**₁ + c₂ **e**₂, which yields the **x** of our problem:

$$\mathbf{x} = \rho(c_1\cos\theta - c_2\sin\theta)\,\mathbf{e}_1 + \rho(c_1\sin\theta + c_2\cos\theta)\,\mathbf{e}_2$$
**(6.7)**

This is precisely the solution we would expect to the original problem, if we would have expanded it in coordinates. It is clearly a rotation combined with a scaling. You would represent it in terms of a matrix operation as

$$\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} \rho\cos\theta & -\rho\sin\theta \\ \rho\sin\theta & \rho\cos\theta \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$
**(6.8)**

when expressed on the {**e**₁, **e**₂} basis.

It is highly satisfactory that our geometric product not only produces this result, but that it does so in the form (6.6): **x** = (**b**/**a**) **c**. That expression is immediately derivable from the original problem statement and completely formulated in terms of the elements of the problem, rather than using an extraneous coordinate system. If you have to write code, that is how you would want to specify it in a high-level programming language for geometry; in comparison, (6.7) and especially (6.8) feel like assembly code, with their use of coordinates reminiscent of registers.

The coordinate-free operator **b**/**a** is a good example of the kind of operational power that the geometric product gives us. We will have much more to say about such operators in Chapter 7.

---

## 6.2 The Geometric Product of Multivectors

In the definition of the geometric product for vectors, we followed a geometric motivation and defined it in terms of inner product and outer product, loosely following its historic process of invention by Clifford. We then claimed it was actually more fundamental than either. If that is indeed the case, we should be able to start with the geometric product and define it algebraically without reference to the other products. We do that now, for it allows us to extend the geometric product properly beyond vector terms and use it as the foundation of our geometric algebra.

### 6.2.1 Algebraic Definition of the Geometric Product

We start with a metric vector space ℝⁿ and its linear space of subspaces ⋀ℝⁿ. Its metric is characterized by a bilinear form Q (see Appendix A), or, equivalently, by an inner product of vectors.

We define the geometric product from ⋀ℝⁿ × ⋀ℝⁿ to ⋀ℝⁿ by the following properties:

- **Scalars.** The geometric product is an extension of the usual scalar multiplication in ⋀ℝⁿ, so the expressions α β and α **x**, α, β ∈ ℝ can from now on be read as involving the geometric product. We will explicitly define this multiplication by a scalar to be commutative with any element A:
  
  $$\alpha A = A\alpha \quad \text{for all } \alpha \in \mathbb{R}, A \in \bigwedge\mathbb{R}^n$$

- **Scalar Squares.** The geometric product **x**² ≡ **x x** of a vector **x** with itself is defined to be a scalar, equivalent to the metric quantity **x** · **x** = Q[**x**, **x**]. This ties the geometric product to the metric of the vector space ℝⁿ.

- **Distributivity and Linearity.** The geometric product is defined to be distributive over the addition of elements:
  
  $$A(B + C) = AB + AC \quad \text{and} \quad (A + B)C = AC + BC$$
  
  This also defines the general linearity of the geometric product (since A can be a scalar).

- **Associativity.** The geometric product is defined to be associative:
  
  $$A(BC) = (AB)C$$
  
  so that we may write ABC without confusion about the result.

- **Commutativity Not Required!** The geometric product is not defined to be either purely commutative or purely anticommutative (although it may be either, for suitably chosen factors). This is essential, as it permits the geometric product to unite the commutative properties of metric computations with the anticommutative properties of spanning to produce a product that is complete in its geometric properties.

Note that our original definition (6.3) of the geometric product as a sum of inner and outer product is not part of these algebraic defining properties. We will actually rederive (6.3), and with it will define the outer product and contraction in terms of the geometric product. Such a procedure demonstrates that it is indeed the more fundamental of the three, our order of treatment in this book notwithstanding.

The geometric product makes our algebra of ⋀ℝⁿ into a true **geometric algebra**, and we will use that term from now on. It transcends the subspace algebra we have used so far, and has a much more rich, powerful, and consistent structure. While subspace algebra was similar to Grassmann-Cayley algebra, geometric algebra closely resembles a nongeometrical mathematical construction called Clifford algebra. The terms are often used interchangeably by others, but we will make a distinction. For the moment, you can think of geometric algebra as the geometrically significant part of Clifford algebra. We will be able to make this distinction more precise in Section 7.7.2.

### 6.2.2 Evaluating the Geometric Product

Since the above are all the properties of the geometric product, they should enable the expansion of arbitrary expressions of the geometric product of multivectors. Let us do some of this before we proceed—we will develop faster techniques to compute with the geometric product, but it is important to realize that these definitions are indeed complete.

The completeness is most easily shown when we have an orthonormal basis for the metric vector space ℝⁿ. We should demonstrate that we can compute the geometric product of any two basis vectors. This should of course agree with our special case for vectors, computed in Section 6.1.4, but we are not allowed to use those. We should work fully from the algebraic definition just given.

The geometric product of a basis vector with itself is easy, since by definition it can be expressed in terms of the bilinear form or the inner product that is part of the definition of the metric vector space:

$$\mathbf{e}_i\,\mathbf{e}_i = \mathbf{e}_i \cdot \mathbf{e}_i = Q[\mathbf{e}_i, \mathbf{e}_i]$$

But the geometric product of two different basis vectors **e**ᵢ **e**ⱼ does not appear to allow simplification by the axioms:

$$\mathbf{e}_i\,\mathbf{e}_j = \,?$$

We know from the vector computations that it cannot be simplified, but we would at least like to be able to show that **e**ⱼ **e**ᵢ = −**e**ᵢ **e**ⱼ to be in correspondence with the geometric product as we defined it earlier for vectors.

There is a neat trick called **polarization** that comes to the rescue. The bilinear form or inner product of the metric vector space can be evaluated on any two vectors. The bilinear nature gives an identity for Q[**x**, **y**] or **x** · **y** that can be manipulated into a symmetric shape:

$$\mathbf{x} \cdot \mathbf{y} = \frac{1}{2}\left((\mathbf{x} + \mathbf{y}) \cdot (\mathbf{x} + \mathbf{y}) - (\mathbf{x} \cdot \mathbf{x}) - (\mathbf{y} \cdot \mathbf{y})\right)$$
$$= \frac{1}{2}\left((\mathbf{x} + \mathbf{y})(\mathbf{x} + \mathbf{y}) - (\mathbf{x}\,\mathbf{x}) - (\mathbf{y}\,\mathbf{y})\right)$$
$$= \frac{1}{2}(\mathbf{x}\,\mathbf{y} + \mathbf{y}\,\mathbf{x})$$
**(6.9)**

Therefore the inner product **x** · **y** of two general vectors is the symmetric part of their geometric product. We are thus able to derive part of our motivating definitions of Section 6.1.2 from the algebraic definition above.

This symmetry property gives us the idea to manipulate our different basis vectors by splitting the product in its symmetric and antisymmetric parts:

$$\mathbf{e}_i\,\mathbf{e}_j = \frac{1}{2}(\mathbf{e}_i\,\mathbf{e}_j + \mathbf{e}_j\,\mathbf{e}_i) + \frac{1}{2}(\mathbf{e}_i\,\mathbf{e}_j - \mathbf{e}_j\,\mathbf{e}_i)$$
$$= \mathbf{e}_i \cdot \mathbf{e}_j + \frac{1}{2}(\mathbf{e}_i\,\mathbf{e}_j - \mathbf{e}_j\,\mathbf{e}_i)$$
$$= 0 + \frac{1}{2}(\mathbf{e}_i\,\mathbf{e}_j - \mathbf{e}_j\,\mathbf{e}_i)$$

since in the orthonormal basis **e**ᵢ · **e**ⱼ = 0 for i ≠ j. It follows that

$$\mathbf{e}_i\,\mathbf{e}_j = -\mathbf{e}_j\,\mathbf{e}_i$$

So the new definition indeed permits us to derive this important property of the multiplication of basis vectors.

With the multiplication of the basis elements established, we can use associativity, linearity, and distributivity to compute the geometric product of any two elements in the linear space ⋀ℝⁿ.

### 6.2.3 Grades and the Geometric Product

At this point you may object that we have not really shown that the geometric product, constructing elements starting from a metric vector space ℝⁿ, really generates the same linear structure of elements of different grades that we had before. We are therefore formally not allowed to write ⋀ℝⁿ for the space in which geometric algebra lives.

That is a correct objection; but if the spaces are not the same, they are certainly algebraically isomorphic, and that is good enough to identify them geometrically. The reason is that the orthonormal basis of the vector space ℝⁿ leads to a basis for the product structure that satisfies **e**ᵢ **e**ⱼ = −**e**ⱼ **e**ᵢ. That is the essence in generating the higher-grade elements. This property is identical to the outer product antisymmetric property **e**ᵢ ∧ **e**ⱼ = −**e**ⱼ ∧ **e**ᵢ. The identity of these properties means that we can use the geometric product to at least faithfully reconstruct the basis of the ladder of subspaces ⋀ℝⁿ that we originally made using the outer product.

And even though the geometric product has richer properties than the outer product, we cannot make other elements beyond the ladder of subspaces. Consider for example **e**₁ (**e**₁**e**₂) as an attempt to make something new. Had we used the outer product, the construction **e**₁ ∧ (**e**₁**e**₂) = **e**₁ ∧ (**e**₁ ∧ **e**₂) would have been zero. For the geometric product, the result is not zero, but it reverts to something we already have:

$$\mathbf{e}_1\,(\mathbf{e}_1\mathbf{e}_2) = \mathbf{e}_1\,\mathbf{e}_1\,\mathbf{e}_2 = (\mathbf{e}_1^2)\,\mathbf{e}_2$$

so this is ±**e**₂, depending on the metric. You can generalize this argument to show that nothing beyond the elements of ⋀ℝⁿ can be made; the scalar squares foil any such attempt. Therefore, the geometric product of a metric vector space ℝⁿ "lives" in precisely the same structure ⋀ℝⁿ as the outer product of the same space ℝⁿ.

However, this analysis brings out an important difference between the geometric product and the outer product. When multiplying the extended basis elements of grade k and grade l by the outer product, we are left with a single element of grade k + l (or zero). With the geometric product, the product of two basis elements of grade k and l may have any of the grades

$$|k - l|, |k - l| + 2, \ldots, (k + l - 2), (k + l)$$

The highest grade (k + l) occurs when all basis vectors in the elements are different. (The geometric product is then essentially the same as the outer product of those elements.) But each vector in common between the two basis elements reduces the grade by two as it combines to produce a scalar. The extreme case is when all the vectors in one are contained in the other, leaving only |k − l| factors as a result. (The geometric product is then the left or right contraction of one argument onto the other.)

If we now have arbitrary elements Aₖ and Bₗ of grade k and l, respectively, these can be decomposed on the bases of ⋀ᵏℝⁿ and ⋀ˡℝⁿ. When we multiply them using the geometric product, any or all of the possible grades between |k − l| and (k + l) may occur. Therefore the geometric product produces multivectors of mixed grade. The grade() operation no longer has a single integer value in geometric algebra.

The algebraic invertibility of the geometric product can now be understood in principle. The series of terms in the geometric product of the two elements Aₖ and Bₗ apparently give us a complete inventory of their relative geometric relationship, allowing full reconstruction of one when we are given the other.

---

## 6.3 The Subspace Products Retrieved

The geometric product is the fundamental product in geometric algebra—you will not need any other product, since it contains all geometric relationships between its arguments. Yet we have seen that the subspace products (by which we mean the outer product, scalar product, and contraction) are also useful geometrically. In fact, the whole geometrical concept of subspace requires the outer product to be encoded in our algebra.

Since we want to have those products to "do geometry," we should show that they are included in our geometric algebra based on the geometric product. There are two routes:

- We could use the symmetries of the geometric product to retrieve outer product and contraction (basically reversing the construction that motivated the geometric product in Section 6.1.2). This is actually only partly successful. It does not define the subspace products fully, but it does show that they are consistent with the symmetry structure of the geometric product. When we perform the analysis in Section 6.3.1 below, we obtain many useful relationships between the various products.

- We can identify the subspace products of blades as certain well-defined grades of their geometric product. This indeed defines them fully, though it gives us less algebraic insight in their relationships. We do this in Section 6.3.2.

In the practice of applying the subspace products, both approaches are useful. Depending on the geometrical problem that one tries to solve computationally, either may feel like the more direct route. That is why we present both.

### 6.3.1 The Subspace Products from Symmetry

The familiar outer product of a vector **a** with a blade **B** can be related to the geometric product by the following two expressions:

$$\mathbf{a} \wedge \mathbf{B} = \frac{1}{2}(\mathbf{a}\,\mathbf{B} + \widehat{\mathbf{B}}\,\mathbf{a})$$
**(6.10)**

$$\mathbf{B} \wedge \mathbf{a} = \frac{1}{2}(\mathbf{B}\,\mathbf{a} + \mathbf{a}\,\widehat{\mathbf{B}})$$
**(6.11)**

where B̂ = (−1)^grade(B) **B** is the grade involution of **B** introduced in Section 2.9.5. (Writing the equations in this form makes it easier to lift them to general multivectors **B**.)

The proof of these statements may be found in Section C.1 of Appendix C. It demonstrates that the two equations above indeed identify the same outer product structure that we had before, at least when one of the factors is a vector, and it proves the associativity (**x** ∧ **y**) ∧ **z** = **x** ∧ (**y** ∧ **z**) of the product thus defined. Because of that associativity, this outer product in terms of the geometric product can be extended to general blades, and by linearity to general multivectors. Only the case of two scalars is formally not included, but other than that this outer product is isomorphic to the outer product we had before.

The contractions can be related to the geometric product in similar fashion when they involve a vector factor **a**:

$$\mathbf{a} \rfloor \mathbf{B} = \frac{1}{2}(\mathbf{a}\,\mathbf{B} - \widehat{\mathbf{B}}\,\mathbf{a})$$
**(6.12)**

$$\mathbf{B} \lfloor \mathbf{a} = \frac{1}{2}(\mathbf{B}\,\mathbf{a} - \mathbf{a}\,\widehat{\mathbf{B}})$$
**(6.13)**

The proof of these statements may be found in Section C.2 of Appendix C.

Unfortunately, because of lack of associativity, we cannot prove the defining equation (3.11) **A**⌋(**B**⌋**C**) = (**A** ∧ **B**)⌋**C** (nor its counterpart for the right contraction). Neither can we define the contraction result on two scalar arguments in this manner. So although the products defined by (6.12) and (6.13) are consistent with the earlier contractions, the contractions based on the symmetries of the geometric product are not pinned down very precisely. This algebraic freedom partly explains the variation in inner products in the geometric algebra literature exposed in Appendix B.

But at least for a vector factor, the constructions above define the subspace products uniquely. Conversely, this means that the geometric product of a vector with an arbitrary multivector can be decomposed using the contraction and the outer product.

$$\mathbf{a}\,\mathbf{B} = \mathbf{a} \rfloor \mathbf{B} + \mathbf{a} \wedge \mathbf{B}$$
**(6.14)**

$$\widehat{\mathbf{B}}\,\mathbf{a} = \mathbf{B} \lfloor \mathbf{a} + \mathbf{B} \wedge \mathbf{a} = -\mathbf{a} \rfloor \mathbf{B} + \mathbf{a} \wedge \mathbf{B}$$
**(6.15)**

where we used (3.19) to convert the right contraction to a left contraction. These equations subsume and generalize (6.3).

The subspace product definitions permit us to change the order of multiplications in a geometric product, which is often convenient in evaluating expressions:

$$\widehat{\mathbf{B}}\,\mathbf{a} = \mathbf{a}\,\mathbf{B} - 2\mathbf{a} \rfloor \mathbf{B} = -\mathbf{a}\,\mathbf{B} + 2\mathbf{a} \wedge \mathbf{B}$$
**(6.16)**

and

$$\mathbf{a}\,\mathbf{B} = \widehat{\mathbf{B}}\,\mathbf{a} + 2\mathbf{a} \rfloor \mathbf{B} = -\widehat{\mathbf{B}}\,\mathbf{a} + 2\mathbf{a} \wedge \mathbf{B}$$
**(6.17)**

In all these equations, you may note that right-multiplication of **B** by **a** is always accompanied by a grade involution—the formulas become simplest or most symmetrical when you define them in terms of **a B**, **a**⌋**B**, and **a** ∧ **B**, combined with B̂ **a**, **B**⌊**a** (= −**a**⌋**B**), and **B** ∧ **a** (= **a** ∧ **B**). This grade involution is apparently the natural geometric sign when moving a vector to the right of a blade. We will see this phenomenon reappear throughout the equations of geometric algebra.

You may be puzzled by a paradox in the associativity of the various products. According to (6.14), the geometric product is the sum of the outer product and contraction. Both the geometric product and the outer product are associative, whereas the contraction is not. How can the sum of something associative and something nonassociative ever be associative itself? The solution is: don't look at it that way. Instead, start with the geometric product, which is defined to be associative. Then derive the outer product as (6.10) (i.e., as half the sum of a geometric product and its swapped version). This is associative since addition is associative. Then derive the contraction as (6.12) (i.e., as half the difference of a geometric product and its swapped version). This is nonassociative, since subtraction is nonassociative. Now there is no paradox.

By linearity, all equations in this section are easily extended from a blade **B** to a general multivector B.

### 6.3.2 The Subspace Products as Selected Grades

An alternative way of obtaining the subspace products from the geometric product is as parts of well-chosen grades using the k-grade selection operator ⟨ ⟩ₖ. For the geometric product on vectors, this is simple:

$$\mathbf{a} \cdot \mathbf{b} = \langle \mathbf{a}\,\mathbf{b} \rangle_0 \quad \text{and} \quad \mathbf{a} \wedge \mathbf{b} = \langle \mathbf{a}\,\mathbf{b} \rangle_2$$
**(6.18)**

This generalizes as follows:

$$A_k \wedge B_l \equiv \langle A_k\,B_l \rangle_{k+l}$$
**(6.19)**

$$A_k \rfloor B_l \equiv \langle A_k\,B_l \rangle_{l-k}$$
**(6.20)**

$$A_k \lfloor B_l \equiv \langle A_k\,B_l \rangle_{k-l}$$
**(6.21)**

$$A_k * B_l \equiv \langle A_k\,B_l \rangle_0$$
**(6.22)**

Blades of negative grade are zero—so the left contraction ⌋ is zero when k > l, and the right contraction ⌊ is zero when k < l. By linearity of the geometric product, all these definitions can be lifted from blades to k-vectors and then to multivectors as a sum over the appropriate grades.

In contrast to the symmetry-based approach, these equations are complete definitions for all arguments. The proofs that these equations give the same products we had in the earlier chapters may be found in Section C.3 of Appendix C. It involves some new manipulation techniques that are useful to study.

A surprising property of these definitions is that the selection of certain grades of the geometric product of blades apparently produces another blade. Beware that this does not generalize to the selection of other grade parts!

Once these correspondences with the old subspace products have been established, some of the properties of the subspace products can be used to simplify grade-based expressions and vice versa. For instance, the symmetry property A ∗ B = B ∗ A of the scalar product can be easily lifted to multivectors as A ∗ B = B ∗ A. This implies

$$\langle AB \rangle_0 = \langle BA \rangle_0$$
**(6.23)**

which is a useful cyclic reordering property of the grade-0 symbol.

The grade approach to the subspace products is a feasible way of implementing all products in geometric algebra based on a single implemented product (the geometric product). This is explored in programming exercise 6.7.1.

---

## 6.4 Geometric Division

With the integration of subspace products with the geometric product, we have a more powerful algebra to analyze subspaces. We now combine our new capability of division by a subspace with the earlier techniques. This not only generalizes the projection, but it also produces the compact representation of a new construction: subspace reflection.

### 6.4.1 Inverses of Blades

The geometric product is invertible, so dividing by a multivector has a unique meaning, equivalent to multiplication by the inverse of the multivector. However, not all multivectors have inverses. Fortunately, we are mostly interested in two kinds: blades, and multivectors that can be written as a product of invertible vectors. The latter are called **versors**, and we treat them in Chapter 7; they are obviously invertible (their inverse is formed by the inverses of the vector factors, in reverse order).

Blades are also invertible, if they have a nonzero norm (i.e., if they are not null-blades; see Appendix A). The inverse of a blade **A** is then

**inverse of a blade A:**
$$\mathbf{A}^{-1} = \frac{\mathbf{A}}{\mathbf{A} * \mathbf{A}} = \frac{\widetilde{\mathbf{A}}}{\mathbf{A} * \widetilde{\mathbf{A}}} = \frac{\widetilde{\mathbf{A}}}{\mathbf{A}^2}$$
**(6.24)**

where Ã is the reverse of Section 2.9.5. This formula is based on the property that the squared norm of a blade is a scalar, which makes the division well defined and unambiguous (since a scalar commutes with the geometric product, its right-division and left-division coincide). Its validity is most easily verified using an orthogonal factorization of the blade **A** as a product of orthogonal vectors: **A** = **a**₁ **a**₂ ⋯ **a**ₖ. Such a factorization can be made for invertible blades by the Gram-Schmidt procedure of Section 6.7.2. By computing the geometric product **A** Ã vector by vector, you find that it is equal to **A** ∗ Ã, so that the inverse formula is indeed correct.

This inverse of a blade is unique, by the associativity argument also used in Section 6.1.5.

### 6.4.2 Decomposition: Projection to Subspaces

We can express a vector **x** trivially relative to an invertible blade **A** as **x** = **x** (**A A**⁻¹). Moving the brackets by associativity and invoking (6.14), we get a pleasantly suggestive rewriting. Let us first explore this for a 1-blade **A**, the vector **a**.

$$\mathbf{x} = (\mathbf{x}\,\mathbf{a})\,\mathbf{a}^{-1}$$
$$= (\mathbf{x} \cdot \mathbf{a} + \mathbf{x} \wedge \mathbf{a})\,\mathbf{a}^{-1}$$
$$= (\mathbf{x} \cdot \mathbf{a})\,\mathbf{a}^{-1} + (\mathbf{x} \wedge \mathbf{a})\,\mathbf{a}^{-1}$$
**(6.25)**

The first term in (6.25) is a vector (since it is a scalar times a vector). We recognize it as (**x** · **a**) **a**⁻¹ = (**x** · **a**⁻¹) **a** = (**x**⌋**a**⁻¹)**a**; that is, as the orthogonal projection of **x** onto **a** (see Section 3.6). We can now write it as a division:

**projection of x onto a:** (**x**⌋**a**)/**a**.

It is the component of **x** in the **a**-direction. The second term in (6.25) must then be the component of **x** that contains no **a**-components at all (since the two terms must add to produce **x**). We follow Hestenes [33] in calling this the **rejection** of **x** by **a**:

**rejection of x by a:** (**x** ∧ **a**)/**a**

We can imagine its construction visually as in Figure 6.3: span the bivector **x** ∧ **a**. This is a reshapeable area element, and it is equivalent to a rectangle perpendicular to **a** spanned by some vector **r** perpendicular to **a**. That rectangular element can be written as the outer product **r** ∧ **a**, but because **r** is perpendicular to **a** (implying that **r** · **a** = 0), we can even write it as a geometric product:

$$\mathbf{x} \wedge \mathbf{a} = \mathbf{r} \wedge \mathbf{a} = \mathbf{r} \cdot \mathbf{a} + \mathbf{r} \wedge \mathbf{a} = \mathbf{r}\,\mathbf{a}$$

This rewriting is helpful because the geometric product is invertible; that makes this equation for **r** solvable. Through right-division by **a** on **r a** = **x** ∧ **a**, we obtain the solution **r** = (**x** ∧ **a**)/**a**, which is indeed the rejection of **x** by **a**.

We thus see that the identity **x** = (**x a**)/**a**, when written out in terms of the inner product and the outer product, is actually a decomposition of the vector **x** relative to **a**, providing its **a**-component and non-**a**-component. It offers us the possibility of describing a vector relative to another vector, but does so in a satisfyingly coordinate-free manner.

> **Figure 6.3:** Projection and rejection of **x** relative to **a**.

Returning to the general blade **A** and again invoking (6.14), we find the decomposition

$$\mathbf{x} = (\mathbf{x}\,\mathbf{A})\,\mathbf{A}^{-1} = (\mathbf{x} \rfloor \mathbf{A})\,\mathbf{A}^{-1} + (\mathbf{x} \wedge \mathbf{A})\,\mathbf{A}^{-1}$$
**(6.26)**

You may expect that the first term is a 1-blade fully contained in **A**, and that it should be equal to the projection of **x** onto **A**.

**projection of x onto A:** (**x**⌋**A**)/**A**.

We have encountered this before (in Section 3.6) as (**x**⌋**A**)**A**⁻¹, which commutes with all products. But structural exercise 7 explores why we can replace the contraction by a geometric division in this formula.

The second term is again called the **rejection** of **x** by **A**,

**rejection of x by A:** (**x** ∧ **A**)/**A**,

since it is a vector perpendicular to **A**. To prove that fact compactly, we combine the subspace products and the grade selection of the geometric product (to be frank, it took us about an hour to make it this simple). If (**x** ∧ **A**) **A**⁻¹ is perpendicular to **A**, it should be perpendicular to any vector in **A**. Let us pick one, **a**, and compute the inner product:

$$\mathbf{a} \cdot \left((\mathbf{x} \wedge \mathbf{A})\,\mathbf{A}^{-1}\right)$$
$$= \langle \mathbf{a}\,(\mathbf{x} \wedge \mathbf{A})\,\mathbf{A}^{-1} \rangle_0$$
$$= \frac{1}{2}\langle \mathbf{a}\,\mathbf{x}\,\mathbf{A}\,\mathbf{A}^{-1} + \mathbf{a}\,\widehat{\mathbf{A}}\,\mathbf{x}\,\widehat{\mathbf{A}^{-1}} \rangle_0$$
$$= \frac{1}{2}\langle \mathbf{a}\,\mathbf{x} - \widehat{\mathbf{A}}\,\mathbf{a}\,\mathbf{x}\,\mathbf{A}^{-1} + 2(\mathbf{a} \wedge \mathbf{A})\,\mathbf{x}\,\mathbf{A}^{-1} \rangle_0$$
$$= \frac{1}{2}\langle \mathbf{a}\,\mathbf{x} - \mathbf{a}\,\mathbf{x}\,\mathbf{A}^{-1}\,\mathbf{A} - 0 \rangle_0$$
$$= \frac{1}{2}\langle \mathbf{a}\,\mathbf{x} - \mathbf{a}\,\mathbf{x} \rangle_0 = 0$$

Identify the steps we took—they are all based on formulas in this chapter and you will see an instructive example of how the grade approach and the symmetry approach to the subspace products can be combined. In the rejection, we can substitute the geometric product in (**x** ∧ **A**) **A**⁻¹ by a right contraction (see structural exercise 8).

Although we can replace the geometric products by contractions in both projection and rejection, there is not necessarily an advantage in doing so. The geometric product is invertible, and this often helps to simplify expressions, so that would plead in favor of leaving it. On the other hand, the contraction helps remind us of the containment relationships (subspaces taken out of other subspaces), and makes it easier to apply duality relationships to convert the subspace products.

Since projection and rejection are linear transformations, we can extend them from vectors to general blades as outermorphisms (and even to multivectors, by linearity). For the projection, we have done this before in Section 4.2.2, and we derived that it boils down to substituting the general blade **X** for the vector **x**, to obtain

**projection of X onto A:**
$$\mathbf{X} \mapsto (\mathbf{X} \rfloor \mathbf{A})\,\mathbf{A}^{-1}$$
**(6.27)**

However, the outermorphic extension of the rejection quickly disappoints, since it becomes a rather trivial operation (although indeed linear). For (**X** ∧ **A**) **A**⁻¹ is zero as soon as **X** contains at least one common vector with **A** (and if both **X** and **A** were bivectors in 3-D, this would always be the case). The easiest way to express the concept of the rejection of a general blade **X** by a subspace **A** is simply as the difference of **X** and its projection: **X** → **X** − (**X**⌋**A**) **A**⁻¹. However, this is not a proper subspace operation; it does not necessarily produce a blade (see structural exercise 9), so it should be used with care. The rejection is not as tidy as it appears at first sight, when we introduced it for vectors.

### 6.4.3 The Other Division: Reflection

We have seen that the geometric product is noncommutative. This implies that geometric division (which is just geometric multiplication by the inverse) is not commutative either. We have also seen that division of (**x a**) by **a** on the right (i.e., right division) produces **x**, as you would hope. Let us investigate the result of left division:

$$\mathbf{a}^{-1}\,\mathbf{x}\,\mathbf{a} = \mathbf{a}^{-1}\,(\mathbf{x}\,\mathbf{a})$$
$$= \frac{1}{\mathbf{a}\,\mathbf{a}}\mathbf{a}\,(\mathbf{x}\,\mathbf{a})$$
$$= \mathbf{a}\,\mathbf{x}\,\mathbf{a}\frac{1}{\mathbf{a}\,\mathbf{a}} \quad [\text{since scalars commute}]$$
$$= (\mathbf{a}\,\mathbf{x})\,\mathbf{a}^{-1}$$
$$= (\mathbf{a} \cdot \mathbf{x})\,\mathbf{a}^{-1} + (\mathbf{a} \wedge \mathbf{x})\,\mathbf{a}^{-1}$$
$$= (\mathbf{x} \cdot \mathbf{a})\,\mathbf{a}^{-1} - (\mathbf{x} \wedge \mathbf{a})\,\mathbf{a}^{-1}$$
**(6.28)**

Compare this to the decomposition of (6.26) (which was made with right division):

$$(\mathbf{x}\,\mathbf{a})\,\mathbf{a}^{-1} = (\mathbf{x} \cdot \mathbf{a})\,\mathbf{a}^{-1} + (\mathbf{x} \wedge \mathbf{a})\,\mathbf{a}^{-1}$$

We observe that in (6.28) the non-**a**-component of **x** (which we called the rejection of **a**) is *subtracted* from the projection of **x** onto **a**, rather than added. Figure 6.4 shows the effect: the vector **x** is reflected in the **a**-line. Only when **x** and **a** have the same direction is there no difference between the two types of division (but they then trivially both result in **x**).

> **Figure 6.4:** Reflection of **x** in **a**.

The bad news is that we have to be careful about the order of division, but the good news is that we have found a simple way to make line reflections: we can reflect **x** through **a** by sandwiching **x** between **a** and **a**⁻¹ as **a**⁻¹ **x a** or equivalently **a x a**⁻¹. This is actually one of the basic constructions in geometric algebra, so common that it could be considered as a product in its own right, the "versor product" of **x** by **a**. It can be extended to blades, and is then a powerful way to represent orthogonal transformations.

The next chapter is fully devoted to this important operation.

---

## 6.5 Further Reading

With the geometric product, you are almost ready to read the literature on geometric algebra. However, since that typically involves the special representations of operators by rotors and versors, we recommend that you wait for one more chapter.

But if you are interested in the historical roots, an inspirational piece (without rotors) that focuses on the development of number systems for geometry is David Hestenes' *Origins of Geometric Algebra*, Chapter 1 in [29]. It traces the developments from Euclid via Descartes to Grassmann, and, implicitly, Clifford. Leo can recommend it as the piece that got him hooked, back in 1997.

---

## 6.6 Exercises

### 6.6.1 Drills

1. Let **a** = **e**₁ + **e**₂ and **b** = **e**₂ + **e**₃ in a 3-D Euclidean space with orthonormal basis {**e**₁, **e**₂, **e**₃}. Compute the following expressions, giving the results relative to the basis {1, **e**₁, **e**₂, **e**₃, **e**₂ ∧ **e**₃, **e**₃ ∧ **e**₁, **e**₁ ∧ **e**₂, **e**₁ ∧ **e**₂ ∧ **e**₃}. Show your work.

   (a) **a a**
   
   (b) **a b**
   
   (c) **b a**
   
   (d) (**e**₁ ∧ **e**₂) **a**
   
   (e) **a** (**e**₁ ∧ **e**₂)
   
   (f) (**e**₁ ∧ **e**₂ ∧ **e**₃) **a**
   
   (g) **a**⁻¹
   
   (h) **b a**⁻¹
   
   (i) (**e**₁ ∧ **e**₂)⁻¹

2. Make a full geometric product multiplication table for the 8 basis elements {1, **e**₁, **e**₂, **e**₃, **e**₁ ∧ **e**₂, **e**₂ ∧ **e**₃, **e**₃ ∧ **e**₁, **e**₁ ∧ **e**₂ ∧ **e**₃}; (a) in a Euclidean metric ℝ³'⁰ and (b) in a metric ℝ²'¹ with **e**₁ · **e**₁ = −1.

### 6.6.2 Structural Exercises

1. Section 6.1.1 demonstrated the noninvertibility of contraction and outer product. Show by a geometrical example that the cross product of two vectors is not invertible either. Also give an algebraic argument based on its (invertible) relationship to the outer product.

2. The pseudoscalar is the highest-order blade in the algebra of ℝⁿ. It receives its name because in many dimensions it is like a scalar in its commutation properties with vectors under the geometric product. In which dimensions does it commute with all vectors?

3. The outer product can be defined as the completely antisymmetric summed average of all permutations of geometric products of its factors, with a sign for each term depending on oddness or evenness of the permutation. For the 3-blade, this means:

   $$\mathbf{x} \wedge \mathbf{y} \wedge \mathbf{z} = \frac{1}{3!}(\mathbf{xyz} - \mathbf{yxz} + \mathbf{yzx} - \mathbf{zyx} + \mathbf{zxy} - \mathbf{xzy})$$
   
   Derive this formula.

4. The parts of a certain grade of a geometric product of blades are not necessarily blades. Show that in a 4-D space with orthonormal basis {**e**ᵢ}⁴ᵢ₌₁, a counterexample is ⟨**e**₁ (**e**₁ + **e**₂) (**e**₂ + **e**₃) (**e**₁ + **e**₄)⟩₂. (You may want to use software for this. If you find a simpler counterexample, let us know...)

5. Show that the definition of the scalar product as A ∗ B = ⟨A B⟩₀ is equivalent to the determinant definition of (3.2). You will then also understand why the matrix in the latter definition has the apparently reversed **a**ᵢ · **b**ₖ₋ⱼ as element (i, j) for k-blades.

6. Originally, we motivated the contraction as the counterpart of an outer product relative to the scalar product, which led to the implicit definition (3.6):

   $$(\mathbf{X} \wedge \mathbf{A}) * \mathbf{B} = \mathbf{X} * (\mathbf{A} \rfloor \mathbf{B})$$
   
   Prove this part of the definition using the grade-based definitions of ∧, ∗, and ⌋ in Section 6.3.2.

7. In the formula (**x**⌋**A**⁻¹) **A**, we can replace the geometric product by a contraction, so that it is in fact the projection (**x**⌋**A**⁻¹)⌋**A**. Show this, using the suggestion that **x**⌋**A**⁻¹ might be a subblade of **A**—which you first need to demonstrate. After that, decompose **x**⌋**A**⁻¹ as a product of orthogonal vectors, and evaluate the two formulas to show their equivalence.

8. As a counterpart of the previous exercise, show that (**x** ∧ **A**⁻¹) **A** = (**x** ∧ **A**⁻¹)⌊**A**. (Hint: Write the second **A** as a wedge product of orthogonal vectors, and peel them off one by one).

9. In a 4-D space with orthonormal basis {**e**ᵢ}⁴ᵢ₌₁, project the 2-blade **X** = (**e**₁ + **e**₂) ∧ (**e**₃ + **e**₄) onto the 2-blade **A** = (**e**₁ ∧ **e**₃). Then determine the rejection as the difference of **X** and its projection. Show that this is not a blade. (See also structural exercise 5 of Chapter 2.)

10. Let an orthonormal coordinate system {**e**ᵢ}³ᵢ₌₁ be given in 3-D Euclidean space ℝ³'⁰. Compute the support vector (i.e., the vector of the point on the line closest to the origin) of the line with direction **u** = **e**₁ + 2**e**₂ − **e**₃, through the point **p** = **e**₁ − 3**e**₂. What is the distance of the line to the origin?

---

## 6.7 Programming Examples and Exercises

### 6.7.1 Exercise: Subspace Products Retrieved

The geometric product is the fundamental product of geometric algebra. Other products are derived from it. In these exercises, we follow Section 6.3 and implement two different ways of retrieving the left contraction and the outer product from the geometric product.

#### Exercise 1a: The Symmetry Approach (for Vectors Only)

Implement the outer product of a vector and any multivector using (6.10):

$$\mathbf{a} \wedge \mathbf{B} = \frac{1}{2}(\mathbf{a}\,\mathbf{B} + \widehat{\mathbf{B}}\,\mathbf{a})$$

Implement the left contraction of a vector and any multivector using (6.12):

$$\mathbf{a} \rfloor \mathbf{B} = \frac{1}{2}(\mathbf{a}\,\mathbf{B} - \widehat{\mathbf{B}}\,\mathbf{a})$$

The downloadable example code provides a bare-bones framework for doing this. You should complete the following functions:

```cpp
// exercise 1a: complete in this function
mv outerProduct_1a(const e3ga::vector &a, const mv &B) {
    printf("Warning: outerProduct_1a() not implemented yet!\n");
    return 0.0f;
}

// exercise 1a: complete in this function
mv leftContraction_1a(const e3ga::vector &a, const mv &B) {
    printf("Warning: leftContraction_1a() not implemented yet!\n");
    return 0.0f;
}
```

After you have completed the functions, compile and run the example. The testing code will complain if you made a mistake in the implementation. You may need the following functions:

- `gradeInvolution(const mv &X)` computes the grade involution of a multivector.
- `gp(const mv &X, const mv &Y)` computes the geometric product of two multivectors. The `*` operator is bound to it, see Table 2.4.

#### Exercise 1b: The Grade Approach

Equations (6.19) and (6.20) provide another way to obtain the outer product and the left contraction, respectively:

$$A_k \wedge B_l \equiv \langle A_k\,B_l \rangle_{k+l}$$

$$A_k \rfloor B_l \equiv \langle A_k\,B_l \rangle_{l-k}$$

Implement this by filling in `outerProduct_1b()` and `leftContraction_1b()` in the example code.

```cpp
// exercise 1b: complete in this function
mv outerProduct_1b(const mv &A, const mv &B) {
    printf("Warning: outerProduct_1b() not implemented yet!\n");
    return 0.0f;
}

// exercise 1b: complete in this function
mv leftContraction_1b(const mv &A, const mv &B) {
    printf("Warning: leftContraction_1b() not implemented yet!\n");
    return 0.0f;
}
```

You may need the following functions:

- `takeGrade(const mv &X, int gradeUsageBitmap)` extracts grade parts from multivector. The `gradeUsageBitmap` is a bitwise or of the constants `GRADE_0`, `GRADE_1`, `GRADE_2`, and `GRADE_3`, which have values 1, 2, 4, 8, respectively. So, to extract grade k, you can also use `takeGrade(X, 1 << k)`. In the context of integers, the `<<` operator means bitwise shift left, of course.

- If you want to know whether a grade part is present in a multivector variable `X`, you can use `((X.gu() & GRADE_k) != 0)`, where k is the grade part index. For example `((X.gu() & GRADE_2) != 0)` is true when the bivector grade part is present in `X`.

### 6.7.2 Gram-Schmidt Orthogonalization

Geometric algebra does not require the representation of its elements in terms of a particular basis of vectors. Therefore, the specific treatment of issues like orthogonalization are much less necessary. Yet it is sometimes convenient to have an orthogonal basis, and such a basis is simple to construct using our products. We saw a first glimpse of this in the example of Section 3.11.1, using the contraction. Now that we have the geometric product we can give a more general and more complete treatment of orthogonalization.

Suppose we have a set of three vectors **v**₁, **v**₂, **v**₃ in a Euclidean space, as in Figure 6.5(a), and would like to form them into an orthogonal basis. The perpendicularized frame will have its vectors denoted as **b**₁, **b**₂, **b**₃; we arbitrarily keep **v**₁ as the first of those (Figure 6.5(b)):

$$\mathbf{b}_1 \equiv \mathbf{v}_1$$

Then we form the rejection of **v**₂ by **v**₁, which is automatically perpendicular to **v**₁, by forming **v**₂ ∧ **b**₁ (Figure 6.5(c)) and dividing out **b**₁ to orthogonalize it (Figure 6.5(d)):

$$\mathbf{b}_2 \equiv (\mathbf{v}_2 \wedge \mathbf{b}_1)/\mathbf{b}_1$$

That is our second vector of the frame. Now we take the rejection of **v**₃ by **b**₁ ∧ **b**₂, which is perpendicular to both **b**₁ and **b**₂. Graphically, this is done by forming the trivector **v**₃ ∧ **b**₁ ∧ **b**₂ (Figure 6.5(e)), and straightening it by dividing it by **b**₁ ∧ **b**₂ (Figure 6.5(f)). Algebraically, **b**₃ is:

$$\mathbf{b}_3 \equiv (\mathbf{v}_3 \wedge \mathbf{b}_1 \wedge \mathbf{b}_2)/(\mathbf{b}_1 \wedge \mathbf{b}_2)$$

and we are done. This is the Gram-Schmidt orthogonalization procedure, rewritten in geometric algebra.

> **Figure 6.5:** Gram-Schmidt orthogonalization as repeated rejections (see text).

Figure 6.6 gives code listing for orthogonalizing an n-dimensional basis. Note that we view the selection of the first vector as a (rather trivial) rejection to produce clean code. Also note that the function throws a `std::string` when it detects a null blade. The rest of the example is identical to that of Section 3.11.1.

```cpp
/**
 * Uses GA to perform Gram-Schmidt orthogonalization.
 * Throws std::string when input vectors 'vIn' are dependent.
 * Results are returned in 'vOut'.
 */
void GramSchmidtGA(const e3ga::vector vIn[], e3ga::vector vOut[], int nbVectors) {
    mv B = 1;
    for (int i = 0; i < nbVectors; i++) {
        mv newB = vIn[i] ^ B;
        
        // check for dependence of input vectors:
        if (_Float(norm_r2(newB)) == 0.0f)
            throw std::string("input vectors are dependent");
        
        // compute orthogonal vector 'i':
        vOut[i] = _vector(newB * inverse(B));
        
        B = newB;
    }
}
```

> **Figure 6.6:** Gram-Schmidt orthogonalization code (Example 2).

The result of the Gram-Schmidt orthogonalization implies that vectors spanning a subspace can be orthogonalized if they are invertible. This has consequences for the blade representing that subspace, for using the new basis we can write it as a geometric product of vectors **b**₁ **b**₂ ⋯ **b**ₖ rather than as an outer product of vectors **v**₁ ∧ **v**₂ ∧ ⋯ ∧ **v**ₖ. This is often useful in algebraic manipulation inside proofs, since the geometric product has richer algebraic properties; for instance, it is invertible, whereas the outer product is not. Since orthogonal vectors anticommute, we have: **an invertible blade can be written as a geometric product of anticommuting vectors.**

In non-Euclidean metrics, null vectors and null blades occur and those are noninvertible. This implies we cannot use the division the orthogonalization algorithm requires. Yet even in such a space, a blade can be written as a geometric product of anticommuting vectors; we just have to compute them in a different manner. We recommend the method described in Section 19.4 as the numerically stable way of finding these anticommuting vectors. The method amounts to computing the metric matrix of the blade and computing its eigenvalue decomposition; the eigenvectors are then used to compute the anticommuting vectors that span the blade.

---

## Footnotes

¹ Note that the inverse for the geometric product is the same we used as "an" inverse for the inner product in Section 3.5.2; it was then not unique, but we conveniently picked one that would be useful in the wider context that we have now reached.
