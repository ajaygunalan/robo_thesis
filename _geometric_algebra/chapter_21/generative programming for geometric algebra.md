# Generative Programming for Geometric Algebra

If efficient GA code requires specializing types, hard-coding metrics, and emitting hand-tuned arithmetic for many combinations of inputs, you immediately face a practical problem: doing this manually scales like a combinatorial explosion. The chapter's answer is generative programming: write software that **synthesizes** the GA implementation you need from a higher-level specification.

The important shift is psychological: geometric algebra stops being "a library you call" and becomes "a high-level language you compile." You express geometry cleanly (coordinate-free), and a generator converts those expressions into coordinate-level code that a CPU can execute directly—without you ever writing error-prone coordinate manipulation by hand.

Where can this transformation happen in the path from your source code to a running executable? The chapter highlights three natural insertion points:

1. **Before compilation (offline code generation).** A separate generator produces source code for the algebra implementation, which you then compile and link like any other library. This is the classic "lex/yacc style" workflow; GA code generators like Gaigen and Gaigen 2 are described as taking this approach. The main downside is integration friction (a separate tool step) and the possibility of extra passes if you want feedback from profiling.

2. **At compile time (meta-programming).** If the language supports it, you can structure the implementation so the compiler itself generates specialized code. In C++, templates can be used this way; the chapter points out integration benefits but also practical pain: template syntax complexity, painful compiler errors, and long compile times.

3. **At run time (JIT-style generation).** Delay code generation until the program runs, generating specialized code the first time you need it. This can adapt to actual input patterns and the specific hardware it runs on, but costs startup time and is unconventional and hard to implement; the chapter notes it wasn't aware of a GA implementation using this at the time of writing.

The chapter's bigger point is that the *idea* is independent of which point you choose: call it a "code generator" either way. The generator's job is to transform "algebra + type structure + high-level function definitions" into an implementation that avoids generic overhead and matches the performance profile of traditional hand-optimized geometry code.
