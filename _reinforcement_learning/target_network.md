# Target Network

## The Problem

In Q-learning, the regression target is:
$$y = r + \gamma \max_{a'} Q_\phi(s', a')$$

The target depends on the same parameters $\phi$ we're updating. Every gradient step moves both the prediction AND the target. This is like a dog chasing its tail—updates oscillate or diverge instead of converging.

## The Solution

Maintain two networks:
- **Current network** $Q_\phi$: Used for predictions, updated every step
- **Target network** $Q_{\phi'}$: Used only to compute targets, updated slowly

The target becomes:
$$y = r + \gamma \max_{a'} Q_{\phi'}(s', a')$$

Now the target is stable while you update $\phi$. The regression looks like supervised learning.

## Update Strategies

**Hard update (classic DQN):**
Every $N$ steps (e.g., 10,000), copy $\phi' \leftarrow \phi$.

Creates a "staircase" target that stays completely fixed for long periods, then jumps.

**Soft update (Polyak averaging):**
Every step: $\phi' \leftarrow \tau \phi + (1-\tau) \phi'$ with small $\tau$ (e.g., 0.001).

Acts as a low-pass filter. Target network slowly tracks the current network without sudden jumps.

## Why It Works

The fundamental issue is that Q-learning combines two operations:
1. Bellman backup (compute target)
2. Function approximation (fit to target)

Neither operation alone is problematic. The Bellman operator is a contraction. Neural network regression is stable. But combined, $\Pi \mathcal{B}$ (project then backup) is not a contraction—there's no convergence guarantee.

Target networks don't fix the theory, but they slow down the instability enough for practical learning. By the time the target network updates, the current network has made enough progress that the new target is "better."

## When to Use

Target networks are standard in:
- DQN and variants (Double DQN, Dueling DQN)
- DDPG, TD3, SAC (continuous control)

Generally: whenever you're doing TD learning with neural networks, use a target network.
