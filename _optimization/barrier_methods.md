---
tags: optimization
---

$$\min \quad f(x) $$
$$\ \text{s.t.}  \quad h_j(x) \leq 0, \quad j = 1, \ldots, l $$


Let  $$X = {x : h_j(x) \leq 0, \quad j = 1, \ldots, l}$$

- Some Barrier functions (defined on the _interior_ of $X$)
$$B(x) = -\sum_{j=1}^{l} \frac{1}{h_j(x)} \quad \text{or} \quad B(x) = -\sum_{j=1}^{l} \log(-h_j(x))$$

- Approximate problem using Barrier function (for $c > 0$)
$$ \begin{align} \min & \quad f(x) + \frac{1}{c}B(x) \ \text{s.t.} & \quad x \in \text{Interior of } X \end{align} $$

Analysis is similar to [[penalty_method]]