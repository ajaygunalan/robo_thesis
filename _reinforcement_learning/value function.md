### What is a Value Function?
A value function tells us how good something is in the context of reinforcement learning. "Good" means the expected total reward in the future if we start from a certain situation and follow a given policy.
Formally, a value function is just an expectation of cumulative discounted reward. Different value functions measure "goodness" of different things (states, or state–action pairs).

---

### V-value (State Value Function)
The state value function $V^\pi(s)$ measures how good it is to be in a state $s$ under policy $\pi$.

$$V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_t \,\big|\, s_0 = s \right]$$

Example: If a robot is at the charging station (state), the V-value tells us the long-term reward it expects if it follows its current policy from there.

---

### Q-value (Action Value Function)
The action value function $Q^\pi(s,a)$ measures how good it is to take action $a$ in state $s$ and then follow policy $\pi$.

$$Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t r_t \,\big|\, s_0 = s, a_0 = a \right]$$

Example: If the robot is at a junction (state), the Q-value for action "turn left" vs. "turn right" tells us which choice will likely give more long-term reward.

---

### Relationship between Them
- V-value: average over all actions according to the policy.
- Q-value: specific to a chosen action.

$$V^\pi(s) = \sum_a \pi(a|s) \, Q^\pi(s,a)$$

---

### Clarification about "S-value"
There is no separate concept of "S-value." Often people confuse V-value with "state-value" (sometimes written as S-value informally). The proper term is V-value function, not S-value.

---

In short:
- Value function = expected future reward measure.
- V-value = goodness of a state.
- Q-value = goodness of a state–action pair.