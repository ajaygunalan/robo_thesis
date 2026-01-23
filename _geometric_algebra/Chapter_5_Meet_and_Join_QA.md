# Chapter 5: Meet and Join (Intersection & Union) — Q&A

---

## 5: How can one algebraic idea handle intersections/unions cleanly enough to later hit offset lines, planes, circles, and spheres without case-by-case hacks?

You read this because "where do these things intersect?" is the question that keeps coming back in every geometry problem—and GA gives you a single language for it, even when the answer changes type (line vs plane) as the configuration changes. The catch is that intersection/union can't be a neat bilinear product, so the chapter builds a tool that's honest about that mess while still letting you compute reliably. The whole story is captured by the idea that intersection and union are two sides of the same outer-product factorization:

$$A = A' \wedge M,\qquad B = M \wedge B',\qquad J = A\cup B = A'\wedge M\wedge B',\qquad M = A\cap B$$

Once you internalize that "common factor" viewpoint, later chapters can reuse it to intersect not just subspaces through the origin, but offset lines/planes—and even circles and spheres—without reinventing a new ad-hoc formula every time.

---

## 5.1: Why does "intersection" sometimes spit out a line and other times a plane for almost-the-same inputs—and what does that reveal about why it can't be linear?

You read this because it explains the one annoying fact you can't ignore: "intersection" is discontinuous when geometry becomes degenerate. Two planes through the origin usually intersect in a line (grade drops), but if they coincide you want the intersection to be the plane itself (grade doesn't drop). No linear or bilinear product can flip grades like that smoothly—so meet/join must be nonlinear, and they must be restricted to blades (true subspaces), not arbitrary multivectors.

The section also warns you not to over-trust magnitude and sign: the intersection subspace is meaningful, but its scale/orientation isn't uniquely determined from the inputs (Figure 5.1 shows you can "reshape" the same blades and suggest different intersection magnitudes). A key practical escape hatch is that many geometric uses are scale-invariant anyway, e.g. projecting onto the meet subspace:

$$\text{proj}_M(x)= (x\,\lrcorner\, M^{-1})\,\lrcorner\, M$$

which doesn't care if you rescale $M$ because $M$ and $M^{-1}$ change together.

---

## 5.2: What do you gain by redefining intersection and union as "greatest common outer factor" and "least common outer multiple" of blades?

You read this because it gives you a definition of "intersection" and "union" that actually generalizes: meet is the greatest common outer factor, join is the least common outer multiple. That sounds abstract, but it's exactly what you want in high dimensions: "what do these subspaces share?" becomes "what blade $M$ divides both $A$ and $B$ under $\wedge$?" and "what's the smallest space containing both?" becomes the join $J$.

**Key equation — the ordered factorization:**
$$A = A' \wedge M,\qquad B = M \wedge B'$$

**Resulting relationship:**
$$A\cup B = A' \wedge M \wedge B',\qquad A\cap B = M$$

This also explains the weird-but-okay ambiguity: you can trade any scalar factor between $M$ and $J$ (multiply $M$ by $\gamma$, and $J$ scales by $1/\gamma$), and most geometric computations won't break because they use only attitudes or scale-invariant combinations.

---

## 5.3: If meet/join come from a messy factorization, how do you turn them into concrete contraction/duality formulas you can actually compute with (and not screw up the signs)?

You read this because "meet/join are defined by factorization" is conceptually nice but useless until you can compute them without guessing the factors. This section shows how to extract the "non-common parts" $A'$ and $B'$ using contractions with $M^{-1}$, carefully ordered so normalization works:

$$B' = M^{-1}\,\lrcorner\, B,\qquad A' = A\,\llcorner\, M^{-1}$$

Then it hands you the workhorse formula you'll actually use in applications: once you know (or choose) the join $J$, you can compute the meet directly by

$$M = A\cap B = (B\,\lrcorner\, J^{-1})\,\lrcorner\, A$$

Even better, the dual form tells you the structure: relative to the join space, the *dual meet* is just an outer product of duals,

$$M\,\lrcorner\, J^{-1} = (B\,\lrcorner\, J^{-1}) \wedge (A\,\lrcorner\, J^{-1})$$

which is why meet/join feel like "wedge, but with the right duality."

---

## 5.4: Can you compute a plane–plane intersection the GA way and see the classical cross product drop out as a special case—while also extracting a meaningful angle/sine from the result?

You read this because it turns meet/join from "definitions" into "I can compute this intersection today," and it shows you that classical 3D tricks are just special cases. In many real problems you already know the ambient space containing both objects (that ambient pseudoscalar *is* the join), so you can plug into the contraction formula and get the intersection blade immediately. The chapter's plane–plane example takes $J=I_3$ and computes $A\cap B$ as a line; the magnitude carries a sine-of-angle meaning, so you get both the intersection *and* a quantitative angle measure "for free."

The payoff is that the familiar cross product drops out as a special case of the same machinery. In 3D, with plane normals as dual vectors, you recover:

$$A^*\times B^* = (A^*\wedge B^*)^* = A\cap B$$

so meet/join aren't some exotic GA add-on—they're the dimension-agnostic version of what you were already doing, except they keep working when the grades and dimensions change.

---

## 5.5: When do meet/join behave nicely (almost linear), and how do you recognize the exact moment degeneracy forces a different join so your computation doesn't silently lie?

You read this because it tells you how to use meet/join without getting blindsided: they behave "nicely" (linearly) as long as you don't cross a degeneracy where the correct join changes. Once a join $J$ is fixed, the meet formula

$$M = (B\,\lrcorner\, J^{-1})\,\lrcorner\, A$$

is linear in $A$ and $B$ because contractions are linear. That's why meet feels stable most of the time. The nonlinearity only shows up when geometry forces a different join—like when a line approaches lying inside a plane, or two planes approach coincidence—and then the correct "ambient space" of the problem collapses.

The section also gives you a brutally practical diagnostic: **if your computed meet (with your chosen join) returns zero, you've hit degeneracy and you must pick another join.** The line–plane example makes this concrete: in general position in 3D with $J=I_3$,

$$M = a\cap B = (B\,\lrcorner\, I_3^{-1})\,\lrcorner\, a = B^*\cdot a$$

a scalar that changes smoothly and whose sign has geometric meaning. But when the line becomes contained in the plane, that expression hits zero, signaling "wrong join"; switching to the plane's pseudoscalar $I_2$ gives a meet that is a *line* (weighted), not a scalar.

---

## 5.6: Why does the magnitude of the meet encode a sine-based "distance" between subspaces—and how can that become a practical measure of "how parallel/orthogonal are these spaces"?

You read this because it answers the question "is meet just symbolic, or does it measure something?"—and the answer is: it measures *distance between subspaces* in the most useful way. If you normalize the join (choose the unit pseudoscalar of the space spanned by $A$ and $B$), then the meet's magnitude becomes a sine-based separation measure: it's $1$ when the subspaces are orthogonal and slides down to $0$ as they become parallel. That's exactly the kind of stable "how close to degenerate are we?" quantity you want in geometry and numerical work.

The section also forces you to get serious about signs: meet may be symmetric or antisymmetric depending on grades, because swapping arguments flips an outer product of duals. The key rule is

$$B\cap A = (-1)^{(j-a)(j-b)} (A\cap B)$$

where $a,b$ are grades of $A,B$ and $j$ is the join grade. That's why two lines through the origin in a plane (measuring an oriented angle) give an antisymmetric meet, while a line–plane meet in 3D can be symmetric even though a sign still encodes "front vs back" piercing.

---

## 5.7: How can meet/join commute with any invertible linear transformation even though they're not bilinear—and what does that say about them being fundamentally nonmetric?

You read this because it resolves an apparent contradiction that matters in applications: meet/join are nonlinear, yet they behave perfectly under invertible linear maps. The reason is structural: meet and join are defined by outer-product containment relationships, and any invertible linear transformation (as an outermorphism) preserves those containments. So you get the clean invariances

$$f[A\cup B] = f[A]\cup f[B],\qquad f[A\cap B] = f[A]\cap f[B]$$

That's huge: it means meet/join are *geometric* in the best sense—they're not artifacts of coordinates or a particular basis.

The subtle but critical computational warning is that when you implement the meet via contractions, you must dualize relative to the *transformed join* $f[J]$, not the original $J$:

$$f[A\cap B] = (f[B]\,\lrcorner\, f[J]^{-1})\,\lrcorner\, f[A]$$

This is also why meet/join are fundamentally nonmetric: even though contractions look metric-dependent, the dependence cancels out in the full construction, so you can temporarily assume a Euclidean metric to make inverses exist and simplify computation.

---

## 5.8: What new power do you get once subspaces don't have to pass through the origin—like getting a finite result for parallel/skew lines and intersections of spheres/circles later?

You read this because "subspaces through the origin" are the toy problem; real geometry is offset, parallel, and skew. This section tells you the chapter's machinery is laying track for the payoff: once you represent offset lines/planes correctly (in the homogeneous model, later), meet stops doing the annoying thing where parallel objects "don't intersect" and instead gives meaningful finite results—parallel lines get a finite meet, and skew lines meet in a scalar proportional to their shortest Euclidean distance. Even more, the conformal model later lets you intersect spheres and circles using the same subspace meet rules, which is the kind of unification that saves you from memorizing a zoo of special-case formulas.

The key point is that the *same* meet computation survives; it's the representation of the objects that changes. In other words, once your objects live as blades in the right model, you're still doing:

$$M = A\cap B = (B\,\lrcorner\, J^{-1})\,\lrcorner\, A$$

but now $A,B$ can encode offset lines/planes (and later circles/spheres), so "intersection" becomes a uniform algebraic operation instead of a geometry cookbook.

---

## 5.9: Why is the literature such a minefield for "meet/join," and how do you avoid learning the wrong operation just because an author uses the same words?

You read this because if you learn meet/join from the wrong source, you will confidently compute the wrong thing—especially in degenerate cases—while thinking you're doing "standard GA." The literature splits: some authors avoid meet/join because they're nonlinear; others "fix" that by redefining join as the outer product and meet via duality, producing the linear *regressive product*. That linearized version is elegant on paper but can fail exactly where you most need incidence geometry (it tends to return zero in degeneracies).

The key equation that exposes the fork-in-the-road is the dual meet identity:

$$(A\cap B)^* = B^*\wedge A^*$$

with the crucial caveat that the dual $(\cdot)^*$ here is relative to the join subspace, not the full-space pseudoscalar. This section also points you to approaches that treat meet/join as projection operators to handle weight/orientation ambiguity more naturally, and it warns about inner-product conventions (contraction vs other "inner products") that can create fake exceptions with scalars and pseudoscalars.

---

## 5.10: What core instincts do the exercises force you to build so meet/join stops feeling like wizardry and starts feeling mechanically predictable?

You read this because meet/join only become trustworthy once you can *predict* them and manipulate them, not just apply a formula and hope. The exercises force you to confront the two real pain points: (1) how grades/signs change under degeneracy, and (2) how to algebraically relate $A,B$ to $M,J$ without losing track of normalization and duality. If you can do these exercises, you stop fearing meet/join—and you stop getting surprised by zero results and sign flips.

A centerpiece is the "general factorization" pattern that shows up constantly in hand-derivations:

$$(A\wedge B)\cap(A\wedge C) = A\,(A\wedge B\wedge C)^*$$

under the assumption that $A,B,C$ share no common factors. That one formula is basically a template: it tells you how a shared subspace pulls out of an intersection and how the remaining "angle/volume" information sits in a dual.

---

## 5.10.1: Can you, on simple blades, predict exactly what meet/join should output—and watch how tiny perturbations trigger grade flips and degeneracy?

You read this because the drills are where the abstract talk turns into muscle memory: you'll see, on the simplest blades, exactly how meet/join encode "union vs intersection," and you'll see degeneracy *happen* when you nudge an input by a tiny amount. That's not a side detail—it's the whole reason meet/join aren't bilinear, and the drills make you comfortable with that reality instead of treating it as a mysterious exception.

The core computational move you keep exercising is: pick/know a join, then compute the meet by contraction,

$$M = A\cap B = (B\,\lrcorner\, J^{-1})\,\lrcorner\, A$$

On tiny examples this becomes intuitive: swapping two lines through the origin in a plane should flip the sign (you're measuring the opposite oriented angle), and perturbing something like $e_2$ into $e_2+10^{-5}e_3$ is exactly the kind of "almost degenerate" case that will force you to notice when the join you assumed stops being the right one.

---

## 5.10.2: Do you understand the structure well enough to prove the reciprocal identities and spot the subtle wrong step in a convincing-but-broken proof?

You read this because it's where you learn to *trust* meet/join by proving the internal consistency yourself—and by learning what the common wrong proofs look like. The reciprocal identities tie together the four protagonists $(A,B,J,M)$ in a way that's easy to use as an algebraic checksum when you're doing derivations or debugging implementations. One of those key identities is:

$$(B\,\lrcorner\, J^{-1}) * (A\,\llcorner\, M^{-1}) = 1$$

and proving it forces you to track grades, ordering, and the role of inverses correctly rather than handwaving "duality makes it work."

The "find the error" exercise is equally valuable because it targets a real trap: assuming inverses and transforms commute the way you wish they did. The bogus step is essentially treating the inverse join as if it transformed by a simple pushforward/pullback identity; the chapter's correct transformation discussion (Section 5.7) makes clear you must transform the join itself and then invert, because dualization is relative to the join subspace, not an absolute object you can carry through $f$ naively.

---

## 5.11: What breaks (or slows to a crawl) when you take meet/join out of the textbook and into real code with real types, real performance limits, and real floating point?

You read this because meet/join are where elegant algebra meets ugly reality: variable grades, degeneracies, runtime cost, and floating point thresholds. The math definition ("outer factorization") is not how most code computes it; practical implementations use specialized algorithms that first decide an output grade (which is exactly where degeneracy causes trouble) and then do a factorization-like procedure. That means meet/join are the first place where your GA code can be both slow and numerically sensitive even if the rest of your algebra is clean.

Underneath, you're still trying to realize the same mathematical object:

$$M = A\cap B = (B\,\lrcorner\, J^{-1})\,\lrcorner\, A,\qquad J=A\cup B$$

but the programming sections show you what changes when $A,B$ don't have fixed types (so you use a generic multivector class), when you want interactivity, and when "almost degenerate" inputs are common rather than rare.

---

## 5.11.1: What do you notice—and what misconceptions die—when you can interactively drag two elements around and watch meet/join jump grades in real time?

You read this because seeing meet/join *move* as you drag inputs around teaches you faster than any static derivation. The example intentionally uses a generic multivector type because neither inputs nor outputs have fixed grade, and it makes the operation tangible: you're literally watching the incidence object (meet or join) update as geometry changes, including the moment it "jumps" when degeneracy flips the expected grade. The core of the example is exactly:

$$X=\texttt{meet}(M_1,M_2)\quad\text{or}\quad X=\texttt{join}(M_1,M_2)$$

depending on what you choose to draw.

It also sneaks in a practical trick: rounding coordinates to coarse steps (multiples of 0.2) makes it easier to *hit* degenerate configurations like parallel vectors on purpose. That's not cosmetic—degeneracies are where the operation's nonlinearity lives, so an interactive tool that helps you explore them is basically a laboratory for building the right intuition.

---

## 5.11.2: Are meet/join so expensive that they'll dominate your runtime, and when should you replace them with a cheaper formula because you already know the relative geometry?

You read this because it tells you the blunt truth: meet/join can be computationally expensive enough to dominate your runtime, so you need to know when not to use them. The benchmark in Gaigen 2 compares a million outer products to a million joins and finds join is roughly two orders of magnitude slower in that setup, for concrete reasons: join/meet require a specialized factorization algorithm and often run through a generic "mv" type with coordinate compression, while ordinary products are straight-line coordinate arithmetic.

The key takeaway is that if you already know the "ambient" subspace and you're in a nondegenerate situation, you can often replace a meet with a much cheaper specialized formula. In the chapter's own words (in the line–plane setting), use the dual normal and a contraction/dot instead of a full meet/join pipeline:

$$M = a\cap B = B^*\cdot a \quad\text{(with } B^*=B\,\lrcorner\, I_3^{-1}\text{)}$$

That's the difference between elegant generality and fast production code.

---

## 5.11.3: How do floating-point thresholds decide when "nearly parallel" becomes "parallel enough" to flip the output grade—and how can you pinpoint the exact epsilon where that flip happens?

You read this because numerical degeneracy is not a philosophical issue—it's a branch in your code. The meet/join algorithm has to decide "what grade should the result be?" and it does that by comparing a condition number to a small threshold. Near-parallel or near-coincident inputs sit right on that knife edge, so tiny floating point differences can make the algorithm flip-flop between "it's a vector" and "it's a bivector," changing the entire meaning of the output.

The example makes this painfully explicit by probing when the join of two almost-parallel vectors changes grade:

$$a=e_1,\qquad b=e_1+\varepsilon e_2,\qquad X = a\cup b = e_1\cup(e_1+\varepsilon e_2)$$

Starting from $\varepsilon=10^{-10}$ and increasing, it detects the point where $X$ stops being treated as a vector and becomes a 2-blade; the flip happens around $10^{-7}$ because the implementation uses an epsilon of $10^{-7}$. In other words: your "geometry" is only as stable as your numerical thresholding policy.
