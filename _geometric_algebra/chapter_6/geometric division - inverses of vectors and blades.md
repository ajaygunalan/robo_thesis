# Geometric division: inverses of vectors and blades

"Invertible product" becomes concrete the moment you define inverses. For a non-null vector $a$,

$$
a^{-1} = \frac{a}{a \cdot a} = \frac{a}{|a|^2},
$$

since $aa = a \cdot a$ is scalar and $a \wedge a = 0$. Null vectors (zero norm in the metric) have no inverse. Associativity matters here: it guarantees the inverse is unique, so "division by $a$" isn't an arbitrary convention.

For blades, the analogous fact is that an invertible blade has a scalar "squared norm" when you pair it with its reverse. If $A$ is a non-null blade, its inverse is

$$
A^{-1} = \frac{\tilde{A}}{A \ast \tilde{A}} = \frac{\tilde{A}}{|A|^2},
$$

where $\tilde{A}$ is reversal and $\ast$ is the scalar product. The idea is simple: $A\tilde{A}$ collapses to a scalar for blades, so division is unambiguous because scalars commute with everything.

Division inherits noncommutativity: right-division and left-division are different operations unless you're dividing by scalars. That "annoyance" is the source of new geometry: swapping the side you divide on flips signs of certain components, and that is exactly what turns decomposition into reflection (the next concept note).

Versors are flagged here as the other main class of invertible multivectors: anything that is a product of invertible vectors is automatically invertible, with inverse given by reversing the factor order and inverting each factor. This is the bridge to Chapter 7's operator machinery.
