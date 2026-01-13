Here is a detailed technical blog post based on **CS 285 Lecture 12**, synthesized with the theoretical frameworks from **Chapters 2 and 5 of _Reinforcement Learning and Optimal Control_** by Dimitri P. Bertsekas.

---

# The Neural Simulator: Backpropagation, Dyna, and the Art of Short Rollouts

**Based on CS 285 Lecture 12 and _Reinforcement Learning and Optimal Control_ by Dimitri P. Bertsekas**

In our previous exploration of Model-Based Reinforcement Learning (Lecture 11), we focused on **Model Predictive Control (MPC)**. In that paradigm, the "policy" is simply an online planner solving an optimization problem at every single time step.1 While robust, MPC is computationally expensive at runtime, requiring significant compute for every action taken.2

Today, we ask: **Can we distill the foresight of the planner into a fast, reactive policy $\pi_\theta(a|s)$?**

This moves us from "planning at test time" to "learning at training time." We effectively want to compile the intelligence of our model-based planner into a neural network that can act instantly. We will explore three distinct architectures for this, progressing from analytical elegance to robust engineering:

1. **Analytic Gradients:** Differentiating directly through the model (Backpropagation Through Time).
    
2. **Model-Based Acceleration (Dyna):** Using the model as a simulator to generate synthetic experience.
    
3. **Short Branching Rollouts:** A hybrid approach that solves the fatal problem of compounding model errors.
    

We will ground these modern Deep RL methods in Dimitri Bertsekas’s framework of **Approximation in Policy Space** and **Simulation-Based Policy Iteration**.

---

## 1. The Analytic Approach: Backpropagation Through Time

If we learn a differentiable neural network model $s_{t+1} = f_\phi(s_t, a_t)$ and represent our policy as a neural network $a_t = \pi_\theta(s_t)$, the entire trajectory of the agent becomes one large, differentiable computation graph.

We can write the cumulative reward 3$J(\theta)$ as a nested function of the policy parameters 4$\theta$ and compute the gradient 5$\nabla_\theta J(\theta)$ via the Chain Rule.6 This is referred to as **Model-Based RL Version 2.0** in the lecture.

### The Gradient Calculation

Using the chain rule, we can compute the gradient recursively.7 The gradient of the reward with respect to the policy parameters depends on the sensitivity of the state to the parameters ($\frac{d s_t}{d \theta}$):

$$ \frac{d J}{d \theta} = \sum_{t=0}^T \left( \frac{d r_t}{d s_t} \frac{d s_t}{d \theta} + \frac{d r_t}{d a_t} \frac{d a_t}{d \theta} \right) $$

This requires calculating the Jacobian of the dynamics, equivalent to **Backpropagation Through Time (BPTT)** used in RNNs.

### The Optimal Control Perspective

Bertsekas discusses this in **Section 5.7 (Approximation in Policy Space)**. He notes that if the system dynamics and cost functions are known and differentiable, the control problem reduces to a deterministic nonlinear programming problem over the parameters $\theta$.

> _"We select the policy by using optimization over a suitably restricted class of policies... usually a parametric family of some form."_ (Bertsekas, p. ix)

In classical control, this concept is related to **Shooting Methods**, where we optimize a trajectory by using the gradient of the cost with respect to the control inputs. Here, we extend that to optimize the policy parameters themselves.

### The Problem: The Curse of Chaos

While mathematically elegant, this method is notoriously unstable in Deep RL.

1. **Vanishing/Exploding Gradients:** Multiplying Jacobians over a long horizon $T$ leads to numerical instability, just as in deep RNNs.
    
2. **The Curse of Chaos:** Physical dynamics are often chaotic. A tiny change in parameters $\theta$ at $t=0$ can lead to a completely different state at $t=100$. This creates a rugged, discontinuous loss landscape where first-order optimizers (like SGD) struggle to find good solutions.
    

---

## 2. The Simulation Approach: Dyna-Style Algorithms

If differentiating _through_ the model is unstable, we should instead use the model as a black-box **Simulator**.

This leads to **Dyna-style algorithms** (**Version 2.5**). The workflow is straightforward:

1. **Learn Model:** Train a dynamics model $f_\phi$ on real data $\mathcal{D}_{real}$.
    
2. **Dream:** Use $f_\phi$ to generate thousands of _synthetic_ trajectories $\{\tau_{syn}\}$.
    
3. **Train:** Use a stable Model-Free algorithm (like PPO or Soft Actor-Critic) to update the policy $\pi_\theta$ using this synthetic data.
    

### Theoretical Context: Simulation-Based Policy Iteration

This approach maps directly to **Simulation-Based Policy Iteration** described in **Bertsekas Section 5.3**.

> _"The simulator provides the ability to generate samples from any state-control pair... This allows the use of methods that rely on a generative model."_

Here, the learned neural network _replaces_ the environment simulator. The benefit is **Sample Efficiency**: we can generate millions of synthetic samples for every real-world interaction, effectively "densifying" the learning signal for the model-free algorithm.

### The Problem: Compounding Errors

The fatal flaw of generating long synthetic trajectories is Compounding Error. If the model has a small error $\epsilon$ at each step, the state error accumulates quadratically or exponentially:

$$ \text{Error}(t) \approx \mathcal{O}(\epsilon t^2) $$

If we train on long synthetic trajectories ($T$ is large), the policy optimizes for a "hallucinated" world that diverges from reality. As Bertsekas warns in **Section 2.1.6**, simulation error can invalidate the policy improvement step, leading to a policy that exploits the model's inaccuracies rather than solving the task.

---

## 3. The Hybrid Solution: Short Branching Rollouts

To balance sample efficiency with model accuracy, we use **Short Branching Rollouts** (**Version 3.0**). This is the mechanism behind state-of-the-art algorithms like **MBPO (Model-Based Policy Optimization)**.

Instead of generating full trajectories from scratch ($s_0 \to s_T$), we perform local expansions:

1. **Branch from Reality:** Sample a state $s \sim \mathcal{D}_{real}$ from the replay buffer. This ensures we start simulation in a valid region of the state space.
    
2. **Short Rollout:** Simulate only $k$ steps forward using the model (where $k$ is small, e.g., 1 to 5).
    
3. **Value Bootstrap:** Use a learned Value Function (Critic) to estimate the long-term return after step $k$.
    

### Theoretical Connection: Limited Lookahead

This architecture implements **Approximation in Value Space** with **Limited Lookahead** (Bertsekas **Section 2.2**).

> _"The motivation for $l$-step lookahead is that for increasing values of $l$, one may require a less accurate approximation to obtain good performance."_ (Bertsekas, p. 52)

In MBRL, we invert this logic: because our approximation (the learned model) is imperfect, we _restrict_ our lookahead to a short horizon $k$.

- By keeping $k$ small, we prevent the compounding error $\epsilon k^2$ from becoming significant.
    
- By using a Q-function (trained via off-policy RL) at the end of the rollout, we account for the infinite horizon without relying on the potentially inaccurate dynamics model.
    

### Solving Distribution Mismatch

This approach solves the critical issue of **Distribution Mismatch**.

- **Long Rollouts:** The policy drives the model into Out-Of-Distribution (OOD) states where predictions are garbage.
    
- **Branched Rollouts:** We anchor the simulation to real data. The policy is trained on transitions $(s, a, s')$ where $s$ is real (from the buffer) and $s'$ is a very short-term prediction, ensuring the model remains trustworthy.
    

---

## Summary: The Spectrum of Model Usage

Lecture 12 defines a spectrum of how learned models can be leveraged:

1. **Pure Planning (MPC):** Use the model for decision-time optimization. Robust but computationally slow. (See **Rolling Horizon**, Bertsekas Sec 2.5.1).
    
2. **Analytic Gradients (Version 2.0):** Differentiate through the model. Analytically precise but numerically unstable due to chaos. (See **Parametric Approximation**, Bertsekas Sec 5.7).
    
3. **Dyna / Short Rollouts (Version 3.0):** Use the model to augment real data with short, trustworthy synthetic futures. This balances sample efficiency with stability.
    

Modern Model-Based RL relies on the insight that a learned model is a valid **local** approximator of the environment. By restricting the model to short rollouts, we allow it to perform dense data augmentation (improving sample efficiency) while relying on model-free value estimation for global consistency.