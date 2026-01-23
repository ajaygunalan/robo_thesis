## Screw motion is the natural normal form for rigid-body rotors

A general rigid body motion rotor is presented in the standard "rotation then translation" factoring, but Chasles' theorem says you can always view the same motion as a *screw*: rotation about some spatial axis together with translation along that axis.

The conformal model makes this decomposition computationally clean because both rotation and translation are already versor-native. The chapter's setup is: start from a motion of the form "translate by $\mathbf{t}$, then rotate in plane $I$," and rewrite it as "translate along the axis, then rotate about a displaced axis," in a way that makes the two factors commute (PDF pages 27–29).

Figure 13.4 (PDF page 28) gives the geometric picture: decompose $\mathbf{t}$ into the component along the rotation axis (translation $w$) and the in-plane component that determines how far the axis must be shifted (vector $v$).

## Extracting the screw parameters without trigonometric pain

Let $I$ denote the rotation plane bivector (in $E^3$ its dual is the rotation axis direction), and let $\mathbf{t}$ be the translation vector of the motion.

The chapter first splits $\mathbf{t}$ relative to the plane $I$:

* the *rejection* (perpendicular-to-plane component) becomes the along-axis translation
  $$
  w=\frac{\mathbf{t}\wedge I}{I},
  $$
* the remaining in-plane part is treated as a 2D problem inside the $I$-plane (PDF page 28–29).

Swapping translations past the rotation rotor yields a "chord" interpretation: $v-Rv\tilde R$ is the chord connecting a point in the rotation plane to its rotated image. Solving the commutation constraint gives the axis offset
$$
v = (1-R^2)^{-1}\,u,
$$
where $u$ is the in-plane component derived from $\mathbf{t}$ (equation (13.13), PDF page 29). The geometry in Figure 13.4 matches this exactly: pick the unique $v$ whose rotation chord fits the needed in-plane discrepancy.

The result is an explicit screw decomposition written entirely in geometric algebra primitives (PDF page 29).

## The logarithm of a rigid body motion rotor

Interpolation wants a logarithm: if $V$ is the rotor for a rigid body motion, you want a bivector $B$ such that
$$
V = e^{B}.
$$
The chapter uses the screw form precisely because the two commuting factors let you add exponents. With the screw parameters in hand, the logarithm becomes a closed-form bivector expression (equation (13.15), PDF page 30):
$$
\log(V)=
-\frac12\,\frac{\mathbf{t}\wedge I}{I}\,\infty
+\frac12\,(1-R^2)^{-1}(\mathbf{t}\rfloor I)\,\infty
-\frac12\,I.
$$
(Here the $\infty$-terms encode translation, while $I$ encodes rotation.)

A key practical step is retrieving rotation and translation parts from the given rotor $V$ using contractions with $o$ and $\infty$ (PDF page 30):

* extract the rotation rotor:
  $$
  R = -\,o\rfloor (V\,\infty),
  $$
* then get the translation vector:
  $$
  \mathbf{t} = -2\, (o\rfloor V)/R.
  $$
  The chapter packages the full computation as pseudocode in Figure 13.5 and calls out the important special cases:
* $R=1$: pure translation, logarithm is just the translation bivector;
* $R=-1$: no unique logarithm (a $\pi$ rotation could be in any plane unless you impose an extra convention; in 2D it can outright fail).

## Interpolation via fractional powers: "do the screw gradually"

Once you can compute $\log(V)$, you can interpolate by taking fractional powers:
$$
V^{1/N}=\exp(\log(V)/N).
$$
Section 13.6 shows this in a particularly geometric setup: use two unit lines $L_1,L_2$, observe that their ratio encodes (essentially) the squared motion versor, and define the step rotor as
$$
V^{1/N}=\exp\!\left(\frac{\log(L_2/L_1)}{2N}\right).
$$
Repeatedly applying this to $L_1$ produces a smooth screw-like interpolation that naturally extrapolates, as in Figure 13.6 (PDF page 31).
