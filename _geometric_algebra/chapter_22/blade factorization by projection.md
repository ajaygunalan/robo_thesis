# Blade Factorization by Projection

Blade factorization is the problem: given a nonzero $k$-blade $B$, find $k$ vectors $b_1,\dots,b_k$ such that
$$
B = b_1\wedge b_2\wedge\cdots\wedge b_k.
$$

This matters whenever downstream code wants *vectors* (linear algebra, graphics pipelines, numerical routines) rather than a compressed blade coordinate representation. It also underpins meet/join algorithms that operate on factors.

A clean approach is iterative "peel-off" using projection onto the blade.

## The Basic Peel-Off Identity

Pick a candidate vector $c$ and project it into the subspace represented by $B$ using contraction (write $\lrcorner$ for left contraction):
$$
f = (c\lrcorner B)\,B^{-1}.
$$

* If $f=0$ (or numerically tiny), $c$ didn't have a useful component in the blade; try another $c$.
* If $f\neq 0$, then $f$ is a **vector factor** of $B$.

Once $f$ is found, you remove it by dividing it out with contraction:
$$
B_f = f^{-1}\lrcorner B. \tag{21.2}
$$

Then structurally,
$$
B = f\wedge B_f,
$$
so you've extracted one factor and reduced the blade grade by one. Repeat until the remainder is a vector.

## Why Candidate Choice Dominates Performance

In high dimensions, random or basis candidates can waste cycles because many project to zero. The stable shortcut is: use $B$'s own coordinate structure to choose candidates that *must* project nontrivially.

Let $E=e_{i_1}\wedge\cdots\wedge e_{i_k}$ be the **basis blade with the largest-magnitude coefficient** in $B$'s expansion. Use the $k$ basis vectors spanning $E$ as candidates. This choice guarantees (in exact arithmetic) that each projection step produces a nonzero factor.

## Practical Algorithm (Orthonormal Factors + Separate Scale)

The factorization procedure is run using a **Euclidean metric** for its internal products to avoid null-vector pathologies (null blades in the target metric are non-null in Euclidean metric, so the algorithm remains well-defined).

1. Input: nonzero blade $B$ of grade $k$.
2. Compute its norm (scale): $s = |B|$.
3. Find the basis blade $E$ with largest coordinate in $B$; extract its spanning basis vectors $\{e_i\}$.
4. Normalize the working blade: $B_c \leftarrow B/s$.
5. For $k-1$ of the basis vectors $e_i$ from $E$:

   * Project: $f_i = (e_i\lrcorner B_c)\,B_c^{-1}$.
   * Normalize $f_i$ and store it.
   * Update: $B_c \leftarrow f_i^{-1}\lrcorner B_c$.
6. The last factor is the remaining vector: $f_k = B_c$. Normalize it.
7. Output: unit vector factors $\{f_i\}$ and the scalar scale $s$.

This returns orthonormal factors **in the Euclidean metric used internally**. If you need orthonormality in another metric, form the metric matrix of the factors, perform an eigenvalue decomposition, and transform the factor set accordingly.

## Why the Projections Don't Vanish (Key Insight, Compressed)

The guarantee rests on the existence of a rotor that takes the "dominant" basis blade $E$ to the blade $B$ without passing through a 90° degeneracy (which would force $E\lrcorner B=0$ and contradict $E$ being dominant). From this, one shows that
$$
(e_i\lrcorner B)\,B^{-1}\neq 0
$$
for each $e_i$ in the spanning set of $E$, and the same argument applies after each peel-off step.
