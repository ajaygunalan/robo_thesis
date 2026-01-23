# reflection refraction and shading

Once you have the closest intersection point of a ray with the scene, the rest of rendering is "what color leaves this surface toward the camera along the ray direction?" The chapter keeps shading mostly classical, but uses CGA where it makes direction updates (reflection/refraction) and geometric checks (visibility to lights) clean and direct.

## Reflection as a conformal sandwich

In the conformal model, reflecting one geometric object in another is a sandwich product, with sign conventions depending on grade and whether you store things dually. For ray tracing you usually want to reflect a **direction**.

The chapter represents surface orientation as a **surface attitude** (a free bivector). To reflect the incident ray direction, it forms the appropriate reflecting element from that attitude and applies the sandwich, producing the reflected direction. The code shows this as a single expression: take the attitude-derived element, sandwich the direction, and negate according to the sign convention for the chosen representations.

The practical meaning is the familiar one: you get the mirror direction without leaving the algebraic framework.

## Refraction uses the classical direction formula (but plugs in directly)

Refraction is handled with the standard vector formula derived from Snell's law. With $n$ the surface normal (unit), $u$ the incident direction (unit), and $\eta$ the refractive constant (index ratio as used by the implementation), the chapter gives:

$$u' = \Big(\operatorname{sign}(n \cdot u)\sqrt{1 - \eta^2 + \eta^2 (n\cdot u)^2} - \eta (n\cdot u)\Big) n + \eta u.$$

In this implementation, both $n$ and $u$ are **free vectors** in the conformal model, so the equation can be used as-is: no conversion layer is needed just to evaluate refraction.

The chapter also points out an extension-principle insight: the same refraction equation can be lifted from vectors to intersecting lines, meaning the formula is compatible with line-based reasoning too, not just direction vectors.

## Shading pipeline: interpolation, bump modulation, visibility-gated lighting

Even though CGA is powerful, the chapter is blunt that shading arithmetic is often simplest in ordinary 3D Euclidean vector form. The ray tracer's shading steps are:

1. **Interpolate surface properties** at the intersection point from per-vertex values using barycentric interpolation (the book's earlier formula (11.19)). This yields the local material color and the local surface attitude/normal to use for lighting.
2. **Apply bump mapping** (if present) by modulating the interpolated surface attitude according to the bump map, again via interpolation-based sampling.
3. **Compute lighting** using an OpenGL-style ambient/diffuse/specular model, evaluated per intersection point (not per vertex).

The key extra step is the visibility check to each light: diffuse and specular contributions only apply if the path from surface to light is unobstructed. The chapter treats transparent objects as obstructions for this purpose, because true shadow refraction would require bending the shadow ray and accounting for it—too complex for the chosen shortcut model.
