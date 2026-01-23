# Chapter 20: The Linear Products and Operations

The linear products we use in this book are the geometric product, the outer product, the contraction inner products, the scalar product, and the commutator product. They are all linear in their arguments. Examples of unary linear operations that are discussed in this chapter are addition, reversion, grade involution, and grade extraction of multivectors. This chapter presents two ways to implement the linear products and operations of geometric algebra.

Both implementation approaches are based on the linearity and distributivity of these products and operations. The first approach uses linear algebra to encode the multiplying element as a square matrix acting on the multiplied element, which is encoded as a column matrix. We present this approach because the matrix ideas are familiar to many people, because it is convenient, and because it works for general Clifford algebras. However, it does not exploit the sparseness of most elements in geometric algebra, and is not used much in practice.

The second approach is effectively a sparse matrix approach and uses the basis blades idea of the previous chapter, storing multivectors as lists of weighted basis blades and literally distributing the work of computing the products and operations to the level of basis blades. This automatically employs the sparseness of geometric algebra and provides a more natural path towards the optimization of Chapter 22. This is also the approach used in our reference implementation.

---

## 20.1 A Linear Algebra Approach

A multivector from an $n$-dimensional geometric algebra can be stored as a $2^n \times 1$ column matrix. Each element in the matrix is a coordinate that refers to a specific basis blade. To formalize this, let us define a row matrix $\mathbb{L}$ whose elements are the basis blades of the basis, listed in order. For example, in 3-D:

$$\mathbb{L} = [\![1, \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_2, \mathbf{e}_2 \wedge \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_3, \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3]\!]$$

Using $\mathbb{L}$ we can represent a multivector $A$ by a $2^n \times 1$ matrix $[\![A]\!]$ with elements

$$A = \mathbb{L} \, [\![A]\!].$$

We use the following notation to indicate equivalence between the actual geometric algebra operations and their implementation in linear algebra:

$$A \rightleftharpoons [\![A]\!].$$

### 20.1.1 Implementing the Linear Operations

The elements of geometric algebra form a linear space, and these linear operations are implemented trivially in the matrix approach:

- **Addition** of elements is performed by adding the matrices:

$$A + B \rightleftharpoons [\![A]\!] + [\![B]\!].$$

- **Scalar multiplication** is implemented as multiplication of the matrix $[\![A]\!]$ by the scalar:

$$\alpha A \rightleftharpoons \alpha \, [\![A]\!].$$

- The **unary linear operations** of reversion, grade involution, and Clifford conjugation can also be implemented as matrices. The entries of these matrices need to be set according to the corresponding operations on the basis blades in $\mathbb{L}$.

  For instance, for the reversion we define the (constant) diagonal matrix $[\![\mathsf{R}]\!]$, whose entries are defined as

  $$[\![\mathsf{R}]\!]_{i,i} = (-1)^{\text{grade}(\mathbb{L}_i)(\text{grade}(\mathbb{L}_i)-1)/2}.$$

  Then reversion is implemented as

  $$\widetilde{A} \rightleftharpoons [\![\mathsf{R}]\!] \, [\![A]\!].$$

- **Extracting the $k$th grade part** of a multivector is also a unary linear operator. For each grade we need to construct a diagonal selection matrix $[\![\mathsf{S}^k]\!]$, so that the operation can be performed as the matrix operator:

  $$\langle A \rangle_k \rightleftharpoons [\![\mathsf{S}^k]\!] \, [\![A]\!].$$

  The entries of the matrix $[\![\mathsf{S}^k]\!]$ must be defined as

  $$[\![\mathsf{S}^k]\!]_{i,j} = \begin{cases} 1 & \text{if } \text{grade}(\mathbb{L}_i) = k \text{ and } i = j \\ 0 & \text{otherwise} \end{cases},$$

  which may be summarized as $[\![\mathsf{S}^k]\!]_{i,j} = \delta^j_i \, \delta^k_{\text{grade}(\mathbb{L}_i)}$.

### 20.1.2 Implementing the Linear Products

The linear products can all be implemented using matrix multiplication. If we consider the geometric product $A B$, the result is linear in $B$, so $A$ is like a linear operator acting on $B$. In the $\mathbb{L}$-based representation, that $A$-operator can be represented by matrix $[\![A^G]\!]$ acting on column matrix $[\![B]\!]$ (the superscript $G$ denotes that $A$ acts on $B$ by the geometric product). That gives

$$A B \rightleftharpoons [\![A^G]\!][\![B]\!].$$

Here $[\![A^G]\!]$ is a $2^n \times 2^n$ matrix; we need to construct it so that it corresponds to the geometric product. As we do so, we find that its entries are certain linear combinations of the coefficients of $A$ on the $\mathbb{L}$-basis. There is therefore not a single representation of the geometric product: each element acts through its own matrix. By the same reasoning, each element $A$ also has an associated outer product matrix $[\![A^O]\!]$, which describes the action of the operation $A \wedge$, and a left contraction matrix $[\![A^L]\!]$ for the operation $A \rfloor$, and so on.

Whenever we want to compute a product, we therefore need to construct the corresponding matrix. Let us describe how that is done for the geometric product matrix $[\![A^G]\!]$.

For simplicity, we temporarily assume that the algebra has a diagonal metric matrix (e.g., a Euclidean metric). To devise a rule on how to fill in the entries of $[\![A^G]\!]$, we consider the geometric product of two basis blades weighted by their respective coordinates from $[\![A]\!]$ and $[\![B]\!]$. These are scalars, and they get multiplied by the geometric algebra elements from $\mathbb{L}$—that is where the structure of geometric algebra enters the multiplication. The product of two such elements $\mathbb{L}_k$ and $\mathbb{L}_j$ is a third element $\mathbb{L}_i$, with a scalar $s^{k,j}_i$ determined by the metric (in a Euclidean metric, $s^{k,j}_i = \pm 1$, with the minus sign occurring for instance for basis 2-blades, so these are not simply the $m_j$ of the metric matrix in (19.1)).

$$\mathbb{L}_k \mathbb{L}_j = s^{k,j}_i \mathbb{L}_i \tag{20.1}$$

Think of the scalars $s^{k,j}_i$ as the "structure coefficients" of the algebra. As their definition shows, they involve the products of basis blades (the components of $\mathbb{L}$), so they can be determined efficiently by the methods of the previous chapter.

We can now specify what the product of the matrices $[\![A]\!]$ and $[\![B]\!]$ should satisfy, coefficient by coefficient:

$$([\![A]\!]_k \mathbb{L}_k)([\![B]\!]_j \mathbb{L}_j) = s^{k,j}_i [\![A]\!]_k [\![B]\!]_j \mathbb{L}_i. \tag{20.2}$$

To achieve the equivalent of this equation through matrix multiplication (i.e., $[\![A^G]\!] [\![B]\!] = [\![C]\!]$), it is clear that $s^{k,j}_i [\![A]\!]_k [\![B]\!]_j$ should end up in row $i$ of $[\![C]\!]$, so $s^{k,j}_i [\![A]\!]_k$ should be on row $i$ of $[\![A^G]\!]$. The fact that $s^{k,j}_i [\![A]\!]_k$ should combine with $[\![B]\!]_j$ means that $s^{k,j}_i [\![A]\!]_k$ should be in column $j$. In summary,

$$([\![A]\!]_k \mathbb{L}_k)([\![B]\!]_j \mathbb{L}_j) = [\![A]\!]_k [\![B]\!]_j s^{k,j}_i \mathbb{L}_i \quad \rightarrow \quad [\![A^G]\!]_{i,j} = \sum_k s^{k,j}_i [\![A]\!]_k. \tag{20.3}$$

This final rule does not involve the symbolic basis list $\mathbb{L}$ anymore, yet is based fully on the geometric algebra structure it contributes. By executing this rule for all indices $k, j$, we obtain, by linearity, a full geometric product matrix $[\![A^G]\!]$. An example of the geometric product matrix $[\![A^G]\!]$ is shown in Figure 20.1 for a 3-D Euclidean metric.

When the metric matrix is nondiagonal, things get slightly more complicated, because the geometric product of two basis blades can result in a sum of basis blades:

$$\mathbb{L}_k \mathbb{L}_j = \sum_i s^{k,j}_i \mathbb{L}_i.$$

It is clear that we should propagate this change to the computation of the matrix $[\![A^G]\!]$:

$$([\![A]\!]_k \mathbb{L}_k)([\![B]\!]_j \mathbb{L}_j) = [\![A]\!]_k [\![B]\!]_j \sum_i s^{k,j}_i \mathbb{L}_i. \tag{20.4}$$

Thus we have to execute the rule in (20.3) for each $s^{k,j}_i [\![A]\!]_k$.

**Summarizing**, the following algorithm computes the geometric product matrix for a multivector $A$:

1. Initialize the matrix $[\![A^G]\!]$ to a $2^n \times 2^n$ null matrix.
2. Loop over all indices $k, j$ to compute the geometric product of all basis blades as in (20.1). How to compute the products of basis blades is described in Chapter 19.
3. Add each $s^{k,j}_i [\![A]\!]_k$ to the correct element of $[\![A^G]\!]$ according to the rule on the right-hand side of (20.3).

### Figure 20.1: Symbolic Matrices for Linear Products

**Figure 20.1:** Symbolic matrices for computing the geometric product ($[\![A^G]\!]$), outer product ($[\![A^O]\!]$) and left contraction ($[\![A^L]\!]$) in a 3-D Euclidean geometric algebra. A notational shorthand is used for readability, i.e., $A_0$ is the scalar coordinate of $[\![A]\!]$, $A_1$ is the coordinate from $[\![A]\!]$ that refers to $\mathbf{e}_1$; $A_{123}$ is the $\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \mathbf{e}_3$-coordinate, etc.

#### Geometric Product Matrix $[\![A^G]\!]$

$$[\![A^G]\!] = \begin{bmatrix}
+A_0 & +A_1 & +A_2 & +A_3 & -A_{12} & -A_{23} & -A_{13} & -A_{123} \\
+A_1 & +A_0 & +A_{12} & +A_{13} & -A_2 & -A_{123} & -A_3 & -A_{23} \\
+A_2 & -A_{12} & +A_0 & +A_{23} & +A_1 & -A_3 & +A_{123} & +A_{13} \\
+A_3 & -A_{13} & -A_{23} & +A_0 & -A_{123} & +A_2 & +A_1 & -A_{12} \\
+A_{12} & -A_2 & +A_1 & +A_{123} & +A_0 & -A_{13} & +A_{23} & +A_3 \\
+A_{23} & +A_{123} & -A_3 & +A_2 & +A_{13} & +A_0 & -A_{12} & +A_1 \\
+A_{13} & -A_3 & -A_{123} & +A_1 & -A_{23} & +A_{12} & +A_0 & -A_2 \\
+A_{123} & +A_{23} & -A_{13} & +A_{12} & +A_3 & +A_1 & -A_2 & +A_0
\end{bmatrix}$$

#### Outer Product Matrix $[\![A^O]\!]$

$$[\![A^O]\!] = \begin{bmatrix}
+A_0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
+A_1 & +A_0 & 0 & 0 & 0 & 0 & 0 & 0 \\
+A_2 & 0 & +A_0 & 0 & 0 & 0 & 0 & 0 \\
+A_3 & 0 & 0 & +A_0 & 0 & 0 & 0 & 0 \\
+A_{12} & -A_2 & +A_1 & 0 & +A_0 & 0 & 0 & 0 \\
+A_{23} & 0 & -A_3 & +A_2 & 0 & +A_0 & 0 & 0 \\
+A_{13} & -A_3 & 0 & +A_1 & 0 & 0 & +A_0 & 0 \\
+A_{123} & +A_{23} & -A_{13} & +A_{12} & +A_3 & +A_1 & -A_2 & +A_0
\end{bmatrix}$$

#### Left Contraction Matrix $[\![A^L]\!]$

$$[\![A^L]\!] = \begin{bmatrix}
+A_0 & +A_1 & +A_2 & +A_3 & -A_{12} & -A_{23} & -A_{13} & -A_{123} \\
0 & +A_0 & 0 & 0 & -A_2 & 0 & -A_3 & -A_{23} \\
0 & 0 & +A_0 & 0 & +A_1 & -A_3 & 0 & +A_{13} \\
0 & 0 & 0 & +A_0 & 0 & +A_2 & +A_1 & -A_{12} \\
0 & 0 & 0 & 0 & +A_0 & 0 & 0 & +A_3 \\
0 & 0 & 0 & 0 & 0 & +A_0 & 0 & +A_1 \\
0 & 0 & 0 & 0 & 0 & 0 & +A_0 & -A_2 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & +A_0
\end{bmatrix}$$

---

The product matrices need to be computed only once, to bootstrap the implementation. The results can be stored symbolically, leading to matrices such as $[\![A^G]\!]$ in Figure 20.1.

The same algorithm can compute the matrix for any product derived from the geometric product. Figure 20.1 also shows matrices for the outer product ($[\![A^O]\!]$) and the left contraction ($[\![A^L]\!]$). Note how these matrices are mostly identical to the geometric product matrix $[\![A^G]\!]$, but with zeros at specific entries. The reason is of course that these products are merely selections of certain grade parts of the more encompassing geometric product.

After the symbolic matrices have been initialized, computing an actual product $C = A B$ is reduced to creating a real matrix $[\![A^G]\!]$ according to the appropriate symbolic matrix and the coordinates of $[\![A]\!]$, and computing $[\![C]\!] = [\![A^G]\!][\![B]\!]$. So computing the products of basis blades as in (20.1) is only required during the initialization step, during which symbolic matrices are computed. This is fine in a general Clifford algebra, in which $A$ may be an arbitrary element of many grades. However, in geometric algebra proper elements tend to be rather sparse on the $\mathbb{L}$ basis, typically being restricted to a single grade for objects (which are represented by blades), or only odd or even grades for operators (which are represented by versors). Then the resulting matrices are sparse, and some kind of optimization in their computation should prevent the needless and costly evaluation of many zero results in their multiplication.

---

## 20.2 The List of Basis Blades Approach

Instead of representing multivectors as $2^n$ vectors and using matrices to implement the products, we can represent a multivector by a list of basis blades. That is how our reference implementation works. The linear products and operations are distributive over addition; for example, for the left contraction and the reverse we have

$$(\mathbf{a}_1 + \mathbf{a}_2 + \cdots + \mathbf{a}_n) \rfloor (\mathbf{b}_1 + \mathbf{b}_2 + \cdots + \mathbf{b}_m) = \sum_{i=1}^{n} \sum_{j=1}^{m} \mathbf{a}_i \rfloor \mathbf{b}_j,$$

$$(\mathbf{b}_1 + \mathbf{b}_2 + \cdots + \mathbf{b}_n)^{\sim} = \sum_{i=1}^{n} \widetilde{\mathbf{b}}_i.$$

Therefore, we can straightforwardly implement any linear product or operation for multivectors using their implementations of basis blades of the previous chapter. As an example, Figure 20.2 gives Java code from the reference implementation that computes the outer product.

### Figure 20.2: Outer Product Implementation

**Figure 20.2:** Implementation of the outer product of multivectors based on the list of blades approach. The `Multivector` class has a member variable `blades`, which is an `ArrayList` of `BasisBlades`. The function `simplify()` simplifies a list of `BasisBlades` by adding those blades that are equal up to scale.

```java
Multivector op(Multivector x) {
    ArrayList result = new ArrayList(blades.size() * x.blades.size());

    // loop over basis blade of 'this'
    for (int i = 0; i < blades.size(); i++) {
        BasisBlade B1 = (BasisBlade)blades.get(i);

        // loop over basis blade of 'x'
        for (int j = 0; j < x.blades.size(); j++) {
            BasisBlade B2 = (BasisBlade)x.blades.get(j);
            // compute actual outer product of the basis blades ...
            // ... and add to result:
            result.add(BasisBlade.op(B1, B2));
        }
    }
    return new Multivector(simplify(result));
}
```

The explicit loops over basis blades and the actual basis blade product evaluations are quite expensive computationally, and implementations based on this principle are about one or two orders of magnitude slower than implementations that expand the loops and optimize them. We will get back to this in Chapter 22.

---

## 20.3 Structural Exercises

1. Why are the first columns of $[\![A^G]\!]$ and $[\![A^O]\!]$ equal to $[\![A]\!]$? Why does this not hold for $[\![A^L]\!]$?

2. Why is $[\![A^O]\!]$ lower triangular?

3. You know that $\mathbf{a} \, \mathbf{B} = \mathbf{a} \rfloor \mathbf{B} + \mathbf{a} \wedge \mathbf{B}$ for a vector $\mathbf{a}$ and a blade $\mathbf{B}$. How do you recognize this fact in the relationship of $[\![A^G]\!]$, $[\![A^L]\!]$ and $[\![A^O]\!]$? Why do we not have $[\![A^G]\!] = [\![A^L]\!] + [\![A^O]\!]$?

4. Compute the matrix for the right contraction.
