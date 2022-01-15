import numpy as np
from common import create_from_wav, plot_spectrum
import matplotlib.pyplot as plt  
from scipy.signal import hilbert

# Read signal's samples from wav file    
Fsamp_rate, t, signal = create_from_wav('audio.wav', 1000)

complex_signal = hilbert(signal)

#complex_signal = np.imag(complex_signal) + 1j*np.real(complex_signal)
complex_signal = np.real(complex_signal) - 1j*np.imag(complex_signal)

# Plot spectrums for signal and complex signal

plot_spectrum(signal, Fs=Fsamp_rate, NFFT=8192, title="Signal's Spectrum")
plot_spectrum(complex_signal, Fs=Fsamp_rate, NFFT=8192, title="Signal's Spectrum after Hilbert Transform")

plt.show()

