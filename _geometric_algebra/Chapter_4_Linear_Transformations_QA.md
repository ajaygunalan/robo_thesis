# Chapter 4: Linear Transformations in Geometric Algebra — Q&A

---

## 4.1 Why do linear transformations matter so much if they can't even do something as basic as translation?

A "linear transformation" can't translate anything because it must preserve the origin and the parallelogram rule. That sounds limiting—until you realize linear maps are the atoms you build *everything else* from. They're the backbone of higher-dimensional "operational models" that *do* represent translations (affine / Euclidean models later in the book), and they're what you get when you zoom in on any smooth transformation: locally, complicated geometry looks linear, which is why differential geometry runs on linear maps. The point is: even if you care about "real" motions like translation, you still end up living in the linear world to compute, approximate, and reason.

**Key equation:**
$$f[\alpha x+\beta y]=\alpha f[x]+\beta f[y]$$

---

## 4.2 How can one simple rule ("preserve the wedge product") let you transform whole subspaces—lines, planes, volumes—as directly as you transform vectors?

The wedge product is how you encode "this whole subspace" as a single object (a blade). The miracle is that a linear map doesn't just move vectors; it moves *the subspaces they span* in one shot, if you demand one structural promise: it must commute with the wedge. That one promise makes "transform the plane" mean literally "transform its spanning bivector," and it guarantees blades stay blades, grades stay grades, and intersections behave predictably. Once you have that, you can stop doing geometry by constantly unpacking objects into coordinates and reassembling them.

**Key equation:**
$$f[A\wedge B]=f[A]\wedge f[B]$$

---

## 4.2.1 Is the outermorphism rule something you choose, or something geometry basically forces on you if you want consistency?

You don't get to "choose" the outermorphism rule if you want consistency—you're basically forced into it by the way blades are built from vectors. A 2-blade $x\wedge y$ is an oriented parallelogram; linear maps preserve the parallelogram construction (that's what linearity *means*), so the only consistent way to transform that parallelogram is to transform its sides and rebuild it. That's exactly the rule $f[x\wedge y]=f[x]\wedge f[y]$, and the same logic climbs the ladder to 3-blades, 4-blades, and beyond.

**Key equation:**
$$f[x\wedge y]=f[x]\wedge f[y]$$

---

## 4.2.2 What surprising "common-sense" intuition fails (like expecting a projected plane to become a line), and what does that reveal about representing geometry correctly?

Here's the intuition trap: you look at a projection that flattens a plane down to a line and think "the plane should become that line." But a blade is not "the set of vectors in the plane"—it's an oriented *area element* representing that plane. Under a projection onto a line, areas don't become lines; they collapse to zero area. The algebra is brutally honest about that: the grade is preserved, and the bivector's magnitude is the area—so if the area dies, the bivector becomes $0$, not a vector. This is exactly the kind of mistake that quietly ruins geometric reasoning if you treat blades as mere labels instead of measurements.

**Key equation:**
$$P[a\wedge b]=P[a]\wedge P[b]=a\wedge 0=0$$

---

## 4.2.3 Can you define the determinant without matrices as "what happens to the pseudoscalar," and instantly read off volume-scaling and orientation flips?

Determinants stop being a matrix ritual and become something you can *see*: "what happens to the pseudoscalar." The pseudoscalar $I_n$ is the unit oriented $n$-volume element of the space; a linear map must send it to another pseudoscalar, which can only differ by a scalar factor. That factor is the determinant—so det is literally "signed volume scaling." Orientation flips? That's $\det(f)<0$. Volume preserved? That's $|\det(f)|=1$. And composition becomes obvious because volumes scale multiplicatively.

**Key equation:**
$$f[I_n]\equiv \det(f)\,I_n$$

---

## 4.3 Once the wedge product behaves nicely under any linear map, what goes wrong (and what new tool fixes it) when you try to transform dot-products and perpendicularity?

Outer products are easy because they're metric-free: they care about span and orientation, not angles or lengths. The moment you want perpendicularity, projections, or "parts along/orthogonal," you're in metric territory—and a generic linear map distorts the metric. That's why the contraction doesn't transform by the naive "just apply $f$ everywhere." You need an additional operator that knows how $f$ interacts with the inner product: the adjoint. Once the adjoint enters, the transformation law becomes precise (and it's the source of all those "inverse/transpose" rules people half-remember from matrices).

**Key equation:**
$$f[A\,\lrcorner\,B]=\bar f^{-1}[A]\,\lrcorner\,f[B]$$

*(same statement as (4.13), with $\bar f$ the adjoint)*

---

## 4.3.1 Why does the scalar product "not change" in one sense, yet lengths and angles can still change—and what's the trap in interpreting that?

The scalar product "doesn't change" only in the boring sense that a scalar stays a scalar under any linear map—so applying $f$ to the *number* $A*B$ does nothing. That is **not** the same as saying the scalar product of the transformed objects stays the same. The trap is confusing $f[A*B]$ with $(f[A])*(f[B])$. In reality, lengths and angles usually *do* change, and the distortion is governed by the metric mapping $g=\bar f\circ f$: the scalar product of transformed vectors becomes a scalar product in a *new metric*.

**Key equation:**
$$f[A*B]=A*B$$

---

## 4.3.2 What is the adjoint really (beyond "it's the transpose"), and why does it control how transformations interact with inner products?

The adjoint isn't "just transpose" as a memorized matrix trick—it's the conceptual move that lets you slide a transformation from one slot of an inner product to the other without changing the value. That's why it's defined implicitly: it's the unique map $\bar f$ satisfying "$f$ on the left equals $\bar f$ on the right." In Euclidean orthonormal coordinates that becomes transpose, but the real point is geometric: $\bar f$ is how you correctly account for metric interactions, and it's the ingredient that makes contraction and duality transformation laws come out cleanly.

**Key equation:**
$$\bar f[a]*b = a*f[b]$$

---

## 4.3.3 What's the exact transformation law for contractions, and how does it secretly encode the inverse/transpose behavior people keep messing up in practice?

Contraction is "take out the part in a perpendicular manner," so when a transformation warps perpendicularity, the contraction can't just follow $f$ blindly. The exact law tells you which object must be corrected by an inverse-adjoint: the piece you're "taking out" has to be mapped back through the distortion before you can remove it orthogonally. This is the clean, basis-free origin of the infamous inverse/transpose behavior—except here it's not folklore; it's forced by the algebra.

**Key equation:**
$$f[A\,\lrcorner\,B]=\bar f^{-1}[A]\,\lrcorner\,f[B]$$

---

## 4.3.4 What makes orthogonal transformations uniquely special—why are they the only ones that preserve the contraction's structure?

Orthogonal transformations are special because they don't warp the metric at all—they preserve inner products. That single fact collapses the whole complication: the adjoint equals the inverse, so the contraction transforms *structure-preservingly*. In other words, orthogonal maps are the rare cases where "transform, then contract" equals "contract, then transform." That's why rotations and reflections are so clean in geometric algebra—and why the book tells you it will mostly care about them.

**Key equation:**
$$f[a]\cdot f[b]=a\cdot b \;\Rightarrow\; \bar f=f^{-1}$$

---

## 4.3.5 If dual objects (like normals) don't transform like the things they're dual to, how many geometry/graphics mistakes does that explain?

Dual objects are where a ton of real-world mistakes come from. A "normal" is not the same kind of geometric thing as a direction vector: it's a *dual representation* of a plane (or higher subspace). Because duality depends on the metric, duals cannot transform by the same rule as direct blades unless the transformation is orthogonal. The clean fix is to define the correct dual transformation $f^*$ by demanding it preserve "being dual," and that forces the determinant and inverse-adjoint to appear. This is exactly the conceptual origin of the "inverse-transpose normal" rule in graphics—except here it's one line, not a superstition.

**Key equation:**
$$f^*[D]=\det(f)\,\bar f^{-1}[D]$$

---

## 4.3.6 Why is the cross product a bad geometric citizen under general linear transforms, and what replaces it without the usual "inverse-transpose normal" headache?

The cross product is a troublemaker because it's secretly a **dual** of a bivector, smuggled into 3D as an ordinary-looking vector. That means under a general linear map it must transform like a dual object, not like a direction—and that's why "transform the normal like you transform points" breaks under non-uniform scaling or shear. Geometric algebra makes the cheat explicit: $a\times b$ is really $(a\wedge b)^*$. Once you keep it as the bivector $a\wedge b$, it transforms by the simple outermorphism rule and you never have to remember the inverse-transpose hack again.

**Key equation:**
$$a\times b=(a\wedge b)^*=(a\wedge b)\,\lrcorner\,I_3^{-1}$$

---

## 4.4 Can you compute the inverse of a linear transformation in a compact, coordinate-free way that works on blades—not just on vectors?

Inverting a linear map is usually taught as a coordinate grind. Here you get a compact, coordinate-free formula that works uniformly on vectors, bivectors, trivectors—any blade—because it's expressed entirely in terms of the outermorphism and the pseudoscalar. The punchline is that the inverse can be written using duality and contraction with $I_n$, with the determinant providing the expected volume-scaling normalization. This is the algebraic reason the classical "adjugate over determinant" formula exists—except now it's not a random trick, it's geometry.

**Key equation:**
$$f^{-1}[A]=\frac{\bar f\!\left[A\,\lrcorner\,I_n^{-1}\right]\,\lrcorner\,I_n}{\det(f)}$$

---

## 4.5 If matrices are just basis-dependent shadows of transformations, what geometric meaning are they hiding, and how do you recover that meaning when you need it?

Matrices are useful precisely because they're *basis-bound*—but that also makes them lie by omission: they hide which geometric operations are being performed. This section shows you how to recover the meaning: a matrix is nothing more than "how the map hits basis vectors," expressed via inner products with a reciprocal frame. Once you see that, you can move smoothly between the clean geometric definition of a transformation and the fast matrix implementation—without confusing the representation (the matrix) with the thing itself (the linear map).

**Key equation:**
$$[[f[x]]]=[[f]]\,[[x]]$$

---

## 4.5.1 What does a single matrix entry mean geometrically, and how does geometric algebra expose that meaning instead of treating it as bookkeeping?

A matrix entry looks like dumb bookkeeping until you translate it back into geometry: it's the $j$-th coordinate of the transformed $i$-th basis vector, which you extract by dotting with the reciprocal basis vector. Geometric algebra even shows you what that extraction *really* is: a wedge-based replacement inside the pseudoscalar followed by contraction with $I_n^{-1}$. That means every matrix entry is secretly a statement about oriented volumes in the chosen basis—something you can reason about, not just compute.

**Key equation:**
$$[[f]]^{\,j}_{\,i}\equiv f[b_i]\cdot b^{\,j}$$

---

## 4.5.2 How do you build the transformation on bivectors/trivectors/etc from the vector transform alone—and why do minors/determinants show up automatically?

Once you know what $f$ does to vectors, you automatically know what it does to bivectors, trivectors, and so on—because the outermorphism builds higher-grade action from wedge products. In matrix language, that means the bivector (and higher-grade) matrices are *made of minors* of the vector matrix. The "minors/determinants show up" not because someone invented them, but because wedge products are multilinear and antisymmetric, so the coefficients naturally become those alternating sums.

**Key equation:**
$$[[f]]^{\,j_1j_2}_{\,i_1i_2} = [[f]]^{\,j_2}_{\,i_2}[[f]]^{\,j_1}_{\,i_1} - [[f]]^{\,j_1}_{\,i_2}[[f]]^{\,j_2}_{\,i_1}$$

---

## 4.6 If you only remember a handful of formulas from this chapter, which ones let you transform wedges, contractions, duals, and inverses without re-deriving everything?

This is the "tattoo these on your brain" section: with a handful of transformation laws you can push $f$ through wedges, scalars, contractions, duals, and inverses without re-deriving anything. The main story is simple: wedges transform by pure outermorphism; contractions require the inverse adjoint; inverses can be written in a clean formula using the pseudoscalar and the determinant. Once these are internalized, linear transformation mistakes stop being mysterious—they become "you applied the wrong map to the wrong representation."

**Key equations:**
$$f[A\wedge B]=f[A]\wedge f[B]$$
$$f[A\,\lrcorner\,B]=\bar f^{-1}[A]\,\lrcorner\,f[B]$$
$$f^{-1}[A]=\frac{\bar f[A\,\lrcorner\,I_n^{-1}]\,\lrcorner\,I_n}{\det(f)}$$

---

## 4.7 Where does this viewpoint pay off later—especially for orthogonal transforms and eigen/singular-value ideas—and what's worth reading next?

This chapter's payoff is that it sets you up for the real stars: orthogonal transformations and their deep, clean representation in geometric algebra (which the book promises to unfold in Chapter 7). The reason you should care now is that the "orthogonal case" is exactly where everything becomes structure-preserving: adjoint equals inverse, contractions behave nicely, duals behave nicely (up to a sign), and you can reason geometrically instead of juggling matrix identities. This section points you toward deeper work (eigen/SVD ideas, multilinear/tensor viewpoints) once you have the geometric product under your belt.

**Key equation:**
$$\text{If } f \text{ is orthogonal, then } \bar f=f^{-1} \text{ and } f[A\,\lrcorner\,B]=f[A]\,\lrcorner\,f[B]$$

---

## 4.8 Which exercises will actually make "orientation, determinant, adjoint, duality" stop being symbols and start being instincts?

The exercises are where "determinant, adjoint, dual, normal" stop being buzzwords. They force you to confront exactly the common confusions this chapter warns about—especially the scalar-product trap and the dual-versus-direct transformation issue. A good example is the adjoint construction formula: it's not just an existence claim; it's a practical recipe that makes you compute $\bar f$ without leaning on coordinates. If you do these problems, you stop trusting memorized rules and start trusting the structure.

**Key equation:**
$$\bar f[x]=\sum_{i=1}^n (x*f[b_i])\,b^{\,i}$$

---

## 4.9 What does this theory look like in real code, and how does it make implementations both faster and harder to mess up?

This is where the chapter stops being "math you nod at" and becomes something you can ship. The big idea is that the algebraic expressions for geometric operations (projection, normal handling, subspace transforms) translate almost directly into code—often with fewer special cases than coordinate methods. And if you care about speed, the same theory tells you exactly what you can precompute: outermorphism matrices per grade, built from basis images, so repeated transformations become fast linear algebra with the *right* semantics baked in.

**Key equation:**
$$P_B[x]=(x\,\lrcorner\,B)\,\lrcorner\,B^{-1}$$

---

## 4.9.1 How can you compute an orthogonal projection onto a plane using one clean algebraic expression instead of coordinate hacks?

Orthogonal projection is usually taught as coordinate formulas, dot products, or matrix pseudoinverses. Here it's one clean geometric expression: contract the vector into the blade, then contract back out with the inverse of that blade. The code mirrors the math almost literally—so you can read the implementation and know what it means geometrically. That's the real win: fewer moving parts, fewer opportunities to get the "which basis, which transpose" details wrong.

**Key equation:**
$$P_B[x]=(x\,\lrcorner\,B)\,\lrcorner\,B^{-1}$$

---

## 4.9.2 Why can a precomputed outermorphism matrix make the same operation dramatically faster, and what exactly is being cached?

If you're applying the *same* linear map a million times, you don't want to rebuild it from contractions and inverses every time. The outermorphism matrix representation is exactly the "compiled" version of $f$: you compute how $f$ acts on basis vectors once, and that determines the matrices for every grade (vectors, bivectors, etc.). What you're caching is the whole multilinear behavior of the wedge—so later you just call `apply_om(M, X)` and get the right transformed blade fast.

**Key equation:**
$$[[f]]^{\,j_1j_2}_{\,i_1i_2} = [[f]]^{\,j_2}_{\,i_2}[[f]]^{\,j_1}_{\,i_1} - [[f]]^{\,j_1}_{\,i_2}[[f]]^{\,j_2}_{\,i_1}$$

---

## 4.9.3 Under non-uniform scaling, why do normals transformed like ordinary vectors become wrong, and how does using 2-blades fix it cleanly?

Non-uniform scaling is the classic moment where normals betray you: if you transform a normal like an ordinary direction vector, it usually stops being perpendicular to the surface. The reason is now clean: a normal vector is a **dual** of a bivector (an attitude/plane element), so it must transform by the dual rule, involving determinant and inverse-adjoint—not by $f$. The clean fix is even better: don't store normals as fake vectors at all; store the surface attitude as a 2-blade, transform it by the outermorphism (simple!), then dualize back to a normal if you need one. The code example makes this painfully concrete: "badNormal" transforms the vector; "goodNormal" transforms the bivector and then dualizes—and only the latter stays orthogonal.

**Key equation:**
$$a\times b \longmapsto \det(f)\,\bar f^{-1}[a\times b]$$

or avoid it entirely via:

$$f[a\wedge b]=f[a]\wedge f[b]$$

>