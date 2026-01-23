# Chapter 21: Fundamental Algorithms for Nonlinear Products

In the previous chapter, we looked at how to implement the *linear* products in geometric algebra. The linearity of these products allowed us to implement them using linear algebra or through a simple double loop. However, there are other operations in geometric algebra that are *nonlinear* (such as inverse, `meet`, `join`, and factorization). These cannot be implemented in the same way.

In this chapter, we discuss the implementation of such nonlinear geometric algebra operations. The nonlinearity results in more complex algorithms, still reasonably efficient but typically an order of magnitude more time-consuming than linear operations.

We give algorithms for the inverse, for exponentiation, for testing whether a multivector is a blade or a versor, for blade factorization, and for the efficient computation of `meet` and `join`.

---

## 21.1 Inverse of Versors (and Blades)

We need to compute the inverse of the elements we construct in geometric algebra. Those are almost exclusively blades or versors (the only exceptions were the bivectors in an exponent, and we have no need to invert those). Invertible blades are always versors, since a $k$-blade (the outer product of $k$ vectors) can always be written as the geometric product of $k$ vectors (i.e., a $k$-versor); see Section 6.4.1. So if we can invert a versor $V$, we can also invert blades and thus most of the elements we construct.

There is a very efficient way to invert versors, which we call the *versor inverse* method (because, in general, it works only on versors). This inversion is almost trivial. It starts with the observation that the quantity $V\tilde{V}$ is always scalar for any versor $V$. This is easily seen by factorizing the versor:

$$V\tilde{V} = (\mathbf{v}_k \cdots \mathbf{v}_2 \mathbf{v}_1)(\mathbf{v}_1 \mathbf{v}_2 \cdots \mathbf{v}_k) = (\mathbf{v}_k \cdots (\mathbf{v}_2 (\mathbf{v}_1 \mathbf{v}_1) \mathbf{v}_2) \cdots \mathbf{v}_k) = \mathbf{v}_k^2 \cdots \mathbf{v}_2^2 \mathbf{v}_1^2.$$

The inverse of the versor is then simply

$$V^{-1} = \tilde{V}/(V\tilde{V}). \tag{21.1}$$

This method would fail if $V\tilde{V} = 0$. But in that case (which may occur when one of the vector factors is a null vector), the multivector $V$ is actually not a versor (since all versors are invertible by definition). $V$ is then not actually a versor since versors are always invertible.

---

## 21.2 Inverse of Multivectors

As long as you stay within the bounds of geometric algebra (as opposed to Clifford algebra; see Section 7.7.2 for our take on the difference), the versor inverse method should cover all of your inversion needs. But should the need arise to invert a general multivector, you can use the following technique to invert *any* invertible multivector. It is based on the linear algebra implementation approach described in Section 20.1. Since

$$A B \rightleftharpoons [\![A^G]\!][\![B]\!],$$

it follows that

$$A^{-1} B \rightleftharpoons [\![A^G]\!]^{-1}[\![B]\!]$$

(just left-multiply both sides by $A$ and $[\![A^G]\!]$). So the matrix of the inverse of $A$ is the inverse of the matrix of $A$. This insight can be used to invert any multivector $A$ as long as the matrix $[\![A^G]\!]$ is invertible, using the following steps:

- Compute the geometric product matrix $[\![A^G]\!]$;
- Invert this matrix;
- Extract $[\![A^{-1}]\!]$ as the first column of $[\![A^G]\!]^{-1}$.

To understand why the last step is correct, inspect the algorithm for computing the geometric product matrix. With the scalar 1 as the first element of $\mathbb{L}$, the first column of the matrix $[\![A^G]\!]$ is constructed from the geometric product of $A$ with the first element of $\mathbb{L}$, which is 1. Therefore the first column of a geometric product matrix $[\![A^G]\!]$ is $[\![A]\!]$ itself (this may also be observed in Figure 20.1). Hence we find the coefficients of $A^{-1}$ as the first column of $[\![(A^{-1})^G]\!] = [\![A^G]\!]^{-1}$.

This inversion method has two main disadvantages: it is both slow and numerically imprecise due to floating point round-off errors. Therefore, you should not use it to invert a blade or a versor—use the method of Section 21.1 for those.

---

## 21.3 Exponential, Sine, and Cosine of Multivectors

The exponential and trigonometric functions were introduced for blades in Section 7.4.2. For easy reference, we repeat the equations for the polynomial expansion of the exponential:

$$\exp(\mathbf{A}) = 1 + \frac{\mathbf{A}}{1!} + \frac{\mathbf{A}^2}{2!} + \cdots$$

If the square of $\mathbf{A}$ is a scalar, this series can be easily computed using standard trigonometric or hyperbolic functions:

$$\exp(\mathbf{A}) = \begin{cases} \cos \alpha + \mathbf{A} \frac{\sin \alpha}{\alpha} & \text{if } \mathbf{A}^2 = -\alpha^2 \\ 1 + \mathbf{A} & \text{if } \mathbf{A}^2 = 0 \\ \cosh \alpha + \mathbf{A} \frac{\sinh \alpha}{\alpha} & \text{if } \mathbf{A}^2 = \alpha^2 \end{cases},$$

where $\alpha$ is a real scalar. Since both a versor and a blade have scalar squares, their exponentials are easy to compute by directly applying these formulas.

Unfortunately, we will need to take exponentials of nonblade elements. The exponentials of general bivectors generate the continuous motions in a geometry, and only in fewer than four dimensions are bivectors always 2-blades. In the important conformal model, rigid body motions are exponentials of bivectors that are not 2-blades, as we saw in Section 13.5. So we need techniques to process them.

When the special cases do not apply, the series for the exponential can be evaluated explicitly up to a certain order. This tends to be slower and less precise. Experience shows that evaluating the polynomial series up to order 10 to 12 gives the best results for 64 bit doubles. For the exponential, a rescaling technique is possible that will increase accuracy, as follows.

Suppose you want to compute $\exp(\mathbf{A})$. If $\mathbf{A}$ is a lot larger than unity, $\mathbf{A}^k$ can be so large that the series overflows the accuracy of the floating-point representation before it converges. To prevent this problem, we can scale $\mathbf{A}$ to near unity before evaluating the series, because of the identity

$$\exp(\mathbf{A}) = \left(\exp\left(\frac{\mathbf{A}}{s}\right)\right)^s.$$

For our purposes, any $s \approx \|\mathbf{A}\|$ will do. In a practical implementation, we choose $s$ to be a power of two, so that we can efficiently compute $\left(\exp \frac{\mathbf{A}}{s}\right)^s$ by repeatedly squaring $\exp\left(\frac{\mathbf{A}}{s}\right)$.

---

## 21.4 Logarithm of Versors

We do not know of a general algorithm for computing the logarithm of arbitrary versors. However, for many useful cases a closed-form solution was found; see, for example, Section 10.3.3 (rotation), Section 13.5.3 (rigid body motion), and Section 16.3.4 (positively scaled rigid body motion). We have not yet included these logarithms in our reference implementation, but you can find a C++ implementation of these logarithms in the GA sandbox source code package.

---

## 21.5 Multivector Classification

At times, it may be useful to have an algorithm that classifies a multivector as either a blade, a versor, or a nonversor. For instance, classification is useful as a sanity check of interactive input, or to verify whether and how a result could be displayed geometrically.

Yet testing whether a multivector is a versor or a blade is nontrivial in our additive representation. A blade test requiring that the multivector is of a single grade is insufficient (for example, $\mathbf{e}_1 \wedge \mathbf{e}_2 + \mathbf{e}_3 \wedge \mathbf{e}_4$ is of uniform grade 2, but not a blade). Adding the rule that the square of the multivector must be a scalar does not help (since $\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3 + \mathbf{e}_4 \wedge \mathbf{e}_5 \wedge \mathbf{e}_6$ squares to $-2$ in a Euclidean metric, but it is not a blade).

The classification algorithm below (from [7]) performs this test correctly. It is one algorithm that can be used either for the versor test or for the blade test. It is natural that these tests should structurally be very similar, for all invertible blades are also versors. As you glance through it, you notice that the algorithm uses inverses. This is fine for a versor test, since versors need to be invertible by definition. However, a blade need not be invertible, and yet null blades are still blades.

In fact, "being a blade" is defined as "factorizable by the outer product", and that does not depend on a metric at all. Our reference [7] makes good use of this freedom: if you are testing whether $V$ is a blade, you must perform the geometric products in the algorithm using a Euclidean metric. This choice of convenience eliminates all null blades that would have had to be taken into account without actually affecting factorizability, and that simplifies the algorithm. (As an example, the multivector $\mathbf{e}_1 \wedge \infty$ is a blade, but in the conformal metric contains a null factor $\infty$. This makes the blade noninvertible, but it is of course still a blade. By using a Euclidean metric, $\infty$ is treated as a regular vector, the blade becomes invertible, and the test can run as it would for $\mathbf{e}_1 \wedge \mathbf{e}_2$).

On the other hand, determining whether a multivector $V$ is a versor (i.e., a geometric product of invertible vectors) clearly depends on the precise properties of the metric. So for a versor test, you have to run this algorithm in the actual metric of the algebra of the versor.

### The Classification Process

The classification process for $V$ consists of three parts:

1. **Test if the versor inverse $\tilde{V}/(V\tilde{V})$ is truly the inverse of the multivector $V$.** This involves the following tests:

   $$\text{grade}(\hat{V} V^{-1}) \stackrel{?}{=} 0,$$

   $$\hat{V} V^{-1} \stackrel{?}{=} V^{-1} \hat{V}.$$

   If either of these tests fails, we can report that the multivector is a nonversor, and hence a nonblade.

   The use of grade involution in the two equations above is an effective trick from [9]. It prevents multivectors that have both odd and even grade parts from sneaking through the test. If $V$ is an even versor, then $\hat{V} = V$. If $V$ is an odd versor, $\hat{V} = -V$. But if $V$ has both odd and even grade parts, the grade involution prevents odd and even parts from recombining in such a way that they cancel each other out. See structural exercise 21.8 for an illuminating example.

2. **The second test is on the grade preservation properties of the versor:** applying a versor (and hence an invertible blade) to a vector should not change the grade. So for each basis vector $\mathbf{e}_i$ of the vector space $\mathbb{R}^n$, the following should hold if $V$ is a versor:

   $$\text{grade}(\hat{V} \mathbf{e}_i \tilde{V}) \stackrel{?}{=} 1.$$

   When the multivector does not pass this test, we report a nonversor (and hence a nonblade); otherwise we know that it is either a versor or a blade.

3. **The final part makes the distinction between blades and versors** by simply checking whether the multivector is of a single grade. If so, it is a blade; otherwise it is a versor.

Unfortunately, we currently have no general solution to the problem of determining the type of multivectors that are not quite blades or not quite versors in a numerically informed manner. We would like to correct any numerical drift in these fundamental properties due to repeated floating point round-off errors, but we do not know how to make versors or blades out of almost-versors and almost-blades in an optimal way in general metrics.

---

## 21.6 Blade Factorization

This section deals with generic *factorization of blades*. That is the problem to find, for a given blade $\mathbf{B}$ of grade $k$, a set of $k$ vectors $\mathbf{b}_i$ such that

$$\mathbf{B} = \mathbf{b}_1 \wedge \mathbf{b}_2 \wedge \cdots \mathbf{b}_k.$$

You may want to factorize a blade because you want to use it as input to libraries that cannot handle blades (such as standard libraries for linear algebra or computer graphics), so that you are required to process their vector factors separately. Or you may need a factorization to implement another low-level algorithm such as the computation of `meet` and `join` below.

We are only concerned with the outer product and consequently (as in the previous section) are allowed to choose any convenient metric. To avoid any problems with null vectors, we use the Euclidean metric for all metric products in the algorithm that follows.

### Finding Potential Factors

A first step towards a useful factorization algorithm is finding potential factors of a blade $\mathbf{B}$. This can be done using projection. Take any candidate vector $\mathbf{c}$ (for example, a basis vector), and project it onto $\mathbf{B}$:

$$\mathbf{f} = (\mathbf{c} \rfloor \mathbf{B}) \mathbf{B}^{-1}.$$

If $\mathbf{f}$ is 0, then another candidate vector should be tried. For better numerical stability, we should also try another candidate when $\mathbf{f}$ is close to 0 (or better yet, try many different candidate vectors and use the one that results in the largest $\mathbf{f}$). In any case, when $\mathbf{f}$ is a usable factor we can remove it from $\mathbf{B}$ simply by dividing it out:

$$\mathbf{B}_f = \mathbf{f}^{-1} \rfloor \mathbf{B}. \tag{21.2}$$

Then we can write (see structural exercise 2)

$$\mathbf{B} = \mathbf{f} \wedge \mathbf{B}_f,$$

so that we have found our first factor of $\mathbf{B}$. We now repeat this process on the blade $\mathbf{B}_f$, iteratively, until we are left with a final vector factor.[^1]

[^1]: We remove the factor $\mathbf{f}$ from $\mathbf{B}$, because we want the factors to be orthogonal. If you just want factors that make up $\mathbf{B}$ and don't care about orthogonality or scale, you may adjust the algorithm to use the original $\mathbf{B}$ in each loop of the final algorithm below. But you must then make sure that your factors are linearly independent.

### Efficient Factor Selection

This basic idea works, but the procedure may be inefficient in high-dimensional spaces. Many candidate vectors may result in a zero value for $\mathbf{f}$, which is a waste of effort. It is better to use the structure of $\mathbf{B}$ itself to limit the search for its factors in an efficient, stable technique, as follows. The blade $\mathbf{B}$, as given, is represented as coordinates relative to a basis of blades. We take the basis blade with the absolute largest coordinate on this basis. Let that be $\mathbf{E} = \mathbf{e}_{i_1} \wedge \mathbf{e}_{i_2} \wedge \ldots \wedge \mathbf{e}_{i_k}$. We then use the basis vectors that make up $\mathbf{E}$ as candidate vectors for projection. This selection procedure guarantees that the projection of each of the candidate vectors is nonzero (we show this at the end of this section).

One final issue is the scaling of each of the factors. Due to the projection, the factors do not have a predictable scale, which is an awkward property. Our implementation of the factorization algorithm normalizes the factors and returns the scale of the blade as a separate scalar.[^2]

[^2]: Other solutions are to premultiply the first factor with the scale, or to apportion the scale evenly over each factor. Which method is most convenient may partly depend on the subsequent use of the factorization. In any case, the unit factors with a separate scale can be transformed into any of the other representations easily.

### The Factorization Algorithm

The final algorithm [6, 8] for factorizing a blade becomes:

1. **Input:** a nonzero blade $\mathbf{B}$ of grade $k$.
2. Determine the norm of $\mathbf{B}$: $s = \|\mathbf{B}\|$.
3. Find the basis blade $\mathbf{E}$ in the representation of $\mathbf{B}$ with the largest coordinate; determine the $k$ basis vectors $\mathbf{e}_i$ that span $\mathbf{E}$.
4. Let the current input blade be $\mathbf{B}_c \leftarrow \mathbf{B}/s$.
5. For all but one of the basis vectors $\mathbf{e}_i$ of $\mathbf{E}$:
   - (a) Project $\mathbf{e}_i$ onto $\mathbf{B}_c$: $\mathbf{f}_i = (\mathbf{e}_i \rfloor \mathbf{B}_c) \mathbf{B}_c^{-1}$.
   - (b) Normalize $\mathbf{f}_i$. Add it to the list of factors.
   - (c) Update $\mathbf{B}_c$: $\mathbf{B}_c \leftarrow \mathbf{f}_i^{-1} \rfloor \mathbf{B}_c$.
6. Obtain the last factor: $\mathbf{f}_k = \mathbf{B}_c$. Normalize it.
7. **Output:** the factors $\mathbf{f}_i$ and the scale $s$.

### Notes on Metric

Some notes on metric are in order. First, the algorithm also works for null blades, since no blade is actually null in the Euclidean metric that is used during the factorization algorithm itself. Second, the output of the algorithm is a set of orthonormal factors in the Euclidean metric that was used within the algorithm. That may not be the metric of the space of interest. If you desire orthonormality in some other metric, construct the metric matrix of the factors, perform an eigenvalue decomposition, and use this to construct an orthonormal set of factors (see also Section 19.4).

### Why Projections Are Nonzero

To see why the projection of $\mathbf{e}_i$ on $\mathbf{B}_c$ is never zero (step 5a), note that there always exists a rotor $R$ that turns $\mathbf{E}$ to the original $\mathbf{B}$. This rotor will never be over 90 degrees (for that would imply that $\mathbf{E} \rfloor \mathbf{B} = 0$, yet we know that $\mathbf{E} \rfloor \mathbf{B}$ must be nonzero to be the basis blade with the largest coordinate in $\mathbf{B}$). We may not be able to compute the rotation $R$ easily, but we can find $R^2 = R R = \mathbf{B}\mathbf{E}^{-1}$. Since $R$ is never over 90 degrees, $R^2$ will never be over 180 degrees. Because of this, the quantity $\frac{1}{2}(\mathbf{e}_i + R^2 \mathbf{e}_i/R^2)$ must be nonzero: no $\mathbf{e}_i$ is rotated far enough by $R^2$ to become its own opposite. We rewrite this and find:

$$\begin{aligned}
0 &\neq \frac{1}{2}(\mathbf{e}_i + R^2 \mathbf{e}_i/R^2) \\
&= \frac{1}{2}(\mathbf{e}_i + \mathbf{B} \mathbf{E}^{-1} \mathbf{e}_i \mathbf{E} \mathbf{B}^{-1}) \\
&= \frac{1}{2}(\mathbf{e}_i - \mathbf{B} \mathbf{E}^{-1} \hat{\mathbf{E}} \mathbf{e}_i \mathbf{B}^{-1}) \\
&= \frac{1}{2}(\mathbf{e}_i - \hat{\mathbf{B}} \mathbf{e}_i \mathbf{B}^{-1}) \\
&= (\mathbf{e}_i \rfloor \mathbf{B}) \mathbf{B}^{-1}.
\end{aligned}$$

Therefore none of the $\mathbf{e}_i$ from $\mathbf{E}$ projects to zero on $\mathbf{B}$, so $\mathbf{f}_1$ is nonzero in the first pass of the algorithm. After removal of $\mathbf{f}_1$, the same argument can be applied to the next $\mathbf{e}_i$ on $\mathbf{B}_c$, and so on. Hence none of the $\mathbf{f}_i$ are zero.

---

## 21.7 The Meet and Join of Blades

When we introduced the `meet` and `join` of blades in Chapter 5, we saw that they are in some sense the geometrical versions of intersection and union from set theory. We can use this correspondence to compute them. To simplify the description of the algorithm, we first illustrate some of the basic ideas with regular set theory and Venn diagrams and then transfer them to `meet` and `join`.

### Set Theory Analogy

Figure 21.1(a) shows a Venn diagram of two nondisjoint sets $\mathbf{A}$ and $\mathbf{B}$, their union, $\mathbf{A} \cup \mathbf{B}$, and their intersection, $\mathbf{A} \cap \mathbf{B}$. We introduce a symmetric set difference through a *delta product*, defining $\mathbf{A} \triangle \mathbf{B}$ as $\mathbf{A} \cup \mathbf{B}$ minus $\mathbf{A} \cap \mathbf{B}$. This is illustrated in Figure 21.1(d). We also use the complement $(\mathbf{A} \triangle \mathbf{B})^*$ as illustrated in Figure 21.1(e). The dashed line along the border of Figure 21.1(e) indicates that $(\mathbf{A} \triangle \mathbf{B})^*$ extends to include all elements that are not in $\mathbf{A}$ or $\mathbf{B}$.

Suppose that we have a function $s()$ that determines the size of a set. We can relate the size of the various sets through

$$s(\mathbf{A} \cup \mathbf{B}) = \frac{s(\mathbf{A}) + s(\mathbf{B}) + s(\mathbf{A} \triangle \mathbf{B})}{2}. \tag{21.3}$$

To see why this holds, first convince yourself that

$$s(\mathbf{A}) + s(\mathbf{B}) = s(\mathbf{A} \cup \mathbf{B}) + s(\mathbf{A} \cap \mathbf{B}),$$

and then superimpose Figure 21.1(b), Figure 21.1(c), and Figure 21.1(d). Note that every area is covered twice, hence the division by 2 in (21.3). Likewise,

$$s(\mathbf{A} \cap \mathbf{B}) = \frac{s(\mathbf{A}) + s(\mathbf{B}) - s(\mathbf{A} \triangle \mathbf{B})}{2}. \tag{21.4}$$

**Figure 21.1:** Venn diagrams illustrating union, intersection, and the delta product of two sets.
- (a) Two sets $\mathbf{A}$ and $\mathbf{B}$
- (b) The union $\mathbf{A} \cup \mathbf{B}$
- (c) The intersection $\mathbf{A} \cap \mathbf{B}$
- (d) The delta product $\mathbf{A} \triangle \mathbf{B}$
- (e) The dual of the delta product $(\mathbf{A} \triangle \mathbf{B})^*$

### The Delta Product for Blades

The `meet` and `join` products are the geometrical versions of set intersection and union, respectively, applied to blades rather than sets. They really work on the bases spanning the blades, and are in that sense discrete. We want to compute the join of two blades $\mathbf{A}$ and $\mathbf{B}$. Instead of thinking of $\mathbf{A}$ and $\mathbf{B}$ as continuous oval blobs, think of them as discrete factors, united by a boundary. That converts Figure 21.1 into Figure 21.2. Let us assume that $\mathbf{A}$ and $\mathbf{B}$ can be factored as

$$\mathbf{A} = \mathbf{a}_1 \mathbf{a}_2 \mathbf{c},$$
$$\mathbf{B} = \mathbf{c} \mathbf{b}_1.$$

This means that $\mathbf{A}$ and $\mathbf{B}$ have one factor $\mathbf{c}$ in common, and $\mathbf{a}_1$, $\mathbf{a}_2$, and $\mathbf{b}_1$ are independent (how we arrive at this factorization is discussed later on). Figure 21.2(a) illustrates this basic setting. Obviously, $\mathbf{A} \cap \mathbf{B}$ is proportional to $\mathbf{c}$ (Figure 21.2(c)), and $\mathbf{A} \cup \mathbf{B}$ is proportional to $\mathbf{a}_1 \wedge \mathbf{a}_2 \wedge \mathbf{c} \wedge \mathbf{b}_1$ (Figure 21.2(b)). Figure 21.2(d) illustrates $\mathbf{A} \triangle \mathbf{B}$, and Figure 21.2(e) illustrates $(\mathbf{A} \triangle \mathbf{B})^*$.

**Figure 21.2:** Venn diagrams illustrating `Meet`, `Join`, and the delta product of two blades.
$\mathbf{A} = \mathbf{a}_1 \wedge \mathbf{a}_2 \wedge \mathbf{c}$, $\mathbf{B} = \mathbf{c} \wedge \mathbf{b}_1$ (see also Figure 21.1).

The algorithm for computing the `meet` and `join` [6, 8] presented in this section first computes the required grade of the `meet` and `join`, for which we need the delta product for blades (from [8]). Then it works towards constructing either the `meet` or the `join`.

As we observed in Section 19.3, the geometric product acts like a spatial exclusive *or* on basis blades. The same is true for regular blades when we focus on highest nonzero grade part of the geometric product: it is the spatial exclusive or of the blades since it contains all the factors that do not occur in both arguments. In our example,

$$\mathbf{A} \mathbf{B} = (\mathbf{a}_1 \mathbf{a}_2 \mathbf{c}) (\mathbf{c} \mathbf{b}_1) = (\mathbf{c} \cdot \mathbf{c}) \mathbf{a}_1 \mathbf{a}_2 \mathbf{b}_1.$$

Note that we do not need to factorize the blades explicitly to get this result. The geometric product automatically eliminates the dependent factors. So the top grade part of a geometric product $\mathbf{A} \mathbf{B}$ is a blade that contains all factors that were present in either $\mathbf{A}$ or $\mathbf{B}$. We call this the *delta product of blades*, and define it as follows:

$$\mathbf{A} \triangle \mathbf{B} \equiv \langle \mathbf{A} \mathbf{B} \rangle_{\text{max}}$$

where max is the largest grade such that $\mathbf{A} \triangle \mathbf{B}$ is not zero. The delta refers to the property of the delta product to compute the blade that contains factors that are present in either of the arguments, which makes it like the symmetric difference of the factors in $\mathbf{A}$ $\mathbf{B}$ which we discussed above.

### Grade Relations

Once we have the delta product of blades, we can derive the following useful relations by analogy to (21.3) and (21.4):

$$\text{grade}(\mathbf{A} \cup \mathbf{B}) = \frac{\text{grade}(\mathbf{A}) + \text{grade}(\mathbf{B}) + \text{grade}(\mathbf{A} \triangle \mathbf{B})}{2} \tag{21.5}$$

$$\text{grade}(\mathbf{A} \cap \mathbf{B}) = \frac{\text{grade}(\mathbf{A}) + \text{grade}(\mathbf{B}) - \text{grade}(\mathbf{A} \triangle \mathbf{B})}{2} \tag{21.6}$$

### Constructing Meet and Join

Our `meet` algorithm starts with a scalar, and expands it by the outer product with new vectors until it arrives at the true meet. Potential factors of the `meet` satisfy the following conditions, which you may verify using Figure 21.2:

- They are not factors of the delta product;
- They are factors of $\mathbf{A}$ and $\mathbf{B}$.

Likewise, the algorithm initially assumes that the `join` is the pseudoscalar, and removes factors from it until the true join is obtained. Factors that should not be in the `join` satisfy the following conditions:

- They are factors of the dual of the delta product;
- They are not factors of $\mathbf{A}$ and $\mathbf{B}$.

Before we can formulate the algorithm, we repeat two relations from Section 5.3:

$$\mathbf{A} \cup \mathbf{B} = \mathbf{A} \wedge ((\mathbf{A} \cap \mathbf{B})^{-1} \rfloor \mathbf{B}) \tag{21.7}$$

$$\mathbf{A} \cap \mathbf{B} = (\mathbf{B} \rfloor (\mathbf{A} \cup \mathbf{B})^{-1}) \rfloor \mathbf{A} \tag{21.8}$$

These equations can be used to obtain the `join` from the `meet`, and vice versa.

### The Meet and Join Algorithm

We now have enough building blocks to construct an algorithm to compute the `meet` and `join`:

1. **Input:** two blades $\mathbf{A}$, $\mathbf{B}$, and possibly a threshold $\epsilon$ for the delta product.

2. If $\text{grade}(\mathbf{A}) > \text{grade}(\mathbf{B})$, swap $\mathbf{A}$ and $\mathbf{B}$. This may engender an extra sign, so be careful when you need to interpret the results (see Section 5.6).

3. Compute the dual of the delta product: $\mathbf{S} = (\mathbf{A} \triangle \mathbf{B})^*$. A threshold $\epsilon$ may be used to suppress floating-point noise when computing the delta product (specifically, when determining what is the top grade part of $\mathbf{A} \mathbf{B}$ that is not zero).

4. Factorize $\mathbf{S}$ into factors $\mathbf{s}_i$.

5. Compute the required grade of the `meet` and `join` ((21.5) and (21.6)).

6. Set $\mathbf{M} \leftarrow 1$, $\mathbf{J} \leftarrow \mathbf{I}_n$ ($\mathbf{I}_n$ denotes the pseudoscalar of the total space).

7. For each of the factors $\mathbf{s}_i$:
   - (a) Compute the projection $\mathbf{p}_i$ and rejection $\mathbf{r}_i$ of $\mathbf{s}_i$ and $\mathbf{A}$:
     $$\mathbf{p}_i = (\mathbf{s}_i \rfloor \mathbf{A}) \rfloor \mathbf{A}^{-1}$$
     $$\mathbf{r}_i = \mathbf{s}_i - \mathbf{p}_i$$
   - (b) If the projection is not zero, then wedge it to the `meet`: $\mathbf{M} \leftarrow \mathbf{M} \wedge \mathbf{p}_i$. If the new grade of $\mathbf{M}$ is the required grade of the `meet`, then compute the `join` using (21.7), and break the loop. Otherwise continue with $\mathbf{s}_{i+1}$.
   - (c) If the rejection is not zero, then remove it from the `join`: $\mathbf{J} \leftarrow \mathbf{r}_i \rfloor \mathbf{J}$. If the new grade of $\mathbf{J}$ is the required grade of the `join`, then compute the `meet` using (21.8), and break the loop. Otherwise continue with $\mathbf{s}_{i+1}$.

8. **Output:** $\mathbf{A} \cap \mathbf{B}$ and $\mathbf{A} \cup \mathbf{B}$.

For added efficiency, step 4 could be integrated into the main loop of the algorithm (i.e., only find factors of $\mathbf{S}$ as required).

Note that the algorithm returns both $\mathbf{A} \cap \mathbf{B}$ and $\mathbf{A} \cup \mathbf{B}$ at the same time, while only one of them may be required. However, benchmarks have shown that this algorithm is more efficient than an algorithm that searches specifically for either the `meet` or the `join`, as it will terminate as soon as it finds either of them. The returned `join` and `meet` are based on the same factorization, so we can use relationships of (21.7) and (21.8) to compute one given the other.

### Complexity Analysis

The number of loop cycles in the algorithm is $n-1$ in the worst case, where $n$ is the dimension of the vector space. This can be understood by analyzing the following worst-case scenario,

$$\mathbf{A} = \mathbf{e}_n, \quad \mathbf{B} = \mathbf{e}_n,$$

in which case

$$\mathbf{A} \triangle \mathbf{B} = 1, \quad \mathbf{S} = (\mathbf{A} \triangle \mathbf{B})^* = \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \cdots \wedge \mathbf{e}_n.$$

The algorithm will start by projecting and rejecting $\mathbf{e}_1$. The projection will be zero, so $\mathbf{M}$ will not grow towards the actual meet (likewise for $\mathbf{e}_2 \cdots \mathbf{e}_{n-1}$). When the projection is zero, the rejection is obviously nonzero, so each of the rejections is removed from $\mathbf{J}$. While this brings $\mathbf{J}$ closer and closer to the actual join, $\mathbf{J}$ has to shrink all the way until it is of grade 1, which will not happen until all $\mathbf{e}_1 \cdots \mathbf{e}_{n-1}$ have been processed, leading to $O(n)$ cycles of the loop.

We should note, however, that when the inputs $\mathbf{A}$ and $\mathbf{B}$ are in general position, the projection and rejection are likely to be nonzero in each cycle of the loop. In that case the required number of cycles is $\min(\text{grade}(\text{meet}), \text{grade}(\text{join})) \leq n/2$. For numerical stability, we should require that the projections and rejections have some minimum weight, which will increase the number of cycles (because some projections and rejections will not be used for computation).

---

## 21.8 Structural Exercises

1. For $A = \mathbf{e}_1 + \mathbf{e}_2 \wedge \mathbf{e}_3$, compute $A^{-1}$, then verify that $\hat{A} A^{-1}$ and $A A^{-1}$ indeed behave differently under the test in the algorithm of Section 21.5.

2. Prove that $\mathbf{f} \equiv (\mathbf{c} \rfloor \mathbf{B})/\mathbf{B}$ is a factor of $\mathbf{B}$ (if nonzero) so that $\mathbf{B} = \mathbf{f} \wedge \mathbf{B}_f$ for some blade $\mathbf{B}_f$. Give an expression for a possible $\mathbf{B}_f$ (it is not unique).
