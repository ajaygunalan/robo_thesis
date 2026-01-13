---
title: "The Ladder of Blades"
tags: [grade, pseudoscalar, pascal]
---

$\wedge$ doesn't just create new objects; it stratifies them by grade.

## Rungs
- grade 0: scalars (0-blades)
- grade 1: vectors (1-blades)
- grade 2: bivectors / plane elements (2-blades)
- grade 3: trivectors / volume elements (3-blades)
- ...
- grade $n$: pseudoscalars (top-grade elements in $\mathbb{R}^n$)

The ladder rule is:
$$\text{grade}(A \wedge B) = \text{grade}(A) + \text{grade}(B)$$

## The ladder ends at the space dimension
In $\mathbb{R}^3$, any 4-fold wedge is $0$: you can't span more independent directions than the ambient space has. The single $0$ represents the "empty subspace", regardless of intended grade.

## Counting basis blades
At grade $k$, there are $C(n,k)$ basis $k$-blades (Pascal's triangle). The top grade $n$ has only one basis element up to scaling: the pseudoscalar $I_n$.

## The first surprise ($n \geq 4$)
The grade-$k$ vector space has dimension $C(n,k)$, but not every element is a blade. Not all k-vectors factor into a single wedge product of vectors.
