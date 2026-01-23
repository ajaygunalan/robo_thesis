# Exponential and Scaling for Multivectors

Exponentials (and related trig functions) are the workhorses behind continuous motions in geometric algebra: rotors, motors, and other versors often come from $e^A$ for some generator $A$. The computational story splits cleanly into (1) cases where $A^2$ is scalar (easy) and (2) cases where it isn't (series + numerical care).

## The Baseline: Power Series

The exponential is defined by the usual series:
$$
\exp(A)=1+\frac{A}{1!}+\frac{A^2}{2!}+\cdots
$$

This is always valid, but not always efficient or numerically pleasant.

## The "Scalar Square" Shortcut

If $A^2$ is a scalar, the series collapses to closed forms. Let $\alpha$ be a real scalar such that $A^2\in\{-\alpha^2,0,+\alpha^2\}$. Then:
$$
\exp(A)=
\begin{cases}
\cos\alpha+\dfrac{A}{\alpha}\sin\alpha & \text{if } A^2=-\alpha^2,\\
1+A & \text{if } A^2=0,\\
\cosh\alpha+\dfrac{A}{\alpha}\sinh\alpha & \text{if } A^2=\alpha^2.
\end{cases}
$$

This covers blades and versors in many practical cases, because their squares are scalar.

## The Hard Case: $A^2$ Not Scalar

General bivectors (especially in dimension $\ge 4$) need not be 2-blades, and in conformal GA the bivectors that generate rigid body motions are often not blades. Then you typically evaluate the series explicitly and truncate.

A practical numerical rule from experience: truncating at about **order 10–12** tends to be the sweet spot for 64-bit doubles—beyond that, you often just accumulate floating-point noise rather than accuracy.

## Rescaling to Avoid Overflow and Improve Accuracy

When $|A|$ is large, early terms $A^k/k!$ can overflow or dominate before the series settles. The fix is to scale $A$ closer to unity:
$$
\exp(A)=\left(\exp\left(\frac{A}{s}\right)\right)^s.
$$

In implementation, choose $s$ as a **power of two** (say $s=2^m$) with $s\approx |A|$. Then:

1. Compute $E=\exp(A/s)$ via the truncated series (now stable because $A/s$ is small).
2. Compute $E^s$ by **repeated squaring**: square $m$ times to raise to $2^m$.

This both reduces overflow risk and typically improves final accuracy for large inputs.

## A Note on Logarithms of Versors

There is no general "logarithm of an arbitrary versor" algorithm in this chapter's scope. What exists instead are **closed-form logs for important subclasses** (e.g., rotations and various rigid body motion versors), with implementations available in reference codebases rather than as a single universal routine.
