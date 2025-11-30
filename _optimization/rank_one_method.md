---
tags: optimization
---

$$B^{k+1} = B^k +\alpha uu^T$$
$$B^{k+1} = B^k + \frac{ZZ^T}{Z^T\gamma^k}$$ 
where $Z=\delta^k-B^k\gamma^k$$

## Difficulties in rank one
1. $B^{k+1}$ is positive definite, if $Z^T\gamma^k > 0$ which can't be guaranteed for every $k$
2. Numerical difficulties if $Z^T\gamma^k \approx 0$