# Supervised Learning of Behaviors

## Introduction: The Promise and Pitfall of Imitation

Imagine teaching a robot to drive by showing it thousands of hours of expert driving footage. The robot watches, learns the mapping from what it sees to what actions the expert takes, and then attempts to drive on its own. This approach—called **behavioral cloning**—is conceptually identical to standard supervised learning: we have inputs (observations), outputs (actions), and we train a neural network to predict the latter from the former.

Yet something goes wrong. The robot drives well for a few seconds, then drifts slightly, encounters a situation it never saw during training, makes a poor decision, drifts further, and eventually crashes. This failure is not a bug in the implementation—it is a fundamental tension at the heart of imitation learning.

The core issue is the **violation of the i.i.d. assumption**. In standard supervised learning, we assume training samples are drawn independently from some fixed distribution, and test samples come from the same distribution. In sequential decision-making, this assumption fails catastrophically. The policy's actions influence future states. If we train on expert demonstrations where states come from the expert's induced distribution $p_{\pi^*}(\mathbf{o}_t)$, but deploy a learned policy that induces a different distribution $p_{\pi_\theta}(\mathbf{o}_t)$, we face **distributional shift**. Small errors compound: a deviation at time $t$ leads to states the expert never visited, where the policy has no reliable training signal.

```
                    DISTRIBUTIONAL SHIFT
                    
  Training Time:          ══════════════════════════════►
                                Expert's trajectory
  ┌─────────────────────────────────────────────────────┐
  │    ●━━━━●━━━━●━━━━●━━━━●━━━━●━━━━●━━━━●━━━━●━━━━●   │
  │         States the policy learns from               │
  └─────────────────────────────────────────────────────┘
  
  Test Time:              ══════════════════════════════►
                                Learned policy's trajectory
  ┌─────────────────────────────────────────────────────┐
  │    ●━━━━●━━━━●╲                                     │
  │                ╲━━●━━━●                             │
  │                       ╲━━●━━━●━━━●  ← Unfamiliar    │
  │                              Drift    territory!    │
  └─────────────────────────────────────────────────────┘
```

This chapter explores four complementary strategies to address this fundamental challenge:

1. **Better models**: Architectures that can represent complex, history-dependent, multimodal behaviors
2. **Smart data collection**: Engineering the training distribution to include recovery behaviors
3. **Pre-training paradigms**: Combining broad, diverse data with narrow, high-quality demonstrations
4. **Multi-task learning**: Training goal-conditioned policies that naturally see diverse states

We begin with the question of model design: even if we could perfectly optimize our policy, what structural limitations might prevent us from representing the expert's behavior?

---

## Part 1: Models for Imitation Learning

### 1.1 Two Fundamental Failure Modes

Before discussing solutions, we must understand what can go wrong even with perfect optimization. Two structural issues plague naive behavioral cloning: **non-Markovian behavior** and **multimodal behavior**.

#### Non-Markovian Behavior

A Markovian policy $\pi_\theta(\mathbf{a}_t | \mathbf{o}_t)$ maps only the current observation to an action. If we observe the same visual scene twice, we take the same action twice—regardless of history. But human demonstrators are non-Markovian. They use memory: having already checked the left mirror, a driver now checks the right. Having already tried one approach to a problem, they try another.

Formally, the expert's policy is:

$$\pi^*(\mathbf{a}_t | \mathbf{o}_1, \mathbf{o}_2, \ldots, \mathbf{o}_t)$$

If we fit a Markovian policy to non-Markovian demonstrations, the best we can do is match the marginal distribution—averaging over all possible histories consistent with the current observation:

$$\pi_\theta(\mathbf{a}_t | \mathbf{o}_t) \approx \mathbb{E}_{\mathbf{o}_{1:t-1} \sim p(\cdot | \mathbf{o}_t)}\left[\pi^*(\mathbf{a}_t | \mathbf{o}_{1:t})\right]$$

This average may be suboptimal or even dangerous.

#### Multimodal Behavior

Even conditioned on full history, experts may exhibit multimodality. In the same situation, the expert sometimes turns left around a tree, sometimes right. Both are valid strategies. If we parameterize $\pi_\theta$ as a unimodal Gaussian (outputting mean and variance), maximum likelihood estimation yields the mean of the modes—which might correspond to driving directly into the tree.

```
           MULTIMODAL BEHAVIOR PROBLEM
           
    Expert demonstrations:         Unimodal policy learns:
    
         ╱── Left path              
        ╱                                 │
       ●     🌳                      ●━━━━━🌳━━━━ Crash!
        ╲                                 │
         ╲── Right path                   
                                    (averages to center)
    
    Both paths are valid,           Mean of modes is
    expert takes either one         catastrophically wrong
```

These two failure modes demand different solutions. For non-Markovian behavior, we need architectures that incorporate history. For multimodal behavior, we need expressive output distributions that can represent multiple modes.

---

### 1.2 Handling History with Sequence Models

The naive approach to history-dependence concatenates all past frames as input. This is problematic: sequences have variable length, and the number of parameters would scale with sequence length (or require padding to some maximum).

The principled solution uses a **sequence model with shared weights** across timesteps. Each frame is processed by the same encoder (typically a CNN), producing per-timestep feature vectors. These features are fed into a sequence model—commonly a Transformer—that outputs an action.

```
         SEQUENCE MODEL ARCHITECTURE
         
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │  o_1    │  │  o_2    │  │  o_t    │    Observations
    │ (image) │  │ (image) │  │ (image) │    (frames)
    └────┬────┘  └────┬────┘  └────┬────┘
         │            │            │
         ▼            ▼            ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │   CNN   │  │   CNN   │  │   CNN   │    Shared weights
    │  f_φ    │  │  f_φ    │  │  f_φ    │    (same encoder)
    └────┬────┘  └────┬────┘  └────┬────┘
         │            │            │
         ▼            ▼            ▼
        h_1          h_2          h_t        Feature vectors
         │            │            │
         └────────────┼────────────┘
                      │
                      ▼
              ┌───────────────┐
              │   Sequence    │
              │    Model      │              e.g., Transformer
              │  (Attention)  │
              └───────┬───────┘
                      │
                      ▼
                    a_t                      Action output
```

Mathematically, we now learn $\pi_\theta(\mathbf{a}_t | \mathbf{o}_1, \ldots, \mathbf{o}_t)$, computed as:

$$\mathbf{h}_i = f_\phi(\mathbf{o}_i) \quad \text{for } i = 1, \ldots, t$$

$$\mathbf{a}_t \sim \pi_\theta\left(\cdot \mid \text{SeqModel}_\psi(\mathbf{h}_1, \ldots, \mathbf{h}_t)\right)$$

where $f_\phi$ is the image encoder with shared weights and $\text{SeqModel}_\psi$ is typically a causal Transformer with positional encodings.

#### A Subtle Pitfall: Causal Confusion

Including history helps but introduces a subtle failure mode called **causal confusion**. Consider a braking scenario where the car's brake indicator light is visible in the image. The policy might learn to attend to the brake light (a correlate of braking, since the expert pressed the brake causing the light to illuminate) rather than the actual cause—a pedestrian ahead.

```
         CAUSAL CONFUSION
         
    Scenario A: Brake light visible     Scenario B: Brake light occluded
    
    ┌─────────────────────────┐         ┌─────────────────────────┐
    │  🚶 ← pedestrian        │         │  🚶 ← pedestrian        │
    │                         │         │                         │
    │   ┌───┐                 │         │   ┌───┐                 │
    │   │🔴│ ← brake light ON │         │   │░░│ ← light blocked  │
    │   └───┘                 │         │   └───┘                 │
    └─────────────────────────┘         └─────────────────────────┘
    
    Policy attends to light → ❌         Policy must attend to
    Learns spurious correlation          pedestrian → ✓
```

When the spurious correlate (brake light) is absent but the true cause (pedestrian) is present, a policy that latched onto the correlate fails catastrophically.

Does including history mitigate this? Partially—the model can observe that the brake light was off in previous frames and just turned on. But if the spurious correlate is always present during training, no amount of history helps.

Can DAgger help? Yes, though not efficiently. DAgger collects expert labels on policy-induced states. If the policy fails to brake (because it attended to the unlit brake light), the expert provides a "brake" label for that state. The policy now sees examples where braking is required but the brake light is off, breaking the spurious correlation. However, de Haan et al. show that DAgger requires many expert queries to overcome causal confusion—hundreds for simple tasks like MountainCar, and tens of thousands for complex tasks like Hopper. Their targeted intervention approach achieves similar performance with far fewer queries by explicitly reasoning about causal structure rather than relying purely on distributional coverage.

---

### 1.3 Handling Multimodality: From Discrete to Continuous

With history addressed, we turn to multimodality. The fundamental challenge is representing distributions with multiple valid modes in the action space.

#### Discrete Actions: The Simple Case

For discrete action spaces (turn left, turn right, go straight), multimodality is handled naturally. The policy outputs a categorical distribution via softmax:

$$p(a_1), p(a_2), \ldots, p(a_K)$$

Cross-entropy loss recovers the empirical action frequencies at each state. If the expert turns left 60% of the time and right 40% at a particular state, the policy learns precisely this distribution.

#### Continuous Actions: The Curse of Dimensionality

For continuous actions (joint angles, steering wheel position), discretization seems appealing but faces the curse of dimensionality. If the action space is $\mathbb{R}^d$ and we use $B$ bins per dimension, we have $B^d$ discrete actions.

For a typical robot arm with $d = 7$ degrees of freedom and $B = 256$ bins:

$$256^7 \approx 10^{17} \text{ actions}$$

This is computationally intractable.

#### Autoregressive Discretization

The solution factorizes the joint distribution over action dimensions **autoregressively**:

$$p(\mathbf{a}_t | \mathbf{s}_t) = p(a_{t,0} | \mathbf{s}_t) \cdot p(a_{t,1} | \mathbf{s}_t, a_{t,0}) \cdot p(a_{t,2} | \mathbf{s}_t, a_{t,0}, a_{t,1}) \cdots$$

Each conditional is a categorical over $B$ bins. The total number of parameters scales as $O(dB)$ rather than $O(B^d)$. At inference, we sample dimension-by-dimension:

```
       AUTOREGRESSIVE DISCRETIZATION
       
       ┌───────────────────────────────────────────────────┐
       │                                                   │
       │  Image ──► Encoder ──┬──► Block 1 ──► p(a_{t,0}|s)│
       │                      │         │                  │
       │                      │         ▼ sample           │
       │                      │       a_{t,0}              │
       │                      │         │                  │
       │                      ├─────────┼──► Block 2 ──►   │
       │                      │         │    p(a_{t,1}|s, a_{t,0})
       │                      │         ▼ sample           │
       │                      │       a_{t,1}              │
       │                      │         │                  │
       │                      └─────────┴──► Block 3 ──►   │
       │                                     p(a_{t,2}|s, a_{t,0}, a_{t,1})
       └───────────────────────────────────────────────────┘
```

**Why does this preserve multimodality?** The key insight is that the joint distribution $p(\mathbf{a} | \mathbf{s})$ can be arbitrarily complex while each conditional remains a simple categorical.

Consider a bimodal distribution with modes at "turn left" $= (-1, 0, 0)$ and "turn right" $= (1, 0, 0)$:

1. The marginal over the first dimension $p(a_{t,0} | \mathbf{s}_t)$ is bimodal with peaks at $-1$ and $+1$
2. After sampling (say $a_{t,0} = -1$), the conditional $p(a_{t,1} | \mathbf{s}_t, a_{t,0} = -1)$ is unimodal at $0$
3. The multimodality is captured in the first factor; subsequent factors refine within the chosen mode

The product of these simple categoricals reconstructs the complex multimodal joint:

$$p(a_{t,2}|\mathbf{s}_t, a_{t,0}, a_{t,1}) \cdot p(a_{t,1}|\mathbf{s}_t, a_{t,0}) \cdot p(a_{t,0}|\mathbf{s}_t) = p(a_{t,0}, a_{t,1}, a_{t,2}|\mathbf{s}_t) = p(\mathbf{a}_t|\mathbf{s}_t)$$

---

### 1.4 Expressive Continuous Distributions: Flow Matching and Diffusion

An alternative to discretization is using expressive continuous density models. The core idea: augment the policy network with a noise input $\xi \sim \mathcal{N}(0, \mathbf{I})$ and learn a mapping from $(\mathbf{o}_t, \xi)$ to $\mathbf{a}_t$. If different noise samples map to different action modes, we capture multimodality while remaining in continuous action space.

```
       NOISE-CONDITIONED POLICY
       
       ┌─────────────────────────────────────────────┐
       │                                             │
       │   Noise ξ ~ N(0,I)                          │
       │        │                                    │
       │        ▼                                    │
       │   ┌─────────┐      ┌─────────┐              │
       │   │         │      │         │              │
       │   │ Neural  │ ───► │ Action  │              │
       │   │   Net   │      │  a_t    │              │
       │   │         │      │         │              │
       │   └─────────┘      └─────────┘              │
       │        ▲                                    │
       │        │                                    │
       │   Observation o_t                           │
       │                                             │
       │   Different ξ ──► Different action modes    │
       └─────────────────────────────────────────────┘
```

The key challenge is ensuring the model actually **uses** the noise. A network can easily learn to ignore $\xi$, collapsing back to a deterministic (and hence unimodal) mapping. Three families of methods enforce noise utilization:

- **Variational Autoencoders (VAEs)**: KL regularizer ensures the latent prior is used
- **Normalizing Flows**: Invertibility guarantees noise determines output
- **Diffusion/Flow Matching**: Iterative denoising where noise determines the trajectory through sample space

We focus on **flow matching**, which has become the dominant approach for robotics applications.

#### The Core Idea of Flow Matching

We want to sample from a complex data distribution $p(\mathbf{x})$ (in our case, $p(\mathbf{a} | \mathbf{o})$). Sampling directly is hard because we don't know $p(\mathbf{x})$ analytically; we only have samples (the expert actions).

The insight: learn a **deterministic transformation** that maps samples from a simple distribution (Gaussian noise) to samples from $p(\mathbf{x})$.

Specifically, we learn a time-dependent **velocity field** $v(\mathbf{x}_\tau, \tau)$ that, when integrated, transports samples from the noise distribution at $\tau = 0$ to the data distribution at $\tau = 1$:

$$\mathbf{x}_1 = \mathbf{x}_0 + \int_0^1 v(\mathbf{x}_\tau, \tau) \, d\tau$$

If $v$ is learned correctly and we start with $\mathbf{x}_0 \sim \mathcal{N}(0, \mathbf{I})$, then $\mathbf{x}_1 \sim p(\mathbf{x})$.

```
       FLOW MATCHING: TRANSPORTING NOISE TO DATA
       
       τ = 0 (Noise)                      τ = 1 (Data)
       
       ┌───────────────────────────────────────────────┐
       │                                               │
       │    ○ ─────────────────────────────────► ●     │
       │      ╲                               ╱        │
       │       ╲    Velocity field v(x,τ)   ╱         │
       │        ╲     guides the flow      ╱          │
       │    ○ ───╲─────────────────────── ╱──► ●      │
       │          ╲                     ╱             │
       │           ╲                   ╱              │
       │    ○ ──────────────────────────────► ●       │
       │                                               │
       │  Gaussian               Multimodal data       │
       │  samples                distribution          │
       └───────────────────────────────────────────────┘
```

#### Training: Conditional Flow Matching

The challenge is that we don't know the ground-truth velocity field. Flow matching sidesteps this by matching **conditional** velocity fields that are easy to compute.

Consider a single data point $\mathbf{x}_1$ (an expert action). We define a **linear interpolation path** between a noise sample $\mathbf{x}_0 \sim \mathcal{N}(0, \mathbf{I})$ and $\mathbf{x}_1$:

$$\mathbf{x}_\tau = \tau \mathbf{x}_1 + (1 - \tau) \mathbf{x}_0$$

The velocity along this path is the time derivative:

$$\frac{d\mathbf{x}_\tau}{d\tau} = \mathbf{x}_1 - \mathbf{x}_0$$

This is the **target velocity**: the direction and magnitude that moves a sample from $\mathbf{x}_0$ at $\tau = 0$ to $\mathbf{x}_1$ at $\tau = 1$ along a straight line.

```
       LINEAR INTERPOLATION PATH
       
                    x_τ = τ·x_1 + (1-τ)·x_0
       
       x_0 (noise)                           x_1 (data)
           ○────────────────●────────────────────●
           │                │                    │
           │                │                    │
         τ = 0           τ = t̂              τ = 1
       
       Target velocity at any point: v = x_1 - x_0
       (constant along the straight-line path)
```

We train a neural network $v_\theta(\mathbf{x}_\tau, \tau)$ to predict this target velocity:

$$\mathcal{L}(\theta) = \mathbb{E}_{\mathbf{x}_0 \sim \mathcal{N}(0, \mathbf{I}), \, \mathbf{x}_1 \sim p_{\text{data}}, \, \tau \sim \mathcal{U}(0, 1)} \left[ \| v_\theta(\mathbf{x}_\tau, \tau) - (\mathbf{x}_1 - \mathbf{x}_0) \|^2 \right]$$

where $\mathbf{x}_\tau = \tau \mathbf{x}_1 + (1 - \tau) \mathbf{x}_0$.

**Why does this work?** Each data point $\mathbf{x}_1$ defines a family of paths (one for each $\mathbf{x}_0$). We train the velocity field to be correct on average over all paths. When we sample at test time, we draw a single $\mathbf{x}_0$ and integrate; the learned velocity field "combines" information from all training examples to route this particular $\mathbf{x}_0$ toward a plausible $\mathbf{x}_1$.

#### Sampling Procedure

At inference time, we numerically integrate the learned velocity field:

**Algorithm: Flow Matching Sampling**
```
1. Sample x_0 ~ N(0, I)
2. For τ in {0, Δτ, 2Δτ, ..., 1-Δτ}:
      x_{τ+Δτ} ← x_τ + v_θ(x_τ, τ) · Δτ     [Euler step]
3. Return x_1
```

The number of function evaluations (NFE) is $1 / \Delta\tau$. Typical values are 10-100 steps. Higher-order integrators (Heun, Runge-Kutta) can reduce NFE.

#### Conditioning on Observations

For policy learning, we want $p(\mathbf{a} | \mathbf{o})$, not just $p(\mathbf{a})$. The velocity network becomes $v_\theta(\mathbf{o}_t, \mathbf{a}_{t,\tau}, \tau)$—it takes the observation as conditioning input.

The complete training procedure for a flow matching policy:

**Algorithm: Flow Matching Policy Training**
```
For each minibatch:
    For each element j in batch:
        1. Sample (o_t^(j), a_t^(j)) from demonstration dataset
        2. Sample noise: a_{t,0}^(j) ~ N(0, I)
        3. Sample flow time: τ^(j) ~ Uniform(0, 1)
        4. Compute noisy action: a_{t,τ}^(j) = τ^(j)·a_t^(j) + (1-τ^(j))·a_{t,0}^(j)
    
    Compute loss:
        L = Σ_j || v_θ(o_t^(j), a_{t,τ}^(j), τ^(j)) - (a_t^(j) - a_{t,0}^(j)) ||²
                                                        └──────────────────┘
                                                          target velocity
    
    Update θ with gradient descent on L
```

```
       FLOW MATCHING POLICY ARCHITECTURE
       
       ┌─────────────────────────────────────────────────────┐
       │                                                     │
       │                    ┌─────────────┐                  │
       │                    │   Velocity  │                  │
       │                    │   v_{t,τ}   │ ◄── Output       │
       │                    └──────┬──────┘                  │
       │                           │                         │
       │                    ┌──────┴──────┐                  │
       │                    │             │                  │
       │                    │   Neural    │                  │
       │                    │   Network   │                  │
       │                    │             │                  │
       │                    └──────┬──────┘                  │
       │                           │                         │
       │              ┌────────────┼────────────┐            │
       │              │            │            │            │
       │              ▼            ▼            ▼            │
       │         ┌────────┐  ┌─────────┐  ┌─────────┐        │
       │         │   τ    │  │ a_{t,τ} │  │   o_t   │        │
       │         │ (time) │  │ (noisy  │  │ (obs)   │        │
       │         │        │  │ action) │  │         │        │
       │         └────────┘  └─────────┘  └─────────┘        │
       │                                                     │
       └─────────────────────────────────────────────────────┘
```

#### Design Decisions and Tradeoffs

Several practical considerations affect flow matching policies:

**Number of denoising steps**: More steps yield better sample quality but slower inference. For real-time robotics at 50 Hz control, this is a bottleneck. Distillation methods and few-step samplers (consistency models) are active research areas.

**Noise schedule**: Linear interpolation is simplest, but other schedules (cosine, learned) can improve performance. The schedule affects how "difficult" each $\tau$ value is to denoise.

**Network architecture**: The velocity network must take $\tau$ as input. Common choices include sinusoidal position embeddings (as in Transformers) or FiLM conditioning layers.

**Relation to diffusion**: DDPM-style diffusion models parameterize the score $\nabla_{\mathbf{x}} \log p_\tau(\mathbf{x})$ or the noise $\epsilon$ added at each step. Flow matching parameterizes the velocity. These are related by change of variables. Flow matching's linear interpolation paths are often simpler than diffusion's SDE formulation, leading to easier training and fewer denoising steps.

---

### 1.5 Action Chunking: Temporal Consistency Through Trajectory Prediction

A seemingly small architectural detail makes a substantial difference: instead of predicting a single action, predict a **chunk** of future actions.

#### Standard vs. Chunked Policies

A conventional policy operates in a single-step loop:

$$\text{Standard: } \mathbf{a}_t \sim \pi_\theta(\mathbf{a}_t | \mathbf{o}_t)$$

An action-chunked policy predicts $K$ future actions simultaneously:

$$\text{Chunked: } \mathbf{a}_{t:t+K} \sim \pi_\theta(\mathbf{a}_{t:t+K} | \mathbf{o}_t)$$

where $\mathbf{a}_{t:t+K} = (\mathbf{a}_t, \mathbf{a}_{t+1}, \ldots, \mathbf{a}_{t+K})$.

```
       STANDARD VS. ACTION-CHUNKED POLICY
       
       Standard Policy:
       ┌────────────────────────────────────────────────┐
       │  o_t → [Policy] → a_t → Execute → o_{t+1}     │
       │  o_{t+1} → [Policy] → a_{t+1} → Execute → ... │
       │  (recompute at every timestep)                │
       └────────────────────────────────────────────────┘
       
       Action-Chunked Policy:
       ┌────────────────────────────────────────────────┐
       │  o_t → [Policy] → [a_t, a_{t+1}, ..., a_{t+K}]│
       │                          │                    │
       │                          ▼                    │
       │         Execute entire chunk open-loop        │
       │                          │                    │
       │                          ▼                    │
       │  o_{t+K+1} → [Policy] → [next chunk] → ...   │
       └────────────────────────────────────────────────┘
```

The policy's output space becomes $\mathbb{R}^{K \times d_a}$ where $d_a$ is the action dimension. For flow matching, we denoise this larger tensor jointly.

#### Why Does Chunking Help?

**Temporal consistency**: A single-step policy can be temporally inconsistent—jittery, oscillating between modes at each timestep. An action chunk must commit to a mode for the chunk's duration. This is particularly important when data has multimodality (different experts, different valid strategies).

**Reduced effective horizon**: If we chunk with $K = 50$ at 50 Hz, we make decisions at 1 Hz. Errors compound over *decision* timesteps, not *control* timesteps. The effective horizon for distributional shift is reduced by factor $K$.

**Better credit assignment**: The model sees entire trajectory segments as targets. Predicting a smooth trajectory is easier than predicting frame-by-frame, since consecutive actions are highly correlated.

#### Tradeoffs

**Open-loop execution**: We don't replan during the chunk. If the environment changes unexpectedly (a human bumps an object), we can't react until the chunk ends. 

**Mitigation**: Receding-horizon control—execute only the first $K' < K$ actions of each chunk, then replan.

**Chunk length selection**: Too short loses benefits; too long becomes too open-loop. Typical values are 10-50 timesteps (0.2-1 second at 50 Hz).

---

### 1.6 Case Study: Putting It All Together

Modern imitation learning systems combine these techniques. The **Diffusion Policy** (Chi et al., 2023) applies diffusion/flow matching to visuomotor policy learning:

- CNN encoder (ResNet-18) processes image observations
- U-Net or Transformer denoises action chunks with prediction horizons that vary by task (the paper defines $T_o$ for observation horizon, $T_p$ for prediction horizon, and $T_a$ for action execution horizon, with typical values ranging from 8 to 16 depending on the task's temporal requirements)
- Works on real robots with ~10 demonstrations per task

The **π₀ system** (Physical Intelligence, 2024) represents the current state-of-the-art, combining:

- Pre-trained VLM backbone: SigLIP (400M parameters) for vision + Gemma (2.6B) for language
- Action expert: 300M parameter module using flow matching
- Action chunks of ~50 timesteps as joint angles
- Multi-embodiment training across robots with 7-18 degrees of freedom

```
       π₀ ARCHITECTURE OVERVIEW
       
    ┌──────────────────────────────────────────────────────────┐
    │                                                          │
    │  Images ──► ViT ──► ViT ──► ViT ─┐                       │
    │  (1-3)                           │                       │
    │                                  ▼                       │
    │                          ┌──────────────┐                │
    │  Language ──────────────►│  Pre-trained │                │
    │  ("fold shirt")          │     VLM      │                │
    │                          │  SigLIP +    │                │
    │                          │   Gemma      │                │
    │                          └──────┬───────┘                │
    │                                 │                        │
    │                    Cross-attention                       │
    │                                 │                        │
    │                                 ▼                        │
    │                          ┌──────────────┐                │
    │  Noise + q_t ──────────►│    Action    │──► Action chunk│
    │  (proprioception)        │    Expert    │   (~50 steps)  │
    │                          │  (300M, FM)  │                │
    │                          └──────────────┘                │
    │                                                          │
    └──────────────────────────────────────────────────────────┘
```

---

## Part 2: The Broad vs. Narrow Data Tradeoff

### 2.1 Why Data Collection Strategy Matters

Even with perfect model architectures, behavioral cloning fails if the training distribution doesn't cover states the policy will encounter. Two practical techniques address this through data collection:

#### Intentional Mistakes and Corrections

Deliberately introduce perturbations during demonstration and record corrective actions. The demonstrator deviates from the optimal trajectory, then recovers.

```
       MISTAKES AND CORRECTIONS
       
       Optimal trajectory:     With intentional mistakes:
       
           ●━━━━━━━━━━●            ●━━━━●╲
                                         ╲━━●  ← mistake
                                             ╲
                                              ●━━●  ← correction
                                                   ╲
                                                    ●
       
       Hurts training loss (mistakes are suboptimal)
       BUT provides recovery signal the policy needs!
```

This hurts training loss (mistakes are suboptimal) but provides training signal for recovery—precisely what the policy needs when it inevitably makes mistakes at test time.

#### Data Augmentation

Synthetically generate "correction" examples. A classic technique from autonomous driving: mount side-facing cameras during data collection. The side cameras see the road from an angle, which looks like a situation where the car has drifted. By labeling side-camera images with corrective steering (turning back toward center), we get recovery data without actually driving off the road.

---

### 2.2 The Fundamental Tradeoff

Data quality exists along two axes:

**Broad data**: Sees many situations but may have suboptimal actions (random exploration, YouTube videos, low-quality teleoperation)

**Narrow data**: High-quality actions but limited state coverage (expert demonstrations of specific tasks)

```
       THE BROAD VS. NARROW TRADEOFF
       
                        Action Quality
                             ▲
                             │
                High         │    ★ Ideal
                             │    (but expensive/impossible)
                             │
                             │         ┌──────────┐
                             │         │  Narrow  │
                             │         │   data   │
                             │         └──────────┘
                             │
                             │
                             │  ┌──────────┐
                Low          │  │  Broad   │
                             │  │   data   │
                             │  └──────────┘
                             │
                             └────────────────────────►
                            Low                    High
                                 State Coverage
```

Neither alone is sufficient:
- Broad data alone: Policy "knows" many situations but doesn't know what to *do* well in any of them
- Narrow data alone: Policy performs well on-distribution but has no recovery behavior for off-distribution states

---

### 2.3 The Pre-training + Post-training Paradigm

The solution mirrors large language model training:

**Pre-training** on broad, lower-quality data. The model learns diverse representations—how objects look, how arms move, spatial relationships—without necessarily learning optimal policies.

**Post-training** (fine-tuning/SFT) on narrow, high-quality data. The model learns *what we want it to do* on top of the rich representations from pre-training.

```
       PRE-TRAINING + POST-TRAINING PARADIGM
       
       ┌─────────────────────────────────────────────────────────┐
       │                                                         │
       │   PRE-TRAINING                    POST-TRAINING         │
       │                                                         │
       │   ┌─────────────┐                ┌─────────────┐        │
       │   │  Broad data │                │ Narrow data │        │
       │   │  ~10,000 hrs│                │  ~20 hrs    │        │
       │   │             │                │             │        │
       │   │  - YouTube  │                │  - Expert   │        │
       │   │  - Teleop   │                │    demos    │        │
       │   │  - Diverse  │                │  - Specific │        │
       │   │    robots   │                │    task     │        │
       │   └──────┬──────┘                └──────┬──────┘        │
       │          │                              │               │
       │          ▼                              ▼               │
       │   ┌─────────────┐                ┌─────────────┐        │
       │   │    Base     │ ─────────────► │   Final     │        │
       │   │    Model    │   Fine-tune    │   Policy    │        │
       │   └─────────────┘                └─────────────┘        │
       │                                                         │
       │   "Knowledge to do it"           "Intent to do it"      │
       │   (visual understanding,         (this specific task,   │
       │    motion primitives,             this strategy)        │
       │    recovery behaviors)                                  │
       │                                                         │
       └─────────────────────────────────────────────────────────┘
```

The two stages serve different purposes:
- Pre-training provides the **knowledge to do it** (visual understanding, motion primitives, recovery behaviors)
- Post-training provides the **intent** (this specific task, this specific strategy)

#### Concrete Numbers from π₀

The π₀ system demonstrates this paradigm with specific data quantities:

- **Pre-training**: ~10,000 hours across multiple robot platforms (bimanual ARX, Franka, UR5e, mobile manipulators)
- **Post-training**: ~20 hours per task (laundry folding, box building)

Key finding: Post-training data alone doesn't work. The robot "gets confused if it makes a mistake" because it's never seen recovery from that state. Combined with pre-training, 20 hours enables robust performance—the pre-training data provides implicit "corrections."

---

## Part 3: Multi-Task Learning to the Rescue

### 3.1 From Single Tasks to Goal-Conditioned Policies

A powerful insight: instead of learning a single task, learn to reach *any* goal. The policy becomes:

$$\pi_\theta(\mathbf{a} | \mathbf{s}, \mathbf{g})$$

where $\mathbf{g}$ is a goal specification (image, coordinates, language instruction).

#### Why Does Multi-Task Learning Help?

Consider a single-task policy for reaching position $\mathbf{p}_1$. Training data includes demonstrations from some initial distribution to $\mathbf{p}_1$. If the policy drifts to a novel state, it has no training signal.

Now consider a goal-conditioned policy trained to reach $\mathbf{p}_1$, $\mathbf{p}_2$, and $\mathbf{p}_3$. Training data includes trajectories from various starting states to various goals. A state that's novel for the "$\mathbf{p}_1$ task" may be on-distribution for the "$\mathbf{p}_2$ task."

```
       MULTI-TASK LEARNING REDUCES DISTRIBUTIONAL SHIFT
       
       Single-task policy (reach p₁):
       
           ┌─────────────────────────┐
           │                         │
           │  ●━━━━━━━━━━●p₁         │
           │  start      goal        │
           │                         │
           │      ○ ← Novel state,   │
           │          no training    │
           │          signal!        │
           └─────────────────────────┘
       
       Goal-conditioned policy (reach any p):
       
           ┌─────────────────────────┐
           │            ●p₂          │
           │           ╱             │
           │  ●━━━━━━━╱━━━●p₁        │
           │  start  ╲               │
           │          ╲              │
           │           ╲●p₃          │
           │                         │
           │      ○ ← This state     │
           │          appears in     │
           │          p₂ training!   │
           └─────────────────────────┘
```

More broadly: goal-conditioning forces the policy to generalize across a space of tasks. This induced generalization improves robustness to distributional shift in any single task.

---

### 3.2 Goal-Conditioned Behavioral Cloning

Given demonstrations $\{\mathbf{s}_1^{(i)}, \mathbf{a}_1^{(i)}, \ldots, \mathbf{s}_T^{(i)}, \mathbf{a}_T^{(i)}\}_{i=1}^N$, each demonstration implicitly defines a goal: the final state $\mathbf{s}_T^{(i)}$. We train:

$$\max_\theta \sum_{i=1}^N \sum_{t=1}^{T-1} \log \pi_\theta(\mathbf{a}_t^{(i)} | \mathbf{s}_t^{(i)}, \mathbf{g} = \mathbf{s}_T^{(i)})$$

No additional labeling is required—the goal is simply each demonstration's terminal state.

#### Two Sources of Distributional Shift

Goal-conditioned BC faces distributional shift in **two** places:

1. **State shift**: States visited by $\pi_\theta$ differ from demonstration states (the usual problem)
2. **Goal shift**: At training time, goals are always states actually reached by demonstrators. At test time, we might specify goals no demonstration reached.

---


### 3.3 Learning from Unstructured Play Data

Lynch et al. (2020) introduce a powerful idea: what if we could learn goal-conditioned policies from "play data"—unstructured teleoperation where humans manipulate objects without any specific task instructions?

#### What is Play Data and Why Use It?

Traditional imitation learning requires carefully staged demonstrations: reset the scene, perform the task, record, repeat. This is expensive and produces narrow data—demonstrations of drawer-opening show exactly how to open the drawer from exactly the starting pose the demonstrator used.

Play data is different. A human teleoperator simply *plays* with objects in the environment—opening drawers, pushing buttons, picking things up, setting them down—driven by curiosity rather than task completion. No scene resets, no task labels, no careful staging.

This approach offers three key advantages:

1. **It is cheap**: Hours of play can be collected continuously without resetting
2. **It is broad**: Play naturally covers diverse states and transitions—the operator gets bored doing the same thing and explores
3. **It contains recovery behaviors**: When playing, humans make mistakes and recover—exactly the transitions missing from expert demonstrations

But play data presents a challenge that structured demonstrations do not: **extreme multimodality**.

#### The Multimodality Problem in Play Data

When playing, humans don't optimize for efficiency. Asked to open a drawer, an operator might grasp the handle from the top, from the bottom, pull quickly, pull slowly, or use different finger positions. The same (current state, goal state) pair maps to many different action sequences.

If we naively train a goal-conditioned policy $\pi_\theta(\mathbf{a} | \mathbf{s}, \mathbf{g})$ on play data, we face the multimodality problem from Section 1.2—but worse. The policy sees conflicting supervision: same inputs, different outputs. A unimodal network learns the average, which may not correspond to any valid strategy.

```
       THE MULTIMODALITY PROBLEM IN PLAY DATA
       
       Same start state s, same goal g (drawer open):
       
       Demo 1: grasp top    ━━●━━━━●━━━━●━━━━●━━▶ goal
       Demo 2: grasp bottom ━━○━━━━○━━━━○━━━━○━━▶ goal  
       Demo 3: grasp middle ━━△━━━━△━━━━△━━━━△━━▶ goal
       
       All three reach the same goal via different strategies.
       Training without disambiguation → policy averages 
       the actions → potentially nonsensical behavior.
```

#### Latent Plans: Disambiguating Strategies

The key insight of Play-LMP (Play-supervised Latent Motor Plans) is to introduce a **latent plan variable** $z$ that captures *which strategy* the agent is executing. Think of $z$ as answering the question: "Given many ways to reach this goal, which approach am I taking right now?"

Once the policy knows the strategy (via $z$), predicting actions becomes much easier—it's no longer averaging over all possible approaches, just following one specific plan.

```
       LATENT PLAN AS STRATEGY SELECTOR
       
       Without latent plan:
         (state, goal) ──► π ──► ??? (which strategy?)
       
       With latent plan:
         (state, goal, z) ──► π ──► actions for strategy z
         
       z ≈ "grasp from top, pull slowly"
       z' ≈ "grasp from bottom, pull quickly"
       
       Different z values → different valid behaviors
       Policy only needs to decode one plan at a time
```

#### The VAE-Style Architecture

Play-LMP uses a variational autoencoder-inspired architecture with three components:

**Plan Recognition (Φ)** is a sequence encoder that sees the *entire trajectory*—all states and actions. Since it has full information about what actually happened, it can identify precisely which strategy was used. It outputs a distribution $q_\Phi(z | \tau)$ over latent plans. This component is used only during training.

**Plan Proposal (Ψ)** sees only the *initial state* and *goal state*—no actions, no intermediate states. It must learn to propose which plans might work to connect these states, outputting $p_\Psi(z | s_i, s_g)$. This is what we use at test time, when we don't yet have a trajectory.

**Action Decoder (π)** takes the current state, goal, and a sampled latent plan $z$, and outputs actions. Because $z$ disambiguates the strategy, this becomes a much simpler unimodal prediction problem.

```
       PLAY-LMP ARCHITECTURE
       
       ┌─────────────────────────────────────────────────────┐
       │  TRAINING                                           │
       │                                                     │
       │    Full trajectory τ                                │
       │    (s₁,a₁,s₂,a₂,...,sₜ)                             │
       │            │                                        │
       │            ▼                                        │
       │    ┌──────────────────┐                             │
       │    │ Plan Recognition │    "what strategy was       │
       │    │       Φ          │     actually used?"         │
       │    └────────┬─────────┘                             │
       │             │ q_Φ(z|τ)                              │
       │             ▼                                       │
       │         sample z ──────────────────┐                │
       │             ▲                      │                │
       │             │ KL divergence loss   │                │
       │             │ (make these match)   ▼                │
       │    ┌────────┴─────────┐    ┌──────────────┐         │
       │    │  Plan Proposal   │    │Action Decoder│         │
       │    │       Ψ          │    │      π       │         │
       │    └────────┬─────────┘    └──────┬───────┘         │
       │             │                     │                 │
       │             │ p_Ψ(z|sᵢ,sₘ)        │ reconstruction  │
       │             │                     │ loss            │
       │    (start state, goal state)     actions            │
       │                                                     │
       └─────────────────────────────────────────────────────┘
       
       ┌─────────────────────────────────────────────────────┐
       │  INFERENCE (test time)                              │
       │                                                     │
       │    (current state, goal) ──► Plan Proposal Ψ        │
       │                                    │                │
       │                              sample z               │
       │                                    │                │
       │    (current state, goal, z) ──► Action Decoder π    │
       │                                    │                │
       │                                 actions             │
       │                                                     │
       │    Plan Recognition Φ is discarded at test time     │
       │                                                     │
       └─────────────────────────────────────────────────────┘
```

#### Why KL Divergence Training Works

The training objective has two parts:

1. **Reconstruction loss**: Given $z$ sampled from Plan Recognition, the decoder must reproduce the actual actions. This ensures $z$ contains useful information about the strategy.

2. **KL divergence**: $D_{KL}(q_\Phi(z|\tau) \| p_\Psi(z|s_i, s_g))$ forces Plan Proposal to match Plan Recognition. Since Plan Recognition sees everything and Plan Proposal sees only endpoints, this teaches Plan Proposal to predict which plans are plausible given only start and goal.

The key insight: Plan Recognition has "privileged information" (the full trajectory) and can perfectly identify the strategy. Plan Proposal must learn to predict the same distribution without that information. By minimizing KL divergence, we transfer the knowledge from the privileged encoder to the one we'll actually use at test time.

#### Why This Addresses Distributional Shift

Play-LMP helps with distributional shift in two ways:

1. **Broad data coverage**: Play data naturally includes many states, transitions, and recovery behaviors that expert demonstrations miss.

2. **Robust strategies**: The latent plan provides a form of commitment—once $z$ is sampled, the policy follows that strategy consistently rather than oscillating between modes. The plan is re-sampled periodically (every $\kappa$ timesteps), allowing adaptation while maintaining coherent behavior within each planning horizon.

Empirically, Lynch et al. found that play-supervised models significantly outperform models trained on task-specific demonstrations, particularly in robustness to perturbations and ability to retry after initial failures.

---
### 3.4 Beyond Imitation: Iterated Self-Improvement

Ghosh et al. (2021) push further: can we learn goal-conditioned policies **without any demonstrations**?

**Algorithm: Iterated Supervised Learning for Goal-Reaching**
```
1. Start with a random policy π_θ
2. Collect trajectories by sampling random goals and executing π_θ
3. For each trajectory, relabel the goal as the state actually reached
4. Train via goal-conditioned BC on relabeled data
5. Repeat from step 2
```

```
       ITERATED GOAL RELABELING
       
       Iteration 1:
       ┌──────────────────────────────────────┐
       │  Command: reach ★                    │
       │  Actual:  ●━━━━●━━●━━○               │
       │                      └─ reached here │
       │                                      │
       │  Relabel: "demo for reaching ○"      │
       └──────────────────────────────────────┘
       
       Iteration 2 (improved policy):
       ┌──────────────────────────────────────┐
       │  Command: reach ★                    │
       │  Actual:  ●━━━━●━━●━━●━━△            │
       │                         └─ closer!   │
       │                                      │
       │  Relabel: "demo for reaching △"      │
       └──────────────────────────────────────┘
       
       Eventually: policy reaches commanded goals
```

**Why does this work?** Initially, the policy reaches random states. But by relabeling, we always have "successful" demonstrations for *some* goal. As the policy improves, it reaches more distant goals, and relabeled training data includes these harder examples. The policy bootstraps from easy (close) goals to hard (far) goals.

This is closely related to **Hindsight Experience Replay** (HER) in reinforcement learning, which applies the same goal-relabeling idea to Q-learning. In sparse-reward settings (reward = 1 if goal reached, 0 otherwise), most trajectories receive zero reward, making learning extremely slow. HER's insight: even a "failed" trajectory successfully reached *some* state. By relabeling the goal to match the state actually reached, every trajectory becomes a "success" that provides positive reward signal. The Q-function learns from these relabeled transitions, eventually generalizing to reach commanded goals.

```
       HINDSIGHT EXPERIENCE REPLAY
       
       Original experience:
         Goal: reach ★
         Trajectory: s₀ → s₁ → s₂ → s₃ (didn't reach ★)
         Reward: 0, 0, 0, 0  ← No learning signal!
       
       Relabeled experience:
         Goal: reach s₃ (the state actually reached)
         Trajectory: s₀ → s₁ → s₂ → s₃ 
         Reward: 0, 0, 0, 1  ← Learning signal!
       
       Q-function learns: "from s₂, action a leads to s₃"
       This knowledge transfers to reaching other goals
```

---

### 3.5 Goal-Conditioned Learning at Scale

Shah et al. (2022) demonstrate goal-conditioned BC at scale for navigation with their **General Navigation Model (GNM)**:

- **Data**: 60 hours aggregated from 8 different robot platforms (TurtleBot, Jackal, Spot, Warthog, ATV) in diverse environments
- **Architecture**: CNN encoder processes current observation and goal image with embodiment context
- **Key result**: Zero-shot transfer to new robots not seen during training

```
       GNM: MULTI-ROBOT GOAL-CONDITIONED NAVIGATION
       
       ┌────────────────────────────────────────────────────┐
       │                                                    │
       │   Embodiment Context c_t                           │
       │          │                                         │
       │          ▼                                         │
       │   ┌──────────────┐                                 │
       │   │ Current obs  │──► CNN ──┐                      │
       │   │     o_t      │          │                      │
       │   └──────────────┘          │    ┌────────────┐    │
       │                             ├───►│ FC Layers  │──► │
       │   ┌──────────────┐          │    │            │    │
       │   │  Goal image  │──► CNN ──┘    │  Shared    │    │
       │   │     o_G      │               │ Abstraction│    │
       │   └──────────────┘               └────────────┘    │
       │                                        │           │
       │                                        ▼           │
       │                               Waypoints + Distance │
       │                                                    │
       │   Training: 8 robot platforms, 60 hours            │
       │   Result: Zero-shot transfer to new robots         │
       │                                                    │
       └────────────────────────────────────────────────────┘
```

Despite different dynamics (differential drive vs. Ackermann steering), camera positions, and speeds, the shared visual representation enables generalization.

#### Why Does Cross-Embodiment Transfer Work?

The key insight is a separation of concerns in the learned representation:

**Visual features are embodiment-agnostic**: "What does the goal look like?" and "What obstacles are ahead?" don't depend on whether the robot has wheels or legs. The CNN encoder learns to extract these universal visual features from diverse training data.

**Embodiment context handles dynamics**: The context vector $c_t$ encodes robot-specific information (maximum speed, turning radius, camera height). The policy learns to interpret visual features *relative to* the embodiment context.

```
       WHY CROSS-EMBODIMENT TRANSFER WORKS
       
       ┌─────────────────────────────────────────────────────┐
       │                                                     │
       │   Visual Encoder (shared across all robots):        │
       │   "I see a hallway with the goal 10 meters ahead"   │
       │                                                     │
       │   Embodiment Context (robot-specific):              │
       │   "I'm a fast outdoor robot" vs "I'm a slow indoor  │
       │    robot with a wide turning radius"                │
       │                                                     │
       │   Policy combines both:                             │
       │   Same visual scene + different context =           │
       │   different waypoints (faster robot plans further)  │
       │                                                     │
       └─────────────────────────────────────────────────────┘
```

A new robot (not seen during training) can still use the learned visual features—it just needs an appropriate embodiment context vector. The policy has learned the abstract mapping from (visual scene, robot capabilities) to navigation behavior.

---

## Conclusion: Recurring Themes

Three fundamental themes weave through this chapter:

**Distributional shift** is the central challenge. Every technique we discussed can be understood as reducing the gap between the policy's induced state distribution $p_{\pi_\theta}(\mathbf{s})$ and the training distribution $p_{\text{train}}(\mathbf{s})$:
- Sequence models handle history-dependent behavior
- Expressive distributions capture multimodality
- Data augmentation covers recovery states
- Pre-training provides broad state coverage
- Multi-task learning forces generalization

**Expressiveness vs. tractability** presents a constant tradeoff. We want policies that represent complex distributions (non-Markovian, multimodal) but that we can train and sample from efficiently. Autoregressive discretization, flow matching, and VAEs occupy different points in this space.

**Broad + narrow data** is the dominant paradigm. Broad data provides robustness and diverse representations; narrow data provides task-specific intent. This appears in data collection strategies (mistakes + corrections, side cameras) and in explicit two-stage training (pre-training on 10,000 hours, post-training on 20 hours).

The field continues to evolve rapidly, but these principles—addressing distributional shift through better models, smarter data, and multi-task learning—remain the foundation upon which modern imitation learning systems are built.

---

## Summary

| Challenge | Solution | Key Technique |
|-----------|----------|---------------|
| Non-Markovian behavior | Sequence models | Transformer over frame embeddings |
| Multimodal behavior | Expressive distributions | Flow matching, autoregressive |
| Distributional shift (states) | Data augmentation | Mistakes + corrections, side cameras |
| Limited coverage | Pre-training | Broad data → narrow fine-tuning |
| Single-task brittleness | Multi-task learning | Goal-conditioned policies |

The path forward combines all these elements: expressive architectures that handle history and multimodality, trained first on broad diverse data and then fine-tuned on task-specific demonstrations, with goal-conditioning to maximize robustness across the state space.
