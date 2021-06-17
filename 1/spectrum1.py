import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

# signal
x = np.array([-1, 2, 0, 1, 3, 3, 2, 0])

# FFT parameters
N = 1024
xFFT1 = fft(x, N)
xFFT2 = xFFT1[0:int(N/2)]
spectrum = np.abs(xFFT2)

# Plot results

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.ylabel('Value')
plt.xlabel('Time')
plt.title('Signal')
plt.stem(x)
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
