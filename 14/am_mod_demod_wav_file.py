import numpy as np
from common import create_harmonic, create_from_wav, am_demod, am_mod, plot_spectrum
from common import filt, interpolate, decimate, create_complex_exponent
import matplotlib.pyplot as plt  
from scipy.io.wavfile import write as write_wav

CARRIER_FREQUENCY = 200e3 # 200 KHz
AM_MODULATION_INDEX = 1

# Read samples from wav file    
# Fs, t, audio_sig = create_from_wav('audio.wav', N=2000)
Fs, t, audio_sig = create_from_wav('audio.wav')

print('Audio Fs =', Fs)

# Interpolate
interp_audio_sig = interpolate(audio_sig, INTERP_ORDER=20, NFIR=101)
Fs_after_interp = 20*Fs # New Fs after interpolation

print('Fs after interpolation =', Fs_after_interp)

# Make AM Modulation
am_mod_sig = am_mod(interp_audio_sig, Fc=CARRIER_FREQUENCY, Fs=Fs_after_interp, mod_id=AM_MODULATION_INDEX)

# Make AM demodulation

demod_sig = am_demod(am_mod_sig, Fc=CARRIER_FREQUENCY, Fs=Fs_after_interp)

# Decimate AM demodulated signal

demod_sig_decim = decimate(demod_sig, DECIM_ORDER=20, NFIR=101)

# Plot signals in time domain

# plt.figure()  
# plt.plot(demod_sig_decim, color='C2', label='AM demodulated signal')
# plt.plot(audio_sig/np.amax(np.absolute(interp_audio_sig)), color='C3', label='Modulation audio signal')
# plt.xlabel('Indexes')
# plt.ylabel('Signal Values')
# plt.legend(loc='upper right')

# Plot am modulated signal in frequency domain

plot_spectrum(am_mod_sig, Fs=Fs_after_interp, NFFT=8192, title='AM Spectrum After Modulation')
plt.show()

# Save demod audio to wav file

MAX_INT16 = 2**15-1

write_wav('demod_signal.wav', int(Fs), np.asarray(MAX_INT16*demod_sig_decim, dtype=np.int16))
