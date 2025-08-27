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
power_csv = data['Potenza_dx_W'].to_numpy()
torque_csv = abs(data['Coppia_dx_Nm'].to_numpy())
speed_csv = abs(data['RPM_dx'].to_numpy())
time = data['Tempo_s'].to_numpy()

max_power_idx = np.argmax(power_csv)
max_time = time[max_power_idx]
max_torque_csv = abs(torque_csv[max_power_idx])
max_speed_csv = abs(speed_csv[max_power_idx])

print(f"Maximum power: {power_csv[max_power_idx]} W at time: {max_time} s")
print(f"Maximum torque: {max_torque_csv} Nm at time: {max_time} s")
print(f"Maximum speed: {max_speed_csv} RPM at time: {max_time} s")

# -------------------------------
# Motor and system configuration
# -------------------------------
R = 0.035
tau_c = 0.1078       # K * i_n
#torque constant
K = 0.0674
V = 48

#stall current (A)
i_s = 350
#no load current (A)
i_n = 1.6
#no load speed (rad/s)
omega_nl_rads = (V-R*i_n)/K
omega_nl_RPM=omega_nl_rads*60/(2*np.pi)

i_model  = np.arange(i_n, i_s, 0.01)
current_csv = torque_csv/K
# -------------------------------
# Motor behavior calculations
# -------------------------------
torque_model = K * i_model - tau_c
omega_model = (V - i_model * R) / K #rad/s
rpm_model = omega_model * 60 / (2 * np.pi) #RPM
power_model = torque_model * omega_model #W
eta = (-R*K*i_model**2 + (tau_c*R + V*K)*i_model - tau_c*V) / (V*K*i_model)

max_power_index = np.argmax(power_model)
max_speed_model = rpm_model[max_power_index]
max_torque_model = torque_model[max_power_index]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(i_model, rpm_model, label="Datasheet limits", color='r', linewidth=2)
ax1.plot(current_csv, speed_csv, label="Actual", color='b', linewidth=2)

ax2 = ax1.twinx()
ax2.plot(i_model, eta, 'r-', label="Efficiency",color='k', linewidth=2)
ax2.set_ylabel('Efficiency', color='r')
ax2.tick_params(axis='y', labelcolor='r')

ax1.set_ylabel("Speed (rad/s)")
ax1.set_xlabel("Torque (Nm)", color='k')
ax1.set_xlim([i_n, i_s])
ax1.set_ylim([0, omega_nl_RPM])
ax1.tick_params(axis='y')
plt.legend()
ax1.grid(True)


# -------------------------------
# Plotting curve for motor
# -------------------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(rpm_model, torque_model, label="Torque", color='b', linewidth=2)
ax1.plot(max_speed_csv, max_torque_csv, 'x', color='orange', markersize=15, label='Max Power Point')

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
plt.plot(current_csv, 'r')
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
