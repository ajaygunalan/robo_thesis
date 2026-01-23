## From "plane + angle" to a rotor

In 3D Euclidean geometric algebra, a rotation is most naturally specified by:

* a rotation plane represented by a unit bivector $I$
* a rotation angle $\theta$ (positive with the orientation of $I$)

Their product $\Phi = I\theta$ is the geometric object ("bivector angle") that does not depend on arbitrary orientation conventions. The rotor is
$$
R = e^{-\Phi/2}.
$$
If you happen to know $c=\cos\theta$, you can assemble $R$ directly as
$$
R=\sqrt{\frac{1+c}{2}}-\sqrt{\frac{1-c}{2}}\,I.
$$
The square roots are just $\cos(\theta/2)$ and $\sin(\theta/2)$ expressed in terms of $\cos\theta$. With standard positive roots, the orientation of $I$ controls the rotation direction.

(These formulas are shown on PDF page 11.)

## A cheap rotor taking one unit vector to another

Given unit vectors $a$ and $b$, there is a simple "minimal" rotor that rotates $a$ into $b$ *within their common plane*:
$$
R=\frac{1+ba}{\sqrt{2(1+a\cdot b)}}.
$$
Geometrically, you avoid computing the half-angle explicitly by observing that $a+b$ points in the half-angle direction when $a\neq -b$. The formula becomes unstable when $a$ and $b$ are near opposite; at $a=-b$, there is no unique rotation plane.

## Rotor from a full frame correspondence (3D-specific trick)

If you know how a whole frame rotates, you can recover the rotor more deterministically.

Let $\{e_i\}$ be three (not necessarily orthogonal) vectors and $\{f_i\}$ their images under the unknown rotation. Let $\{f^i\}$ be the **reciprocal frame** of $\{f_i\}$. Then in 3D the rotor satisfies
$$
R \sim 1 + \sum_{i=1}^3 f^i e_i,
$$
after which you scale/normalize so that $R\tilde R=1$.

Two sharp caveats from the text (PDF page 11–12):

* it returns zero for rotations by $\pi$ (so it literally fails there),
* it becomes unstable near $\pi$.

## The logarithm of a 3D rotor

Because 3D rotors are exponentials of bivectors (2-blades), you often want the generating bivector back—especially for interpolation.

Write a unit rotor as
$$
R = \langle R\rangle_0 + \langle R\rangle_2,
$$
with scalar part $\langle R\rangle_0$ and bivector part $\langle R\rangle_2$. The principal logarithm can be expressed in terms of those grade parts (PDF page 12):
$$
\log(R)=\frac{\langle R\rangle_2}{|\langle R\rangle_2|}\,
\text{atan}\!\left(\frac{|\langle R\rangle_2|}{|\langle R\rangle_0|}\right),
$$
with the practical instruction to use $\text{atan2}$ for stability and correct quadrant handling.

Special cases matter:

* When $\langle R\rangle_0=0$, the naive division inside $\text{atan}$ is ill-defined even though the rotation plane is still meaningful (this is exactly why $\text{atan2}$ is recommended).
* At $R=1$ the logarithm is essentially $0$ and numerically well-behaved.
* At $R=-1$ the rotation plane is ambiguous; you cannot resolve it without injecting an arbitrary choice.

## Exponentials you actually implement

To go the other direction (bivector $\to$ rotor), for a bivector $x$ in Euclidean 3D you have $x^2\le 0$. Let $h=\sqrt{-x^2}$. Then:
$$
e^x = \cos h + \frac{\sin h}{h}\,x,
$$
with the expected limit $e^0=1$ when $h\to 0$. Numerically, you also guard against floating point roundoff making $x^2$ slightly positive.

## Rotation interpolation: roots via logs (and the slerp form)

Given two orientations $R_1$ and $R_2$, define the relative rotation
$$
R = \frac{R_2}{R_1}.
$$
To apply this in $n$ equal steps, compute the incremental rotor
$$
r = R^{1/n} = e^{\log(R)/n},
$$
and the $k$-th interpolated pose is $r^k R_1$. Figure 10.4 on PDF page 13 shows this as repeatedly applying small equal rotations to an object (a bivector in the illustration).

There's also an explicit "slerp" closed form. If
$$
\frac{R_2}{R_1}=\cos(\theta/2)-I\sin(\theta/2),
$$
then for $\lambda\in[0,1]$:
$$
R_\lambda =
\frac{\sin((1-\lambda)\theta/2)}{\sin(\theta/2)}\,R_1
+\frac{\sin(\lambda\theta/2)}{\sin(\theta/2)}\,R_2.
$$
The chapter's preference is clear: the incremental-log form is structurally simpler, and once you're living in bivector space you can design higher-order interpolation (splines) without fighting ad-hoc quaternion formulas.

The programming example (PDF page 20, Figure 10.5) visualizes this by interpolating an oriented frame and drawing its trail.
