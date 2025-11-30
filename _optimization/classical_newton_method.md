---
tags: optimization
---

[[ellipse_into_circular_contour]]


In this method ($d^k = -(H^k)^{-1}g^k$) At each point, we replace the function locally with a convex quadratic function and solve it in one step. Then, we go to the next point. This Provides smooth convergence, less sensitivity to start point compared to [[steepest_descent_method]], we replace each point with a line (first-order Taylor series).


### Downsides
1. Requires $O(n^3)$ computational effort for every iteration
2. Requires $O(n^2)$ memory for every iteration
3. No guarantee that $d^k$ is a descent direction
4. Sometimes $H^k$ may be [[singular]] $\implies$ difficulty in inverting numerically.
5. No guarantee that $f (x^{k+1}) < f (x^k)$ (no line search) $\implies \alpha^k = 1$
6. Sensitive to initial point for non-quadratic functions
7. Locally convergent with order of convergence two
8. Initialization of $x^0$ requires knowledge of $x^*$! ^6dd2f7
 
 
 [video](https://www.youtube.com/watch?v=QnLvBNp8gkg&list=PL6EA0722B99332589&index=14)