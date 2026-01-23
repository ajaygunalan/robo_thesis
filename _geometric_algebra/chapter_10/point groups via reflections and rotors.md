## Point groups as "finite closure under composing symmetries"

Crystallography asks a brutally concrete question: if you stand at a point in a crystal, which reflections and rotations can you have such that repeatedly composing them produces only finitely many distinct symmetries? That finite set of local operators is a **point group**.

The vector space model is ideal here because everything is local and directional: symmetries fix the origin and only manipulate directions around it.

## Reflections are vectors-as-operators

Let $a$ be a unit vector ($a^2=1$) used as the oriented normal of a reflection plane through the origin. Then reflecting a vector $x$ is
$$
x' = -a x a.
$$
As a transformation on vectors, $a$ and $-a$ act the same—so the *unoriented* plane is encoded. But if you want the cleanest classification of symmetry operators, you keep track of orientation at the operator level, so the sign still matters in the algebra of versors.

## Rotations are products of reflections (and "$\pm$" matters)

An even number of reflections is a rotation. With two reflection normals $a,b$, the composed operator is the rotor-like versor
$$
R \equiv ab.
$$
A $p$-fold rotational symmetry means applying the induced rotation to vectors $p$ times returns the original vector. Since $R$ and $-R$ generate the same sandwiching action, that condition can show up as either $R^p=1$ or $R^p=-1$ at the operator level. The chapter chooses the more specific "spin-aware" condition when classifying operator sets; in general, for a $p$-fold symmetry you have
$$
R^{2p}=1.
$$

## A 2D example: the four-fold point group $2H_4$

In the plane, take two generating reflection normals $a,b$. For a four-fold symmetry, impose:
$$
a^4=1,\qquad b^4=1,\qquad (ab)^8=1.
$$
This forces $a$ and $b$ to be unit vectors with relative angle $\pi/4$.

The resulting point group (denoted $2H_4$ in the chapter's reference) contains 16 versor operators. A compact way to see the set is:

* **rotations (and their sign variants):** $\pm 1,\ \pm ab,\ \pm (ab)^2,\ \pm ba$
* **reflections (and their sign variants):** $\pm a,\ \pm aba,\ \pm bab,\ \pm b$

Acting on a point/vector $x$ by sandwiching $x_i = V_i x V_i^{-1}$ produces only 8 distinct locations from these 16 operators, because the $\pm$ pairs act identically on vectors.

## 3D point groups from three generators and Coxeter's finiteness test

In 3D, you generally need three generating reflection normals $a,b,c$. A standard way to encode the constraints is:
$$
(ab)^{2p}=(bc)^{2q}=(ca)^{2r}=1.
$$
Each product is a rotation whose axis ("pole") is some unit vector; equivalently, these can be written as exponentials with angles $\pi/p$, $\pi/q$, $\pi/r$.

A necessary condition for the generated operator set to be finite is Coxeter's inequality:
$$
\frac{1}{p}+\frac{1}{q}+\frac{1}{r} > 1.
$$
The integer solutions $(p,q,r)$ produce the finite 3D point groups.

## Why this stops at point groups

To get full crystallographic space groups, symmetries must also be compatible with translations. The vector space model does not represent translations structurally, so you lose the "single algebraic object + uniform operator" convenience. The chapter explicitly points forward to richer models (notably conformal geometric algebra) that incorporate translation natively.

Figure 10.6 on PDF page 21 shows the idea computationally: choose generating vectors, brute-force multiply to generate new versors, and apply them to a single point to visualize the orbit (24 symmetries shown for a hexagonal configuration; the largest cubic point group has 48 operators).
