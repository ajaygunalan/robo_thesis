---
tags: controls
---

### Filter Models & Definitions

The fundamental distinction between filter types is the presence of feedback in the difference equation.

#### Finite Impulse Response (FIR)

The output is a function of a finite number of past and present input samples only. It is non-recursive.

$y[n] = \sum_{k=0}^{N-1} b_k x[n-k]$ 

#### Infinite Impulse Response (IIR)

The output is a function of both input samples and previous output samples. It is recursive.

$y[n] = \sum_{k=0}^{M} b_k x[n-k] - \sum_{k=1}^{N} a_k y[n-k]$ 

The standard first-order low-pass filter, $y[n] = \alpha x[n] + (1-\alpha) y[n-1]$, is a canonical IIR filter.

---

### Analysis in a Robotics Context

#### Phase Delay ($\tau_p$) and Group Delay ($\tau_g$)

- Phase Delay ($\tau_p$): The time lag experienced by a single, steady-state sinusoidal frequency. Imagine a persistent 60 Hz motor vibration appearing in the force readings; phase delay is the specific time shift that the filter applies _only to that 60 Hz signal component_.
    
- Group Delay ($\tau_g$): The time lag of a complex signal's overall envelope, representing the delay of a transient event. If the robot makes contact at t=0, group delay measures the time it takes for the _peak_ of that impact force to appear in the filtered signal. This is the more physically intuitive measure of control lag.
    

For nearly all robotic F/T applications, both delays are negligible compared to the system's mechanical response and control cycle time. A distinction becomes critical only when designing responses to events that occur _within_ a single control cycle, such as sub-millisecond impact analysis or high-bandwidth haptic feedback.

---

### The Deeper Insight

The choice between FIR and IIR filters in robotics is not a balanced trade-off; it is a settled engineering decision based on application constraints. The theoretical benefits of a FIR filter (e.g., guaranteed stability, linear phase) are outweighed by the computational efficiency and "good enough" performance of a simple IIR filter for real-time control.

The industry standard is to use a first-order IIR filter for online noise suppression. FIR filters are reserved for offline analysis or specialized research where precise waveform preservation is a primary scientific requirement, not a control objective. For a practicing roboticist, the IIR filter is the correct and sufficient tool for the task.