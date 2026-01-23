## A triangle as a pure directional equation

A planar triangle can be encoded without any point locations at all. Pick an oriented plane with unit bivector $I$. Represent the three directed sides as vectors $a,b,c$ satisfying the single closure constraint
$$
a+b+c=0.
$$
Geometrically, you might draw the edges tip-to-tail, but algebraically you are always free to redraw all vectors as anchored at the origin (the configuration is purely directional). Figure 10.1 on PDF page 3 makes this explicit by showing both drawings as the same algebra.

## Defining angles by geometric ratios (no sign headaches)

Instead of introducing unsigned angles and then patching signs later, define the *oriented* angles directly from vector ratios. With side lengths $a=|a|$, $b=|b|$, $c=|c|$ and the triangle's angles $\alpha,\beta,\gamma$ oriented consistently in the plane, the key move is to define:
$$
-\frac{b}{a}\equiv \frac{b}{a}e^{I\gamma},\qquad
-\frac{c}{b}\equiv \frac{c}{b}e^{I\alpha},\qquad
-\frac{a}{c}\equiv \frac{a}{c}e^{I\beta}.
$$
Each ratio is simultaneously a *scale* (the length ratio) and a *rotor* (the oriented turn in the plane).

Multiplying the three definitions and using $a+b+c=0$'s implied cyclic consistency gives
$$
e^{I(\alpha+\beta+\gamma)} = \left(-\frac{c}{b}\right)\left(-\frac{b}{a}\right)\left(-\frac{a}{c}\right)=-1=e^{I\pi},
$$
so
$$
\alpha+\beta+\gamma=\pi\mod(2\pi).
$$
The usual "sum of angles" theorem is just rotor bookkeeping.

## Trig functions appear by grade-splitting

The geometric product automatically splits into scalar (dot) and bivector (wedge) parts. For example, the first ratio implies
$$
-b\cdot a = ab\cos\gamma,\qquad
-b\wedge a = ab\,I\sin\gamma,
$$
and similarly for the other two angles. The scalar parts *are* cosines; the bivector parts *are* sines with their plane and orientation attached.

## Law of cosines from one square

Solve $a+b+c=0$ for $c$ and square:
$$
c^2=(a+b)^2=a^2+b^2+ab+ba=a^2+b^2+2a\cdot b.
$$
With the angle convention encoded above, this becomes the standard law of cosines:
$$
c^2=a^2+b^2-2ab\cos\gamma.
$$

## Law of sines from one wedge identity

Take the outer product of $a+b+c=0$ with each side in turn. You get the compact identity
$$
a\wedge b=b\wedge c=c\wedge a,
$$
which is actually valid in *any* ambient dimension as long as everything lies in one plane. Dividing out the oriented plane $I$ yields the classical form:
$$
\frac{\sin\alpha}{a}=\frac{\sin\beta}{b}=\frac{\sin\gamma}{c}.
$$

## Oriented area as a clean bivector ratio

The triangle's oriented area is most naturally a scalar extracted from a bivector by dividing by the plane's unit bivector:
$$
\Delta=\frac{a\wedge b}{2I}=\frac{b\wedge c}{2I}=\frac{c\wedge a}{2I}.
$$
This keeps area tied to orientation, instead of smuggling orientation in as an afterthought.
