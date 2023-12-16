import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, firwin

Fs = 100     # Hz
Ts = 1/Fs

Fsig = 5     # Hz

Fc = 10      # Hz

NUM_POINTS = 0.2e3

NFIR = 101

# Create Signal

t = np.arange(NUM_POINTS)*Ts

sig = np.cos(2*np.pi*Fsig*t)

# Filter

fir_taps = firwin(numtaps=NFIR, fs=Fs, cutoff=Fc)

filt_sig = lfilter(fir_taps, 1.0, sig)

# Plot results

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, sig, '-o', color='C1')
plt.xlabel('time, s')
plt.title('Original Signal')
plt.subplot(2, 1, 2)
plt.plot(t, filt_sig, '-o', color='C2')
plt.xlabel('time, s')
plt.title('Filtered Signal')

plt.grid(True)

plt.figure()

plt.subplot(2, 1, 1)
plt.magnitude_spectrum(sig, Fs=Fs, scale='dB')
plt.title("Original Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.subplot(2, 1, 2)
plt.magnitude_spectrum(filt_sig, Fs=Fs, scale='dB')
plt.title("Filtered Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.show()
