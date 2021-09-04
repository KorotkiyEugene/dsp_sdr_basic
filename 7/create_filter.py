import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, butter, firls, remez, firwin, firwin2, group_delay
from scipy.fftpack import fft, fftshift

NFIR = 101
Fs = 20e3
Fc = 1e3

# Create filter

fir_taps = firwin(numtaps=NFIR, fs=Fs, cutoff=Fc, window=('blackmanharris'), pass_zero='lowpass')

np.savetxt('filter_coeffs.txt', np.transpose(fir_taps), newline=', ')

plt.figure(figsize=(16, 10), dpi=120)

# Plot impulse responce

plt.subplot(1, 2, 1)
plt.title('Impulse responce', fontsize=12)
plt.stem(fir_taps, use_line_collection=True, basefmt='C0')
plt.xlim([0, NFIR-1])
plt.xlabel('Samples')
plt.grid(True)

# Plot freq responce

plt.subplot(1, 2, 2)
plt.title('Frequency responce', fontsize=12)
freq, resp = freqz(fir_taps)
resp = np.abs(resp)
freq = Fs/2*freq/np.pi 
plt.plot(freq, 20*np.log10(resp))
plt.xlabel('Frequency (Hz)')
plt.grid(True)

plt.show()
