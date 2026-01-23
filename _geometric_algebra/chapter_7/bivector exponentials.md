# Bivector Exponentials

Building rotors as products of vectors is constructive and geometric, but exponentials are what turn "rotation by angle in plane" into a single expression, and what keeps the story intact when the metric changes.

## Pure rotors as exponentials of 2-blades

In Euclidean signature, a unit plane bivector $I$ satisfies $I^2 = -1$. That makes the exponential of a bivector behave like a complex unit:

$$
e^{I\psi} = \cos\psi + I\sin\psi.
$$

So a rotation of angle $\phi$ in plane $I$ has rotor

$$
R = \cos(\phi/2) - I\sin(\phi/2) = e^{-I\phi/2}.
$$

The win here is not "prettier trig." Exponentials make algebraic manipulation track geometric commutation relations directly. If an element anticommutes with $I$, it slides through $e^{-I\phi/2}$ by flipping the sign in the exponent; if it commutes, it slides through unchanged. That is the same geometric information as "in the plane" vs "orthogonal to the plane," encoded as algebra.

## Metric-dependent behavior: trig, nilpotent, hyperbolic

The exponential definition by power series still works when the metric is not Euclidean. For a 2-blade $A$, the key fact is that $A^2$ is scalar (possibly negative, zero, or positive). That forces the exponential into one of three canonical families:

* If $A^2 = -\alpha^2$:
  $$
  e^{A} = \cos\alpha + \frac{A}{\alpha}\sin\alpha
  $$
  (elliptic, rotation-like).

* If $A^2 = 0$:
  $$
  e^{A} = 1 + A
  $$
  (parabolic, nilpotent; later this is how translations show up in conformal models).

* If $A^2 = +\alpha^2$:
  $$
  e^{A} = \cosh\alpha + \frac{A}{\alpha}\sinh\alpha
  $$
  (hyperbolic, boost/scale-like).

So "exponentials of bivectors" are not just for rotations; they are a uniform interface to continuous orthogonal motions across signatures.

## Are all rotors bivector exponentials? Almost—but with sharp boundaries

In Euclidean and Minkowski spaces, every orthogonal transformation continuously connected to the identity can be written in the form

$$
x \mapsto e^{-B/2} \, x \, e^{B/2}
$$

for some bivector $B$. Outside those signatures, the statement fails in general.

In the favorable cases (Euclidean and Minkowski), there's an additional structural bonus: any bivector can be decomposed into a sum of mutually commuting 2-blades (geometrically, orthogonal rotation/boost planes). When the parts commute, the exponential factorizes cleanly:

$$
e^{-(B_1 + \cdots + B_k)/2} = e^{-B_k/2} \cdots e^{-B_1/2}.
$$

This is the algebraic form of "a general rotor is built from independent planar motions."

The warning label is essential: in general, $e^{B} e^{A} \neq e^{A+B}$ unless $A$ and $B$ commute (up to a few accidental edge cases where one exponential collapses to a scalar). Noncommutativity is not a technical nuisance; it is exactly the geometric coupling between rotations in skew planes.

## Logarithms and interpolation

If $R = e^{-B/2}$, it's tempting to define $B = -2\log R$, then interpolate by roots:

$$
R^{1/N} = \exp(\log(R)/N).
$$

This works conceptually, but $\log$ is not unique (periodicity shifts by multiples of $4\pi$ in the pure rotation case), and closed forms exist mainly when the generating bivector is a single 2-blade (where inverse trig/hyperbolic functions apply). For general bivectors, extracting a geometrically meaningful logarithm amounts to factorizing into commuting planes first—often the hard part.
