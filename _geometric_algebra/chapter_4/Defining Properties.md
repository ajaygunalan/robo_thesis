---
title: "Defining Properties"
tags: [linear-map, intuition]
---

A "linear transformation" is the class of maps that are rigid about one thing: origin-anchored structure. If you scale a vector or add two vectors via the parallelogram rule, the map respects that construction.

Start with the why: in geometry you often want predictable behavior under "change of coordinates" or "change of viewpoint". A map that breaks addition or scaling destroys proportionality, parallelism through the origin, and the ability to build bigger objects from smaller ones. So we demand:

- $f(\alpha x) = \alpha f(x)$
- $f(x + y) = f(x) + f(y)$

Together:
$$f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$$

Geometric meaning (Figure 4.1):
- Scaling: points along a line through the origin stay on a line through the origin; ratios along that line are preserved.
- Addition: the image of a parallelogram is the parallelogram of the images.

That's why rotations about the origin, reflections through origin-containing subspaces, and scalings qualify; translations don't—they shift the origin and generally turn linear (homogeneous) subspaces into offset (affine) ones.

This chapter intentionally stays within one space $\mathbb{R}^n \to \mathbb{R}^n$.
