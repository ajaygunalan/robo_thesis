## A single reflection operator that doesn't care what you reflect

Classically, reflecting a line in a plane forces you to split the job: find the intersection point, reflect the direction, then rebuild the line. The conformal model lets you refuse that whole workflow: if reflection is a versor, you reflect *the multivector that represents the object*, and location+orientation go along automatically.

The seed is the standard vector-space-model reflection of a vector $\mathbf{u}$ in a (not-necessarily-unit) normal $\mathbf{n}$:
$$
\mathbf{u}' = -\,\mathbf{n}\,\mathbf{u}/\mathbf{n},
$$
which is the geometric-algebra rewrite of $\mathbf{u}-2(\mathbf{u}\cdot \mathbf{n})\mathbf{n}$ (PDF page 24).

Because the conformal model contains the Euclidean model as a subalgebra, the same algebraic identity is valid there. The upgrade is: once you recognize the reflecting plane as a dual plane vector $\pi$, the exact same sandwiching pattern reflects *any directly represented flat* $X$:
$$
X \;\mapsto\; \pi\,\hat X\,\pi^{-1}.
$$
Here $\hat{X}$ is the grade involution, which neatly absorbs the grade-dependent sign flips that appear when reflecting blades (the chapter explicitly uses this trick when reflecting a line through the origin before translating to the general case). This is equation (13.11) (PDF page 25).

Figure 13.3 (PDF page 23) visualizes the point: the line $\Lambda$ and plane $\pi$ are reflected as whole conformal objects, not as "a point plus a direction," and the result $\pi\Lambda/\pi$ is the reflected line in one shot.

If you *do* want the intersection point, you can still extract it algebraically as a meet: the chapter notes the flat point of intersection can be obtained by the contraction $\pi\rfloor \Lambda$ (PDF page 25).

## Differential mirror motion: a first-order versor perturbation yields a second-order curve

Section 13.7 pushes the same reflection operator into a "moving mirror" situation: reflect an element $X$ in a dual plane $\pi$, then rotate the plane slightly around a line $\Lambda$ and ask what happens to the reflected object.

Using the general perturbation-versor machinery developed earlier in the book, the chapter derives a compact bivector for the induced displacement of the reflection operator. In its final geometric form (PDF page 32), the perturbation is a rotation about the line obtained by projecting the mirror-rotation axis $\Lambda$ onto the mirror plane $\pi$:
$$
B \;=\; 2\,(\pi\wedge \Lambda)^{*}\wedge \pi,
$$
where the intermediate algebra rewrites the expression into "dual of a meet" language. The takeaway is not the symbol pushing; it's the geometry: *changing the mirror plane produces a rotation of the reflected object around the projected axis*.

Figure 13.7 (PDF page 33) shows the effect vividly. For a reflected point, the exact orbit (red) is well-approximated at first order by points produced by rotating around that projected line (black), and the same construction works unchanged when $X$ is a line instead of a point (panel b). The punchline the chapter stresses is subtle but important: first-order perturbations in a versor can naturally generate second-order geometric paths, so you get a "better curve" than a naïve first-order Taylor expansion of positions.
