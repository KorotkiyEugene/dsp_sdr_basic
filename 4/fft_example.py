import numpy as np
import matplotlib.pyplot as plt
import scipy

# Defining Parameters
Fs = 50e6
Ts = 1/Fs

NSAMP = int(1e5)
NFFT = 1024
SNR = 60

F = 4.88e6
Amp = 0.5  # pwr = 20*log10(0.5) = -6.0206 dB

Win = scipy.signal.windows.nuttall(NFFT, sym=False)
WIN_CPG = -20*np.log10(np.sum(Win)/NFFT)  # Window Coherent Power Gain

t = np.arange(1, NSAMP + 1) * Ts

fVals = Fs * np.arange(-NFFT/2, NFFT/2) / NFFT

# Creating Signal, Adding Noise, Calc Reference Signal and Noise Power
sig = Amp * np.exp(2*np.pi*1j*F*t)

measured_pwr_sig = 10*np.log10(np.mean(np.abs(sig)**2))
print("Measured signal power: {:.2f} dB".format(measured_pwr_sig))

sig_w_noise = sig + np.random.normal(0, np.sqrt(10**(-SNR/10)), sig.shape) + 1j * np.random.normal(0, np.sqrt(10**(-SNR/10)), sig.shape)

noise = sig_w_noise - sig

measured_pwr_noise = 10*np.log10(np.mean(np.abs(noise)**2))
print("Measured noise power: {:.2f} dB".format(measured_pwr_noise))

# Spectrum Analysis
fft_sig = np.fft.fftshift(np.fft.fft(sig[:NFFT] * Win, NFFT))
fft_sig_pwr_dB = 10*np.log10(np.abs(fft_sig/NFFT)**2)
fft_sig_pwr_dB += WIN_CPG

plt.figure()
plt.plot(fVals, fft_sig_pwr_dB)
plt.title("Power spectrum for signal without noise")
plt.ylabel("Power, dB")
plt.xlabel("Frequency, Hz")

fft_sig_w_noise = np.fft.fftshift(np.fft.fft(sig_w_noise[:NFFT] * Win, NFFT))
fft_sig_w_noise_pwr_dB = 10*np.log10(np.abs(fft_sig_w_noise/NFFT)**2)
fft_sig_w_noise_pwr_dB += WIN_CPG

plt.figure()
plt.plot(fVals, fft_sig_w_noise_pwr_dB)
plt.title("Power spectrum for signal with noise")
plt.ylabel("Power, dB")
plt.xlabel("Frequency, Hz")

fft_noise = np.fft.fftshift(np.fft.fft(noise[:NFFT] * Win, NFFT))
fft_noise_pwr_dB = 10*np.log10(np.abs(fft_noise/NFFT)**2)
fft_noise_pwr_dB += WIN_CPG

plt.figure()
plt.plot(fVals, fft_noise_pwr_dB)
plt.title("Power spectrum for noise")
plt.ylabel("Power, dB")
plt.xlabel("Frequency, Hz")

measured_pwr_noise_from_spectrum = 10*np.log10(np.sum(np.abs(fft_noise/NFFT)**2))
print("Measured noise power from spectrum: {:.2f} dB".format(measured_pwr_noise_from_spectrum))

plt.show()
