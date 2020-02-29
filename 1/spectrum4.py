import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

# Create Signal

N = 512

t = np.linspace(0, 20, N, endpoint=True)

x = np.zeros(N)

for i in range(1, 10000):
    x += np.sin(i*t)/i

# Get Spectrum

xFFT1 = fft(x, N)

xFFT2 = xFFT1[0:N/2]

spectrum = np.abs(xFFT2)

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
