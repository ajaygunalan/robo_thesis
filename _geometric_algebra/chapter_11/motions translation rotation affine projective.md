# Motions: Translation, Rotation, Affine, Projective

Once you represent geometry as blades in the embedding space, motions become transformations of those blades. The chapter's operational thesis is that the homogeneous model makes "moving geometry around" more uniform than in a pure vector space model, because the same multivector types encode both direction and location.

## Outermorphisms and How Duals Transform

A linear map on vectors extends to blades as an outermorphism: if $x\mapsto f[x]$, then $X\mapsto f[X]$ for every blade $X$. Dual blades transform by the adjoint-like rule
$$
X^*\mapsto f^*[X^*] \equiv \det(f)\,f^{-1}[X^*],
$$
which collapses to $\pm f$ for orthogonal maps. This is the algebraic reason direct and dual representations do not always "move the same way," except for special transformations like rotations.

## Translation as a Linear Operator on Blades

A translation must move locations but leave pure directions unchanged. In the homogeneous model, translation is a linear map on blades:
$$
T_t[X] = X + t\wedge(e_0^{-1}X).
$$
The chapter notes this map has determinant $1$, so it preserves volumes/areas in the embedding space and, importantly, does not disturb the point normalization needed for affine ratios. Applying this to a pure direction blade yields no change, matching the "elements at infinity can't be translated" intuition.

For dual flats the translation law is different (because duals transform by the adjoint rule):
$$
T_t^*[X^*] = X^* - e_0^{-1}\wedge(tX^*),
$$
and in fact $T_t^* = T_t^{-1}$ since $\det(T_t)=1$.

## Rotation: The Nice Case

A Euclidean rotation about an axis through the origin is represented by an even versor (rotor) $R$. Because $R$ commutes with $e_0$, it acts uniformly on *both* direct and dual flats via the same sandwich:
$$
X\mapsto RXR^{-1},\qquad X^*\mapsto RX^*R^{-1}.
$$
This is the homogeneous model's cleanest motion law, and it foreshadows why later models (conformal GA) try hard to make more transformations look like versor sandwiches.

General rotations about an axis not through the origin can be built by translate–rotate–translate, producing different explicit formulas for direct and dual representations because translation itself is asymmetric between them.

Rigid body motion (rotation then translation) is just the composition of the two operators above—again, applied to any blade grade without special cases.

## Building Geometry by Moving It

A pragmatic modeling pattern emerges: construct a standard flat at the origin (e.g., $e_0\wedge \mathbf{e}_1$ for a canonical line), rotate it to set direction, then translate it to set location. This cleanly separates "attitude" (a base-space operation) from "placement" (the homogeneous extension), showing the homogeneous model as a structured augmentation of the vector space model rather than a replacement.

## Affine Transformations as "Preserve Weight," Projective as "Anything Linear"

Affine transformations are characterized by preserving point weights (the $e_0$ coefficient), because only then do ratios along a line behave meaningfully. This becomes the defining condition
$$
A[e_0]=e_0,
$$
equivalently $A[e_0^{-1}]=e_0^{-1}$. The chapter shows how an affine map decomposes into a linear base-space map $f$ plus translation $t$, and how to express the combined action on general multivectors:
$$
A[X] = f[X] + t\wedge\big(e_0^{-1}f[X]\big).
$$
This is the algebraic backbone behind why affine combinations (and algorithms like de Casteljau interpolation) are affinely covariant.

Projective transformations are simply *all* linear transformations of $\mathbb R^{n+1}$, interpreted back in the base space. They may send finite points to infinity. Because outermorphisms act on all grades, you can push projective geometry beyond "point loci" to "flat loci," e.g. solving $X\cdot A[X]=0$ for blades $X$ of different grades gives point conics and line conics in the same formalism (Figure 11.10, PDF p. 38).
