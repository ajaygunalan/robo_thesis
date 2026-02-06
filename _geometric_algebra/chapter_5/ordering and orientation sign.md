# ordering and orientation sign

Meet carries orientation information, so its sign must be interpreted relative to a chosen orientation of the join pseudoscalar. Changing the sign of the join flips the sign of every meet computed relative to it; keep that convention fixed across a calculation.

Swapping the arguments of the meet may also flip the sign, depending only on co-dimensions inside the join. If $a=\mathrm{grade}(A)$, $b=\mathrm{grade}(B)$, and $j=\mathrm{grade}(J)$ for $J=A\cup B$, then
$$
B \cap A = (-1)^{(j-a)(j-b)}\, (A \cap B).
$$

This parity rule matches common cases:

- Two lines in a plane: $a=b=1$, $j=2$, so $(j-a)(j-b)=1$ and the meet is antisymmetric, matching the sign flip of $\sin(-\theta)=-\sin(\theta)$ when you reverse the oriented angle.
- A line and a plane in 3D: $a=1$, $b=2$, $j=3$, so $(j-a)(j-b)=2$ and the meet is symmetric; the sign still records which side the line pierces relative to the oriented plane, but swapping argument order does not introduce an extra minus sign.

This rule generalizes across all incidence types and geometric models; only $(j-a)$ and $(j-b)$ matter, not the particular embedding model.
