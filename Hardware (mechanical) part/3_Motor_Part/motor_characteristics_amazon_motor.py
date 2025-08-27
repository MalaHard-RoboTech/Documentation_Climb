import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# import csv data
# -------------------------------
file_path = 'dati_motore_dx.csv'
data = pd.read_csv(file_path)

# -------------------------------
# max value about simulation
# -------------------------------
#rochetto diameter 5cm 
power_csv = data['Potenza_dx_W'].to_numpy()
torque_csv = data['Coppia_dx_Nm'].to_numpy()
speed_csv = data['RPM_dx'].to_numpy()
time = data['Tempo_s'].to_numpy()

max_power_idx = np.argmax(power_csv)
max_time = time[max_power_idx]
max_torque_csv = abs(torque_csv[max_power_idx])
max_speed_csv = abs(speed_csv[max_power_idx])

print(f"Maximum power: {power_csv[max_power_idx]} W at time: {max_time} s")
print(f"Maximum torque: {max_torque_csv} Nm at time: {max_time} s")
print(f"Maximum speed: {max_speed_csv} RPM at time: {max_time} s")


# --------------------------------------
# 1. Raw Motor Specifications (from Amazon)
# --------------------------------------
motor_specs = {
    "model": "6384",
    "kv_rating_rpm_per_v": 120,                 # KV in RPM/V
    "nominal_voltage_range_v": (24, 36),        # Operating voltage
    "no_load_speed_rpm_24v": 3600,
    "no_load_current_a_12v": 2.5,
    "max_power_w": 4600,
    "efficiency": 0.85,
    "max_load_kg": 150,
    "shaft_diameter_mm": 10,
    "dimensions_mm": (63, 80),                  # Diameter, Length
    "weight_g": 1052
}

# --------------------------------------
# 2. Derived Motor Constants
# --------------------------------------

# Kv (RPM/V) to K (Nm/A)
Kv = motor_specs["kv_rating_rpm_per_v"]
K = 60 / (2 * np.pi * Kv)  # Motor constant [Nm/A]

# Operating voltage (updated to 36V)
V = 36

# No-load speed at 36V (extrapolate linearly from 24V spec)
rpm_noload = motor_specs["no_load_speed_rpm_24v"] * (36 / 24)
omega_noload = rpm_noload * 2 * np.pi / 60  # Convert to rad/s

# No-load current (scaled linearly from 12V value)
i_n = motor_specs["no_load_current_a_12v"] * 3  # Approx ~7.5 A

# Estimate resistance (assumed)
R = 0.05  # Ohm

# Estimate Coulomb friction torque
tau_c = K * i_n  # Nm

# Max operating current estimate from max power
# Guess omega at full power (~300 rad/s)
i_s = motor_specs["max_power_w"] / (K * 300)  # i = P / (K * omega)
i_s = min(i_s, 50)  # Clamp to 150A

# --------------------------------------
# 3. Motor Behavior Modeling
# --------------------------------------

i = np.arange(i_n, i_s, 0.1)  # Current sweep

torque_model = K * i - tau_c
omega_model = (V - i * R) / K
rpm_model = omega_model * 60 / (2 * np.pi)
power_model = torque_model * omega_model

# Efficiency model (from derived formula)
eta = (-R * K * i**2 + (tau_c * R + V * K) * i - tau_c * V) / (V * K * i)

# --------------------------------------
# 4. Print Summary
# --------------------------------------
print("Motor Constant K (Nm/A):", round(K, 4))
print("Estimated Resistance R (Ohm):", R)
print("Coulomb Torque tau_c (Nm):", round(tau_c, 4))
print("Voltage V (V):", V)
print("No-load Current i_n (A):", i_n)
print("Estimated Max Current i_s (A):", round(i_s, 2))


max_power_index = np.argmax(power_model)
max_speed_model = rpm_model[max_power_index]
max_torque_model = torque_model[max_power_index]

# -------------------------------
# Plotting curve for motor
# -------------------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(rpm_model, torque_model, label="Torque", color='b', linewidth=2)
ax1.plot(max_speed_csv, max_torque_csv, 'x', color='orange', markersize=15, label='Max Power Point')
ax1.plot(max_speed_csv, max_torque_csv, 'o', color='red', markersize=5)

ax1.set_xlabel("Speed (RPM)")
ax1.set_ylabel("Torque (Nm)", color='k')
ax1.tick_params(axis='y')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(rpm_model, power_model, label="Power", color='r', linestyle='--', linewidth=2)
ax2.set_ylabel("Power (W)", color='k')
ax2.tick_params(axis='y')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper center')

plt.title("Torque and Power vs Speed (RPM) - Single Motor @ 36V")
fig.tight_layout()
# plt.show()

# -------------------------------
# Plotting csv data
# -------------------------------
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(torque_csv, 'b')
plt.plot(max_power_idx, torque_csv[max_power_idx], 'x', color='orange', label='Max Torque')
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('Torque [Nm]')
plt.title('CSV Data: Torque')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(speed_csv, 'r')
plt.plot(max_power_idx, speed_csv[max_power_idx], 'x', color='orange', label='Max Speed')
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('Speed [RPM]')
plt.title('CSV Data: Speed')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(power_csv, 'g')
plt.plot(max_power_idx, power_csv[max_power_idx], 'x', color='orange', label='Max Power')
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('Power [W]')
plt.title('CSV Data: Power')
plt.legend()

plt.tight_layout()
plt.show()
