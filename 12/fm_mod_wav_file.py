import numpy as np
from common import create_harmonic, create_from_wav, fm_mod, plot_spectrum, filt, interpolate, decimate
import matplotlib.pyplot as plt  

# Read samples from wav file    
Fs, t, audio_sig = create_from_wav('audio.wav', 1000)
print('Audio Fs =', Fs)

# Interpolate
interp_audio_sig = interpolate(audio_sig, INTERP_ORDER=20, NFIR=101)
Fs_after_interp = 20*Fs # New Fs after interpolation

print('Fs after interpolation =', Fs_after_interp)

# Make FM Modulation
fm_mod_sig = fm_mod(interp_audio_sig, Fc=200e3, Fs=Fs_after_interp, FM_dev = 25e3)

# Plot signals in time domain

plt.figure()  
plt.plot(fm_mod_sig, color='C2', label='FM modulated signal')
plt.plot(interp_audio_sig/np.amax(np.absolute(interp_audio_sig)), color='C3', label='Modulation audio signal')
plt.xlabel('Indexes')
plt.ylabel('Signal Values')
plt.legend(loc='upper right')

# Plot fm modulated signal in frequency domain

plot_spectrum(fm_mod_sig, Fs=Fs_after_interp, NFFT=8192, title='FM Spectrum')

plt.show()
