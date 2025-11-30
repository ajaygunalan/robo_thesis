# Matrix as Sum of Rank-1 Matrices

## Core Insight
Every matrix is built from rank-1 "building blocks"

## 1. Fundamental Theorem

**Theorem**: Any matrix $A \in \mathbb{R}^{m \times n}$ with rank $r$ can be written as:
$$A = \sum_{i=1}^r u_i \otimes v_i$$
where $\otimes$ denotes outer product $(u_i v_i^T)$.

**Key Fact**: $r$ is the minimum number of rank-1 terms needed.

## 2. Three Perspectives

### Algebraic View
- Column-row expansion: $A = [a_1|...|a_n] = \sum_i a_i e_i^T$
- Connects to [[lu_decomposition]]: $A = LU = \sum_i \ell_i u_i^T$

### Geometric View
- Each $u_i \otimes v_i$ is a "fundamental action" of $A$
- Like building blocks assembling complex structures

### Optimal Decomposition via SVD
$$A = \sum_{i=1}^r \sigma_i u_i v_i^T$$
- Ordered by importance: $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_r$
- Best $k$-rank approximation: keep first $k$ terms
- See [[_linear_algebra/svd]] for details


