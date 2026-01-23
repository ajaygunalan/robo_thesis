# Meet and Join via Delta Product

Meet and join are the blade analogs of intersection and union: they operate on the subspaces *spanned by blade factors* rather than on raw coefficients. The computational problem is that you want $A\cap B$ and $A\cup B$ without explicitly enumerating bases or doing expensive subspace computations outside GA.

The chapter's algorithm gets there by combining three ideas:

1. a blade "symmetric difference" built from the geometric product,
2. grade bookkeeping to know what you're aiming for, and
3. an incremental construction that terminates as soon as either the meet or the join reaches the required grade.

## Delta Product: A Blade-Level Symmetric Difference

For blades $A$ and $B$, look at the geometric product $AB$. Its **highest nonzero grade part** behaves like a spatial XOR: it keeps the factors that are present in either argument but not in both.

Define the **delta product**:
$$
A\Delta B \equiv \langle AB\rangle_{\max},
$$
where $\max$ is the largest grade for which that grade component is nonzero.

In implementation you often need a threshold $\varepsilon$ when deciding which is the top nonzero grade, to suppress floating-point noise.

## Grade Relations That Mimic Set Identities

By analogy with size formulas for union/intersection of sets, blade grades satisfy:
$$
\operatorname{gr}(A\cup B)=\operatorname{gr}(A)+\operatorname{gr}(B)+\frac{\operatorname{gr}(A\Delta B)}{2}, \tag{21.5}
$$
$$
\operatorname{gr}(A\cap B)=\operatorname{gr}(A)+\operatorname{gr}(B)-\frac{\operatorname{gr}(A\Delta B)}{2}. \tag{21.6}
$$

These tell you the **target grades** of meet and join before you compute them.

## Converting Meet ↔ Join Once One Is Known

Two identities tie the operations together:
$$
A\cup B = A\wedge\big((A\cap B)^{-1}\lrcorner B\big), \tag{21.7}
$$
$$
A\cap B = \big(B\lrcorner (A\cup B)^{-1}\big)\lrcorner A. \tag{21.8}
$$

So the algorithm can search for either one and derive the other immediately.

## The Algorithm (Computes Both, Stops Early)

Let $I_n$ be the pseudoscalar of the full space, and let $X^*$ denote duality. The algorithm starts by factoring the dual of the delta product:
$$
S = (A\Delta B)^*,
$$
and writing $S$ as a product of vector factors $s_i$ (using any blade-factorization routine).

Then:

1. Input: blades $A,B$ (optionally with threshold $\varepsilon$ for delta product detection).
2. If $\operatorname{gr}(A)>\operatorname{gr}(B)$, swap them (track sign conventions if you care about oriented results).
3. Compute $S=(A\Delta B)^*$.
4. Factorize $S$ into vectors $\{s_i\}$.
5. Compute target grades using (21.5)–(21.6).
6. Initialize:

   * meet accumulator $M\leftarrow 1$,
   * join accumulator $J\leftarrow I_n$.
7. For each factor $s_i$:

   * Compute projection and rejection of $s_i$ relative to $A$:
     $$
     p_i = (s_i\lrcorner A)\lrcorner A^{-1},\qquad r_i=s_i-p_i.
     $$
   * If $p_i\neq 0$: grow the meet
     $$
     M\leftarrow M\wedge p_i.
     $$
     If $\operatorname{gr}(M)$ hits the target meet grade, compute the join via (21.7) and stop.
   * If $r_i\neq 0$: shrink the join by removing the "shouldn't belong" factor
     $$
     J\leftarrow r_i\lrcorner J.
     $$
     If $\operatorname{gr}(J)$ hits the target join grade, compute the meet via (21.8) and stop.
8. Output: $A\cap B$ and $A\cup B$.

A key practical point: even if you only *want* the meet or only the join, computing both this way can be faster because the loop terminates as soon as **either** target grade is reached, and the second result then falls out from the identities.

## Complexity Intuition

Worst case is $O(n)$ loop cycles in an $n$-dimensional space (you can construct cases where the algorithm must peel almost all factors). But for blades in general position, projection and rejection tend to be nonzero, and the number of cycles is closer to
$$
\min(\operatorname{gr}(\text{meet}),\operatorname{gr}(\text{join}))\le \frac{n}{2},
$$
with extra iterations sometimes required in practice if you enforce minimum magnitudes for numerical stability.
