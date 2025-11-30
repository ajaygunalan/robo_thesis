### The Frobenius Norm of A

$$||A||_F^2 = \sum_{i=1}^{n} \sum_{j=1}^{m} a_{ij}^2= a_{11}^2 + a_{12}^2 + \cdots + a_{1n}^2 + a_{21}^2 + a_{22}^2 + \cdots + a_{nn}^2$$ $$||A||_F^2 =\text{tr}(A^T A)$$ $$||A||_F^2 = \sigma_1^2 + \sigma_1^2 + \cdots + \sigma_r^2 \quad (\text{eigenvalues of} \; A^TA)$$



#### Key Properties

The Frobenius norm has several elegant properties that make this problem tractable:


##### 1. Invariance Under Orthogonal Transformations

For any orthogonal matrix $Q$ (where $Q^T Q = I$): $$||QA||_F^2 = ||A||_F^2$$


**Geometric Intuition**: Orthogonal transformations (such as rotations, reflections, and permutations) preserve lengths and angles, and thus preserve the Frobenius norm. This norm measures a matrix’s total energy—the sum of the squared magnitudes of its entries—derived from the squared lengths of its column vectors. Since orthogonal transformations reorient data without distorting vector lengths, they leave the Frobenius norm unchanged, unlike non-orthogonal transformations (e.g., scaling or shearing) which alter vector lengths and change the norm.



##### 2. Cyclic Property of Trace

$$\underbrace{\text{tr}(A^T B)}_{1} = \underbrace{\text{tr}(B^T A)}_{2} = \underbrace{\text{tr}(BA^T)}_{3}$$

$1$ and $2$ are $T$ of each other so they hold true.

$1$ and $3 \implies \text{tr}(CD) = \text{tr}(DC)$  holds because have the [[same_eigenvalues_different_eigenvectors]]



##### 3. Decomposition Formula

$||X - YQ||_F^2 = ||X||_F^2 + ||Y||_F^2 - 2\text{tr}(Q^T Y^T X)$

This transforms our problem: minimize distance → maximize correlation.

Since $|X|_F^2$ and $|Y|_F^2$ are constants, we need only maximize $\text{tr}(Q^T Y^T X)$.

