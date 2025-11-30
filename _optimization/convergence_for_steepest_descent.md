---
tags: optimization
---

$$\min f(x) \overset{\text{def}}{=}\frac{1}{2} x^THx - c^Tx$$

where $H$ is a symmetric positive definite matrix.

Convergence depends upon the [[condition_number]] of the Hessian matrix $H$.
	- For circular contours (1 iteration)
	- For elliptical takes more iterations depends upon starting point.

![[steepest_descent_elliptical_convergence.png]]

