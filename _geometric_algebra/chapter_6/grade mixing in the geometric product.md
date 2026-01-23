# Grade mixing in the geometric product

Outer products are grade-pure: a k-blade wedged with an l-blade gives a $(k+l)$-blade or zero. The geometric product is different because whenever the two factors share directions, those shared vector factors can collapse to scalars (via vector squares), and each such collapse drops grade by two. The result is a controlled "fan" of possible grades rather than a single grade.

For basis blades this is easiest to see. Multiply a k-blade basis element by an l-blade basis element. If none of their basis vectors overlap, the product essentially behaves like a wedge and you get the top grade $(k+l)$. If one basis vector overlaps, it can be commuted next to its twin (picking up signs) and then squared into a scalar, removing two vector factors from the exterior-like part, so the grade drops by 2. Do that repeatedly and the possible grades are

$$
|k-l|,\ |k-l|+2,\ \dots,\ k+l-2,\ k+l.
$$

The extreme $|k-l|$ happens when one blade's directions are entirely contained in the other: "everything cancels down" except the difference in dimensionality, which is exactly the geometric shadow of contraction.

This grade fan is why the geometric product feels like it contains "a complete inventory" of relative geometry: metric relationships (lengths/angles) and incidence-like relationships (containment/spanning) appear simultaneously as different grade parts of the same product. It's also why you should stop thinking of grade as a single integer for a generic multivector product; mixed-grade outputs are normal, not exceptional.
