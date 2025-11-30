---
tags: optimization
---

![[trust_region.png]]

[[modified_newton_method]] does quadratic approximates. **But what is the region in which this approximation is valid?** This is called the region of trust. If the approximation is bad, you decrease the size of this region and vice-versa. Mathematically it is the set of all points within euclidean norm $\Delta^k$. i.e. 
$$\implies \ohm^k = {x : \left\| x^{k+1} - x^{k} \right\|} \le \Delta^k$$


$\Delta^k$ decreased or increase based on $\frac{f(x^k) - f(x^{k+1})}{f^k_q(x^k) - f^k_q(x^{k+1})}$ where $f^k_q$ is the quadratic approximation at $x^k$



[video](https://www.youtube.com/watch?v=Xxi8Cro-ssQ&list=PL6EA0722B99332589&index=1)