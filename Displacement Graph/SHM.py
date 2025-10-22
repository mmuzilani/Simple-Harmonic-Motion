# Simple Harmonic Motion using Python
import numpy as np
import matplotlib.pyplot as plt

# Parameters

# some basic values
A = 1   # amplitude
w = 2 * np.pi   # angular frequency
phi = 0   # phase
t = np.linspace(0, 2, 500)   # time range

# Displacement
x = A * np.cos(w * t + phi)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(t, x, linewidth=2)
plt.title('Simple Harmonic Motion')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)


# Save & show
plt.savefig('shm.png')
plt.show()
