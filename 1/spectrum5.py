import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

# Create Signal

N = 512

ZEROS_N = int(N/4);

t = np.linspace(0, 0.5, N, endpoint=True)

f1 = 1000

x = np.zeros(N);

x = x + np.sin(2*np.pi*f1*t)

#x[1:ZEROS_N] = 0;

# Get Spectrum

xFFT1 = fft(x, N)

xFFT2 = xFFT1[0:int(N/2)]

spectrum = 20*np.log10(np.abs(xFFT2)*2/N)

# Plot results

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.ylabel('Value')
plt.xlabel('Time')
plt.title('Signal')
plt.plot(x)
plt.grid()

plt.subplot(1, 2, 2)
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.title('Spectrum')
plt.plot(spectrum)
plt.xlim([0, N/2])
plt.grid()

plt.tight_layout()
plt.show()

