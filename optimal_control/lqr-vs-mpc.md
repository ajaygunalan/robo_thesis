# LQR vs MPC: A Unified Treatment

## 1. The Core Problem

Both the Linear Quadratic Regulator (LQR) and Model Predictive Control (MPC) address the same fundamental question: given a system's current state, what control input minimizes a cost function while driving the system toward a target? The difference lies in whether we account for physical constraints.

---

## 2. The Unconstrained Case: LQR

### Formulation

LQR minimizes a quadratic cost over an infinite horizon with no inequality constraints:

$$J_{\infty}^{*}(x(0)) = \min_{u_0, u_1, \ldots} \sum_{k=0}^{\infty} \left( x_k' Q x_k + u_k' R u_k \right)$$

subject only to linear dynamics $x_{k+1} = Ax_k + Bu_k$, where $Q \succeq 0$ and $R \succ 0$.

### Why Infinite Horizon?

LQR *can* be solved over a finite horizon $N$, but this yields time-varying gains $F_0, F_1, \ldots, F_{N-1}$ that change at every step (because "time-to-go" shrinks). As $N \to \infty$, the Riccati Difference Equation converges to a steady-state $P_{\infty}$, producing a single constant gain $F_{\infty}$. This is vastly simpler to implement and guarantees closed-loop stability.

### The Solution: A Closed-Form Formula

Because there are no constraints, the cost function is a smooth quadratic bowl. Finding its minimum requires only setting the gradient to zero—a linear equation. The result is the **Algebraic Riccati Equation (ARE)**:

$$P_{\infty} = A' P_{\infty} A + Q - A' P_{\infty} B (B' P_{\infty} B + R)^{-1} B' P_{\infty} A$$

Once solved offline, the optimal control law is:

$$u^{*}(k) = F_{\infty} x(k), \quad \text{where } F_{\infty} = -(B' P_{\infty} B + R)^{-1} B' P_{\infty} A$$

No optimization solver runs online—just a single matrix multiplication per time step.

### Properties of the LQR Control Law

**Static (Time-Invariant):** The gain $F_{\infty}$ is constant. Whether the system has run for 1 second or 100 years, the same matrix applies.

**Linear:** Control effort scales proportionally with state deviation. Doubling the state doubles the input.

**Globally Valid:** With no constraints, the formula $u = F_{\infty}x$ holds for any state in $\mathbb{R}^n$, no matter how far from the origin. This implicitly assumes infinite actuator authority—if the state is large, LQR demands arbitrarily large inputs.

**Value Function:** The optimal cost-to-go is a single quadratic: $J_{\infty}^{*}(x) = x' P_{\infty} x$, serving as a global Lyapunov function that guarantees stability (provided $(A,B)$ is stabilizable and $(Q^{1/2}, A)$ is observable).

### Intuition

Think of a spring: displacement (state) produces proportional restoring force (control). The relationship $u = -kx$ holds everywhere, assuming the spring never saturates or hits a wall.

---

## 3. The Constrained Case: MPC

### Why Constraints Change Everything

Real systems have limits: actuators saturate, states must remain within safety bounds. LQR ignores these, potentially demanding inputs like $u = 1000$ when the valve maxes out at $u = 1$. MPC explicitly incorporates constraints.

### Formulation

MPC solves a constrained optimization over a finite horizon $N$:

$$J_{0}^{*}(x(t)) = \min_{U_0} \left( p(x_N) + \sum_{k=0}^{N-1} q(x_k, u_k) \right)$$

subject to:

- Dynamics: $x_{k+1} = Ax_k + Bu_k$
- State constraints: $x_k \in \mathcal{X}$
- Input constraints: $u_k \in \mathcal{U}$
- Terminal constraint: $x_N \in \mathcal{X}_f$

Here $\mathcal{X}$ and $\mathcal{U}$ are polyhedral sets encoding physical limits.

### Why Finite Horizon?

MPC *could* theoretically use an infinite horizon, but this creates an optimization problem with infinitely many decision variables—computationally impossible with constraints. A finite $N$ yields a tractable Quadratic Program (QP) or Linear Program (LP) with a fixed number of variables.

To recover infinite-horizon behavior, we use the **Constrained LQR (CLQR)** trick: set the terminal cost $p(x_N) = x_N' P_{\infty} x_N$ (the LQR cost) and choose $\mathcal{X}_f$ as the region where constraints are inactive. If $N$ is large enough, the state enters this "LQR region" by step $N$, and finite-horizon MPC becomes equivalent to infinite-horizon optimal control.

### Why No Closed-Form Solution?

With constraints, the unconstrained minimum (bowl's bottom) may lie outside the feasible region. The gradient-equals-zero formula fails because the optimum sits on a constraint boundary. No single algebraic expression covers all cases—a numerical solver must search the feasible region at every time step.

### The Receding Horizon Mechanism

MPC computes a sequence $u_0^{*}, u_1^{*}, \ldots, u_{N-1}^{*}$ but applies only the first input $u_0^{*}$. At the next step, it measures the actual state and re-solves. This raises two questions:

**Why compute a full sequence if we discard most of it?**

The sequence proves a feasible path exists. A single-step ("myopic") calculation might drive the system into a dead end—a state where no future input can satisfy constraints. By looking $N$ steps ahead, the controller anticipates approaching limits and acts early. For example, with $N = 2$ a system may diverge into infeasibility; increasing to $N = 4$ reveals a valid trajectory to the origin.

**Why not apply the entire sequence?**

The sequence is based on a model prediction. Reality introduces disturbances and model errors. Applying all $N$ inputs would be open-loop control—blindly following a plan regardless of what actually happens. By applying only $u_0^{*}$ and re-solving with fresh measurements, MPC closes the loop, correcting errors immediately.

**Why not just compute one input per step?**

You could if you knew the exact value function $J^{*}(x)$—the true cost-to-go from any state. But constructing this explicitly for constrained systems suffers from the curse of dimensionality. The $N$-step sequence approximates this cost while guaranteeing feasibility.

### The Control Law Structure: Piecewise Affine

Unlike LQR's single linear law, the MPC solution is a **Piecewise Affine (PWA) function**. The state space partitions into polyhedral regions $CR_j$, each with its own affine law:

$$u^{*}(k) = F_j x(k) + g_j \quad \text{if } x(k) \in CR_j$$

This arises because different constraints become **active** (binding) in different regions. Near the origin, no constraints bind and the law resembles LQR. Near a saturation limit, the input clamps to $u_{\max}$. The explicit MPC solution stitches these behaviors together.

**Value Function:** Piecewise quadratic (for quadratic cost) or piecewise linear (for 1-norm/∞-norm cost)—reflecting the region-dependent structure.

### Stability

Finite horizon does not automatically guarantee stability. MPC requires careful design: a terminal cost $p(x_N)$ and terminal set $\mathcal{X}_f$ that together ensure the closed-loop system converges. The standard choice—using LQR's $P_{\infty}$ as terminal cost and the unconstrained region as $\mathcal{X}_f$—inherits LQR's stability properties once constraints become inactive.

### Intuition

Imagine the spring inside a box. Near the center, it behaves like LQR. But if displaced too far, it hits the wall—an active constraint. The control law transitions from proportional ($u = -kx$) to saturated ($u = u_{\max}$). MPC's PWA structure captures exactly these transitions.

---

## 4. Computation: Formula vs. Solver

The fundamental computational difference stems from constraints.

**LQR** has a closed-form solution. The ARE is solved once offline; online control is a single matrix multiplication $u = F_{\infty}x$. You *could* run an optimization solver at every step, but it would return the same $F_{\infty}$ every time—wasteful redundancy.

**MPC** must solve an optimization online because the active constraint set depends on the current state. At time $t$, the system might be far from limits (LQR-like behavior). At $t+1$, a disturbance pushes it near $x_{\max}$, activating a different constraint and changing the optimal law. Without solving based on the measured state, we cannot know which constraints matter.

| Aspect | LQR | MPC |
|--------|-----|-----|
| **Solution method** | Algebraic Riccati Equation (offline) | QP/LP solver (online) |
| **Online cost** | Matrix multiply | Optimization solve |
| **Why?** | No constraints → closed-form exists | Constraints → must search boundaries |

---

## 5. Summary Comparison

| Aspect | LQR | MPC |
|--------|-----|-----|
| **Constraints** | None | Explicit (states and inputs) |
| **Typical Horizon** | Infinite | Finite (receding) |
| **Control Law** | Linear: $u = F_{\infty}x$ | Piecewise Affine: $u = F_j x + g_j$ |
| **Value Function** | Global quadratic | Piecewise quadratic/linear |
| **Computation** | Offline ARE + online multiply | Online QP/LP |
| **Stability** | Guaranteed (Riccati + Lyapunov) | Requires terminal cost/constraint design |
| **Global validity** | Entire $\mathbb{R}^n$ | Feasible set $\mathcal{X}_0 \subseteq \mathbb{R}^n$ |

---

## 6. When Are They Equivalent?

MPC reduces to LQR when:

- No constraints are imposed ($\mathcal{X} = \mathbb{R}^n$, $\mathcal{U} = \mathbb{R}^m$)
- The cost is quadratic
- The horizon is sufficiently long (or terminal cost equals $P_{\infty}$)

Equivalently, if the state $x(t)$ is close enough to the origin that no constraints are active, the MPC solution becomes identical to the linear LQR law. **Mathematically, LQR is a special case of MPC** where $N \to \infty$ and the constraint sets are unbounded.

---

## 7. Key Takeaways

1. **LQR** solves unconstrained optimal control with an elegant closed-form: one constant matrix, computed offline, applied forever.

2. **MPC** handles constraints by solving a finite-horizon optimization online, applying only the first input, and re-solving—converting open-loop planning into closed-loop feedback.

3. **The horizon choice** is driven by practicality: infinite horizon gives LQR a constant gain; finite horizon makes MPC's constrained optimization tractable.

4. **The control law structure** differs because constraints create region-dependent behavior: LQR is globally linear; MPC is piecewise affine.

5. **Computation** differs because constraints eliminate closed-form solutions: LQR uses a formula; MPC uses a solver.

6. **They converge** when constraints are inactive—MPC then behaves exactly like LQR.

---

## 8. What's Next?

This note covered the theoretical foundations. Three questions remain for practical MPC design:

1. **How do we identify the largest region of initial states** for which a controller exists that guarantees the system will never violate its constraints? → [[invariant-sets]]

2. **How does MPC handle uncertainty** without becoming overly conservative or computationally intractable? → [[robust-mpc]]

3. **How do we implement MPC in practice** — tracking nonzero references, finding regions efficiently, and approximating explicit solutions? → [[mpc-implementation]]
