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
    
    where $h$ is the time step---
tags: optimal_control
lecture: "8"
---

# Linear Quadratic Regulator (LQR)

## Previous Lecture Recap

- Deterministic Optimal Control
- Pontyagin's Maximum Principle
- Indirect (Single) Shooting Method

## Today's Topics

- LQR Problem
- LQR as a Quadratic Program (QP)
- Riccati Recursion

## LQR Problem

The Linear Quadratic Regulator problem can be formulated as:

$$\min_{X_{1:N} \\ U_{1:N-1}} J = \sum_{k=1}^{N-1} \frac{1}{2} X_k^T Q_k X_k + \frac{1}{2} U_k^T R_k U_k + \frac{1}{2} X_N^T Q_N X_N$$

Subject to: $$X_{k+1} = A_k X_k + B_k U_k$$

Where:

- $Q_k \geq 0$ (positive semi-definite)
- $R_k > 0$ (positive definite)

### Example: Double Integrator

![[double_integrator.png]]

Consider a system representing a brick sliding on ice (no friction):

$$\dot{X} = \begin{bmatrix} \dot{q} \\ \ddot{q} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} q \\ \dot{q} \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u$$

Where:

- $q$ is position
- $\dot{q}$ is velocity
- $\ddot{q}$ is acceleration
- $u$ is force (control input)

Discretized system: $$X_{k+1} = \begin{bmatrix} 1 & h \\ 0 & 1 \end{bmatrix} \begin{bmatrix} q_k \\ \dot{q_k} \end{bmatrix}  + \begin{bmatrix} \frac{1}{2}h^2 \\ h \end{bmatrix} u_k$$

 $$X_{k+1} = AX_k + Bu_k$$
Where $h$ is the time step.

## LQR as a Quadratic Program (QP)

### Reformulation as Standard QP

Assuming $X_1$ (initial state) is given (not a decision variable):

1. Define decision vector: $$z = \begin{bmatrix} U_1 \\ X_2 \\ U_2 \\ X_3 \\ \vdots \\ X_N \end{bmatrix}$$
    
2. Define Hessian matrix: $$H = \begin{bmatrix} R_1 & & & \\ & Q_2 & & \\ & & R_2 & \\ & & & \ddots \\ & & & & Q_N \end{bmatrix}$$
    
    Such that $J = \frac{1}{2} z^T H z$
    
3. Define constraint matrices $C$ and $d$: $$\begin{bmatrix} B_1 & -I & 0 && \cdots & 0 \\ 0 & A_2 & B_2 & -I & \cdots & 0 \\ \vdots & & \ddots & & \\ 0 & \cdots & 0 & A_{N-1} & B_{N-1} & -I \end{bmatrix} \begin{bmatrix} U_1 \\ X_2 \\ U_2 \\ \vdots \\ X_N \end{bmatrix} = \begin{bmatrix} -A_1X_1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}$$
    
    $$Cz = d$$
    

### Standard QP Formulation

Now we can write the LQR problem as a standard QP:

$$\min_z \frac{1}{2} z^T H z$$ $$\text{s.t. } C z = d$$


### Lagrangian and KKT Conditions

The Lagrangian of this QP is: $$L(z, \lambda) = \frac{1}{2} z^T H z + \lambda^T [C z - d]$$

KKT Conditions: $$\nabla_z L = H z + C^T \lambda = 0$$ $$\nabla_\lambda L = C z - d = 0$$

Which gives the linear system: $$\begin{bmatrix} H & C^T \\ C & 0 \end{bmatrix} \begin{bmatrix} z \\ \lambda \end{bmatrix} = \begin{bmatrix} 0 \\ d \end{bmatrix}$$

We get the exact solution by solving one linear system!

**Note**: This approach is much better than shooting methods!

## A Closer Look at the LQR QP

The KKT system for LQR is very sparse (lots of zeros) and has lots of structure:

![[lqr_structure.png]]


## Riccati Recursion

![[riccati_recursion.png]]

From our analysis, we have a recursion for $K$ and $P$:

$$P_N = Q_N$$ 
$$K_k = (R + B^T P_{k+1} B_n)^{-1} B_n^T P_{k+1} A_n$$ 
$$P_k = Q + A^T P_{k+1} (A_n - B K_k)$$

This is called the Riccati equation/recursion.

We can solve the QP by doing a backward Riccati pass (k, p, u) followed by a forward rollout (x) to compute $X_{1:N}$ and $U_{1:N-1}$.

### Computational Complexity

- General (dense) QP has complexity $O([N(n+m)]^3)$, where:
    - $N$ is the horizon length
    - $n$ is the state dimension
    - $m$ is the control dimension
- Riccati solution is $O(N(n+m)^3) \implies$  linear in time horizon

### Advantages of Riccati Solution

- Riccati exactly matches QP solution
- Feedback policy allows us to:
    - Change initial state $x_0$
    - Reject noise/disturbances

## Infinite-Horizon LQR

![[infinite_lqr.png]]

For time-invariant LQR systems converge to constants: 

For stabilization problems, we typically use the constant gain matrix $K$.


The backward recursion for $P$ becomes:

$$K_k = (R + B^T P_{k+1} B)^{-1} B^T P_{k+1} A$$ 
$$P_k = Q + A^T P_{k+1} (A + B K_k)$$

In the infinite-horizon limit: $$P_{k+1} = P_k = P_{\infty}$$

This can be solved as a root-finding/fixed-point problem.

**Note**: Programming languages like Julia, MATLAB, and Python provide a "dare" (Discrete Algebraic Riccati Equation) function that does this for you.---
tags: optimal_control
lecture: "9"
---
### Last Time:
- LQR via Shooting
- LQR as a QP
- LQR via Riccati
- Infinite Horizon LQR

### Today:
- Controllability
- Dynamic Programming

## Duality & Regularization

## Controllability
![[controllability.jpg]]

![[underactuate_vs_fully_acutuated.jpg]]
![[underactuate_vs_fully_acutuated_math.jpg]]
### How do we know if LQR will work?

- We already know Q ≥ 0, R > 0
- For the time-invariant case, there is a simple answer. (not for time variant)

For any initial state $X_0$, $X_N$ is given by: 
$$X_N = AX_{N-1} + BU_{N-1}$$ 
$$= A(AX_{N-2} + BU_{N-2}) + BU_{N-1}$$ 
$$= A^N X_0 + A^{N-1}BU_0 + A^{N-2}BU_1 + ... + BU_{N-1}$$

$\color{red}{A^N}$ $\implies \infty$ if the system is open-loop unstable, the eigen values are about the circle of $|r| = 1$ hence, numerically you cant do $A^N$.

$$= \underbrace{[B \ AB \ A^2B \ ... \ A^{N-1}B]}_{C} \begin{bmatrix} U_{N-1} \\ U_{N-2} \\ \vdots \\ U_0 \end{bmatrix} + A^N X_0$$

$C$ is big fat matrix, hence under-determined , hence solution is least square.

Without loss of generality, we solve for $X_N = 0$

This is equivalent to a least-squares problem for $U_{0:N-1}$:

$$\begin{bmatrix} U_{N-1} \\ U_{N-2} \\ \vdots \\ U_0 \end{bmatrix} = 
\underbrace{[C^T(CC^T)^{-1}]}_{Pesudo-Inverse}(X_N - A^N X_0)$$

To solve this least-square problem don't use the [[Pseudo Inverse]] cuz $C*C$ the [[condition number]] gets doubled which is bad. Don't use [[subjects/Linear Algebra/SVD]] cuz of computational  load. Use [[QR]] factorization for least-square. avoids squaring.  

The controllability [[Gramian]] for discrete-time LTI systems equals $C·C^T$, where $C$ is the controllability matrix. It determines system controllability by its rank

For $CC^T$ to be invertible $\implies \text{rank}(C) = n$, where $n = \text{dim}(X)$


So, far its both for LTI and LTV, Now for LTI,  I can stop at $n$ time steps in $C$ because the Cayley-Hamilton theorem says that $A^N$ can be written in terms of a linear combination of lower powers of $A$ up to $n$:

$$A^N = \sum_{k=0}^{n-1} \alpha_k A^k \quad \text{(for some } \alpha_k \text{)}$$

Therefore adding more time steps/columns to $C$ can't increase the rank.

$$\Rightarrow C = \underbrace{[B \ AB \ ... \ A^{n-1}B]}_{\text{Controllability Matrix}}$$


A fully actuated system has as many independent actuators as degrees of freedom, which is reflected in a full-rank B matrix. This means that each control input affects a distinct component of the system’s state, enabling instantaneous, independent control over all degrees of freedom. In contrast, an underactuated system has fewer actuators than degrees of freedom, resulting in a B matrix that is not full rank and therefore exhibits some linear dependencies among the inputs. While such systems cannot control all states instantaneously, they can still be controllable over time. By examining the full controllability matrix—which incorporates both the system’s dynamics (the A matrix) and the control input matrix (B)—one can determine if the system can be driven to any desired state via dynamic coupling. The **controllability index** further quantifies this by specifying the minimum number of time steps required to achieve full control despite underactuation.


## Bellman's Principle

- Optimal control problems have an inherently sequential structure
- Past control inputs can only affect future states. Future inputs can't affect past states
- Bellman's Principle ("Principle of Optimality") formalizes this

![[bellman_principle_optimality_trajectory.png]]


- Sub-trajectories of optimal trajectories have to be optimal for the appropriately defined sub-problem

Bellman's principle of optimality states that an optimal solution to a problem is made up of optimal solutions to its subproblems. To test this, you can shorten the time horizon from the start ("head")—if the trajectory remains optimal, the principle holds. However, shortening from the end ("tail") may remove important terminal conditions, potentially breaking optimality.

## Dynamic Programming
![[dp.jpg]]

- Bellman's Principle suggests starting from the end of the trajectory and working backwards
- We've already seen this with Riccati & Pontryagin
- Define "optimal cost-to-go" aka "value function" $V_k(X)$
- Encodes cost incurred starting from state $X$ at time $k$ if we act optimally

### For LQR

$$V_N(X) = \frac{1}{2}X^T Q_N X = \frac{1}{2}X^T P_N X$$

- Back up one step and calculate $V_{N-1}(x)$:

$$V_{N-1} = \min_U \frac{1}{2}X_{N-1}^T Q X_{N-1} + \frac{1}{2}U^T R U + V_N(AX_{N-1} + BU_{N-1})$$

---

$$\Rightarrow \min_U \frac{1}{2}U^T R U + \frac{1}{2}(AX_{N-1} + BU)^T P_N (AX_{N-1} + BU)$$

Taking derivative w.r.t. $u$ and setting to zero: $$\Rightarrow RU + B^T P_N (AX_{N-1} + BU) = 0$$

Solving for $u_{N-1}$: $$\Rightarrow U_{N-1} = \underbrace{-(R + B^T P_N B)^{-1} B P_N A}_{K_{N-1}} X_{N-1}$$

---

- Plug $U = -KX$ back in:

$$\Rightarrow V_{N-1}(X) = \frac{1}{2}X^T \underbrace{[Q + K^T R K + (A-BK)^T P_N (A-BK)]}_{P_{N-1}} X$$

$$\Rightarrow V_{N-1}(X) = \frac{1}{2}X^T P_{N-1} X$$

- Now we have a backward recursion for $K$ and $P$ that we iterate until $k = 0
- For LQR, riccati is the Dynamic programming

## Dynamic Programming Algorithm


- $V_N(x) \leftarrow l_N(x)$
- $k \leftarrow N$
- $while \quad k > 1$
	- $$V_{k-1}(X) = \min_{U\in\mathcal{U}} [l(X,U) + V_k(f(X,U))]$$
	- $k \leftarrow k-1$
- $end$

- If we know $V_k(x)$, the optimal policy is:


$$U_k(X) = \underset{U\in\mathcal{U}}{\operatorname{arg\,min}} [l(X,U) + V_{k+1}(f(X,U))]$$

- DP equations can be equivalently written in terms of "action-value" or "Q" function:

$$S_k(X,U) = l(X,U) + V_{k+1}(f(X,U))$$

- Usually denoted $Q(X,U)$ but we'll use $S(X,U)$
- Avoids need for explicit dynamics model 
[model RL vs model free RL](https://youtu.be/RtGsW12LRjk?list=PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI&t=4281)

## The Curse of Dimensionality

- DP is sufficient for global optimum
- Only tractable for simple problems (LQR, low dimensional)
- $V(x)$ stays quadratic for LQR but becomes impossible to write analytically even for simple nonlinear problems
- Even if we could, $\min_U S(x,u)$ will be non-convex and possibly hard to solve
- Cost of DP blows up with state dimension due to cost of representing $V(X)$




## Why Do We Care?


- Approximate DP with a function approximator for $V(X)$ or $S(X,U)$ (model free vs model based) is very powerful
- Forms basis for modern RL
- DP generalizes to stochastic problems (just wrap everything in expectations). Pontryagin does not.

## Connection: Lagrange Multipliers ≈ Gradient of the Value Function
![[largarnage_multipler.jpg]]

This connects trajectory optimization and DP.

Consider the finite-horizon optimal control problem written as a constrained optimization over the whole trajectory $\{x_k, u_k\}$, with equality constraints

$$x_{k+1} - f_k(x_k, u_k) = 0$$

for each $k$. Form the Lagrangian

$$L = \ell_N(x_N) + \sum_{k=0}^{N-1} \left[ \ell_k(x_k, u_k) + \lambda_{k+1}^\top (f_k(x_k, u_k) - x_{k+1}) \right]$$

The Lagrange multipliers $\lambda_k$ associated with the dynamic constraints satisfy backward recursion conditions that match costate equations (Pontryagin). At an optimal solution, there is a deep relationship:

$$\lambda_k = \nabla_x V_k(x_k)$$

i.e., the multiplier at time $k$ is the gradient of the optimal cost-to-go with respect to the state.

**Intuitively:**
- $V_k(x_k)$ is the optimal total future cost from state $x_k$
- Changing $x_k$ slightly changes the optimal total cost; that sensitivity is $\nabla_x V_k(x_k)$
- In the constrained optimization viewpoint, the dual variable $\lambda_k$ also captures exactly that sensitivity to the constraint $x_k$ because it enforces dynamics

So trajectory optimization (with KKT conditions / multipliers) and dynamic programming (with value functions) are two views of the same underlying structure.

### For LQR: Explicit Connection

We know from DP that the value function is quadratic:

$$V_k(x) = \frac{1}{2} x^\top P_k x$$

Therefore:

$$\lambda_k = \nabla_x V_k(x_k) = P_k x_k$$

This shows directly that the costate $\lambda_k$ from Pontryagin and the Riccati matrix $P_k$ from DP encode the same information—the sensitivity of optimal cost to state perturbations.

---
tags: optimal_control
lecture: "10"
---


# Lecture 10: Convexity and Convex Model-Predictive Control

## Last Time:
- Controllability
- Dynamic Programming

## Today:
- Convexity Background
- Convex MPC

---

## Convex Model-Predictive Control

- LQR is very powerful but we often need to reason about constraints
- Often these are simple (e.g. actuator limits)
- Constraints break the Riccati solution, but we can still solve the QP online
- Convex MPC has gotten popular as computers have gotten faster

---

## Background: Convexity

![[convex_set.png]]
- A line connecting any 2 points in the set is fully contained in the set

### Standard Examples of Convex Sets:
- Linear subspaces: $Ax = b$
- Half space/box/polytope: $Ax \leq b$
- Ellipsoids: $x^T P x \leq 1$, $P \geq 0$
- Cones: $|x_1| = \|x_{2:n}\|_2$
  - "Second-order" cone (like ice cream cone)

---

## Convex Function

- A function $f(x) : \mathbb{R}^n \to \mathbb{R}$ whose epigraph is a convex set


![[convex_fucntion.png]]
### Standard Examples of Convex Functions:
- Linear: $f(x) = c^T x$
- Quadratic: $f(x) = \frac{1}{2}x^T Q x + q^T x$, $Q \geq 0$
- Norms: $f(x) = |x|$ (any norm)

---

## Convex Optimization Problem
Minimize a convex function over a convex set

### Standard Examples:
- **Linear Program (LP)**: $f(x)$, $c(x)$ both linear
- **Quadratic Program (QP)**: Quadratic $f(x)$, linear $c(x)$
- **Quadratically-Constrained QP (QCQP)**: $"$, ellipsoid $c(x)$
- **Second-order Cone Program (SOCP)**: linear $f(x)$, cone $c(x)$

### Key Properties:
- Convex optimization problems don't have any spurious local optima that satisfy KKT
  - If you find a local KKT solution, you have the solution
- Practically, Newton's method converges really fast and reliably (5-10 iterations max)
  - Can bound solution time for real-time control

---

## Convex MPC

Think "constrained LQR"

![[convex_mpc_block_digram.png]]
![[mpc_traj.png]]

### From Dynamic Programming:
Remember from DP, if we have a cost-to-go function $V(x)$, we can get $u$ by solving a one-step problem:

$$u_n = \arg\min_{u} \ell(x,u) + V_{n+1}(f(x,u))$$

$$= \arg\min_{u} \frac{1}{2}u^T R u + (Ax + Bu)^T P_{LQR}(Ax + Bu)$$

- We can add constraints on $u$ to this one-step problem
- But this will perform poorly because $V(x)$ was computed without constraints
  - **Why?** The LQR Value function $P_{LQR}$ assumes infinite actuator authority.
  - If we are saturated (hitting a limit), $P_{LQR}$ underestimates the true cost to reach the goal.
  - We need a "Horizon" $H$ long enough to see that the constraints will continue to limit us in the future.

### Multi-step Approach:
There's no reason I can't add more steps to the one-step problem:

$$\min_{x_{1:H}, u_{1:H-1}} \sum_{n=1}^{H-1} \frac{1}{2}x_n^T Q x_n + \frac{1}{2}u_n^T R u_n + x_H^T P_H x_H$$

Subject to constraints:
1. **Dynamics:** $x_{k+1} = Ax_k + Bu_k$
2. **Inequalities (The "Walls"):** $u_{min} \leq u_k \leq u_{max}$ (e.g., thrust limits)

where $x_H^T P_H x_H$ is the "Terminal Cost" (LQR cost-to-go).

- $H = N$ is called "Horizon"

### Properties:
- With no additional constraints, MPC ("receding horizon") exactly matches LQR for any $H$
- **Intuition**: Explicit constrained optimization over first $H$ steps gets the state close enough to the reference that constraints are no longer active and LQR cost-to-go is valid further into the future

### In General:
- A good approximation of $V(x)$ is important for good performance
- Better $V(x)$ $\Rightarrow$ shorter horizon
- Longer $H$ $\Rightarrow$ less reliance on $V(x)$

### Mathematical Implementation (The "Solver" View):
While the summation above is the theory, the computer (e.g., OSQP solver) solves a standard Quadratic Program (QP) by "stacking" vectors.

**1. The Decision Variable ($z$):**
We stack all future inputs and states into one giant vector $z$:
$$z = [u_0^T, x_1^T, u_1^T, x_2^T, \dots, u_{H-1}^T, x_H^T]^T$$

**2. The Optimization Problem:**
$$\min_z \frac{1}{2}z^T \mathcal{H} z + q^T z$$
subject to:
$$l \leq \mathcal{C} z \leq u$$

**3. How Constraints are Enforced:**
- **Dynamics as Equality Constraints:** The physics $x_{k+1} = Ax_k + Bu_k$ are rewritten as linear equalities:
  $$Ax_k + Bu_k - x_{k+1} = 0$$
  This corresponds to the `C` matrix in code (dynamics error must be 0).

- **Actuator Limits:** The simple bounds $u_{min} \leq u_k \leq u_{max}$ are enforced directly on the rows of $z$ corresponding to $u$.

---

## Example: Planar Quadrotor

![[quadrotor.png]]

### Dynamics:
$$m\ddot{x} = -(u_1 + u_2)\sin(\theta)$$

$$m\ddot{y} = (u_1 + u_2)\cos(\theta) - mg$$

$$J\ddot{\theta} = \frac{\ell}{2}(u_2 - u_1)$$

### Linearize about hover:
$$u_1 = u_2 = \frac{1}{2}mg$$

This gives:

$$\Delta\ddot{x} \approx -g\Delta\theta$$

$$\Delta\ddot{y} \approx \frac{1}{m}(\Delta u_1 + \Delta u_2)$$

$$\Delta\ddot{\theta} \approx \frac{1}{J}\frac{\ell}{2}(\Delta u_2 - \Delta u_1)$$

### State-Space Form:
$$\begin{bmatrix} \Delta\dot{x} \\ \Delta\dot{y} \\ \Delta\dot{\theta} \\ \Delta\ddot{x} \\ \Delta\ddot{y} \\ \Delta\ddot{\theta} \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & -g & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta y \\ \Delta\theta \\ \Delta\dot{x} \\ \Delta\dot{y} \\ \Delta\dot{\theta} \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ \frac{1}{m} & \frac{1}{m} \\ -\frac{\ell}{J} & \frac{\ell}{J} \end{bmatrix} \begin{bmatrix} \Delta u_1 \\ \Delta u_2 \end{bmatrix}$$

$$\dot{x} = Ax + Bu$$

### MPC Cost Function:
$$J = \sum_{n=1}^{H-1} \frac{1}{2}(x_n - x_{ref})^T Q(x_n - x_{ref}) + \frac{1}{2}u_n^T R u_n + \frac{1}{2}(x_H - x_{ref})^T P_H(x_H - x_{ref})$$

**Note on Terminal Cost ($P_H$):**
In code (`mpc.ipynb`), we calculate $P$ using the discrete algebraic Riccati equation:
$$P = \text{dare}(A, B, Q, R)$$
By using the unconstrained LQR solution ($P$) as the cost for the final step $H$, the MPC controller "approximates" the infinite horizon, ensuring stability even if $H$ is short.

---

## Summary

Convex MPC combines the power of LQR with the ability to handle constraints by:
1. Using a receding horizon optimization approach
2. Solving a constrained convex optimization problem at each time step
3. Using an LQR-based terminal cost to approximate the infinite-horizon cost-to-go
4. Leveraging fast, reliable convex optimization solvers for real-time control

---

## Algorithm: The Receding Horizon Loop

This is the practical implementation (matches `mpc_controller` in code):

1. **Measure:** Get current state $x_t$.
2. **Update:** Update the QP constraints to reflect the current state as the starting point ($x_0 = x_t$).
   - *Code:* `lb[1:6] .= -A*x`
3. **Solve:** Run the numerical solver (OSQP) to find the optimal sequence $u_0, \dots, u_{H-1}$ that satisfies constraints ($u_{min} \leq u \leq u_{max}$).
4. **Act:** Apply **only** the first control input $u_0$ to the system.
   - *Code:* `return u_hover + Δu` (first element only)
5. **Repeat:** Discard the rest of the plan, shift the horizon, and repeat at $t+1$.

### Why discard the calculated steps? (The "Waste" vs. "Feedback" Trade-off)
It seems wasteful to compute 20 steps ($u_{0:19}$) and throw away 19. We do this to create **Feedback**:

1. **Model Mismatch:** The mathematical model $x_{k+1} = Ax + Bu$ is perfect, but reality has wind, friction, and noise ($w$).
2. **Drift:** If we blindly executed the sequence $u_{0:19}$ (Open Loop), the errors $w$ would accumulate, and the drone would crash.
3. **Correction:** By measuring $x_{t+1}$ and re-solving, we correct for the errors introduced in the previous step. This turns the optimization into a **Closed Loop** controller.---
tags: optimal_control
lecture: "11"
---
# Lecture 11

## Last Time:
- Convex Optimization Overview
- Convex MPC

## Today:
- Nonlinear Trajectory Optimization
- Differential Dynamic Programming

## What About Nonlinear Dynamics?

- Linear stuff often works well, so use it if you can
- Nonlinear dynamics makes MPC problem non-convex
  - $\Rightarrow$ no convergence/optimality guarantees
- Can work well in practice with effort

## Nonlinear Traj Opt Problem:

$$
\begin{align}
\min_{x_k, u_k} \quad & J = \sum_{k=0}^{N-1} \ell_k(x_k, u_k) + \ell_N(x_N) \\
& \qquad \underbrace{\qquad\qquad\qquad}_{\text{running cost}} \\
\text{s.t.} \quad & x_{k+1} = f(x_k, u_k) \quad \leftarrow \text{ nonlinear} \\
& x_k \in \mathcal{X}_k \quad \left\} \text{ non-convex constraints} \right. \\
& u_k \in \mathcal{U}_k \quad \left. \phantom{\}} \right\}
\end{align}
$$

- Usually assume cost + constraints are $C^2$ (continuous 2nd derivatives)

---

## Differential Dynamic Programming (DDP)

- Nonlinear trajopt method based on approximate DP
- Use a 2nd-order Taylor expansion of cost-to-go in DP to compute Newton steps
- Very fast convergence is possible
- Can stop early in real-time application

### Cost-to-go Expansion:

$$
V_n(x + \delta x) \approx V_n(x) + p_n^T \delta x + \frac{1}{2} \delta x^T P_n \delta x
$$

$$
p_N = \nabla_x \ell_N(x) \qquad P_N = \nabla_{xx}^2 \ell_N(x)
$$

### Action-Value Function Expansion:

$$
S_n(x+\delta x, u+\delta u) \approx S_n(x,u) + \begin{bmatrix} g_x \\ g_u \end{bmatrix}^T \begin{bmatrix} \delta x \\ \delta u \end{bmatrix} + \frac{1}{2} \begin{bmatrix} \delta x \\ \delta u \end{bmatrix}^T \begin{bmatrix} G_{xx} & G_{xu} \\ G_{ux} & G_{uu} \end{bmatrix} \begin{bmatrix} \delta x \\ \delta u \end{bmatrix}
$$

$(G_{ux} = G_{xu}^T)$

$$
\begin{align}
V_{n-1}(x) = \min_{\delta u} \bigg[ & S_{n-1}(x,u) + g_x^T \delta x + g_u^T \delta u \\
& + \frac{1}{2} \delta x^T G_{xx} \delta x + \frac{1}{2} \delta u^T G_{uu} \delta u \\
& + \frac{1}{2} \delta x^T G_{xu} \delta u + \frac{1}{2} \delta u^T G_{ux} \delta x \bigg]
\end{align}
$$

$$
\nabla_{\delta u} [\cdot] = g_u + G_{uu} \delta u + G_{ux} \delta x = 0
$$

---

## Optimal Control Solution

$$
\begin{align}
\Rightarrow \delta u_{n-1} &= -G_{uu}^{-1} g_u - G_{uu}^{-1} G_{ux} \delta x \\
& \quad \underbrace{\qquad}_{d_{n-1}} \quad \underbrace{\qquad\quad}_{K_{n-1}} \\
&= -d_{n-1} - K_{n-1} \delta x
\end{align}
$$

$$
\underbrace{-d_{n-1}}_{\text{"Feed-forward"}} \quad \underbrace{-K_{n-1} \delta x}_{\text{"Feedback"}}
$$

### Plug back into $S_{n-1}$ to get $V_{n-1}(x+\delta x)$:

$$
\begin{align}
\Rightarrow V_{n-1}(x+\delta x) = & V_{n-1}(x) + g_x^T \delta x + g_u^T(-d_{n-1}-K_{n-1}\delta x) \\
& + \frac{1}{2} \delta x^T G_{xx} \delta x + \frac{1}{2}(-d_{n-1}-K_{n-1}\delta x)^T G_{uu}(\cdots) \\
& - \frac{1}{2} \delta x^T G_{xu}(\cdots) - \frac{1}{2}(\cdots)^T G_{ux} \delta x
\end{align}
$$

$$
\Downarrow
$$

$$
\boxed{
\begin{align}
P_{n-1} &= G_{xx} + K_{n-1}^T G_{uu} K_{n-1} - G_{xu} K_{n-1} - K_{n-1}^T G_{ux} \\
p_{n-1} &= g_x - K_{n-1}^T g_u + K_{n-1}^T G_{uu} d_{n-1} - G_{xu} d_{n-1}
\end{align}
}
$$

---

## Matrix Calculus

- given $f(x): \mathbb{R}^n \to \mathbb{R}^m$, look at 2nd-order Taylor expansions
- if $m = 1$:

$$
f(x+\delta x) \approx f(x) + \underbrace{\frac{\partial f}{\partial x}}_{\mathbb{R}^{1 \times n}} \delta x + \frac{1}{2} \delta x^T \underbrace{\frac{\partial^2 f}{\partial x^2}}_{\mathbb{R}^{n \times n}} \delta x
$$

- for $m > 1$: $\frac{\partial^2 f}{\partial x^2}$ is a 3rd-rank tensor. Think of "3D matrix"
  We need some tricks to deal with these

### Kronecker Product:

$$
\underbrace{A}_{\ell \times m} \otimes \underbrace{B}_{m \times p} = \begin{bmatrix} a_{11}B & a_{12}B & \cdots \\ a_{21}B & a_{22}B & \cdots \\ \vdots & \vdots & \end{bmatrix}_{\ell n \times mp}
$$

### Vectorization Operator

$$
\underbrace{A}_{\ell \times m} = \underbrace{[A_1 \; A_2 \; A_3 \; \cdots \; A_m]}_{\text{column vectors}}
$$

$$
\text{vec}(A) = \begin{bmatrix} A_1 \\ A_2 \\ A_3 \\ \vdots \\ A_m \end{bmatrix}_{\ell m \times 1}
$$

### The "vec trick"

$$
\text{vec}(ABC) = (C^T \otimes A) \, \text{vec}(B)
$$

$$
\Rightarrow \text{vec}(AB) = (B^T \otimes I) \, \text{vec}(A) = (I \otimes A) \, \text{vec}(B)
$$

---

## Differentiating Matrices

- If I want to diff a matrix wrt a vector, vectorize the matrix:

$$
\frac{\partial A(x)}{\partial x} = \underbrace{\frac{\partial \, \text{vec}(A)}{\partial x}}_{\ell m \times n} \quad \text{(implied whenever we diff a matrix)}
$$

### Taylor expansion of $f(x)$:

$$
\begin{align}
f(x+\delta x) &\approx f(x) + \underbrace{\frac{\partial f}{\partial x}}_{A} \delta x + \frac{1}{2} (\delta x^T \otimes I) \underbrace{\frac{\partial^2 f}{\partial x^2}}_{\frac{\partial A}{\partial x} = \frac{\partial \, \text{vec}(A)}{\partial x}} \delta x \\
&= \frac{\partial}{\partial x}[\text{vec}(I \, A \, x \, \delta x)]
\end{align}
$$

### Sometimes we need to diff through a transpose:

$$
\frac{\partial}{\partial x}(A(x)^T B) = \underbrace{(B^T \otimes I) T}_{\text{"commutator matrix"}} \frac{\partial A}{\partial x}
$$

$$
T \, \text{vec}(A) = \text{vec}(A^T)
$$

---

## Action-Value Function Derivatives:

$$
S_k(x,u) = \ell_k(x,u) + V_{k+1}(f(x,u))
$$

$$
\Rightarrow \frac{\partial S}{\partial x} = \frac{\partial \ell}{\partial x} + \underbrace{\frac{\partial V}{\partial f}}_{A} \frac{\partial f}{\partial x} \quad \Rightarrow \quad \boxed{g_x = \nabla_x \ell_k + A_k^T p_{k+1}}
$$

$$
\frac{\partial S}{\partial u} = \frac{\partial \ell}{\partial u} + \underbrace{\frac{\partial V}{\partial f}}_{B} \frac{\partial f}{\partial u} \quad \Rightarrow \quad \boxed{g_u = \nabla_u \ell_k + B_k^T p_{k+1}}
$$

---

## Second-Order Derivatives:

$$
\boxed{
\begin{align}
G_{xx} &= \frac{\partial^2 S}{\partial x^2} = \nabla_{xx}^2 \ell_k + A_k^T P_{k+1} A_k + (p_{k+1} \otimes I)^T T \frac{\partial^2 A}{\partial x^2} \\
G_{uu} &= \frac{\partial^2 S}{\partial u^2} = \nabla_{uu}^2 \ell_k + B_k^T P_{k+1} B_k + (p_{k+1} \otimes I)^T T \frac{\partial^2 B}{\partial u^2} \\
G_{xu} &= \frac{\partial^2 S}{\partial x \partial u} = \nabla_{xu}^2 \ell_k + A_k^T P_{k+1} B_k + (p_{k+1} \otimes I)^T T \frac{\partial^2 A}{\partial u}
\end{align}
}
$$
---
tags: optimal_control
lecture: "12"
---

## Last Time:
- Convex MPC Examples
- Nonlinear Traj Opt
- DDP/iLQR

## Today:
- DDP details + extensions
- Constraints

---

## DDP Recap:

**Solve the unconstrained traj Opt problem:**

$$
\min_{x_{1:N}, u_{1:N-1}} J = \sum_{n=1}^{N-1} \ell(x_n, u_n) + \ell_N(x_N)
$$

$$
\text{s.t. } x_{n+1} = f(x_n, u_n)
$$

**Backward Pass:**

$$
V_n(x+\delta x) \approx V(x) + p_n^T\delta x + \frac{1}{2}\delta x^T P_n \delta x
$$

$$
P_N = \nabla^2 \ell_N(x), \quad p_N = \nabla \ell_N(x)
$$

$$
V_{n-1}(x+\delta x) = \min_{\delta u} S(x+\delta x, u+\delta u)
$$

$$
\Rightarrow \begin{cases}
\delta u_{n-1} = -d_{n-1} - K_{n-1}\delta x_{n-1} \\
P_{n-1} = G_{xx} + K^T G_{uu}K - G_{xu}K - K^T G_{ux} \\
p_{n-1} = g_x - K^T g_u + K^T G_{uu}d - G_{xu}d
\end{cases}
$$

---

## Forward Rollout

$$
\Delta J = 0
$$
$$
x_1' = x_1
$$

**for** $k = 1:N-1$

$$
u_n' = u - \alpha d_n - K_n(x_n' - x_n)
$$
$$
x_{n+1}' = f(x_n', u_n')
$$
$$
\Delta J \leftarrow \Delta J + \alpha g_u^T d_n
$$

**end**

**Line Search:**

```
α = 1

do:
    x', u', ΔJ = rollout(x, u, d, K, α)
    α ← cα

while J(x', u') ≤ J(x, u) - bΔJ

x, u ← x', u'
```

- **repeat until** $|d|_\infty < \text{tol}$
- **Armijo parameters:** $c \sim \frac{1}{2}$, $b \sim 10^{-4} - 0.01$

---

## Examples:

- Cartpole + acrobot swing up
- DDP can converge in fewer iterations but iLQR often wins in wall-clock time
- Problems are nonconvex $\Rightarrow$ can land in different local optima depending on initial guess

## Regularization

- Just like standard Newton, $V(x)$ and/or $S(x,u)$ Hessians can become indefinite in backward pass
- Regularization is definitely necessary for DDP, often a good idea with iLQR as well.
- Many options for regularizing:
  - Add a multiple of identity to $\nabla^2 S(x,u)$
  - Regularize $P_n$ or $G_{xx}$ as needed in the backward pass
- **Regularize just** $G_{uu} = \nabla_u^2 S(x,u)$ **(this is the only matrix you have to invert):**

  $$
  d = G_{uu}^{-1}g_u, \quad K = G_{uu}^{-1}G_{ux}
  $$

- This last one is good for iLQR but not DDP
- Regularization should not be required for iLQR but can be necessary due to floating-point error.

---

## DDP Notes:

**Positives:**
+ Can be very fast (iterations + wall-clock)
+ One of the most efficient methods due to exploitation of DP structure
+ Always dynamically feasible due to forward rollout $\Rightarrow$ can always execute on robot
+ Comes with TVLQR tracking controller for free $\Rightarrow$ can be very effective for online use

**Negatives:**
- Does not naturally handle constraints
- Does not support infeasible initial guess for state trajectory due to forward rollout. Bad for "maze" or "bug trap" problems.
- Can suffer from numerical ill-conditioning on long trajectories.

---

## Handling Constraints in DDP

- Many options depending on type of constraint
- Torque limits can be handled with a "squashing function" e.g. $\tanh(u)$:


![[torque_limits.png]]

- Effective, but adds nonlinearity and may need more iterations
- Better option: Solve box-constrained QP in the backward pass!

  $$
  \delta u = \arg\min_{\delta u} S(x+\delta x, u+\delta u)
  $$
  $$
  \text{s.t. } u_{\min} \leq u+\delta u \leq u_{\max}
  $$

- State constraints are harder. Often penalties are added to cost function. Can cause ill-conditioning.
- Better option: Wrap entire DDP algorithm in an Augmented Lagrangian method.
- AL method adds linear (multiplier) and quadratic (penalty) terms to the cost $\Rightarrow$ Fits into DDP nicely.
---
tags: optimal_control
lecture: "13"
---

## Last Time:
- DDP details
- Constraints

## Today:
- Minimum/free-time problems
- Direct Trajectory Optimization
- Direct Collocation
- Sequential Quadratic Programming

---

## Handling Free/Minimum-Time Problems

**min time**

$$
\begin{align}
\min_{x(t), u(t), T_f} \quad & T = \int_0^{T_f} 1 \, dt \\
\text{s.t.} \quad & \dot{x} = f(x, u) \\
& x(T_f) = x_{goal} \\
& u_{min} \leq u \leq u_{max}
\end{align}
$$

- We don't want to change the number of knot points
- Make $h$ (time step) from RK a "control input"
  - $x_{n+1} = f_{RK4}(x_n, u_n, h)$
  - $U = [u_n, h_n]$

- Also want to scale the cost by $h$ e.g.
  $$J(X, U) = \sum_{n} h_n \ell(x_n, u_n) + \ell_f(x_N)$$

- Requires constraints on $h$, otherwise solver can "cheat physics" by making $h$ very large or negative.

- Always nonlinear/nonconvex even if dynamics are linear

---

## Direct Traj Opt

**Basic strategy:** Discretize/"transcribe" continuous-time problem into a standard nonlinear program (NLP):

**"Standard" NLP:**
$$
\begin{align}
\min_x \quad & f(x) \quad \leftarrow \text{ cost function} \\
\text{s.t.} \quad & c(x) = 0 \quad \leftarrow \text{ "dynamics" constraints} \\
& d(x) \leq 0 \quad \leftarrow \text{ other constraints}
\end{align}
$$

- All functions assumed $C^2$ smooth
- Lots of off-the-shelf solvers for large-scale NLP
- Most common: **IPOPT** (free), **SNOPT** (commercial), **KNITRO** (commercial)
- Common solution: **Sequential Quadratic Programming (SQP)**

---

## SQP

**Strategy:** Use 2nd order Taylor expansion of the Lagrangian and linearize $c(x)$, $d(x)$ to approximate the NLP as a QP:

$$
\begin{align}
\min_{\delta x} \quad & f(x) + g^T \delta x + \frac{1}{2} \delta x^T H \delta x \\
\text{s.t.} \quad & c(x) + C \delta x = 0 \\
& d(x) + D \delta x \leq 0
\end{align}
$$

Where:
- $H = \frac{\partial^2 \mathcal{L}}{\partial x^2}$
- $g = \frac{\partial f}{\partial x}$
- $C = \frac{\partial c}{\partial x}$
- $D = \frac{\partial d}{\partial x}$
- $\mathcal{L}(x, \lambda, \mu) = f(x) + \lambda^T c(x) + \mu^T d(x)$

---

## SQP (continued)

- Solve QP to compute primal-dual search direction:
  $$\delta z = [\delta x, \delta \lambda, \delta \mu]$$

- Perform line search with merit function

- With only equality constraints, reduces to Newton method

- Think of SQP as a generalization of Newton's method to handle inequalities

- Can use any QP solver for sub-problems but good implementations typically warm start using previous QP iteration

- For good performance on TrajOpt problems, taking advantage of sparsity in KKT systems is critical.

- If inequalities are convex (e.g. conic) can generalize SQP to **SCP** (sequential convex programming) where inequalities passed directly to the sub-problem solver.

---

## Direct Collocation

- So far we've used explicit RK methods:
  $$\dot{x} = f(x, u) \rightarrow x_{n+1} = f_{RK}(x_n, u_n)$$

- This makes sense if you're doing a rollout

- However in a direct method we're just enforcing dynamics as equality constraints between knot points:
  $$c_n(x_n, u_n, x_{n+1}, u_{n+1}) = 0$$
  $\Rightarrow$ implicit integration is "free"

- Collocation methods use polynomial splines to represent trajectories and enforce dynamics as constraints on spline derivatives.

- Classic DIRCOL algorithm uses cubic splines for states and piecewise linear interpolation for $u(t)$

---

## DIRCOL Spline Approximations

**"Collocation point"**

![[collocation_pts.png]]

Cubic spline for state:
$$
\begin{align}
x(t) &= c_0 + c_1 t + c_2 t^2 + c_3 t^3 \\
\dot{x}(t) &= c_1 + 2c_2 t + 3c_3 t^2
\end{align}
$$

Linear system relating coefficients to states:
$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1 & h & h^2 & h^3 \\
0 & 1 & 2h & 3h^2
\end{bmatrix}
\begin{bmatrix}
c_0 \\ c_1 \\ c_2 \\ c_3
\end{bmatrix}
=
\begin{bmatrix}
x_n \\ \dot{x}_n \\ x_{n+1} \\ \dot{x}_{n+1}
\end{bmatrix}
$$

---

## DIRCOL Integration

Evaluate at $t_{n+\frac{1}{2}}$:

$$
\begin{align}
x_{n+\frac{1}{2}} &= x(t_n + h/2) = \frac{1}{2}(x_n + x_{n+1}) + \frac{h}{8}(\dot{x}_n - \dot{x}_{n+1}) \\
&= \frac{1}{2}(x_n + x_{n+1}) + \frac{h}{8}(\underbrace{f(x_n, u_n) - f(x_{n+1}, u_{n+1})}_{\text{continuous-time dynamics}})
\end{align}
$$

$$
\begin{align}
\dot{x}_{n+\frac{1}{2}} &= \dot{x}(t_n + h/2) = -\frac{3}{2h}(x_n - x_{n+1}) - \frac{1}{4}(\dot{x}_n + \dot{x}_{n+1}) \\
&= -\frac{3}{2h}(x_n - x_{n+1}) - \frac{1}{4}(f(x_n, u_n) + f(x_{n+1}, u_{n+1}))
\end{align}
$$

$$u_{n+\frac{1}{2}} = u(t_n + h/2) = \frac{1}{2}(u_n + u_{n+1})$$

We can enforce the dynamics constraints:

$$
\begin{align}
c_n(x_n, u_n, x_{n+1}, u_{n+1}) &= \\
\underbrace{f(x_{n+\frac{1}{2}}, u_{n+\frac{1}{2}})}_{\text{continuous dynamics}} &+ \frac{3}{2h}(x_n - x_{n+1}) + \frac{1}{4}(f(x_n, u_n) + f(x_{n+1}, u_{n+1})) = 0
\end{align}
$$

- Note that only $x_n$, $u_n$ are decision variables (not $x_{n+\frac{1}{2}}$, $u_{n+\frac{1}{2}}$)
- Called **"Hermite-Simpson"** integration
- Achieves 3rd order integration accuracy like RK3
- Requires fewer dynamics calls than explicit RK3!

---

## Comparison: RK3 vs Hermite-Simpson

**Explicit RK3:**
$$
\begin{align}
f_1 &= f(x_n, u_n) \\
f_2 &= f(x_n + \frac{1}{2}hf_1, u_n) \\
f_3 &= f(x_n + 2hf_1 - hf_2, u_n) \\
x_{n+1} &= x_n + \frac{h}{6}(f_1 + 4f_2 + f_3)
\end{align}
$$
$\Rightarrow$ **3 dynamics calls per time step**

**Hermite-Simpson:**
$$
f(x_{n+\frac{1}{2}}, u_{n+\frac{1}{2}}) + \frac{3}{2h}(x_n - x_{n+1}) - \frac{1}{4}(\underbrace{f(x_n, u_n) + f(x_{n+1}, u_{n+1})}_{\text{these get re-used at adjacent steps!}}) = 0
$$
$\Rightarrow$ **Only 2 dynamics calls per time step!**

- Since dynamics calls often dominate total compute cost, this is ~30-50% savings!

---

## Example:
- Acrobot w/DIRCOL
- Warm starting with dynamically infeasible guess can help a lot!
