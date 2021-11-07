import numpy as np
import matplotlib.pyplot as plt

Fs = 2.4e6 # 2.4 MSPS

raw_data = np.fromfile("recorded_signal.dat", dtype="float32")

complex_sig = raw_data[0::2] + 1j*raw_data[1::2]

plt.psd(complex_sig, NFFT=1024, Fs=Fs)
plt.title("Power spectrum of 'signal' loaded from file")
plt.show() 