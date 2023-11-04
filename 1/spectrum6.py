import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500                   # Sampling frequency, Hz
t = np.arange(0, 1, 1/fs)  # Time vector, sec

# Generate a harmonic signal: sum of two sine waves
f1, f2 = 5, 50             # Frequencies, Hz
signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# Plot the signal
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Harmonic Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum using magnitude_spectrum function
plt.subplot(2, 1, 2)
plt.magnitude_spectrum(signal, Fs=fs, scale='dB')
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.tight_layout()
plt.show()