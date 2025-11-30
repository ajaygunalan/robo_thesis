---
tags: optimization
---

$(H^k)^{-1}$ is computationally expensive so we approximate it by symmetric & positive definite $B^k$ and it satisfies **quasi-newton conditions**:

$$ B^{k+1}(g^{k+1}-g^k) = x^{k+1}-x^k $$
$$\Longrightarrow B^{k+1}\gamma^k = \delta^k$$ ^96ef25

 when [[wolfe]] is satisfies, $\exists \; B^{k+1}$ which satisfies QN condition. After $n$ iterations $B^n = (H^k)^{-1}$ if $\delta^1, \ldots, \delta^n$ are linearly independent.


**How to get $B^{k+1}$ ?** 
- [[rank_one_method]]  
- [[rank_two_methods]].





[video](https://www.youtube.com/watch?v=XpPvsMhxwSM&list=PL6EA0722B99332589&index=18)