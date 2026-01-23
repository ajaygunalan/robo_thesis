# Multivector Classification: Blade vs Versor

If your GA code accepts multivectors from computation (or users), you eventually need a sanity check: *is this thing actually a blade? a versor? or neither?* This is not a trivial "grade check," because additively represented multivectors can mimic superficial properties of blades/versors while failing the structural definition.

## Why Naive Tests Fail

Two common "obvious" tests are wrong:

1. **Uniform grade is not enough.**
   A grade-2 multivector like $e_1\wedge e_2 + e_3\wedge e_4$ has only bivector terms, but it's not a single 2-blade (it doesn't represent one 2D subspace factorization).

2. **"Square is scalar" is not enough.**
   Even a non-blade can square to a scalar; for example (in Euclidean metric) $e_1\wedge e_2\wedge e_3 + e_4\wedge e_5\wedge e_6$ squares to $-2$ without being a blade.

So you need tests that probe *how the multivector behaves under the operations that define blades and versors.*

## Metric Subtlety: Blade vs Versor Are Not the Same Kind of Question

* **Blade-ness** ("factorizable by outer products") is metric-independent.
* **Versor-ness** ("product of invertible vectors") depends on the metric because invertibility does.

A practical trick follows from this: when testing for blades, you can perform the geometric products in a **Euclidean metric** to avoid null factors complicating invertibility—without changing the underlying factorability question.

## Classification Algorithm (Structure-First)

Let $V$ be the multivector to classify. Let $\hat V$ denote **grade involution** (flip the sign of odd grades), and let $V^{-1}$ be the candidate inverse computed using the fast versor inverse construction.

### 1) First Gate: Does the "Versor Inverse" Behave Like a Real Inverse?

Compute the candidate inverse (via the versor inverse method), then validate it with two checks that explicitly use grade involution:

* Require that $V(\hat V)^{-1}$ is a scalar:
  $$
  \operatorname{grade}(V(\hat V)^{-1}) = 0.
  $$

* Require left/right consistency:
  $$
  V(\hat V)^{-1} = V^{-1}\hat V.
  $$

The grade involution here is not decoration: it blocks mixed-grade multivectors (odd+even parts) from "cheating" by cancellation. For a pure even versor, $\hat V=V$; for a pure odd versor, $\hat V=-V$. Mixed-grade objects don't reduce to a clean $\pm V$, so they tend to fail these constraints.

If either check fails, classify **nonversor**, hence also **nonblade** in this scheme.

### 2) Second Gate: Does It Preserve Vector Grade Under Versor Action?

A defining property of a versor is that it maps vectors to vectors under the sandwich action. For each basis vector $e_i$ of the underlying vector space, require:
$$
\operatorname{grade}(\hat V\,e_i\,V^{-1}) = 1.
$$

If this fails for any $e_i$, classify **nonversor**.

If it passes, $V$ is structurally consistent with a versor (and invertible blades are a subset of that).

### 3) Final Split: Blade or Versor?

Now the distinction is simple:

* If $V$ has **a single grade**, classify **blade**.
* Otherwise, classify **versor**.

## What Remains Unresolved in General

Even with classification, there is no general, metric-agnostic way here to "snap" a numerically drifted multivector back to the nearest true blade or versor optimally—especially in general metrics. That's an open practical issue for robust implementations.
