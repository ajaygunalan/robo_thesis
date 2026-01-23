# scene transformations and interactive modeling

Ray tracing is useless if you can't pose a scene and a camera. This chapter builds a small interactive modeler (Figure 23.2 on page 11) and uses it to show one of CGA's most practical wins: Euclidean transformations become *directly executable* versor expressions, and many mouse-driven manipulations become literal one-liners.

## Versors as graphics transforms

In the conformal model, Euclidean motions (rotation, translation, reflection) and uniform scaling can be represented as versors/rotors. Applying a transform to a blade is the standard sandwich:

* take your blade $X$,
* apply $X' = V X \tilde{V}$ (reverse $\tilde{V}$).

In code, that's the repeated pattern `xf * blade * reverse(xf)`.

Composition order matters in interactive work:

* **premultiply** to apply the new motion in the *global* frame,
* **postmultiply** to apply it in the *local/current* object frame.

That single rule is what makes "dragging in view space" feel intuitive.

## Mouse input: from pixels to a 2D vector

The UI toolkit delivers mouse coordinates as pixel integers. The chapter immediately maps this to a 2D Euclidean vector in the viewport plane, with a flipped $y$ so that "up is up." Then differences of consecutive positions give a motion vector used to drive all manipulations.

## Scaling: exponentiate the dilation generator

Scaling is done using a scaling versor based on $(o \wedge \infty)$. The user's vertical mouse motion controls the scale parameter; exponentiation gives a smooth, logarithmic feel (dragging up/down multiplies/divides scale). The implementation relies on postmultiplying by the object's current transform so the scaling occurs about the object's own center without extra bookkeeping.

## Translation: build a translator in the right frame

For translation parallel to the viewport, the mouse motion is naturally expressed in the camera frame, but the object's transform composition may require a world-frame translator. The chapter's pattern is:

1. turn the (scaled) 2D mouse motion into the corresponding free vector in camera coordinates,
2. map that vector into world coordinates by sandwiching with the camera transform,
3. exponentiate to get a translator.

A key pragmatic detail is scaling the mouse motion so the selected object "sticks" to the cursor; the scaling depends on the object's depth and the camera field of view.

Translation orthogonal to the viewport is similar, except you use only the vertical mouse component and scale it with depth so distant objects respond faster (otherwise depth dragging would feel frozen).

## Object rotation: a trackball built from sphere intersections

Rotation is the most geometric interaction. When rotation mode is active, the modeler draws a transparent sphere around the object and treats it as a "trackball" surface. The user's previous and current mouse positions define two lines through the camera center into the scene; intersect those lines with the sphere to get two points on the sphere.

From there, the rotation is computed by constructing the two lines from the sphere center through those points, then building the rotor that carries one line to the other using a line-product normalization trick (conceptually the conformal analogue of "the rotor from the half-angle object"). Figure 23.3 on page 14 sketches this whole construction.

## Camera transforms: translation, spaceball rotation, orbiting

Camera translation is simpler than object translation because the mouse motion is already in camera coordinates, so you can form the translator directly by exponentiating the appropriate free vector.

Camera rotation uses a "spaceball" interface (Figure 23.4 on page 15):

* dragging *outside* a central circle rotates about $e_3$ (in-plane screen rotation),
* dragging *inside* rotates about $e_1$ and $e_2$ (tilt).

The rotors come from exponentiating small 2-blades built from mouse position/motion; the constructions are short enough to be read as geometry rather than as "matrix gymnastics."

Orbiting the camera around a selected object is the most subtle case because the rotation center is a world-space point while the user input lives in the camera frame. The chapter handles this by:

1. computing the orbit center relative to the camera as a flat point (by transforming the flat origin through the object's transform and pulling it into the camera frame),
2. building a translator to that offset,
3. conjugating the rotation by that translator so the rotation happens about the desired point,
4. composing it into the camera transform.
