## Force & Torque Sensor Filtering

  
  

$$\mathbf{W}_{\text{filtered}} = \mathcal{D}(\mathcal{C}(\mathcal{L}(\mathbf{W}_{\text{raw}})))$$

  

Where:

- $\mathbf{W}_{\text{raw}} = [f_x, f_y, f_z, \tau_x, \tau_y, \tau_z]^T$: Raw 6-DOF wrench measurements from the sensor.

- $\mathcal{L}(\cdot)$: Low-pass filtering operation applied **before** compensation.

- $\mathcal{C}(\cdot)$: Gravity and bias compensation operation.

- $\mathcal{D}(\cdot)$: Deadband filtering operation applied **after** compensation.

- $\mathbf{W}_{\text{filtered}}$: Final processed wrench ready for control input.

  

## Filters
  

### Low-Pass Filtering
  

Applied to raw sensor data before compensation to remove high-frequency noise using a first-order IIR [[filter]].

  

$$H(z) = \frac{\alpha}{1 - (1-\alpha)z^{-1}} \quad \text{where}$$

  
  

Default Parameters:

- filter coefficient $\alpha = = \frac{\omega_c \Delta T}{1 + \omega_c \Delta T}$

- angular cutoff frequency  $\omega_c = 2\pi rad/s

- sampling period  $\Delta T = 0.002$ s

- cutoff frequency $f_c = 200$ Hz

  
  
  

Implementation:

$$\mathbf{W}_{\text{lpf}}[n] = \alpha \mathbf{W}_{\text{raw}}[n] + (1-\alpha) \mathbf{W}_{\text{lpf}}[n-1]$$

  

### Gravity and bias compensation operation

  Check this [[force_torque_sensor_calibration]]

###  Deadband Filtering 
  

Applied to compensated wrench data after gravity and bias removal to suppress residual errors and provide clean zero-force detection.

  

$$\mathcal{D}(w_i, \tau_i) = \begin{cases}

0 & \text{if } |w_i| \leq \tau_i \\

w_i & \text{if } |w_i| > \tau_i

\end{cases}$$

  

Default Thresholds: $\tau_f = 0.5$ N (forces), $\tau_\tau = 0.01$ Nm (torques)

  

$$\mathbf{W}_{\text{filtered}} = \begin{bmatrix} \mathcal{D}(\mathbf{f}, \tau_f) \\ \mathcal{D}(\boldsymbol{\tau}, \tau_\tau) \end{bmatrix}$$