# angle from meet magnitude

Meet/join come with a shared scalar ambiguity ([[scalar ambiguity and attitude]]), so quantitative information appears only after you fix a normalization convention. The join is the natural place to do that: choose an oriented pseudoscalar $I$ for the join space and normalize your join $J$ relative to it. That choice pins down a consistent scaling for meets computed relative to $J$.

With that normalization in place, the magnitude of the meet becomes a measure of relative attitude. For normalized blades $A$ and $B$ inside a normalized join,
$$
\lvert A \cap B\rvert
$$
behaves like a sine of the relevant subspace angle: it is $1$ for orthogonal subspaces and decays continuously to $0$ as they become parallel.

One way to see the sine enter is to track what happens when you normalize the join. The join is proportional to a spanned volume blade like $A' \wedge B$, and normalizing it divides by a scalar that is the dualized magnitude of that spanned volume. Spanned volumes in the exterior algebra carry the familiar $\sin(\theta)$ factor measuring how non-parallel their arguments are, so the compensating rescale transfers that factor to the meet.

The sign of that “oriented sine” requires additional care: it depends on join orientation and may or may not flip under swapping the arguments. Keep those conventions separate in [[ordering and orientation sign]].
