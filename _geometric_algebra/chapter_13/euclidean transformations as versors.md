## Why isometries become versors here

Because squared Euclidean distance is encoded by the representational inner product, a Euclidean transformation (distance-preserving map in $E^n$) must lift to an inner-product-preserving map in $\mathbb{R}^{n+1,1}$. That is, Euclidean isometries correspond to orthogonal transformations of the representational space. In geometric algebra, orthogonal transformations are represented by versors (sandwich operators).

There's one extra constraint: not every orthogonal transformation of $\mathbb{R}^{n+1,1}$ is a Euclidean motion of the modeled space. The model's "distance interface" depends on the distinguished element $\infty$, so a Euclidean versor must preserve $\infty$ under the sandwich action:
$$
V\,\infty\,V^{-1}=\infty.
$$
This pins down exactly which versors correspond to Euclidean transformations.

## Reflections generate everything

The simplest versors are vectors, and in this model the vectors that qualify as Euclidean reflection versors are precisely dual plane vectors. That's the algebraic packaging of the classical theorem: every Euclidean isometry is a composition of reflections in planes.

Figure 13.1 (PDF page 12) illustrates the two key constructions: two parallel reflecting planes yield a translation, and two intersecting reflecting planes yield a rotation.

## Two elementary proper motions: translations and rotations

A proper rigid motion is an even versor (a rotor after normalization). The chapter derives explicit closed forms by multiplying reflection planes.

### Translation rotor from two parallel planes

Reflect in two parallel planes with shared unit normal $\mathbf{n}$ and offsets $\delta_1,\delta_2$. Their product collapses to a translator of the form
$$
T_{\mathbf{t}} = 1 - \tfrac12\,\mathbf{t}\,\infty,
\qquad
\mathbf{t}=2(\delta_2-\delta_1)\mathbf{n}.
$$
The derivation is short because $\infty^2=0$, so the exponential representation truncates immediately:
$$
T_{\mathbf{t}}=\exp(-\mathbf{t}\,\infty/2).
$$
This is the algebraic reason translations commute and add: products of translators just add the translation vectors (PDF page 26).

### Rotation rotor is literally the Euclidean rotor you already know

If both reflection planes pass through the chosen origin point, the plane vectors are purely Euclidean and their product is the standard Euclidean rotor $R$ from the vector space model. In the conformal setting, it rotates the Euclidean part of a point while leaving $o$ and $\infty$ invariant (PDF page 12–13). The exponential form stays the familiar one:
$$
R=\exp(-I\phi/2)=\cos(\phi/2)-\sin(\phi/2)\,I,
$$
with $I$ the unit bivector of the rotation plane.

A general rigid body motion is then a translation followed by a rotation, represented as a rotor of the form $T_{\mathbf{t}}R$ (PDF page 13).

## The operational-model payoff: covariance "for free"

Once motions are versors, structure preservation stops being a hope and becomes a theorem you can exploit as a design principle.

The versor sandwich preserves:

* geometric products: $V[XY]=V[X]V[Y]$,
* linearity: $V[\alpha X+\beta Y]=\alpha V[X]+\beta V[Y]$,
* grade: $V[\langle X\rangle_k]=\langle V[X]\rangle_k$.

So any construction built from geometric-algebra operations (outer/inner products, contractions, duality, meet/join, inverses, grade selection) automatically transforms covariantly:
$$
V(A\circ B)V^{-1}=(VAV^{-1})\circ(VBV^{-1})
$$
for the relevant product $\circ$ (PDF page 14).

That covariance has a companion fact the chapter makes explicit: *properties* expressed as scalar equations in the algebra become invariants under Euclidean motions. If "being a point" is characterized by $p^2=0$ and a weight condition involving $\infty$, then a Euclidean versor preserves those conditions because it preserves the products and preserves $\infty$ (PDF page 15–16).
