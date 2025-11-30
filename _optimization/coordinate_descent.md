---
tags: optimization
---

if $f(x)$ is like $4x^2_1 +x^2_2$ then for every coordinate minimize $f(x)$  w.r.t.  $x_i$ , keeping the other coordinate variables constant. 

1. Initialize $x^0$ and  $\epsilon$, set $k:=0$
2. while [[stopping_condition]]
	1. for $I = 1, \dots, n$
		1. $x_i^{new} = \arg \min_{x_i} f(x)$
		2. $x_i = x_i^{new}$
	end for
3. End While
Output: $x^* =x^k$ a stationary point of f(x)

Globally convergent if a search along any coordinate direction yields a unique minimum point.

[start here](https://youtu.be/XpPvsMhxwSM?list=PL6EA0722B99332589&t=1600)