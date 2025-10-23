# Simple Harmonic Motion (SHM) - Interactive version
import numpy as np
import matplotlib.pyplot as plt

# --- User Inputs ---
A = float(input("Enter amplitude (meters): "))
w = float(input("Enter angular frequency (rad/s): "))
phi = float(input("Enter phase (radians): "))
t_max = float(input("Enter total time (seconds): "))
dt = float(input("Enter time step (seconds): "))

# --- Time array ---
t = np.arange(0, t_max, dt)

# --- SHM Equations ---
x = A * np.cos(w * t + phi)            # Displacement
v = -A * w * np.sin(w * t + phi)       # Velocity

# --- Plot Displacement & Velocity vs Time ---
plt.figure(figsize=(10,5))
plt.plot(t, x, label='Displacement (x)')
plt.plot(t, v, label='Velocity (v)')
plt.title('Simple Harmonic Motion')
plt.xlabel('Time (s)')
plt.ylabel('Displacement / Velocity')
plt.legend()
plt.grid(True)
plt.show()
