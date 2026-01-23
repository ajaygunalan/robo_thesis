# Outermorphisms, Nonlinear Algorithms, and Performance Benchmarks

A versor sandwiching action $X \mapsto V X \tilde{V}$ is not just "some nonlinear thing"; when restricted to the appropriate subspaces it induces an **outermorphism**—a linear map on blades that respects the outer product structure. The chapter uses this to motivate a practical performance tactic: if you apply the same transformation many times, it can be faster to compute a **matrix representation** of the outermorphism once and then apply that matrix repeatedly.

The tradeoff is amortization. Applying a rotor directly is already efficient when specialized, but building a matrix can make each subsequent point transform cheaper still, especially when the transformed object has a constant coordinate (common in homogeneous/conformal encodings). In the chapter's illustration, applying an outermorphism matrix to a flat homogeneous point becomes a straight affine-looking formula: dot products plus a constant term, with saved multiplies due to the constant coordinate. Whether this wins depends on (1) the cost to initialize the matrix, (2) how many times you'll apply it, and (3) how much cheaper matrix-application is than the versor path in your implementation.

## Specializing nonlinear algorithms

The chapter then asks a natural question: can the same specialization tricks accelerate the "nonlinear" routines from earlier implementation chapters (things like inverses, exponentials, classification, factorization)? The answer is "often yes," with one recurring condition: the generator must be able to keep intermediate variable types predictable—sometimes by unrolling loops.

- **Versor (and blade) inverse** is a small closed-form expression and is very amenable to specialization.
- **General multivector inverse** benefits partly: you can initialize the geometric product matrix more efficiently when many coordinates are known zero, but the overall return type can't be decided at generation time because it depends on the runtime matrix inversion outcome.
- **$\exp$, $\sin$, $\cos$ of multivectors** can be highly optimized if the generator can prove that $A^2$ is scalar for the specialized input type, enabling special-case closed forms; otherwise you need a runtime test ("is $A^2$ scalar?") to choose between special cases and generic series evaluation.
- **Multivector classification** and **blade factorization** can be optimized significantly once loops over basis vectors are unrolled so the generator can specialize each test; some runtime work remains for tasks that inherently depend on values (e.g., selecting the "largest" basis blade).
- **Meet and join** resist this approach because key intermediate types depend on the actual runtime values (e.g., delta products), forcing unavoidable conditional structure that specialization alone can't erase.

## Performance benchmarks

Finally, the chapter grounds all of this in benchmarks: multiple versions of a ray tracer were implemented using different models of 3D Euclidean geometry (some linear algebra, some GA, some with outermorphism matrices), and their rendering times were compared. The models listed include 3D linear algebra, 3D GA with rotors, 3D GA with outermorphism matrices, 4D homogeneous-coordinate-style approaches (LA and GA), and a 5D conformal GA version.

The reported results (relative to a 3D linear algebra baseline) show the intended narrative: specialized GA can match linear algebra performance closely, and the conformal model carries a modest overhead in this workload:

| Model | Relative time (vs 3D LA) |
|-------|-------------------------:|
| 3D LA | 1.00× |
| 3D GA with outermorphism matrices | 0.98× |
| 3D GA | 1.05× |
| 4D LA (homogeneous) | 1.22× |
| 4D GA (homogeneous) | 1.2× |
| 5D GA (conformal) | 1.26× |

## Takeaways

Two sober takeaways close the chapter. First, "conformal is slower" is not a law; it's a tradeoff that can be engineered down, and the chapter notes cases where conformal modeling even beat traditional methods in certain tasks. Second, specialization buys you speed and readability—your types look like geometry (line, circle, rotor) instead of "multivector everywhere"—but it costs you the ability to store arbitrary multivectors in those variables. The pragmatic stance is: keep the general multivector as a fallback, but don't let it dictate the performance profile of the whole program.
