# inverse via pseudoscalar

The pseudoscalar provides a coordinate-free formula for $f^{-1}$ when $f$ is invertible (equivalently, $\det(f)\neq 0$). Fix an oriented unit [[pseudoscalar]] $I_n$ and use duality as defined in [[duality and orthogonality]]. The [[adjoint|contraction transformation law]] then controls how duality interacts with $f$. Combining these gives
$$
f^{-1}[A] = \frac{\bar{f}\left[A \lrcorner I_n^{-1}\right] \lrcorner I_n}{\det(f)}.
$$
Read this as a sequence. Contract $A$ with $I_n^{-1}$ to reach complementary grade, apply the adjoint $\bar f$, contract with $I_n$ to return to the original grade, then divide by the [[determinant]]. The geometric meaning of dualization itself lives in [[duality and orthogonality]].

An equivalent dual form is often easier to remember:
$$
(f^{-1}[A])^* = \frac{\bar{f}[A^*]}{\det(f)}.
$$
In words, the dual of the inverse is the adjoint applied to the dual, normalized by $\det(f)$.

The formula passes basic sanity checks. Applying it to the pseudoscalar gives $f^{-1}[I_n] = I_n / \det(f)$, confirming that $\det(f^{-1}) = 1/\det(f)$. Applying it to a scalar returns the scalar unchanged, as any outermorphism should. On vectors, the formula reproduces the classical adjugate-over-determinant construction.
