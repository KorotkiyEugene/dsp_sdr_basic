import numpy as np
import matplotlib.pyplot as plt
from common import filt, fm_demod, decimate, create_complex_exponent 
from scipy.io.wavfile import write as write_wav

Fs = 2.4e6           # 2.4 MSPS
FM_CARRIER = 0       # Hz
FM_DEVIATION = 50e3  # Hz
FM_DEMOD_WAV_FILE_NAME = 'fm_station.wav'

# Read recorded complex radio signal from file

raw_data = np.fromfile("recorded_signal.dat", dtype="float32")
complex_sig = raw_data[0::2] + 1j*raw_data[1::2]

plt.figure()
plt.psd(complex_sig, NFFT=1024, Fs=Fs)
plt.title("Power spectrum of 'signal' loaded from file")

# Shift FM carrier to zero frequency and filter to make IQ

shifted_to_zero_complex_sig = complex_sig*create_complex_exponent(Fc=-FM_CARRIER, Fs=Fs, Amp=1, N=len(complex_sig))
sig_iq = filt(shifted_to_zero_complex_sig, Fs=Fs, Fc=150e3, NFIR=101)

plt.figure()
plt.psd(shifted_to_zero_complex_sig, NFFT=1024, Fs=Fs)
plt.title("Power spectrum of shifted 'signal'")

# Decimate by 6 before FM demodulation (to decrease amount of data)

sig_iq_decim = decimate(sig_iq, Fs=Fs, DECIM_ORDER=6, NFIR=101)

plt.figure()
plt.psd(sig_iq_decim, NFFT=1024, Fs=Fs/6)
plt.title("Power spectrum of 'signal' before FM demodulation")

# Make FM demodulation

demod_sig = fm_demod(sig_iq_decim, Fs=Fs/6, FM_dev=FM_DEVIATION)

# Decimate FM demodulated signal

demod_sig_decim = decimate(demod_sig, Fs=Fs, DECIM_ORDER=10, NFIR=101)

plt.figure()
plt.psd(demod_sig_decim, NFFT=1024, Fs=Fs/60)
plt.title("Power spectrum of 'signal' after FM demodulation")

plt.show()

# Save demod audio to wav file

MAX_INT16 = 2**15-1

write_wav(FM_DEMOD_WAV_FILE_NAME, int(Fs/60), np.asarray(MAX_INT16*demod_sig_decim, dtype=np.int16))