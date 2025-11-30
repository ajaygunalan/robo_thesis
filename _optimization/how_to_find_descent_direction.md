---
tags: optimization
---

![[descnet_direction.png]]
Descent direction set: ${d \in \mathbb{R^n}: g^{kT}d < 0}$ where $g^k = g(x^k)$
Think of A has rotating the vector $-g^K$

Let $g^k \ne 0$,  $d^k = -A^kg^k = A^k (-g^k)$  where $A^k$ is symmetric matrix.
if $A^k$ is **positive definite**  $\implies \quad d^k = -A^kg^k$ is a descent direction
