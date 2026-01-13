# Sampling-Based Motion Planning

## Notation

|Symbol|Definition|
|---|---|
|$\mathcal{W}$|Workspace: physical world ($\mathbb{R}^2$ or $\mathbb{R}^3$)|
|$\mathcal{O} \subset \mathcal{W}$|Obstacle region: fixed occupied space|
|$\mathcal{A}$|Robot: movable body|
|$\mathcal{C}$|Configuration space: all possible robot states|
|$q \in \mathcal{C}$|Configuration: complete specification of robot pose (position, orientation, joint angles)|
|$q_I, q_G \in \mathcal{C}$|Initial and goal configurations (the query pair)|
|$\mathcal{C}_{obs} \subset \mathcal{C}$|Obstacle region in $\mathcal{C}$: configurations where $\mathcal{A}$ intersects $\mathcal{O}$|
|$\mathcal{C}_{free} = \mathcal{C} \setminus \mathcal{C}_{obs}$|Free space: collision-free configurations|
|$\dim(\mathcal{C})$|Degrees of freedom (e.g., 6 for rigid body in $\mathbb{R}^3$)|
|$G = (V, E)$|Graph with vertices $V$ and edges $E$|
|$\|q_1 - q_2\|$|Distance metric in $\mathcal{C}$|
|$\alpha_i$|Random sample from $\mathcal{C}$|

**Motion planning problem:** Given $(q_I, q_G)$, find a continuous path $\tau: [0,1] \to \mathcal{C}_{free}$ with $\tau(0) = q_I$ and $\tau(1) = q_G$.

---

## 1. Geometric Modeling

Motion planning operates on mathematical representations within world $\mathcal{W}$ (typically $\mathbb{R}^2$ or $\mathbb{R}^3$), constructing obstacles $\mathcal{O}$ (fixed occupied regions) and robots $\mathcal{A}$ (movable bodies) via geometric primitives.

|Representation|Definition|Implementation|
|---|---|---|
|**Boundary**|Outer shell only|Vertices, edges, faces; triangle meshes|
|**Solid**|Complete occupied volume|Algebraic inequalities ($f(x,y,z) \leq 0$)|

Solid representations enable efficient collision detection: evaluating $f(x,y,z) \leq 0$ immediately classifies points as interior (collision) or exterior (free). Boundary representations require additional computation for inside/outside determination.

---

## 2. Motion Planning Paradigms

### 2.1 Combinatorial Motion Planning

Combinatorial (exact) methods explicitly construct $\mathcal{C}_{obs}$ and $\mathcal{C}_{free}$. These are _complete_: guaranteed to find solutions if they exist.

Algorithms: cell decompositions (vertical, cylindrical algebraic), roadmap methods (Canny's algorithm, visibility graphs).

**Limitation:** Runtime grows exponentially with $\dim(\mathcal{C})$, restricting use to low-dimensional problems. Valuable when completeness or optimal paths are required.

### 2.2 Sampling-Based Motion Planning

Sampling-based methods probe $\mathcal{C}$ via sampling, treating collision detection as a black box—avoiding explicit $\mathcal{C}_{obs}$ construction. Dominates modern robotics due to superior dimensional scaling.

Guarantees: _probabilistically complete_ (solution found as $t \to \infty$) or _resolution complete_ (solution found given sufficient sampling density).

Applications: high-DOF manipulators, humanoids, multi-robot coordination, protein folding.

---

## 3. RRT and PRM: Two Paradigms for Sampling-Based Planning

The fundamental distinction in sampling-based planning lies in query multiplicity. **Single-query** problems specify one $(q_I, q_G)$ pair with no precomputation benefit. **Multiple-query** problems assume numerous queries for a fixed robot/obstacle configuration, justifying preprocessing investment. This distinction motivates two complementary algorithms: Rapidly-exploring Random Trees (RRT) for single-query and Probabilistic Roadmaps (PRM) for multiple-query scenarios.

### 3.1 RRT: Query-Time Tree Construction

RRT constructs a tree rooted at $q_I$, incrementally extending toward unexplored $\mathcal{C}$ regions:

1. **Init:** $G = {q_0 = q_I}$
2. **Iterate:** For random sample $\alpha_i \in \mathcal{C}$:
    - Find $q_n = \arg\min_{q \in G} |q - \alpha_i|$ (nearest vertex)
    - Extend from $q_n$ toward $\alpha_i$ via straight-line path
    - On collision, terminate at $q_s$ nearest obstacle boundary
    - Add vertex $q_s$, edge $(q_n, q_s)$ to $G$

This produces Voronoi-biased expansion—main branches rapidly reach distant regions before subsidiaries fill intermediate space—enabling efficient exploration without parameter tuning. Bidirectional variants grow trees from both $q_I$ and $q_G$, terminating on connection. Originally developed for differential constraints where system dynamics restrict feasible motions.

### 3.2 PRM: Preprocessed Roadmap Architecture

PRM separates computation into two phases. **Preprocessing** (query-independent): initialize empty graph $G$; sample $q \in \mathcal{C}$ and add collision-free samples as vertices; connect neighbors ($k$-nearest or radius-based) via collision-free edges. **Query phase**: connect $q_I$, $q_G$ to nearby roadmap vertices; execute A* for the connecting path. Preprocessing amortizes across queries, enabling rapid subsequent resolution.

### 3.3 Structural Divergence

Despite both constructing graphs, RRT and PRM differ fundamentally:

|Property|RRT|PRM|
|---|---|---|
|**Topology**|Tree (acyclic)|Network (cycles, redundancy)|
|**Root**|Explicit at $q_I$|None|
|**Coverage**|Partial (query-specific corridor)|Global ($\mathcal{C}_{free}$ connectivity)|
|**Construction**|During query|Before query|

The critical distinction is **root dependency**. Every RRT vertex exists as an extension from $q_I$; changing $q_I$ invalidates the entire structure. Transforming an existing RRT to a new root fails because $\mathcal{O}$ remains fixed in world frame—transformed vertices may intersect obstacles despite original validity. PRM avoids this by distributing samples globally without query reference; any $(q_I, q_G)$ can connect to the existing structure representing $\mathcal{C}_{free}$ connectivity.

Coverage strategy follows directly: RRT terminates on solution (or resource exhaustion), covering only the traversed corridor; PRM continues until adequate $\mathcal{C}_{free}$ coverage (vertex count/density criteria), ensuring paths for diverse queries.

### 3.4 Algorithm Selection

PRM's reusability requires static $\mathcal{O}$—if obstacles move or robot geometry changes, the roadmap invalidates. This yields clear selection criteria:

|RRT|PRM|
|---|---|
|Single query|Multiple queries, same environment|
|Dynamic/changing environment|Static robot/obstacle configuration|
|No preprocessing time|Preprocessing time available|
|Differential constraints|Rapid post-setup resolution required|

The fundamental tradeoff: preprocessing investment versus per-query computation.

---

## 4. Conclusion

Sampling-based planning addresses $\mathcal{C}_{obs}$ construction intractability via sampling and collision detection.

**RRT:** Search tree rooted at $q_I$ with Voronoi-biased expansion. Single-query design avoids preprocessing but produces query-specific structures.

**PRM:** Reusable roadmap via global sampling. Requires static environments but minimizes per-query computation under that assumption.

The root dependency preventing RRT reuse is the key structural distinction for algorithm selection.