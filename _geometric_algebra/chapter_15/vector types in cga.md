# vector types in cga

## The problem: "vector" means five different things

Classical Euclidean geometry and physics reuse the same Euclidean vector symbol $u$ for roles that have *different allowed motions*: a free direction, a plane normal, a force sliding along its line, a tangent attached to a point, and a "position vector" pretending to be a point. If you implement these naively in coordinates, you end up enforcing transformation rules by convention or by a zoo of separate data types.

The conformal model instead encodes each role as a distinct multivector element so that **the same Euclidean rotors/translators automatically give the correct transformation behavior** (Figure 15.11, page 16).

## Free vector (direction without location)

A free direction is represented as
$$u \wedge \infty.$$
It rotates as $u$ rotates, but translating it does nothing: it is translation-invariant. This is also the natural parameter for the translation rotor $\exp(-\tfrac12 u\wedge \infty)$.

## Normal vector (plane normal that can slide in its plane)

A plane normal through the origin is just the Euclidean vector $u$. Under a translation by $p$ it becomes
$$T_p[u] = u + (p\cdot u)\infty,$$
which has two key geometric meanings:

1. Translations perpendicular to $u$ leave it unchanged (so you may "draw it anywhere on its plane" without changing the computational object).
2. The translated form represents the plane with normal direction $u$ passing through $p$, with only the component $p\cdot u$ affecting its offset (correctly reflecting that a plane has one scalar degree of freedom for location along its normal).

## Line vector (force-like vector that slides along a line)

A line-direction concept that is free to slide along its carrier is represented as
$$o \wedge u \wedge \infty.$$
Under translation,
$$T_p[o \wedge u \wedge \infty] = p \wedge u \wedge \infty = o \wedge u \wedge \infty + (p\wedge u)\wedge \infty.$$
This shows invariance precisely when $p\wedge u=0$, i.e., translation along the line direction. The "extra" term encodes the line's moment-like location information orthogonal to $u$.

## Tangent vector (direction attached to a point)

A tangent vector at the origin is
$$o \wedge u.$$
Translating it carries both the point and the direction along; it is not translation-invariant because it is *attached*.

This matches how velocity vectors, surface tangents, and other "at-a-point" vectors behave in geometry and physics.

## Position vector vs point

The chapter is blunt about the usual abuse: using a Euclidean vector to denote a point is only possible after silently choosing an origin. CGA makes that explicit: points are represented by conformal null vectors; a Euclidean vector becomes a "position vector" only as a parameter that translates a chosen origin point. Concretely, translating the origin point $o$ by Euclidean displacement $u$ produces the point
$$u = e^{-u\infty/2} \, o \, e^{u\infty/2}.$$
Changing the reference origin changes the Euclidean vector parameter needed to reach the same point, which is exactly why "position vectors" are convention-heavy and bug-prone.

## Why this matters in code

By representing these concepts as distinct CGA elements, you can apply a single rotor/translator implementation and get the correct behavior "for free," instead of encoding it in custom classes and ad-hoc transformation logic. The chapter also notes the overhead can be kept modest in a good implementation (on the order of tens of percent), especially with code generation for specialized routines.
