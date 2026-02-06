# Replay Buffer

## The Problem

Online learning with neural networks fails because sequential transitions are correlated. State $s_t$ is nearly identical to $s_{t+1}$. SGD assumes i.i.d. data—training on a correlated stream causes the network to overfit to the local trajectory and forget everything else.

## The Solution

Store transitions $(s, a, r, s')$ in a large buffer. During training, sample random mini-batches from the buffer instead of using the latest transition.

## Why It Works

**Decorrelation:** Random sampling breaks temporal correlations. A batch might contain transitions from different episodes, different parts of state space, different policies. This looks i.i.d. to the optimizer.

**Data efficiency:** Each transition can be used for multiple gradient updates instead of being discarded after one use. In sample-limited settings (robotics, expensive simulations), this matters enormously.

## Implementation

```
Buffer B (fixed size, e.g., 1M transitions)

Collect:
  Take action, observe (s, a, r, s')
  Store in B (overwrite oldest if full)

Train:
  Sample random batch of N transitions from B
  Compute loss and update network
```

## Off-Policy Requirement

Replay buffers make learning off-policy by definition. The transitions in the buffer came from old policies—potentially very different from the current policy. This is why replay buffers pair naturally with Q-learning (off-policy) but not with vanilla policy gradients (on-policy).

## Variants

**Prioritized Experience Replay:** Sample transitions with high TD error more frequently. High error = high "surprise" = more to learn from.

**Hindsight Experience Replay (HER):** For goal-conditioned tasks, relabel failed trajectories as successes for different goals. Turns sparse reward into dense signal.
