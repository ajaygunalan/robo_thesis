# N-Step Returns

## The Problem

TD(0) uses a 1-step target: $r_t + \gamma V(s_{t+1})$. Low variance, but biased if $V$ is wrong.

Monte Carlo uses the full return: $\sum_{k=0}^{T} \gamma^k r_{t+k}$. Unbiased, but high variance from accumulating randomness.

Neither extreme is optimal.

## The Solution: N-Step Returns

Look ahead $n$ steps with real rewards, then bootstrap:

$$G_t^{(n)} = \sum_{k=0}^{n-1} \gamma^k r_{t+k} + \gamma^n V(s_{t+n})$$

- $n=1$: TD(0) — max bias, min variance
- $n=\infty$: Monte Carlo — min bias, max variance
- $n \in (1, \infty)$: Interpolation

**Intuition:** Use real rewards for the near-term (where variance is still low), then cut off with the value estimate before variance explodes.

## N-Step Advantage

For policy gradients with a critic:

$$\hat{A}_t^{(n)} = \left[ \sum_{k=0}^{n-1} \gamma^k r_{t+k} \right] + \gamma^n V(s_{t+n}) - V(s_t)$$

## Generalized Advantage Estimation (GAE)

Instead of picking one $n$, take a weighted average of ALL n-step returns.

Define the TD residual: $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$

**GAE formula:**
$$\hat{A}_t^{\text{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}$$

**Recursive implementation:**
$$\hat{A}_t = \delta_t + (\gamma \lambda) \hat{A}_{t+1}$$

The parameter $\lambda \in [0,1]$ controls the bias-variance tradeoff:
- $\lambda = 0$: Pure 1-step TD (high bias, low variance)
- $\lambda = 1$: Approaches Monte Carlo (low bias, high variance)
- $\lambda \in (0.9, 0.99)$: Practical sweet spot

## Connection to Eligibility Traces

GAE is equivalent to TD(λ) with eligibility traces. The forward view (weighted sum of n-step returns) equals the backward view (decaying credit assignment). Same math, different implementation.

## When to Use

- **Q-learning (DQN):** N-step returns speed up reward propagation
- **Policy gradients (PPO, A3C):** GAE is standard for advantage estimation
- **Actor-critic:** GAE for the advantage, TD for the critic
