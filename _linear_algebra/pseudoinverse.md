# Pseudoinverse

## Definition First

The Moore-Penrose pseudoinverse $A^\dagger$ satisfies four conditions:
1. $AA^\dagger A = A$
2. $A^\dagger A A^\dagger = A^\dagger$
3. $(AA^\dagger)^T = AA^\dagger$ ($AA^\dagger$ is symmetric)
4. $(A^\dagger A)^T = A^\dagger A$ ($A^\dagger A$ is symmetric)

## What It Does

The pseudoinverse $A^\dagger$ is a generalization of the ordinary matrix inverse that applies to any matrix (square or rectangular, full rank or rank-deficient). Intuitively, $A^\dagger$ serves as a "best possible inverse" of $A$ in situations where $A$ cannot be inverted in the usual sense.

## Connection to Linear Systems

For any $Ax = b$:
- $x^* = A^\dagger b$ minimizes $\|Ax - b\|_2$
- Among all minimizers, $x^*$ has smallest $\|x\|_2$

### Unifies All Cases:
1. **Unique solution exists**: $A^\dagger = A^{-1}$ (square, invertible)
2. **No solution exists**: $A^\dagger b$ gives least squares solution
3. **Infinitely many solutions**: $A^\dagger b$ gives minimum norm solution
4. **General case**: $A^\dagger$ handles all above cases automatically

## Computational Methods

| Method | When to Use | Key Advantage | Complexity |
|--------|-------------|---------------|------------|
| Normal Equations $(A^T A)^{-1}A^T$ | Small, well-conditioned | Simple formula | $O(mn^2)$ |
| QR Decomposition | Medium problems | Better stability | $O(mn^2)$ |
| SVD | Rank-deficient or ill-conditioned | Most general | $O(mn^2)$ |

**Warning**: Normal equations square the condition number: $\kappa(A^T A) = \kappa(A)^2$

For detailed SVD computation, see [[subjects/Linear Algebra/SVD]].

## Relationship to Fundamental Subspaces
- Projects onto $\text{Row}(A)$ via $A^\dagger A$
- Projects onto $\text{Col}(A)$ via $AA^\dagger$
- See [[Four Fundamental Subspaces]]

