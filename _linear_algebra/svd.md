# Singular Value Decomposition

## The Universal Matrix Factorization

**Theorem**: Every matrix $A \in \mathbb{R}^{m \times n}$ has a unique SVD:
$$A = U\Sigma V^T$$
where $U$, $V$ are orthogonal and $\Sigma$ is diagonal.

## 1. Multiple Perspectives

### Geometric View
SVD transforms space through three operations:
1. $V^T$ rotates and aligns input vectors
2. $\Sigma$ stretches/shrinks along principal axes
3. $U$ rotates vectors to final positions

### Algebraic View
SVD represents a matrix as a sum of rank-1 components:
$$A = \sum_{i=1}^r \sigma_i u_i v_i^T$$
These components are ordered by importance ($\sigma_1 \geq \sigma_2 \geq ...$).

### Generalization of Eigendecomposition
- Works for ALL matrices (not just square/symmetric)
- When $A$ is symmetric: $U = V$ and $\sigma_i = |\lambda_i|$

## 2. Fundamental Properties

### The Singular Values
- Unique and ordered: $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_r > 0$
- $\sigma_i = \sqrt{\text{eigenvalue of } A^T A}$
- Determine rank: $r =$ number of nonzero $\sigma_i$

### Connection to Subspaces
The SVD reveals the four fundamental subspaces:
- Column space: spanned by first $r$ columns of $U$
- Row space: spanned by first $r$ columns of $V$
- Null space: spanned by last $n-r$ columns of $V$
- Left null space: spanned by last $m-r$ columns of $U$


## A Note on Singular Value Decomposition (SVD)

Your notes on SVD are excellent. The one crucial point to emphasize is its role in low-rank approximation. The SVD expresses a matrix as a sum of rank-1 matrices, ordered by the magnitude of the singular values:

$$A = \sum_{i=1}^{r} \sigma_i u_i v_i^T = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \cdots + \sigma_r u_r v_r^T$$

The best rank-$k$ approximation to $A$ (for $k < r$) is simply the sum of the first $k$ terms. This is incredibly powerful for data compression and noise reduction, as it isolates the most significant "pieces" of the matrix.