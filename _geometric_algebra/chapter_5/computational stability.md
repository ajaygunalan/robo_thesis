# computational stability

General meet/join computation is typically implemented as a factorization algorithm. That makes it much slower than ordinary exterior products, and it also introduces numerical sensitivity near degenerate configurations.

Two practical consequences:

- **Cost.** If you already know the ambient join subspace (so you know a join pseudoscalar), it is usually better to bypass general meet/join and compute the meet by the fixed-join contraction formula in [[meet from join]].
- **Grade flip-flop.** A factorization-based implementation must decide the output grade, commonly by comparing a condition-number-like quantity to a threshold. Near degeneracy (nearly parallel directions, near containment), tiny perturbations can push that test across the threshold, so the result can flip between output grades even while the geometry changes smoothly.

For example, probing when the join of two nearly parallel vectors changes from "vector" to "bivector" reveals a transition at internal epsilon scales (typically around $10^{-7}$). Use [[piecewise linearity and degeneracy]] for the geometric "wrong join" diagnostic, and design downstream code to handle regime switches explicitly.
