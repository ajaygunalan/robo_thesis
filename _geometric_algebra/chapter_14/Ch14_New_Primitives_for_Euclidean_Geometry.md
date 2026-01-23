# 14 New Primitives for Euclidean Geometry

This chapter continues the development of the conformal model of Euclidean geometry. We have seen in the previous chapter how the model includes flats and directions as blades and Euclidean transformations on them as versors. That more or less copied the capabilities of the more familiar homogeneous model, though in a structure-preserving form, which permits metrically significant interpolation.

In this chapter, we show that the blades of the conformal model can represent many more elements that are useful in Euclidean geometry: They give us spheres, circles, point pairs, and tangents as direct elements of computation. Having those available will extend the range of computations that can be done by the basic products of geometric algebra, which is the subject of the next chapter. Here we carefully develop the representation of these new elements and show how to retrieve their parameters. You will for instance see that the sphere through the four points $p$, $q$, $r$, and $s$ is the blade $p \wedge q \wedge r \wedge s$, and that you can immediately read off its center and radius from the dual sphere $(p \wedge q \wedge r \wedge s)^*$.

Again, we urge the use of interactive visualization to get the maximum enjoyment out of this chapter. The conformal model is not abstract mathematics, it is a practical tool!

---

## 14.1 Rounds

We have made the representation of flats by considering blades containing the point at infinity $\infty$. We can make other blades through the outer product of finite points only. It is a happy surprise that this gives us the direct representations of spheres, circles, and other related elements. For such elements we do not have the analogy of the homogeneous model to guide us, and it is actually somewhat easier to introduce them through their duals and then derive their direct representation from that. Once we have the results, either mode is easy to work in, it just depends on the manner in which your data has been given (we will find that if you know the center and radius of a sphere, you should use the dual to construct its blade; if you know four points on the sphere, you should use the direct representation).

### 14.1.1 Dual Rounds

We start with the dual representation of a real sphere of radius $\rho$, located at the origin $o$ (see Figure 14.1(a)). According to Table 13.2, this is

$$\text{dual sphere at origin: } \sigma = o - \frac{1}{2}\rho^2 \infty.$$

Let us cut this dual origin sphere with a plane through the origin, dually represented as $\pi = \mathbf{n}$. Such a plane is perpendicular to the sphere in our Euclidean base space. In the representation, this perpendicularity of a plane and a sphere set corresponds to the statement

$$\pi \cdot \sigma = 0.$$

This is easily verified for the particular situation we have at the origin: $\mathbf{n} \cdot (o - \frac{1}{2}\rho^2 \infty) = 0$. The general result is achieved through the familiar argument on covariance: the condition is formulated as a scalar-valued inner product; therefore, it is invariant under orthogonal transformations; therefore, it is invariant under versors; therefore, when both elements are rotated and translated it still holds; therefore, it holds universally as the condition for perpendicularity of a sphere and a plane through its center. Again, the structure preservation saves us proving statements in their most general form: one example suffices to make it true anywhere.

We can form the blade $\kappa = \sigma \wedge \pi$. Since this is the outer product of two duals, it must be the dual representation of the meet of plane and sphere (for $(A \cap B)^* = B^* \wedge A^*$, see (5.8)). In our Euclidean space, the meet is clearly a circle (see Figure 14.1(b)), and if everything is consistent, its dual representation, $\kappa$, must be a dual circle.

$$\text{dual circle at origin: } \kappa = \sigma \wedge \pi = (o - \frac{1}{2}\rho^2 \infty) \wedge \mathbf{n},$$

where $\mathbf{n}$ is the dual representation of the carrier plane $\pi$ of the circle. This is how simple it is to represent a dual circle in the conformal model: it is a 2-blade.

If you are still suspicious whether this really is a dual circle, probe this dual element $\kappa$ with a point $x$ and check for which points $x$ this is zero. That gives the condition

$$0 = x \rfloor (\sigma \wedge \pi) = (x \cdot \sigma)\pi - (x \cdot \pi)\sigma.$$

Then take the inner product of this with $\pi$, which gives $0 = (x \cdot \sigma)\pi \cdot \pi$, and the inner product with $\sigma$, which gives $0 = (x \cdot \pi)\sigma \cdot \sigma$. Since both $\pi \cdot \pi$ and $\sigma \cdot \sigma$ are nonzero (at the origin, and therefore everywhere) this indeed retrieves the independent conditions $x \cdot \sigma = 0$ and $x \cdot \pi = 0$, so the point $x$ must be both on the sphere and on the plane. In Euclidean terms, the former condition is $\mathbf{x}^2 = \rho^2$, and the second is $\mathbf{x} \cdot \mathbf{n} = 0$, which is clearly sufficient to construct the circle equation $x_1^2 + x_2^2 = \rho^2$ for coordinates of $\mathbf{x}$ in the $\mathbf{n}$-plane.

We can cut the circle with yet another plane $\pi'$, perpendicular to both $\sigma$ and $\pi$ (see Figure 14.1(c)). In 3-D, that gives us a dual *point pair*, which is indeed a sphere on a line, the set of points with equal distance to the center $o$. It is dually represented as

$$\text{dual point pair at origin: } \sigma \wedge \pi \wedge \pi'.$$

The Euclidean bivector $\pi' \wedge \pi$ is the dual meet of the two planes, and dually denotes the carrier line of the point pair. In an $n$-dimensional space, the process continues, and you can cut the original sphere with $n$ hyperplanes before the outer product trivially returns zero (which makes geometric sense, since there are only $n$ independent hyperplanes at the origin in $n$-dimensional space).

Let us call the elements we obtain in this way *dual rounds*. Their general form, when centered on the origin, is

$$\text{real dual round at origin: } (o - \frac{1}{2}\rho^2 \infty)\mathbf{E}_k, \tag{14.1}$$

with $\mathbf{E}_k$ a purely Euclidean $k$-blade dually denoting the carrier flat of the round. Since the blades are generated in properly factored form, we will prefer to denote them using the geometric product; however, you could use the outer product instead (see structural exercise 8). When we translate them by a translation over $\mathbf{c}$, the dual sphere part moves to $c - \frac{1}{2}\rho^2 \infty$, whereas the purely Euclidean part changes according to (13.7) (i.e., to $-c \rfloor (\infty\mathbf{E}_k)$). Therefore, the general form for a round centered at $c$ is

$$\text{real dual round at } c: \quad (c - \frac{1}{2}\rho^2 \infty)\left(-c \rfloor (\infty\mathbf{E}_k)\right). \tag{14.2}$$

We will later relate the Euclidean blade $\mathbf{E}_k$ to a specifically chosen orientation for the carrier flat $c \wedge \mathbf{A}_{n-k} \wedge \infty$, and then set $\mathbf{E}_k = (-1)^n \mathbf{A}_{n-k}^\star$ to represent this same orientation dually. For now, focus on the form of the expression rather than on such details.

We started from a real dual sphere to produce these elements; had we started from an imaginary sphere $o + \frac{1}{2}\rho^2 \infty$ (see Section 13.1.3), we would have produced dual *imaginary rounds*. These therefore only differ from the real rounds in replacing $\rho^2$ by $-\rho^2$. As we saw before, we can have representation of imaginary rounds in a real algebra, since only squared distances enter our computations.

You may wonder why we did not encounter *imaginary flats* in the previous chapters. But flats are always real, for they have no size measure like a radius. They merely have a weight, and when its sign changes, this simply changes their orientation. Of course, rounds also have a weight, which gives them an orientation and a density.

### 14.1.2 Direct Rounds

Now that we have made *dual* spheres, circles, and point pairs, real or imaginary, we also want to know their *direct* representation: they will give us yet another type of blade in the conformal model $\mathbb{R}^{n+1,1}$ with a clear geometric meaning in $\mathbb{E}^n$.

Instead of undualizing the duals, we now have enough experience with the conformal model to guess the direct representation and then relate it to the duals afterwards. The resulting computation is surprisingly easy and coordinate-free, and a good example of the kind of symbolic computational power the operational model of Euclidean geometry affords.

Let us consider the 3-D Euclidean space $\mathbb{E}^3$. A sphere in that space is determined by four points. We take four unit points $p$, $q$, $r$, $s$. We are bold and guess that the sphere $\Sigma$ is represented by the blade

$$\Sigma = p \wedge q \wedge r \wedge s,$$

but of course we should prove that. First, we manipulate it using the antisymmetry of the outer product, subtracting $p$ from all terms but the first, to obtain

$$\Sigma = p \wedge (q - p) \wedge (r - p) \wedge (s - p).$$

Then we dualize, producing

$$\Sigma^* = p \rfloor \left((q - p) \wedge (r - p) \wedge (s - p)\right)^*. \tag{14.3}$$

We suspect that this might be a dual sphere, but this is in a form we have not seen before: it is apparently characterized by a point on it contracted on something else. From Table (13.2), we only know it in the form $c - \frac{1}{2}\rho^2 \infty$, given its unit center point $c$ and radius $\rho$. But if we know a unit point $p$ on the sphere, then $\rho$ is easily computed through $p \cdot c = -\frac{1}{2}\rho^2$, and using $p \cdot \infty = -1$, we can group these results in a compact form:

$$\text{dual sphere around } c \text{ through } p: \quad p \rfloor (c \wedge \infty). \tag{14.4}$$

We recognize $c \wedge \infty$ as the flat point at the center of the sphere.

Returning to (14.3), if $\Sigma^*$ is supposed to be a dual sphere through $p$, then the expression under the dual should be a representation of the flat point at the center, possibly weighted. From its form, it is the meet of three elements that are dually represented by $(q-p)$, $(r-p)$, and $(s-p)$. What is $(q-p)$? Since it is a dual representation of some element, we probe it with a point $x$ to find out: $0 = x \cdot (q - p)$, so $x \cdot p = x \cdot q$, so $d_E^2(x,p) = d_E^2(x,q)$. It follows that

$$q - p \text{ is the dual midplane between the unit points } p \text{ and } q. \tag{14.5}$$

So the expression $\left((q - p) \wedge (r - p) \wedge (s - p)\right)^*$ computes the intersection of the midplanes between the three point pairs, which is indeed a weighted copy of the flat point at the center $\alpha(c \wedge \infty)$. Therefore we indeed have a (weighted) dual sphere. It follows that the outer product of four points is a sphere.

The relationship between dual and direct representation of the sphere,

$$\alpha(c - \frac{1}{2}\rho^2 \infty) = (p \wedge q \wedge r \wedge s)^*,$$

implies that the (center, radius) formulation is exactly dual to the four-point definition. We can compute the weight $\alpha$ by taking the contraction with $-\infty$ on both sides, giving

$$\alpha = -\infty \rfloor (p \wedge q \wedge r \wedge s)^* = -(\infty \wedge p \wedge q \wedge r \wedge s)^*.$$

This gives us an easy way to compute the squared radius of a sphere through four points as the square of the corresponding normalized dual sphere. Some duals and signs cancel, and we get

$$\rho^2 = (c - \frac{1}{2}\rho^2 \infty)^2 = \left((p \wedge q \wedge r \wedge s)^*\right)^2 / \alpha^2 = \frac{(p \wedge q \wedge r \wedge s)^2}{(p \wedge q \wedge r \wedge s \wedge \infty)^2}.$$

It is nice to have such a quantitative computational expression for the radius of the sphere through four points in such a coordinate-free form. In structural exercise 1, you derive a similar direct expression for the center of the sphere.

The computation we have just done was in 3-D space, which is why we needed to use four elements to span the sphere. Apart from that, nothing in the computation depended on the dimensionality. If we move into a plane, exactly the same construction can be used to show that three unit points $p \wedge q \wedge r$ span a circle, of which the radius squared is proportional to $(p \wedge q \wedge r)^2$. (If you are uncomfortable about whether this might be true in a general offset plane, just move the plane so that it contains the origin, perform the construction, and move it back to where it came from. The structure preservation of the versors then makes the result move with the motion and be valid in the offset plane as well.) Summarizing:

| Element | Representation |
|---------|----------------|
| oriented sphere through points $p, q, r, s$ | $p \wedge q \wedge r \wedge s$ |
| oriented circle through points $p, q, r$ | $p \wedge q \wedge r$ |
| oriented point pair through points $p, q$ | $p \wedge q$ |

We emphasize that a directed point pair is a *single* element of conformal geometric algebra, just one 2-blade $B$. There is therefore no need to make a separate data structure for an edge, because the point pair contains all information. So in contrast to the homogeneous model, we can have a line segment as a single element of computation. It is even possible to retrieve the constituent points from the 2-blade $B$ (see (14.13) in structural exercise 4). That is of course not possible for the other blades representing rounds; many triples of points determine the same circle.

As you play with such elements $p \wedge q \wedge r \wedge s$ in an interactive software package with visualization, it is pleasing to see how the independence of the result on motions of the points over the sphere is captured by the antisymmetry of the outer product. Switching on some display of the orientation of the sphere (as captured by the sign of its weight), you should see that orientation change in continuous and predictable manner, depending on whether $p, q, r, s$ form a positively oriented tetrahedron or not. Can you determine the geometrical relationship between $p$, $q$, $r$, and $s$ that makes the sphere become zero (see structural exercise 3)?

### 14.1.3 Oriented Rounds

We have seen above that a dual circle $\kappa$ can be characterized as the dual meet $\sigma \wedge \pi$ of a sphere $\sigma$ and a plane $\pi$ through the sphere's center (so that the two are perpendicular and $\sigma \cdot \pi = 0$). This was a geometrical construction, and we were not too particular about the signs involved. But you normally want to use the capability of geometric algebra to represent oriented spheres, circles, and point pairs, so we should be more specific. The orientation of the direct circle $K$ in direct representation is most easily characterized as the orientation of its carrier plane $K \wedge \infty$; proper dualization then gives the form we should use for the dual representation to get the desired matching orientation.

To avoid having to fix signs later, we work from a direct form with obviously correct orientation (though with a somewhat mysterious spherical part) to determine the correct dual. We claim that the direct form of a round at the origin is

$$\Sigma = (o + \frac{1}{2}\rho^2 \infty)\mathbf{A}_k, \tag{14.6}$$

with $\mathbf{A}_k$ purely Euclidean. The carrier flat of this round is $\Pi = \Sigma \wedge \infty = o \wedge \mathbf{A}_k \wedge \infty$, with the orientation of $\mathbf{A}_k$. We compute the corresponding dual:

$$\begin{aligned}
\Sigma^* &= \left((o + \frac{1}{2}\rho^2 \infty)\mathbf{A}_k\right) \rfloor (o \wedge \mathbf{I}_n^{-1} \wedge \infty) \\
&= \left(\widehat{\mathbf{A}}_k(o + \frac{1}{2}\rho^2 \infty)\right) \rfloor (o \wedge \infty \wedge \widehat{\mathbf{I}}_n^{-1}) \\
&= \widehat{\mathbf{A}}_k \rfloor \left((o - \frac{1}{2}\rho^2 \infty) \wedge \widehat{\mathbf{I}}_n^{-1}\right) \\
&= (o - \frac{1}{2}\rho^2 \infty)(\mathbf{A}_k \rfloor \widehat{\mathbf{I}}_n^{-1}) \\
&= (o - \frac{1}{2}\rho^2 \infty)\mathbf{A}_k^\star(-1)^n.
\end{aligned} \tag{14.7}$$

This shows both the correctness of the direct representation of the round (since it produces a dual of the correct form), and how we should choose the sign of the dual to represent a round with a particular orientation. You should really use this instead of the earlier expression (14.2), which was unspecific on the orientation.

For instance, to dually represent a circle with unit radius rotating positively (counterclockwise) in the $\mathbf{e}_1 \wedge \mathbf{e}_2$-plane, we have $\mathbf{A}_2 = \mathbf{e}_1 \wedge \mathbf{e}_2$. In 3-D space with the regular pseudoscalar, the dual circle is $(o - \frac{1}{2}\infty)(-\mathbf{e}_3)$; in a 4-D space, the dual circle would be $(o - \frac{1}{2}\infty)(-\mathbf{e}_3 \wedge \mathbf{e}_4)$.

Collectively, we call these elements derived from the intersection of a sphere with planes *direct rounds*, a term that includes oriented spheres, oriented circles, and oriented point pairs in 3-D, but clearly extends to any dimension. The above shows its representation to be

$$\text{direct real round at origin: } \Sigma = (o + \frac{1}{2}\rho^2 \infty)\mathbf{A}_k. \tag{14.8}$$

Note the difference with the dual round representation of (14.1): for a real direct round, a factor appears that looks like an imaginary dual sphere. Direct imaginary rounds are of the form $(o - \frac{1}{2}\rho^2 \infty)\mathbf{A}_k$, simply changing the sign on $\rho^2$.

To correspond to mathematical tradition, we can call a round a $(k-1)$-sphere if its carrier has dimension $k$. The mathematical indication of dimensionality refers to the dimension of the manifold of its shell. What we call a sphere in 3-D is a 2-D curved surface, and therefore called a 2-sphere; we could call it a 2-round. A circle is a 1-D manifold and therefore a 1-sphere. A point pair is a 0-sphere; it is unique in having two separate components.

By translation using a rotor $T_\mathbf{c}$, we can produce general rounds around any point $c$, as the elements

$$\text{direct round: } (c + \frac{1}{2}\rho^2 \infty) \wedge \left(-c \rfloor (\widehat{\mathbf{A}}_k \infty)\right), \tag{14.9}$$

where we used the translation formula (13.7). A $k$-sphere is therefore represented by a $(k + 2)$-blade. The associated dual round with the same orientation is

$$\text{dual round: } (c - \frac{1}{2}\rho^2 \infty) \wedge \left(-c \rfloor (\widehat{\mathbf{A}}_k^\star \infty)\right), \tag{14.10}$$

which is an $(n - k)$-blade. (To obtain (14.10), we applied (13.7) to (14.7), and canceled some signs.) These expressions have been collected in Table 14.1 for easy reference, though more compactly denoted through translation rotors applied to standard forms around the origin.

---

## 14.2 Tangents as Intersections of Touching Rounds

In the representation of a round the radius can be set to zero. This results in a blade that squares to zero. To find its geometric interpretation, let us construct a setup in which it naturally occurs. We put two (dual) spheres with equal radius $\rho$ at opposite sides of the origin, in the unit $\mathbf{e}_1$-direction, as depicted in Figure 14.2. You can easily verify that these spheres are represented by the vectors $o \pm \mathbf{e}_1 + \frac{1}{2}(1 - \rho^2)\infty$. We compute the dual meet by the outer product of the duals and simplify the outcome:

$$\left(o - \mathbf{e}_1 + \frac{1}{2}(1 - \rho^2)\infty\right) \wedge \left(o + \mathbf{e}_1 + \frac{1}{2}(1 - \rho^2)\infty\right) = \left(o - \frac{1}{2}(\rho^2 - 1)\infty\right) \wedge (2\mathbf{e}_1) \tag{14.11}$$

There are three cases:

- When $\rho^2 > 1$ (as in Figure 14.2(a)) we get a real dual circle, nicely factored in the outer product as the intersection of a real dual sphere (with squared radius $\rho^2 - 1$) and the dual plane $2\mathbf{e}_1$ that denotes the flat carrier plane of the circle.

- But when we have $\rho^2 < 1$ (as in Figure 14.2(c)), the resulting intersection circle becomes imaginary and is factored as the intersection of a plane and an imaginary sphere (with the squared radius $\rho^2 - 1$ now being negative).

- When $\rho^2 = 1$, we get Figure 14.2(b). Geometrically, we would say that the spheres now have a tangent 2-blade in common. You can think of this tangent 2-blade as the intersection point of the two spheres with a tiny bit of plane attached. We have sketched it like that in Figure 14.2(b). This is apparently represented by the dual blade $o \wedge (2\mathbf{e}_1)$.

It is interesting that we obtain this kind of infinitesimal element through application of the incidence operator, not by any differentiation or limiting process, and that we therefore have them available as regular blades of the conformal model. The only unusual thing about them is that they square to zero.

Let us study this class of blade in its direct form, at the origin. We can make it by setting the radius of a direct round to zero, producing from (14.8) the element $o \wedge \mathbf{A}_k$ as the standard form at the origin. For $k = 2$, a tangent 2-blade results. These are new elements; we shall call them *(direct) tangents*.

$$\text{direct tangent at origin: } o \wedge \mathbf{A}_k$$

They have a location (here $o$) and a direction, but they are not flats (since they lack the element $\infty$). A direct flat can be constructed from such an element by making it pass through infinity, as $(o \wedge \mathbf{A}_k) \wedge \infty$; this shows clearly that $\mathbf{A}_k$ is the directional element of the tangent.

If $\mathbf{A}_k$ is a vector $\mathbf{A}_1 = \mathbf{a}$, this tangent element looks like $o \wedge \mathbf{a}$. This may be pictured as a vector in direction $\mathbf{a}$ located at the origin. We can find out which point set it represents by solving $x \wedge (o \wedge \mathbf{a}) = 0$, and this yields that only $x = o$ is in it, but clearly $o \wedge \mathbf{a}$ is more than just $o$; it also has a directional part $\mathbf{a}$. It can be made as the meet of two circles (see structural exercise 7). Note that a tangent vector is *not* a small vector: the signed length of a vector is given by its weight, and that can be arbitrarily big. It is the *size* of the tangent vector element that is zero, as its zero square shows; you can interpret it as a pair of very close points, if that helps. The sharp distinction between size and weight occurs for the first time in the conformal model, which therefore appears as the natural framework to represent elements that are small in their 2-point geometric size, yet have a finite weight. These are finite elements of geometry, not infinitesimals!

The dual representation of the tangent is of course obtained from the representation of the dual round of (14.10), setting its radius to zero, giving

$$\text{dual tangent at origin: } o \wedge \mathbf{A}_k^\star(-1)^n.$$

As with the rounds, this involves a sign to relate the orientation to that of the direct representation. Apart from that, you see that the dualization is the Euclidean dual: *the tangents embed the vector space model into the conformal model, one copy at each location*. In mathematics, this is called the *tangent bundle*; the conformal model gives us its elements as regular elements of computation.

Displacing a direct tangent element using a translation rotor, it becomes

$$\text{direct tangent: } p \wedge (-p \rfloor (\widehat{\mathbf{A}}_k \infty)).$$

Note that you should not simply use $p \wedge \mathbf{A}_k$ as the translated element!

A tangent $X$ is a blade characterized by having zero square ($X^2 = 0$), since it is like a round with zero radius. But it does not contain $\infty$ (so that $\infty \wedge X \neq 0$). A dual tangent $X^*$ satisfies the dual of these conditions: $(X^*)^2 = 0$, while $\infty \rfloor X^* \neq 0$. Because of these conditions, it is consistent to view a *point* as a special case of a tangent element, with a scalar directional part denoting its weight: $p \wedge \alpha$. In that view, a point is a localized scalar.

### 14.2.1 Euclid's Elements

We have now found all elements of Euclidean geometry as encoded in the conformal model. The basic objects are represented by the blades assembled in Table 14.1.

Note in the table that, apart from the flats, the elements retain their appearance after dualization: a dual direction may be confused with a directly represented direction, a tangent with a dual tangent, and a real dual round with an imaginary direct round, all of complimentary Euclidean properties of direction and/or size. Since we cannot tell them apart from their structure alone, we need to specify somehow whether they are intended for direct or dual usage.

This is a bit of a nuisance; we might have hoped that direct and dual representations had been more clearly separated in the conformal model. But at least direct and dual elements transform in precisely the same manner under even versors, so keeping track of their nature is only required for interpretation, not for correct algebraic manipulation. That in itself is an improvement over the homogeneous model in which direct and dual representations translate differently.

**Table 14.1: All nonzero blades in the conformal model of Euclidean geometry and their parameters.**

*Locations are denoted by dual spheres. The normalized points $q$ are probes to give locations closest to $q$; one may just use $q = o$. The directions are computed in direct form, although the dualized version is also given. The weight in all cases is computed as $\sqrt{|q \rfloor \text{direction}(X)|^2}$, orientation is relative to the chosen pseudoscalar for the directional subspace.*

*As for notation, $\widehat{X} = (-1)^{\text{grade}(X)}X$ is the grade involution, $\mathbf{E}^\star$ is a Euclidean dual, $X^{-*}$ is the undualization in the full space. $\mathsf{T}_\mathbf{p}$ denotes a translation to the position $\mathbf{p}$ relative to the origin, to signify the general form of the elements.*

| Standard Form $X$ | Condition | Direction $\mathbf{E}\infty$ | Location | Squared Size |
|-------------------|-----------|------------------------------|----------|--------------|
| **direction** | $\infty \wedge X = 0$ | | | |
| $\mathbf{E}\infty$ | $\infty \rfloor X = 0$ | $X$ | none | none |
| **dual direction** | $\infty \wedge X = 0$ | | | |
| $-\mathbf{E}^\star\infty$ | $\infty \rfloor X = 0$ | $X^{-*}$ | none | none |
| **flat** | $\infty \wedge X = 0$ | | | |
| $\mathsf{T}_\mathbf{p}[o \wedge (\mathbf{E}\infty)]$ | $\infty \rfloor X \neq 0$ | $-\infty \rfloor X$ | $(q \rfloor X)/X$ | none |
| **dual flat** | $\infty \wedge X \neq 0$ | | | |
| $\mathsf{T}_\mathbf{p}[\widehat{\mathbf{E}^\star}]$ | $\infty \rfloor X = 0$ | $-\infty \rfloor X^{-*}$ | $(q \wedge X)/X$ | none |
| **tangent** | $\infty \wedge X \neq 0$ | | | |
| $\mathsf{T}_\mathbf{p}[o\mathbf{E}]$ | $\infty \rfloor X \neq 0$ | $-(\infty \rfloor X) \wedge \infty$ | $\frac{X}{-\infty \rfloor X}$ | 0 |
| | $X^2 = 0$ | | | |
| **dual tangent** | $\infty \wedge X \neq 0$ | | | |
| $\mathsf{T}_\mathbf{p}[o\mathbf{E}^\star(-1)^n]$ | $\infty \rfloor X \neq 0$ | $(-\infty \rfloor X^{-*}) \wedge \infty$ | $\frac{X}{-\infty \rfloor X}$ | 0 |
| | $X^2 = 0$ | | | |
| **round** | $\infty \wedge X \neq 0$ | | $\frac{X}{-\infty \rfloor X}$ | |
| $\mathsf{T}_\mathbf{p}[(o + \frac{1}{2}\rho^2\infty)\mathbf{E}]$ | $\infty \rfloor X \neq 0$ | $-(\infty \rfloor X) \wedge \infty$ | or $-\frac{1}{2}\frac{X\infty X}{(\infty \rfloor X)^2}$ | $\rho^2 = +\frac{X\widehat{X}}{(\infty \rfloor X)^2}$ |
| | $X^2 \neq 0$ | | | |
| **dual round** | $\infty \wedge X \neq 0$ | | $\frac{X}{-\infty \rfloor X}$ | |
| $\mathsf{T}_\mathbf{p}[(o - \frac{1}{2}\rho^2\infty)\mathbf{E}^\star(-1)^n]$ | $\infty \rfloor X \neq 0$ | $(-\infty \rfloor X^{-*}) \wedge \infty$ | or $-\frac{1}{2}\frac{X\infty X}{(\infty \rfloor X)^2}$ | $\rho^2 = -\frac{X\widehat{X}}{(\infty \rfloor X)^2}$ |
| | $X^2 \neq 0$ | | | |

### 14.2.2 From Blades to Parameters

So far, we have constructed the elements from parameters such as centers, radii, and directions. But we also need the reverse process to find out what kind of element a computation has produced, so we need to be able to classify a given blade and retrieve its parameters. For this task, the intimidating Table 14.1 is intended as reference.

Computing these geometric parameters of the various kinds of blades is not too hard, and the various formulas are easily proved (or derived when you have forgotten them) from a blade in its standard form around the origin. This is allowed as long as all formulas are Euclidean covariant (i.e., they don't use position or orientation-dependent constructions). You know from Section 13.2 that a good way to guarantee that is to write them using only the standard products, and only $\infty$ as a special element (since the point at infinity is a Euclidean invariant).

We give the algebraic formulas for size, weight, location, and direction. In an implementation, you can often just read off these elements as the coefficients of specific components of the blade normalized by the overall weight (which may be found as another coefficient)---as long as you do not use different coordinate systems within a single application.

- **Squared Size.** The square of a normalized dual sphere gives you its radius squared, for

$$(o - \frac{1}{2}\infty\rho^2)^2 = -\frac{1}{2}(o\infty + \infty o)\rho^2 = \rho^2.$$

For a dual round in general, you need to do a normalization and mind some grade-dependent signs. An unnormalized dual round $X$ has

$$X^2 = (o - \frac{1}{2}\rho^2\infty)\mathbf{E}^\star(o - \frac{1}{2}\rho^2\infty)\mathbf{E}^\star = \rho^2\mathbf{E}^\star\widehat{\mathbf{E}^\star}.$$

Since $\infty \rfloor X = \mathbf{E}^\star(-1)^n$, the squared size can now be computed by normalization and by a grade inversion to compensate for the extra sign in the Euclidean part. This gives

$$\rho^2 = \frac{X\widehat{X}}{(\infty \rfloor X)^2}.$$

For the direct representation of a round, the structure is similar. Therefore, the total formulas are as indicated in Table 14.1. It is good custom to denote the squared size rather than the size itself, since the square may be negative and we want to avoid introducing complex numbers.

All tangents and dual tangents have size 0. For the flats and directions, size is not an issue, since they do not have any (they only have a weight).

- **Direction, Weight, and Orientation.** A flat or round is in a translated linear subspace with a certain direction. This direction can be retrieved from the element by a specific formula for each category of element. The formulas are easily derived, they merely strip off the positional parts (if any) and supply a $\infty$-factor (if lacking). All return a direction of the form $\mathbf{E} \wedge \infty$, with $\mathbf{E}$ purely Euclidean, and may be found in Table 14.1.

The Euclidean parts of these directions may not be of unit weight or positive orientation relative to the pseudoscalar of the Euclidean subspace they belong to. In that case, the magnitude of the direction is the *weight* of the element, and its sign the *orientation*. The orientation is somewhat arbitrary, since it must be relative to the orientation of the pseudoscalar, which is a matter of choice or convention. The weight of an element of the form $\mathbf{E}\infty$ can be computed by stripping off the $\infty$ (through a contraction with $o$ or any other normalized point $q$), and computing the weight of the Euclidean part. That gives

$$\sqrt{|q \rfloor \text{direction}(X)|^2} = \sqrt{|q \rfloor (\mathbf{E}\infty)|^2}.$$

Since all elements have a direction, all elements have a weight and orientation. In some cases, these weights have a traditional way being displayed: a vector of weight 2 can be depicted as having length 2, and a tangent bivector of weight 2 as an area element of 2 area units. But a sphere of weight 2 is *not* a sphere of radius 2; rather it should be visualized as a heavier or denser spherical shell.

- **Location.** The location of a blade should be the Euclidean coordinates of some relevant point. For a round, this is naturally the center, but for flats such as lines and planes such a point is not uniquely indicated in a coordinate-free manner.

For flats, we can either take the point of it that is closest to the origin (obviously not coordinate-free) or the point that is closest to some given point $q$. The formulas in the table actually produce a normalized dual sphere $\sigma$ as the location (rather than a point, i.e., a dual sphere of radius zero), since that is a simple formula. This is often sufficient in intermediate computations, but you can take its Euclidean part as the Euclidean location vector (easy in most coordinate-based implementations, though algebraically it is $(o \wedge \infty) \rfloor (o \wedge \infty \wedge \sigma)$).

For the rounds, we only need to strip off the carrier part to be left with a dual sphere around the center, and this is done by computing $X/(-\infty \rfloor X)$. Alternatively, we may compute the normalized center point directly as a dual sphere of radius zero through

$$c = -\frac{1}{2}\frac{X\infty X}{(\infty \rfloor X)^2}.$$

For now, just accept this formula. We will appreciate this properly as computing the reflection of $\infty$ in the normalized round when we treat the operators of the conformal model in Chapter 16.

The result of these considerations is Table 14.1, which computes all parameters of the elements of all classes.

---

## 14.3 A Visual Explanation of Rounds as Blades

The vector space model and the homogeneous model may have accustomed us to thinking of the blades in a representation space as always representing flat elements in the base space. Algebraically, this interpretation appears to be supported by the idea that they must represent subspaces and therefore be linear. However, this argument confuses the representational space with the base space that is being represented. We can show you more visually why the surprising characterization of Euclidean rounds by blades works, to convince you of its intuitive correctness. In this section we will "pop up" the $\infty$-dimension graphically, though we will necessarily show you only the conformal model for a 2-D Euclidean geometry $\mathbb{E}^2$.

### 14.3.1 Point Representation

We have seen that a Euclidean point at the location $\mathbf{x}$ is represented as the conformal vector

$$x = o + \mathbf{x} + \frac{1}{2}\mathbf{x}^2\infty.$$

In 2-D Euclidean space $\mathbb{E}^2$, this requires a 4-D representational space $\mathbb{R}^{3,1}$ with a basis like $\{o, \mathbf{e}_1, \mathbf{e}_2, \infty\}$. This would seem to be hard to visualize. However, the $o$-dimension works very much like the extra dimension in homogeneous coordinates: it allows us to represent offset linear subspaces (i.e., linear subspaces that are shifted out of the origin in a representational space with basis $\{\mathbf{e}_1, \mathbf{e}_2, \infty\}$). So because of the $o$-term, we are allowed to draw conformal planes, lines, and so on, that do not need to go through the origin. If you accept that, we do not need to draw this dimension explicitly. We just use this freedom and know that such elements are blades in the representational space because of the $o$-dimension.

The $\infty$-dimension is new relative to the homogeneous model, and much more interesting. If we draw the Euclidean 2-space as the $\mathbf{e}_1 \wedge \mathbf{e}_2$-plane, then there is apparently a *paraboloid* $(\mathbf{x}, \frac{1}{2}\mathbf{x}^2\infty)$ in the $\infty$-direction that we should get to know better, for the points of Euclidean space are represented on it. By studying the combinations of points on this paraboloid, we should be able to get an intuition on how the conformal model actually works. In Figure 14.3, you see the 2-D Euclidean space laid out in white, and the $\infty$-paraboloid indicated vertically above it.

A conformal null vector $x$ representing a point ends on the paraboloid, just above the point at the location $\mathbf{x}$ in the Euclidean plane which it represents. We draw it as the parabola point with location vector $\mathbf{x} + \frac{1}{2}\mathbf{x}^2\infty$, letting the extra dimension $o$ play the role of the homogeneous coordinate. In Figure 14.3, we have drawn a vertical connecting line between the point $x$ and its representation; since that line runs in the $\infty$-direction, it is represented by the line $x \wedge \infty$ in this homogeneous depiction of the conformal model (with $x$ on it and $\infty$ as its direction). That vertical line is therefore the visualization of the flat point $x \wedge \infty$ at the location of $X$.

We have also drawn a plane at $x$, tangent to the paraboloid. This is actually the representational plane $x^*$: it consists of all the vectors perpendicular to the vector $x$ (in this metric). (It doesn't *look* perpendicular, but that is because we are interpreting with Euclidean eyes.) This is a direct consequence of the null-vector representation of Euclidean points. A conformal vector $y$ is on a plane $\Pi$ if and only if $y \wedge \Pi = 0$. Or, if we have a dual representation of the plane, $\pi = \Pi^*$, then $y$ is in the plane if and only if $y \cdot \pi = 0$. You will remember that the metric of the conformal model is set up in such a way that $x \cdot x = 0$, and the motivation for that was that a point represented by $x$ has distance 0 to itself in the Euclidean metric. We now see that we can also read this as

> If the vector $x$ represents a Euclidean point, then $x$ is on the tangent plane to the paraboloid that is dually represented by $x$.

Since $y = x$ is the only null vector that satisfies $y \cdot x = 0$, the plane dually represented by $x$ cannot intersect the paraboloid anywhere else, so it must indeed be the tangent plane to the paraboloid.

### 14.3.2 Circle Representation

Let us find out what another representative vector $\sigma$ on this tangent plane represents in the Euclidean base space. We can construct it from a point $C$ in the Euclidean space, making a vertical line $c \wedge \infty$ out of its representative $c$, and intersect that with the tangent plane. That gives a representation point $\sigma = x \rfloor (c \wedge \infty)$. We have met this element $\sigma$ as representing a dual circle through the point $x$ with center $c$. Let us find out why this is the correct interpretation in this visualization as well. The position of $\sigma$ relative to $x$ is sketched in Figure 14.4. Since $\sigma$ is on the plane with dual representation $x$, we must have $\sigma \cdot x = 0$. But this also implies that $x \cdot \sigma = 0$, which we would interpret as $x$ being on the plane dually represented by $\sigma$. What is this dual plane of $\sigma$, and what other point representatives are on it? All such points $y$ must satisfy $y \cdot \sigma = 0$, and therefore $\sigma \cdot y = 0$. So all these points must be such that $\sigma$ lies on their tangent plane; that must imply that they are the contour of the parabola as seen from $\sigma$. Together, they lie on the plane dually represented by $\sigma$, which therefore passes through the parabola in the way indicated in Figure 14.4. That is then a geometrical way of constructing the dual of $\sigma$: as the connecting plane of tangent points to the paraboloid as seen from $\sigma$. In projective geometry, this construction is known as determining the *polar* of $\sigma$ relative to the paraboloid. When you project down the resulting ellipse, you find a circle of Euclidean points, so *the plane dual to $\sigma$ is the direct representation of a circle*. We show a cross section of this situation in Figure 14.5 for clarity (alternatively, you can see this as a depiction of the conformal model of a 1-D space).

> A circle is represented by a plane that cuts the paraboloid in an ellipse, which projects down to a circle in the Euclidean space.

The position of the plane relative to the point $\sigma$ can be understood as follows. Since $\sigma = x \rfloor (c \wedge \infty) = (x \cdot c)\infty + c$, we have $\sigma^2 = -2(x \cdot c)$, so that $\sigma$ can be written as $\sigma = c - \frac{1}{2}\sigma^2\infty$. Therefore, the point $\sigma$ is a distance of $\frac{1}{2}\sigma^2$ under the paraboloid at $c$. When we look for the intersections with a vertical line $x \wedge \infty$ at any location $x$ with both the plane dually represented by $\sigma$ and the tangent plane at $c$, we find that these are $x \cdot (c - \frac{1}{2}\sigma^2\infty) = x \cdot c + \frac{1}{2}\sigma^2$ and $x \cdot c$, respectively. This shows that *the dual plane $\sigma$ is parallel to and above the tangent plane at $c$, by an amount of $\frac{1}{2}\sigma^2$ in the $\infty$-direction*. So the dual plane $\sigma$ is as far above the paraboloid as $\sigma$ is below it. This computation of the relative position of $\sigma$ and its dual plane $\sigma$ holds independently of the value of $\sigma^2$. If it is positive, we have the construction depicted in Figure 14.4; if it is zero, we have the dual plane of a point, which is the tangent plane depicted in Figure 14.3; and if it is negative, the point $\sigma$ is above the paraboloid, and the dual plane $\sigma$ below it, still parallel to the tangent plane. Thus we find a sensible real construction of the dual of an imaginary circle.

### 14.3.3 Euclidean Circles Intersect as Planes

Figure 14.6 shows how to do the intersection of two Euclidean spheres (which in 2-D are of course circles) in the conformal model. The answer is a Euclidean point pair (i.e., a 0-sphere). We know that the 2-D conformal model would represent this as the outer product of two null vectors $x \wedge y$. That is represented as a line in this homogeneous depiction of the representational space, intersecting the paraboloid at the two representatives of the points $x$ and $y$.

The figure shows clearly that this line representing the intersection of the two circles is the intersection of the two planes representing the circles. Those planes are in turn the duals of the circle representations $\sigma$ and $\tau$ as homogeneous points under the paraboloid.

There is therefore nothing quadratic about intersecting two circles once we are in the conformal model; it is the same as intersecting planes. If the planes should intersect in a line that does not pass through the parabola, we would interpret this as an imaginary point pair (it is a nice puzzle to construct its location), but there is nothing irregular about the intersection itself. Here is the take-home message of all this visualization:

> In the conformal model of a 2-D Euclidean space, intersecting circles is identical to intersecting offset planes in a space of one more dimension (the $\infty$-dimension). In yet one more dimension (the $o$-dimension), this is identical to intersecting subspaces through the origin. Therefore, the meet of origin blades in the conformal model is effectively circle intersection.

We hope this visualization helps you understand slightly better where those two extra dimensions come from, and why flat elements through the origin of the representational space $\mathbb{R}^{n+1,1}$ (its blades) can represent round elements in the Euclidean space $\mathbb{E}^n$.

---

## 14.4 Application: Voronoi Diagrams

The *Voronoi diagram* of a set of points is a graph that partitions space into the parts closest to each of them, as in the base plane in Figure 14.7. In computational geometry literature [12], an interesting construction is made that turns the computation of a Voronoi diagram of a set of points into computing a convex hull of a properly constructed polyhedron in a space of one more dimension, projected down. The polyhedron is made up of parts of tangent planes of lifts of the original points to a paraboloid set up in the extra dimension. This paraboloid construction is usually presented as a special clever trick, and not used in other algorithms. We will show that it is essentially the conformal model, and therefore much more widely applicable than is usually appreciated. Let us analyze the Voronoi construction in more detail, making full use of the convenient metric that the conformal model dictates for the extension of the Euclidean base space $\mathbb{E}^n$ to $\mathbb{R}^{n+1,1}$.

We have just seen how points are mapped to the paraboloid in the conformal model construction and how we can use a homogeneous model in the resulting space to consider the tangent planes. Now consider two points $\mathcal{P}$ and $\mathcal{Q}$ of the Euclidean base space, lifted to the paraboloid as $p$ and $q$. If we want to determine which points are closer to one than the other, the separation line between those is the *perpendicular bisector*, which is the line dually represented as $p - q$ in the conformal model. In the paraboloid representation, this line can be made by intersecting the tangent planes to $p$ and $q$. We show this in two steps: first, since the tangent planes are dually represented by $p$ and $q$, their meet is $\Lambda = (p \wedge q)^{-*}$. To find what this line in our model represents, we need to turn it into a plane stretching to infinity, and intersect that with the 2-D Euclidean base space. The plane is $\infty \wedge \Lambda = \infty \wedge (p \wedge q)^{-*} = (\infty \rfloor (p \wedge q))^{-*} = (p - q)^{-*}$. The intersection with the base plane gives $(p - q) \rfloor (o \wedge \mathbf{I}_2 \wedge \infty) = (p - q)^{-*}$, consistent with our assumption that this line was dually represented by $p - q$.

These perpendicular bisectors of point connections are the carriers of potential edges of the Voronoi diagrams in $\mathbb{E}^n$. We still need to select those among them that are actually closest to the given points not overruled by other bisectors of even closer points. When we study this by entering a third point $\mathcal{R}$, we have to decide among the bisectors dually represented as $p - q$, $q - r$, and $r - p$. These are lines in the intersection of the three tangent planes dually represented by $p$, $q$, and $r$, and they intersect in a single point in the representational space. This point is dually represented by $p \wedge q \wedge r$, and it represents the circumcircle of $p$, $q$, and $r$. Its projected location in the base space is the center of the circumcircle. It is clear that the parts of the bisectors that show up in the Voronoi diagram are the lines that are highest in the $\infty$-direction of the representation.

This holds for each triplet of points: the representations of the Voronoi lines connect the intersection points of each triplet of tangent planes, in the highest possible manner. Therefore we can determine the Voronoi diagram by constructing all such lines and determining their upper convex hull in the $\infty$-direction. It is illustrated as the green network in Figure 14.7, which projects down to the black Voronoi diagram in the 2-D Euclidean base space.

Using the principle of duality, this construction can be improved and made much more direct, for the intersection line $(p \wedge q)^{-*}$ of a tangent plane of point representatives $p$ and $q$ is exactly dual to the connection line $p \wedge q$ between the point representatives. When we take the dual of the complete network of line segments representing the Voronoi diagram, this generates a network that forms the convex hull of the point representatives themselves. It is illustrated as the blue network in Figure 14.7. It is in fact the representation of the *Delaunay triangulation* of the point set. That is the network of which the edges denote the closest point connections, indicated in red in Figure 14.7.

So the Delaunay triangulation of a set of points can be determined by lifting them all to a paraboloid, taking their convex hull, and projecting back. The corresponding Voronoi diagram is obtained from this by duality. That is precisely the convex hull algorithm from [12]. We have shown that this is actually a hidden application of the conformal model. You can play around with this algorithm in the programming example of Section 14.9.1.

---

## 14.5 Application: Fitting a Sphere to Points

### 14.5.1 The Inner Product Distance of Spheres

The inner product of the conformal model was defined to give a good correspondence to the squared Euclidean distance of normalized points in $\mathbb{E}^n$ represented as vectors in $\mathbb{R}^{n+1,1}$. Meanwhile, we have found that vectors of $\mathbb{R}^{n+1,1}$ can also represent dual spheres (and planes) of $\mathbb{E}^n$. We investigate what distance measure between spheres is defined by the inner product of vectors.

When we have two dual spheres $\sigma_1 = c_1 - \frac{1}{2}\rho_1^2\infty$ and $\sigma_2 = c_2 - \frac{1}{2}\rho_2^2\infty$, their inner product is

$$\sigma_1 \cdot \sigma_2 = c_1 \cdot c_2 + \frac{1}{2}(\rho_1^2 + \rho_2^2) = \frac{1}{2}\left(\rho_1^2 + \rho_2^2 - d_E^2(C_1, C_2)\right),$$

where $d_E^2(C_1, C_2)$ is the square of the Euclidean distance of their centers.

Figure 14.8 shows some situations for the geometry of the inner product. Let us first assume that one of the spheres is a point. In that case we find two situations, depending on whether the point is inside or outside the other sphere. If it is outside, as in Figure 14.8(a), the inner product denotes minus half the tangential distance of the point to the sphere, since its value becomes

$$\sigma \cdot p = -\frac{1}{2}\left(d_E^2(C,P) - \rho^2\right).$$

When the point is inside, the interpretation as a real distance changes to Figure 14.8(b). It is interesting to see what happens when the point gets close to the sphere at a distance $\rho + \delta$ from the center: then the inner product is equal to $-\rho\delta$, to first order in $\delta$. That implies that for points close to the sphere, it is linearly proportional to their distance to the sphere. This is a useful distance measure in optimization problems involving spheres, and we use it for sphere fitting in the next section.

For the general case of two spheres, the quantity representing the inner product can be constructed by a nested tangent construction, as illustrated in Figure 14.8(c). This does not immediately convey its usefulness. But Figure 14.8(d) shows an interesting special case: *when the inner product of two spheres is zero, they intersect orthogonally*. In this sense, the inner product of the conformal model is a measure of orthogonality.

By contrast, the outer product of two dual spheres is their dual intersection. When two spheres touch, this is a tangent element, characterized by having a zero square. So *when the outer product of two spheres has zero norm, they touch*.

### 14.5.2 Fitting a Sphere to Points

The representation of spheres as vectors leads to a simple method to fit the optimal sphere to a set of points, minimizing the sum of the squared distances (well, almost). This uses the structure of the conformal model to derive a procedure that can be executed classically. This section was inspired by [48].

In fitting a sphere to a set of points $\{p_i\}_{i=1}^N$, we can ask to minimize the sum of the squared distances. If a point $p$ is at a close distance $\delta$ to a dual sphere $\sigma$ with radius $\rho$, the inner product $p \cdot \sigma$ is $-\rho\delta$, to first order in $\delta$ (see previous section). Therefore for a close point, the squared distance is $(p \cdot \sigma)^2/\rho^2 = (p \cdot \sigma)^2/\sigma^2 = (p \cdot \sigma)(p \cdot \sigma^{-1})$, for a normalized sphere, $\sigma$, for which $-\infty \cdot \sigma = 1$.

So as a cost function for the fit we have

$$\Gamma \equiv \sum_i (p_i \cdot \sigma)(p_i \cdot \sigma^{-1}).$$

We ask for the $\sigma$ that minimizes this. Differentiating with respect to $\sigma$ and equating to 0 gives

$$0 = \frac{\partial\Gamma'}{\partial\sigma} = 2\sum_i (p_i \cdot \sigma)(p_i \wedge \sigma)\sigma^{-3}.$$

Unfortunately, we do not know how to solve this equation, since it is strongly nonlinear in $\sigma$.

If we change the problem slightly, we can ask for the sphere that minimizes the summed squares of $\rho\delta$ rather than $\delta$. This would minimize the distances to the points, but with a preference for small spheres. In practice, this solution will be close to the one we would have wanted. In this form it is solvable, for now the cost function is

$$\Gamma' \equiv \sum_i (p_i \cdot \sigma)(p_i \cdot \sigma),$$

and optimization of this gives

$$0 = \frac{\partial\Gamma'}{\partial\sigma} = 2\sum_i p_i(p_i \cdot \sigma).$$

The single occurrence of $\sigma$ makes this a linear equation that can be solved using standard linear algebra techniques, as follows. First, we realize that we can write the conformal space inner product in terms of a Euclidean inner product by the using metric matrix $[\![M]\!]$, which in 3-D is as given in Table 13.1:

$$[\![M]\!] = \begin{bmatrix} 0 & 0 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ -1 & 0 & 0 & 0 & 0 \end{bmatrix}$$

for a conformal model with basis $\{o, \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \infty\}$. Now $p \cdot \sigma$ is implemented on the vectors $[\![p]\!]$ and $[\![\sigma]\!]$ as an expression in the usual linear algebra of a Euclidean space:

$$p \cdot \sigma = [\![p]\!]^T [\![M]\!] [\![\sigma]\!],$$

where we should use the vector $[\![1, p_1, p_2, p_3, \frac{1}{2}(p_1^2 + p_2^2 + p_3^2)]\!]^T$ as a representation for each measured point $p$. We then need to solve, in least-squares fashion,

$$\sum_i [\![p_i]\!] [\![p_i]\!]^T [\![M]\!] [\![\sigma]\!] = 0.$$

To avoid the trivial solution $[\![\sigma]\!] = 0$, we use the scaling freedom in our representation to demand that $\sigma \cdot \sigma$ be constant and equal to 1. The nontrivial least-squares solution is then found using the standard singular value decomposition of the data matrix

$$[\![D]\!] \equiv \sum_i [\![p_i]\!] [\![p_i]\!]^T [\![M]\!] = [\![U]\!] [\![\Lambda]\!] [\![V]\!]^T.$$

The optimal $\sigma$ is the last column of $[\![V]\!]$, which is the eigenvector corresponding to the smallest singular value. This is proportional to the dual sphere that minimizes $\Gamma'$, and you can compute its center and radius using Table 14.1.

If you truly needed to minimize $\Gamma$ rather than $\Gamma'$, you can use the solution for $\Gamma'$ as the seed for a nonlinear optimization method such as Levenberg-Marquardt.

---

## 14.6 Application: Kinematics

### 14.6.1 Forward Kinematics

In computer animation and robotics, *forward kinematics* is used to compute the location and change of geometrical objects given a change in their parameters. As a typical example of the kind of problem, we treat the forward kinematics of a humanoid arm, in which we need to compute where the limbs end up, given the angles of the various joints. With translations and rotations both available as versors, we can now write this in terms of the conformal model.

In the classical way of doing this, one uses the homogeneous model to compute the rigid body motion matrices for vectors, as in Table 12.2, and multiplies those to get a transformation matrices for points on each of the limbs. That chain structure is of course essential to the problem, and also found in the conformal model solution. The only difference is that the resulting rigid body motion versors can be applied to elements of any kind, not just vectors. When all you need to do is to control a robot, this is not that relevant, but if you want to render an animation of the arm, this is potentially useful. There is no longer a necessity to decompose the graphic elements of a limb down to the level of vectors or points; line elements, circles, or tangent bivectors are just as easily transferred and rendered at their proper location on the moved arm.

To take a specific example, let us take the structure of a Unimation Puma 560 robot. We start with the definition of the robot dimensions and the directions of their rotation planes from its manual. This gives the essential kinematics structure indicated in gray in Figure 14.9. It is encoded as translations (in meters) and rotation bivectors as:

| | Translation | Rotation Bivector |
|---|-------------|-------------------|
| $\mathbf{t}_1$ | $6.60\mathbf{e}_3$ | $\mathbf{B}_1 = \mathbf{e}_1 \wedge \mathbf{e}_2$ |
| $\mathbf{t}_2$ | $4.31\mathbf{e}_1 + 1.49\mathbf{e}_2$ | $\mathbf{B}_2 = \mathbf{e}_3 \wedge \mathbf{e}_1$ |
| $\mathbf{t}_3$ | $-0.20\mathbf{e}_3$ | $\mathbf{B}_3 = \mathbf{e}_3 \wedge \mathbf{e}_1$ |
| $\mathbf{t}_4$ | $4.33\mathbf{e}_1$ | $\mathbf{B}_4 = \mathbf{e}_2 \wedge \mathbf{e}_3$ |
| $\mathbf{t}_5$ | $0$ | $\mathbf{B}_5 = \mathbf{e}_3 \wedge \mathbf{e}_1$ |
| $\mathbf{t}_6$ | $0.56\mathbf{e}_1 + 0.11\mathbf{e}_2$ | $\mathbf{B}_6 = \mathbf{e}_2 \wedge \mathbf{e}_3$ |

We can introduce a set of graphic elements $X_i^j$ to be drawn for limb $i$; they can be points, bivectors, circles, spheres, or whatever you need to draw the limb. You initially specify them in the coordinate frame of the corresponding limb $i$. In Figure 14.10, each limb is drawn by means of the point at its the origin $o$, the tangent blade of the rotation plane at the origin indicated as the tangent bivector $o \wedge \mathbf{B}_i$, and the point pair $o \wedge \mathsf{T}_{\mathbf{t}_i}[o]$ drawn as a line segment.

With that, we can initialize the translation versors for each limb $L_i$. We also compute where their rotation bivectors (the duals of the rotation axes) are in the home position when expressed in world coordinates relative to the base of the robot. This is done by simply translating the $\mathbf{B}_i$ by the successive translation of each joint. The representative rendering elements $X_i^j$ are translated in precisely the same manner (we call the result $Y_i^j$).

$$T_0 = 1 \qquad T_i = T_{i-1} e^{-\mathbf{t}_i\infty/2}$$
$$A_i = T_{i-1} \mathbf{B}_i \widetilde{T}_{i-1}$$
$$Y_i^j = T_{i-1} X_i^j \widetilde{T}_{i-1}$$

This concludes the setup of the robot kinematics parameterization, and allows us to draw the arm in the gray home position in Figure 14.9.

If the rotation angles $\phi_i$ are now specified at run time, we can compute the rigid body motion rotors $M_i$ for each of the limbs. This merely involves rotating around each of the rotation bivectors $A_i$ by the angle $\phi_i$, and stacking the results for each successive joint.

You should realize in this that the extension of $M_{i-1}$ to $M_i$ should be done by a multiplication on the *right* by the next rotation around the $A_i^*$-axis, since that is a transformation given in the next object frame. The explanation is independent of rotors and holds in general for the composition of operators. To perform an operator $Y$ (given in a local frame) when one is in the state $X$ implies that one should undo the present state rotor $X$ first (to get to the proper frame for application of $Y$), then do $Y$, and restore the frame by putting the result at $X$. Those operations are all performed by the customary left multiplication $(XYX^{-1})X = XY$, but the result is equivalent to the right multiplication of $X$ by $Y$.

The resulting run-time algorithm is now straightforward:

$$M_0 = 1 \qquad M_i = M_{i-1} e^{-A_i\phi_i/2}$$
$$Z_i^j = M_i Y_i^j \widetilde{M}_i$$

We can use the rigid body motions $M_i$ to draw the representative elements $Z_i^j$, giving a rendering of the moved arm as in Figure 14.9.

The universality of the transformation of the rendering elements $X_i^j$ is the essential difference with the usual homogeneous coordinate solution. You could also have obtained this functionality by computing with the homogeneous coordinate matrices throughout and applying the result as an outermorphism matrix in the final equation. In that case, you would still need to employ the conformal model to make that work on rendering elements that are not the flats of the homogeneous model.

### 14.6.2 Inverse Kinematics

In computer animation and robotics, *inverse kinematics* is the problem of finding parameters such as angles in a model to make it reach a certain specified position. Inverse kinematics is a notoriously hairy problem in geometrical computation and typically does not have a unique solution. Depending how it is hinged, each robot need its own specific solution to compute its joint angles. Closed solutions are rare, and typically numerical techniques are used.

The conformal model should be highly suited to represent this problem in Euclidean geometry, using its capability to compute directly with spatial quantities. Where a classically specified solution typically abounds in trigonometric functions because it tries to find a solution in terms of scalars (the angles), geometric algebra can avoid this almost completely. Instead, it computes spatial rotors by using intersections of spheres and ratios of lines. Trigonometry is only required if one wants angles as final results, and then involves a logarithm.

Having said that, these techniques have not yet been developed in great generality. To give a sample of what might be possible, we briefly discuss a very simple robot arm with a straightforward inverse kinematics algorithm, featuring some of the typical issues in such problems. The arm is of the humanoid type upper and lower limb, depicted in Figure 14.10, with limb lengths $\lambda_1$ and $\lambda_2$. The elbow is a simple planar hinge, but the shoulder is a spherical joint. With the shoulder fixed, we are asked to reach a target location $p$ with the wrist from a standard pose in which the arm is horizontally stretched out in the $\mathbf{e}_1$ direction. The limb lengths are given. The principle of the solution we follow is partly inspired by [34].

We choose our coordinate origin at the shoulder, with $\mathbf{e}_3$ as the vertical direction.

1. **The Tilt Plane.** There is an obvious degree of freedom in this problem: we can freely choose the plane in which we bend the elbow. This tilt plane contains the upper and lower arm. It certainly needs to contain the line $L$ through shoulder and wrist, which is

$$L = o \wedge p \wedge \infty.$$

Therefore it is natural to parameterize the tilt plane by a tilt angle of rotation around that line. We define the corresponding tilt rotor $R_t$ as

$$R_t \equiv \exp(\check{L}^*\phi/2),$$

where $\check{L}$ denotes the normalized $L$. To specify the direction of $\Pi_t$, we need a reference direction for the tilt plane. Let that be the vertical plane through $L$ (i.e., the plane $\Pi_0 = \mathbf{e}_3 \wedge L$). Then the actual tilt plane is

$$\Pi_t = R_t \Pi_0 \widetilde{R}_t.$$

2. **The Elbow Location.** The elbow needs to be in the tilt plane at the correct limb lengths from the shoulder and the wrist. We therefore set up two dual spheres: the shoulder sphere $\sigma_s \equiv o - \frac{1}{2}\lambda_1^2\infty$ and the wrist sphere $\sigma_w \equiv p - \frac{1}{2}\lambda_2^2\infty$. Their dual meet is the dual circle $\sigma_s \wedge \sigma_w$, and the intersection of that dual circle with the tilt plane is the elbow point pair $P_e$ given by

$$P_e = (\sigma_s \wedge \sigma_w) \rfloor \Pi_s.$$

This gives two possibilities for the elbow. The point pair $P_e$ can be split into its two components $P_e = p_- \wedge p_+$ by the technique in (14.13). We choose one of those as the elbow location $q$. The only concern here is consistency between subsequent solutions, and that is guaranteed by its automatic sign relationship to the orientation of the tilt plane.

The intersection may lead to an imaginary point pair. In that case there is no solution: the robot cannot reach the desired location. Whether this is the case is a simple test on the sign of $P_e^2$, which must be nonnegative for a real solution to exist.

3. **The Elbow Angle Rotor.** The elbow rotor $R_e$ is the rotor required to rotate from the lower arm direction given by the line $A = o \wedge q \wedge \infty$ to the upper arm direction $B = q \wedge p \wedge \infty$.

We saw in the vector space model that there are several cheap ways of determining a rotor between two directions (Section 10.3). It is a happy surprise that these methods all transfer immediately to conformal lines through any point by literal substitution of the lines for the vectors in those equations. They then yield the conformal rigid body rotor (including translation) to turn one line to the other.

It is not hard to see why this should be so. We consider two lines $U$ and $V$ relative to their common point $x$. Then the lines may be represented as $U = x \wedge \mathbf{u} \wedge \infty$ and $V = x \wedge \mathbf{v} \wedge \infty$. The constructions to quickly produce a rotor from the two normalized Euclidean directions $\mathbf{u}$ and $\mathbf{v}$ in Section 10.3 were based on the geometric product $\mathbf{u}\mathbf{v}$ and on the squared sum $\mathbf{u}+\mathbf{v}$ of the two direction vectors $\mathbf{u}$ and $\mathbf{v}$. These quantities are easily computed from the two lines. The geometric product of lines through the origin is the same as of their directions, for we can factor out the flat point at the origin: $UV = \mathbf{u}(o \wedge \infty)(o \wedge \infty)\mathbf{v} = \mathbf{u}\mathbf{v}$. Also, the sum of the two lines conveys the sum of the directions $U + V = x \wedge (\mathbf{u} + \mathbf{v}) \wedge \infty$, and geometric ratios with the square of that quantity therefore also reproduce the vector space results.

We pick the method of the sum of the lines in (10.13) and compute the local elbow rotor as

$$R_e = \frac{1 + VU}{\sqrt{2(1 + V \rfloor U)}}. \tag{14.12}$$

This equation is translation-covariant and holds at $x = 0$, so it is valid everywhere. It is the rotor of a rotation in the tilt plane, at the elbow $q$, over the correct angle.

4. **Shoulder Rotor.** The rotor $R_s$ for the shoulder angle of the spherical joint can be computed in a similar way. We use the two lines along the home position of the upper arm $A_0 = o \wedge \mathbf{e}_1 \wedge \infty$ and along its computed desired position $A = o \wedge q \wedge \infty$. That gives the spherical joint rotor $R_s$ by applying a formula such as (14.12). This rotor resides at the shoulder.

5. **Splitting the Spherical Joint.** Not every spherical joint controller can handle a rotation in the combined form of simultaneous rotations over its two degrees of freedom. In that case, we need to split $R_s$ into two rotors.

To be specific, let us assume that our arm needs to rotate first from the home position of the lower arm around the vertical axis $\mathbf{e}_3$, and then in a vertical plane.

To compute the first rotor, we simply compute the projected arm line onto the plane $\mathbf{e}_3^* = o \wedge \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \infty$ (call it $\Pi_3$):

$$A_1 = (A \rfloor \Pi_3)/\Pi_3.$$

This can also be computed more directly as the rejection $(A \wedge \mathbf{e}_3)/\mathbf{e}_3$. The rotor $R_1$ from $A_0$ to $A_1$ is then determined like (14.12). The remaining rotor is $R_2$ is determined by the condition that $R_1 R_2 = R_s$, so that $R_2 = \widetilde{R}_1 R_s$. This is a rotation in the plane of the original bivector $\mathbf{e}_1 \wedge \mathbf{e}_3$, but rotated by $R_1$.

6. **Determining the Angles.** All rotors we have determined are centered around their own points. The corresponding rotation angles follow from the Euclidean part of their logarithm (13.15), though it is actually more efficient to compute the vector space logarithm of (10.14) of their Euclidean part. (The outcome is the same, for taking the Euclidean part is the rejection of the rotor by $o \wedge \infty$, which is a covariant construction).

If this is a robotics problem, you may indeed have to go down to scalar angles to feed them to the joint controllers. But if this were an animation problem, you should keep the results in rotor form, for they can be used directly to render the elements that characterize the limbs in their correct location and attitude.

You see how this solution uses a combination of the capabilities of the conformal model to compute with offset planes and spheres, and of its natural reduction to the vector space model at each fixed location.

The implementation of such an algorithm for this particular robot performs about 40 percent faster than the implementation of the classical, angle-based solution [34]. The main reason for that is partly the avoidance of trigonometry, and partly the avoidance of representational switching that is typically required within a classical solution between its several efficient internal representations (from homogeneous coordinate matrices to quaternions and back, for instance).

---

## 14.7 Further Reading

The use of circles as elements of computation is not new. A fairly complete treatment may already be found in 19th century works [9, 10] and a later summary of such techniques is in the 1941 book by Forder [22]. No one seems to have realized explicitly that the system can be extended with Euclidean versors, though they do make obviously covariant constructions. That breakthrough came in 1999 with [31].

With elements like lines, circles, and rigid body motion rotors as primitives, the conformal model can be used to describe arbitrary shapes in terms of such descriptors. Rosenhahn [53, 54] has used this to do model-based tracking. His work is especially interesting for explicit structural switching between the projective geometry of observation (naturally described as linear transformations in the homogeneous model) and the desired accurate Euclidean reconstruction (for which the conformal model is most suited). This stratification of geometries is important.

Conformal geometric algebra can be used to perform target calibration in a more direct way than by iteratively treating translational and rotational components separately as we did in the vector space model of Section 10.4.2. The first results may be found in the work of Valkenburg et al. [62, 64].

---

## 14.8 Exercises

### 14.8.1 Drills

These drills intend to familiarize you with the form of common geometric elements and their parameters in the conformal model. We recommend doing them by hand first, and check them with interactive software later.

1. Give the direct representation of the point pair (0-sphere) $P$ spanned by the points $p_1$ and $p_2$ at location $\mathbf{e}_1$ and $\mathbf{e}_2$, with weights 2 and $-1$.

2. Compute center and radius of $P$.

3. Give the dual representation of $P$, and use it to compute radius and center.

4. Retrieve the locations of the original points from $P$ (see (14.13) below).

5. Compute the carrier line (see Section 15.2.2) of $P$, both in direct and dual form.

6. Give the direct representation of the circle $K$ through $p_1$, $p_2$, and the unit point at location $\mathbf{e}_3$.

7. Compute the squared radius and the center of the circle $K$.

8. Give the direct representation of the sphere $\Sigma$ through $K$ and the origin.

9. Compute the dual of $\Sigma$ and read off its center and squared radius directly from that dual representation.

### 14.8.2 Structural Exercises

1. The normalized sphere through four points $p$, $q$, $r$, $s$ is: $\Sigma = (p \wedge q \wedge r \wedge s)/(p \wedge q \wedge r \wedge s \wedge \infty)^*$. Show that the Euclidean vector pointing to the center of this sphere is

$$\mathbf{c} = (o \wedge \infty) \rfloor \left(o \wedge \infty \wedge \Sigma^*\right) = \left((o \wedge \infty) \rfloor \Sigma\right)^\star,$$

Note that the final rewriting involves the Euclidean dual. The first form is the rejection of the non-Euclidean parts from the dual. It is easily implemented as simply listing the Euclidean part of the normalized dual sphere.

2. The weight of a round spanned by four points is related to the volume of the simplex spanned by those points. Show that the weight of $p \wedge q \wedge r/2!$ is the area of the triangle $pqr$, and that the weight of the sphere $p \wedge q \wedge r \wedge s/3!$ is the volume of the tetrahedron $pqrs$.

3. The weight of a dual sphere $\sigma$ is the weight of its center, and equal to $\infty \cdot \sigma$. Dualize this expression to discover when a sphere through the points $p$, $q$, $r$, $s$ becomes zero.

4. In many computations resulting in a point pair $P$, you would like to have it in the factorized form $P = p_- \wedge p_+$, which is unique apart from scaling. Show that $p_+$ and $p_-$ can be computed as:

$$\text{point pair decomposition: } p_\pm = \frac{P \mp \sqrt{P^2}}{-\infty \rfloor P}. \tag{14.13}$$

(Hint: Simply substitute $P = p_- \wedge p_+$, and develop the terms in the formula; this shows why the formula works.)

5. For a flat point $P = p \wedge \infty$, (14.13) does not work, since it then requires division by a null vector. In that case, the simplest method is to retrieve the Euclidean position vector $\mathbf{p}$ and use that to make the point $p$. In an implementation, the coordinates of $\mathbf{p}$ are found as the coefficients of the basis blades $\mathbf{e}_1 \wedge \infty$, $\mathbf{e}_2 \wedge \infty$, and $\mathbf{e}_3 \wedge \infty$, divided by the coordinate of $o \wedge \infty$. Algebraically, show that

$$\mathbf{p} = -\frac{(o \wedge \infty) \rfloor (o \wedge P)}{(o \wedge \infty) \rfloor P}.$$

6. Show that the cosine of the angle between two lines $L$ and $M$ through a common point $p$ can be computed as the usual formula (3.5) directly applied to the lines themselves rather than to their directions.

7. Compute the meet of the dual circles $\kappa_1 = \mathsf{T}_{\mathbf{e}_2}[(o - \frac{1}{2}\infty)(-\mathbf{e}_3)]$ and $\kappa_2 = \mathsf{T}_{-\mathbf{e}_2}[(o - \frac{1}{2}\infty)(-\mathbf{e}_3)]$, both residing in the $\mathbf{e}_1 \wedge \mathbf{e}_2$-plane. It is a tangent vector---what is its weight, and how is that related to the geometry of the situation?

8. In any of the expressions for the direct or dual directions $\mathbf{E} \wedge \infty$, you can replace the outer product with a geometric product to write $\mathbf{E}\infty$. Why is a similar substitution not true for general tangents?

9. In Figure 14.7, the green line segments are part of the Voronoi diagram. The points of these segments should represent Euclidean circles. Draw these circles in the Euclidean space. Similarly, the edges of the Delaunay triangulation represent circles, but they are imaginary. Draw some of those. (For a hint, see Figure 15.8.)

10. Use (3.6) and (3.18) to show that

$$\|\infty \wedge X\|^2 = -\|\infty \rfloor X\|^2$$

for general $X$. (Remember that the squared norm is defined through $\|Y\|^2 \equiv Y * \widetilde{Y}$.)

11. Extending Figure 14.8, draw pictures displaying the inner product of two spheres when the center of one is contained inside the other sphere, and when one sphere is fully contained inside the other sphere.

---

## 14.9 Programming Examples and Exercises

### 14.9.1 Voronoi Diagrams and Delaunay Triangulations

This example uses `c2ga` (the 2-D conformal model implementation) to compute Voronoi diagrams and Delaunay triangulations. These geometric constructions were discussed in Section 14.4. The example lets the user drag 2-D points around, and create new ones.

The Voronoi diagrams and Delaunay triangulations are updated in real time, using the following steps:

- First, the 2-D points (including their `ni`-coordinate) are passed as a set of 3-D vectors to QHull, an existing library for computing convex hulls. The third dimension is of course the $\infty$-direction of the conformal model.
- The resulting convex hull is stored in a custom data structure called `DelaunayTriangulation`.
- Backface culling is used to remove the unwanted part of the convex hull.
- The Voronoi diagram or the Delaunay triangulation is drawn.

We explain each of the steps in more detail below. (Using QHull is a bit backwards, since QHull itself is able to compute Voronoi diagrams and Delaunay triangulations directly. However, implementing our own convex hull algorithm just for this example would be overdoing things.)

#### Passing the Points to QHull

QHull does not accept 2-D conformal points as input. So we have to collect the $\mathbf{e}_1$-, $\mathbf{e}_2$-, and $\infty$- coordinates into an array that can be passed to QHull:

```cpp
// the input points come from this array:
const std::vector<normalizedPoint> &points;

// We store the coordinates in the following array:
// 'coordT' is just a floating point type (e.g., float or double)
std::vector<coordT> qhCoord(points.size()*3);

// extract the e1-, e2-, ni-coordinates for each point:
for (unsigned int i = 0; i < points.size(); i++) {
    qhCoord[i * 3 + 0] = points[i].e1();
    qhCoord[i * 3 + 1] = points[i].e2();
    qhCoord[i * 3 + 2] = points[i].ni();
}

// pass 'qhCoord' to QHull
// ...
```

Note that `p.ni()` actually retrieves the $\infty$-coordinate of a point $p$, which would algebraically be denoted as the operation $-o \cdot p$, involving `no` rather than `ni`.

#### Storing the Hull in a DelaunayTriangulation

QHull returns the convex hull as a set of triangles. The vertices of the triangles are the same points that were originally passed to QHull (i.e., no new points are created). The example stores the convex hull in a class called `DelaunayTriangulation`. This class contains an array of `DelaunayTriangle`s, and an array of `DelaunayVertex`es:

```cpp
class DelaunayTriangulation {
public:
    // ... (Constructors, etc)

    std::vector<DelaunayVertex> m_vertices;
    std::vector<DelaunayTriangle> m_triangles;
};
```

Each `DelaunayVertex` contains a `normalizedPoint` that specifies its position. Each `DelaunayTriangle` contains an array of three vertices and an array of three neighboring triangles (both specified by their index). A `DelaunayTriangle` also contains a `circle` that passes through all three vertices, as described next.

#### Backface Culling

The convex hull is fully closed, but we do not need the triangles that close the top of the paraboloid, as these are not part of the Delaunay triangulation. Fortunately, QHull abides by the counterclockwise-orientation rule for triangles (see Section 2.13.2), so that we can use backface culling to remove the unwanted triangles. Here we compare the orientation of the circles spanned by the vertices of each triangle to the free bivector $\mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \infty$:

```cpp
// 'DT' is a DelaunayTriangulation
// get the vertices of the triangle:
DelaunayVertex &V1 = DT.m_vertices[vtxIdx[0]];
DelaunayVertex &V2 = DT.m_vertices[vtxIdx[1]];
DelaunayVertex &V3 = DT.m_vertices[vtxIdx[2]];

// Check if 'front-facing':
// 1: Compute the circle spanned by the three vertices:
circle C = _circle(V1.m_pt ^ V2.m_pt ^ V3.m_pt);

// 2: Compare orientation:
if (_Float(C << (e1 ^ e2 ^ ni)) < 0.0)
    continue; // do not use this triangle

// else: this triangle is valid
```

The circle `C` is stored along with each triangle for later use; the center point of the circle is a vertex of the Voronoi diagram.

#### Drawing the Result

Drawing the Delaunay triangulation from a `DelaunayTriangulation` is straightforward. Drawing the Voronoi diagram is less so. First, we need to find the neighbors of every Delaunay triangle, on a per-edge basis. This is computed when the `DelaunayTriangulation` is initialized and stored in each `DelaunayTriangle`. With this information available, drawing the Voronoi diagram is done by connecting the center points of neighboring triangles with line segments. For each edge that does not have a neighboring triangle, we draw a (dashed) line from the center point through the midpoint of the edge.

### 14.9.2 Exercise: Drawing Euclid's Elements

This example provides the bare-bones code to draw Euclid's elements (i.e., all flat, round, free, and tangents blades of the conformal model). It is your job to fill in the code that creates a typical element of each class and grade. You'll have to give each element the appropriate size and orientation, such that the end result looks somewhat like Figure 14.12.

Note that you could copy the coordinates directly from the figure, but then you might as well go straight to the solution that is provided with the GA sandbox source code package. An example of the code you have to complete is

```cpp
name = "flat point";
X = no; // <-- EXERCISE: insert correct primitive (flat point) here
```

### 14.9.3 Conformal Primitives and Intersections

In this example we repeat the blade visualization example of Section 11.13.2, only this time in the conformal setting that considerably extends the blades to be drawn. Again the user can create and drag points, and create primitives by selecting a number of these points. The primitives that can be constructed are lines, planes, circles, and spheres.

The example draws all these primitives and their intersections. A screenshot is shown in Figure 14.13.

A circle is created by selecting three points. If one of these points is the point at infinity---which for this occasion is located conveniently in the upper-right corner of the viewport---then a line is created. Circles and lines can be computed using the same code, because a line is just a special type of circle (i.e., one that passes through infinity):

```cpp
circle C = _circle(g_points[pointIdx1] ^ g_points[pointIdx2] ^
    g_points[pointIdx3]);
```

Spheres and planes are created by selecting four points, and computed as follows:

```cpp
sphere S = _sphere(g_points[pointIdx1] ^ g_points[pointIdx2] ^
    g_points[pointIdx3] ^ g_points[pointIdx4]);
```

Again, a plane is a special type of sphere for which one of the selected points is infinity.

The intersections of the primitives are computed by the following code, which spells out the meet:

```cpp
// P1 and P2 are two multivectors (the primitives)
I = unit_e(join(P1, P2));
mv intersection = (P1 << I) << P2;
```

As in Section 11.13.2, we use orthogonal projection to enable the creation of degenerate situations.

```cpp
// P1 and P2 are two multivectors (the primitives)
mv projection = (P1 << inverse(P2)) << P2;

// check if projection of P1 onto P2 is 'close' to P1
const float CLOSE = 0.02f;
if (_Float(norm_e(projection - P1)) < CLOSE) {
    // yes: P1 = projection of P1 onto P2
    P1 = projection;
}
```

This projection step is of course performed before the intersection test, not after. Note that orthogonal projections involving round conformal objects do not behave as you would expect, as this would result in conics (which the conformal model obviously cannot represent). For more details, see Section 15.3.

#### Creating Points

Just as in Section 11.13.2, new points can be created by a mouse-click. The user then expects a point to appear under the mouse cursor. The code to create a point at the correct location is very similar to that in Section 11.13.2, except that this time we use a versor to apply the inverse modelview transformation (in the homogeneous example, we constructed an outermorphism directly from the inverted modelview matrix):

```cpp
// create point at required location and 'distance'
point pt = _point(c3gaPoint(_vectorE3GA(vectorAtDepth(distance,
    mousePos) - e3 * distance)));

// retrieve modelview matrix from OpenGL:
float modelviewMatrix[16];
glGetFloatv(GL_MODELVIEW_MATRIX, modelviewMatrix);

// convert modelview matrix to versor:
bool transpose = true;
TRversor V = _TRversor(matrix4x4ToVersor(modelviewMatrix, transpose));

// apply (inverse) OpenGL 'versor' to transform the point to the
// global frame
pt = inverse(V) * pt * V;
```

The function `matrix4x4ToVersor()` will be discussed in Section 16.10.1. It converts 4x4 translate-rotate-scale matrices into conformal versors.

### 14.9.4 Fitting a Sphere to a Set of Points

This example implements the equations for fitting a sphere from Section 14.5. The user can drag and create points, as in the previous example. The program tries to fit a sphere to these points as well as it can under the least-squares condition. As noted in Section 14.5, the minimization criterion has a preference for small spheres.

The code is straightforward to implement given the algorithm that was spelled out in Section 14.5:

- The matrix $P = \sum_i [\![p_i]\!] [\![p_i]\!]^T$ is computed;
- Then, the metric matrix $M$ is initialized;
- The product of these matrices is computed `PM = P * M`;
- The singular value decomposition (SVD) is computed, resulting in the matrices `U`, `S`, and `V`;
- The coordinates of the dual sphere `DS` are set to the last column of `V`.

```cpp
dualSphere fitSphere(const std::vector<point> &points) {
    float P[5 * 5];

    // compute matrix P = sum_i (points[i] . points[i]^T)
    {
        // first clear all entries:
        for (int i = 0; i < 5 * 5; i++) P[i] = 0.0f;

        // fill the matrix:
        for (unsigned int p = 0; p < points.size(); p++) {
            // get coordinates of point 'p':
            const mv::Float *pc = points[p].getC(point_no_e1_e2_e3_ni);
            for (int i = 0; i < 5; i++)
                for (int j = i; j < 5; j++) {
                    P[i * 5 + j] += pc[i] * pc[j];
                    P[j * 5 + i] = P[i * 5 + j];
                }
        }
    }

    // initialize the metric matrix:
    float M[5 * 5] = {
        //  no     e1     e2     e3     ni
        0.0f,  0.0f,  0.0f,  0.0f, -1.0f,  // no
        0.0f,  1.0f,  0.0f,  0.0f,  0.0f,  // e1
        0.0f,  0.0f,  1.0f,  0.0f,  0.0f,  // e2
        0.0f,  0.0f,  0.0f,  1.0f,  0.0f,  // e3
       -1.0f,  0.0f,  0.0f,  0.0f,  0.0f   // ni
    };

    // construct OpenCV matrices (on stack)
    CvMat matrixP = cvMat(5, 5, CV_32F, P);
    CvMat matrixM = cvMat(5, 5, CV_32F, M);

    // use OpenCV to multiply matrices
    float PM[5 * 5];
    CvMat matrixPM = cvMat(5, 5, CV_32F, PM);
    cvMatMul(&matrixP, &matrixM, &matrixPM);

    // use OpenCV to compute SVD
    float S[5 * 5], U[5 * 5], V[5 * 5];
    CvMat matrixS = cvMat(5, 5, CV_32F, S);
    CvMat matrixU = cvMat(5, 5, CV_32F, U);
    CvMat matrixV = cvMat(5, 5, CV_32F, V);
    int flags = 0;
    cvSVD(&matrixPM, &matrixS, &matrixU, &matrixV, flags);

    // extract last column of V (coordinates of dual sphere);
    dualSphere DS(dualSphere_no_e1_e2_e3_ni,
        V[0 * 5 + 4], V[1 * 5 + 4], V[2 * 5 + 4], V[3 * 5 + 4], V[4 * 5 + 4]);

    return DS;
}
```

The OpenCV library is used to implement the linear algebra operations (matrix multiplication and SVD).

Interestingly, the sphere-fitting-algorithm will come up with a plane when this is the optimal solution! As an easy way to create this situation, we have provided an option in a popup menu that projects all points onto the $\mathbf{e}_3^*$ plane.
