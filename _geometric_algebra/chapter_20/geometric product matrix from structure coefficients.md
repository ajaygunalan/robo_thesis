# Geometric Product Matrix from Structure Coefficients

The geometric product is bilinear, so if you freeze the left factor $A$, the map

$$
B \mapsto AB
$$

is linear in $B$. That single observation lets you implement multiplication as "apply a matrix," provided you know how the algebra multiplies basis blades. The chapter's matrix approach is exactly this operator viewpoint.

## Step 1: encode basis-blade multiplication as structure coefficients

Fix an ordered basis-blade list $\mathcal{L} = [L_0, \dots, L_{2^n-1}]$. For basis blades, the geometric product has the form

$$
L_k L_j = \sum_i s_{k,j}^{\,i} L_i,
$$

where the scalars $s_{k,j}^{\,i}$ are the **structure coefficients** of the algebra. In a diagonal metric (e.g., Euclidean), the product of two basis blades often lands on a *single* basis blade (up to a sign), so the sum collapses to one term; in a non-diagonal metric you genuinely get sums of basis blades. The chapter calls out both cases explicitly.

The important implementation point is: computing $s_{k,j}^{\,i}$ is "where the geometric algebra lives." Once you have those coefficients (via basis-blade product routines from the previous chapter), the rest is linear algebra bookkeeping.

## Step 2: derive the operator matrix for left-multiplication by $A$

Write

$$
A = \sum_k a_k L_k, \qquad B = \sum_j b_j L_j.
$$

Then

$$
\begin{aligned}
AB
&= \sum_{k,j} a_k b_j (L_k L_j) \\
&= \sum_{k,j} a_k b_j \sum_i s_{k,j}^{\,i} L_i \\
&= \sum_i \left( \sum_{k,j} a_k b_j s_{k,j}^{\,i} \right) L_i.
\end{aligned}
$$

So the output coordinate $c_i$ (for $C = AB$) is

$$
c_i = \sum_j \left( \sum_k s_{k,j}^{\,i} a_k \right) b_j.
$$

This is exactly the matrix–vector pattern $c_i = \sum_j (A^G)_{ij} b_j$, meaning the **geometric-product operator matrix** for left multiplication by $A$ has entries

$$
(A^G)_{ij} = \sum_k s_{k,j}^{\,i} a_k.
$$

The chapter presents this same rule as the definitive "fill-in" formula for the matrix that represents left-multiplication by $A$.

Two consequences are worth being blunt about:

- There is **no single universal geometric-product matrix**. Every left factor $A$ produces its own matrix $A^G$, because the entries are linear combinations of the coefficients of $A$.

- All the complexity is pushed into computing $s_{k,j}^{\,i}$ (basis-blade products). Once you can do that, building $A^G$ is systematic.

## Step 3: the construction algorithm

To compute $A^G$ from $A$ in an $n$-dimensional algebra:

1. Initialize $A^G$ as a $2^n \times 2^n$ zero matrix.
2. For each pair of basis blades $(L_k, L_j)$, compute the product $L_k L_j$ and express it in the basis as $\sum_i s_{k,j}^{\,i} L_i$.
3. Accumulate contributions into the operator matrix using
   $$
   (A^G)_{ij} \mathrel{+}= s_{k,j}^{\,i} a_k
   $$
   for every nonzero structure coefficient.

The only difference between diagonal and non-diagonal metrics is whether step 2 returns a single term (one $i$) or many (a sum over $i$).
