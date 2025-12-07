---
tags: optimal_control
lecture: "6"
---



## Duality & Regularization

### Equality Constraints

- **Problem Formulation**: $$\begin{align} \min_x f(x) \ \text{s.t. } c(x) = 0 \end{align}$$
    
- **We can theoretically turn this into**: $$\min_x f(x) + P_\infty(c(x))$$
    
    where $$P_\infty(c(x)) = \begin{cases} 0, & c(x) = 0 \\ +\infty, & c(x) \neq 0 \end{cases}$$
    
_Practically terrible approach_ (log barrier is $\approx$ the above smoothly), but we can get the same effect by solving (primal-dula trick):

$$\min_x \max_\lambda f(x) + \lambda^T c(x)$$
- the above eqn is equivalent to the $\min_x f(x) + P_\infty(c(x))$
- Whenever $c(x) \neq 0$, inner problem blows up

### Inequality Constraints

- **Problem Formulation**: $$\begin{align} \min_x f(x) \ \text{s.t. } c(x) \geq 0 \end{align}$$
    
- **Transformation**: $$\min_x f(x) + P_\infty^-(c(x))$$
    
    where $$P_\infty^- = \begin{cases} 0, & c(x) \geq 0 \\ +\infty, & c(x) < 0 \end{cases}$$
    
- **Saddle Point Formulation**: $$\min_x \max_{\lambda \geq 0} f(x) - \lambda^T c(x)$$
    
    - When $c(x) <0$, inner problem blows up

### KKT Interpretation

- KKT conditions define a saddle point in $(x,\lambda)$
- $\implies$ gradient descent on $x$ and ascent on $\lambda$
- $\implies$ $\min$ w.r.t. $x$ and $\max$ w.r.t. $\lambda$ $\implies$ saddle point
- KKT system should have $\dim(x)$ positive eigenvalues and $\dim(\lambda)$ negative eigenvalues at optimum → called **quasi-definite**

**Regularization:** If the Hessian has wrong inertia (non-convex problem), add $\beta I$ to force correct eigenvalue structure:

$$\begin{bmatrix} H+\color{green}{\beta I} & C^T \\ C & -\color{red}{\beta I} \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta \lambda \end{bmatrix} = \begin{bmatrix} -\nabla_x L \\ -c(x) \end{bmatrix}$$
where $\beta > 0$

- Systems still overshoot → need **globalization** (line search / trust region)

---

## From Direction to Step Size (Globalization)

Regularization gives us an invertible system and a descent direction $\Delta x$. But Newton is a *local* method—a full step ($\alpha=1$) may be invalid.

**The conflict in constrained problems:** A step might decrease $f(x)$ but increase $\|c(x)\|$. We need a single scalar to arbitrate → **merit function**.

---

## Merit Functions

How do we do a [[line_search_techniques]] on a root-finding problem?

Find $x^*$ s.t. $c(x^*) = 0$
- Define scalar "merit function" $P(x)$ to measure distance to solution
- The merit function wraps the residual into a single scalar we can minimize

### Standard Merit Function Choices

- $P(x) = \frac{1}{2}c(x)^T c(x) = \frac{1}{2}||c(x)||_2^2$
- $P(x) = ||c(x)||_1$ (any norm works)

### Armijo Line Search on Merit Function

- $\alpha = 1$
- while  $P(x+\alpha \Delta x) > P(x) + b\alpha\nabla P(x)^T \Delta x$
	- $\alpha \leftarrow \theta\alpha$
- end
- $x \leftarrow x + \alpha\Delta x$

$b$ is tolerance, $\alpha$ is step length

---

## Constrained Optimization

In optimal control, we rarely solve just $c(x)=0$. The merit function must balance three competing concerns:

1. **Objective decrease** — is $f(x)$ getting smaller?
2. **Inequality feasibility** — is $c(x) \geq 0$ satisfied?
3. **Equality feasibility** — is $d(x) = 0$ satisfied?

### Problem Formulation

$$\begin{align} \min_x f(x) \ \text{s.t. } c(x) \geq 0 \ d(x) = 0 \end{align}$$

### Lagrangian

$$L(x,\lambda,\mu) = f(x) - \lambda^T c(x) + \mu^T d(x)$$

### Merit Function Options

1. KKT Residual approach: $$P(x,\lambda,\mu) = \frac{1}{2}||r_{KKT}(x,\lambda,\mu)||_2^2$$
    
    Where $r_{KKT}(x,\lambda,\mu)$ is the vector: $$\begin{bmatrix} \nabla_x L \\ \min(0,c(x)) \\ d(x) \end{bmatrix}$$
    
2. Penalty approach: $$P(x,\lambda,\mu) = f(x) + \rho\left\|\begin{bmatrix}\min(0,c(x)) \\ d(x)\end{bmatrix}\right\|_1$$
    
    Where $\rho$ is a scalar weight parameter

### Maratos Effect & Second-Order Corrections

- **Maratos Effect:** Occurs when the **penalty weight** $\rho$ in the merit function is set too high. This causes excessive **backtracking** during line search, resulting in **slow convergence**—even when the Newton step is valid.

- **Second-Order Corrections:** To overcome the Maratos effect, evaluate the constraint at the new step location $c(x + \Delta x)$ and solve the linear system again. This extra step is relatively cheap and recovers fast local convergence.

### References

1. [Numerical Optimization](https://www.math.uci.edu/~qnie/Publications/NumericalOptimization.pdf)
2. [Convex Optimization – Boyd and Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)