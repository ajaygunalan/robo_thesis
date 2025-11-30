# Positive Definite Matrices

## Definition
A symmetric matrix $A$ is positive definite if $x^T Ax > 0$ for all $x \neq 0$.

## Equivalent Conditions
The following are equivalent for symmetric $A$:
1. $A$ is positive definite
2. All eigenvalues are positive
3. All leading principal minors are positive
4. $A = R^T R$ for some invertible $R$ (Cholesky factorization)

## Properties
- Positive definite matrices are invertible
- If $A$ is positive definite, so is $A^{-1}$
- Sum of positive definite matrices is positive definite

## Applications
- Optimization: Positive definite Hessian implies local minimum
- Numerical methods: Ensures stability
- Statistics: Covariance matrices

