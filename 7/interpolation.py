import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, firwin

Fs = 100     # Hz
Ts = 1/Fs

F1 = 1       # Hz

NUM_POINTS = 0.2e3

NFIR = 101
INTERP_ORDER = 10

# Create Signal

t = np.arange(NUM_POINTS)*Ts

sig = np.cos(2*np.pi*F1*t)

# Interpolate

sig_with_zeros = np.zeros(int(NUM_POINTS*INTERP_ORDER))
sig_with_zeros[::INTERP_ORDER] = sig

#print(sig)
#print(sig_with_zeros)

interp_fir_taps = firwin(numtaps=NFIR, fs=Fs*INTERP_ORDER, cutoff=Fs/2)

interp_sig = lfilter(interp_fir_taps, 1.0, sig_with_zeros)

interp_sig = INTERP_ORDER*interp_sig;

# Plot results

plt.figure()
plt.title('Signal')
plt.plot(interp_sig[int(NFIR/2):], '-o', color='C1')
plt.stem(sig_with_zeros, linefmt='C2', basefmt='C0')

plt.xlabel('Indexes')
plt.grid(True)

plt.figure()

plt.subplot(2, 1, 1)
plt.magnitude_spectrum(sig, Fs=Fs, scale='dB')
plt.title("Original Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.subplot(2, 1, 2)
plt.magnitude_spectrum(interp_sig, Fs=Fs*INTERP_ORDER, scale='dB')
plt.title("Interpolated Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.show()
