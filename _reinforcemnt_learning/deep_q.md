# Deep RL with Q-Functions

## Online Q-Learning Is Not Gradient Descent

Recall the online Q-learning update with a neural network $Q_\phi$:

$$\phi \leftarrow \phi - \alpha \frac{dQ_\phi}{d\phi}(s_i, a_i) \left( Q_\phi(s_i, a_i) - \left[ r_i + \gamma \max_{a'} Q_\phi(s_i', a') \right] \right)$$

This looks like gradient descent on a squared error loss. However, it fails in practice with deep neural networks.

**The problem:** Gradient descent assumes a fixed target. In Q-learning, the target $y_i = r_i + \gamma \max_{a'} Q_\phi(s_i', a')$ depends on the same parameters $\phi$ we are updating.

**Analogy:** It's like a dog chasing its own tail. Every step you take to move $Q(s,a)$ closer to the target also moves the target itself. This leads to oscillation and divergence.

---

## Stability Problems in Deep Q-Learning

There are two specific reasons why naive Deep Q-Learning fails:

1. **Correlated Samples:** In online RL, sequential states are highly correlated ($s_t \approx s_{t+1}$). SGD assumes independent and identically distributed (i.i.d.) data. Training on a correlated stream causes the network to overfit to the local trajectory and "forget" everything else.
    
2. **Moving Targets:** As mentioned above, the regression target changes every time we update the network weights.
    

**Question:** How do we stabilize training to make it look more like supervised learning?

---

## Solution 1: Replay Buffers

To fix **Correlated Samples**, we use a **Replay Buffer** (Experience Replay).

1. Store transitions $(s, a, r, s')$ in a large buffer $\mathcal{B}$.
2. During training, sample a random mini-batch from $\mathcal{B}$ instead of using the latest transition.

**Why this works:**

- **Decorrelation:** Random sampling breaks temporal correlations; the batch looks i.i.d.
- **Data Efficiency:** We reuse a single transition multiple times for learning, rather than throwing it away immediately.

---

## Solution 2: Target Networks

To fix **Moving Targets**, we introduce a **Target Network**.

- Maintain a second network $Q_{\phi'}$ with parameters $\phi'$.
- Use $\phi'$ only to calculate the target values.
- Use $\phi$ (current network) to predict values and update weights.

$$y_i = r_i + \gamma \max_{a'} Q_{\phi'}(s_i', a')$$

### Updating the Target Network

The target network is effectively frozen to provide a stable regression target. We update it slowly to track $\phi$:

- **Hard Update (Classic DQN):** Copy $\phi' \leftarrow \phi$ every $N$ steps (e.g., every 10,000 steps). This creates a "staircase" target that stays fixed for long periods.
- **Soft Update (Polyak Averaging):** Update at every step: $\phi' \leftarrow \tau \phi + (1-\tau) \phi'$ with small $\tau$ (e.g., 0.001). This acts like a low-pass filter.

---

## The "Classic" DQN Algorithm

Putting it all together (Mnih et al. 2013):

1. **Collect:** Take action using $\epsilon$-greedy policy, store $(s, a, r, s')$ in Replay Buffer $\mathcal{B}$.
2. **Sample:** Sample random mini-batch from $\mathcal{B}$.
3. **Target:** Compute $y = r + \gamma \max_{a'} Q_{\phi'}(s', a')$ using the Target Network.
4. **Update:** Minimize loss $(Q_\phi(s, a) - y)^2$ on the Current Network.
5. **Sync:** Periodically update $\phi'$ to match $\phi$.

---

## Overestimation Bias

**The Problem:** Q-Learning tends to overestimate values.

Because $\mathbb{E}[\max(X_1, X_2)] \ge \max(\mathbb{E}[X_1], \mathbb{E}[X_2])$, taking the max over noisy Q-values adds a positive bias. Since the policy is greedy, it picks actions with "optimistic noise," accumulating error.

**Question:** Can we reduce this bias without training extra networks?

---

## Solution: Double Q-Learning

**Key Insight:** Decouple the selection of the best action from the evaluation of that action.

**Standard Q-Learning (Biased):**

$$y = r + \gamma Q_{\phi'}(s', \arg\max_{a'} Q_{\phi'}(s', a'))$$

_(Target network selects action AND evaluates it)_

**Double Q-Learning (Unbiased):**

$$y = r + \gamma Q_{\phi'}(s', \arg\max_{a'} Q_{\phi}(s', a'))$$

_(Current network $\phi$ selects best action; Target network $\phi'$ evaluates its value)_

This simple change effectively eliminates the positive bias and significantly improves performance with no computational cost.

---

## Multi-Step Returns (N-Step)

- **Standard Q-learning** uses 1-step returns (Bias: High, Variance: Low).
- **Monte Carlo** uses infinite-step returns (Bias: Low, Variance: High).

**N-Step Returns:**

$$y_{t} = \sum_{k=0}^{N-1} \gamma^k r_{t+k} + \gamma^N \max_{a'} Q_{\phi'}(s_{t+N}, a')$$

- **Pro:** Propagates rewards faster (less bias).
- **Con:** Technically requires on-policy data. If $N$ is small, we often ignore the off-policy correction (or cut the trace if the data is too off-policy).

---

## Q-Learning with Continuous Actions

In discrete action spaces, $\max_a Q(s,a)$ is easy: just evaluate Q for all actions.

**The Problem:** In continuous spaces, computing the max is an optimization problem itself.

### Option 1: Stochastic Optimization

Sample $N$ random actions, evaluate Q, pick the best.

- **Pros:** Dead simple, parallelizable.
- **Cons:** Inaccurate. (Can be improved with Cross-Entropy Method or CMA-ES).

### Option 2: Normalized Advantage Functions (NAF)

Restrict the Q-function architecture to be quadratic in $a$:

$$Q_\phi(s,a) = -\frac{1}{2}(a - \mu_\phi(s))^T P_\phi(s) (a - \mu_\phi(s)) + V_\phi(s)$$

- **Max:** Analytically $\mu_\phi(s)$.
- **Value:** $V_\phi(s)$.
- **Cons:** Limits expressivity (Q-function must be unimodal).

### Option 3: DDPG (Deep Deterministic Policy Gradient)

Learn an approximate maximizer. Train a second network (actor) $\mu_\theta(s)$ to output the action that maximizes $Q$.

- **Critic Update:** Minimize $(Q_\phi(s, a) - y)^2$ using Target Networks.
- **Actor Update:** Maximize $Q_\phi(s, \mu_\theta(s))$.

$$\nabla_\theta J \approx \nabla_a Q_\phi(s,a)\big|_{a=\mu(s)} \cdot \nabla_\theta \mu_\theta(s)$$

This essentially turns Q-learning into an Actor-Critic method where the critic defines the policy.

---

## Practical Tips

- **Huber Loss:** Squared error gradients explode when error is large. Use Huber loss (L2 near zero, L1 far from zero) or gradient clipping.
- **Schedules:** Anneal learning rates and exploration ($\epsilon$) over time.
- **Double Q:** Almost always use it. There is rarely a downside.
- **Prioritized Experience Replay:** Don't sample uniformly. Sample transitions with high TD-error (high "surprise") more frequently.

---

## Summary

|Problem|Solution|
|---|---|
|Correlated Samples|Replay Buffer|
|Moving Targets|Target Network|
|Overestimation Bias|Double Q-Learning|
|Bias/Variance Tradeoff|N-Step Returns|
|Continuous Actions|DDPG (Actor approximates max) or NAF|