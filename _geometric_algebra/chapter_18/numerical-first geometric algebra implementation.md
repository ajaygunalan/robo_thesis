# Numerical-First Geometric Algebra Implementation

A practical geometric algebra implementation is judged by what it does **at run time**. The chapter is explicit about the target: efficient **numerical** computation, not symbolic computer algebra. Any symbolic manipulation belongs on the "scaffolding" side of the boundary—use it to *bootstrap* an implementation (e.g., to help derive code or structure), then keep it out of the hot loop.

This philosophy shapes the whole presentation style of the implementation material:

- The goal is not to build a system that reasons about expressions; it's to build a system that evaluates multivector expressions reliably and quickly.
- The exposition aims to stay largely independent of any single library's internals, but it does point to a concrete "this is what efficiency looks like" reference: Gaigen 2, the engine behind the GA sandbox code used throughout the book's programming examples.
- To separate "clarity" from "performance," the authors also provide a separate reference implementation (in Java) intended for education and readability rather than computational intensity.

The upshot is a disciplined mental model: *symbolic work is an implementation aid, not an algorithmic dependency*.
