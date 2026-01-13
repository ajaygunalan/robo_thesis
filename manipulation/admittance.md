# Admittance Controller: Key Equations

## 1. Admittance Dynamics

$$\ddot{x}_k = M^{-1}(F_k - D\dot{x}_k - Kx_k)$$

## 2. Integration

$$\dot{x}_{k+1} = \dot{x}_k + \ddot{x}_k \cdot \Delta t$$

$$x_{k+1} = x_k + \dot{x}_{k+1} \cdot \Delta t$$

## 3. Velocity Command

$$v_{k+1} = \dot{x}_{k+1} + K_p \cdot e_k$$

Where:

$$e_k = x_{des} - x_{curr,k}$$