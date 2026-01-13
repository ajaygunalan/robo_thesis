# CS 285 Reading Map (Lectures 1–22)

A comprehensive reading map selecting the **single best section** for each lecture from multiple textbooks.

## Strategy

- **Sutton & Barto** for fundamentals — notation ($S, A, R$) matches CS 285 slides
- **Bertsekas '25** for advanced algorithms and modern architectures (PPO, MPC, Transformers)
- **Lattimore '20** for bandits — the gold standard reference

---

## Module 1: Fundamentals (Lectures 1–8)

| Lecture | Topic | Best Book | Reading Section | Why this choice? |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Introduction** | Sutton & Barto | Ch. 1 | Establishes the Agent-Environment loop and "Reward Hypothesis" perfectly. |
| **2** | **Supervised / Imitation** | Bertsekas '25 | Sec 3.4.1 | Sutton doesn't cover Imitation; Bertsekas covers it as "Classifiers for Policy Space." |
| **3** | **Neural Networks** | Bertsekas '25 | Sec 3.1–3.2 | Explains training Neural Networks for RL function approximation (Sutton assumes you know this). |
| **4** | **RL Basics (MDPs)** | Sutton & Barto | Ch. 3 | The definitive definition of MDPs, Returns, and Episodes in standard CS notation. |
| **5** | **Policy Gradients** | Sutton & Barto | Ch. 13.1–13.3 | Derives the Policy Gradient Theorem (REINFORCE) clearly. Essential reading. |
| **6** | **Actor-Critic** | Sutton & Barto | Sec 13.5 | Explains how adding a "Critic" (Value Function) reduces variance in gradients. |
| **7** | **Value Functions** | Sutton & Barto | Ch. 9 | "On-policy Prediction with Approximation." Explains fitting value functions. |
| **8** | **Deep RL (DQN)** | Sutton & Barto | Sec 16.5 & 11.3 | Sec 16.5 is a case study on Atari (DQN). Sec 11.3 explains the "Deadly Triad" instability. |

---

## Module 2: Advanced Algorithms (Lectures 9–12)

Sutton & Barto stops covering modern architectures here; Bertsekas takes over.

| Lecture | Topic | Best Book | Reading Section | Why this choice? |
| :--- | :--- | :--- | :--- | :--- |
| **9** | **Advanced PG (PPO/TRPO)** | Bertsekas '25 | Sec 3.5.3 | Explicitly covers PPO (Proximal Policy Optimization) and Trust Regions, which Sutton misses. |
| **10** | **Planning (MCTS)** | Sutton & Barto | Sec 8.11 | "Monte Carlo Tree Search." A clearer explanation of the AlphaGo planner than Bertsekas. |
| **11** | **Model-Based RL (MPC)** | Bertsekas '25 | Sec 1.6.9 | "Model Predictive Control." Bertsekas is the world expert on MPC. |
| **12** | **MB Policy Learning (Dyna)** | Sutton & Barto | Ch. 8 | Explains Dyna (using a model to generate simulated training data). |

---

## Module 3: Exploration & Offline RL (Lectures 13–16)

| Lecture | Topic | Best Book | Reading Section | Why this choice? |
| :--- | :--- | :--- | :--- | :--- |
| **13** | **Exploration (Bandits)** | Lattimore '20 | Ch. 7 & 36 | Ch 7 (UCB) and Ch 36 (Thompson Sampling) are the gold standard. |
| **14** | **Exploration 2 (Deep)** | Bertsekas '25 | Sec 3.5.5 | "Random Search and Cross-Entropy Methods" (Evolutionary strategies). |
| **15** | **Offline RL 1 (Batch)** | Bertsekas '25 | Sec 3.3.1 | "Fitted Value Iteration." This is the mathematical name for Offline/Batch RL. |
| **16** | **Offline RL 2 (CQL)** | Bertsekas '25 | Sec 2.5 | "Constrained Rollout." Explains constraining a policy to stay close to data (essential for Offline RL). |

---

## Module 4: Frontiers (Lectures 17–22)

| Lecture | Topic | Best Book | Reading Section | Why this choice? |
| :--- | :--- | :--- | :--- | :--- |
| **17** | **RL Theory** | Bertsekas '25 | Sec 1.5 | "Visualizing Approximation in Value Space." Explains error bounds intuitively. |
| **18** | **Variational Inference** | — | — | Topic belongs to Probabilistic ML (VAEs); not covered in standard RL texts. |
| **19** | **Control as Inference** | — | — | Advanced topic (MaxEnt RL); not in standard textbooks. |
| **20** | **Inverse RL** | — | — | Books generally assume the Reward is known. |
| **21** | **Sequence Models (Transformers)** | Bertsekas '25 | Sec 2.3.8 | "Inference in Transformers." The only book that treats LLMs as RL problems. |
| **22** | **Meta-Learning** | Bertsekas '25 | Sec 1.6.8 | "Adaptive Control." Meta-RL is mathematically treated as Adaptive Control here. |

---

## Key to Abbreviations

- **Sutton & Barto:** *Reinforcement Learning: An Introduction* (2018)
- **Bertsekas '25:** *A Course in Reinforcement Learning* (2nd Edition, 2025)
- **Lattimore '20:** *Bandit Algorithms* (2020)
