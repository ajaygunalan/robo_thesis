---
tags: optimization
---

## Conjugate
1. No second order plus no matrix is involved
2. sensitive to [[line_search_techniques]]
3. Need $0(n)$ computation and storage

## Quasi-Newton
1. In addition to finding conjugate, they find them closer to the newton directions near solution. Hence, they are fast.
2. Need $0(n^2)$ computation and storage
3. Robust