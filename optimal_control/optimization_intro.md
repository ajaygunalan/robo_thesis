---
tags: optimal_control
lecture: 3, 4, 5
---

# Root Finding and Minimization

### Notation

- Given $f(x) : \mathbb{R}^n \rightarrow \mathbb{R}$
- $\frac{\partial f}{\partial x} \in \mathbb{R}^{1 \times n}$ is a row vector $\implies [a_1 \; a_2 ... \; a_n] \implies$ chain rule works 
- That's because $\frac{\partial f}{\partial x}$ is the linear operator mapping $\Delta x$ into $\Delta f$: 
$$f(x + \Delta x) \approx f(x) + \frac{\partial f}{\partial x} \Delta x$$
- Similarly $g(y) : \mathbb{R}^m \rightarrow \mathbb{R}^n$ 
$$\frac{\partial g}{\partial y} \in \mathbb{R}^{n \times m}$$ because: $$g(y + \Delta y) \approx g(y) + \frac{\partial g}{\partial y} \Delta y$$
- These conventions make the chain rule work: $f(g(y + \Delta y)) \approx f(g(y)) + \frac{\partial f}{\partial x}|_{g(y)} \frac{\partial g}{\partial y}|_y \Delta y$

#### Convenient Definitions

- $\nabla f(x) = (\frac{\partial f}{\partial x})^T \in \mathbb{R}^{n \times 1}$ (column vector)
- $\nabla^2 f(x) = \frac{\partial}{\partial x}(\nabla f(x)) \approx \frac{\partial^2 f}{\partial x^2} \in \mathbb{R}^{n \times n}$
- $f(x + \Delta x) \approx f(x) + \frac{\partial f}{\partial x}\Delta x + \frac{1}{2}\Delta x^T \frac{\partial^2 f}{\partial x^2}\Delta x$

### Root Finding

- Given $f(x)$, find $x^*$ such that $f(x^*) = 0$
- Example: equilibrium of a continuous-time dynamics
- Closely related: fixed point $f(x^*) = x^*$ (equilibrium of discrete-time dynamics)

#### Fixed-Point Iteration
- I didn't understand this, so I'm skipping this
- Simplest solution method
- If fixed point is stable, just "iterate the dynamics" until it converges
- Only works if $x^*$ is a stable equilibrium point and if initial guess is in the basin of attraction
- Can converge slowly (depends on $f$)
- gradient descent is fixed point iteration applied to the gradient of our model $f$
-  $O(n)$

#### Newton's Method

- Fit a linear approximation to $f(x)$: $f(x + \Delta x) \approx f(x) + \frac{\partial f}{\partial x}|_x \Delta x$
- Set approximation to zero and solve for $\Delta x$: 
$$f(x) + \frac{\partial f}{\partial x}\Delta x = 0 \Rightarrow \Delta x = -(\frac{\partial f}{\partial x})^{-1}f(x)$$
- Apply correction: $x \leftarrow x + \Delta x$
- Repeat until convergence

#### Example: Backward Euler

- $f(x_{k+1}, x_k, u_k) = 0$ (implicit dynamics)
- $x_{k+1} = x_k + hf(x_{k+1})$ (evaluate $f$ at future time)
- $\Rightarrow f(x_{k+1}, x_k, u_k) = x_{k+1} - x_k - hf(x_{k+1}) = 0$
- implicit dynamics better stability 
- Very fast convergence with Newton (Quadratic)
- Can get machine precision
- Most expensive part is solving a linear system $O(n^3)$ which is inverting Hessian.
- Can improve complexity by taking advantage of problem structure/sparsity
- Quasi newton $O(n^2)$

## Minimization

$$\underset{x}{\min} f(x) \quad f(x):\mathbb{R}^n \rightarrow \mathbb{R}$$
- If $f$ is smooth, $\frac{\partial f}{\partial x}|_{x^*} = 0$ at a local minimum
- Now we have a root-finding problem $\nabla f(x) = 0$
$\implies$ Apply Newton!

$$\nabla f(x + \Delta x) \approx \nabla f(x) + \underbrace{\frac{\partial}{\partial x}(\nabla f(x))}_{\nabla^2 f}\Delta x = 0$$
$$\Rightarrow \Delta x = -(\nabla^2 f(x))^{-1}\nabla f(x)$$ 
$$x \leftarrow x + \Delta x$$
- Repeat until convergence

### Intuition

- Fit a quadratic approximation to $f(x)$
- Exactly minimize approximation

#### Example

- $\underset{x}{\min} f(x) = x^4 + x^3 - x^2 - x$
- Starting points: 1.0, -1.5, 0 (0 maximizes!)
- [video](https://youtu.be/f7yF0KOV-sI?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=2609)

## Take-away Messages

- Newton is a local root-finding method
- Will converge to the closest fixed point to the initial guess (min, max, saddle)

### Sufficient Conditions

- $\nabla f = 0$ is a "first-order necessary condition" for a minimum. Not a sufficient condition.
- Looking at scalar case: $\Delta x = -(\nabla^2 f)^{-1}(\nabla f)$
    - $\nabla^2 f > 0 \Rightarrow$ descent (minimization)
    - $\nabla^2 f < 0 \Rightarrow$ ascent (maximization)
- In $\mathbb{R}^n$, $\nabla^2 f > 0$, $\nabla^2 f \in S_{++}^n$ (positive definite) $\Rightarrow$ descent
- If $\nabla^2 f > 0$ everywhere (∀x) $\Rightarrow$ $f(x)$ is strongly convex $\Rightarrow$ Can always solve with Newton
- Usually not the case for hard/nonlinear problems

## Regularization

- Practical solution to ensure minimization:
- $H \leftarrow \nabla^2 f$
- while $H  \cancel{>}  0$
	- $H \leftarrow H + \beta I \quad (\beta > 0)$
- end
- $\Delta x = -H^{-1}\nabla f$
- $x \leftarrow x + \Delta x$

- Also called "damped Newton" (shrinks steps)
- Guarantees descent
- Regularization makes sure we minimize
- Consider overshoot as a potential issue


# Optimization Methods

## Line Search

- Often $\Delta x$ step from Newton overshoots the minimum
- To fix this, check $f(x + \Delta x)$and **backtrack** until we get a "good" reduction
- Many strategies available

### Armijo Rule

A simple and effective line search strategy:

- $\alpha = 1$
- while $f(x+\alpha\Delta x) > f(x) + b\underbrace{\alpha\nabla f(x)^T\Delta x}_{\text{Expected reduction from 1st order taylor linearization}}$
	- $\alpha \leftarrow c\alpha$ (where $c$ is a scalar $< 1$)
- end

[[armijo]] uses first order Taylor expansion
[[wolfe]] uses second order Taylor expansion
cubic line search for third order Taylor expansion

 b: tolerance parameter


### Intuition
- easily parallelizable
- Make sure step agrees with linearization within some tolerance $b$

### Typical Values

- c = 1/2
- b = 10⁻⁴ ~ 0.1

### Key Takeaway

- Newton with simple + cheap modifications ("globalization strategies") is extremely effective at finding local optima

## Equality Constrained Minimization

### Problem Formulation

$$\underset{x}{\min} f(x) \quad f(x):\mathbb{R}^n \rightarrow \mathbb{R}$$
s.t. $C(x) = 0  \quad C(x):\mathbb{R}^n \rightarrow \mathbb{R^m}$


### First-Order Necessary Conditions

1. Need $\nabla f(x) = 0$ in free directions. Non-free directions you can't move so gradients need not be zero.
2. Need $C(x) = 0$

![[grad_f_constraints.png]]

### Lagrangian Approach

- Any non-zero component of $\nabla f$ must be normal to the constraint at an optimum. Equivalently, $\nabla f$  must be parallel to $\nabla C$ 
$$ \implies \nabla f + \lambda \nabla C = 0$$
$\lambda$ is the Lagrange multiplier ("dual variable")


### General Form

$$\frac{\partial f}{\partial x} + \lambda^T\frac{\partial C}{\partial x} = 0, \lambda \in \mathbb{R}^m$$

###  Lagrangian 
$$L(x,\lambda) = f(x) + \lambda^T C(x)$$

### Optimality Conditions via Lagrangian

$$\nabla_x L(x,\lambda) = \nabla f + \left(\frac{\partial C}{\partial x}\right)^T\lambda = 0$$
$$\nabla_\lambda L(x,\lambda) = C(x) = 0$$

### Newton's Method for Solving KKT System

$$\nabla_x L(x+\Delta x, \lambda+\Delta \lambda) \approx \nabla_x L(x,\lambda) + \frac{\partial^2 L}{\partial x^2}\Delta x + \underbrace{\frac{\partial^2 L}{\partial x \partial \lambda}}_{(\frac{\partial C}{\partial X})^T}\Delta \lambda = 0$$
$$\nabla_\lambda L(x+\Delta x, \lambda+\Delta \lambda) \approx C(x) + \frac{\partial C}{\partial x}\Delta x = 0$$

### KKT System

$$ 
\begin{bmatrix} 
	\frac{\partial^2 L}{\partial x^2} & \left(\frac{\partial C}{\partial x}\right)^T \\
	\frac{\partial C}{\partial x} & 0 
\end{bmatrix} 
\begin{bmatrix} 
	\Delta x \\ 
	\Delta \lambda 
\end{bmatrix}
= 
\begin{bmatrix}
	-\nabla_x L(x,\lambda) \\ 
	-C(x) 
\end{bmatrix}
$$

## Gauss-Newton Method

$$\frac{\partial^2 L}{\partial x^2} = \nabla^2 f +  \underbrace{\frac{\partial}{\partial x}\left[\left(\frac{\partial C}{\partial x}\right)^T\lambda\right]}_{\text{computationally expensive}}$$


- We often drop the 2nd **constraint curvature** term
- Slightly slower convergence than full Newton (more iterations) but iterations are cheaper. Often wins in wall-clock time
- check this [code](https://github.com/Optimal-Control-16-745/lecture-notebooks/blob/main/Lecture%204/equality-constraints.ipynb), if you don't understand.


### Key Takeaways

Excellent [Example](https://youtu.be/lIuPIlDxLNU?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=3084) of Why Full Newton gets stuck Gauss-Newton doesn't.  Basically $\frac{\partial^2 L}{\partial x^2}$ might become in-definite due to  constraint curvature,  even if $\nabla^2 f > 0$. Hence we need to **regularize**. Thus second-term won't help that's why  Gauss-Newton is often used in practice

## Inequality Constraints

### Problem Formulation

$$  \min_x  f(x) $$
$$ C(x) \geq 0 $$



![[inequa_cons.png]]

### First-Order Necessary Conditions

1. $\nabla f = 0$ in the free directions
2. $C(x) \geq 0$

### KKT Conditions

$$\nabla f - \left(\frac{\partial C}{\partial x}\right)^T\lambda = 0 \leftarrow \text{"stationarity"}$$
$$C(x) \geq 0 \leftarrow \text{"primal feasibility"}$$
$$\lambda \geq 0 \leftarrow \text{"dual feasibility"}$$
$$\lambda \odot C(x) = \lambda^T C(x) = 0 \leftarrow \text{"complementarity"}$$

In the interior $C(x) > 0$, it looks like an unconstrained problem hence, you want $\lambda = 0$ (in-active constraint). When you hit the constraint $C(x) = 0$, it becomes a equality problem. (active problem) hence, you want $\lambda > 0$. This switching of whether $\lambda$  or $C(x)$ is zero is the complementary conditions.


In case of equality constraint, the sign of $\lambda$ (push/pull) doesn't matter.  Where in In-equality constraint, you only want push of the constraint and not pull. 