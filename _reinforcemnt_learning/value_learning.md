# Value Function Methods

## Can We Omit the Policy Gradient?

Recall the Actor-Critic update:

$$\nabla_\theta J(\theta) \approx \sum \nabla_\theta \log \pi_\theta(a|s) \hat{A}^\pi(s,a)$$

The advantage $\hat{A}^\pi(s,a)$ tells us how much better action $a$ is compared to the average.

**The Logic:** If we calculate $A^\pi(s,a)$ (or $Q^\pi(s,a)$) perfectly, we know exactly which action is best (the one with the largest return). Why do we need a stochastic policy $\pi_\theta$ to slowly nudge probability mass toward it?

**Idea:** Just pick the action with the biggest return!

$$\pi'(a_t|s_t) = \begin{cases} 1 & \text{if } a_t = \arg\max_a Q^\pi(s_t, a) \ 0 & \text{otherwise} \end{cases}$$

This implies we can omit the explicit policy (the actor) entirely and just learn the value function (the critic). The policy becomes implicit: $\pi(s) = \arg\max_a Q(s,a)$.

---

## Policy Iteration

The general recipe for value-based RL is **Policy Iteration**. It alternates between two steps:

1. **Policy Evaluation:** Estimate $V^\pi(s)$ or $Q^\pi(s,a)$ for the current policy $\pi$.
2. **Policy Improvement:** Update $\pi$ to be greedy with respect to the estimated value.

$$\pi' \leftarrow \arg\max_a Q^\pi(s,a)$$

Steps 1 and 2 repeat until convergence.

---

## Value Iteration (Dynamic Programming)

If the state space $S$ and action space $A$ are small and discrete (tabular), and we know the transitions $p(s'|s,a)$, we can simplify this.

Instead of fully evaluating the policy (which takes time), we can update the value function using the greedy policy immediately.

**Value Iteration Algorithm:**

$$V(s) \leftarrow \max_a \left( r(s,a) + \gamma \sum_{s'} p(s'|s,a) V(s') \right)$$

We don't strictly need to store the policy; we just iterate $V$ until it converges to $V^*$ (the optimal value function).

---

## Fitted Value Iteration

**The Problem:** In the real world, state spaces are continuous or massive (images, robot joints). We can't use a table. This is the _Curse of Dimensionality_.

**Solution:** Use a Neural Network to approximate the value function: $V_\phi(s) \approx V^*(s)$.

**Algorithm:**

1. Collect data using some policy.
2. Compute targets using the Bellman max operator: $$y_i = \max_{a_i} \left( r(s_i, a_i) + \gamma \mathbb{E}_{s'}[V_\phi(s_i')] \right)$$
3. Train $\phi$ via regression (Supervised Learning): $$\mathcal{L}(\phi) = \frac{1}{2} \sum | V_\phi(s_i) - y_i |^2$$

**The Fatal Flaw:** To compute the target $y_i$, we need to calculate the expectation $\mathbb{E}[V_\phi(s_i')]$. This requires knowing the transition dynamics $p(s'|s,a)$ to integrate over possible next states.

We usually don't know the physics of the world (**Model-Free RL**).

---

## Fitted Q-Iteration

**Question:** How do we perform value iteration without knowing the system dynamics?

**Solution:** Learn $Q(s,a)$ instead of $V(s)$.

Recall:

$$Q^\pi(s,a) = r(s,a) + \gamma \mathbb{E}_{s'}[V^\pi(s')]$$

Since $V^*(s') = \max_{a'} Q^*(s', a')$, the target becomes:

$$y_i = r_i + \gamma \max_{a'} Q_\phi(s_i', a')$$

**Why this fixes the flaw:** The expectation is over $s'$, but we have a sample transition $(s_i, a_i, r_i, s_i')$ from our dataset. We use the single sample $r_i + \gamma \max Q(s_i', a')$ as an unbiased estimate of the expected value. The max operator is now inside the expectation (over $a'$), which we can compute because we have the Q-function.

### The Algorithm (Batch Mode)

1. **Collect dataset:** $\mathcal{D} = {(s_i, a_i, s_i', r_i)}$ using some policy (can be any policy!).
2. **Compute targets:** $y_i = r_i + \gamma \max_{a'} Q_\phi(s_i', a')$.
3. **Regress:** Update $\phi$ to minimize $\sum (Q_\phi(s_i, a_i) - y_i)^2$.
4. Repeat.

**Why this is powerful:**

- **Model-free:** No integrals over next states required.
- **Off-policy:** The transitions can come from anywhere (random data, old policies). The target uses $\max_{a'} Q$, which approximates the optimal policy regardless of how the data was collected.

---

## Online Q-Learning

Instead of fitting a whole batch, we can update parameters after every step.

1. Take action $a_i$, observe $(s_i, a_i, s_i', r_i)$.
2. Compute target: $y_i = r_i + \gamma \max_{a'} Q_\phi(s_i', a')$.
3. Gradient update: $$\phi \leftarrow \phi - \alpha \frac{dQ_\phi}{d\phi}(s_i, a_i) \cdot (Q_\phi(s_i, a_i) - y_i)$$

**Critique:** This looks like gradient descent, but strictly speaking it isn't. The target $y_i$ also depends on $\phi$ (the network parameters). We are chasing a moving target.

---

## Exploration

Since the policy is implicitly "take the max Q," it is deterministic. To learn, we must explore.

- **Epsilon-Greedy:** With probability $\epsilon$ take random action, otherwise max.
- **Boltzmann:** Sample $a \sim \exp(Q(s,a))$.

---

## Theory: The "Sad Corollary"

Does Q-Learning with Neural Networks converge? We analyze this using **Operators**.

### 1. The Bellman Operator ($\mathcal{B}$)

The "backup" step (calculating the target) is an operator $\mathcal{B}$:

$$\mathcal{B}V = \max_a (r + \gamma \mathcal{T}_a V)$$

**Key Result:** $\mathcal{B}$ is a **contraction** in the $L_\infty$ norm (max norm). This means applying it brings value functions closer together.

**Result:** Tabular Value Iteration ($V \leftarrow \mathcal{B}V$) is guaranteed to converge to $V^*$.

### 2. The Projection Operator ($\Pi$)

When we train a Neural Network, we are projecting the true target value onto the space of representable functions $\Omega$ (our network architecture).

$$\Pi V = \arg\min_{V' \in \Omega} \frac{1}{2} \sum | V'(s) - V(s) |^2$$

**Key Result:** $\Pi$ is a **contraction** in the $L_2$ norm (Euclidean distance).

### 3. The "Sad Corollary" ($\Pi\mathcal{B}$)

Fitted Value/Q Iteration combines these steps: $Q \leftarrow \Pi \mathcal{B} Q$.

- $\mathcal{B}$ contracts in $L_\infty$.
- $\Pi$ contracts in $L_2$.
- $\Pi \mathcal{B}$ is **NOT a contraction of any kind**.

**Conclusion:** Fitted Q-Iteration and Q-Learning with non-linear function approximation (neural nets) do not theoretically guarantee convergence. They can oscillate or diverge.

However, in practice, we can make them work well with specific tricks (like **Replay Buffers** and **Target Networks**), which forms the basis of **DQN (Deep Q-Networks)**.

---

## Summary

|Algorithm|Learned Function|Requires Model?|On/Off Policy|Converges?|
|---|---|---|---|---|
|Value Iteration|Tabular $V(s)$|Yes|Off|Yes|
|Fitted Value Iter.|NN $V_\phi(s)$|Yes|Off|No*|
|Fitted Q-Iter.|NN $Q_\phi(s,a)$|No|Off|No*|
|Q-Learning|Online NN $Q_\phi(s,a)$|No|Off|No*|

* "No" means no theoretical guarantee with neural networks, though it is widely used in practice.