# Policy Gradient 

We start with a **stochastic policy** parameterized by θ:

$$\pi_\theta(a \mid s)$$

This policy tells us, given a state $s$, how likely we are to take action $a$.

Our goal is to **tune θ** to maximize expected reward by doing gradient ascent:

$$\theta_{\text{new}} \leftarrow \theta_{\text{prev}} + \alpha \nabla_\theta J(\theta)$$

So the whole game is: **compute $\nabla_\theta J(\theta)$**.


## Objective: Expected Return over Trajectories

Consider an episode (trajectory):

$$\tau = (s_1, a_1, s_2, a_2, \ldots, s_T, a_T)$$

Define the **reward** of a trajectory as:

$$R(\tau) = \sum_{t=1}^{T} r(s_t, a_t) \tag{4}$$

The policy objective is:

$$J(\theta) = \mathbb{E}_{\tau} \left[ \sum_{t=1}^{T} r(s_t, a_t) \right] = \mathbb{E}_\tau [R(\tau)]$$

Writing the expectation as a sum over all possible trajectories:

$$J(\theta) = \sum_{\tau} P_\theta(\tau) \cdot R(\tau)$$

where $P_\theta(\tau)$ is the probability of seeing trajectory τ under policy $\pi_\theta$.

Now differentiate:

$$\nabla_\theta J(\theta) = \sum_\tau \nabla_\theta P_\theta(\tau) \cdot R(\tau) \tag{7}$$

So the next step is: **what is $P_\theta(\tau)$?**



## Factorizing the Trajectory Probability

A trajectory is $s_1, a_1, s_2, a_2, \ldots$, so its probability is:

$$P_\theta(\tau) = P(s_1, a_1, s_2, a_2, \ldots, s_T, a_T)$$

Using the chain rule of probability, we can write this as:

$$P_\theta(\tau) = P(s_1) \cdot P(a_1 \mid s_1) \cdot P(s_2 \mid s_1, a_1) \cdot P(a_2 \mid s_2, s_1, a_1) \cdot P(s_3 \mid s_2, a_2, s_1, a_1) \cdots$$

This is the fully general (ugly) factorization. Now we use two standard assumptions.

### Markov Property (Environment)

The environment is a Markov decision process, so the **next state only depends on current state and action**:

$$P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots) = P(s_{t+1} \mid s_t, a_t)$$

So all that history in the conditioning of $s_{t+1}$ can be dropped.

### Policy Structure (Agent)

Our policy only looks at the **current state**, not the full history:

$$P(a_t \mid s_t, s_{t-1}, a_{t-1}, \ldots) = \pi_\theta(a_t \mid s_t)$$

So the messy action conditionals become nice policy terms.

### Putting it Back Together

Substituting those simplifications into the big product:

$$P_\theta(\tau) = P(s_1) \cdot \pi_\theta(a_1 \mid s_1) \cdot P(s_2 \mid s_1, a_1) \cdot \pi_\theta(a_2 \mid s_2) \cdot P(s_3 \mid s_2, a_2) \cdots$$

We can write this compactly as:

$$P_\theta(\tau) = P(s_1) \prod_{t=1}^{T} \Big[ \pi_\theta(a_t \mid s_t) \cdot P(s_{t+1} \mid s_t, a_t) \Big] \tag{13}$$

Only the **policy terms $\pi_\theta$** depend on θ. The environment dynamics $P(s_{t+1} \mid s_t, a_t)$ and initial state distribution $P(s_1)$ do not.



## The Log Trick

Now take the log of Equation (13):

$$\log P_\theta(\tau) = \log P(s_1) + \sum_{t=1}^{T} \Big[ \log \pi_\theta(a_t \mid s_t) + \log P(s_{t+1} \mid s_t, a_t) \Big]$$

Since only the policy terms depend on θ:

$$\log P_\theta(\tau) = \sum_{t=1}^{T} \log \pi_\theta(a_t \mid s_t) + \text{const}$$

Now differentiate:

$$\nabla_\theta \log P_\theta(\tau) = \sum_{t=1}^{T} \nabla_\theta \log \pi_\theta(a_t \mid s_t) \tag{16}$$

This is where we use the general identity for the derivative of a logarithm:

$$\frac{d}{dx}\log f(x) = \frac{f'(x)}{f(x)}$$

Applied to probabilities:

$$\nabla_\theta \log P_\theta(\tau) = \frac{\nabla_\theta P_\theta(\tau)}{P_\theta(\tau)}$$

Rearrange this:

$$\nabla_\theta P_\theta(\tau) = P_\theta(\tau) \cdot \nabla_\theta \log P_\theta(\tau) \tag{19}$$



## Plugging Back into the Objective Gradient

Recall Equation (7). Using the identity from Equation (19):

$$\nabla_\theta J(\theta) = \sum_\tau P_\theta(\tau) \cdot \nabla_\theta \log P_\theta(\tau) \cdot R(\tau)$$

This is an expectation over trajectories:

$$\nabla_\theta J(\theta) = \mathbb{E}_\tau \left[ \nabla_\theta \log P_\theta(\tau) \cdot R(\tau) \right]$$

Now substitute Equation (16) and recall Equation (4):

$$\nabla_\theta J(\theta) = \mathbb{E}_\tau \left[ \left(\sum_{t=1}^{T} \nabla_\theta \log \pi_\theta(a_t \mid s_t)\right) \left(\sum_{t=1}^{T} r(s_{t}, a_{t})\right) \right] \tag{22}$$

That's the **classic full-trajectory policy gradient** (REINFORCE form).

In words: for each trajectory, we sum up the log-prob gradients of all actions, multiply by the total return of the trajectory, and take the expectation.



## From Full Return to Reward-to-Go

It's correct, but it's also noisy as hell. Every action gradient at time $t$ gets multiplied by the **entire** episode reward, including rewards that happened _before_ that action. That doesn't make much sense intuitively and it inflates variance. This is where **reward-to-go** comes in.

$$G_t(\tau) := \sum_{t'=t}^{T} r(s_{t'}, a_{t'})$$

$$\nabla_\theta J(\theta) = \mathbb{E}_\tau \left[ \sum_{t=1}^{T} \nabla_\theta \log \pi_\theta(a_t \mid s_t) G_t(\tau) \right] \tag{25}$$

Same expectation as Equation (22), but lower variance: we stopped blaming actions for rewards that preceded them. For discounting, just use $G_t(\tau) := \sum_{t}^{T} \gamma^{t'-t} r(s_{t'}, a_{t'})$.



## Monte Carlo Estimation

Equation (25) is elegant, but computing $\mathbb{E}_{\tau}[\cdot]$ exactly requires summing over all possible trajectories—an astronomically large (or infinite) set—with environment dynamics we typically don't know in closed form. The solution: **sample and average**.

Collect $N$ trajectories by running the policy, where each trajectory $\tau_i = (s_{i,1}, a_{i,1}, r_{i,1}, \dots, s_{i,T}, a_{i,T}, r_{i,T})$. For each, compute reward-to-go backwards:

$$G_{i,T} = r_{i,T}, \quad G_{i,t} = r_{i,t} + G_{i,t+1} \quad \text{for } t = T-1,\dots,1$$

Then estimate the gradient:

$$\hat{g} = \frac{1}{N} \sum_{i=1}^{N} \sum_{t=1}^{T} \nabla_\theta \log \pi_\theta(a_{i,t} \mid s_{i,t}) G_{i,t}$$

Update the policy:

$$\theta \leftarrow \theta + \alpha \hat{g}$$

This estimator $\hat{g}$ is unbiased (its expectation equals the true gradient) and its variance shrinks with more trajectories. By the law of large numbers, it converges to $\nabla_\theta J(\theta)$ as $N \to \infty$.
