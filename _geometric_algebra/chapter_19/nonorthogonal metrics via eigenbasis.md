# nonorthogonal metrics via eigenbasis

Bitmap "XOR-and-sign" multiplication relies on orthogonality: the clean behavior that distinct basis vectors anticommute and repeated ones collapse via a diagonal $e_i^2=m_i$. In many geometric algebra models you deliberately work in nonorthonormal bases where the metric matrix has off-diagonal entries. The conformal model is a canonical example: including basis vectors often denoted $o$ and $\infty$ yields a non-diagonal multiplication table (so $o\cdot\infty$ is nonzero).

Rather than designing a brand-new basis-blade product algorithm for each nonorthogonal metric, the chapter uses a linear-algebra escape hatch: if the metric matrix is symmetric (as it is for standard bilinear forms in geometric algebra), then by the spectral theorem it can be orthogonally diagonalized. Concretely, there exists an orthonormal eigenbasis in which the metric becomes diagonal.

That yields a general algorithm for geometric products under arbitrary symmetric metrics:

1. **Precompute** the eigenvectors and eigenvalues of the metric matrix once, when the metric is initialized.
2. **Change basis**: express the operands in the eigenbasis coordinates.
3. **Multiply** using the orthogonal-metric blade product machinery, with the eigenvalues providing the diagonal metric coefficients.
4. **Change basis back** to express the result in the original (possibly nonorthogonal) basis.

For the conformal-style $o,\infty$ pair, one convenient orthogonalizing change is to take linear combinations like
$$f_4=\frac{\sqrt{2}}{2}(o-\infty),\qquad f_5=\frac{\sqrt{2}}{2}(o+\infty),$$
so that the new basis vectors have diagonal squared norms (one positive, one negative), placing you back in the "diagonal metric" world that orthogonal multiplication handles well.

Two implementation consequences matter:

* **You don't want to do this at runtime for every product.** Practical implementations precompute the geometric products of basis blades ahead of time (effectively a multiplication table), so the expensive eigenbasis machinery is paid once, not per multiply.
* **A product may no longer be a single basis blade in the original basis.** Basis changes can turn a blade in one basis into a *sum* of blades in another; so after you transform back, the product of two basis blades can become a multivector. A classic conformal-flavored example is:
  $$o \cdot \infty = -1 + o\wedge \infty,$$
  which already shows a scalar part and a bivector part appearing together.

So, the bitmap basis-blade engine remains the computational core, but nonorthogonal metrics force you to wrap it in "change basis → multiply → change basis back," and to accept that "basis blade in" does not always mean "basis blade out."
