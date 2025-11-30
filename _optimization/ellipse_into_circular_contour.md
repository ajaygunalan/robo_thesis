---
tags: optimization
---

![[cholesky.png]]

$$ \min f(x) \stackrel{\text{def}}{=} \frac{1}{2}x^THx - c^Tx $$


$H = L L^T$ is [[cholesky]] decomposition and define $y = L^Tx$

after algebraic rank, we will get $x^{k+1} = x^k - H^{-1}\nabla f(x^k)$ which is the [[classical_newton_method]]

