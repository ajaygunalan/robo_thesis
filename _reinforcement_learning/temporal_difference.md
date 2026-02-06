# Temporal Difference Learning

## The Problem

Monte Carlo methods wait until an episode ends to update value estimates. This is wasteful—you observe useful information at every step but can't use it until termination.

## The Core Idea: Bootstrapping

TD methods update estimates using other estimates. Instead of waiting for the true return, use your current guess of future value as a stand-in.

**The TD target:**
$$\text{Target} = r_t + \gamma V(s_{t+1})$$

**The TD error (δ):**
$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

This is the difference between what you expected and what you got (reward + new estimate).

**The update:**
$$V(s_t) \leftarrow V(s_t) + \alpha \delta_t$$

Shift your estimate toward the target by a small step.

## Why It Works

The Bellman equation says:
$$V^\pi(s) = \mathbb{E}[r + \gamma V^\pi(s')]$$

TD exploits this recursive structure. If your value estimates satisfy Bellman, the TD error is zero on average. If not, the updates push you toward consistency.

## Bias-Variance Tradeoff

| Method | Bias | Variance | Why |
|--------|------|----------|-----|
| Monte Carlo | None | High | Uses true returns, but one sample of a long random trajectory |
| TD(0) | Yes | Low | Uses estimates (biased if wrong), but only one step of randomness |

TD introduces bias because the target depends on $V(s_{t+1})$, which may be wrong. But variance drops dramatically because you're not accumulating randomness over many steps.

## TD for Control: Q-Learning

Apply TD to action-values instead of state-values:

$$Q(s,a) \leftarrow Q(s,a) + \alpha \left( r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right)$$

The $\max$ makes this off-policy: you learn about the greedy policy while following any exploration policy.

## Biological Connection

The TD error δ resembles dopamine neuron firing in the brain. Dopamine spikes when rewards exceed expectations (positive δ) and dips when rewards disappoint (negative δ). TD learning may be how biological systems do credit assignment.
