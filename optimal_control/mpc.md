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
3. **Correction:** By measuring $x_{t+1}$ and re-solving, we correct for the errors introduced in the previous step. This turns the optimization into a **Closed Loop** controller.