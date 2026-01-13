---
title: "Chapter 4 — Linear Transformations of Subspaces"
tags: [geometric-algebra, linear-transformations, blades, outermorphism]
chapter: 4
---
# Linear transformations of subspaces

Linear maps are taught as "things that move vectors around." Geometry, however, lives in subspaces—lines, planes, volumes—and in GA those are blades. The goal of this chapter is to stop decomposing subspaces into vectors just to transform them: extend a linear map so it acts on blades *directly*, preserving the algebraic structure we've built.

The foundation rests on the [[Defining Properties|defining properties]] of linear maps: scaling and addition preservation. A blade is a *span-with-orientation*—if $A = a_1 \wedge \ldots \wedge a_k$, then transforming the subspace should mean "transform the generators, then re-span." That single demand becomes the **outermorphism** rule: $f(A \wedge B) = f(A) \wedge f(B)$. The [[Outermorphisms|outermorphism extension]] shows this is well-defined—different factorizations of the same blade yield the same transformed blade—and that scalars pass through untouched while sums remain sums. Every linear map on vectors lifts uniquely to the full exterior algebra.

Once $\wedge$ is handled, you peel into the metric. Top-grade blades track signed hypervolume, so asking "how does $f$ scale the unit pseudoscalar?" forces the answer $f(I_n) = \det(f)\, I_n$, and the [[Determinant|determinant]] emerges not as a computational recipe but as the geometric fact that *linear maps scale volumes by a single signed factor*. Orientation-reversing maps flip the sign; singular maps collapse dimension and annihilate the pseudoscalar entirely.

Contractions and duals depend on the inner product, so you need the **adjoint**—the unique map $f^\dagger$ satisfying $\langle f(a), b \rangle = \langle a, f^\dagger(b) \rangle$. The [[Metric Products|metric products]] section derives how $f$ interacts with $\lrcorner$: in general, contracting then transforming differs from transforming then contracting, but for **orthogonal maps** the two commute. This is the structural divide: $\wedge$-structure survives any linear map, while $\lrcorner$-structure survives exactly the orthogonal ones.

Those laws pay off immediately. The [[Inverses|inverse]] of a nonsingular linear map acquires a compact, coordinate-free formula built from the adjoint and determinant—no row-reduction required. When you do need coordinates, the [[Matrix Representations|matrix representations]] section shows how to recover standard matrix mechanics as a basis-bound implementation layer, translating between the geometric picture and the computational one without privileging either.

The [[Examples|worked examples]]—scaling, projection, rotation, point reflection—make these abstractions concrete. Scaling reveals how eigenvalues distribute across grades; projection shows orthogonal decomposition at work; rotation exposes the **eigenblade**, an invariant plane that survives unchanged while everything else rotates around it; and point reflection demonstrates grade-dependent sign flips. Each example is a test case for the general machinery, turning abstract product laws into geometric intuition.

The chapter's punchline is a clean dichotomy: the outer product's "span" structure is algebraically robust, surviving every linear map intact, while the inner product's "angle" structure is fragile, preserved only by the special maps—orthogonal transformations—that respect lengths and perpendicularity. Understanding which structure you need tells you which maps you're allowed to use, and that awareness is the bridge between abstract algebra and geometric reasoning.
