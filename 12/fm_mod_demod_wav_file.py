import numpy as np
from common import create_harmonic, create_from_wav, fm_demod, fm_mod, plot_spectrum
from common import filt, interpolate, decimate, create_complex_exponent
import matplotlib.pyplot as plt  
from scipy.io.wavfile import write as write_wav

FM_CARRIER = 200e3 # 200 KHz
FM_DEVIATION = 25e3

# Read samples from wav file    
Fs, t, audio_sig = create_from_wav('audio.wav')
print('Audio Fs =', Fs)

# Interpolate
interp_audio_sig = interpolate(audio_sig, INTERP_ORDER=20, NFIR=101)
Fs_after_interp = 20*Fs # New Fs after interpolation

print('Fs after interpolation =', Fs_after_interp)

# Make FM Modulation
fm_mod_sig = fm_mod(interp_audio_sig, Fc=FM_CARRIER, Fs=Fs_after_interp, FM_dev=FM_DEVIATION)

# Shift FM carrier to zero frequency and filter to make IQ

shifted_to_zero_fm_sig = fm_mod_sig*create_complex_exponent(Fc=-FM_CARRIER, Fs=Fs_after_interp, Amp=1, N=len(fm_mod_sig))
sig_iq = filt(shifted_to_zero_fm_sig, Fc=0.5, NFIR=101)

# Make FM demodulation

demod_sig = fm_demod(sig_iq, Fs=Fs_after_interp, FM_dev=FM_DEVIATION)

# Decimate FM demodulated signal

demod_sig_decim = decimate(demod_sig, DECIM_ORDER=20, NFIR=101)

# Plot signals in time domain

# plt.figure()  
# plt.plot(demod_sig_decim, color='C2', label='FM demodulated signal')
# plt.plot(audio_sig/np.amax(np.absolute(interp_audio_sig)), color='C3', label='Modulation audio signal')
# plt.xlabel('Indexes')
# plt.ylabel('Signal Values')
# plt.legend(loc='upper right')

# Plot fm modulated signal in frequency domain

plot_spectrum(shifted_to_zero_fm_sig, Fs=Fs_after_interp, NFFT=8192, title='FM Spectrum after freq shift')
plot_spectrum(sig_iq, Fs=Fs_after_interp, NFFT=8192, title='FM IQ Spectrum')

plt.show()


# Save demod audio to wav file

MAX_INT16 = 2**15-1

write_wav('demod_signal.wav', int(Fs), np.asarray(MAX_INT16*demod_sig_decim, dtype=np.int16))
