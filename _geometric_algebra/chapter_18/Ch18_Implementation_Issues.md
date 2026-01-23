# Chapter 18: Implementation Issues

In the first two parts of this book, we have given an abstract description of geometric algebra that is mostly free of coordinates and other low-level implementation details. Even though we have provided many programming examples, this may still have left you with a somewhat unreal feeling about geometric algebra, and an impression that any implementation of geometric algebra would be computationally prohibitive in a practical application. To address these concerns, Part III gives details on how to create an efficient numerical implementation of geometric algebra.

We describe the implementation of all products, operations, and models that were used in the preceding parts. The description is from the viewpoint of representing multivectors as a weighted sum of basis blades, an approach that was already hinted at in Section 2.9.4. This is by far the most common way of implementing geometric algebra, although other approaches are also possible. We briefly mention alternatives in Section 18.3.

Our ultimate goal is efficient numerical implementation, not symbolic computer algebra. An efficient geometric algebra implementation uses symbolic manipulations only to bootstrap the implementation, and not during actual run-time computations. We have tried to keep the implementation description independent of any particular implementation, although Chapter 22 is basically a high-level description of how `Gaigen 2` works. `Gaigen 2` is the implementation behind the GA sandbox source code package that you have used in the programming examples and exercises.

---

## 18.1 The Levels of Geometric Algebra Implementation

All multivectors can be decomposed as a sum of basis blades. An example of a basis for a 3-D geometric algebra is

$$\left\{ \underbrace{1}_{\text{scalars}}, \quad \underbrace{\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3}_{\text{vector space}}, \quad \underbrace{\mathbf{e}_1 \wedge \mathbf{e}_2, \mathbf{e}_2 \wedge \mathbf{e}_3, \mathbf{e}_3 \wedge \mathbf{e}_1}_{\text{bivector space}}, \quad \underbrace{\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3}_{\text{trivector space}} \right\}.$$

The number of $k$-blades in a geometric algebra over an $n$-dimensional space is $\binom{n}{k}$, so there are a total of

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

basis elements required to span the entire geometric algebra. On such a basis we can represent any multivector $\mathbf{A}$ as a column vector $[[\mathbf{A}]]$ with $2^n$ elements, containing the coefficients of $\mathbf{A}$ on the basis. $\mathbf{A}$ can be retrieved by a matrix multiply of a symbolic row vector containing the basis elements. For the 3-D example above, this would be

$$\mathbf{A} = [[1, \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_2, \mathbf{e}_2 \wedge \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3]] \, [[\mathbf{A}]].$$

A $k$-blade only contains elements of grade $k$, and therefore has many zero entries in its coefficient vector $[[\mathbf{A}]]$, making the representation by $2^n$ elements rather wasteful. This effect becomes stronger in higher dimensions.

We should therefore explore the idea to make a more sparse representation of the elements of geometric algebra. It can still be based in this sum of basis blades principle, just executed with more sensitivity to the essential structure of geometric algebra.

With the sum of basis blades implementation as our core approach, a geometric algebra implementation naturally splits into four levels:

1. Selecting the basis blades and implementing the basic operations on them;
2. Implementing linear operations for multivectors;
3. Implementing nonlinear operations on multivectors;
4. The application level.

The following chapters first describe the first three levels, then continue to provide additional detail on efficiency and implementation, and finally talk about the fourth level, as follows:

- **Implementing Basic Operations for Basis Blades (Chapter 19).** Clearly, it pays to consider the lowest implementation level in detail. We introduce a convenient representation of basis blades and show how the elementary operations have a satisfyingly Boolean nature when considered on the basis. This will deepen your understanding of them and leads to efficient algorithms for the most basic computations.

- **The Linear Middle Level (Chapter 20).** We then use those basic capabilities to establish the middle level. Many operations of geometric algebra are linear and distributive. This property makes their implementation quite simple, given that we can already compute them for the basis blades. We consider implementation of this level through matrices (most directly exploiting the linear nature of the operators) or by looping over lists of basis blades (which more naturally leads to an efficient implementation).

- **The Nonlinear Level (Chapter 21).** Geometric algebra contains some important operations that are elementary, but not linear or distributive (examples are inversion, `meet` and `join`, and exponentiation). As a consequence, the approach used in the middle-level implementation cannot be used here. These operations are implemented using specialized algorithms, which are actually largely independent of the middle-level implementation. Only for efficiency reasons do we sometimes need direct access to the multivector representation (e.g., to find the largest coordinate in a numerically stable factorization algorithm).

- **Our Reference Implementation (Online).** To better illustrate the implementation ideas, we have written an accompanying reference implementation in Java based on the list of basis blades approach. It is available at http://www.geometricalgebra.net. This reference implementation was written for educational purposes, and it is not the same as the GA sandbox source code package. The difference is that in our reference implementation we have favored simplicity and readability over efficiency, so we do not recommend using it for computationally intensive applications.

- **Efficient Implementation (Chapter 22).** We show how to specialize the implementation according to the structure of geometric algebra to obtain high run-time efficiency. We also present benchmarks that illustrate that the performance of geometric algebra can be close to traditional (linear-algebra-based) geometry implementations, despite the much higher dimensionality of $2^n$ for its internal algebra. It describes techniques applied in `Gaigen 2`, which is the efficient software behind the GA sandbox source code package, and what we use in our applications.

- **The Application Level (Chapter 23).** You could consider the actual use of geometric algebra in your own application the fourth implementation level. In Chapter 23 we give an example of such practical use, in the form of the description of a ray tracer that was implemented using the conformal model. We describe the equations of the ray tracer in actual code and highlight decisions such as picking the right conformal primitive to represent a particular concept. The benchmarks of Chapter 22 are based on this ray tracer.

---

## 18.2 Who Should Read What

The implementation description is quite detailed and not everyone will want to read all of it. We envision three types of audiences:

- If you are **new to geometric algebra**, the first two parts of the book may leave you wondering how this is ever going to work in an actual implementation (with those weird metrics, as a graded algebra, with so many diverse products, etc.). The following chapters should remove the fuzziness and magic. First, you will want to read Chapter 20 on linear operations. This should give you the comfortable feeling that geometric algebra is fully consistent, since it has the structure of the linear algebra of selected matrices. After that, you may want to read the first part of Chapter 19 on basis blades as it provides another viewpoint for understanding the basic products. Then give a cursory look to the rest of the chapters, but be sure to read the benchmarks that compare geometric algebra to traditional methods in Section 22.5.

- If you are **considering using geometric algebra** in one of your programs, you might want some background information that helps you pick a particular implementation, especially the appropriate representation of the elements of geometry. In that case we recommend skipping Chapter 19 on basis blades, but reading all of the linear Chapter 20. Then give a cursory look at the nonlinear algorithms and efficiency (Chapter 21 and 22). Finally, read the ray-tracing Chapter 23 in detail, as it will show you actual geometric algebra code that might be similar to what you're going to write yourself, regardless of what implementation you pick.

- If you are a **hard-core coder** and want to write your own implementation, or simply want to know all the details, we suggest you read all chapters in full detail and the proper order.

---

## 18.3 Alternative Implementation Approaches

In the coming chapters, we will concentrate on one specific implementation approach, where multivectors are represented as a sum of basis blades. It is what we found worked best for low-dimensional geometric algebras useful to computer science. It is also the most commonly used approach by others. But before we explore the detailed consequences, we use the remainder of this chapter to mention some different approaches, just to widen your field of view. Some of these methods affect only the middle (linear) implementation level, while others are so radically different that they affect every level.

### 18.3.1 Isomorphic Matrix Algebras

The linearity and associativity of geometric algebra suggests representing the whole algebra with its geometric product by a single matrix algebra: all elements become represented as $2^n \times 2^n$ matrices, and the geometric product is represented as the matrix product. This is structurally pretty and quite well known among mathematicians as a desirable representation technique, but it is computationally very expensive. It is in fact a representation of Clifford algebra rather than geometric algebra (see Section 7.7.2), and as such rather wasteful: in a true geometric usage of properly constructed elements such as blades and versors, the corresponding matrices tend to be sparse, but this implementation does not make use of that property. Also, it cannot implement the contraction and outer product as easily as the geometric product.

We will use this idea briefly to implement inversion of general multivectors in Section 21.2.

### 18.3.2 Irreducible Matrix Implementations

The $2^n \times 2^n$ matrices do not form the smallest matrix representation of the algebra, if we follow common practice in mathematics and allow the field of the linear mappings they represent to include not only $\mathbb{R}$ (the real numbers), but also $\mathbb{C}$ (the complex numbers) and $\mathbb{H}$ (the quaternions).

Such linear matrix representations have long been known for Clifford algebras of spaces $\mathbb{R}^{p,q}$ with arbitrary signature $(p, q)$ (which means $p + q$ spatial dimensions, of which $p$ basis vectors have a positive square, and $q$ have a negative square; see Appendix A). Again, each element of the algebra is represented as a matrix, and the matrix product of two such representatives is precisely the representation of the element that is their geometric product. We repeat part of the table of such representations in Table 18.1 (see [49]), and offer some structural exercises at the end of this chapter to familiarize yourself with them.

The structural advantage of such representations is that the geometric product becomes a simple matrix multiply (although the elements of the matrix may be reals, complex numbers, or quaternions). However, this is mostly a mathematical curiosity that will not save processing time in practice, since approximately the same number of operations have to be performed as in the basis-of-blades representation that is our reference implementation. (Only if special hardware were present to handle complex number and quaternion multiplications more efficiently than arbitrary multiplications, could these methods become more efficient than the multiplication of real valued matrices.)

**Table 18.1:** Matrix representations of Clifford algebras of signatures $(p,q)$. Notation: $\mathbb{R}(n)$ are $n \times n$ real matrices, $\mathbb{C}(n)$ are $n \times n$ complex-valued matrices, and $\mathbb{H}(n)$ are $n \times n$ quaternion-valued matrices. The notation $^2\mathbb{R}(n)$ is used for ordered pairs of $n \times n$ real matrices (which you may think of as a block-diagonal $2n \times 2n$ matrix containing two real $n \times n$ real matrices on its diagonal and zeros elsewhere), and similarly for the other number systems.

|         | $q = 0$         | $q = 1$         | $q = 2$         | $q = 3$         |
|---------|-----------------|-----------------|-----------------|-----------------|
| $p = 0$ | $\mathbb{R}(1)$ | $\mathbb{C}(1)$ | $\mathbb{H}(1)$ | $^2\mathbb{H}(1)$ |
| $p = 1$ | $^2\mathbb{R}(1)$ | $\mathbb{R}(2)$ | $\mathbb{C}(2)$ | $\mathbb{H}(2)$ |
| $p = 2$ | $\mathbb{R}(2)$ | $^2\mathbb{R}(2)$ | $\mathbb{R}(4)$ | $\mathbb{C}(4)$ |
| $p = 3$ | $\mathbb{C}(2)$ | $\mathbb{R}(4)$ | $^2\mathbb{R}(4)$ | $\mathbb{R}(8)$ |
| $p = 4$ | $\mathbb{H}(2)$ | $\mathbb{C}(4)$ | $\mathbb{R}(8)$ | $\mathbb{C}(8)$ |

Moreover, the matrix representations have the disturbing disadvantage that they only work for the geometric product. As long as they are used for the Clifford algebras for which they were developed, this is not a problem—but it makes this representation cumbersome for geometric algebra in general, where derived products such as the outer product and contractions are also important. True, a similar representation of outer products can be easily established, but one would have to switch between representations to perform one product or the other, as both may be needed in a single application. And unfortunately, since the contraction inner products are not associative, they are not isomorphic to matrix algebras, so they cannot be implemented in the same framework. (Actually, this non-associativity of the contraction will require special measures in any implementation scheme, including ours.)

### 18.3.3 Factored Representations

The mostly multiplicative structure of geometric algebra (with versors as geometric products of vectors, and blades as outer products of vectors) has recently been explored by the authors to produce factorized representations. This seems a viable implementation method for high-dimensional algebras, but more research is needed.

A $k$-blade can be stored as a list of $k$ vectors. The outer product of these vectors is the value of the blade. Likewise, a versor can be stored as a list of vectors whose geometric product is the value of the versor. The storage requirement of blades and versors becomes $O(n^2)$ compared to $O(2^n)$ for the basis-of-blades method. Multivectors that are not blades or versors can only be represented as a sum of multiple blades or versors, and thus require more storage.

This multiplicative representation is radically different from the usual additive representation. As a consequence, the implementation of products and operations is also very different. What may be a difficult problem in one implementation approach can be trivial in the other, and vice versa. For example, addition is simple in the basis of blades approach, but one of the hardest problems in a factored representation. The `meet` and `join` are trivial with factored representation (given that you already have a linear algebra library like LAPACK), while they lead to a rather involved algorithm in the sum-of-basis-blades approach.

We do not discuss this approach further because it is best suited for high-dimensional ($n > 10$) geometric algebras, which are of less interest in this book. The details will appear in Daniel Fontijne's Ph.D. thesis.

---

## 18.4 Structural Exercises

1. In a 2-D Euclidean geometric algebra on an orthonormal basis $\{\mathbf{e}_1, \mathbf{e}_2\}$, the general element $X$ can be written as:

   $$X = x_0 + x_1 \, \mathbf{e}_1 + x_2 \, \mathbf{e}_2 + x_{12} \, \mathbf{e}_{12}.$$

   According to Table 18.1, this algebra should be representable as the matrix algebra $\mathbb{R}(2)$ (i.e., we should be able to find a $2 \times 2$ matrix representing the general element so that the geometric product of elements is represented as the matrix product). Show that the following works:

   $$[[\mathbf{x}]] = \begin{bmatrix} x_0 + x_2 & x_1 - x_{12} \\ x_1 + x_{12} & x_0 - x_2 \end{bmatrix}$$

   This is not unique; some permutations of the same principles work as well, but not all. Why must the scalar part always be on the diagonal?

2. For a 3-D Euclidean vector space, show that you can generate a matrix algebra from the following representation of a vector $\mathbf{x} = x \, \mathbf{e}_1 + y \, \mathbf{e}_2 + z \, \mathbf{e}_3$:

   $$[[\mathbf{x}]] = \begin{bmatrix} z & 0 & x & -y \\ 0 & z & y & x \\ x & y & -z & 0 \\ -y & x & 0 & -z \end{bmatrix}$$

   Compute the representation of a general element of this algebra. (This representation is not in Table 18.1 because it is not the smallest matrix algebra; see the following exercise).

3. For a 3-D Euclidean vector space, the matrix representation $\mathbb{C}(2)$ from Table 18.1 may be generated by:

   $$[[\mathbf{x}]] = \begin{bmatrix} z & x + iy \\ x - iy & -z \end{bmatrix},$$

   where $i$ is the complex imaginary (so $i^2 = -1$). Verify this and compute the representation of a general element of this algebra.
