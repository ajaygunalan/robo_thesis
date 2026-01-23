# Chapter 19: Basis Blades and Operations

All geometric algebra implementations that represent multivectors as a weighted sum of basis blades will, at some point, have to compute products of basis blades. Among the various products, the capability to compute the geometric product (also for non-Euclidean metrics) is clearly the minimum requirement, as the outer product and various flavors of the inner products can be derived from it using the (anti-)symmetry or grade selection techniques of Chapter 6.

This chapter describes how to implement this geometric product of basis blades through a convenient representation of basis blades. The algorithms described are quite simple, yet intricate enough that we need (pseudo)code to describe them precisely. Instead of introducing our own pseudocode language, we opted to simply use Java. The code in this chapter therefore corresponds well to our reference implementation at our web site http://www.geometricalgebra.net, although it was sometimes slightly polished for presentation.

Conceptually, our basis blades representation uses a list of booleans and applies Boolean logic to the elements of that list. But in practice, the list of booleans is implemented using bitmaps and the bitwise boolean operators. To correspond more directly to the actual implementation, that is how we present the representation and its operators in this chapter.

---

## 19.1 Representing Unit Basis Blades with Bitmaps

When we want to represent the geometric algebra of an $n$-dimensional space, we start with a set of $n$ independent basis vectors $\{\mathbf{e}_i\}_{i=1}^{n}$. They need not be orthonormal or even orthogonal; the geometric product of the space will essentially define their relevant geometrical relationships. A *basis blade* is a nonzero outer product of a number of these basis vectors (or a unit scalar). Hence, a basis blade either contains a specific basis vector or not.

Thus, each basis blade in an algebra can be represented by a list of boolean values, where each boolean indicates the presence or absence of a basis vector. The list of booleans is naturally implemented using a bitmap, which is why we call this the **bitmap representation** of basis blades.

The bits in the bitmap are assigned in the logical order: bit 0 stands for $\mathbf{e}_1$, bit 1 stands for $\mathbf{e}_2$, bit 2 stands for $\mathbf{e}_3$, and so on. Table 19.1 shows how this works out. The unit scalar does not contain any basis vectors, so it is represented by $0_b$ (in this chapter, the postfix, subscript $b$ indicates a binary number). A blade such as $\mathbf{e}_1 \wedge \mathbf{e}_3$ contains $\mathbf{e}_1$ and $\mathbf{e}_3$, so it is represented by $001_b + 100_b = 101_b$.

Visually, the bits are stored in reversed order relative to how we would write them as basis blades. In a basis blade, $\mathbf{e}_1$ is the left-most basis vector, while in bitmap representation it is the right-most bit. While this is slightly inconvenient for reasoning about them, it is more consistent for implementation. If an extra dimension is required, the next most significant bit in the bitmap is used and previous results are automatically absorbed.

**Table 19.1:** The bitmap representation of basis blades. Note how the representation scales up with the dimension of the algebra.

| Basis Blade | Bitmap Representation |
|-------------|----------------------|
| $1$ | $0_b$ |
| $\mathbf{e}_1$ | $1_b$ |
| $\mathbf{e}_2$ | $10_b$ |
| $\mathbf{e}_1 \wedge \mathbf{e}_2$ | $11_b$ |
| $\mathbf{e}_3$ | $100_b$ |
| $\mathbf{e}_1 \wedge \mathbf{e}_3$ | $101_b$ |
| $\mathbf{e}_2 \wedge \mathbf{e}_3$ | $110_b$ |
| $\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3$ | $111_b$ |
| $\mathbf{e}_4$ | $1000_b$ |
| ... | ... |

**Table 19.2:** Bitwise boolean operators used in Java code examples.

| Symbol | Operation |
|--------|-----------|
| `&` | Bitwise boolean "and" |
| `^` | Bitwise boolean "exclusive or" |
| `>>>` | Unsigned bitwise "shift right" |

In our reference implementation, we use 32-bit integers as our bitmaps. This allows us to represent all basis blades of the geometric algebra of a 32-D space. This should be more than enough for practical usage in computer science applications. Further, this basis-of-blades method of implementing geometric algebra is only practical up to around 10-D spaces, since the number of basis blades required to represent an arbitrary multivector grows quickly, as $2^n$. The products have to process combinations of all basis blades from both arguments, so you typically will run out of processing time before you run out of memory. But should you ever need more than 32 dimensions, extending the range of the bitmaps is straightforward.

The reference implementation stores basis blades in a class named `BasisBlade`. The class has only two member variables, `bitmap` (an integer) and `scale` (a floating point number). `scale` allows the basis blade to have an arbitrary sign or scale; this is what we called the *weight* in Part I. The name `ScaledBasisBlade` might have been a more accurate class description, but we found that a bit too verbose.

In Table 19.2, we show the symbols used for the bitwise boolean operations. These symbols are identical to the ones Java uses. Note that in code listings, $\wedge$ may appear as `^`.

---

## 19.2 The Outer Product of Basis Blades

We now show how to compute the products on the basis blades using the bitmap representation. To compute the outer product of two basis blades, we first check whether they are dependent (i.e., whether the two blades have a common basis vector factor). If they do, they have a bit in common, so dependence of blades is checked simply with a binary *and*. If the blades are dependent, then the outcome of the outer product is 0 and the algorithm described below does not need to be executed.

If the blades are independent, computing their outer product is done (up to a scale factor) by taking the bitwise *exclusive or* of the bitmaps. For example,

$$(\mathbf{e}_2 \wedge \mathbf{e}_3) \wedge \mathbf{e}_1 = \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3$$

is equivalent to

$$110_b \wedge 001_b = 111_b.$$

The hardest part in implementing the outer product is computing the correct sign for the result. The bitmap representation assumes that the basis vectors are in canonical order (e.g., using just the bitmap you cannot represent $\mathbf{e}_3 \wedge \mathbf{e}_1$, only $\mathbf{e}_1 \wedge \mathbf{e}_3$). We should employ the `scale` member variable to represent $\mathbf{e}_3 \wedge \mathbf{e}_1$ as $-1.0 * (\mathbf{e}_1 \wedge \mathbf{e}_3)$.

When you compute the sign of the outer product result by hand, you count how many basis vectors have to swap positions to get the result into the canonical order. Each swap of position causes a flip of sign. In our example, all that is required is that $\mathbf{e}_3$ and $\mathbf{e}_1$ swap positions, so we get a negative sign.

To compute this sign algorithmically, we have to compute, for each 1-bit in the first operand, the number of less significant 1-bits in the second operand. This is implemented somewhat like a convolution, in that the bitmaps are slid over each other bit by bit. For each position, the number of matching 1-bits counted. Figure 19.1 shows the implementation of this idea (the `bitCount()` function counts the number of nonzero bits in a word). The implementation of the outer product itself is in Figure 19.2; this function actually also implements the geometric product, as described in the next section.

**Figure 19.1:** This function computes the sign change due to the reordering of two basis blades into canonical order.

```java
// Arguments 'a' and 'b' are both bitmaps representing
// basis blades.
double canonicalReorderingSign(int a, int b) {
    // Count the number of basis vector swaps required to
    // get 'a' and 'b' into canonical order.
    a = a >>> 1;
    int sum = 0;
    while (a != 0) {
        // the function bitCount() counts the number of
        // 1-bits in the argument
        sum = sum + subspace.util.Bits.bitCount(a & b);
        a = a >>> 1;
    }
    // even number of swaps -> return 1
    // odd number of swaps -> return -1
    return ((sum & 1) == 0) ? 1.0 : -1.0;
}
```

**Figure 19.2:** This function will compute either the geometric product (in Euclidean metric only) or the outer product, depending on the value of argument `outer`.

```java
BasisBlade gp_op(BasisBlade a, BasisBlade b, boolean outer) {
    // if outer product: check for independence
    if (outer && ((a.bitmap & b.bitmap) != 0))
        return new BasisBlade(0.0);

    // compute the bitmap:
    int bitmap = a.bitmap ^ b.bitmap;

    // compute the sign change due to reordering:
    double sign = canonicalReorderingSign(a.bitmap, b.bitmap);

    // return result:
    return new BasisBlade(bitmap, sign * a.scale * b.scale);
}
```

---

## 19.3 The Geometric Product of Basis Blades in an Orthogonal Metric

The implementation of the geometric product is similar to that of the outer product as long as we stay in an *orthogonal metric* with respect to the orthonormal basis $\{\mathbf{e}_i\}_{i=1}^{n}$. Such a metric has $\mathbf{e}_i \cdot \mathbf{e}_j = 0$ for $i \neq j$, and $\mathbf{e}_i \cdot \mathbf{e}_i = m_i$; therefore, its *metric matrix* is diagonal:

$$\mathbf{e}_i \cdot \mathbf{e}_j = m_i \delta^i_j, \tag{19.1}$$

where $\delta^i_j$ is the *Kronecker delta function*, returning 1 when $i$ equals $j$, and zero otherwise. A particular example is the Euclidean metric, for which $m_i = 1$ for all $i$, so that the metric matrix is the identity matrix. In general, the $m_i$ can have any real value, but $-1$, $0$, and $1$ will be the most prevalent in many applications.

There are now two cases:

- For blades consisting of *different* orthogonal factors, we have the usual equivalence of the outer product and the geometric product:

$$\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \cdots \wedge \mathbf{e}_k = \mathbf{e}_1 \mathbf{e}_2 \cdots \mathbf{e}_k.$$

- However, when two factors are in common between the multiplicands, the outer product produces a zero result, but the geometric product does not. Instead, it annihilates the dependent-basis vectors, effectively replacing them by metric factors. For example,

$$(\mathbf{e}_1 \wedge \mathbf{e}_2)(\mathbf{e}_2 \wedge \mathbf{e}_3) = m_2 \mathbf{e}_1 \wedge \mathbf{e}_3.$$

In the bitmap representation, these two cases are easily merged. Both results may be computed as the bitwise exclusive or operation (i.e., $011_b \wedge 110_b = 101_b$). In this sense, the geometric product acts as a "spatial exclusive or" on basic blades.

As for the outer product, the result of the geometric product "exclusive or" should be given the correct sign to distinguish between the outcomes $\mathbf{e}_1 \wedge \mathbf{e}_3$ and $\mathbf{e}_3 \wedge \mathbf{e}_1$. We therefore also have to perform reordering techniques to establish the sign of the result on the standard basis. Those sign changes are identical to those for the outer product: we count the number of basis vector swaps required to get the result into canonical order and use this to determine the sign.

In a Euclidean metric, all diagonal metric factors are 1, so this bit pattern and sign computation is all there is to the geometric product. The function that computes the geometric product in this simple Euclidean case is therefore virtually the same as the function for computing the outer product (see Figure 19.2), the only difference being the dependence check required for the outer product. That close and convenient similarity is due to the use of the orthonormal basis in the representation.

When the metric is not Euclidean but still diagonal, we need to incorporate the metric coefficients of the annihilated basis vectors into the scale of the resulting blade. Which basis vectors are annihilated is determined with a bitwise *and*. We do not show the resulting code, which simply invokes the Euclidean code with this extension; you can consult the reference implementation on our web site for the details.

---

## 19.4 The Geometric Product of Basis Blades in Nonorthogonal Metrics

In practical geometric algebra we naturally encounter nonorthonormal bases. For example, in the conformal model we may want to represent $o$ and $\infty$ directly as basis vectors. This leads to a nondiagonal multiplication table (and therefore nondiagonal metric matrix):

|   | $o$ | $\mathbf{e}_1$ | $\mathbf{e}_2$ | $\mathbf{e}_3$ | $\infty$ |
|---|-----|----------------|----------------|----------------|----------|
| $o$ | 0 | 0 | 0 | 0 | $-1$ |
| $\mathbf{e}_1$ | 0 | 1 | 0 | 0 | 0 |
| $\mathbf{e}_2$ | 0 | 0 | 1 | 0 | 0 |
| $\mathbf{e}_3$ | 0 | 0 | 0 | 1 | 0 |
| $\infty$ | $-1$ | 0 | 0 | 0 | 0 |

The orthogonal metric method of the previous section does not seem to apply to this case. Yet the methods employed for the orthogonal metrics are more general than they seem. By the spectral theorem from linear algebra (a matrix is orthogonally diagonalizable if and only if it is symmetric), an arbitrary metric matrix can always be brought into diagonal form by an appropriate coordinate transformation to an orthonormal basis.

Therefore we can compute geometric products in the conformal model by temporarily switching to a new basis that is orthonormal. Such a basis is computed by finding the eigenvalue decomposition of the metric matrix. For our conformal model example, such a basis would be

$$\mathbf{f}_1 = \mathbf{e}_1$$

$$\mathbf{f}_2 = \mathbf{e}_2$$

$$\mathbf{f}_3 = \mathbf{e}_3$$

$$\mathbf{f}_4 = \frac{1}{2}\sqrt{2}(o - \infty)$$

$$\mathbf{f}_5 = \frac{1}{2}\sqrt{2}(o + \infty).$$

The $\mathbf{f}_i$ are all basis vectors with $\mathbf{f}_i \cdot \mathbf{f}_i = 1$, except for $\mathbf{f}_5 \cdot \mathbf{f}_5 = -1$. (Alternatively, we could use $\mathbf{f}_4 = e = o - \infty/2$ and $\mathbf{f}_5 = \bar{e} = o + \infty/2$, as in (13.6).) The new basis is therefore one of the orthogonal metrics of the previous section, and we can revert to the previous methods. So, to compute the geometric product in an arbitrary metric:

1. Compute the eigenvectors and eigenvalues of the metric matrix. This has to be done once, when the object that represents the metric is initialized.

2. Apply a change-of-basis to the input such that it is represented with respect to the eigenbasis.

3. Compute the geometric product on this new orthogonal basis (the eigenvalues specify the metric).

4. Apply another change of basis to the result, to get back to the original basis.

In practical implementations, the computation of the geometric product of the basis blades is done beforehand, so this way of implementing it does not slow down the application at run-time. The code for this algorithm is rather involved, so we do not show the implementation here. If you are interested, you can find it in the `subspace.basis` package at http://www.geometricalgebra.net.

One detail to note is that the result of a geometric product is not always a single basis blade anymore. When switching back and forth between one basis and another, a single basis blade can convert into a sum of multiple basis blades. This is in agreement with what one would expect. An example is easily given: in the conformal model, $o \infty = -1 + o \wedge \infty$.

---

## 19.5 The Metric Products of Basis Blades

We use the term *metric product* collectively to denote the scalar product, left and right contraction, and the inner products used by others and exposed in Appendix B. From the algorithmic viewpoint, they are all similar, for they can all be derived from the geometric product by extracting the appropriate grade parts of the result (the same could be done for the outer product, if you wish).

Let $\mathbf{A}$ and $\mathbf{B}$ be two basis blades of grade $a$ and $b$, respectively. Then the rules for deriving a particular metric product from the geometric product of two basis blades are:

- **Left contraction.** If $a \leq b$, $\mathbf{A} \rfloor \mathbf{B} = \langle \mathbf{A} \mathbf{B} \rangle_{b-a}$, otherwise 0.

- **Right contraction.** If $a \geq b$, $\mathbf{A} \lfloor \mathbf{B} = \langle \mathbf{A} \mathbf{B} \rangle_{a-b}$, otherwise 0.

- **Dot product:** If $a \leq b$, then the dot product is equal to the left contraction. Otherwise, it is equal to the right contraction.

- **Hestenes metric product.** Like the dot product, but 0 when either $\mathbf{A}$ or $\mathbf{B}$ is a scalar.

- **Scalar product.** $\mathbf{A} * \mathbf{B} = \langle \mathbf{A} \mathbf{B} \rangle_0$.

The grade of a basis blade is determined simply by counting the number of 1-bits in the bitmap. The reference implementation can therefore implement the inner products exactly as defined. For example, to compute the left contraction of a grade-1 blade and a grade-3 blade, it extracts the grade $3 - 1 = 2$ part from their geometric product.

If one were to write a dedicated version of the metric product implementation, an optimization would be to check whether one lower-grade basis blade is fully contained in the higher-grade basis blade before performing the actual product. If this condition is not satisfied, the metric product (of whatever flavor) will always be 0. This containment is tested by checking whether all set bits in the lower-grade blade are also set in the higher-grade blade. For nonorthogonal metrics, this check should be done after the change to the eigenbasis.

---

## 19.6 Commutator Product of Basis Blades

The commutator product of basis blades is easily derived from the geometric product using the following equation from Section 8.2.1:

$$\mathbf{A} \times \mathbf{B} \equiv \frac{1}{2}(\mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A}).$$

---

## 19.7 Grade-Dependent Signs on Basis Blades

Implementing the reversion, grade involution (Section 2.9.5), and Clifford conjugation (structural exercise 8, Section 2.12.2) is straightforward for basis blades. These grade-dependent sign operators toggle the sign of basis blades according to a specific multiplier based on the grade $a$ of the blade (see Table 19.3).

**Table 19.3:** Reversion, grade involution, and Clifford conjugate for basis blades.

| Operation | Multiplier for Grade $a$ | Pattern |
|-----------|--------------------------|---------|
| Reversion | $(-1)^{a(a-1)/2}$ | $+ + - - + + - -$ |
| Grade involution | $(-1)^a$ | $+ - + - + - + -$ |
| Clifford conjugation | $(-1)^{a(a+1)/2}$ | $+ - - + + - - +$ |

As an example, the reverse of $\mathbf{e}_1 \wedge \mathbf{e}_2$ is computed by first determining the grade (which is 2) and then applying the correct multiplier (in this case $(-1)^{2(2+1)/2} = -1$) to the `scale` of the blade.

The last column of Table 19.3 shows the repetitive pattern over the varying grades that describes the behavior of each operation: "$-$" stands for multiplication by $-1$, while "$+$" stands for multiplication by $+1$. It shows, for instance, that the grade involution toggles the sign of all odd-grade parts while it leaves the even grade parts unchanged.
