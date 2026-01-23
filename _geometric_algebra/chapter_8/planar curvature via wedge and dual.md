# Planar Curvature via Wedge and Dual

Curvature is the first place where "coordinate-free" differential geometry stops being aesthetic and starts being useful. In the plane, there's a classic geometric definition: the curvature at a point is the reciprocal radius of the **osculating (tangent) circle**. Geometric algebra turns the derivation into a short wedge/dual computation.

## Setup: the tangent circle constraints

Let $r(\tau)$ be a planar curve with derivatives $\dot{r}(\tau)$ and $\ddot{r}(\tau)$. Let the osculating circle have center $c$ and radius $\rho$. Points on it satisfy

$$
(c - r)^2 = \rho^2.
$$

Differentiate with respect to $\tau$:

1. First derivative:

$$
2(c - r) \cdot \dot{r} = 0 \quad \Rightarrow \quad (c - r) \perp \dot{r}.
$$

2. Second derivative:

$$
-2 \, \dot{r} \cdot \dot{r} + 2(c - r) \cdot \ddot{r} = 0 \quad \Rightarrow \quad (c - r) \cdot \ddot{r} = |\dot{r}|^2.
$$

So $c - r$ is orthogonal to $\dot{r}$, and its dot with $\ddot{r}$ is fixed.

## The GA move: bundle the dot constraints with a contraction into a wedge

The terms $(c - r) \cdot \dot{r}$ and $(c - r) \cdot \ddot{r}$ suggest contracting $(c - r)$ into the bivector $\dot{r} \wedge \ddot{r}$:

$$
(c - r) \, \rfloor \, (\dot{r} \wedge \ddot{r}) = ((c - r) \cdot \dot{r}) \, \ddot{r} - ((c - r) \cdot \ddot{r}) \, \dot{r}.
$$

Insert the constraints:

* $(c - r) \cdot \dot{r} = 0$,
* $(c - r) \cdot \ddot{r} = |\dot{r}|^2$,

to get the identity

$$
(c - r) \, \rfloor \, (\dot{r} \wedge \ddot{r}) = -|\dot{r}|^2 \, \dot{r} = -\dot{r}^{\,3}
$$

(where $\dot{r}^{\,3}$ here is shorthand for $|\dot{r}|^2 \dot{r}$).

In 2D, trivectors vanish, so $(c - r) \wedge (\dot{r} \wedge \ddot{r}) = 0$. That means the contraction above can be treated as a geometric product in a way that lets you "divide" by the bivector $\dot{r} \wedge \ddot{r}$ (assuming it's nonzero, i.e., you're not at an inflection with zero curvature).

## Closed form: center and radius

Rearranging gives a compact expression for the center:

$$
c = r - \frac{\dot{r}^{\,3}}{\dot{r} \wedge \ddot{r}}.
$$

Once you have $c - r$, the radius follows from $\rho^2 = (c - r)^2$:

$$
\rho^2 = \left( \frac{\dot{r}^{\,3}}{\dot{r} \wedge \ddot{r}} \right)^2.
$$

What's hiding inside that fraction is geometrically clean: only the component of $\ddot{r}$ **orthogonal** to $\dot{r}$ contributes (the parallel component corresponds to reparameterization speed changes, not bending).

## Curvature: wedge + dual

Curvature is $\kappa = 1/\rho$. In the oriented plane, dualize the bivector $\dot{r} \wedge \ddot{r}$ with the plane pseudoscalar $I_2$. Choosing the sign convention via $\dot{r}^*$ (the "positive normal" direction), you get

$$
\kappa = \frac{(\dot{r} \wedge \ddot{r})^*}{|\dot{r}|^3}.
$$

This is the coordinate-free curvature formula: "signed area rate" (the bivector $\dot{r} \wedge \ddot{r}$) divided by cubic speed.

If you drop into coordinates $r(\tau) = x(\tau) e_1 + y(\tau) e_2$, it becomes the familiar expression

$$
\kappa = \frac{\dot{x} \, \ddot{y} - \dot{y} \, \ddot{x}}{(\dot{x}^2 + \dot{y}^2)^{3/2}},
$$

but GA makes it obvious *why* that determinant appears: it's the pseudoscalar dual of the wedge $\dot{r} \wedge \ddot{r}$, i.e., the signed infinitesimal area spanned by velocity and acceleration.
