import numpy as np
from common import create_harmonic, plot_spectrum
import matplotlib.pyplot as plt
from scipy.signal import hilbert

Fsamp_rate = 100e3    
Fsig = 10e3        # Frequency of signal 
    
dummy, t, signal = create_harmonic(Fc=Fsig, Fs=Fsamp_rate, Amp=1, N=1e3)   

complex_signal = hilbert(signal)

#complex_signal = np.imag(complex_signal) + 1j*np.real(complex_signal)
complex_signal = np.real(complex_signal) - 1j*np.imag(complex_signal)

# Plot spectrums for signal and complex signal

plot_spectrum(signal, Fs=Fsamp_rate, NFFT=8192, title="Signal's Spectrum")
plot_spectrum(complex_signal, Fs=Fsamp_rate, NFFT=8192, title="Signal's Spectrum after Hilbert Transform")

plt.show()

