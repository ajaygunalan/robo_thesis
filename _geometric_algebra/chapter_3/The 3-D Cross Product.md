---
title: "The 3-D Cross Product"
tags: [geometric-algebra, cross-product, duality]
---

# The Cross Product: What It Really Is

## Classic uses in 3-D

- **Normal vectors:** $x \times y$ is perpendicular to the plane spanned by $x, y$.
- **Rotational velocities:** velocity of a point $x$ rotating about axis $a$ uses $a \times x$.
- **Intersecting planes:** normals $a, b$ of planes give an intersection direction $a \times b$.

The catch: these tricks don't generalize cleanly beyond 3-D, and even in 3-D the "normal vector" doesn't transform like the plane it represents under general linear maps (hence special-case code in graphics pipelines).

## The honest definition: cross product = dual of a bivector

Let $I_3$ be the 3-D pseudoscalar. Then

$$ a \times b = (a \wedge b)^* = (a \wedge b) \lrcorner I_3^{-1} $$

This makes the dependency explicit:

1. $a \wedge b$ spans the plane (metric-free),
2. dualization uses the metric to pick the orthogonal complement.

That's exactly why $\times$ is "more complicated than it looks."

## Replacing each use with a blade-native operation

- **Normals:** don't turn a plane into a vector; keep it as the bivector $a \wedge b$. The plane _is_ the object.
    
- **Velocities:** rewrite $$ a \times x = (a \wedge x)^* = x \lrcorner A $$ where $A = a^*$ is the rotation plane. Now rotation is natively "in a plane," which generalizes to higher dimensions.
    
- **Intersections:** the same algebra that turns wedge into meet (later chapters) handles plane/line/hyperplane intersections uniformly; the cross product case is just the 3-D shadow of that.
    

So the recommendation is blunt: when you _mean_ a plane, use a bivector; when you _mean_ an orthogonal complement, dualize explicitly; don't carry around a special operator whose whole job is to hide those steps.