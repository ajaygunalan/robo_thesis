# Least Squares

## Why Least Squares?

When the system $Ax = b$ is **inconsistent**, we seek the best approximate solution by minimizing the Euclidean error:

$$\min_x |Ax - b|_2$$

This gives the $x$ for which $Ax$ is as close as possible to $b$.

## Problem Statement

Find $\hat{x}$ such that:

$$\hat{x} = \arg\min_x |Ax - b|_2^2$$

Setting the gradient to zero leads to the **normal equations**:

$$A^T A \hat{x} = A^T b$$

## Geometric Insight

- $A\hat{x}$: projection of $b$ onto $\text{Col}(A)$
- $r = b - A\hat{x}$: the residual is orthogonal to $\text{Col}(A)$
- This minimizes the distance from $b$ to any vector in $\text{Col}(A)$

**Orthogonality condition:**

$$A^T(b - A\hat{x}) = 0$$

## Solution Methods

### 1. Normal Equations

$$\hat{x} = (A^T A)^{-1}A^T b$$

-  Simple
-  Prone to numerical instability
-  Use for small, well-conditioned problems

### 2. QR Decomposition

If $A = QR$, then:

$$\hat{x} = R^{-1}Q^T b$$

- More stable than normal equations
- Slightly higher computational cost
- Preferred for medium-sized problems

### 3. SVD (Singular Value Decomposition)

If $A = U\Sigma V^T$, then:

$$\hat{x} = V\Sigma^{\dagger}U^T b$$

-  Most stable, works even when $A$ is rank-deficient
-  Most computationally expensive
-  Use for ill-conditioned or under/over-determined systems

## Pseudoinverse Formulation

$$\hat{x} = A^{\dagger}b$$

Where $A^{\dagger}$ is the **Moore-Penrose pseudoinverse**.

- Recovers least squares solution for overdetermined systems: $A^{\dagger} = (A^T A)^{-1}A^T$
- Gives **minimum-norm solution** when solutions aren't unique
- Provides a unified framework for all linear systems

## Summary Flow

```
Inconsistent System → Minimize ||Ax - b||₂
                     ↓
             Solve Normal Equations
                     ↓
           Use One of Three Methods:
       Normal Eq   →   QR   →   SVD
                     ↓         ↓
                  All yield x = A†b
```

**Core Idea:** Least squares replaces an unsolvable exact problem with a well-posed approximation by projecting $b$ onto the column space of $A$.