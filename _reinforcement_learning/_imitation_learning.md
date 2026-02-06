# Maximum Likelihood and Imitation Learning

## 1. Maximum Likelihood Estimation

Given $N$ i.i.d. samples $\{x_1, \ldots, x_N\}$ from a parametric model $p_\theta(x)$, we seek the parameter $\theta$ that best explains the data.

By independence, the joint probability (likelihood) is:

$$L(\theta) = \prod_{i=1}^{N} p_\theta(x_i)$$

The MLE maximizes this:

$$\theta_{\text{ML}} = \arg\max_\theta \prod_{i=1}^{N} p_\theta(x_i)$$

Since $\log$ is strictly increasing, maximizing $L(\theta)$ is equivalent to maximizing $\log L(\theta)$:

$$= \arg\max_\theta \log \prod_{i=1}^{N} p_\theta(x_i)$$

Since $\log$ converts products to sums:

$$= \arg\max_\theta \sum_{i=1}^{N} \log p_\theta(x_i)$$

The gradient for optimization:

$$\nabla_\theta J_{\text{ML}}(\theta) = \sum_{i=1}^{N} \nabla_\theta \log p_\theta(x_i)$$

---

## 2. Behavioral Cloning as MLE

In imitation learning, we have expert demonstrations: states $s_t$ and corresponding actions $a_t^{\text{expert}}$. We model a policy $\pi_\theta(a \mid s)$ and treat each $(s, a)$ pair as a data point.

Substituting into the MLE framework:

$$J_{\text{BC}}(\theta) = \sum_{i,t} \log \pi_\theta(a_{i,t}^{\text{expert}} \mid s_{i,t})$$

$$\nabla_\theta J_{\text{BC}}(\theta) = \sum_{i,t} \nabla_\theta \log \pi_\theta(a_{i,t}^{\text{expert}} \mid s_{i,t})$$

This is standard cross-entropy loss. **Behavioral cloning is MLE on expert state-action pairs.**

---

## 3. Policy Gradient as Reward-Weighted MLE

In RL, we maximize expected cumulative reward without expert data:

$$J(\theta) = \mathbb{E}_{\tau \sim p_\theta(\tau)}\left[\sum_t r(s_t, a_t)\right]$$

The policy gradient is:

$$\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \underbrace{\left(\sum_t \nabla_\theta \log \pi_\theta(a_{i,t} \mid s_{i,t})\right)}_{\text{same as BC}} \cdot \underbrace{R(\tau_i)}_{\text{reward weight}}$$

The first term is identical to behavioral cloning's gradient. The difference: each trajectory is weighted by its cumulative reward $R(\tau_i) = \sum_t r(s_{i,t}, a_{i,t})$.

---

## 4. Unified View

| | Behavioral Cloning | Policy Gradient |
|---|---|---|
| **Data** | Expert trajectories | Self-generated trajectories |
| **Weight** | Uniform (all = 1) | Cumulative reward of each trajectory |

**Policy gradient = MLE on your own behavior, weighted by outcome quality.**

High-reward trajectories get reinforced; low-reward ones don't. Behavioral cloning is the special case where all expert actions are weighted equally.
