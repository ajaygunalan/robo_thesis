# geometric differentiation

Geometric algebra lets you talk about "change" without immediately collapsing into coordinates, but it also forces you to be honest about what kinds of changes preserve meaning. A blade isn't "just a vector with extra components"; it encodes a subspace. If you perturb it by arbitrary addition, you can easily fall out of the space of blades and lose the geometric object you thought you were tracking. The chapter's first move is therefore philosophical-but-technical: **treat small changes as infinitesimal orthogonal transformations** (rotor-generated), not as naive additive noise.

That decision makes the commutator algebra the natural language of motion. Once you package infinitesimal rotor action into a single grade-preserving product, you get a clean Taylor series for sandwiching and a direct bridge to Lie algebra. That whole mechanism lives in [[commutator product and rotor calculus]]: it's where "differentiate a motion" becomes "compute a commutator."

With that in place, the chapter can ask sharper sensitivity questions than "how does X change?":

* what happens when the *thing being transformed* changes, and
* what happens when the *transformer* changes?

Those are not the same, and the difference matters in real geometry problems (like optics). The bookkeeping for "error bivectors" and how they conjugate or morph under versor changes is the point of [[versor perturbation propagation]].

Only after transformational change is under control does the chapter pivot to the more classical notion of parameter dependence: functions of a scalar parameter, then functions of a vector, and finally functions of general multivectors. The key is that some derivatives are scalar operators (they commute) while others are themselves geometric elements and must be multiplied with the full geometric product. The scalar "move in direction $\mathbf{a}$" operator is the clean entry point; see [[directional derivative in geometric algebra]]. It's where geometric algebra starts to disagree with "pattern-matched" real calculus in instructive ways (e.g., differentiating inversion).

From there, the chapter rebuilds the familiar $\nabla$ operator in a way that keeps grades and products honest. The vector derivative is a *geometric* operator: when you multiply it into a field, it naturally splits into divergence-like and curl-like pieces via inner/outer product decomposition. The operator rules (especially the product and chain rules in a noncommutative algebra) are the heart of [[vector derivative and geometric gradient]].

Finally, the same construction lifts to derivatives with respect to multivectors. This isn't just "more general" for its own sake; it's what makes rotor estimation and geometric optimization feel native rather than bolted-on. The chapter's capstone example—deriving the optimality condition for Wahba/Procrustes-style rotor fitting—sits in [[multivector derivative and rotor optimization]].

Two worked applications anchor the abstractions back to geometry: curvature of a planar curve (where wedge/dual expressions expose exactly what curvature depends on) and sensitivity of reflection under mirror tilt (where the "twice the angle" folklore becomes a clean bivector computation). The curvature story is kept self-contained in [[planar curvature via wedge and dual]], while the mirror story lives with versor sensitivity because that's what it really is.
