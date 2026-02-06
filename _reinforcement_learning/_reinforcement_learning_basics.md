# Reinforcement Learning Basics

## Introduction: Beyond Imitation

In the previous chapter, we explored **imitation learning**—training policies by mimicking expert demonstrations. We learned to map observations to actions through supervised learning, wrestling with distributional shift and architectural challenges. But this approach has a fundamental limitation: it can only reproduce behavior that exists in the training data.

What if we have no good demonstrations? What if the task is so novel that no expert has solved it before? What if we want to discover behaviors *better* than any human has achieved? These questions point to the need for a different paradigm—one where an agent learns not by copying, but by **trial and error**.

This is the domain of **reinforcement learning (RL)**. Instead of labeled demonstrations, we provide the agent with a **reward function** that specifies what outcomes are desirable. The agent interacts with its environment, observes the consequences of its actions, and gradually learns to maximize long-term reward. No explicit teacher is required—the reward signal itself guides the learning process.

```
                    FROM IMITATION TO REINFORCEMENT

    Imitation Learning:                 Reinforcement Learning:
    
    ┌──────────────────────┐            ┌──────────────────────┐
    │   Expert Demo        │            │   Reward Function    │
    │   (s, a) pairs       │            │   r(s, a) → ℝ        │
    └──────────┬───────────┘            └──────────┬───────────┘
               │                                   │
               ▼                                   ▼
    ┌──────────────────────┐            ┌──────────────────────┐
    │   Supervised         │            │   Trial & Error      │
    │   Learning           │            │   Exploration        │
    └──────────┬───────────┘            └──────────┬───────────┘
               │                                   │
               ▼                                   ▼
    ┌──────────────────────┐            ┌──────────────────────┐
    │   π(a|s) ≈ π*(a|s)   │            │   π(a|s) maximizes   │
    │   Copy expert        │            │   expected reward    │
    └──────────────────────┘            └──────────────────────┘
```

Consider autonomous driving. In imitation learning, we trained on expert driving data, and the best we could hope for was to match human performance. In reinforcement learning, we define what "good driving" means—perhaps staying on the road, reaching destinations efficiently, avoiding collisions—and let the agent discover how to achieve these goals. The agent might discover strategies humans never considered.

The transition from imitation to reinforcement learning requires new mathematical machinery. We need to formalize what it means for an agent to act in an environment over time, to accumulate rewards, and to optimize behavior. This chapter builds that foundation, introducing the **Markov decision process** as our mathematical model, defining the **RL objective**, exploring the **anatomy of RL algorithms**, and introducing **value functions** as a key conceptual tool.

---

## Part 1: The Markov Decision Process

### 1.1 From Static Predictions to Sequential Decisions

In supervised learning, each prediction is independent. We classify an image, then move on to the next, with no connection between predictions. In sequential decision-making, actions have consequences that unfold over time. Pressing the accelerator now affects where we are in ten seconds, which affects what decisions we face then.

To reason about sequential decisions, we need a mathematical model of how the world evolves. The foundation is the **Markov chain**—the simplest probabilistic model of a dynamical system.

#### The Markov Chain

A **Markov chain** $\mathcal{M} = \{\mathcal{S}, \mathcal{T}\}$ consists of two elements: a **state space** $\mathcal{S}$ containing all possible states $\mathbf{s} \in \mathcal{S}$ (which may be discrete or continuous), and a **transition operator** $\mathcal{T}$ that specifies how states evolve.

The transition operator defines a conditional distribution $p(\mathbf{s}_{t+1} | \mathbf{s}_t)$—the probability of transitioning to state $\mathbf{s}_{t+1}$ given that we are currently in state $\mathbf{s}_t$. This is called a **transition probability** or **transition dynamics**.

```
                    MARKOV CHAIN
                    
          p(s₂|s₁)           p(s₃|s₂)           p(s₄|s₃)
    (s₁) ─────────► (s₂) ─────────► (s₃) ─────────► (s₄)
    
    
    Time:   t=1           t=2           t=3           t=4
```

The crucial property is the **Markov property**: the future is independent of the past given the present. Formally:

$$\mathbf{s}_{t+1} \perp \mathbf{s}_{1:t-1} \mid \mathbf{s}_t$$

In words: if we know the current state, knowing the history provides no additional information for predicting the next state. The state captures all relevant information about the system.

#### State Marginals and the Transition Operator

Given an initial distribution $p(\mathbf{s}_1)$ over states and the transition dynamics, we can compute the **state marginal** at any time $t$—the probability distribution over states at time $t$. This computation involves marginalizing over all possible paths:

$$p(\mathbf{s}_{t+1}) = \sum_{\mathbf{s}_t} p(\mathbf{s}_{t+1} | \mathbf{s}_t) p(\mathbf{s}_t)$$

This equation reveals why we call $\mathcal{T}$ an "operator": it acts on probability distributions to produce new probability distributions. For discrete state spaces, if we represent the state marginal at time $t$ as a vector $\mu_t$ (where entry $i$ is $p(\mathbf{s}_t = i)$), then:

$$\mu_{t+1} = \mathcal{T} \mu_t$$

where $\mathcal{T}_{i,j} = p(\mathbf{s}_{t+1} = i | \mathbf{s}_t = j)$ is the transition matrix. This linear algebraic view will prove important when we analyze RL algorithms theoretically.

```
                    TRANSITION OPERATOR AS MATRIX
                    
    Current state marginal:           Next state marginal:
    
         ┌ p(sₜ = 1) ┐                     ┌ p(sₜ₊₁ = 1) ┐
    μₜ = │ p(sₜ = 2) │      𝒯         μₜ₊₁ = │ p(sₜ₊₁ = 2) │
         │    ...    │   ──────►           │     ...     │
         └ p(sₜ = n) ┘                     └ p(sₜ₊₁ = n) ┘
         
                        μₜ₊₁ = 𝒯 μₜ
```

---

### 1.2 Adding Actions: The Markov Decision Process

A Markov chain models systems that evolve on their own, like weather patterns or stock prices (approximately). But we want to model agents that take **actions** to influence outcomes. This leads to the **Markov decision process (MDP)**.

A **Markov decision process** $\mathcal{M} = \{\mathcal{S}, \mathcal{A}, \mathcal{T}, r\}$ extends the Markov chain with two new elements: an **action space** $\mathcal{A}$ containing all possible actions $\mathbf{a} \in \mathcal{A}$, and a **reward function** $r : \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ that assigns a scalar reward to each state-action pair.

The transition operator now conditions on actions: $p(\mathbf{s}_{t+1} | \mathbf{s}_t, \mathbf{a}_t)$. The next state depends on both where we are and what we do.

```
                    MARKOV DECISION PROCESS
                    
                        (a₁)            (a₂)            (a₃)
                          │               │               │
                          │               │               │
                          ▼               ▼               ▼
    p(s₂|s₁,a₁)      p(s₃|s₂,a₂)      p(s₄|s₃,a₃)
    (s₁) ────────► (s₂) ────────► (s₃) ────────► (s₄)
    
    
    At each state sₜ, agent chooses action aₜ
    Transition depends on BOTH state and action
    Reward r(sₜ, aₜ) received at each step
```

The reward function is central to RL. It encodes what we want the agent to achieve. For driving, $r(\mathbf{s}, \mathbf{a})$ might give positive reward for making progress toward a destination and negative reward for collisions. The reward function replaces the expert demonstrations of imitation learning.

```
                    REWARD FUNCTION EXAMPLES
                    
    ┌────────────────────────────────────────────────────────┐
    │                                                        │
    │   🚗 Safe driving               🚗💥 Collision          │
    │   r(s, a) = +1                  r(s, a) = -100         │
    │   (high reward)                 (low reward)           │
    │                                                        │
    └────────────────────────────────────────────────────────┘
    
    The reward function tells us which states and actions are better.
    By the time you're about to hit someone, it's too late!
    → Need to optimize for LONG-TERM reward, not just immediate.
```

#### Turning an MDP into a Markov Chain

Here's a key insight: once we fix a **policy** $\pi_\theta(\mathbf{a} | \mathbf{s})$—a distribution over actions given states—an MDP becomes a Markov chain. The combined state-action tuple $(\mathbf{s}_t, \mathbf{a}_t)$ evolves according to:

$$p((\mathbf{s}_{t+1}, \mathbf{a}_{t+1}) | (\mathbf{s}_t, \mathbf{a}_t)) = p(\mathbf{s}_{t+1} | \mathbf{s}_t, \mathbf{a}_t) \cdot \pi_\theta(\mathbf{a}_{t+1} | \mathbf{s}_{t+1})$$

```
                    MDP + POLICY = MARKOV CHAIN
                    
    MDP (actions undetermined):        With policy π(a|s):
    
         (a₁)       (a₂)       (a₃)         ┌────┐     ┌────┐     ┌────┐
           ?          ?          ?          │ a₁ │     │ a₂ │     │ a₃ │
           │          │          │          └──┬─┘     └──┬─┘     └──┬─┘
    (s₁)───►(s₂)───►(s₃)───►(s₄)         ┌──┴─┐     ┌──┴─┐     ┌──┴─┐
                                          │ s₁ │────►│ s₂ │────►│ s₃ │
                                          └────┘     └────┘     └────┘
                                          
    Actions are "free variables"          Combined (s,a) pairs form
                                          a Markov chain!
```

This observation is fundamental: the policy determines the distribution over trajectories, and analyzing this distribution is the key to understanding RL.

---

### 1.3 Partial Observability

So far, we assumed the agent observes the full state $\mathbf{s}_t$. In practice, agents often have incomplete information. A robot sees pixels from its camera, not the exact positions and velocities of all objects. A self-driving car doesn't know other drivers' intentions.

A **partially observed Markov decision process (POMDP)** $\mathcal{M} = \{\mathcal{S}, \mathcal{A}, \mathcal{O}, \mathcal{T}, \mathcal{E}, r\}$ adds an **observation space** $\mathcal{O}$ and an **emission operator** $\mathcal{E}$ that generates observations from states: $p(\mathbf{o}_t | \mathbf{s}_t)$.

```
                    POMDP GRAPHICAL MODEL
                    
                    (o₁)     (o₂)     (o₃)    ← Observations
                      ↑        ↑        ↑       (what agent sees)
                      │        │        │
                    (s₁)────►(s₂)────►(s₃)    ← Hidden states
                      │        │        │       (true world state)
                      │        │        │
                      ↓        ↓        ↓
                    (a₁)     (a₂)     (a₃)    ← Actions
    
    The agent sees observations o, not states s
    Must infer about hidden state from observation history
```

In a POMDP, the policy cannot simply condition on $\mathbf{s}_t$ (which is hidden). Instead, it must condition on the observation history or some sufficient statistic thereof. This is why sequence models—like the Transformers we discussed for imitation learning—are valuable: they can maintain implicit beliefs about hidden state.

**For the remainder of this chapter, we focus on the fully observed case (MDPs).** The core RL concepts translate to POMDPs, but the exposition is cleaner with full observability.

---

### 1.4 Trajectories and Marginals

With the MDP defined and a policy fixed, we can write down the distribution over **trajectories**—sequences of states and actions.

A trajectory $\tau = (\mathbf{s}_1, \mathbf{a}_1, \mathbf{s}_2, \mathbf{a}_2, \ldots, \mathbf{s}_H, \mathbf{a}_H)$ is a complete sequence over horizon $H$. The **trajectory distribution** factorizes as:

$$p_\theta(\mathbf{s}_1, \mathbf{a}_1, \ldots, \mathbf{s}_H, \mathbf{a}_H) = p(\mathbf{s}_1) \prod_{t=1}^{H} \pi_\theta(\mathbf{a}_t | \mathbf{s}_t) p(\mathbf{s}_{t+1} | \mathbf{s}_t, \mathbf{a}_t)$$

We denote this compactly as $p_\theta(\tau)$. Note that $\theta$ appears in the subscript because the policy parameters influence the trajectory distribution through the $\pi_\theta$ terms.

```
                    TRAJECTORY DISTRIBUTION
                    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │  p_θ(τ) = p(s₁) × π_θ(a₁|s₁) × p(s₂|s₁,a₁)                 │
    │                × π_θ(a₂|s₂) × p(s₃|s₂,a₂)                  │
    │                × ...                                        │
    │                × π_θ(aₕ|sₕ)                                 │
    │                                                             │
    │         ┌───────┐     ┌───────┐     ┌───────┐              │
    │         │Initial│     │ Policy│     │Dynamics│              │
    │         │ dist. │  ×  │ terms │  ×  │ terms  │              │
    │         └───────┘     └───────┘     └───────┘              │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

#### State-Action Marginals

Often we care not about entire trajectories but about the distribution over states (or state-action pairs) at particular times. The **state marginal** at time $t$ is:

$$p_\theta(\mathbf{s}_t) = \sum_{\mathbf{a}_{1:t-1}, \mathbf{s}_{1:t-1}} p(\mathbf{s}_1) \prod_{t'=1}^{t-1} \pi_\theta(\mathbf{a}_{t'} | \mathbf{s}_{t'}) p(\mathbf{s}_{t'+1} | \mathbf{s}_{t'}, \mathbf{a}_{t'})$$

This looks intimidating, but recall our earlier insight: with a fixed policy, we have a Markov chain. So $p_\theta(\mathbf{s}_t)$ is simply $\mu_t = \mathcal{T}_\theta^{t-1} \mu_1$, where $\mathcal{T}_\theta$ is the transition operator of the induced Markov chain.

The **state-action marginal** is the joint distribution over state and action at time $t$:

$$p_\theta(\mathbf{s}_t, \mathbf{a}_t) = \pi_\theta(\mathbf{a}_t | \mathbf{s}_t) \cdot p_\theta(\mathbf{s}_t)$$

**Sampling from marginals:** While computing marginals analytically requires expensive summations, *sampling* is easy. To get samples from $p_\theta(\mathbf{s}_t)$, simply run the policy in the environment for $t$ steps and record $\mathbf{s}_t$. This "simulation" approach to computing expectations is central to RL algorithms.

---

## Part 2: Defining the RL Objective

### 2.1 Maximizing Long-Term Reward

With the mathematical machinery in place, we can state the RL objective precisely. We want to find policy parameters $\theta$ that maximize expected cumulative reward:

$$\theta^* = \arg\max_\theta \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{H} r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

Let's unpack this. The expectation is over trajectories drawn from the trajectory distribution $p_\theta(\tau)$, which depends on the policy through $\theta$. Inside the expectation, we sum rewards over all timesteps. The objective is to find parameters that maximize this expected sum.

Why the expectation? Because both the policy (if stochastic) and the environment dynamics (if stochastic) introduce randomness. The same policy might produce different trajectories on different runs. We optimize average performance.

Why the sum over time? Because we care about long-term outcomes, not just immediate rewards. A chess player sacrifices a pawn (negative immediate reward) to set up checkmate (large positive reward later). The sum captures this temporal credit assignment.

```
                    THE RL OBJECTIVE
                    
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │              H                                            │
    │   J(θ) = 𝔼   [ Σ  r(sₜ, aₜ) ]    ← Expected total reward │
    │         τ~p_θ  t=1                                        │
    │                                                           │
    │   θ* = arg max J(θ)              ← Optimal parameters     │
    │            θ                                              │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
    
    Key insight: Actions affect future STATES, not just immediate rewards
    
    Time:     t=1     t=2     t=3     t=4     ...     t=H
              │       │       │       │               │
    Rewards:  r₁  +   r₂  +   r₃  +   r₄  +  ...  +  rₕ
              └───────┴───────┴───────┴───────────────┘
                    Sum these to get return R(τ)
```

---

### 2.2 The Markov Chain View

We can rewrite the RL objective in terms of state-action marginals:

$$\mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{H} r(\mathbf{s}_t, \mathbf{a}_t)\right] = \sum_{t=1}^{H} \mathbb{E}_{(\mathbf{s}_t, \mathbf{a}_t) \sim p_\theta(\mathbf{s}_t, \mathbf{a}_t)}\left[r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

This follows from linearity of expectation. The left side takes expectations over full trajectories; the right side takes expectations over marginals at each timestep, then sums.

Using our vector notation for discrete states and actions, let $\vec{r}$ be a vector with entry $r(\mathbf{s} = i, \mathbf{a} = j)$ for each state-action pair. Let $\mu_t$ be the state-action marginal at time $t$, represented as a vector. Then:

$$\sum_{t=1}^{H} \mathbb{E}_{p_\theta(\mathbf{s}_t, \mathbf{a}_t)}\left[r(\mathbf{s}_t, \mathbf{a}_t)\right] = \sum_{t=1}^{H} \mu_t^T \vec{r}$$

Since $\mu_t = \mathcal{T}_\theta^{t-1} \mu_1$ (applying the transition operator $t-1$ times to the initial distribution), we get:

$$\sum_{t=1}^{H} \mu_t^T \vec{r} = \left[\sum_{t=1}^{H} \mathcal{T}_\theta^{t-1} \mu_1\right]^T \vec{r}$$

```
                    MARKOV CHAIN VIEW OF RL OBJECTIVE
                    
    Trajectory view:              Marginal view:
    
    𝔼      [ r₁ + r₂ + ... + rₕ ]     =    𝔼   [r₁] + 𝔼   [r₂] + ...
     τ~p_θ                               μ₁       μ₂
    
    Full trajectory                    Sum of per-timestep
    expectation                        marginal expectations
    
    
    In vector form:
    
    ┌ p(s=1, a=1) ┐        ┌ r(s=1, a=1) ┐
    │ p(s=1, a=2) │        │ r(s=1, a=2) │
    │     ...     │   ·    │     ...     │   =   𝔼[r]
    │ p(s=n, a=m) │        │ r(s=n, a=m) │
    └─────────────┘        └─────────────┘
          μₜ                    r⃗
          
                    μₜᵀ r⃗  =  expected reward at time t
```

This linear algebraic perspective, while abstract, provides insight into RL theory. It shows that the RL objective depends on the policy only through the state-action marginals it induces.

---

### 2.3 Infinite Horizon and Stationary Distributions

What happens as the horizon $H \to \infty$? The sum of rewards might diverge. To handle this, we often introduce a **discount factor** $\gamma \in (0, 1)$ and consider:

$$J(\theta) = \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

The discount factor serves multiple purposes. Mathematically, it ensures convergence (the sum is bounded by $\frac{R_{\max}}{1-\gamma}$ where $R_{\max}$ is the maximum reward). Economically, it models preference for immediate over delayed rewards. Practically, it reduces variance in gradient estimates by downweighting distant (and hard to predict) rewards.

Alternatively, consider the average reward as $H \to \infty$:

$$\lim_{H \to \infty} \frac{1}{H} \sum_{t=1}^{H} \mathbb{E}_{p_\theta(\mathbf{s}_t, \mathbf{a}_t)}\left[r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

Under certain regularity conditions (ergodicity), the state-action marginal $p_\theta(\mathbf{s}_t, \mathbf{a}_t)$ converges to a **stationary distribution** $\bar{\mu}$ that satisfies:

$$\bar{\mu} = \mathcal{T}_\theta \bar{\mu}$$

That is, $\bar{\mu}$ is a fixed point of the transition operator—applying one transition leaves the distribution unchanged. Equivalently, $\bar{\mu}$ is an eigenvector of $\mathcal{T}_\theta$ with eigenvalue 1.

```
                    STATIONARY DISTRIBUTION
                    
    Starting from any initial distribution μ₁:
    
    μ₁ ──𝒯──► μ₂ ──𝒯──► μ₃ ──𝒯──► ... ──𝒯──► μ̄
    
    After many transitions, converge to stationary distribution μ̄
    
    μ̄ = 𝒯 μ̄     (μ̄ unchanged by transition)
    
    (𝒯 - I) μ̄ = 0    (μ̄ is eigenvector with eigenvalue 1)
    
    
    Infinite horizon average reward:
    
         1   H
    lim  ─   Σ  𝔼   [r(sₜ,aₜ)]  =  𝔼    [r(s,a)]  =  μ̄ᵀ r⃗
    H→∞  H  t=1  μₜ                 μ̄
```

While we rarely solve for stationary distributions directly in practical RL algorithms, this analysis provides theoretical grounding and intuition for algorithm design.

---

### 2.4 Why Expectations Matter

A subtle but important point: in RL, we almost always care about **expectations**. The reward function $r(\mathbf{s}, \mathbf{a})$ may be non-smooth or even discontinuous. Falling off a cliff might give reward $-1$ while staying on solid ground gives $+1$—a discontinuous jump. But the *expected* reward under a stochastic policy is smooth in the policy parameters.

Consider a simple example: an agent at a cliff edge with parameter $\theta$ controlling the probability of falling:

$$\pi_\theta(\mathbf{a} = \text{fall}) = \theta, \quad r(\text{fall}) = -1, \quad r(\text{stay}) = +1$$

The reward function is not differentiable in the action. But the expected reward is:

$$\mathbb{E}_{\pi_\theta}[r] = \theta \cdot (-1) + (1-\theta) \cdot (+1) = 1 - 2\theta$$

This is smooth (linear) in $\theta$, and we can compute gradients with respect to policy parameters even though rewards are discontinuous.

```
                    SMOOTHING VIA EXPECTATIONS
                    
    Reward function r(s, a):          Expected reward 𝔼[r]:
    
       +1 ─────┐                         +1 ─────╲
               │                                  ╲
               │ Jump at cliff edge               ╲  Smooth in θ!
               │                                   ╲
       -1 ─────┘                         -1 ────────
           stay   fall                        0     1
           (action)                           θ (policy parameter)
    
    Stochastic policies smooth out discontinuities in reward landscape
```

This smoothing property is why stochastic policies and expectations are central to RL theory, even when we ultimately want deterministic behavior.

---

## Part 3: The Anatomy of an RL Algorithm

### 3.1 The Three-Step Loop

Despite the diversity of RL algorithms, most share a common high-level structure. The **anatomy of an RL algorithm** consists of three repeating steps:

```
                    THE RL ALGORITHM LOOP
                    
                ┌─────────────────────────────────────┐
                │                                     │
                │      ┌───────────────────┐          │
                │      │  1. GENERATE      │          │
                │      │     SAMPLES       │          │
                │      │  (run policy)     │◄─────────┤
                │      └────────┬──────────┘          │
                │               │                     │
                │               ▼                     │
                │      ┌───────────────────┐          │
                │      │  2. FIT MODEL /   │          │
                │      │     ESTIMATE      │          │
                │      │     RETURN        │          │
                │      └────────┬──────────┘          │
                │               │                     │
                │               ▼                     │
                │      ┌───────────────────┐          │
                │      │  3. IMPROVE       │          │
                │      │     POLICY        │──────────┘
                │      └───────────────────┘
                │
                └─────────────────────────────────────┘
```

**Step 1: Generate Samples.** Run the current policy in the environment (or a simulator) to collect experience. This produces trajectories or transitions $(\mathbf{s}, \mathbf{a}, r, \mathbf{s}')$ that reveal how the policy performs.

**Step 2: Fit a Model or Estimate Return.** Use the samples to learn something useful: the expected return, a value function, a dynamics model, or some other quantity. This step extracts signal from the raw experience.

**Step 3: Improve the Policy.** Use the learned quantities to update the policy parameters, hopefully increasing expected reward.

Different RL algorithms instantiate these steps differently. In a simple **policy gradient** method:
- Step 1: Collect trajectories by running $\pi_\theta$
- Step 2: Compute the total return $R_\tau = \sum_t r_t$ for each trajectory  
- Step 3: Update $\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)$

In **model-based RL**:
- Step 1: Collect transitions $(\mathbf{s}, \mathbf{a}, \mathbf{s}')$
- Step 2: Fit a dynamics model $f_\phi(\mathbf{s}, \mathbf{a}) \approx \mathbf{s}'$
- Step 3: Use the model to plan or compute policy gradients

---

### 3.2 A Simple Example: Direct Policy Search

The simplest instantiation uses the loop directly for gradient-based optimization:

```
                    SIMPLE POLICY GRADIENT
                    
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   1. Generate Samples:                                     │
    │      Run π_θ for N trajectories, collect {τ₁, τ₂, ..., τₙ}│
    │                                                            │
    │   2. Estimate Return:                                      │
    │                    1   N                                   │
    │      J(θ) ≈ ──   Σ   R(τᵢ)     where R(τ) = Σₜ rₜ        │
    │                N  i=1                                      │
    │                                                            │
    │   3. Improve Policy:                                       │
    │      θ ← θ + α ∇_θ J(θ)                                   │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
```

The challenge is Step 3: how do we compute $\nabla_\theta J(\theta)$? The objective depends on $\theta$ through the trajectory distribution $p_\theta(\tau)$, which involves the stochastic policy and environment dynamics. We'll address this in later chapters when we cover policy gradient algorithms.

---

### 3.3 Another Example: RL by Backpropagation

If we have a differentiable dynamics model, we can backpropagate through time:

```
                    RL BY BACKPROPAGATION
                    
    1. Generate Samples:
       Collect transitions (s, a, s')
       
    2. Fit Model:
       Learn f_φ such that s_{t+1} ≈ f_φ(s_t, a_t)
       
       ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐
       │ sₜ  │──►│     │──►│     │──►│sₜ₊₁ │
       │     │   │ f_φ │   │     │   │     │
       │ aₜ  │──►│     │   │     │   │     │
       └─────┘   └─────┘   └─────┘   └─────┘
       
    3. Improve Policy:
       Backprop through f_φ and r to train π_θ(s) = a
       
       ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   ┌───┐
       │ sₜ  │──►│ π_θ │──►│ f_φ │──►│sₜ₊₁ │──►│ r │──► Reward
       └─────┘   └─────┘   └─────┘   └─────┘   └───┘
                    ▲                           │
                    └───────────────────────────┘
                         Backpropagate gradient
```

This approach learns the dynamics and uses gradient descent on a "computational graph" that includes both policy and model. The challenge is that errors in the model compound over long horizons, and the approach requires differentiable dynamics (ruling out contact-rich tasks with discontinuities).

---

### 3.4 Which Parts Are Expensive?

Understanding computational costs guides algorithm design:

```
                    COMPUTATIONAL COSTS
                    
    ┌───────────────────┬─────────────────────────────────┐
    │  STEP             │  COST                           │
    ├───────────────────┼─────────────────────────────────┤
    │                   │                                 │
    │  1. Generate      │  Real robot: 1× real time      │
    │     Samples       │  (can't speed up physics!)     │
    │                   │                                 │
    │                   │  Fast simulator: up to 10000×  │
    │                   │  real time                     │
    │                   │                                 │
    ├───────────────────┼─────────────────────────────────┤
    │                   │                                 │
    │  2. Estimate      │  Trivial if just summing       │
    │     Return        │  rewards                       │
    │                   │                                 │
    │                   │  Expensive if fitting a model  │
    │                   │  (neural network training)     │
    │                   │                                 │
    ├───────────────────┼─────────────────────────────────┤
    │                   │                                 │
    │  3. Improve       │  One gradient step: trivial    │
    │     Policy        │                                 │
    │                   │  Planning with model:          │
    │                   │  expensive                     │
    │                   │                                 │
    └───────────────────┴─────────────────────────────────┘
```

The critical bottleneck in real-world RL is **sample generation**. When interacting with physical systems—robots, autonomous vehicles, power grids—data collection runs at real time. We cannot speed up physics. This motivates **sample efficiency**: getting good policies with minimal environment interaction.

In contrast, with fast simulators, we can generate millions of samples quickly, and the bottleneck shifts to computation (fitting models, updating policies). Different algorithm choices are appropriate for different regimes.

---

## Part 4: Value Functions and Q-Functions

### 4.1 Handling Expectations with Temporal Structure

The RL objective involves nested expectations over long horizons:

$$\mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{H} r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

Expanding this for even a short horizon reveals complexity. For $H=3$:

$$\mathbb{E}_{\mathbf{s}_1 \sim p(\mathbf{s}_1)} \mathbb{E}_{\mathbf{a}_1 \sim \pi(\mathbf{a}_1 | \mathbf{s}_1)} \left[ r(\mathbf{s}_1, \mathbf{a}_1) + \mathbb{E}_{\mathbf{s}_2 \sim p(\mathbf{s}_2 | \mathbf{s}_1, \mathbf{a}_1)} \left[ \ldots \right] \right]$$

The key insight is that these expectations have **recursive structure**. If we knew the expected reward-to-go from any state-action pair, we could simplify optimization dramatically.

---

### 4.2 The Q-Function

The **Q-function** (or action-value function) captures this recursive structure. For a policy $\pi$, the Q-function is defined as:

$$Q^\pi(\mathbf{s}_t, \mathbf{a}_t) = \sum_{t'=t}^{H} \mathbb{E}_{\pi}\left[r(\mathbf{s}_{t'}, \mathbf{a}_{t'}) \mid \mathbf{s}_t, \mathbf{a}_t\right]$$

In words: $Q^\pi(\mathbf{s}, \mathbf{a})$ is the expected total reward from taking action $\mathbf{a}$ in state $\mathbf{s}$, then following policy $\pi$ thereafter.

```
                    Q-FUNCTION DEFINITION
                    
    Q^π(sₜ, aₜ) = Expected total reward from (sₜ, aₜ) onward
    
    
    Time:    t      t+1     t+2     t+3    ...     H
             │       │       │       │              │
             ▼       ▼       ▼       ▼              ▼
    
         (sₜ,aₜ) → (sₜ₊₁,aₜ₊₁) → (sₜ₊₂,aₜ₊₂) → ... → (sₕ,aₕ)
             │         │           │                    │
             ▼         ▼           ▼                    ▼
             rₜ   +   rₜ₊₁   +   rₜ₊₂   +  ...  +    rₕ
             └─────────────────────────────────────────┘
                              Q^π(sₜ, aₜ)
                              
    The current (sₜ, aₜ) is fixed; future actions follow π
```

Why is this useful? If we know $Q^\pi$, we can evaluate whether an action is better than what $\pi$ would typically do. And we can *improve* the policy by selecting actions with higher Q-values.

---

### 4.3 The Value Function

The **value function** (or state-value function) is the expected Q-value under the policy:

$$V^\pi(\mathbf{s}_t) = \mathbb{E}_{\mathbf{a}_t \sim \pi(\mathbf{a}_t | \mathbf{s}_t)}\left[Q^\pi(\mathbf{s}_t, \mathbf{a}_t)\right] = \sum_{t'=t}^{H} \mathbb{E}_{\pi}\left[r(\mathbf{s}_{t'}, \mathbf{a}_{t'}) \mid \mathbf{s}_t\right]$$

The value function tells us how good it is to *be* in a state, averaging over actions the policy would take. The relationship between $V^\pi$ and $Q^\pi$ is:

$$V^\pi(\mathbf{s}) = \mathbb{E}_{\mathbf{a} \sim \pi(\mathbf{a} | \mathbf{s})}\left[Q^\pi(\mathbf{s}, \mathbf{a})\right]$$

And the RL objective can be expressed as:

$$\mathbb{E}_{\mathbf{s}_1 \sim p(\mathbf{s}_1)}\left[V^\pi(\mathbf{s}_1)\right]$$

The expected value of the start state is exactly the RL objective!

```
                    VALUE FUNCTION AND Q-FUNCTION
                    
    V^π(s) = 𝔼_{a~π(a|s)} [ Q^π(s, a) ]
    
    
                          Q^π(s, a₁)
                         ╱
              ┌───┐     ╱
          s ──│ π │────●─── Q^π(s, a₂)    V^π(s) = weighted
              └───┘     ╲                  average of Q-values
                         ╲
                          Q^π(s, a₃)
                          
                          
    RL Objective = 𝔼_{s₁~p(s₁)} [ V^π(s₁) ]
    
    Value of being in start states = total expected reward!
```

---

### 4.4 Using Q-Functions for Policy Improvement

The real power of Q-functions emerges in policy improvement. Given $Q^\pi$ for the current policy $\pi$, we can construct a better policy $\pi'$.

**Idea 1: Greedy Policy.** Set the new policy to always take the action with highest Q-value:

$$\pi'(\mathbf{a} | \mathbf{s}) = \begin{cases} 1 & \text{if } \mathbf{a} = \arg\max_{\mathbf{a}'} Q^\pi(\mathbf{s}, \mathbf{a}') \\ 0 & \text{otherwise} \end{cases}$$

This policy is at least as good as $\pi$, and typically better. Crucially, it doesn't matter what $\pi$ was—once we have the Q-function, we can improve.

**Idea 2: Policy Gradient with Advantage.** Define the **advantage function**:

$$A^\pi(\mathbf{s}, \mathbf{a}) = Q^\pi(\mathbf{s}, \mathbf{a}) - V^\pi(\mathbf{s})$$

The advantage measures how much better action $\mathbf{a}$ is compared to the average action under $\pi$. Modify $\pi$ to increase the probability of actions with positive advantage.

```
                    POLICY IMPROVEMENT WITH Q-FUNCTIONS
                    
    Current policy π with Q-function Q^π(s, a):
    
    ┌────────────────────────────────────────────────────┐
    │  IDEA 1: Greedy Improvement                        │
    │                                                    │
    │  π'(a|s) = 1  if  a = arg max Q^π(s, a')          │
    │                          a'                        │
    │                                                    │
    │  Always pick the best action according to Q^π     │
    │  This policy is guaranteed to be ≥ as good as π!  │
    └────────────────────────────────────────────────────┘
    
    ┌────────────────────────────────────────────────────┐
    │  IDEA 2: Advantage-Weighted Improvement            │
    │                                                    │
    │  A^π(s, a) = Q^π(s, a) - V^π(s)   ← Advantage     │
    │                                                    │
    │  If A^π(s, a) > 0: action a is better than average│
    │  If A^π(s, a) < 0: action a is worse than average │
    │                                                    │
    │  Increase π(a|s) for positive-advantage actions   │
    └────────────────────────────────────────────────────┘
```

These ideas—using Q-functions for policy improvement—are central to RL. We'll revisit them repeatedly in later chapters when we cover specific algorithms.

---

## Part 5: Types of RL Algorithms

### 5.1 A Taxonomy

RL algorithms can be categorized by how they instantiate the three-step loop, particularly how they estimate return (Step 2) and improve the policy (Step 3). The main categories are:

```
                    TAXONOMY OF RL ALGORITHMS
                    
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │  1. POLICY GRADIENT                                       │
    │     Directly differentiate the RL objective w.r.t. θ     │
    │     Examples: REINFORCE, PPO                             │
    │                                                           │
    │  2. VALUE-BASED                                           │
    │     Estimate Q* or V* of the OPTIMAL policy              │
    │     Extract policy by taking arg max of Q*               │
    │     No explicit policy network (policy is implicit)      │
    │     Examples: Q-learning, DQN                            │
    │                                                           │
    │  3. ACTOR-CRITIC                                          │
    │     Estimate Q^π or V^π of the CURRENT policy            │
    │     Use value estimates to compute policy gradients      │
    │     Both policy (actor) and value (critic) networks      │
    │     Examples: A3C, SAC                                   │
    │                                                           │
    │  4. MODEL-BASED                                           │
    │     Estimate the dynamics model p(s'|s, a)               │
    │     Use the model for:                                   │
    │       - Planning (no explicit policy)                    │
    │       - Backpropagating gradients to policy              │
    │       - Generating synthetic experience                  │
    │     Examples: Dyna, MuZero                               │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

Let's examine each category in more detail.

---

### 5.2 Policy Gradient Methods

**Policy gradient** methods directly optimize the RL objective by computing gradients with respect to policy parameters:

$$\theta \leftarrow \theta + \alpha \nabla_\theta \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_t r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

The challenge is computing this gradient when the expectation is over a distribution that depends on $\theta$. The famous **policy gradient theorem** provides a solution (covered in later chapters).

```
                    POLICY GRADIENT ALGORITHM
                    
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   Generate samples:   Collect trajectories {τᵢ} from π_θ  │
    │                                                            │
    │   Estimate return:    Compute R(τᵢ) = Σₜ r(sₜ, aₜ)        │
    │                                                            │
    │   Improve policy:     θ ← θ + α ∇_θ 𝔼[Σₜ r(sₜ, aₜ)]      │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
    
    Pro: Directly optimizes the objective we care about
    Con: Often requires many samples (high variance gradients)
```

---

### 5.3 Value-Based Methods

**Value-based** methods don't maintain an explicit policy network. Instead, they estimate the Q-function of the *optimal* policy, denoted $Q^*$. The optimal policy is then:

$$\pi^*(\mathbf{a} | \mathbf{s}) = \begin{cases} 1 & \text{if } \mathbf{a} = \arg\max_{\mathbf{a}'} Q^*(\mathbf{s}, \mathbf{a}') \\ 0 & \text{otherwise} \end{cases}$$

```
                    VALUE-BASED ALGORITHM
                    
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   Generate samples:   Collect transitions (s, a, r, s')   │
    │                       using some exploration policy       │
    │                                                            │
    │   Estimate return:    Fit Q(s, a) ≈ Q*(s, a)              │
    │                       (using Bellman equations)           │
    │                                                            │
    │   Improve policy:     π(s) = arg max_a Q(s, a)            │
    │                       (implicit, no gradient step!)       │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
    
    Pro: Can reuse data efficiently (off-policy)
    Con: Limited to discrete actions (arg max intractable for continuous)
```

---

### 5.4 Actor-Critic Methods

**Actor-critic** methods combine ideas from both approaches. They maintain both a policy network (the "actor") and a value network (the "critic"). The critic estimates $Q^\pi$ or $V^\pi$ for the *current* policy (not the optimal one). The actor is improved using information from the critic.

```
                    ACTOR-CRITIC ALGORITHM
                    
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   Generate samples:   Collect transitions using π_θ       │
    │                                                            │
    │   Estimate return:    Fit V(s) ≈ V^π(s) or               │
    │   (CRITIC)            Fit Q(s,a) ≈ Q^π(s, a)             │
    │                                                            │
    │   Improve policy:     θ ← θ + α ∇_θ 𝔼[Q(s, a)]           │
    │   (ACTOR)             (gradient uses critic's estimate)   │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
    
    ┌──────────────────────────────────────────────────────────┐
    │                                                          │
    │   ┌─────────┐         ┌─────────┐                       │
    │   │  ACTOR  │ ──────► │  CRITIC │                       │
    │   │   π_θ   │         │  V_φ    │                       │
    │   └────┬────┘         └────┬────┘                       │
    │        │                   │                            │
    │        │ actions           │ value estimates            │
    │        ▼                   ▼                            │
    │   ┌───────────────────────────────────────┐             │
    │   │          ENVIRONMENT                   │             │
    │   └───────────────────────────────────────┘             │
    │                                                          │
    └──────────────────────────────────────────────────────────┘
    
    Pro: Lower variance than pure policy gradient
    Pro: Works with continuous actions (unlike pure value-based)
```

---

### 5.5 Model-Based Methods

**Model-based** methods learn a dynamics model $p_\phi(\mathbf{s}' | \mathbf{s}, \mathbf{a})$ (or a deterministic approximation $\mathbf{s}' \approx f_\phi(\mathbf{s}, \mathbf{a})$). The model can then be used in several ways:

```
                    MODEL-BASED RL
                    
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   Generate samples:   Collect transitions (s, a, s')      │
    │                                                            │
    │   Fit model:          Learn f_φ(s, a) ≈ s'                │
    │                       (supervised learning!)              │
    │                                                            │
    │   Improve policy:     Multiple options:                   │
    │                                                            │
    │     Option A: PLANNING (no explicit policy)               │
    │       - Trajectory optimization (continuous actions)      │
    │       - Tree search (discrete actions, e.g., MCTS)       │
    │                                                            │
    │     Option B: BACKPROP through model                      │
    │       - Compute ∇_θ J using differentiable model         │
    │       - Update policy by gradient descent                 │
    │                                                            │
    │     Option C: Use model for VALUE LEARNING                │
    │       - Dynamic programming with model                    │
    │       - Generate synthetic experience for model-free RL   │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
    
    Pro: Very sample efficient (model can generalize)
    Con: Model errors can compound over long horizons
```

---

### 5.6 Comparison: Sample Efficiency

**Sample efficiency** measures how much environment interaction is needed to learn a good policy. This is critical when data collection is expensive (real robots, clinical trials, etc.).

The most important factor is whether an algorithm is **on-policy** or **off-policy**:

- **On-policy:** Each time the policy changes, new samples must be collected. Old data becomes stale because it came from a different policy.
- **Off-policy:** Can improve the policy using data collected by *any* policy. Can reuse historical data across many policy updates.

```
                    SAMPLE EFFICIENCY SPECTRUM
                    
    More Efficient ◄─────────────────────────────────► Less Efficient
    (fewer samples)                                    (more samples)
    
    ┌───────────────────────────────────────────────────────────────┐
    │                                                               │
    │  Model-based    Off-policy    Actor-critic    On-policy       │
    │    deep RL       Q-learning                    policy        │
    │                                                gradient      │
    │      ●──────────────●──────────────●──────────────●          │
    │      │              │              │              │          │
    │      │              │              │              │          │
    │   Can simulate     Reuses all     Partial       Must collect │
    │   experience       past data      data reuse    fresh data   │
    │   with model                                    each update  │
    │                                                               │
    │                                                               │
    │   Evolutionary/gradient-free: even less efficient ──────►    │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
```

Why use less efficient algorithms? Because **wall-clock time is not the same as sample efficiency**. With fast simulators, generating samples is cheap, and simpler on-policy algorithms may reach good performance faster in real time despite needing more samples. The tradeoff depends on the problem setting.

---

### 5.7 Comparison: Stability and Ease of Use

A critical practical question: does the algorithm converge, and to what?

In supervised learning, gradient descent on a convex (or mildly non-convex) loss reliably finds good solutions. In RL, the situation is more complex:

```
                    STABILITY COMPARISON
                    
    ┌─────────────────────┬────────────────────────────────────────┐
    │  METHOD             │  STABILITY PROPERTIES                  │
    ├─────────────────────┼────────────────────────────────────────┤
    │                     │                                        │
    │  Value-based        │  Fixed-point iteration, not gradient  │
    │  (Q-learning)       │  descent. Minimizes "Bellman error,"  │
    │                     │  not expected reward directly.        │
    │                     │  May not converge with function       │
    │                     │  approximation (neural networks)!     │
    │                     │                                        │
    ├─────────────────────┼────────────────────────────────────────┤
    │                     │                                        │
    │  Model-based        │  Model fitting DOES converge          │
    │                     │  (supervised learning).               │
    │                     │  But: better model ≠ better policy!   │
    │                     │  Model errors compound unpredictably. │
    │                     │                                        │
    ├─────────────────────┼────────────────────────────────────────┤
    │                     │                                        │
    │  Policy gradient    │  The ONLY method that directly does   │
    │                     │  gradient ascent on expected reward!  │
    │                     │  But: high variance, often unstable.  │
    │                     │                                        │
    └─────────────────────┴────────────────────────────────────────┘
```

The key insight: only policy gradient methods directly optimize the RL objective. Other methods optimize surrogate objectives (Bellman error, model likelihood) that correlate with but do not equal expected reward. This disconnect can cause surprising failures in practice.

---

### 5.8 Summary of Algorithm Types

```
                    ALGORITHM SUMMARY TABLE
                    
    ┌────────────────┬────────────────────────────────────────────┐
    │  ALGORITHM     │  KEY CHARACTERISTICS                       │
    │  TYPE          │                                            │
    ├────────────────┼────────────────────────────────────────────┤
    │                │                                            │
    │  Policy        │  • Directly optimizes expected reward      │
    │  Gradient      │  • Works with any action space            │
    │                │  • On-policy: needs fresh samples         │
    │                │  • High variance gradients                │
    │                │  Examples: REINFORCE, PPO, TRPO           │
    │                │                                            │
    ├────────────────┼────────────────────────────────────────────┤
    │                │                                            │
    │  Value-Based   │  • Learns Q* or V* for optimal policy     │
    │                │  • Off-policy: can reuse all data         │
    │                │  • Limited to discrete actions            │
    │                │  • May not converge with deep networks    │
    │                │  Examples: Q-learning, DQN                │
    │                │                                            │
    ├────────────────┼────────────────────────────────────────────┤
    │                │                                            │
    │  Actor-Critic  │  • Combines policy and value learning     │
    │                │  • Lower variance than policy gradient    │
    │                │  • Works with continuous actions          │
    │                │  • Can be on or off-policy                │
    │                │  Examples: A3C, SAC, TD3                  │
    │                │                                            │
    ├────────────────┼────────────────────────────────────────────┤
    │                │                                            │
    │  Model-Based   │  • Learns environment dynamics            │
    │                │  • Most sample efficient                  │
    │                │  • Model errors can compound              │
    │                │  • Flexible: planning or policy learning  │
    │                │  Examples: Dyna, MBPO, MuZero             │
    │                │                                            │
    └────────────────┴────────────────────────────────────────────┘
```

---

## Conclusion: The RL Framework

This chapter established the mathematical foundation for reinforcement learning. We began by formalizing sequential decision-making through **Markov decision processes**, capturing how states evolve, actions influence outcomes, and rewards signal desirability. The **trajectory distribution** emerged as the central object of study—a distribution over sequences that depends on the policy parameters we wish to optimize.

The **RL objective** crystallized: maximize expected cumulative reward. We saw how this objective can be expressed in terms of state-action marginals, how infinite horizons lead to stationary distributions, and why expectations smooth out discontinuities in reward landscapes.

We dissected the **anatomy of RL algorithms**—the three-step loop of sampling, estimation, and improvement—and examined how different algorithm families instantiate these steps. **Value functions** and **Q-functions** emerged as key tools, capturing expected future reward and enabling principled policy improvement.

The taxonomy of algorithms reveals fundamental tradeoffs:

```
                    FUNDAMENTAL TRADEOFFS
                    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │  SAMPLE EFFICIENCY vs. WALL-CLOCK TIME                      │
    │  Model-based methods use fewer samples but require         │
    │  expensive model learning and planning.                    │
    │                                                             │
    │  STABILITY vs. FLEXIBILITY                                  │
    │  Policy gradients directly optimize the objective but      │
    │  have high variance. Value methods are more stable but    │
    │  don't directly optimize reward.                           │
    │                                                             │
    │  ON-POLICY vs. OFF-POLICY                                   │
    │  Off-policy methods reuse data efficiently but introduce  │
    │  bias from distribution mismatch. On-policy methods are   │
    │  unbiased but wasteful of data.                           │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

The coming chapters will dive deep into each algorithm family. We'll derive the policy gradient theorem, explore Q-learning and its deep variants, understand actor-critic architectures, and examine model-based approaches. Each chapter builds on the foundation established here: the MDP framework, the RL objective, and the interplay between policies, values, and models.

The journey from imitation to reinforcement learning represents a fundamental shift in how we think about learning. Rather than copying demonstrations, we optimize for outcomes. Rather than supervised signals, we use rewards. Rather than static prediction, we reason about sequential consequences. This shift opens vast new possibilities—agents that discover novel strategies, exceed human performance, and solve problems no expert has tackled—but demands new mathematical tools and algorithmic insights. We have built the foundation; now we construct the edifice.

---

## Appendix: Key Equations Reference

**Markov Chain:**
$$\mathcal{M} = \{\mathcal{S}, \mathcal{T}\}, \quad p(\mathbf{s}_{t+1}) = \sum_{\mathbf{s}_t} p(\mathbf{s}_{t+1} | \mathbf{s}_t) p(\mathbf{s}_t), \quad \mu_{t+1} = \mathcal{T}\mu_t$$

**Markov Decision Process:**
$$\mathcal{M} = \{\mathcal{S}, \mathcal{A}, \mathcal{T}, r\}, \quad r : \mathcal{S} \times \mathcal{A} \to \mathbb{R}$$

**POMDP:**
$$\mathcal{M} = \{\mathcal{S}, \mathcal{A}, \mathcal{O}, \mathcal{T}, \mathcal{E}, r\}, \quad p(\mathbf{o}_t | \mathbf{s}_t)$$

**Trajectory Distribution:**
$$p_\theta(\mathbf{s}_1, \mathbf{a}_1, \ldots, \mathbf{s}_H, \mathbf{a}_H) = p(\mathbf{s}_1) \prod_{t=1}^{H} \pi_\theta(\mathbf{a}_t | \mathbf{s}_t) p(\mathbf{s}_{t+1} | \mathbf{s}_t, \mathbf{a}_t)$$

**RL Objective (Finite Horizon):**
$$\theta^* = \arg\max_\theta \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{H} r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

**RL Objective (Discounted Infinite Horizon):**
$$\theta^* = \arg\max_\theta \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r(\mathbf{s}_t, \mathbf{a}_t)\right]$$

**Stationary Distribution:**
$$\bar{\mu} = \mathcal{T}_\theta \bar{\mu}, \quad (\mathcal{T}_\theta - \mathbf{I})\bar{\mu} = 0$$

**Q-Function:**
$$Q^\pi(\mathbf{s}_t, \mathbf{a}_t) = \sum_{t'=t}^{H} \mathbb{E}_{\pi}\left[r(\mathbf{s}_{t'}, \mathbf{a}_{t'}) \mid \mathbf{s}_t, \mathbf{a}_t\right]$$

**Value Function:**
$$V^\pi(\mathbf{s}_t) = \mathbb{E}_{\mathbf{a}_t \sim \pi(\mathbf{a}_t | \mathbf{s}_t)}\left[Q^\pi(\mathbf{s}_t, \mathbf{a}_t)\right]$$

**Advantage Function:**
$$A^\pi(\mathbf{s}, \mathbf{a}) = Q^\pi(\mathbf{s}, \mathbf{a}) - V^\pi(\mathbf{s})$$

**Greedy Policy Improvement:**
$$\pi'(\mathbf{a} | \mathbf{s}) = \mathbf{1}\left[\mathbf{a} = \arg\max_{\mathbf{a}'} Q^\pi(\mathbf{s}, \mathbf{a}')\right]$$
