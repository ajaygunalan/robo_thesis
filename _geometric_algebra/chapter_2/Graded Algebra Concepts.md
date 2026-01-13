---
title: "Graded Algebra Concepts"
tags: [k-vectors, multivectors, grassmann, reversion]
---

With blades you have a clean geometry. With addition, you get a bigger algebra. This section tells you what stays geometric.

## k-blades vs k-vectors
- k-blade: factorizable wedge $a_1 \wedge \ldots \wedge a_k$ (or $0$).
- k-vector: linear combination of basis k-blades.

Every blade is a k-vector, but for $n \geq 4$ many k-vectors are not blades, so they no longer represent a single subspace.

## Multivectors and the Grassmann algebra
Allow sums across grades and you get multivectors. With $\wedge$ extended by distributivity, this is the exterior (Grassmann) algebra. In $\mathbb{R}^n$ it has $2^n$ basis elements in total.

The grade selector $\langle A \rangle_k$ pulls out the grade-$k$ part; wedge products then assemble grade-by-grade.

## Two orientation bookkeepers
- Reversion: reverse factor order; on a k-blade it's a sign $(-1)^{k(k-1)/2}$.
- Grade involution: flip by parity; on a k-blade it's $(-1)^k$.

You don't use these for flair—you use them because order and parity control signs once expressions get long.
