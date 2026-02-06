Here is a comprehensive technical blog post based on **CS 285 Lecture 10**, enriched with the theoretical frameworks from **Chapters 1 and 2 of _Reinforcement Learning and Optimal Control_** by Dimitri P. Bertsekas.

---

# The Known World: Optimal Control, Planning, and Model-Based Reinforcement Learning

**Based on CS 285 Lecture 10 and _Reinforcement Learning and Optimal Control_ by Dimitri P. Bertsekas**

In previous explorations of Reinforcement Learning (RL), we often operated under the assumption that the environment was a "black box."1 The agent had to sample transitions blindly to understand the world. But what if we already know how the world works? What if we have the differential equations of a robot arm, the rules of Go, or a learned neural network simulator?

When the dynamics $p(s_{t+1} | s_t, a_t)$ are known (or learned), the problem shifts from **learning** to **planning**. In Control Theory, this is the domain of **Optimal Control**.

This post explores the algorithms used to make decisions when the dynamics are known, ranging from discrete tree searches like MCTS to continuous trajectory optimization like iLQR. We will ground these modern planning algorithms in the foundational theory of **Deterministic Dynamic Programming** and **Approximation in Value Space** as detailed by Dimitri Bertsekas.

---

## 1. The Optimal Control Objective

In Model-Based RL, our goal is to minimize cost (or maximize reward) over a finite horizon $T$. If the system is deterministic, the dynamics are described by $x_{k+1} = f_k(x_k, u_k)$.

Bertsekas formally defines the deterministic problem in **Section 1.1**:

> _"We want to minimize the cost over all sequences $\{u_0, ..., u_{N-1}\}$ that satisfy the control constraints, thereby obtaining the optimal value $J^*(x_0) = \min_{u_k \in U_k(x_k)} \left[ g_N(x_N) + \sum_{k=0}^{N-1} g_k(x_k, u_k) \right]$."* (Bertsekas, p. 3)

### Open-Loop vs. Closed-Loop Planning

A critical distinction made in Lecture 10 is between open-loop and closed-loop planning.

1. **Open-Loop:** We solve for a sequence of actions $u_1, \dots, u_T$ at the start. This is a plan executed blindly without feedback.
    
2. **Closed-Loop:** We solve for a policy $\pi(u_t | x_t)$. This allows the agent to react to stochasticity and model errors.
    

As noted in the lecture, **Open-Loop planning is suboptimal in stochastic environments**. However, finding a full closed-loop policy $\pi$ is computationally expensive. The standard engineering solution is to perform **Open-Loop Planning** but apply it in a **Closed-Loop** fashion via **Model Predictive Control (MPC)**.

Bertsekas describes this as **Multistep Lookahead** or **Rolling Horizon**:

> _"At state $x_k$, we minimize the cost of the first $l > 1$ stages... This makes intuitive sense, since in this case, the cost of more stages is treated exactly, i.e., with optimization."_ (Bertsekas, p. 52)

By replanning at every time step, we gain the benefits of feedback control while essentially solving a deterministic trajectory optimization problem.

---

## 2. Gradient-Free Planning: Stochastic Optimization

When the dynamics $f(x, u)$ are non-differentiable or highly complex (e.g., a physics engine with contacts), we cannot use gradients. We must rely on **Stochastic Optimization** methods, often referred to as "shooting methods."

### Random Shooting and the Cross-Entropy Method (CEM)

The simplest approach is "Random Shooting": guess a batch of action sequences, simulate them, and pick the best one. While simple, it suffers heavily from the curse of dimensionality.

A powerful refinement is the **Cross-Entropy Method (CEM)** (Lecture 10, Slide 15).2 Instead of a fixed distribution, we iteratively refine our sampling distribution to focus on high-reward regions:

1. **Sample** 3$N$ action sequences from a distribution 4$p(A)$ (e.g., a Gaussian).5
    
2. **Evaluate** the return $J(A)$ for each sequence using the model.
    
3. **Select Elites:** Pick the top $M$ sequences with the highest return.
    
4. **Refit:** Update the mean and variance of $p(A)$ to match the elites.
    
5. **Repeat.**
    

CEM acts as a heuristic optimizer for the Bellman operator's maximization step. It allows us to perform lookahead minimization in continuous spaces without needing derivatives.

---

## 3. Discrete Planning: Monte Carlo Tree Search (MCTS)

When the action space is discrete (like in Chess or Go), we can model the planning problem as a search tree. However, full tree search is impossible due to the branching factor.

**Monte Carlo Tree Search (MCTS)** solves this by performing **Approximate Value Iteration** on the search tree. It builds a sparse tree by simulating trajectories, balancing exploration and exploitation using the **Upper Confidence Bound (UCT)** score.6

### Theoretical View: Stochastic Rollout

Bertsekas provides a rigorous foundation for MCTS in **Section 2.4.2 (Stochastic Rollout and Monte Carlo Tree Search)**. He frames MCTS as a sophisticated form of **Rollout**, which relies on the **Policy Improvement Principle**.

> _"Rollout may also be combined with adaptive simulation and Monte Carlo tree search... The use of simulation often allows for implementations that do not require a mathematical model, a major idea that has allowed the use of DP beyond its classical boundaries."_ (Bertsekas, Preface, p. x)

In MCTS, the "heuristic" used for rollout is often a random policy.7 As we run more simulations, our estimate of the Q-values at the root converges, effectively performing a local policy improvement step 8$\pi_{MCTS}(s) = \arg\max_a Q(s,a)$.9

---

## 4. Gradient-Based Planning: Trajectory Optimization

If the dynamics $x_{t+1} = f(x_t, u_t)$ and cost $c(x, u)$ are differentiable (e.g., known physics equations or a learned neural network), we can use gradients to optimize the sequence of actions directly.

### Shooting vs. Collocation

Lecture 10 (Slides 24-25) highlights two primary formulations:

1. Shooting Method: We optimize only over the actions $u_1, \dots, u_T$. The states are implicit functions of the actions: $x_t = f(f(...f(x_1, u_1)...), u_{t-1})$.
    
    $$ \min_{u_1, \dots, u_T} \sum_{t=1}^T c(x_t(u_{1:t-1}), u_t) $$
    
    We calculate gradients $\frac{dJ}{du_t}$ using backpropagation through time (BPTT). However, this method is notoriously unstable for long horizons (the "butterfly effect").
    
2. Collocation: We treat both states $x$ and actions $u$ as decision variables, linked by equality constraints:
    
    $$ \min_{u_{1:T}, x_{1:T}} \sum c(x_t, u_t) \quad \text{s.t.} \quad x_{t+1} = f(x_t, u_t) $$
    
    By optimizing constraints and costs simultaneously, collocation is often more numerically stable than shooting, preventing the gradients from exploding.
    

---

## 5. The Linear-Quadratic Regulator (LQR)

A special case of trajectory optimization arises when the system is **Linear** and the cost is **Quadratic**:

- Dynamics: $x_{t+1} = F_t x_t + f_t u_t$
    
- Cost: $c(x, u) = \frac{1}{2} x^T C x + \frac{1}{2} u^T c u$
    

As detailed in **Bertsekas Section 1.3.7**, this admits an elegant analytical solution via Dynamic Programming. We don't need iterative gradient descent; we can compute the optimal control law using the **Riccati Equation**.

> _"It can be shown in generality that when the system is linear and the cost is quadratic, the optimal policy and cost-to-go function are given by closed-form expressions, regardless of the number of stages."_ (Bertsekas, p. 39)10

The solution is a time-varying linear feedback controller: $u_t = K_t x_t + k_t$.

### Iterative LQR (iLQR)

Real-world systems are rarely linear. However, we can approximate them as linear _locally_. **Iterative LQR (iLQR)** combines the power of trajectory optimization with the efficiency of LQR:

1. Guess a trajectory.
    
2. Linearize the dynamics and quadratize the cost around the trajectory (Taylor Expansion).
    
3. Solve the local LQR problem to find a better direction.
    
4. Update the trajectory and repeat.
    

This acts like Newton's method for control, converging very quickly to a locally optimal trajectory.

---

## 6. Bridging Theory and Practice: MPC

Whether we use CEM, MCTS, or iLQR, we rarely execute the full plan $u_{1:T}$. In a stochastic world, the model is never perfect.

To handle this, we use **Model Predictive Control (MPC)**:

1. Observe state $x_t$.
    
2. Plan optimal sequence $u_t, \dots, u_{t+H}$.
    
3. Execute **only the first action** $u_t$.
    
4. Observe new state $x_{t+1}$, shift the horizon, and repeat.
    

This converts our open-loop planners into a closed-loop policy. As Bertsekas notes in **Section 2.5.1**, MPC is a heuristic that provides a robust feedback mechanism.

### Certainty Equivalence

MPC relies on the principle of **Certainty Equivalence**: we replace the random variables (future disturbances) with their expected values (usually zero) and solve the deterministic problem.11

> _"Generally, if the optimal policy is unaffected when the disturbances are replaced by their means, we say that certainty equivalence holds."_ (Bertsekas, p. 40)

While exact certainty equivalence only holds for Linear-Quadratic-Gaussian (LQG) systems, treating complex stochastic problems as deterministic ones within an MPC loop is the "secret sauce" that powers much of modern robotics and model-based RL.