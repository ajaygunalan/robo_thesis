## Directions, not places

In an $n$-dimensional physical space, "direction" is the thing you can add and scale without ever talking about *where* it is. Put every direction at the origin and you get the mathematical vector space $\mathbb{R}^n$. Equip it with the metric of your physical space (typically Euclidean), and you can do geometry computationally inside the geometric algebra of that metric vector space.

This is why the vector space model is such a clean computational representation: it is *structurally* about directions at a single location. The moment you need actual translation structure, you're outside its natural jurisdiction.

## Higher-dimensional directions are blades

A single 1D direction is a vector. A $k$-dimensional directed subspace is represented by a $k$-blade: an outer product of $k$ independent vectors.

A critical detail: most $k$-blades are *not* closed under addition. The sum of two $k$-blades is generally a $k$-*vector* that may not be decomposable as one outer product. Only in grades $0,1,(n-1),n$ does arbitrary addition stay within the space of "pure" blades. So "a direction" is not the same thing as "a multivector with only grade $k$"; the latter can represent mixtures of $k$-directions.

## What a direction "has": attitude, weight, orientation

In this model, a directed object carries three separable aspects:

* **Attitude:** which subspace it points along (the geometric content).
* **Weight:** how much of it (length/area/volume magnitude of the blade).
* **Orientation:** the handedness/sign information.

These are not optional decorations; they matter whenever you compare, intersect, project, or transform directions.

## The basic directional operations

The vector space model gives a compact algebraic toolkit that directly corresponds to geometric manipulations of subspaces:

* **Composition:** outer products build higher-dimensional directions from 1D ones.
* **Angle/proximity between directions:** contraction captures relative angles even between objects of different grades.
* **Orthogonal complements:** duality represents a $k$-direction by the $(n-k)$-direction orthogonal to it.
* **Incidence:** meet and join define intersection/union of directions using wedge + duality (and are the directional analog of subspace intersection/span).
* **Projection:** orthogonal projection is naturally expressed via contraction.
* **Reflections:** sandwiching with a versor reflects directions (with care about orientation conventions).
* **Rotations:** rotors implement rotations cleanly, and even the geometric product of directions can *generate* the rotation operators you need.

The punchline is that these are structural facts about directions in $\mathbb{R}^n$. The rest of the chapter is about turning those facts into concrete computational techniques in $\mathbb{R}^2$ and $\mathbb{R}^3$.
