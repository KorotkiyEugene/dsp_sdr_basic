import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, firwin

Fs = 100     # Hz
Ts = 1/Fs

F1 = 1       # Hz

NUM_POINTS = 0.3e3

NFIR = 101
DECIM_ORDER = 10

# Create Signal

t = np.arange(NUM_POINTS)*Ts

sig = np.cos(2*np.pi*F1*t)

# Decimate

decim_fir_taps = firwin(numtaps=NFIR, fs=Fs, cutoff=Fs/(2*DECIM_ORDER))

filt_sig = lfilter(decim_fir_taps, 1.0, sig)

decim_sig = filt_sig[::DECIM_ORDER]

#print(filt_sig[0:100])
#print(decim_sig[0:100])

# Plot results

plt.figure()
plt.title('Signal')
plt.plot(filt_sig, '-o', color='C1')
plt.stem(np.linspace(0, NUM_POINTS-DECIM_ORDER, decim_sig.size), decim_sig, linefmt='C2', basefmt='C0')

plt.xlabel('Indexes')
plt.grid(True)

plt.figure()

plt.subplot(2, 1, 1)
plt.magnitude_spectrum(sig, Fs=Fs, scale='dB')
plt.title("Original Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.subplot(2, 1, 2)
plt.magnitude_spectrum(decim_sig, Fs=Fs/DECIM_ORDER, scale='dB')
plt.title("Decimated Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.show()
