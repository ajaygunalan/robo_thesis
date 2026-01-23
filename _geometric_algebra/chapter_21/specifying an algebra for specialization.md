# Specifying an Algebra for Specialization

Specialization needs a source of truth: a compact description of "which geometric algebra am I working in, and which parts of it does my program actually use?" The chapter treats the **algebra specification** as the starting point for code generation.

At minimum, the specification must pin down four things.

## Dimension and basis naming

You specify the algebra's dimension $n$ (for $G(\mathbb{R}^n)$). You also specify a basis for $\mathbb{R}^n$—not necessarily orthonormal—and you're allowed to name basis vectors in a way that makes generated code readable. This matters because GA notation isn't universally standardized, so tooling should adapt to the names that make sense in your domain.

## Metric, including non-diagonal forms

Even though any metric can be represented in diagonal form in some basis, the chapter argues you often *don't want* that basis. In some models the "intuitive" basis is off-diagonal and can be more efficient because it lines up with which coordinates are actually distinct and needed. The conformal model example is the most concrete: the null vectors $o$ and $\infty$ are more fundamental for many constructions than alternative basis choices, and using an $o, \infty$-centric basis reduces redundancy.

The chapter illustrates this with a conformal line written in two different bases. Using an $o, \infty$-friendly basis, a line can be represented with six independent coordinates, schematically:

$$
A = A_{1o\infty} e_{1o\infty} + A_{2o\infty} e_{2o\infty} + A_{3o\infty} e_{3o\infty} + A_{12\infty} e_{12\infty} + A_{13\infty} e_{13\infty} + A_{23\infty} e_{23\infty}.
$$

In a different conformal basis (the chapter contrasts it with an $e, \bar{e}$-style choice), the same line representation expands to nine stored coordinates, with three duplicated equalities among them—so you pay extra storage and processing for information that isn't actually independent.

## Specialized types

You define the domain-specific multivector types your program will use (vector, rotor, point, line, circle, …) by listing which basis blades they contain. The chapter also suggests tagging whether a type is intended to be a blade or a versor, enabling optional runtime validity checks in debug builds. Beyond that, the spec can optionally mark some coordinates as constant (so they need not be stored) and can specify coordinate ordering (useful when interoperating with external libraries that expect a specific layout).

## Constants

Programs repeatedly use fixed multivectors like basis vectors or the pseudoscalar $I$. The chapter's view is that these should be part of the spec and generated as special constant types that mostly act as symbolic tokens—so the generator (or compiler) can optimize away their use inside expressions instead of treating them as runtime data.

---

The end result of a good specification is more than speed: it also improves code meaning. Instead of every variable being "multivector," your program can say "line" or "tangentVector," making the geometry explicit. The tradeoff is obvious: specialized types reduce the ability to shove arbitrary multivectors into any variable, so you keep general multivectors as an escape hatch when you need flexibility.
