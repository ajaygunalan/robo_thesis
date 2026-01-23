# cga ray tracer overview

A ray tracer takes a scene description (geometry + materials + lights + camera) and computes the image you'd see from the camera by simulating light transport in the most brute-force way that still feels structured: cast a ray, find the first hit, shade it, and if the material demands it, recurse with secondary rays. The chapter's angle is not "how to ray trace" in the abstract; it's how to do it while letting the *conformal model of Euclidean geometry* carry the geometric meaning all the way into executable C++.

## What this implementation includes (and intentionally excludes)

This is a complete-but-limited tracer:

* It renders still frames only (no animation system).
* Geometry is polygonal triangle meshes only (no curved primitives).
* No kinematic chains / articulated rigs.
* It supports texturing and bump mapping.
* Shading follows the standard OpenGL fixed-function style (ambient/diffuse/specular), but performed per intersection point rather than per vertex.
* It supports reflection and refraction (so rays recurse).
* The focus is *not* aggressive global optimization; the chapter keeps acceleration ideas "classical" rather than exotic.

## Why CGA helps, even when you care about speed

CGA's pitch here is semantic compression: points, lines, planes, spheres, and rigid motions have representations that make "the right formula" look like the thing it computes. Instead of moving between coordinate systems and bespoke intersection routines, you keep objects as geometric entities and write operations in terms of those entities.

The chapter also makes a blunt performance point: you don't have to pay for symbolic beauty if your implementation is smart. Many operations that look "algebra heavy" can compile down to cheap coordinate shuffles if your library (or code generator) knows the model's structure. One illustrative example is extracting a Euclidean direction from a CGA line using a contraction with $(\infty \wedge o)$; in a tuned implementation this can reduce to assembling a few stored coefficients rather than doing a full inner product evaluation. Likewise, dualization against basis elements (especially the pseudoscalar) can be implemented as deterministic coordinate manipulation rather than runtime algebra.

This chapter uses Gaigen 2 for CGA implementation and shows equations as C++-like code. The main "notation translation" quirks are:

* `.` is C++ member access (not an inner product).
* Because `.` is taken, the code uses `<<` for the inner product.
* It writes `no` for $o$ and `ni` for $\infty$.

## The real theme: elegance where it's free, specialization where it's not

CGA gives "natural" representations for everything in the scene, and the chapter starts from that ideal. But the tracer's hot paths (especially intersections and repeated attribute queries) force representational choices that anticipate the operations you'll do most often.

So the design stance becomes: stay inside the conformal framework so transformations and geometric relations stay coherent, but don't insist that every concept be stored in the most uniform, all-purpose blade if extracting what you need would dominate runtime. The chapter later quantifies this trade: a conformal implementation can be measurably slower than a pure 3D vector-space version (about 25% in their benchmark), while the gap to a 4D homogeneous-coordinate implementation is much smaller (under 5%).
