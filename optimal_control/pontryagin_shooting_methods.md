---
tags: optimal_control
lecture: "7"
---

## Deterministic Optimal Control

![[control.png]]

### Continuous Time

- **Objective**: $$\min_{X(t), U(t)} J(X(t), U(t)) = \int_{t_0}^{t_f} \ell(X(t), U(t)) dt + \ell_F(X(t_f))$$ where:
    
    - $J(X(t), U(t))$ is the cost function
    - $\ell(X(t), U(t))$ is the "stage cost"
    - $\ell_F(X(t_f))$ is the "terminal cost"
- **Constraints**:
    
    - $\dot{X}(t) = f(X(t), U(t))$ (dynamics constraint)
    - Possibly other constraints
- This is an "infinite-dimensional" optimization problem
- Solutions are open-loop trajectories
- Only a handful of problems have analytic solutions (LQR)
    

### Discrete Time

- **Objective**: $$\min_{X_{1:N}, U_{1:N-1}} J(X_{1:N}, U_{1:N-1}) = \sum_{k=1}^{N-1} \ell(X_k, U_k) + \ell_F(X_N)$$
    
- **Constraints**:
    
    - $X_{k+1} = f(X_k, U_k)$ (dynamics)
    - $U_{min} \leq U_k \leq U_{max}$ ∀ k (torque limits)
    - $c(X_n) \geq 0$ ∀ k (obstacle/safety constraints)
- This is a finite-dimensional problem
- Samples $X_k, U_k$ are often called "knot points" (splines)
- Continuous → discrete uses integration (e.g., Runge-Kutta)
- Discrete → continuous using interpolation
    

## Pontryagin's Minimum Principle
![[shooting_method.png]]

- Also called "Maximum Principle" if maximizing a reward
- First-order necessary conditions for a deterministic optimal control problem
- In discrete time, special case of KKT conditions

### Formulation

Given: $$\min_{X_{1:N}, U_{1:N-1}} \sum_{k=1}^{N-1} \ell(X_k, U_k) + \ell_F(X_N)$$

Subject to: $$X_{k+1} = f(X_k, U_k)$$

We can form the Lagrangian: $$L = \sum_{k=1}^{N-1} \ell(X_k, U_k) + \lambda_{k+1}^T (f(X_k, U_k) - X_{k+1}) + \ell_F(X_N)$$

- This result is usually stated in terms of the **Hamiltonian system** which is the dual of the Lagrangian.

 $$H(X, U, \lambda) = \ell(X, U) + \lambda^T f(X, U)$$

Plugging the Hamiltonian into the Lagrangian: $$L = H(X_1, U_1, \lambda_2) + \left[\sum_{k=2}^{N-1} H(X_k, U_k, \lambda_{k+1}) - \lambda_k^T X_k \right] + \ell_F(X_N) - \lambda_N^T X_N$$

index manipulation is integration by parts,

Taking derivatives with respect to $X$ and $\lambda$:

$$\frac{\partial L}{\partial \lambda_k} = \frac{\partial H}{\partial \lambda_k} - X_{k+1} = f(X_k, U_k) - X_{k+1} = 0$$

$$\frac{\partial L}{\partial X_k} = \frac{\partial H}{\partial X_k} - \lambda_k^T = \frac{\partial \ell}{\partial X_k} + \lambda_{k+1}^T \frac{\partial f}{\partial X_k} - \lambda_k^T = 0$$

$$\frac{\partial L}{\partial X_N} = \frac{\partial \ell_F}{\partial X_N} - \lambda_N^T = 0$$

For $U$, we write the minimization explicitly to handle torque limits: $$U_k = \arg\min_U H(X_k, U, \lambda_{k+1})$$ $$\text{s.t. } U \in \mathcal{U}$$

where $\mathcal{U}$ is shorthand for "in feasible set" (e.g., $U_{min} \leq U \leq U_{maX}$)

### Summary (Discrete Time)

$$X_{k+1} = \nabla_\lambda H(X_k, U_k, \lambda_{k+1})$$ 
$$\lambda_k = \nabla_X H(X_k, U_k, \lambda_{k+1})$$ 
$$U_k = \arg\min_U H(X_k, U, \lambda_{k+1})$$ 
$$\text{s.t. } U \in \mathcal{U}$$ $$\lambda_N = \frac{\partial \ell_F}{\partial X_N}$$

[this is related to backpropagataion](https://youtu.be/ZoLmQB6C7WU?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=2694)

### Continuous Time Equivalent

$$\dot{X} = \nabla_\lambda H(X, U, \lambda)$$ 
$$-\dot{\lambda} = \nabla_X H(X, U, \lambda)$$ 
$$U = \arg\min_{\tilde{U}} H(X, \tilde{U}, \lambda)$$
$$\text{s.t. } \tilde{U} \in \mathcal{U}$$ 
$$\lambda(t_F) = \frac{\partial \ell_F}{\partial X}$$



Neural ODE or Continuous Network 


He's talking about how the first two equations in Pontryagin's minimum principle, when written in continuous time, look very similar to what we find in Hamiltonian mechanics in physics.

Specifically:

- $\dot{x} = \nabla_\lambda H(x, u, \lambda)$ — time evolution of the state $x$
- $\dot{\lambda} = -\nabla_x H(x, u, \lambda)$ — time evolution of the costate $\lambda$

In physics, the Hamiltonian is written in terms of **generalized coordinates** $q$ and **conjugate momenta** $p$:

$$H(q, p) = T(q, p) + V(q)$$

where $T$ is kinetic energy and $V$ is potential energy.

The Lagrange multipliers $\lambda$ in control theory are analogous to the **conjugate momenta** $p$ in physics. Momentum in physics is a Lagrange multiplier associated with the kinematic constraints of the system.

This connection is not always immediately obvious, but it shows how fundamental the concepts of Lagrange multipliers and optimization are, appearing in both control theory and classical mechanics.
[connection to physics
](https://youtu.be/ZoLmQB6C7WU?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=2797)

## Notes on Control Methods

- Historically, many algorithms were based on integrating ODEs forward and backward to perform gradient descent
- These are called "indirect" and/or "shooting" methods
- In continuous time, $\lambda(t)$ is called the "costate" trajectory
- These methods have largely fallen out of favor due to vanishing/exploding gradients as computers have improved


## LQR Problem

- **Objective**: $$\min_{x_{1:N} \; u_{1:N-1}} J = \sum_{k=1}^{N-1} \frac{1}{2}X_k^T Q_k X_k + \frac{1}{2}U_k^T R_k U_k + \frac{1}{2}X_N^T Q_N X_N$$
    
- **Constraints**:
    
    - $X_{k+1} = A_k X_k + B_k U_k$
    - $Q \geq 0$, $R > 0$
- Can (locally) approximate many nonlinear problems
- Computationally tractable
- Many extensions (e.g., infinite horizon, stochastic, etc.) 
- "Time invariant" if $A_k = A$, $B_k = B$, $Q_k = Q$, $R_k = R$ ∀ $k$ (Time varying) otherwise

### LQR with Indirect Shooting

$$X_{k+1} = \nabla_\lambda H(X_k, U_k, \lambda_{k+1}) = AX_k + B U_k$$ $$\lambda_k = \nabla_X H(X_k, U_k, \lambda_{K+1}) = QX_k + A^T \lambda_{K+1}$$ $$\lambda_N = Q_N X_N$$ 
$$U_k = \nabla_u H(X_k, U_k, \lambda_{k+1}) = 0 \Rightarrow -R^{-1}B^T \lambda_{k+1}$$

#### Procedure

1. Start with initial guess $U_{1:N-1}$
2. Simulate/rollout to get $X_{1:N}$
3. Backward pass to get $\lambda$, $\Delta u$
4. Rollout with line search on $\Delta u$
5. Go to 3 until convergence

#### Why Indirect Shooting Fell Out of Favor

Indirect shooting (forward–backward integration with gradient descent on controls) is numerically fragile compared to modern methods:

**Problems with the approach:**
- Inherits classic gradient descent pathologies: vanishing/exploding gradients over long horizons ("tail wagging the dog"), slow convergence, and sensitivity to step size
- As horizon increases, iterations explode and convergence becomes unreliable—doubling the horizon already causes significant slowdown, and longer horizons "really struggle and blow up"
- Constraints (input bounds, collision avoidance) are difficult to enforce cleanly within indirect formulations

**What replaced it:**
- Modern compute enables posing optimal control as finite-dimensional nonlinear programs solved with second-order / Newton-type methods (SQP, direct collocation, DDP, iLQR)
- These direct methods are better conditioned, scale better, handle constraints naturally, and avoid the worst numerical pathologies of indirect shooting
- Indirect LQR now serves primarily as a historical/pedagogical tool

## Example: Double Integrator

- System dynamics: $$\dot{X} = \begin{bmatrix} \dot{q} \\ \ddot{q} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} q \\ \dot{q} \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u$$
    
    where:
    
    - $q$ is position
    - $\dot{q}$ is velocity
    - $u$ is force/acceleration
- Think of this as a brick sliding on ice (no friction)
    
- Discrete time dynamics: $$X_{n+1} = \begin{bmatrix} 1 & h \\ 0 & 1 \end{bmatrix} \begin{bmatrix} q_n \\ \dot{q}_n \end{bmatrix} + \begin{bmatrix} \frac{1}{2}h^2 \\ h \end{bmatrix} u_n$$
    
    where $h$ is the time step