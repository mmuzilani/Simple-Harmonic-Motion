# Simple Harmonic Motion (SHM) - Interactive Version


## Features
- Users can input:
  - **Amplitude (A)** in meters
  - **Angular frequency (w)** in rad/s
  - **Phase (φ)** in radians
  - **Total simulation time (t_max)** in seconds
  - **Time step (dt)** in seconds
- Calculates **displacement** and **velocity** over time.
- Plots both **displacement** and **velocity** on a single graph using `matplotlib`.
- Beginner-friendly and easy to experiment with different SHM parameters.

## Example Input
amplitude (meters): 2
angular frequency (rad/s): 2
phase (radians): 0
total time (seconds): 10
time step (seconds): 0.01


## How to Run
1. Make sure Python is installed.
2. Install required libraries if not installed:
   ```bash
   pip install numpy matplotlib

Enter the values when prompted.

A graph showing displacement vs time and velocity vs time will be displayed.

Notes

Try changing amplitude, frequency, and phase to see how the SHM changes.

Smaller dt gives smoother curves but may take slightly longer to compute.
