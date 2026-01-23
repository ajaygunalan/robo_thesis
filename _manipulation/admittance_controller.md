# Admittance

> Frames used: **W** world/base_link, **P** probe/TCP (paper's body ${b}$), **S** F/T sensor.  


---

## Notation & helpers (once)

- **Pose** $X_{WP}=(R_{WP}, p_{WPo})$.
- **Twist** $V=[ \boldsymbol\omega;\mathbf{v} ]\in\mathbb{R}^6$ (angular, linear).
- **Wrench** $F=[ \mathbf{f};\boldsymbol\tau ]\in\mathbb{R}^6$ (force, torque).
- **Small pose offset** $\delta X=[ \delta\mathbf{r};\delta\mathbf{p} ]\in\mathbb{R}^6$ (rot, trans).
- **Adjoints** (with $\widehat{p}$ the skew map):
$$\mathrm{Ad}_{\text{pose}}(R)=\mathrm{diag}(R,R),\quad \mathrm{Ad}_{\text{twist}}(R,p)=\begin{bmatrix}R&0\ \widehat{p} R&R\end{bmatrix},\quad \mathrm{Ad}_{\text{force}}=\mathrm{Ad}_{\text{twist}}^\top.$$
    
Re-expression $A\to B$: $V_B=\mathrm{Ad}_{\text{twist}}(X_{BA})V_A$, $F_B=\mathrm{Ad}_{\text{force}}(X_{BA})F_A$.
    
- $\mathrm{Exp3},\mathrm{Log3}$ on $SO(3)$.
    
- **sat_norm**: $\mathrm{sat_norm}(\mathbf{u},u_{\max}) = \mathbf{u}$ if $|\mathbf{u}|\le u_{\max}$, else $\mathbf{u} \frac{u_{\max}}{|\mathbf{u}|}$.
    

---

## Initialization (time $k=0$)

- **Period** $\Delta t>0$.
    
- **Admittance gains** $M,B,K\in\mathbb{R}^{6\times6}$ (diag, $>0$).
    
- **World P-gain** $K_p^W\in\mathbb{R}^{6\times6}$ (units $1/s$).
    
- **Limiter params (world)**: $\dot{\mathbf{v}}_{\max},\dot{\boldsymbol\omega}_{\max},\mathbf{v}_{\max},\boldsymbol\omega_{\max}$, workspace box $[x_{\min},x_{\max}]\times[y_{\min},y_{\max}]\times[z_{\min},z_{\max}]$.
    
- **Desired at $k=0$**: $X_{WP,\text{des}}^{(0)}$, $V_{WP,\text{des}}^{W,(0)}$ (often $\mathbf{0}$).
    
- **Measured**: $X_{WP,\text{meas}}^{(0)}$ (FK).
    
- **State (in P axes tied to desired)**: $\delta X_{P}^{(0)}=\mathbf{0}$, $\dot{\delta X}_{P}^{(0)}=\mathbf{0}$.
    
- **Limiter memory**: $V_{\text{prev}}=\mathbf{0}$.
    

---

## Per-tick loop (compute $k\to k{+}1$)

### **Step 0 — Wrench (already in probe axes)**

Read $F_{P\text{ext},P}^{(k)}$ from `/netft/proc_probe` (gravity/bias compensated; expressed in P). No extra re-expression here.

---

### **Step 1 — Admittance ODE in P**

$$M \ddot{\delta X}_{P}^{(k)}+B \dot{\delta X}_{P}^{(k)}+K \delta X_{P}^{(k)}=F_{P\text{ext},P}^{(k)}.$$

Semi-implicit Euler:

$$\dot{\delta X}_{P}^{(k+1)}=\dot{\delta X}_{P}^{(k)}+\ddot{\delta X}_{P}^{(k)}\Delta t,\quad \delta X_{P}^{(k+1)}=\delta X_{P}^{(k)}+\dot{\delta X}_{P}^{(k+1)}\Delta t.$$

---

### **Step 2 — Re-express offset/rate to world (use _desired_ pose)**

Build adjoints from $X_{WP,\text{des}}^{(k)}=(R_{\text{des}}^{(k)},p_{\text{des}}^{(k)})$:

$$\mathrm{Ad}_{\text{pose}}^{(k)}=\mathrm{diag}(R_{\text{des}}^{(k)},R_{\text{des}}^{(k)}),\quad \mathrm{Ad}_{\text{twist}}^{(k)}=\begin{bmatrix}R_{\text{des}}^{(k)}&0\ \widehat{p_{\text{des}}^{(k)}} R_{\text{des}}^{(k)}&R_{\text{des}}^{(k)}\end{bmatrix}.$$

Then

$$\delta X_{W}^{(k+1)}=\mathrm{Ad}_{\text{pose}}^{(k)} \delta X_{P}^{(k+1)},\qquad \dot{\delta X}_{W}^{(k+1)}=\mathrm{Ad}_{\text{twist}}^{(k)} \dot{\delta X}_{P}^{(k+1)}.$$

_Ideal controller anchors P on the **desired** pose; no robot feedback enters this mapping._

---

### **Step 3 — Commanded pose in world**

$$R_{WP,\text{cmd}}^{(k+1)}=\mathrm{Exp3}(\delta\mathbf{r}_W^{(k+1)}) R_{WP,\text{des}}^{(k)},\quad p_{WPo,\text{cmd}}^{(k+1)}=p_{WPo,\text{des}}^{(k)}+\delta\mathbf{p}_W^{(k+1)}.$$

Let $X_{WP,\text{cmd}}^{(k+1)}=(R_{WP,\text{cmd}}^{(k+1)},p_{WPo,\text{cmd}}^{(k+1)})$.

---

### **Step 4 — Pose error (measured → commanded)**

$$e_{R_W}^{(k)}=\mathrm{Log3}\big(R_{WP,\text{cmd}}^{(k+1)}R_{WP,\text{meas}}^{(k)\top}\big),\quad e_{p_W}^{(k)}=p_{WPo,\text{cmd}}^{(k+1)}-p_{WPo,\text{meas}}^{(k)},\quad e_{X_W}^{(k)}=\begin{bmatrix}e_{R_W}^{(k)}\ e_{p_W}^{(k)}\end{bmatrix}.$$

---

### **Step 5 — World twist command (include desired twist)**

$$\boxed{ V_{WP,\text{cmd}}^{W,(k+1)}= \underbrace{V_{WP,\text{des}}^{W,(k)}}_{\text{planner}} +\underbrace{\dot{\delta X}_{W}^{(k+1)}}_{\text{admittance}} +\underbrace{K_p^W e_{X_W}^{(k)}}_{\text{P correction}} }$$

---

### **Step 6 — Single world-space limiter (rate → workspace → velocity)**

Let $V^{-}=V_{WP,\text{cmd}}^{W,(k+1)}$. With memory $V_{\text{prev}}$:

**(a) Acceleration (rate) limit**

$$\Delta V=V^{-}-V_{\text{prev}},\quad \Delta\boldsymbol\omega\leftarrow\mathrm{sat_norm}(\Delta\boldsymbol\omega,\dot{\boldsymbol\omega}_{\max}\Delta t),\quad \Delta\mathbf{v}\leftarrow\mathrm{sat_norm}(\Delta\mathbf{v},\dot{\mathbf{v}}_{\max}\Delta t),$$

$$V^{(a)}=V_{\text{prev}}+\begin{bmatrix}\Delta\boldsymbol\omega\ \Delta\mathbf{v}\end{bmatrix}.$$

**(b) Workspace wall** (one-sided gating, use $p_{WPo,\text{meas}}^{(k)}$)  
For $i\in{x,y,z}$:

$$p_i\le x_{\min}\Rightarrow v^{(a)}_i\gets\max(0, v^{(a)}_i),\qquad p_i\ge x_{\max}\Rightarrow v^{(a)}_i\gets\min(0, v^{(a)}_i).$$

Result $V^{(b)}$.

**(c) Velocity norm caps**

$$\mathbf{v}^{+}=\mathrm{sat_norm}(\mathbf{v}^{(b)},|\mathbf{v}_{\max}|),\quad \boldsymbol\omega^{+}=\mathrm{sat_norm}(\boldsymbol\omega^{(b)},|\boldsymbol\omega_{\max}|),\quad V^{+}=\begin{bmatrix}\boldsymbol\omega^{+}\ \mathbf{v}^{+}\end{bmatrix}.$$

Update $V_{\text{prev}}\gets V^{+}$. _(Limiter is an engineering safety layer; the paper's ideal controller does not prescribe one.)_

---

### **Step 7 — Resolved-rates IK (publish joint velocities)**

Find $\dot{q}^{(k)}$ to track $V^{+}$ at the TCP in W:

$$\dot{q}^{(k)}=\arg\min_{\dot{q}} \big|J_s(q^{(k)}) \dot{q}-V^{+}\big|^2+\lambda|\dot{q}|^2\quad \text{s.t.} \dot{q}_{\min}\le\dot{q}\le\dot{q}_{\max}.$$

Send $\dot{q}^{(k)}$ to the velocity controller.

---

## Commit

Store $\delta X_{P}^{(k+1)}$, $\dot{\delta X}_{P}^{(k+1)}$, $V_{\text{prev}}=V^{+}$ (and advance $X_{WP,\text{des}}$ if the planner updates it).

---

.  