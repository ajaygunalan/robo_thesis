---
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

