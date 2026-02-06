## Actor-Critic Algorithms

---

## REINFORCE Has Brutal Variance

Recall the REINFORCE policy gradient:

$$ \nabla_\theta J(\theta) \approx \frac{1}{N}\sum_{i=1}^N \sum_{t=1}^T \nabla_\theta \log \pi_\theta(a_{i,t} \mid s_{i,t}) \cdot \hat{Q}_{i,t} $$

where $\hat{Q}_{i,t}$ is the **reward-to-go**:

$$ \hat{Q}_{i,t} = \sum_{t'=t}^T r(s_{i,t'}, a_{i,t'}) $$

This reward-to-go is a **single-sample estimate** of the true expected return.

**The problem:** From any state, many different futures are possible—the policy is stochastic, the environment is stochastic. But we only see _one_ trajectory. We're estimating a complex expectation with a single sample.

Fewer samples → higher variance. A single-sample estimator has maximum variance.

**Question:** Can we get a better estimate of expected future reward?

---

## Learn a Value Function

If we could compute the _true_ expected reward-to-go instead of using one sample, variance would drop dramatically.

Define three related quantities:

**State-action value (Q):** $$ Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t'=t}^T r_{t'} \mid s_t=s, a_t=a \right] $$

**State value (V):** $$ V^\pi(s) = \mathbb{E}_{a \sim \pi} \left[ Q^\pi(s,a) \right] $$

**Advantage (A):** $$ A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s) $$

**Intuition:**

- $Q^\pi(s,a)$: expected return if you take action $a$ then follow $\pi$
- $V^\pi(s)$: expected return if you just follow $\pi$ (average over actions)
- $A^\pi(s,a)$: how much _better_ (or worse) action $a$ is compared to your average behavior

**Why advantage is ideal:** The policy gradient becomes:

$$ \nabla_\theta J(\theta) = \mathbb{E}_\pi \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot A^\pi(s_t, a_t) \right] $$

You increase probability of actions that are _better than average_ and decrease probability of actions that are _worse than average_. The value function $V^\pi(s)$ serves as a state-dependent baseline.

**This is actor-critic:** An **actor** (policy $\pi_\theta$) that picks actions, and a **critic** (value function $V_\phi$ or $Q_\phi$) that evaluates how good things are. The critic tells the actor how much each action helped or hurt.

### Policy Evaluation View

The value function isn't just a variance-reduction gadget – it *is* the RL objective written per-state:

$J(\theta) = \mathbb{E}_{s_1 \sim p(s_1)} \big[ V^{\pi_\theta}(s_1) \big]$

If you can estimate $V^{\pi_\theta}(s)$ well, you can literally **evaluate how good your policy is** just by looking at the values of the initial states.

---

## How Do We Learn the Critic?

We want to learn $V_\phi(s) \approx V^\pi(s)$ from rollout data. This is called **policy evaluation**.

### Option 1: Monte-Carlo Targets

Use the actual returns you observed:

$$ y_{i,t}^{\text{MC}} = \sum_{t'=t}^T r_{i,t'} $$

Train by regression: $$ \mathcal{L}(\phi) = \frac{1}{2} \sum_{i,t} \left( V_\phi(s_{i,t}) - y_{i,t}^{\text{MC}} \right)^2 $$

**Why this helps even with single samples:** The neural network sees many similar states with different outcomes. It learns to _average out_ the randomness through generalization. Two nearby states with returns 8 and 12 will both get predictions around 10.

- **Pro:** Unbiased targets
- **Con:** High variance (depends on entire random future)

### Historical Examples of Policy Evaluation
(Slide 10) provides context on how Value Function fitting has been used in history:
- **TD-Gammon (Tesauro 1992):** Used a neural network to estimate $V(s)$ for Backgammon.
- **AlphaGo (Silver et al. 2016):** Used a value network $\hat{V}_\phi^\pi(s)$ to predict the winner from the current board state, improving over Monte Carlo tree search rollouts alone.

### Option 2: Bootstrapped Targets ([[temporal_difference|TD-style]])

Use the Bellman equation: $$ V^\pi(s_t) = \mathbb{E}\left[ r_t + \gamma V^\pi(s_{t+1}) \right] $$

Approximate with a single transition: $$ y_{i,t}^{\text{boot}} = r_{i,t} + \gamma V_{\phi_{\text{old}}}(s_{i,t+1}) $$

**Intuition:** Instead of waiting for the full trajectory, use: "reward now + my current estimate of future value." This is the core idea of [[temporal_difference|bootstrapping]].

- **Pro:** Much lower variance (only one step of randomness)
- **Con:** Biased (if $V_\phi$ is wrong, targets are wrong)

**The fundamental tradeoff:** We trade lots of variance for some bias.

---

## Putting It Together: The Batch Actor-Critic Algorithm

1. **Generate samples:** Run policy $\pi_\theta$, collect trajectories
2. **Fit critic:** Train $V_\phi$ on sampled rewards (MC or bootstrap targets)
3. **Compute advantage:** For each $(s_t, a_t, r_t, s_{t+1})$: $$\hat{A}_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)$$
4. **Policy gradient:** $$\hat{g} = \frac{1}{N} \sum_{i,t} \nabla_\theta \log \pi_\theta(a_{i,t} \mid s_{i,t}) \cdot \hat{A}_{i,t}$$
5. **Update:** $\theta \leftarrow \theta + \alpha \hat{g}$

The critic replaces the raw Monte-Carlo returns with a smoothed, lower-variance estimate.

---

## Infinite Horizons Blow Up

With bootstrapping, each backup adds to the value. If episodes never end and rewards are positive, values become infinite.

**Question:** How do we handle infinite or very long horizons?

---

## Discount Factors

Introduce $\gamma \in (0,1)$:

$$ y_t = r_t + \gamma V(s_{t+1}) $$

**Interpretations:**

1. **"Fear of death":** With probability $1-\gamma$ at each step, you enter a "death state" with zero reward forever. You prefer rewards sooner because you might not be around later.
    
    - **Formal Dynamics:** The discount factor modifies the transition probabilities of the MDP: $$\tilde{p}(s' \mid s, a) = \gamma p(s' \mid s, a)$$
    - The remaining probability mass $1-\gamma$ transitions to the absorbing "death state."
2. **Variance reduction:** Far-future rewards are highly uncertain. Discounting downweights them, reducing variance.
    

### Two Options for Discounting in Policy Gradients

**Option 1 — Discount only the returns:** $$ G_t = \sum_{t'=t}^T \gamma^{t'-t} r_{t'} $$

**Option 2 — Also discount the gradient contributions:** $$ \nabla_\theta J \approx \sum_t \gamma^{t-1} \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot G_t $$

Option 2 is mathematically correct for a truly discounted objective (later decisions matter less). **In practice, people usually use Option 1** because we want good behavior at _all_ time steps, not just early ones.

---

## Batch Size of 1 Doesn't Work

The online actor-critic updates after every single transition:

1. Take action $a \sim \pi_\theta(\cdot|s)$, observe $r, s'$
2. Critic update: target = $r + \gamma V_\phi(s')$
3. Advantage: $\hat{A} = r + \gamma V_\phi(s') - V_\phi(s)$
4. Policy gradient step on this single sample

**Problem for deep RL:** Neural networks hate batch size 1. Updates are way too noisy.

---

## Parallelization

**Synchronized parallel:**

- Run $N$ environments in parallel
- Each takes one step → gather $N$ transitions
- Update with this batch
- Repeat

**Asynchronous (A3C-style):**

- Multiple workers run independently
- Each computes gradients and pushes to a shared model
- Gradients are slightly stale → small bias, but much faster

---

## On-Policy Methods Waste Data

On-policy methods throw away data after each policy update. Once $\pi_\theta$ changes, old transitions are "off-policy" and invalid.

**Question:** Can we reuse old transitions from a [[replay_buffer]]?

---

## The "Broken" Naive Off-Policy Algorithm
Before learning the solution, it is important to understand why we cannot simply use a [[replay_buffer]] with the standard Actor-Critic logic (Slides 21-23).

If we define a naive algorithm that samples a batch $(s_i, a_i, r_i, s_i')$ from a buffer and updates:
1. **The Critic:** $y_i = r_i + \gamma \hat{V}(s_i')$
2. **The Actor:** $\nabla J \approx \frac{1}{N} \sum \nabla \log \pi(a_i|s_i) \hat{A}(s_i, a_i)$

**This algorithm is broken for two reasons:**
1. **Wrong Target Value:** The target $r_i + \gamma \hat{V}(s_i')$ assumes that after $s_i'$, we will follow the *current* policy. However, $\hat{V}$ approximates the value of the *current* policy, but the transition $s_i \to s_i'$ might not reflect the current policy's dynamics if the buffer is old.
2. **Wrong Gradient Action:** The policy gradient theorem requires optimizing the action $a_i$ taken by the *current* policy $\pi_\theta$. The action $a_i$ in the buffer was sampled from an *old* policy $\pi_{old}$. Optimizing likelihood for actions we wouldn't take anymore is incorrect.

## Learn Q Instead of V

**Key insight:** The Q-function $Q(s,a)$ is valid for _any_ action, not just actions from the current policy. We can train it on old data.

### Learning Q from Replay

Store transitions $(s, a, r, s')$ in a [[replay_buffer]]. For each sampled batch:

1. Sample next action from _current_ policy: $a' \sim \pi_\theta(\cdot|s')$
2. Target: $y = r + \gamma Q_{\phi_{\text{old}}}(s', a')$
3. Regress $Q_\phi$ onto targets

The transition came from an old policy, but the target uses the _current_ policy's action $a'$.

### Policy Gradient with Off-Policy Critic

For each state $s_i$ in the batch:

1. Sample fresh action: $\tilde{a}_i \sim \pi_\theta(\cdot|s_i)$
2. Gradient estimate: $$ \hat{g} = \frac{1}{N} \sum_i \nabla_\theta \log \pi_\theta(\tilde{a}_i \mid s_i) \cdot Q_\phi(s_i, \tilde{a}_i) $$

We use $Q$ directly (no baseline) because we can cheaply sample many actions per state to reduce variance.

**Remaining bias:** The _states_ in the buffer came from old policies ($s \sim d^{\pi_{\text{old}}}$ instead of $s \sim d^{\pi_{\text{new}}}$). We can't easily fix this.

- **Why it's acceptable:** We want the optimal policy for the correct distribution, but we are learning on a **broader** distribution (the replay buffer contains history from many policies). As long as the buffer covers the states the current policy visits (plus more), we generally learn a valid policy.

This pattern underlies algorithms like **SAC** and **DDPG**.

In practical deep RL implementations, you'll often see two extra details:

- The policy-gradient term is frequently computed with the **reparameterization trick**. For a Gaussian actor, you write $a = \mu_\theta(s) + \sigma_\theta(s)\odot\epsilon$, with $\epsilon \sim \mathcal{N}(0,I)$, and backpropagate through $Q_\phi(s,a)$ instead of using only score-function gradients.
- There are many **fancier ways to fit $Q_\phi$** than the naïve regression above ([[target_network|target networks]], double Q-learning), which is why these ideas show up in modern algorithms like Soft Actor–Critic.

---

## What If We Want Zero Bias?

Using the critic as a return _replacement_ introduces bias (the critic is never perfect).

**Question:** Can we use the critic while keeping the gradient unbiased?

---

## Use Critic as Baseline Only

Instead of replacing returns, just subtract the critic as a baseline:

$$ \nabla_\theta J = \mathbb{E} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot (G_t - V_\phi(s_t)) \right] $$

**Key fact:** Any baseline that depends _only on state_ (not action) keeps the gradient unbiased: $$ \mathbb{E}_{a \sim \pi} \left[ \nabla_\theta \log \pi_\theta(a \mid s) \cdot b(s) \right] = 0 $$

Here you still use full Monte-Carlo returns $G_t$, but the critic turns them into advantage-like signals. Variance drops because you're subtracting the "expected" part and keeping only the deviation.

**Summary of two uses:**

- **Critic as return replacement:** Biased but low variance
- **Critic as baseline:** Unbiased, medium variance

### Action-Dependent Baselines (Control Variates)

If the baseline depends on action too, $B(s,a)$, you need a correction term: $$ \nabla_\theta J = \mathbb{E} \left[ \nabla_\theta \log \pi_\theta(a_t \mid s_t) \cdot (G_t - B(s_t, a_t)) \right] + \nabla_\theta \mathbb{E}_{a \sim \pi} \left[ B(s_t, a) \right] $$

The second term can often be computed analytically or with many action samples. This is **Q-Prop**.

---

## TD vs MC Is a Hard Choice

**One-step TD advantage** (max bias, min variance): $$ \hat{A}^{(1)}_t = r_t + \gamma V(s_{t+1}) - V(s_t) $$

**Monte-Carlo advantage** (min bias, max variance): $$ \hat{A}^{\text{MC}}_t = \sum_{t'=t}^\infty \gamma^{t'-t} r_{t'} - V(s_t) $$

**Question:** Can we get something in between?

---

## Solution: [[n_step_returns|N-Step Returns]] and GAE

See [[n_step_returns]] for the full treatment. The key ideas:

$$ \hat{A}^{(n)}_t = \left[ \sum_{l=0}^{n-1} \gamma^l r_{t+l} \right] + \gamma^n V(s_{t+n}) - V(s_t) $$

- $n=1$: Pure TD (max bias, min variance)
- $n \to \infty$: Pure Monte-Carlo (min bias, max variance)

**Generalized Advantage Estimation (GAE)** takes a weighted average of all n-step returns using the [[temporal_difference|TD residual]] $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$:

$$ \hat{A}_t^{\text{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l} $$

The parameter $\lambda \in [0,1]$ controls the bias-variance tradeoff. Practical sweet spot: $\lambda \in (0.9, 0.99)$.

---

## Practical Design Choices

|Dimension|Options|
|---|---|
|**What to learn**|$V$, $Q$, or $A$|
|**Fitting method**|Monte-Carlo, 1-step TD, n-step, GAE|
|**How critic is used**|Return replacement (biased) vs baseline (unbiased)|
|**Data usage**|On-policy vs off-policy + [[replay_buffer]]|
|**Architecture**|Separate actor/critic networks vs shared trunk|
|**Parallelism**|Synchronous vs asynchronous workers|

### Architecture Notes

**Two separate networks:** Simple, stable. Actor and critic have independent parameters.

**Shared trunk with two heads:** More efficient (shared features), but harder to train—actor and critic gradients have different scales and statistics.

---

## Summary

|Problem|Solution|
|---|---|
|REINFORCE has high variance|Learn a critic to estimate expected returns|
|How to learn the critic?|MC targets (unbiased) or TD targets (low variance)|
|Infinite horizons blow up|Discount factor $\gamma$|
|Batch size 1 too noisy|Parallel environments|
|On-policy wastes data|Off-policy with Q-function + [[replay_buffer]]|
|Want unbiased gradients|Use critic as baseline only|
|TD vs MC is a hard choice|[[n_step_returns]] or GAE|

**The critic doesn't solve RL—it gives the policy gradient a much cleaner learning signal.**