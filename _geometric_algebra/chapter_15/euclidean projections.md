# euclidean projections

## The blade projection formula

In geometric algebra, projection of a blade $X$ onto a blade $P$ is another blade:
$$X \mapsto (X \rfloor P)/P,$$
where division is by geometric product (Equation 15.7). In the conformal model this behaves as expected when $X$ is a **flat**.

## Why projecting a round doesn't give an ellipse

If $X$ is a **round**, you might hope projection onto a plane gives a conic (e.g., circle $\to$ ellipse). But an ellipse is not represented by a blade in CGA, so this operation cannot return one. What it returns instead is a *round* determined by an orthogonality construction.

The chapter connects projection to meet via an identity (recalled from earlier chapters) that effectively says: the projection is proportional to a meet involving a construction that contains $X$ and is perpendicular to the target blade. In Euclidean terms, that construction is naturally read as a **plunge**: "build the simplest element that contains $X$ and intersects the target perpendicularly, then intersect back."

## Geometric outcomes you should expect

The examples in Figure 15.10 (page 14) summarize the behavior:

* **Circle onto plane**: the result is a **circle**—specifically, the equator of the sphere that contains the original circle and plunges into the plane. This is the "closest" round consistent with orthogonal incidence, not a conic shadow.
* **Line onto plane**: because the intermediate "plunging" object remains a flat, the result is the familiar orthogonal projection line.
* **Line onto sphere**: the result is a **great circle**, which is a coherent notion of "projecting a line onto a sphere."
* More exotic: even a tangent vector can be projected onto a sphere, producing a point pair where the plunging circle meets the sphere.

The meta-message is that projection generalizes from flats to rounds in a way that is algebraically consistent and geometrically interpretable, even if it doesn't match "project by dropping perpendiculars and expect a conic."
