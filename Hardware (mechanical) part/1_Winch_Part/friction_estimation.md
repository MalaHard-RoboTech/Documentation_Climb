# Lecture: Identifying Friction Parameters from Motor Telemetry

## 🧬 Fundamental Model

We begin with the dynamic equation of a motor system:

$$
\tau_m = \hat{\tau}_{fr}(\dot{\theta}) + I\ddot{\theta} + \tau_{gp}
$$


Where:

- $\tau_m$: measured motor torque (from telemetry)  
- $\hat{\tau}_{fr}(\dot{\theta})$: modeled friction torque (function of velocity)  
- $I \ddot{\theta}$: inertial torque (acceleration component)  
- $\tau_{gp}$: gravity or passive torque (e.g. cables, bias)


In low acceleration ramps, we approximate:

$$
\tau_m \approx \hat{\tau}_{fr}(\dot{\theta})
$$

---

## 🔢 Friction Model

We define the friction torque model as:
$$
\hat{\tau}_{fr}(\dot{\theta}) = \operatorname{sgn}(\dot{\theta}) \left[ \tau_c + (\tau_s - \tau_c) \cdot e^{-\left|\frac{\dot{\theta}}{\theta_{th}}\right|} \right] + k_v \dot{\theta}
$$

$$
\hat{\tau}_{fr}(\dot{\theta}) = \operatorname{sgn}(\dot{\theta}) \left[ P_1 + P_2 \cdot e^{-\left|\frac{\dot{\theta}}{P_3}\right|} \right] + P_4 \dot{\theta}
$$
Where:

- $P_1 = \tau_c$: Coulomb friction  
- $P_2 = \tau_s$: Stiction (static friction)  
- $P_3 = \theta_{\text{th}}$: Transition threshold (velocity scale of exponential decay)  
- $P_4 = k_v$: Viscous coefficient (proportional to velocity)

---

## ✅ Goal

Estimate coefficients $P_1$, $P_2$, $P_3$, $P_4$ using real telemetry from:

- $\dot{\theta}$: motor velocity (rad/s)  
- $\tau_m$: motor torque (Nm)


---

## ➜ Step 1: Velocity Ramps

Perform a series of positive and negative velocity ramps, ideally:

- Slowly sweep $\dot{\theta}$ from $-\omega_{\text{max}}$ to $+\omega_{\text{max}}$
- Include dwell time at each step to reduce acceleration
- Repeat multiple times to reduce noise

---

## ➜ Step 2: Record Telemetry

From your data source (e.g. `ArganelloEnhancedTelemetry`):

- Extract:
  - $\dot{\theta}$: `motor_vel`
  - $\tau_m$: `motor_torque`

Construct the dataset:

- For each sample:
  - $x = [\text{sgn}(\dot{\theta}), e^{-|\dot{\theta}| / P_3}, \dot{\theta}]$
  - $y = \tau_m$

---

## ➜ Step 3: Nonlinear Least Squares Estimation

You are solving:

$$
\tau_m = \text{sgn}(\dot{\theta}) \cdot \left( P_1 + P_2 \cdot e^{-|\dot{\theta}| / P_3} \right) + P_4 \cdot \dot{\theta}
$$

This is a **nonlinear regression problem**. Use `scipy.optimize.curve_fit` to fit:

In this step, we estimate the friction parameters \( P_1, P_2, P_3, P_4 \) by **minimizing the sum of squared errors** between the measured motor torque and the modeled friction torque.

We define the following cost function:

$$
J(P_1, P_2, P_3, P_4) = \sum_{i=1}^{n} \left( \tau_{m,i}^{\text{measured}} - \tau_{m,i}^{\text{model}} \right)^2
$$

Nonlinear solvers **require an initial guess**. Good initial values improve convergence and prevent local minima.

A reasonable starting point could be:

- $P_1 = 0.2$ — approximate Coulomb friction (Nm)  
- $P_2 = 0.1$ — exponential slope (Nm)  
- $P_3 = 0.5$ — transition velocity (rad/s)  
- $P_4 = 0.01$ — viscous gain (Nm⋅s/rad)


These will be refined by the optimizer to best fit your data.


```python
import numpy as np
from scipy.optimize import curve_fit

# Fill in actual telemetry data
velocities = np.array([...])  # rad/s
torques = np.array([...])     # Nm

def friction_model(w, P1, P2, P3, P4):
    return np.sign(w) * (P1 + P2 * np.exp(-np.abs(w) / P3)) + P4 * w

# Initial guess for [P1, P2, P3, P4]
initial_guess = [0.1, 0.1, 1.0, 0.01]

params, _ = curve_fit(friction_model, velocities, torques, p0=initial_guess)
P1, P2, P3, P4 = params

print(f"P1 (Coulomb):   {P1:.4f} Nm")
print(f"P2 (stiction):  {P2:.4f} Nm")
print(f"P3 (threshold): {P3:.4f} rad/s")
print(f"P4 (viscous):   {P4:.4f} Nm⋅s/rad")
```

---

## 📊 Step 4: Plot and Validate

To validate your model visually:

```python
import matplotlib.pyplot as plt

predicted = friction_model(velocities, *params)

plt.plot(velocities, torques, 'b.', label='Measured')
plt.plot(velocities, predicted, 'r-', label='Model')
plt.xlabel("Velocity (rad/s)")
plt.ylabel("Torque (Nm)")
plt.grid(True)
plt.title("Friction Model Fit (Nonlinear)")
plt.legend()
plt.show()
```

---

> 🧠 This approach captures the exponential transition between stiction and Coulomb friction, and includes a viscous term. It is significantly more expressive than the linear approximation.


