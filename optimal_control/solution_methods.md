---
tags: optimal_control
lecture: "5"
---


# Solution Methods

### [[active_set]]

- Switch inequality constraints on/off and solve equality-constrained problem
- Works well if you can guess active set well
- If you guess wrong, check the constraints after the solution.
	- a constraint that should have bee in the active-set but not included in the active set, then it is constraint violation
	- if you put a constraint that should not have been in active-set but you have included in the active-set. then lambda will be negative. pulling rather than pushing. so drop it.

### [[penalty_method]]

- Replace constraints with cost terms that penalize violation: $$\min_x f(x) \;  \text{s.t. } c(x) \geq 0\Rightarrow \min_x f(x) + \frac{\rho}{2}[\min(0,c(x))]^2$$

![[penalty_example.png]]


- Easy to implement
- Has issues with ill-conditioning (have to crank $\rho \to \infty$)
- Can't solve to high accuracy
- " ill-conditioning" $\implies H \implies$   huge spread in eigen values ([[condition_number]]) $\implies$ You will lose $\log_{10}$ of  ([[condition_number]]) of $A$ in $Ax=b$  digits numerically (e.g. $10^5$)
- also, not $C^2$ smooth.
- introduce $\lambda$ in addition to penalty term and you use the penalty value to estimate $\lambda$
- Popular fix: estimate $\lambda$ from penalty at each iteration → converge with finite $\rho$ called "[[augmented_lagrangian_method]]" (also closely related to [[ADMM]])
- -outer/inner loop

[video](https://youtu.be/bsBXk17rff4?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=2105)

### [[interior_point]]/[[barrier_methods]]

- Replace inequalities with barrier function in objective: $$\min_x f(x)  \;  \text{s.t. } x \geq 0 \Rightarrow \min_x f(x) - \rho \log(x)$$ 


![[barrier_example.png]]

- [[barrier_and_penalty_methods]]
- Gold standard for convex problems
- Fast convergence with Newton
- can give real-time guarantees
- Strong theoretical properties
- Used in IPOPT
- naive implementation is ill-conditioned so use Primal-Dual Interior Point Method

## Primal-Dual Interior Point Method

$$\min_x f(x) \:  \text{s.t. } x \geq 0\Rightarrow \min_x f(x) - \rho \log(x)$$ 

First-order necessary condition: $$\frac{\partial f}{\partial x} - \frac{\rho}{x} = 0$$

- This "primal" $1^{st}$ order condition blows up as $x \to 0$
- We can fix this with the "primal-dual trick"
- Introduce new variable $\lambda = \frac{\rho}{x} \Rightarrow x\lambda = \rho$ $$\nabla f - \lambda = 0$$
$$x\lambda = \rho$$
- The second equation is a relaxed complementarity from KKT (switching)
- Converges to exact KKT solution as $\rho \to 0$. We lower gradually as solver converges from $\rho \approx 1$ to $\rho \approx 10^{-6}$

- Note we still need to enforce $x \geq 0$ and $\lambda \geq 0$  (other two KKT condition) (with line search) which might be tricky hence use Log-Domain Interior-Point Method. 

### Intuition: The Primal-Dual "Trick"

The standard barrier gradient $\nabla f - \rho/x = 0$ is numerically unstable because $\rho/x \to \infty$ as $x \to 0$. The "Primal-Dual Trick" stabilizes this by:

1. **Linearization:** Defining $\lambda = \rho/x$ transforms the unstable hyperbolic term into the bilinear constraint $x\lambda = \rho$.
2. **Relaxed KKT:** This system mimics the KKT complementarity condition $x\lambda = 0$, but with a "relaxation" parameter $\rho$. As we anneal $\rho \to 0$, the solution trajectory (Central Path) smoothly converges to the true KKT point without touching the boundary $x=0$.

## Log-Domain Interior-Point Method

- More general case: $$\min_x f(x)$$ $$\text{s.t. } c(x) \geq 0$$
    
- Simplify by introducing a "slack variable": $$\min_{x,s} f(x) \Rightarrow \min_{x,s} f(x) - \rho \log(s)$$ $$\text{s.t. } c(x) - s = 0, s \geq 0 \Rightarrow \text{s.t. } c(x) - s = 0$$
    
- Lagrangian: $$L(x,s,\lambda) = f(x) - \rho \log(s) - \lambda^T(c(x) - s)$$
    
- $1^{}st$ order Conditions: 
- $$\nabla_x L = \nabla f - (\frac{\partial c}{\partial x})^T \lambda = 0$$ $$\nabla_s L = -\frac{\rho}{s} + \lambda = 0 \Rightarrow s \odot \lambda = \rho \text{(relaxed complementary)}$$ 
- $$\nabla_\lambda L = s - c(x) = 0$$
    
- To ensure $s \geq 0$ and $\lambda \geq 0$, introduce change of variables: $$s = \sqrt{\rho}e^\sigma \Rightarrow \lambda = \sqrt{\rho}e^{-\sigma}$$
    
- Now (relaxed) complementarity is always satisfied
    
- Plug back into $1^{st}$ order conditions: 
$$\nabla f - (\frac{\partial c}{\partial x})^T \sqrt{\rho}e^{-\sigma} = 0$$
$$c(x) - \sqrt{\rho}e^\sigma = 0$$
    
- We can solve these with (Gauss) Newton: $$\begin{bmatrix} H & \sqrt{\rho}C^Te^{-\sigma} \\ C & -\sqrt{\rho}e^\sigma \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta \sigma \end{bmatrix} = \begin{bmatrix} -\nabla f + C^T\sqrt{\rho}e^{-\sigma} \\ -c(x) + \sqrt{\rho}e^\sigma \end{bmatrix}$$

### Intuition: Why Log-Domain?

Standard Primal-Dual methods require strictly enforcing $x, \lambda > 0$ (typically via line search), which can be computationally fragile. The Log-Domain formulation removes this burden by construction:

1. **Implicit Positivity:** By parametrizing slack and dual variables as exponentials ($s \propto e^\sigma, \lambda \propto e^{-\sigma}$), they remain strictly positive for any $\sigma \in \mathbb{R}$.
2. **Automatic Complementarity:** The parametrization $s\lambda = (\sqrt{\rho}e^\sigma)(\sqrt{\rho}e^{-\sigma}) \equiv \rho$ satisfies the relaxed KKT condition identically, reducing the system to just the primal and dual residuals.

## Example: Quadratic Program

$$\min_x \frac{1}{2}x^TQx + q^Tx, \quad Q > 0$$ $$\text{s.t. } Ax \geq b$$ $$Cx = d$$

- Super useful in Control
- Can be solved very fast ($\sim$ kHz)