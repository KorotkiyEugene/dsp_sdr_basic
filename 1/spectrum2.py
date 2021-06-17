import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

# Create Signal

N = 512

t = np.linspace(0, 0.5, N, endpoint=True)

f1 = 1000

f2 = 2000

f3 = 5000

x = np.zeros(N)

#x = x + np.sin(2*np.pi*f1*t)

#x = x + np.sin(2*np.pi*f2*t)

#x = x + np.sin(2*np.pi*f3*t)

# Get Spectrum

xFFT1 = fft(x, N)

xFFT2 = xFFT1[0:int(N/2)]

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
