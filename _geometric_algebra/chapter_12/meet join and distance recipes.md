## The "Plücker table" is just wedge + meet in disguise

Traditional references present line/plane/point interactions as a bag of formulas with bracket-notation types. Chapter 12's main practical point is: once points, lines, and planes are embedded as blades, every entry in those tables is a standard operation—usually a wedge (join/span) or a meet (intersection via duality). You can derive what you need instead of hoping the right row exists.

Below are the core recipes the chapter highlights (Table 12.1, printed p.330, plus a few "beyond the table" cases).

## Point–plane: a meet that returns a scalar distance

For a plane with normal $n$ and offset $\delta$, and a point at $p$, the meet gives
$$
\Pi \cap P = n\cdot p - \delta.
$$
This is the oriented distance (up to the normalization of $n$). The important conceptual upgrade is that a scalar (a grade-0 blade) isn't "nothing"—it can be a meaningful geometric coincidence measure.

## Line–origin: distance and closest point from the moment

For a line in Plücker form $\{a,m\}$:

* squared distance to the origin:
  $$
  d^2 = \frac{m\cdot m}{a\cdot a},
  $$
* closest point on the line to the origin (as homogeneous point coordinates):
  $$
  P_{\min} = (m \times a : a\cdot a).
  $$
  These drop out cleanly because $m$ is exactly the "lever arm" information of the line relative to the origin.

## Spanning: wedge builds the "obvious" higher object

A plane through a line $\{a,m\}$ and a point $p$ has homogeneous plane coordinates
$$
[a \times p - m : m \cdot p].
$$
This is what you get by wedging the point with the line and then reading off the plane's normal/offset components; it's the same construction as "two points span a line," just one grade up.

Similarly, augmenting a line by an additional direction $n$ yields a plane
$$
[a \times n : n \cdot m],
$$
which the chapter turns into an exercise precisely because it's a straight wedge expansion once you treat everything as blades.

## Line–plane: meet gives the intersection point (when not parallel)

Intersect a line $\{a,m\}$ with a plane $[n:-\delta]$ in general position. The meet produces a homogeneous point:
$$
P = (m \times n + \delta a : a \cdot n).
$$
Interpreting $(v : s)$ as a homogeneous point at Euclidean location $v/s$, the intersection location is
$$
p = \frac{m \times n + \delta a}{a\cdot n}.
$$

## Two lines: meet distinguishes skew from intersecting

For two **skew** lines $L_1=\{a_1,m_1\}$ and $L_2=\{a_2,m_2\}$, the meet returns a scalar that encodes their signed separation:
$$
L_1 \cap L_2 = -\,m_1\cdot a_2 - m_2\cdot a_1.
$$
This compact form is easiest if you use the dual-line representation for one of the lines (the algebra kills the "wrong-grade" terms automatically).

If two nonparallel lines intersect, the meet is no longer a scalar—it becomes a point. The chapter gives an explicit Plücker-form expression for the intersection point (not typically listed in tables), illustrating the bigger theme: once you keep the algebraic structure, you can push past the canned formulas when your application needs it.
