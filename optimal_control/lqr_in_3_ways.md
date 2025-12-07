---
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

**Note**: Programming languages like Julia, MATLAB, and Python provide a "dare" (Discrete Algebraic Riccati Equation) function that does this for you.