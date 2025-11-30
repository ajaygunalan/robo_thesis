---
tags: optimization
---

In [[classical_newton_method]], ![[classical_newton_method#^6dd2f7]] not practical, and $H^k$ may not be positive definite or close to singular (not invertible). Hence, for $\delta >0$, Find the smallest $\zeta_k \ge 0$ s.t. smallest eigenvalue of $H^K + \zeta_kI >  \delta$. This ensures $H^K + \zeta_k$  is positive definite. Also, use [[line_search_techniques]] This is known as the **Modified Newton Method**: $d^k = -(H^k + \zeta_kI)^{-1}g^k$. 

When $\zeta^k$ is very high, it behaves like the Steepest descent, and when it is low, it's a classical newton (quadratic) approximation. **How you get $\zeta_k$ ?**: start with reasonable value of $\zeta_k$ and if [[cholesky]] factorization of $(H^k + \zeta_kI)$ is positive definite, stop, else double and check again by [[cholesky]]. **Convergence**: global convergence (no restriction on $x^0$) and has order of convergence = 2.   



[video](https://www.youtube.com/watch?v=Xxi8Cro-ssQ&list=PL6EA0722B99332589&index=1)

