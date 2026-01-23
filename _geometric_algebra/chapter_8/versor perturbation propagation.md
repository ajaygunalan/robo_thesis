# Versor Perturbation Propagation

Once you accept "only rotor-type perturbations preserve geometric meaning," you still face two distinct sensitivity problems:

1. the operand changes inside a fixed transformation, versus
2. the transformation itself changes.

They look similar syntactically but behave differently algebraically.

## 1) Transforming a perturbation: conjugate the error bivector

Suppose you transform $X$ by a versor $V$:

$$
X \mapsto V X V^{-1}.
$$

Now perturb $X$ by a small rotor $e^{-\delta A/2}$:

$$
X \mapsto e^{-\delta A/2} X e^{\delta A/2}.
$$

If you do both—first perturb, then apply $V$—you get

$$
V \, (e^{-\delta A/2} X e^{\delta A/2}) \, V^{-1} = (V e^{-\delta A/2} V^{-1}) \, (VXV^{-1}) \, (V e^{\delta A/2} V^{-1}).
$$

Using the exponential/versor conjugation rule,

$$
V e^{-\delta A/2} V^{-1} = e^{-V(\delta A)V^{-1}/2},
$$

so **the perturbation generator bivector simply conjugates**:

$$
\delta A \mapsto V(\delta A)V^{-1}.
$$

This is exact (no "first-order only" caveat). It's the cleanest possible message: *push the error bivector through the same transform*.

## 2) Perturbing the versor: the induced error is a difference of bivectors

Now the trickier case. Keep $X$ fixed but perturb the transformer:

$$
V \mapsto e^{-\delta A/2} \, V \, e^{\delta A/2}.
$$

You want the perturbation *as seen on the result* $VXV^{-1}$: i.e., rewrite the new mapping as "old result, then a small rotor." To first order, you can expand and isolate the effective perturbing versor acting on $VXV^{-1}$, which yields an induced bivector

$$
\delta B = \delta A - V \, \delta A \, V^{-1}.
$$

This is a deep-looking but natural structure: the "same" perturbation bivector $\delta A$ applied on the left and right of $V$ doesn't survive unchanged after you compare it to $V$'s own action. What remains is the **mismatch** between $\delta A$ and its conjugate.

Key warning: this is **local** (first-order). For finite changes, higher-order effects matter and the "effective axis/plane" typically moves.

## Application: tilting a mirror rotates the reflection result

A planar mirror through the origin with normal $n$ reflects by

$$
n[X] \equiv n X n^{-1}.
$$

Perturb the normal by a small change $a$. The directional derivative with respect to $n$ shows the reflected output changes (to first order) by a commutator with a bivector:

$$
(a \ast \partial_n) \, (n X n^{-1}) = (nXn^{-1}) \times (2 n^{-1} \wedge a).
$$

So locally, the change in the reflected element is itself rotor-generated, with effective generator

$$
B = 2 n^{-1} \wedge a.
$$

Now relate $a$ to an actual mirror motion: rotate the mirror by a small angle $\phi$ in plane $I$ (unit 2-blade), so the mirror normal changes by

$$
a = n \times (I\phi).
$$

Substitute into $B$:

$$
B = 2\phi \, n^{-1} \wedge (n \times I) = 2\phi \, n^{-1} \wedge (n \rfloor I).
$$

That single bivector encodes both *which plane* the reflected object rotates in and *by how much*.

In 3D, if $m = I^*$ is the rotation axis of the mirror motion and $n$ is unit, dualize $B$ to get a rotation axis for the reflection:

$$
b = B^* = 2\phi \, \frac{m \wedge n}{|n|}.
$$

Geometrically: $b$ is the projection of $m$ onto the mirror plane (the "rejection" of $m$ by $n$). If $\psi$ is the angle between $m$ and $n$, the reflected output rotates by angle

$$
\beta = |b| = 2\phi \sin\psi.
$$

This recovers the folklore ("mirror tilt doubles the ray angle") as a special case: when $m \perp n$ ($\psi = \pi/2$), $\beta = 2\phi$; when $m \parallel n$, $\beta = 0$.

The real win is not the number 2: it's that the whole sensitivity—axis, plane, magnitude—drops out as one bivector computation.
