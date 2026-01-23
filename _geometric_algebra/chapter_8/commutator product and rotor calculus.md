# Commutator Product and Rotor Calculus

Differentiating geometry is easy to do badly: if you "perturb a blade" by adding an arbitrary multivector, you typically destroy the blade structure and therefore the geometric object. The rotor viewpoint fixes this. In geometric algebra, the meaningful infinitesimal change of an object is the one you get by applying an infinitesimal **orthogonal transformation**, i.e., a small rotor.

## The commutator product as "infinitesimal action"

A rotor acts by sandwiching:

$$
X \mapsto R X \tilde{R}, \qquad R = e^{-B/2}
$$

with bivector $B$ (the generator: plane + angle).

If you expand $e^{-B/2} X e^{B/2}$, the first-order term is always the same bilinear combination of $X$ and $B$. That motivates defining the **commutator product**

$$
X \times B \;\equiv\; \tfrac{1}{2}(XB - BX).
$$

(The book writes this with a small "x" to avoid confusing it with the 3D cross product.)

This is the exact object you want because it measures how noncommutativity drives change: when $XB = BX$, the commutator vanishes and the rotor has no first-order effect on $X$.

## Grade preservation: why bivectors are special

For general multivectors, the commutator need not preserve grade. But when the second argument is a **bivector**, it does:

$$
\mathrm{grade}(X \times B) = \mathrm{grade}(X) \quad \text{if } \mathrm{grade}(B) = 2.
$$

That's not a cosmetic property. It's the algebraic statement that infinitesimal rotations move a geometric object **within its type**: vectors stay vectors, bivectors stay bivectors, $k$-blades stay $k$-blades. Without this, even a first-order "Taylor term" would fall outside the object you meant to differentiate.

## Rotor Taylor series: exponentiating commutators

With the commutator product in place, rotor action becomes an iterated commutator series:

$$
e^{-B/2} X e^{B/2} = X + (X \times B) + \tfrac{1}{2}((X \times B) \times B) + \tfrac{1}{3!}(((X \times B) \times B) \times B) + \cdots
$$

This is the geometric-algebra analogue of "exponentiating a Lie algebra action": the rotor's finite motion is the exponential of its infinitesimal generator.

A *small* rotor $R \approx e^{-\delta B/2}$ gives the first-order perturbation rule:

$$
e^{-\delta B/2} X e^{\delta B/2} = X + (X \times \delta B) + O(\delta^2).
$$

So the correct notion of "$\delta X$" for geometric objects is **not** arbitrary addition; it is

$$
\delta X = X \times \delta B
$$

for some small bivector $\delta B$.

## Lie algebra in one line: commutators of motions are motions

Successive infinitesimal rotor actions add at first order, but their noncommutativity shows up at second order. If you apply a small $A$-rotation, then a small $B$-rotation, and then undo them in the opposite order, the net effect is (to lowest nontrivial order) another rotor-like change whose generator is the bivector commutator $A \times B$.

This is the Lie bracket story of continuous transformation groups, but in GA it's brutally concrete: **bivectors are closed under the commutator product**, so you can generate new infinitesimal motions by commuting old ones.

A vivid 3D example: let

$$
A = e_1 \wedge e_2, \quad B = e_2 \wedge e_3.
$$

Then $A \times B = -e_3 \wedge e_1$. Two rotation planes generate the third via a commutator maneuver. (By contrast, translations commute, so commutators don't create "new translation directions.")

The practical punchline is that rotor calculus turns "differentiate motion" into "compute commutators," and turns controllability questions into "what bivector directions can my commutators span?"
