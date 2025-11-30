Actor–Critic is a family of reinforcement learning methods that combine two components:

- **Actor**: the part of the model that represents the policy, i.e., it chooses which action to take in a given state. It directly outputs actions (deterministic or probabilistic).
    
- **Critic**: the part of the model that estimates the [[value function]] (e.g., Q-value or V-value). It evaluates how good the action taken by the actor is, by predicting expected future rewards.
    

The actor updates its policy parameters in the direction suggested by the critic, while the critic updates its value estimates based on observed rewards and temporal-difference errors.

This setup is useful because:

- Pure policy-based methods (actor only) can be unstable since they rely only on reward signals.
    
- Pure value-based methods (critic only) can’t easily handle continuous action spaces.
    
- Actor–Critic combines both: the actor explores and learns actions, while the critic stabilizes learning by providing a baseline/value signal.
    

Classic examples: **A2C/A3C (Advantage Actor–Critic), DDPG (Deep Deterministic Policy Gradient), SAC (Soft Actor–Critic)**.

==