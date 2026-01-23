# Recovering subspace products from the geometric product

Once the geometric product is primitive, "other products" are best treated as projections of it—either by symmetry tricks or by grade selection. The symmetry route is most transparent when one factor is a vector $a$ and the other is a blade $B$. Using grade involution ($\hat{B} = (-1)^{\mathrm{grade}(B)} B$), the wedge and left contraction appear as the half-sum and half-difference:

$$
a \wedge B = \tfrac{1}{2}(aB + \hat{B} a), \qquad
a \rfloor B = \tfrac{1}{2}(aB - \hat{B} a),
$$

with analogous formulas for $B \wedge a$ and $B \lfloor a$. These identities let you *rewrite* products by swapping order at the cost of a correction term, which is the practical algebra you actually use when simplifying expressions.

The grade-selection route is cleaner as a full definition for arbitrary blades. With $\langle \cdot \rangle_k$ the grade-k part,

$$
a \cdot b = \langle ab \rangle_0, \quad a \wedge b = \langle ab \rangle_2,
$$

and more generally for k- and l-blades,

$$
A_k \wedge B_l = \langle A_k B_l \rangle_{k+l}, \qquad
A_k \rfloor B_l = \langle A_k B_l \rangle_{l-k}, \qquad
A_k \lfloor B_l = \langle A_k B_l \rangle_{k-l},
$$

with the scalar product as $\langle AB \rangle_0$. This route is complete (it defines all cases), and it suggests an implementation strategy: implement just geometric product + grade projection, then derive everything else mechanically.

A small but important computational perk drops out: the scalar part is cyclic in the sense $\langle AB \rangle_0 = \langle BA \rangle_0$, a reordering rule that often "unlocks" simplifications when you only care about scalars (norms, determinants, invariants).
