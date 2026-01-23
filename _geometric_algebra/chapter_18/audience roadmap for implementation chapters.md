# Audience Roadmap for Implementation Chapters

The chapter doesn't pretend every reader needs every detail. It basically offers three reading modes, each tuned to a different kind of uncertainty.

## If you're new and GA still feels like magic

Start where the structure looks most familiar: go first to the chapter that treats a big chunk of GA as linear operators (the "this is consistent, not mystical" experience). After that, dip into the early basis-blade material to see how the primitive products behave on the basis. Then skim the remaining implementation material, but make sure you don't miss the benchmark section that compares GA performance to more traditional approaches—because that's where the "is this practical?" question gets answered most directly.

## If you want to use GA in a program (not implement it)

You care less about the lowest-level blade mechanics and more about what representation choices and operations will actually appear in your code. In that mode: read the linear implementation material carefully, skim the nonlinear and efficiency chapters for orientation, and then spend real time on the application chapter (the ray-tracing example) because it shows what "GA in production-style code" actually looks like—especially the decisions about what primitives represent what concepts.

## If you want to write an implementation (or you want every detail)

Read everything, in order, and don't skip the "how the sausage is made" parts. The whole point of the later chapters is that efficiency comes from respecting structure; you don't get that by only reading summaries.
