# Reinforcement Learning: A Mathematical Foundation

Reinforcement Learning (RL) sits at the intersection of control theory, machine learning, and biological learning. This guide builds from core definitions through to practical algorithms, connecting the mathematical machinery to intuition.

## The MDP Framework

A Markov Decision Process (MDP) provides the formal foundation: a state space $\mathcal{S}$, action space $\mathcal{A}$, transition kernel $P(s' \mid s, a)$, reward function $R(s',s,a)$, and discount factor $\gamma \in [0,1)$. States evolve as $s_{k+1} \sim P(\cdot \mid s_k, a_k)$—you control the policy $\pi$; everything else is environment.

A **policy** $\pi(a \mid s)$ maps states to action distributions—your "controller" that determines what to do given what you observe.

The **value function** $V^\pi(s)$ captures the expected discounted return from state $s$:

$$V^\pi(s) = \mathbb{E}\left[ \sum_{k=0}^{\infty} \gamma^k r_k \mid s_0 = s \right]$$

The **Q-function** (or action-value) refines this by conditioning on both state and action—"how good is *this* move?":

$$Q(s,a) = \mathbb{E}\left[R(s',s,a) + \gamma V(s')\right] = \sum_{s'} P(s' \mid s,a)\big(R(s',s,a) + \gamma V(s')\big)$$

These connect directly: $V(s) = \max_a Q(s,a)$ and $\pi(s) = \arg\max_a Q(s,a)$. Knowing one lets you compute the other.

## Bellman's Principle

The recursive foundation of RL: *whatever happens next, the rest of the path must be optimal*. This transforms an exponential planning problem into a local recursion:

$$V(s) = \max_a \mathbb{E}\left[ r_0 + \gamma V(s_1) \right]$$

Today's value equals the best immediate reward plus discounted future value. For Q-values:

$$Q(s,a) = \mathbb{E}\left[ r_0 + \gamma \max_{a'} Q(s_1, a') \right]$$

## Model-Based Methods: Dynamic Programming

When transition dynamics $P$ and rewards $R$ are known, classical dynamic programming applies.

**Value Iteration** sweeps over all states, updating values toward the Bellman optimum:

$$V(s) \leftarrow \max_a \sum_{s'} P(s' \mid s,a)\Big(R(s',s,a) + \gamma V(s')\Big)$$

The greedy policy $\pi(s) = \arg\max_a \sum_{s'} P(s' \mid s,a)(\cdots)$ is extracted at the end.

**Policy Iteration** alternates between evaluation and improvement: first solve for $V^\pi$ under the current policy (the "critic"), then update $\pi \leftarrow \arg\max_a \mathbb{E}[r + \gamma V^\pi(s')]$ (the "actor").

## Model-Free Methods: Learning from Experience

In realistic settings we often lack the model—we must learn from sampled trajectories instead.

### Monte Carlo Methods

Episodic MC waits until termination, then uses the total discounted return $R_\Sigma = \sum_{k=1}^{n} \gamma^k r_k$ to update visited states or state-action pairs:

$$V^{\text{new}}(s_k) = V^{\text{old}}(s_k) + \frac{1}{n}\left(R_\Sigma - V^{\text{old}}(s_k)\right)$$

MC is asymptotically unbiased (no bootstrapping), but sample-inefficient with high variance. Credit assignment is uniform—every decision along the trajectory shares equal responsibility for success or failure.

### Temporal-Difference Learning

TD methods update *before* an episode ends using **bootstrapping**: replacing the unknown true return with a target that uses current value estimates.

**TD(0)** defines a one-step target and TD error:

$$\text{Target} = r_k + \gamma V^{\text{old}}(s_{k+1}), \qquad \delta_k = r_k + \gamma V^{\text{old}}(s_{k+1}) - V^{\text{old}}(s_k)$$

The update $V^{\text{new}}(s_k) = V^{\text{old}}(s_k) + \alpha\delta_k$ emphasizes events immediately preceding reward—one time-step credit assignment that aligns with biological reward-prediction error in dopamine systems.

**n-step TD** looks further ahead:

$$R_\Sigma^{(n)} = \sum_{j=0}^{n} \gamma^{j} r_{k+j} + \gamma^{n+1} V(s_{k+n+1})$$

As $n \to \infty$, TD converges to MC: TD(∞) ≡ MC.

**TD-λ** forms a geometric mixture of n-step returns:

$$R_\Sigma^\lambda = (1-\lambda)\sum_{n=1}^\infty \lambda^{n-1} R_\Sigma^{(n)}$$

The parameter $\lambda \in [0,1]$ controls the bias-variance tradeoff between TD(0) and MC. Forward-view equals the backward-view with eligibility traces in implementation.

TD methods introduce bias via bootstrapping but achieve much lower variance than MC and learn online, step by step.

### Q-Learning

The model-free, off-policy workhorse:

$$Q(s,a) \leftarrow Q(s,a) + \alpha \cdot \left(r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right)$$

Q-learning is off-policy TD(0) for control—it improves the greedy policy with respect to Q, but data may come from an ε-greedy or random behavior policy. This contrasts with **SARSA**, its on-policy cousin.

## Policy Gradient Methods

Rather than learning values and deriving a policy, directly optimize policy parameters through gradient ascent:

$$\nabla_\theta J \approx \mathbb{E}\left[ Q(s,a) \nabla_\theta \log \pi_\theta(a \mid s) \right]$$

This enables learning in continuous action spaces and stochastic policies.

## Continuous Control and HJB

For continuous-time control, Bellman's principle becomes the Hamilton-Jacobi-Bellman PDE:

$$\frac{\partial V}{\partial t} = \min_{u} \left( \nabla V \cdot f(x,u) + L(x,u) \right)$$

This connects RL to classical optimal control theory.

## Function Approximation and Deep RL

Replace tabular representations with neural networks to handle high-dimensional spaces. DQN demonstrated that experience replay and target networks stabilize Q-learning at scale. Modern variants—SAC, CQL, IQL, RLPD—are all methods to approximate and stabilize these Bellman updates in large problems.

## Mental Model

Think of the **value function** as a terrain map of state space: high plateaus are good futures, valleys are bad. The **policy** is your compass pointing uphill—either greedy with respect to Q or following policy gradients. Learning algorithms are methods for surveying this terrain: with a known map (model-based) or by walking and sampling elevations (model-free).

This mathematical framework powers everything from simple games to complex robotics and autonomous systems.
