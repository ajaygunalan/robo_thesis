A Markov Decision Process (MDP) is the standard mathematical framework used to describe decision-making problems in reinforcement learning. It models an environment where an agent interacts over time. An MDP is defined by the tuple

M=(S,A,P,r,γ)\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{P}, r, \gamma)

- **S**: set of states (the situations the agent can be in).
    
- **A**: set of actions (choices available to the agent).
    
- **P**: transition probability function P(s′∣s,a)P(s'|s,a), which gives the probability of moving to state s′s' when taking action aa in state ss.
    
- **r**: reward function r(s,a)r(s,a), the immediate scalar feedback for taking action aa in state ss.
    
- **γ**: discount factor 0≤γ<10 \leq \gamma < 1, which determines how much the agent values future rewards compared to immediate ones.
    

The goal of the agent in an MDP is to find a policy (a mapping from states to actions) that maximizes the expected cumulative reward over time.

