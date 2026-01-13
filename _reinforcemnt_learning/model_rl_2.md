Here is a detailed technical blog post based on **CS 285 Lecture 11**, synthesized with the theoretical frameworks from **Chapters 1 and 2 of _Reinforcement Learning and Optimal Control_** by Dimitri P. Bertsekas.

---

# The Map and the Territory: Model-Based RL, Uncertainty, and Adaptive Control

**Based on CS 285 Lecture 11 and _Reinforcement Learning and Optimal Control_ by Dimitri P. Bertsekas**

In Model-Free Reinforcement Learning, the agent acts as a wanderer in the dark, learning to react to situations based solely on trial and error.1 **Model-Based Reinforcement Learning (MBRL)** takes a fundamentally different approach: it attempts to act as a cartographer. By learning a map of the world (the transition dynamics $p(s'|s,a)$), the agent can simulate the future and plan a path to its goal.

The promise of MBRL is **Sample Efficiency**. As shown in the lecture, model-based methods can learn tasks in minutes of real-time interaction that might take model-free methods days to master.

However, relying on a learned map introduces a new, dangerous adversary: **Model Bias**. If the map is wrong, the plan will fail. This post explores how modern Deep MBRL algorithms navigate the challenges of **Distribution Shift**, **Epistemic Uncertainty**, and **Complex Observations**, grounding these solutions in the classical control theory of **Certainty Equivalence** and **Adaptive Control**.

---

## 1. The Naïve Approach: System Identification

The most intuitive formulation of MBRL (referred to as "Version 0.5" in the lecture) is a linear two-step process:

1. **Data Collection:** Run a base policy $\pi_0$ (e.g., a random policy) to collect transitions $\mathcal{D} = \{(s, a, s')\}$.
    
2. **System Identification:** Train a neural network $f_\theta(s, a)$ to minimize the prediction error $\sum || f_\theta(s, a) - s' ||^2$.
    
3. **Planning:** Use the learned model $f_\theta$ to plan a sequence of actions that maximizes reward.
    

This approach mirrors the classical engineering discipline of **System Identification**. As Bertsekas describes in **Section 1.3.8 (Systems with Unknown Parameters - Adaptive Control)**:

> _"An apparently reasonable form of suboptimal control is to separate the control process into two phases, a parameter estimation (or identification) phase and a control phase... The final parameter estimates from the first phase are then used to implement an optimal control law."_ (Bertsekas, p. 41)

### The Failure Mode: Distributional Shift

While conceptually simple, "Version 0.5" fails efficiently in complex environments. The culprit is **Distributional Shift**.

1. The model $f_\theta$ is trained on the distribution of states visited by the random policy, $p_{\pi_0}(s)$.
    
2. The planner optimizes for high reward, producing a new trajectory that visits a different distribution of states, $p_{\pi_f}(s)$.
    
3. Because neural networks generalize poorly outside their training distribution, the model makes errors in these new states.
    
4. The planner **exploits** these errors. If the model erroneously predicts that "wiggling the leg" leads to infinite velocity, the planner will choose that action.
    

As Bertsekas warns regarding parameter identification:

> _"The control process may make some of the unknown parameters invisible to the estimation process... Therefore, [parameters] are not identifiable when feedback control is applied."_ (Bertsekas, p. 42)

---

## 2. Closing the Loop: Iterative Learning and MPC

To fix distribution shift, we must close the loop between data collection and planning. We cannot simply learn once and plan once; we must iterate.

### Version 1.0: Data Aggregation

Instead of training once, we alternate between training and data collection.

1. Train model on $\mathcal{D}$.
    
2. Plan actions using the model.
    
3. Execute actions to collect new data and append to $\mathcal{D}$.
    
    This ensures the model is trained on the specific distribution of states the planner actually visits.
    

### Version 1.5: Model Predictive Control (MPC)

Even with aggregation, the model will never be perfect. To handle residual errors, we replace Open-Loop planning with **Model Predictive Control (MPC)**.

1. Plan a sequence over horizon $H$.
    
2. Execute **only the first action** $a_t$.
    
3. Observe the real state $s_{t+1}$.
    
4. Re-plan.
    

This strategy transforms an open-loop plan into a closed-loop policy. As defined in **Bertsekas Section 2.5.1**, MPC acts as a **Rolling Horizon** scheme:

> _"Model predictive control... can be viewed as a specialized rollout method that is based on a suboptimal optimization for reaching a goal state... The optimization is repeated at each step $k$ with the new state $x_k$."_ (Bertsekas, p. 108)

Replanning at every step provides feedback. If the model diverges from reality, MPC sees the error immediately at the next step and re-optimizes.2

---

## 3. The Limits of Certainty Equivalence

MPC relies on a simplifying assumption known as **Certainty Equivalence**. We replace the stochastic, unknown system dynamics with the "expected" prediction of our neural network and plan as if the world were deterministic.

> _"Assume that certainty equivalence holds (i.e., replace stochastic quantities by some typical values, such as their expected values) and apply exact DP..."_ (Bertsekas, Section 2.3.2, p. 76)

This fails when the model is **confidently wrong**. A standard neural network minimizes Mean Squared Error (MSE), which targets the mean of the data. In regions with no data, the network might predict a valid-looking mean with high confidence, masking its ignorance. To plan safely, the agent needs to quantify **Uncertainty**.

---

## 4. Aleatoric vs. Epistemic Uncertainty

To make robust decisions, we must distinguish between two types of uncertainty (Lecture 11, Slide 14):

1. **Aleatoric Uncertainty (Statistical):** Inherent noise in the system (e.g., a coin flip). This is irreducible.
    
2. **Epistemic Uncertainty (Model):** Ignorance about the underlying physics due to a lack of data.3 "The model is certain about the data, but _we_ are not certain about the model." This is **reducible** with more data.
    

Epistemic uncertainty is the key to solving the "hallucinating planner" problem. If the model knows it is ignorant about a specific state-action pair, the planner can avoid it.

### Deep Ensembles

Since true Bayesian inference is intractable for neural networks, we use **Bootstrap Ensembles**. We train $N$ independent models $\{f_{\theta_1}, \dots, f_{\theta_N}\}$ on the same dataset.

- **Prediction:** The mean of the ensemble $\frac{1}{N} \sum f_{\theta_i}(s, a)$.
    
- **Uncertainty:** The variance (disagreement) among the ensemble members.
    

If the models disagree, we are in Out-Of-Distribution (OOD) territory.

---

## 5. Uncertainty-Aware Planning

Armed with an estimate of uncertainty, we can modify our planning objective to implement **Risk-Averse Control** or **Dual Control**.

$$ J(a) = \mathbb{E}[\text{Reward}] - \lambda \cdot \text{Var}[\text{Dynamics}] $$

- **Pessimism ($\lambda > 0$):** We penalize actions with high variance. This forces the planner to stay in "known" regions of the state space, preventing the exploitation of model hallucinations.
    
- **Optimism ($\lambda < 0$):** We reward variance to encourage exploration. This drives the agent to visit unknown states to gather data and reduce epistemic uncertainty.
    

This connects to the concept of **Dual Control** mentioned by Bertsekas (p. 42), where inputs must balance _probing_ (learning the system) and _control_ (achieving the goal).

---

## 6. Complex Observations and Latent Spaces

Finally, when the state space consists of high-dimensional images ($o_t$), planning directly in pixel space is inefficient. We often learn a Latent Space Model.

$$ z_t = E(o_t), \quad z_{t+1} = g(z_t, a_t) $$

This connects to Bertsekas’s discussion of **Partial State Information** and **Belief States** (**Section 1.3.6**).

> _"The belief state... can serve as 'state' in an appropriate DP algorithm."_ (Bertsekas, p. 35)

In this context, the latent state $z_t$ acts as a sufficient statistic (a belief state) summarizing the history of observations. By planning in this compact latent space, we perform **Problem Approximation** (Bertsekas, **Chapter 6**), effectively aggregating complex pixel states into a manageable representation for the planner.

---

## Summary

Model-Based RL bridges the gap between the sample-inefficiency of learning and the rigorous structure of control theory.

1. **System Identification** provides the map but suffers from **Distribution Shift**.
    
2. **MPC (Replanning)** mitigates model errors by closing the loop, aligning with **Rolling Horizon** theory.
    
3. **Ensembles** estimate **Epistemic Uncertainty**, allowing the agent to distinguish between known physics and dangerous hallucinations, moving beyond brittle **Certainty Equivalence**.