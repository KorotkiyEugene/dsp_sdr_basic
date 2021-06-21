import serial, time
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

Fs = 6250     # Hz
Ts = 1/Fs
NFFT = 4*1024
OFFSET = int(0.1*NFFT)

# Time vector
t = np.linspace(0, NFFT-1, NFFT)*Ts
# Frequency vector
f = np.linspace(0, int(NFFT/2)-1, int(NFFT/2))*Fs/NFFT

#ser=serial.Serial("/dev/ttyACM1",115200,timeout=1)
ser=serial.Serial(port="COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# Wait for serial to be ready
time.sleep(1)
# Flush buffers
ser.flushInput()

x = np.zeros(NFFT+OFFSET)
 
for i in range(NFFT+OFFSET):
    x[i] = 5*float(ser.readline().strip().decode())/1024;
    #print(x[i])

ser.close()

# Get Spectrum

x = x[OFFSET-1:-1]

xFFT1 = fft(x, NFFT)/NFFT
xFFT2 = xFFT1[0:int(NFFT/2)]

spectrum = 20*np.log10(np.abs(xFFT2))

# Plot results

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.ylabel('Value (volts)')
plt.xlabel('Time (seconds)')
plt.title('Signal')
plt.plot(t, x)
plt.grid()

plt.subplot(1, 2, 2)
plt.ylabel('Power (dBm)')
plt.xlabel('Frequency (Hz)')
plt.title('Spectrum')
plt.plot(f, spectrum)
plt.grid()

plt.tight_layout()
plt.show()
