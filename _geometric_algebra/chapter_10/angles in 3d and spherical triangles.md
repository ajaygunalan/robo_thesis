## Angles in $\mathbb{R}^3$ are best treated as "bivector angles"

In 3D Euclidean space, the genuinely directional grades are vectors (1D directions) and bivectors (2D directions/planes through the origin). If you normalize everything to unit magnitude, "what is the angle between them?" is answered most cleanly by their *geometric ratio*.

The key philosophical point is that in 3D the *product* "rotation plane $\times$ rotation amount" is the geometric object. Trying to isolate a scalar angle by itself forces you to pick a conventional orientation for a plane, which is an extra non-geometric choice. In many computations you never need that scalar anyway: the rotor or bivector angle already is the thing you apply.

## Vector–vector: the ratio is a rotor

For unit vectors $u,v$, the geometric ratio
$$
R=\frac{v}{u}
$$
is a rotor encoding both the plane of rotation and the relative angle taking $u$ to $v$. That rotor is the complete oriented angular relationship.

## Bivector–bivector: reduce to vector–vector via dual normals

For unit bivectors (planes) $U,V$, take their dual normals:
$$
u\equiv U^*=\frac{U}{I_3},\qquad v\equiv V^*=\frac{V}{I_3},
$$
where $I_3$ is the 3D pseudoscalar. Then
$$
\frac{V}{U}=\frac{v}{u},
$$
so the angle between planes becomes the angle between their normals. Geometrically, the "measuring plane" ends up perpendicular to the line of intersection of the two planes, automatically.

## Vector–bivector: extracting the "tilt into a plane"

Given a unit bivector $U$ (a plane) and a unit vector $v$, the relationship is not "one plane angle" but "how far must $v$ rotate to lie in $U$" plus "which way is 'toward the plane'."

The chapter sets up a constructive definition: find a unit vector $w$ lying in the plane $U$ and perpendicular to $v$ such that rotating $v$ toward the plane over angle $\alpha$ makes it compatible with spanning $U$ alongside $w$. Algebraically (see Figure 10.2 on PDF page 6), demand
$$
U = v\, e^{w I_3 \alpha}\, w.
$$
This pins down both $w$ and $\alpha$ inside the product $vU$. Multiplying by $I_3$ "undualizes" it into a rotor-like exponential:
$$
v U I_3 = e^{wI_3\alpha}\,wI_3 = e^{wI_3(\pi/2+\alpha)}.
$$
Taking a logarithm retrieves the combined plane-and-angle information (though the chapter notes it would be nicer to isolate just the bivector angle $\alpha\,wI_3$).

## Spherical triangles: encode sides and angles as exponentials

A spherical triangle on the unit sphere can be described by vertex directions and the planes of its great-circle edges. Figure 10.3 on PDF page 7 shows the geometry and labels.

Let $\hat a,\hat b,\hat c$ be unit vectors to the vertices. Define three bivectors $\mathbf{A},\mathbf{B},\mathbf{C}$ whose magnitudes $A,B,C$ are the *side lengths* (arc angles) by:
$$
\frac{\hat a}{\hat b}\equiv e^{\mathbf{C}},\qquad
\frac{\hat b}{\hat c}\equiv e^{\mathbf{A}},\qquad
\frac{\hat c}{\hat a}\equiv e^{\mathbf{B}}.
$$
Then define the *internal angles* $a,b,c$ via ratios of the corresponding unit bivectors $\hat{\mathbf{A}},\hat{\mathbf{B}},\hat{\mathbf{C}}$:
$$
\frac{\hat{\mathbf{B}}}{\hat{\mathbf{A}}}\equiv -e^{I_3 c},\qquad
\frac{\hat{\mathbf{C}}}{\hat{\mathbf{B}}}\equiv -e^{I_3 a},\qquad
\frac{\hat{\mathbf{A}}}{\hat{\mathbf{C}}}\equiv -e^{I_3 b}.
$$

Multiplying the unit-vector side relations gives the compact closure:
$$
e^{\mathbf{A}}e^{\mathbf{B}}e^{\mathbf{C}}=1,
$$
and multiplying the unit-bivector angle relations gives:
$$
e^{I_3 c}e^{I_3 b}e^{I_3 a}=-1.
$$

Splitting by grade recovers classical spherical trig. In particular, taking scalar parts yields the cosine laws:
$$
\cos C=\cos A\cos B+\sin A\sin B\cos c,
$$
and, with the characteristic sign difference coming from the second product,
$$
\cos c=-\cos a\cos b+\sin a\sin b\cos C.
$$

The chapter's stance is blunt: once you can compute with these rotors/bivectors directly, reducing everything back to scalar identities is often a step backward.
