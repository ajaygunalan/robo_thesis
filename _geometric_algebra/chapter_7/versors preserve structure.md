# Versors Preserve Structure

A versor is the general operator concept behind reflections and rotations: "a product of invertible vectors, used by sandwiching." Once you accept that definition, orthogonal geometry becomes a study of what sandwiching preserves.

## Versors and the versor product

A $k$-versor is

$$
V = v_k \cdots v_2 v_1
$$

with each $v_i$ invertible. Geometrically, this is "$k$ reflections glued together." The induced action on a blade $X$ of grade $x$ is the **versor product**:

$$
V[X] = (-1)^{xv} V \, X \, V^{-1},
$$

where $v$ is the parity of $V$ (even/odd number of vector factors). This single formula encodes both cases:

* **Even versor (rotation-type):** $V[X] = V X V^{-1}$.
* **Odd versor (reflection/antirotation-type):** $V[X] = V \widehat{X} V^{-1}$, because $\widehat{X} = (-1)^x X$.

The inverse is always the reverse-ordered product of inverses. For unit versors (notably rotors), the inverse is the reverse.

## Even vs odd: determinant and handedness

Versors split orthogonal maps into two geometrically distinct classes:

* Even versors preserve handedness and have determinant $+1$.
* Odd versors flip handedness and have determinant $-1$.

The determinant calculation is remarkably clean: it depends only on the parity of the versor, not on the signature of the metric. This is the operator-level explanation for why "rotations" and "reflections" are separated so naturally by "even" vs "odd."

## Versor products are exactly orthogonal transformations

The defining property of orthogonal maps is inner-product preservation. Versor actions satisfy it automatically:

$$
V[x] \cdot V[y] = x \cdot y.
$$

Conversely, every orthogonal linear map can be represented as a versor action (a geometric algebra restatement of "orthogonal maps are compositions of reflections," with the computational operator built in).

## Structure preservation: the real prize

Because versor actions are orthogonal and extend as outermorphisms, they preserve the whole product structure of geometric algebra. Concretely, for suitably defined products:

* wedges map to wedges,
* contractions map to contractions,
* the geometric product is preserved.

The geometric product preservation is the one that changes how you think about "multiplication" in GA:

$$
V[A] \, V[B] = V[AB].
$$

It means you can transform an entire construction by transforming its inputs.

A particularly useful corollary is how versors interact with exponentials of bivectors:

$$
V[\exp(B)] = \exp(V[B]).
$$

So you can "move" a rotor (or any bivector exponential) by transforming its generating bivector.

## Operators as objects, and nested vs concatenated motion

Versors don't just transform geometric objects; they transform other operators. Two patterns separate cleanly:

* **Concatenation:** "do $V_1$, then $V_2$" corresponds to multiplying versors $V_2 V_1$.
* **Nesting:** "transform the operator $V_1$ by $V_2$" corresponds to sandwiching $V_2 V_1 V_2^{-1}$.

This is the GA version of conjugation in matrix groups, but here it has immediate geometric meaning because the operator itself is a multivector with a plane/axis interpretation.
