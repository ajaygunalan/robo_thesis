# 15 Constructions in Euclidean Geometry

Now that the previous chapters have given us such a range of elements of Euclidean geometry as the blades in the conformal model, we want to combine them into useful constructions. As always, this is no more than the application of operations we introduced in Part I, but they take on intriguing and useful meanings.

The `meet` is greatly extended in its capabilities to intersect arbitrary flats and rounds (though always with the same formula $X \cap Y = Y^* \rfloor X$), or to compute other incidences. The results can be real or imaginary, or even the infinitesimal tangents. The dual of the `meet` provides a novel operation: the `plunge`, which constructs the simplest element intersecting a given group of elements perpendicularly. Once recognized, you will spot it in many constructions, and it enables you to quickly write down correct expressions for, say, the contour circle of a sphere seen from a given point.

We show how all the various concepts of a vector in classical geometry find their specific expression in the conformal model. Normal vector, position vector, free vector, line vector, and tangent vector now all automatically move in the correct way under the same Euclidean rotors. This demonstrates clearly that the conformal model performs both the geometrical computations and the "data type management" required in Euclidean geometry.

We conclude with a sample analysis of some involved planar geometry (the geometry of a Voronoi cell), and compare the coordinate-free conformal solution to the many parameters involved in even just specifying the classical solution.

---

## 15.1 Euclidean Incidence and Coincidence

The basic constructions in geometric algebra are spanning and intersection. In the vector space model prevalent in Part I, these were fairly straightforward operations on subspaces through the origin. They still are in the representational space of the conformal model, but their interpreted Euclidean consequences deserve careful study. They offer a rich syntax for a constructive and consistent specification language for Euclidean geometry.

### 15.1.1 Incidence Revisited

We have encountered the `meet` in a general context in Chapter 5. Within the conformal model, we used it in the previous chapter to construct elements by intersection with other elements. Since the basic elements of point, sphere, and plane are all dually represented as vectors, it was easiest to study the `meet` in its dual form:

$$(A \cap B)^* = B^* \wedge A^*.$$

If your application involves a lot of intersections, it is often convenient to stay in the dual representation. However, you should still be careful: the duality in the `meet` needs to be taken relative to the `join`, which may change for successive `meet` operations, so you may not be able to use a single dual representation of an element for all its uses.

The principle of the `meet` is that it constructs the largest subblade common to the blades $A$ and $B$. The duality relative to the `join` constructs the complements within the smallest blade containing both; these complements do not contain common factors, so that their outer product is nonzero. In that sense, they are independent blades. With that, the containment relationship that gives us the `meet` is easily verified in its dual form:

$$0 = x \rfloor (A \cap B)^* = x \rfloor (B^* \wedge A^*) = (x \rfloor B^*) \wedge A^* + \widehat{B^*} \wedge (x \rfloor A^*),$$

and the constructed independence of $A^*$ and $B^*$ then implies that $x$ is contained in $(A \cap B)$ if and only if it is contained in both $A$ and $B$. This is easily extended by associativity. Three intersecting spheres, dually represented by $a$, $b$, $c$, will `meet` in the point pair $(a \wedge b \wedge c)^{-*}$ (where the `join` is the full pseudoscalar); see Figure 15.1(a).

In the conformal model, the `meet` of two elements may be imaginary. For instance, the `meet` of three spheres that do not really intersect is an imaginary point pair. The dual of this imaginary point pair is a real circle; see Figure 15.1(b). When we draw that using visualization software, we find that this real circle intersects the original spheres perpendicularly. This bears investigating: can we construct elements that perpendicularly intersect other elements by taking the dual of the `meet`?

**Figure 15.1:** (a) The `meet` of three intersecting dual spheres $a$, $b$, $c$ is the real point pair with dual representation $c \wedge b \wedge a$ (in blue), whereas their `plunge` is an imaginary (dashed) circle. (b) The `plunge` of three nonintersecting spheres is the circle with direct representation $c \wedge b \wedge a$ (in green), while their `meet` is an imaginary (speckled) point pair. To assist 3-D interpretation, some real intersection circles are indicated in red.

### 15.1.2 Co-incidence

Let us consider what kind of element is constructed by the dual operation to the `meet`. Its definition would be that its *direct* representation is $B^* \wedge A^*$. If we call the `meet` the incidence, we could call this "co-incidence", in the algebraic jargon that associates "co-" with "dual."

When we treated the scalar product in Section 3.1.4, we saw that two blades $A$ and $B$ of the same grade are orthogonal to each other when their scalar product is zero. This is equivalent to the scalar product of their duals being zero, since the scalar product of elements or their duals differ only by a sign (do structural exercise 1 if you want to know which sign). For blades of nonequal grades, this extends to their contractions, although the order now matters (since the contraction of a higher-grade blade onto a lower-grade blade is trivially zero anyway). For a blade $X$ of grade smaller than $A$ to be perpendicular to $A$, we must have

$$X \perp A \iff X \rfloor A = 0.$$

Algebraically, when you write out $X$ and $A$ in their factors, the common parts of $X$ and $A$ produce a scalar, and the result then reduces to orthogonality of one of the remaining factors of $X$ with all the remaining factors of $A$.

Suppose we have two blades $A$, $B$, and are looking for the Euclidean object $X$ that is perpendicular to each. We therefore need to satisfy $X \rfloor A = 0$ and $X \rfloor B = 0$. Dualizing this we get $X \wedge A^* = 0$ and $X \wedge B^* = 0$. By choosing the duality relative to the `join` of the two blades $A$ and $B$, we can make $A^*$ and $B^*$ to be independent blades, just as we did for the `meet` above. This prevents their outer product from being trivially zero. A blade $X$ of lowest grade orthogonal to every non-scalar factor in $A$ and $B$, and hence

$$X = B^* \wedge A^*,$$

where the order was chosen to correspond to the convention for the `meet`.

Whereas the `meet` constructs a representation of an object *in common* with given elements, this operation of plunging (our term) constructs the representation of an object that is *most unlike* other elements, in the orthogonal sense that it intersects them *perpendicularly*. We coined the term `plunge` (which according to Webster's dictionary may be etymologically related to plumb) to give the feeling of this perpendicular dive into its arguments. Since perpendicularity is a metric concept, the `plunge` is a truly metric operation, whereas the `meet` is not. The `plunge` is an elementary construction in Euclidean geometry that deserves to be better known. It is occasionally found in older works in the Grassmannian tradition [9, 22].

With the associativity of the outer product, the `plunge` easily extends to more elements, so that the general element perpendicular to $A_1$, $A_2$, and so on, has the direct representation $X = \cdots \wedge A_2^* \wedge A_1^*$. The `plunge` of three spheres, as in Figure 15.1(b), is therefore a circle:

$$X = C^* \wedge B^* \wedge A^*.$$

Shrinking the dual spheres to zero radius so that they become points, you see that the `plunge` gives a circle through those points, consistent with our earlier derivation of the interpretation of such an element $c \wedge b \wedge a$, with $a$, $b$, and $c$ point representatives. We now see that to contain a point $a$ is equivalent to plunging into the zero-radius sphere $a^{-*}$ at that point. Letting the radius of a dual sphere go to infinity gives a dual plane; the `plunge` of such diverse elements can be mixed easily, as Figure 15.2 shows.

**Figure 15.2:** The `plunge` $c \wedge b \wedge a$ of dual plane $c$, dual sphere $b$, and point $a$.

### 15.1.3 Real Meet or Plunge

The `meet` and the `plunge` are clearly each other's dual relative to the `join`. Moreover, should the result of one of them be imaginary, the other is real. This can only happen for rounds (since flats are always real). That principle helps with finding and visualizing an imaginary `meet`.

Take again the three spheres of Figure 15.1(b). They do not intersect and therefore have an imaginary point pair as their `meet`. This implies that their `plunge` is a real circle. This imaginary point pair and the real circle are algebraically each other's dual. Geometrically, this duality is a polar relationship on the unique smallest sphere containing either point pair or circle (or both, since they are on the same sphere). This is easily shown from the standard representation of such rounds:

$$\left((o + \tfrac{1}{2}\rho^2 \infty) \mathbf{E}\right)^* = (o - \tfrac{1}{2}\rho^2 \infty) \mathbf{E}^\star (-1)^n.$$

If the former is a real circle on the sphere with squared radius $\rho^2 > 0$, then $\mathbf{E}$ is of grade 2; in a 3-D Euclidean space the latter is then a point pair on the imaginary sphere of the same radius (since $\mathbf{E}^\star$ is of grade 1). That locates the imaginary `meet`.

> *If a circle is considered as the real equator of a sphere, its dual is the imaginary point pair that form the poles. Vice versa, the dual of a real point pair is the imaginary equator of a sphere that has the point pair as its poles.*

Knowing this polar relationship of `meet` and `plunge`, we can also determine the location of the imaginary circle that is the `meet` of two nonintersecting spheres, as indicated in Figure 15.3(a). The `plunge` of the two spheres is a point pair (indicated in blue). The location of this point pair is found by realizing that any sphere that is perpendicular to both spheres should contain it (since the `plunge` is an associative operation), and so should every circle, plane, or line perpendicular to both spheres. The simplest way to localize it is then as the intersection of the line through the centers (which is clearly perpendicular to both spheres) and the unique perpendicular sphere with its center on this line, as indicated in Figure 15.3(a) (in white). That is precisely the sphere on which we should determine the `meet` as the dual to this point pair, which is the imaginary equator indicated as a dashed circle in Figure 15.3(a) (in green). We will give the formula for this sphere in Section 15.2.3.

Once you know how to find this round that contains both `meet` and `plunge`, their visualization is easy, whether they are imaginary or not. Verify that this indeed gives the localization of both in Figure 15.3.

**Figure 15.3:** The `meet` and `plunge` of two spheres at increasing distances. When they do not intersect (a,c), the red dual spheres have a real `plunge` and an imaginary `meet`. When they do intersect (b), the `meet` is real and the `plunge` imaginary. In all cases `meet` and `plunge` are each other's dual (i.e., polars on the three white spheres). Imaginary elements are depicted as speckled.

### 15.1.4 The Plunge of Flats

The construction of a general flat $p \wedge \mathbf{E} \wedge \infty$ can also be interpreted as a `plunge`. As a definite example, let us interpret the line $p \wedge \mathbf{u} \wedge \infty$. According to the `plunge` construction, this should perpendicularly intersect the points $p$ and $\infty$ (so that it contains them), and it should moreover be perpendicular to $\mathbf{u}^*$, which is the plane through the origin with normal vector $\mathbf{u}$. Obviously, this `plunge` must then be the direct representation of the line through $p$ in the $\mathbf{u}$ direction. This is illustrated in Figure 15.4(a). Including another Euclidean vector factor $\mathbf{v}$ gives an element that should meet the dual line $\mathbf{u} \wedge \mathbf{v}$ perpendicularly, and is therefore the direct representation of a plane. Removing the Euclidean factor (by setting it equal to the 0-blade 1) gives the representation of a flat of dimension zero (i.e., a direct flat point $p \wedge \infty$, which is the element that perpendicularly connects the small dual sphere $p$ with the point at infinity $\infty$).

Now let us revisit the object $p \rfloor (c \wedge \infty)$ from (14.4), which contains such a flat point in its construction. It was a dual sphere through the point $p$, with center $c$. Undualizing this, we find that it is the direct object

$$S = p \wedge (c \wedge \infty)^{-*}.$$

**Figure 15.4:** (a) The `plunge` construction of the line $p \wedge \mathbf{u} \wedge \infty$. (b) Visualization of the point $c \wedge \infty$ and its consistency with constructing the dual sphere $p \rfloor (c \wedge \infty)$, given a point $p$.

We see that this indeed contains $p$ (it `plunge`s into $p$ since it is a direct representation of the form $p \wedge$), and that we should think of it as also plunging into the flat point $c \wedge \infty$. We have just seen that such a flat point in itself is the `plunge` of $c$ and $\infty$, connecting those two dual elements. We observe that we get an intuitively satisfying picture like Figure 15.4(b), in which the flat point $c \wedge \infty$ has "hairs" extending from $c$ to infinity. Intersecting all of those perpendicularly while also passing through the given point $p$ must produce a sphere.

Carrying this type of thinking to its logical extreme, we can also interpret a purely Euclidean blade such as $\mathbf{v} \wedge \mathbf{u}$ as a direct element of our geometry. Since it is a purely Euclidean 2-blade, we have already met it as the dual representation of the line that is the `meet` of the two dual planes $\mathbf{u}$ and $\mathbf{v}$ passing through the origin. But if we interpret $\mathbf{v} \wedge \mathbf{u}$ directly, it should be the `plunge` of the two planes represented dually by $\mathbf{u}$ and $\mathbf{v}$ (i.e., the general element that is perpendicular to both).

Any cylinder with their common line as its axis is a solution, so this is like a nest of cylinders of arbitrary radius but fixed axis. However, as soon as we try to pick out one of the cylinders by specifying a point $p$ on it, the element $p \wedge (\mathbf{v} \wedge \mathbf{u})$ is a unique circle. So a more accurate description is that $\mathbf{v} \wedge \mathbf{u}$ represents a stack of nests of circles. But that is also not quite right, since these elements are not circles yet (we have specified only a grade 2 object, not grade 3); rather, $\mathbf{v} \wedge \mathbf{u}$ is a stack of nests of potential circles. This may seem like an uncommon object, until you realize that a rotation rotor can be made from this dual line $L^* = \mathbf{v} \wedge \mathbf{u}$ as $\exp(\alpha \, \mathbf{v} \wedge \mathbf{u})$. Then the element $L^* = \mathbf{v} \wedge \mathbf{u}$ in fact describes a collection of orbits of the rotating points, as indicated in Figure 15.5 (in which the actual orbits $p \wedge L^*$ are drawn).

**Figure 15.5:** The circular orbits of a line $L$, which are $p \wedge L^*$ for various points $p$. The orbits of points on the line are tangent bivectors, depicted as small oriented disks.

The point of all this discussion is that the conformal model suggests, in its algebraic coherence, a consistent and rich language for Euclidean geometry. It contains objects that we have not seen this explicitly before, but that on closer scrutiny represent familiar geometric concepts, and endows them with precise computational properties. Now that we have an algebraic way to combine them, it pays to try and get them into more practical form into our intuition, so that we can use them as active concepts in the solution of problems. This takes practice, and we recommend playing with interactive software packages like GAViewer to absorb this into your intuition---the old-fashioned derivations on paper are rather useless for this (though they should be used to check and/or prove the correctness of your new insights).

---

## 15.2 Euclidean Nuggets

When you work with the conformal model in a practical application, you will find that you often need to convert elements, and that certain operations appear to be useful nuggets, occurring again and again. We provide some in this section, and try to discern some patterns. This is certainly not a complete inventory of such elementary constructions. We hope that the techniques we expose in deriving them will give you the skills to derive your own special expressions, should your application require them.

### 15.2.1 Tangents Without Differentiating

When you need the tangent to a flat $\Pi$ or to a round $\Sigma$ passing through one of its points $p$, you can compute this without differentiation. Calling the element $X$ (so that $p \wedge X = 0$), its tangent is

$$\text{tangent to } X \text{ at } p: \quad p \rfloor \hat{X} \tag{15.1}$$

The tangents are illustrated in Figure 15.6.

The formula is easy to prove for a flat through the origin: $o \rfloor (o \wedge \mathbf{E} \wedge \infty)^\wedge = o \wedge \mathbf{E}$, and because of Euclidean covariance, this holds everywhere for any flat. For a round the proof is also most simply done at the origin $o$. A direct round through $o$ with center $c$ and direction $\mathbf{E}\infty$ is $o \wedge \left(c \rfloor (-\mathbf{E}\infty)\right)$, according to structural exercise 4. Then the proposed formula (15.1) gives, by straightforward computation, that the tangent equals $o \wedge (\mathbf{c} \rfloor \mathbf{E})^\wedge$, which is the correct result in its geometrical aspects: its directional part is an element of the carrier $\mathbf{E}$, perpendicular to the radial vector. Note that this local tangent blade is weighted by the magnitude of the radial vector $\mathbf{c}$, which is the radius $\rho$. The occurrence of $\rho$ (rather than $\rho^2$) may seem to require complex numbers for imaginary rounds. However, imaginary rounds contain no real points, so they have no real tangents either.

**Figure 15.6:** The tangents of flats and rounds at one of their points are simply computed by the contraction. No differentiation is required.

### 15.2.2 Carriers, Tangent Flat

Let us define the *carrier* of an element as the smallest grade flat that contains it. A flat is therefore its own carrier. The carrier of a round $\Sigma$ (which may be a tangent) is

$$\text{carrier of round } \Sigma: \quad \Sigma \wedge \infty.$$

This is easily proved: $\left((c + \tfrac{1}{2}\rho^2 \infty) \wedge \mathbf{E}\right) \wedge \infty = c \wedge \mathbf{E} \wedge \infty.$

We can use this to compute the *tangent flat* to an element $X$ at one of its points $p$ as $(p \rfloor \hat{X}) \wedge \infty$. This applies to rounds and flats alike; though for a flat it is the identity. Tangents do not have tangent flats, though they do have a carrier.

### 15.2.3 Surrounds, Factorization of Rounds

A round $\Sigma$ can be surrounded by the smallest sphere containing it. In its dual representation, that *surround* of $\Sigma$ is

$$\text{surround of round } \Sigma: \quad \frac{\Sigma}{\Sigma \wedge \infty}, \tag{15.2}$$

in which the division denotes right division (i.e., $\Sigma (\Sigma \wedge \infty)^{-1}$). This even applies to tangents, but it then returns the locational point of the tangent, in agreement with the intuition that a tangent has zero size. Formula (15.2) can be interpreted as the dual of $\Sigma$ relative to the carrier of dimension $k$; therefore the expression equals $(c - \tfrac{1}{2}\rho^2\infty)(-1)^k$, which is a dual sphere containing $\Sigma$. We prove the surround formula below.

If the round $\Sigma$ is given in its dual form, you need the dual of (15.2):

$$\text{surround of dual round } \sigma: \quad (-1)^k \frac{\hat{\sigma}}{\infty \rfloor \sigma}. \tag{15.3}$$

The signs ensure that the computed surround is the same as before, but you could ignore them.

A round can be factored as the geometric product of its surround and its carrier:

$$\text{factorization of a round } \Sigma: \quad \Sigma = \left(\frac{\Sigma}{\Sigma \wedge \infty}\right) (\Sigma \wedge \infty), \tag{15.4}$$

and its dual is

$$\text{factorization of a dual round } \sigma: \quad \sigma = \left(\frac{\sigma}{\infty \rfloor \sigma}\right) (\infty \rfloor \sigma), \tag{15.5}$$

in which you need to include the $(-1)^k$ (as in (15.3)) if you need the proper orientation of the surround. These unique factorization formulas are the motivation behind the expression for the surrounding sphere. It is easy to show that the center of the surrounding sphere is in the carrier plane; and then (15.4) actually represents the perpendicular `meet` of carrier and surround. This makes the factorization geometrically very natural (see Figure 15.7). Algebraically, this factorization in orthogonal factors is important in symbolic simplification of formulas involving rounds. Given a round like a circle, such a factorization gives us a better understanding of it: the carrier plane gives us direction, weight, and orientation of the circle, and the sphere gives us its location (i.e., center) and size (i.e., radius squared).

**Figure 15.7:** The factorization of rounds, using their carrier and surround. A point pair $P$ is factorized as the intersection of its surrounding dual sphere $P/(P \wedge \infty)$ and the carrier line $P \wedge \infty$. A circle $K$ is factorized as the intersection of the dual surrounding sphere $K/(K \wedge \infty)$ and the carrier plane $K \wedge \infty$.

A special case is a point pair, for which the same formulas hold, for it is clearly also a round. Now $\Sigma \wedge \infty$ represents the carrier line, and division again gives the containing sphere, as shown in Figure 15.7. The result is an expression for *the smallest sphere containing two points*:

$$\frac{p \wedge q}{p \wedge q \wedge \infty} = \frac{(p \wedge q) \rfloor (p \wedge q \wedge \infty)}{-2p \cdot q} = -\tfrac{1}{2}\left(p + q + (p \cdot q)\infty\right).$$

The overall sign in this makes the `meet` correct, but you can ignore it if you are not interested in such matters of orientation.

For the proof of the correctness of the surround formula (15.2), we need to show that the center of the surround is in the carrier plane. So we reflect the surround in that plane and verify that this merely changes the surround by a sign. Using the reflection formula for a dual element into a directly represented mirror (from Table 7.1), we find that the derivation is quicker when we reflect in the inverse of the carrier (which makes no difference geometrically). We obtain

$$(\Sigma \wedge \infty)^{-1} \left(\Sigma (\Sigma \wedge \infty)^{-1}\right) (\Sigma \wedge \infty) = (\Sigma \wedge \infty)^{-1} \Sigma = \widetilde{\Sigma} (\Sigma \wedge \infty)^{-1},$$

so that this dual sphere becomes a signed multiple of itself (in the final transition, we took the reverse and computed the resulting sign, after realizing that the reverse of a vector is the vector itself). It follows that the center of the sphere is on the mirroring carrier. As a consequence, the outer product of the dual surround sphere with the carrier must be zero; therefore you can replace the geometric product in (15.4) with a contraction, showing clearly that it expresses a `meet` of the carrier with the surround (in that order).

### 15.2.4 Affine Combinations

An affine combination of two normalized points gives a 1-parameter family of normalized dual spheres (so *not* of points!):

$$\lambda p + (1 - \lambda) q. \tag{15.6}$$

The corresponding dual spheres are depicted in Figure 15.8 for the 2-D case. As $\lambda$ becomes infinite, the dual sphere approaches the midplace $p - q$ (with enormous weight).

**Figure 15.8:** Affine combinations of the point $p$ (red) and $q$ (blue) in the plane are dual circles. The amount of each point is indicated by the color mixture. Imaginary circles result for some values; they have been dashed, and their centers follow the regular affine interpolation.

These dual spheres all intersect the smallest dual sphere through $p$ and $q$ orthogonally, as you may easily verify:

$$\left(\lambda p + (1 - \lambda) q\right) \rfloor \left(\tfrac{1}{2}(p + q) + \tfrac{1}{2}(p \cdot q) \infty\right) = 0.$$

Their radius squared is $-\lambda(1 - \lambda) d_E^2(p, q)$, so that imaginary dual spheres result for $0 < \lambda < 1$. (Those imaginary dual spheres do not look orthogonal to the smallest containing sphere in Figure 15.8, but their inner product with it is indeed zero.) Comparing this to the treatment in the homogeneous model where this affine combination is used in Section 11.2.3 to obtain the points between $p$ and $q$, we find that the centers of the resulting dual spheres certainly behave exactly like the locations in the affine interpolation, though they are surrounded by imaginary dual spheres for the values of interest. To mimic that interpolation precisely within the conformal model, you should interpolate flat points rather than zero-radius dual spheres: $\lambda (p \wedge \infty) + (1 - \lambda) (q \wedge \infty)$ is the flat point at location $\lambda \mathbf{p} + (1 - \lambda) \mathbf{q}$.

Within the conformal model, other affine combinations become feasible. The affine combinations of flats are a simple extension of those seen in the homogeneous model in Section 11.2.3 and require little explanation. As there, 3-D lines can only be added if they have a finite point in common, which implies in the conformal model that they have two points in common, one of which is the point at infinity. Two circles $K_1$ and $K_2$ can now also be affinely combined, but like lines only if they have a point pair in common (which may be imaginary, as it usually is for two circles in a common plane); their sum then sweeps out circles on the common sphere $K_1 \cup K_2$ also containing the point pair, as illustrated in Figure 15.9(a). Similarly, two point pairs can be combined affinely if they have one point in common, and the results are point pairs that sweep out the circle that is their `join`, illustrated in Figure 15.9(b).

**Figure 15.9:** Affine combination of circles (a) and point pairs (b). These only generate other objects if they form a 1-parameter family, which implies that they should have a point pair or point in common, respectively. We show equal increments of the affine parameter to demonstrate its nonlinear relationship to angles or arcs.

All these additive combinations transform covariantly, so they are geometrically sensible constructions. But you should avoid using them, for they parameterize the intermediate elements awkwardly. It is much more preferable to use the two generative elements to produce a *rotor* that affects the transformations; its parameters can be directly interpreted as angles and scalings of the intermediate elements. We develop that technique in the next chapter.

---

## 15.3 Euclidean Projections

In geometric algebra, the projection of a blade $X$ onto a blade $P$ is another blade:

$$X \mapsto (X \rfloor P)/P, \tag{15.7}$$

where the division uses the geometric product. Applying this to the conformal model, we find the expected projection behavior if $X$ is a flat (as we will show below when discussing Figure 15.10(b)).

But when $X$ is a round, this is not the projection you might expect. For instance, consider Figure 15.10(a), the projection of a circle onto a plane. You may have hoped for an ellipse, but an ellipse is not represented by a blade in our model, and therefore cannot be the outcome of (15.7). Instead, the result of the projection of a circle onto a plane is a particular circle. To explain this effect, and derive precisely which circle, we recall (11.17):

$$A \cap (X \wedge A^{-*}) = (X \wedge A^{-*})^*_A = (X \rfloor A) \rfloor A.$$

So the projection is proportional to the `meet` of $A$ with $X \wedge A^{-*}$ (by the magnitude $A^{-2}$). In our Euclidean situation, the latter is the `plunge` of $X$ into $A$: it contains $X$ and intersects $A$ perpendicularly. In the case of projecting a circle onto a plane, we indeed get the construction of Figure 15.10(a), resulting in a circle that is the equator of the sphere that plunges into the plane and contains the circle $C$.

It is instructive to see what happens for flats, for instance when $X$ is a line $L$ and $A$ a plane $\Pi$ as in Figure 15.10(b). Now $L \wedge \Pi^*$ is the plane containing $L$ perpendicular to $\Pi$, which is itself a flat. Therefore the `meet` with $\Pi$ now produces the expected line onto the plane that is the orthogonal projection of the line onto the plane in the usual sense.

Figure 15.10(c) shows that when $X$ is a line $L$ and $A$ is a sphere $S$, we get a great circle on the sphere, which is indeed a sensible interpretation of what it would be to project a line on a sphere. Obviously, these examples generalize to the other elements we have treated. You can even project a tangent vector onto a sphere (and the result is the point pair in which the plunging circle containing the tangent vector meets the sphere).

**Figure 15.10:** Orthogonal projections in the conformal model of Euclidean geometry.

In summary, the operation of projection generalizes from flats in a sensible, but somewhat unusual manner, providing a fundamental operation that seems to be new to Euclidean geometry. We have yet to discover applications in which it might be useful to encode these constructions compactly.

---

## 15.4 Application: All Kinds of Vectors

In the classical way of computing with geometry, we have different needs for indicating 1-D directional aspects. They all use a vector $\mathbf{u}$, but in different ways, which should transform in different manners to be consistent with that usage.

We may just mean the direction $\mathbf{u}$ in general, which is a *free vector* that can occur at any location. Or we may attach a vector to a point $p$ to make a *tangent vector* $p$ at the location $\mathbf{u}$ (which feels more like two geometrical elements put together rather than as a unified concept). In 3-D, a *normal vector* can be used to denote a plane; it can be placed anywhere in that plane (this practice generalizes to hyperplanes in $n$-D). The *direction vector* of a line gives it an affine length measure that can be used anywhere along it; such a vector is free to slide along the line. Finally, a *position vector* is used to denote the location of a point relative to another point (the origin). This is actually a tangent vector that is always attached to the origin (though in coordinate-based approaches, the origin is often left implicitly understood).

Each of these concepts can be defined as an element in the conformal model, and this makes them have precisely the right transformation properties. Of course this is true for higher-dimensional directional elements as well, and we have treated them all above. But it pays to treat the vectors separately and explicitly. You know them intimately, and may have come across problems in modeling and coding in which the coordinate approach just was not specific enough to specify permitted transformations. The typical solution would be to define different data structures for each, with their own methods [24, 13]. The conformal model offers an alternative: use precise algebraic elements that have the correct transformational properties, and then use just general methods (versors) to transform them. Each object automatically transforms correctly. Moreover, its clear algebraic relationship to the other computational elements dispenses with the need for a profusion of new methods explicitly specifying the various interactions. The algebraic data structures automatically perform computation and administration at the same time.

So, let us make these types of vectors; they are illustrated in Figure 15.11.

| Vector Type | Origin Form | Translated Form | Squared Norm | Localization Symmetry |
|-------------|-------------|-----------------|--------------|----------------------|
| Free | $\mathbf{u} \wedge \infty$ | $\mathbf{u} \wedge \infty$ | 0 | space |
| Normal | $\mathbf{u}$ | $p \rfloor (\mathbf{u} \wedge \infty)$ | $\mathbf{u}^2$ | plane |
| Line | $o \wedge \mathbf{u} \wedge \infty$ | $p \wedge \mathbf{u} \wedge \infty$ | $-\mathbf{u}^2$ | line |
| Tangent | $o \wedge \mathbf{u}$ | $p \wedge (p \rfloor (\mathbf{u} \wedge \infty))$ | 0 | point |

**Figure 15.11:** In the conformal model, the various kinds of vectorlike concepts of Euclidean geometry are clearly distinguished, each with its own form properly transforming under the permissible Euclidean transformations.

- **Free Vector $\mathbf{u} \wedge \infty$.** A 1-D direction without location is represented by the element $\mathbf{u} \wedge \infty = \mathbf{u} \infty$. Its directional aspect is exhibited by applying a rotation rotor to it:

  $$\mathsf{R}[\mathbf{u} \wedge \infty] = \mathsf{R}[\mathbf{u}] \wedge \mathsf{R}[\infty] = \mathsf{R}[\mathbf{u}] \wedge \infty,$$

  which shows that $\mathbf{u}$ is the element denoting its direction. Applying a translation rotor gives

  $$\mathsf{T}_\mathbf{p}[\mathbf{u} \wedge \infty] = \mathsf{T}_\mathbf{p}[\mathbf{u}] \wedge \mathsf{T}_\mathbf{p}[\infty] = \left(\mathbf{u} + (\mathbf{p} \cdot \mathbf{u}) \infty\right) \wedge \infty = \mathbf{u} \wedge \infty,$$

  so that it is translation-invariant. It has no specific location, so this is truly a free vector. It corresponds to the entity $\mathbf{u}$ in the homogeneous model. In the conformal model, it is the parameter of the translation rotor $\exp(-\mathbf{u} \wedge \infty/2)$. That rotor can be applied anywhere, and we now see why we are allowed to draw its action as a vector at any location, as is customary.

- **Normal Vector $\mathbf{u}$.** The normal vector of a plane in the origin is the purely Euclidean element $\mathbf{u}$, just as in the vector space model. It clearly indicates a direction vector, for applying a rotation to it we get $\mathsf{R}[\mathbf{u}]$. However, there is also a translational element. Applying the translation rotor gives

  $$\mathsf{T}_\mathbf{p}[\mathbf{u}] = p \rfloor (\mathbf{u} \wedge \infty) = \mathbf{u} + (\mathbf{p} \cdot \mathbf{u}) \infty.$$

  There are two consequences of this equation. First, it shows that the element $\mathbf{u}$ is insensitive to translations in the directions perpendicular to $\mathbf{u}$. We can depict it freely anywhere in the dual plane $\mathbf{u}$. It therefore truly is a normal vector of the plane; the classical liberty to draw such a normal vector anywhere on the plane is now fully part of the internal algebraic freedom of the computational element.

  The second consequence is that this equation gives the normal vector representation of a plane with normal direction $\mathbf{u}$ passing through $p$ instead of $o$. It is only the component $\mathbf{p} \cdot \mathbf{u}$ that affects the representation, and we recognize that as proportional to the oriented distance to the origin. This is the correct 1-D locational aspect of the plane: only its $\mathbf{u}$-component matters.

- **Line Vector $o \wedge \mathbf{u} \wedge \infty$.** A concept that is less explicit in classical considerations in geometry is the direction vector of a line. It is important in classical mechanics, where it is used to denote a force. Such a force is free to act anywhere along its carrier line, and therefore is a vector-like concept that should be permitted to slide along a well-defined line.

  An element with the correct symmetry is $o \wedge \mathbf{u} \wedge \infty$, which we are used to viewing as the line itself. It rotates to $o \wedge \mathsf{R}[\mathbf{u}] \wedge \infty$, which clearly indicates that it has a 1-D directional aspect. When we translate it, we obtain

  $$\mathsf{T}_\mathbf{p}[o \wedge \mathbf{u} \wedge \infty] = p \wedge \mathbf{u} \wedge \infty = o \wedge \mathbf{u} \wedge \infty + (\mathbf{p} \wedge \mathbf{u}) \wedge \infty.$$

  Again there are two consequences of this equation. First, it shows that the element is invariant under translations for which $\mathbf{p} \wedge \mathbf{u} = 0$ (i.e., motions along the line). Second, it shows how to make a general element with this property, passing through the point $p$. Only the part of $\mathbf{p}$ perpendicular to $\mathbf{u}$ affects the location, so a line in 3-D has a 2-D locational parameter complementary (i.e., dual) to its direction vector. This is effectively the "moment" we encountered in the homogeneous model.

  It is perhaps surprising that a line vector should be a 3-blade, but it really unites three separate concepts: a location $p$, a direction $\mathbf{u}$, and the straightness in its extension to the point at infinity $\infty$. All are required to define all aspects of its symmetry; the inclusion of $\infty$ allows the invariant shifting along the carrier.

- **Tangent Vector $o \wedge \mathbf{u}$.** A vector with direction $\mathbf{u}$ at the point location $o$ is represented as $o \wedge \mathbf{u}$. A rotation changes this to $o \wedge \mathsf{R}[\mathbf{u}]$, so that $\mathbf{u}$ is its only rotational aspect. A translation carries the direction vector along with the point. This is perhaps best seen when we first rewrite to $o \wedge \mathbf{u} = o \wedge \left(o \rfloor (\mathbf{u} \wedge \infty)\right)^\wedge$, and then translate:

  $$\mathsf{T}_\mathbf{p}[o \wedge \mathbf{u}] = \mathsf{T}_\mathbf{p}[o \wedge \left(o \rfloor (\mathbf{u} \wedge \infty)\right)^\wedge] = p \wedge \left(p \rfloor (\mathbf{u} \wedge \infty)\right)^\wedge.$$

  The location $p$ is explicitly present in the result; so the tangent vector has all the locational aspects of $p$, and moves with the point it is attached to.

  In classical applications, you draw tangent vectors all the time, as velocities, directions of motions on a surface, and so on. Apparently we can do a lot without having them explicitly represented as an element of computation---but now that we have this representation, we can use it. We will see several examples of its potential use in the ray tracer application of Chapter 23.

- **Position Vector.** The most common informal use of a Euclidean vector $\mathbf{u}$ has no counterpart in the conformal model: to denote a point in space. That practice attempts to use an element of the vector space model (the algebra of directions) to denote a location. This is only possible by using some standard point, namely an origin $o$, as a reference. We need to make this algebraically explicit: if $\mathbf{u}$ is meant to emanate from $o$, the position vector should encode $o$ in its definition. That makes it either the tangent vector $o \wedge \mathbf{u}$ or the line $o \wedge \mathbf{u} \wedge \infty$. It is not the line, for that loses essential aspects of the location $o$ due to its linear translation symmetry. The position vector has some feature of the tangent vector $o \wedge \mathbf{u}$, and can be seen as an amount of travel along that vector. But that encodes one point ($p$) in terms of another ($o$), and therefore does not really resolve the issue.

  Of course, in the conformal model we have a much better alternative: the point is represented as the representational null vector $u$. If we should want to know its location relative to any other point $q$, that is the Euclidean vector $\mathbf{u} - \mathbf{q} = u - q + \tfrac{1}{2}(u \cdot q) \infty$, but you do not need to know that to compute with the point $u$.

  The representative vector for the point $u$ may be obtained by using $\mathbf{u}$ in a translation rotor applied to $q$. Taking $q = o$, that gives us the correspondence to the classical characterization by a relative position vector:

  $$u = \mathsf{T}_{\mathbf{u}-o}[o] = e^{-\mathbf{u}\infty/2} \, o \, e^{\mathbf{u}\infty/2}.$$

  There is now a clear distinction between the vector parameter $\mathbf{u}$ characterizing the location and the standard element $o$ to which it is to be applied. If $o$ is chosen differently, $\mathbf{u}$ needs to change to reach the same point $u$. There is of course nothing geometrically intrinsic about the position vector $\mathbf{u}$ of a point $u$, and it is no wonder that the many tacit conventions in this position vector representation of a point are a source of errors and abuse. Homogeneous coordinates were the first step to a true point representation, but only the conformal model gives the full operational functionality expected from the representation of the most basic elements of geometry.

So, in summary: there is no need for separate data structures for the various kinds of vectors. As basic elements of computation, they are an integral element of the algebra, automatically inheriting their relationships with other elements through all of its products. Using this operational model of Euclidean geometry gives us more precision and flexibility, and simpler code. There is a small computational overhead to this, which we discuss in Part III; in a good implementation, this can be kept below 25 percent (which is actually also the cost of employing the structurally inferior homogeneous coordinates). Paradoxically, such efficiency is achieved by recognizing the class of an element and treating it with dedicated code; but the difference with the classical approach is that this special code is established by an automatic code generator rather than by the programmer herself.

---

## 15.5 Application: Analysis of a Voronoi Cell

To give an example of how the conformal model can be used in derivations of expressions, we take a detailed example from planar geometry involving distances in an essential manner. Given four points $p$, $q$, $r$, $s$ in the plane, we will compute the potential edge of the Voronoi diagram across the common edge $pr$ of the triangles $prs$ and $pqr$. We compute all its parameters, its carrier line, an end point, and its edge length. In the classical approach, this would involve a lot of trigonometry, which in turn would require you to define a host of intermediate variables and edge length parameters, as in Figure 15.12(b). We will show how it can all be done based on the four points only, with seemingly no trigonometry at all. You should see this as an isolated exercise in uncovering some common computational techniques for this type of problem.

We will go slowly and point out useful techniques on the way. You can skip this section without missing much, though you may want to contrast the directness of the conformal model result (15.8) (fully expressible in the original four points) with the classical result (15.10) (which requires many derived quantities even to be stated).

**Figure 15.12:** Definition of symbols for the Voronoi derivations, (a) for the conformal model derivation, and (b) for the classical, $p$-centered derivation.

### 15.5.1 Edge Lines

To keep life simple, we start from normalized points $p$, $q$, $r$, $s$, so that $-\infty \cdot p = 1$, and so on.

The Voronoi edge element that interests us lies on the perpendicular bisector of the connection line of $p$ and $q$, indicated in Figure 15.12(a). A point $x$ on it therefore satisfies $x \cdot p = x \cdot q$, which we can rewrite to $x \cdot (q - p) = 0$. Therefore the perpendicular bisector is dually characterized by

$$\text{dual perpendicular bisector: } q - p.$$

This element $q - p$ has a weight, a condition number that determines its significance. We can compute the norm squared as

$$(q - p) \cdot (q - p)^\sim = -2p \cdot q = d_E^2(p, q)$$

so the norm equals the squared length of the edge connecting $p$ and $q$. But this poses the problem of whether to take the positive or negative square root, and thus threatens to lose valuable orientation information. It is better to retain the directionality by computing the linear quantity

$$\infty \rfloor (q - p)^* = \left(\infty \wedge (\mathbf{q} - \mathbf{p})\right)^* = \left(\infty \wedge (\mathbf{q} - \mathbf{p})\right) \rfloor \left(o \wedge \mathbf{I}_2^{-1} \wedge \infty\right) = (\mathbf{q} - \mathbf{p})^\star \wedge \infty,$$

in which $( )^\star$ denotes the Euclidean dual in the plane. This direction is orthogonal in a consistent directed manner to the direction vector connecting $\mathbf{p}$ to $\mathbf{q}$, so this immediately gives both length and orientation. Consistency is obtained by relating all such signs and orientations to the same pseudoscalar of the plane (as implicit in the duality).

### 15.5.2 Edge Point

We form the dual midplane $r - q$, and compute the intersection of this with the earlier dual midplane $q - p$ to obtain a flat end point of our edge. This is, dually,

$$(q - p) \wedge (r - q) = p \wedge q + q \wedge r + r \wedge p,$$

which incidentally shows in its symmetry that only the order of $p$, $q$, $r$ matters, and then only by changing the sign of the result. We would have obtained the same intersection by intersecting with the midplane $p - r$. You can confirm that the result is a dual flat by taking a contraction with $\infty$; that indeed gives zero.

This dual flat point is not normalized. (Note that a flat point $x \wedge \infty$ is normalized when its norm is 1, and a point $x$ is normalized when its weight is 1 (so that $-\infty \rfloor x = 1$).) Its normalization factor may be useful in further computations of quantitative properties. If desired, we can normalize a flat point by the algebraic construction

$$X \mapsto \frac{X}{(o \wedge \infty) \rfloor X},$$

and this implies that a dual flat point is normalized by the substitution

$$X^* \mapsto \frac{X^*}{o \wedge \infty \wedge X^*}.$$

We can take any point instead of the arbitrary origin $o$, and it is important to wield this capability to keep formulas simple. For the dual flat point we just computed, which is based on a $q$-centered computation, it seems indicated to take $q$ for the arbitrary origin point $o$ in the normalization (but we could take $r$ or $p$ as well). That yields as normalized flat intersection point the circumcenter of the triangle formed by $p$, $q$, $r$:

$$\text{flat circumcenter: } M = \frac{p \wedge q + q \wedge r + r \wedge p}{p \wedge q \wedge r \wedge \infty}.$$

### 15.5.3 Edge Length

We can compute the other intersection in the quadrangle between the dual midlines $(r - p)$ and $(s - p)$ in the same manner, and normalize the resulting dual intersection point $N^*$ by $(p \wedge r \wedge s \wedge \infty)$. From those two intersection points, we should be able to deduce the length of the potential edge of the Voronoi diagram.

It is possible to do this by computing their square distance, but this again gives consistency issues in choosing the square root. Let us instead derive this length as the weight of the line connecting the two intersection points. If we had been in the homogeneous model, this line would have been $M \wedge N$. Computations with flats in the conformal model do not work quite so simply. When we have the flat points $M = m \wedge \infty$ and $N = n \wedge \infty$ rather than the corresponding points $m$ and $n$, we compute the desired line $m \wedge n \wedge \infty$ as $m \wedge N$. To do so, we should retrieve $m$ from the dual flat point $M^*$ as $o \rfloor M = (o \wedge M^*)^{-*}$. This also produces a term proportional to $\infty$, but the outer product in the line computation kills that anyway, which is a trick to remember! And again, since we can choose any normalized point as $o$, we pick $q$ when we observe that doing so reduces the number of terms in the computation.

We now spell out the manipulation to obtain the connecting line; note that all we really do is substitution of known properties, perhaps guided by the idea that the result should be part of the dual line $(r - p)$. We denote the scalar normalizations of the two points by $\alpha_M$ and $\alpha_N$, to unclutter the formulas.

$$\begin{aligned}
m \wedge n \wedge \infty &= \alpha_M \alpha_N \left(q \wedge (q - p) \wedge (r - q)\right)^{-*} \wedge \left((s - r) \wedge (p - s)\right)^{-*} \\
&= -\alpha_M \alpha_N \left((r - p) \wedge p \wedge q)\right)^{-*} \wedge \left((r - p) \wedge (p - s)\right)^{-*} \\
&= -\alpha_M \alpha_N \left((r - p) \wedge p \wedge q)\right)^{*} \wedge \left((r - p) \wedge (p - s)\right)^{*} \\
&= -\alpha_M \alpha_N \left(\left((r - p) \wedge (p - s)\right) \cap \left((r - p) \wedge p \wedge q\right)\right)^{*} \\
&= -\alpha_M \alpha_N (r - p)^* \left((r - p) \wedge (p - s) \wedge p \wedge q\right)^{*} \\
&= \alpha_M \alpha_N (r - p)^* (p \wedge q \wedge r \wedge s)^* \\
&= \frac{(r - p)^* (p \wedge q \wedge r \wedge s)^*}{(p \wedge q \wedge r \wedge \infty)^* (p \wedge r \wedge s \wedge \infty)^*}.
\end{aligned} \tag{15.8}$$

In the derivation we were striving towards a form that could use the `meet` identity (5.11). The final results confirms that we are on the line $(r - p)^*$, and it gives the length of the resulting segment between $M$ and $N$. Don't forget that $(r - p)^*$ contributes a factor $d_E(r,p)$ to the length, as we derived above.

Taking $q$ as variable for the moment, the length of the edge segment becomes zero when $p \wedge q \wedge r \wedge s = 0$, and this is when $q$ lies on the circle $p \wedge r \wedge s$. Move it beyond the circle and it changes sign. Negative edge length is an indication that another edge should become the Voronoi edge, namely the part of $(s - q)^*$ computed completely analogously (most simply by a cyclic permutation of $p$, $q$, $r$, $s$). It is rather satisfying that this condition is completely embedded in the basic computation; nowhere did we put in the circle $p \wedge r \wedge s$ explicitly, but the rearrangements of the outer products just made it appear naturally. The two terms in the denominator are dual oriented planes describing the two triangles involved; each term is twice the signed area of its corresponding triangle.

### 15.5.4 Conversion to Classical Formulas

The above computation using the conformal model was a fairly straightforward application of algebra on the combination of the basic points by standard operations. Where it may not have seemed straightforward, it was because this is the first time we encounter these techniques. The coordinate-free form of the final result is rather pleasing, and directly interpretable in terms of relative point positions.

By contrast, let us show how the results would look in classical form, to show that the conformal model result conveniently hides a lot of trigonometry. This requires the introduction of lots of symbols for local edge lengths and angles. For that, at least, we can use the natural correspondence to the geometric algebra of 2-D Euclidean space.

For the following computations, it is convenient to choose the (arbitrary) origin at $p$, denoting the Euclidean vectors to $q$, $r$, $s$ by $\mathbf{q}$, $\mathbf{r}$, $\mathbf{s}$, respectively. Then the dual plane is

$$r - p = \mathbf{r} + \tfrac{1}{2}\mathbf{r}^2\infty$$

We will also use polar coordinates relative to $p$ to convert the conformal expressions to more classical forms. That essentially means that we are using a vector space model based in $p$. We define the norms of $\mathbf{q}$, $\mathbf{r}$, $\mathbf{s}$ as $\kappa$, $\rho$, $\sigma$, and the angles through the implicit definitions also used in the vector space model treatment of a triangle (in (10.3)):

$$\mathbf{s}/\mathbf{r} = \sigma/\rho \, e^{\mathbf{I}_2\psi}, \quad \mathbf{r}/\mathbf{q} = \rho/\kappa \, e^{\mathbf{I}_2\phi},$$

so that $\psi$ is the angle from $\mathbf{s}$ to $\mathbf{r}$, and $\phi$ from $\mathbf{r}$ to $\mathbf{q}$ (see Figure 15.12(b)).

We prefer to redo parts of the computation rather than to perform an immediate substitution in the final conformal result (15.8). This shows the representation of intermediate quantities in an educational manner.

$$\begin{aligned}
(q - p) \wedge (r - q) &= (q - p) \wedge (r - p) \\
&= (\mathbf{q} + \tfrac{1}{2}\mathbf{q}^2\infty) \wedge (\mathbf{r} + \tfrac{1}{2}\mathbf{r}^2\infty) \\
&= \mathbf{q} \wedge \mathbf{r} + \infty \wedge (\mathbf{r} \mathbf{q}^2 - \mathbf{q} \mathbf{r}^2)/2 \\
&= \left(1 - \frac{\mathbf{r}\mathbf{q}^2 - \mathbf{q}\mathbf{r}^2}{2 \mathbf{q} \wedge \mathbf{r}} \infty\right) (\mathbf{q} \wedge \mathbf{r}).
\end{aligned}$$

The final form can be interpreted using Table 14.1, or by realizing that it should be the dual of a flat point $x \wedge \infty$, and computing quickly what form such a dual should have:

$$(x \wedge \infty) \rfloor (o \wedge \widetilde{\mathbf{I}}_2 \wedge \infty) = ((o + \mathbf{x}) \wedge \infty) \rfloor (o \wedge \widetilde{\mathbf{I}}_2 \wedge \infty) = \widetilde{\mathbf{I}}_2 + \infty \, \mathbf{x} \rfloor \widetilde{\mathbf{I}}_2 = (1 - \mathbf{x} \infty)\widetilde{\mathbf{I}}_2.$$

Either way, it follows that the intersection point is located at

$$\mathbf{m} = \frac{\mathbf{r} \mathbf{q}^2 - \mathbf{q} \mathbf{r}^2}{2\mathbf{q} \wedge \mathbf{r}} = \frac{\rho \, \breve{\mathbf{q}} - \kappa \, \breve{\mathbf{r}}}{2 \sin \phi} \widetilde{\mathbf{I}}_2, \tag{15.9}$$

where $\breve{\mathbf{q}}$, $\breve{\mathbf{r}}$ are unit vectors along $\mathbf{q}$ and $\mathbf{r}$, respectively. The intersection has a numerical strength measured by the norm of $\mathbf{q} \wedge \mathbf{r}$, which is $\kappa\rho \sin \phi$. Incidentally, this is the equation for the center of the circumcircle of the triangle $PQR$ in its classical form.

The edge length computed before can be converted into a more classical form using the same polar coordinates relative to $p$ (which is the chosen origin $o$):

$$\begin{aligned}
&(r - p)^* \frac{(p \wedge q \wedge r \wedge s)^*}{(p \wedge q \wedge r \wedge \infty)^* (p \wedge r \wedge s \wedge \infty)^*} = \\
&= (\mathbf{r} + \tfrac{1}{2} \rho^2 \infty)^* \frac{\left(o \wedge (\mathbf{q} + \tfrac{1}{2}\kappa^2 \infty) \wedge (\mathbf{r} + \tfrac{1}{2} \rho^2 \infty) \wedge (\mathbf{s} + \tfrac{1}{2}\sigma^2 \infty)\right)^*}{(o \wedge \mathbf{q} \wedge \mathbf{r} \wedge \infty)^* (o \wedge \mathbf{r} \wedge \mathbf{s} \wedge \infty)^*} \\
&= (\mathbf{r} + \tfrac{1}{2} \rho^2 \infty)^* \frac{(o \wedge \tfrac{1}{2} (\kappa^2 \mathbf{r} \wedge \mathbf{s} + \rho^2 \mathbf{s} \wedge \mathbf{q} + \sigma^2 \mathbf{q} \wedge \mathbf{r}) \wedge \infty)^*}{(o \wedge \mathbf{q} \wedge \mathbf{r} \wedge \infty)^* (o \wedge \mathbf{r} \wedge \mathbf{s} \wedge \infty)^*} \\
&= (\mathbf{r} + \tfrac{1}{2} \rho^2 \infty)^* \frac{\kappa\rho\sigma (-\kappa \sin \psi + \rho \sin(\phi + \psi) - \sigma \sin \phi)}{2(-\kappa\rho \sin \psi) (-\rho\sigma \sin \phi)} \\
&= (\breve{\mathbf{r}} + \tfrac{1}{2} \rho \infty)^* \frac{-\kappa \sin \psi + \rho \sin(\phi + \psi) - \sigma \sin \phi}{2 \sin \phi \sin \psi}.
\end{aligned}$$

So this gives the length of the edge in completely classical terms as

$$\frac{-\kappa \sin \psi + \rho \sin(\phi + \psi) - \sigma \sin(\phi)}{2 \sin \phi \sin \psi}, \tag{15.10}$$

and moreover that it is a part of the line orthogonal to $\breve{\mathbf{r}}$, passing midway through it (since the distance to $p$ is clearly $\tfrac{1}{2} \rho$).

The derivation spelled out in this manner may look rather intimidating. Yet it is fully algebraic from the conformal model result, which itself was straightforward algebra (with a clear geometrical interpretation). There was no need for the usual careful checking of signs and symbols with messy figures to develop the result. And of course, one doesn't need to compute this result at all, because the original conformal expression of (15.8) has the same value. It is a disadvantage of the classical expression that the symmetry is hidden in the peculiar variables, and that the circumcircle as the essential curve for the change of sign is hidden in the final expression. All one should need to specify for a Voronoi edge are the original four points, and it is satisfying to see that the conformal model can express the total quantitative result in terms of those points only.

---

## 15.6 Further Reading

Geometry using `meet` and `plunge` was developed in a 1941 book by Forder [22], which is full to the brim with useful geometrical results. He uses Grassmann's notation, in which $a \wedge b$ is denoted as $[a \; b]$, and dualization is denoted by $|a$ rather than $a^*$.

Forder's book is one of several instances that demonstrate how far Grassmann's heritage was developed into quantitative geometry. He wrote it to "redress the balance" between the use of Grassmann algebra in physics (where he says "it has at last won an established place") and in geometry (where it is "less widely appreciated").

The book may look rather intimidating, but with interactive software should now have become quite readable: all equations can be drawn, for this is the algebra of geometry.

---

## 15.7 Exercises

### 15.7.1 Drills

1. Compute the tangent at the origin of the sphere $\Sigma$ through the points at locations $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$, and $\mathbf{e}_3$ (you computed this sphere $\Sigma$ in the drills of Chapter 14).

2. Factorize the circle $K$ through the points at locations $\mathbf{e}_1$, $\mathbf{e}_2$, and $\mathbf{e}_3$ (you computed this circle $K$ in the drills of Chapter 14).

3. Use that factorization of the circle $K$ to spot its squared radius, center, carrier, and surround, by inspection.

4. Project the point at the origin onto the carrier plane of the circle $K$.

5. Make the free vector, tangent vector, line vector, and normal vector in the direction $\mathbf{e}_1$, at the origin (if a location is required).

6. Rotate each of the vectors of the previous exercise by $\pi/2$ in the $\mathbf{e}_1 \wedge \mathbf{e}_2$ plane. Explain the results.

7. Translate each of the vectors of the previous exercise by $\mathbf{e}_1 + \mathbf{e}_2$. Explain the results.

### 15.7.2 Structural Exercises

1. Express the scalar product of two blades in terms of the scalar product of their duals. It should only differ by a sign, which you should express in terms of the grade of the blades and the space they reside in.

2. What is the geometry of the element $p \wedge \mathbf{u}$, where $p$ is a point and $\mathbf{u}$ a Euclidean vector? (Hint: View it as a `plunge`. Counterhint: It is *not* the tangent vector $o \wedge \mathbf{u}$ moved to $p$.)

3. Show that the tangent of a tangent is zero. (Hint: Realize that a tangent is also a round; now use (15.1).)

4. On a circle $K$, find the closest and furthest points to a given point $c$ (in $n$-D!).
   - Hint 1: Set up a dual sphere with parametric radius around $c$, and compute the `meet` with $K$.
   - Hint 2: The `meet` of parametric sphere and $K$ should be a tangent vector at the desired points.
   - Hint 3: Use the algebraic property of tangents, which is that they are rounds that square to zero, to get a second-order equation for the radius, and solve.
   - Hint 4: Compute the locations of the tangent vectors.

5. Show that the dual sphere $s = r \rfloor (p \wedge q) = (r \rfloor p) q - (r \rfloor q) p$ is a member of the parameterized family (15.6), passing through $r$ (but nonnormalized).

6. It is interesting to study the outcome of the construction $p \rfloor (q \wedge r)$, which crops up frequently in some form or other in computations. Depending on whether you let $p$, $q$, $r$ be equal to points, dual spheres, or the point at infinity $\infty$, different constructions appear. Play with this construction, either by hand or (preferably) in an interactive visualization package. What is $\infty \rfloor (q \wedge r)$? What is $r \rfloor (q \wedge \infty)$?

7. Give the formula for the circle through a point pair $p \wedge q$ intersecting the dual plane $\pi$ perpendicularly, and for the circle having a tangent vector in direction $\mathbf{u}$ at $p$ and plunging into $\pi$.

8. Derive the factorization of a dual round (15.5) from the factorization of a direct round (15.4).

9. Construct the contour of a sphere $\Sigma$ as seen from a point $p$ (i.e., the circle $K$ of points where the invisible part of the sphere borders the visible part, as in Figure 15.13). (Hint: The white sphere in the figure is a clue to the construction. Express it first, using the `plunge`. Then construct the circle as a `meet`.)

10. You can derive all types of vectors of Section 15.4 by relating them to two points $a$ and $b$, which are combined using the various products of geometric algebra. Identify the types of the following elements and relate them geometrically to $a$ and $b$: $\infty \rfloor (a \wedge b)$, $\infty \wedge (a \wedge b)$, $\infty \wedge (\infty \rfloor (a \wedge b))$, $\infty \rfloor (\infty \wedge (a \wedge b))$, $a \rfloor (\infty \wedge (a \wedge b))$, $a \wedge (\infty \rfloor (a \wedge b))$. How is their squared norm related to the oriented distance of $a$ and $b$? For the null elements, can you retrieve this distance in another manner?

11. Show that the tangent with direction element $\mathbf{E}$ at $p$ can be written in two equivalent forms:

    $$\text{tangent } \mathbf{E} \text{ at } p: \quad p \wedge \left(- p \rfloor (\hat{\mathbf{E}}\infty)\right) = p \rfloor (p \wedge \hat{\mathbf{E}} \wedge \infty).$$

**Figure 15.13:** Construction of the contour circle $K$ of a dual sphere $\sigma = \Sigma^*$ seen from a point $p$ (see Exercise 9).

---

## 15.8 Programming Examples and Exercises

The three examples for this chapter are interactive versions of Figure 15.2 (the `plunge`), Figure 15.8 (affine combinations of points), and Figure 15.10 (Euclidean projections), respectively.

### 15.8.1 The Plunge

This example draws a green circle that is the `plunge` of the following three primitives:

```cpp
const int NB_PRIMITIVES = 3;
mv g_primitives[NB_PRIMITIVES] = {
    // point:
    c3gaPoint(-1.0f, 1.5f, 0.0f),
    // dual sphere:
    3.25f * e1 + 2.68f * e2 - 0.34f * e3 + 1.00f * no + 8.43f * ni,
    // dual plane:
    -e2 + 2.0f * ni,
};
```

Computing and drawing the `plunge` is as simple as

```cpp
draw(g_primitives[0] ^ g_primitives[1] ^ g_primitives[2]);
```

You can translate the sphere and the point. Notice how the circle always intersects the point, sphere, and plane orthogonally.

### 15.8.2 Affine Combinations of Points

As described in Section 15.2.4, affine combinations of points are circles in $\mathbb{E}^2$. This example uses `c2ga` to implement an interactive version as shown in Figure 15.14. The code to draw the circles is:

```cpp
const mv::Float STEP = 0.1f;
for (mv::Float lambda = -1.0f; lambda <= 2.0f; lambda += STEP) {
    // set color, turn GL stipple on when circle is imaginary.
    // ... (omitted)

    // draw the circle:
    draw(lambda * g_points[0] + (1.0f - lambda) * g_points[1]);
}
```

As an extra feature, the example also draws the bisecting line (in green) between the two points, using:

```cpp
draw(g_points[0] - g_points[1]);
```

**Figure 15.14:** Screenshot of Example 2.

### 15.8.3 Euclidean Projections

As described in Section 15.3, orthogonal projection in the conformal model behaves somewhat unexpectedly. This example draws a line or circle, and its projection onto a plane. You can change the arguments interactively, and optionally cause the `plunge` to be drawn. Figure 15.15 shows a screenshot.

From formula to program is straightforward, for the projection itself is drawn using

```cpp
// CL is circle or line
// PL is plane
draw((CL << inverse(PL)) << PL);
```

and the optional `plunge` is drawn as:

```cpp
draw(CL ^ dual(PL));
```

**Figure 15.15:** Screenshot of Example 3. The green circle is projected onto the blue plane. The projection is drawn in cyan. The sphere is the `plunge` of circle and plane, which explains the geometry of the projection.
