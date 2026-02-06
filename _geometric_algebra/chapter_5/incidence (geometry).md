# incidence (geometry)

In geometry, **incidence** is the relationship “lies in / passes through / is contained in.” Typical examples are “a point lies on a line,” “a line lies in a plane,” or “two planes share a line.”

Geometric algebra expresses incidence as *containment conditions* between blades (or between a blade and a vector/point representation). In direct form, a common pattern is:
$$
x\ \text{is incident to}\ A \quad\Longleftrightarrow\quad x\wedge A = 0,
$$
read as “$x$ lies in the subspace represented by $A$.” In dual form (after dualizing against an appropriate pseudoscalar for the relevant join space), incidence often becomes an inner-product-like condition, e.g. a point satisfying a hyperplane equation.

Chapter 5 introduces **incidence products** on blades that *construct* incidence outcomes rather than merely testing them:
- The **meet** $A\cap B$ returns the intersection subspace (“what is common?”).
- The **join** $A\cup B$ returns the span/union subspace (“what is the smallest space containing both?”).

These operations are geometrically faithful but nonlinear near degeneracy (output grade can jump), which is why the book restricts them to blades; see [[meet and join]] and [[piecewise linearity and degeneracy]].

related: [[meet and join]], [[meet from join]], [[piecewise linearity and degeneracy]].
