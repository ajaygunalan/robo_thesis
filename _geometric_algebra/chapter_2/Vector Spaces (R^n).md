---
title: "Vector Spaces (R^n)"
tags: [linear-algebra, metric-free]
---

Start with a real vector space $\mathbb{R}^n$: vectors, addition, scalar multiplication. Standard axioms are fine, but they keep scalars and vectors in separate worlds.

This chapter's goal is to compute with homogeneous subspaces (through the origin). Describing a plane by equations or parameters works, but it leaves you without a single element you can add/scale/combine the way you do with vectors. The missing bridge is the outer product.

## Homogeneous subspaces as primitives
A line through the origin is the set $\{\lambda a\}$; a plane is $\{\lambda a + \mu b\}$; and so on. The chapter treats these not as sets but as algebraic elements with attitude, orientation, and weight.

## Scalars re-enter as geometry
To keep the pattern unbroken, the 0D homogeneous subspace (the origin) is represented by a scalar: a 0-blade. Then scalar multiplication becomes the same spanning product in disguise:

- $\alpha \wedge x = x \wedge \alpha = \alpha x$.

With that, "scalars vs vectors" looks less like a metaphysical divide and more like "different grades of subspace elements".

## Why banning the metric is clarifying
Without a metric you can't use perpendicularity, so "plane = normal vector" is off the table. Representation must come from spanning, not from measurement. That forces the algebra to be about incidence and independence first—exactly what $\wedge$ encodes.
