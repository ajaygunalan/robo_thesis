# Sandwich Reflections

A reflection is the primitive orthogonal operation, and geometric algebra expresses it in one move: turn a "mirror direction" into an operator via a sandwiching product. The point is not the particular mirror (line vs plane) but the *pattern*: reflect by conjugating with an invertible vector/blade, and let the inverse erase irrelevant scale.

## Line vs hyperplane: same sandwich, different sign

There are two closely related "reflections" that share the same algebraic shape but correspond to different geometric mirrors:

* **Reflection in a line through the origin** characterized by a vector $a$ uses
  $$
  x \mapsto a \, x \, a^{-1}.
  $$
  This keeps the component along the line and flips the orthogonal component. Because $a^{-1}$ cancels scalars, only the *attitude* of the line matters.

* **Reflection in a hyperplane** (the usual mirror reflection) with dual normal vector $a$ uses
  $$
  x \mapsto -a \, x \, a^{-1}.
  $$
  This flips the component normal to the plane and keeps the in-plane component.

These two differ only by a minus sign, but their determinants behave differently in $n$ dimensions. Hyperplane reflection always has determinant $-1$. The "line reflection" has determinant $(-1)^{n+1}$, which reveals a subtlety: in 3-D, a line "reflection" is actually a proper rotation (det $= +1$), not a reflection in the classical sense.

## Extending to blades: outermorphisms force the same sandwich

A reflection is linear on vectors, so it extends uniquely to blades by outermorphism. For the line version the extension is clean:

$$
X \mapsto a \, X \, a^{-1}.
$$

For the hyperplane mirror, the correct extension introduces a grade-dependent sign through the **grade involution** $\widehat{X}$ (which flips odd grades):

$$
X \mapsto a \, \widehat{X} \, a^{-1}.
$$

This is not decorative: it is what makes the mirror behave consistently across grades so that "reflect a plane" really produces the reflected plane with the right orientation bookkeeping.

## Reflection in an arbitrary subspace blade

Once you stop insisting the mirror must be a hyperplane, any invertible blade $A$ representing a subspace can act as a reflector. The vector reflection is often written in a "rejection-flip" form,

$$
x \mapsto x - 2 \, (x \wedge A) \, A^{-1},
$$

which collapses to a sandwiching expression

$$
x \mapsto -A \, x \, A^{-1}.
$$

When extended to a blade $X$ of grade $x$ reflected in a mirror blade $A$ of grade $a$, the outcome picks up a parity factor:

$$
X \mapsto (-1)^{x(a+1)} \, A \, X \, A^{-1}.
$$

The important lesson is not memorizing signs; it's that signs encode orientation conventions. If you represent either the mirror or the thing being reflected *dually* instead of directly, the sign rules change again (this is the bookkeeping summarized in the chapter's Table 7.1). If you don't care about orientation at all, you can often get away with the universal "unsigned" heuristic $X \mapsto A X A^{-1}$, but you're then explicitly discarding information.

## Why this matters

This sandwich reflection is the gateway drug: once reflections are conjugations, products of reflections become products of vectors/blades, and orthogonal operators become *elements of the algebra*. That is exactly what rotors and versors exploit.
