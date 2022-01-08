import numpy as np
from common import create_harmonic, create_from_wav, am_mod, plot_spectrum, filt, interpolate, decimate
import matplotlib.pyplot as plt  

Fcarrier = 200e3

# Read samples from wav file    
Fs, t, audio_sig = create_from_wav('audio.wav', 1000)
print('Audio Fs =', Fs)

# Interpolate
interp_audio_sig = interpolate(audio_sig, INTERP_ORDER=20, NFIR=101)
Fs_after_interp = 20*Fs # New Fs after interpolation

print('Fs after interpolation =', Fs_after_interp)

# Make AM Modulation
am_mod_sig = am_mod(interp_audio_sig, Fc=Fcarrier, Fs=Fs_after_interp, mod_id=1)

# Plot signals in time domain

plt.figure()  
plt.plot(am_mod_sig, color='C2', label='AM modulated signal')
plt.plot(interp_audio_sig/np.amax(np.absolute(interp_audio_sig)), color='C3', label='Modulation audio signal')
plt.xlabel('Indexes')
plt.ylabel('Signal Values')
plt.legend(loc='upper right')

# Plot fm modulated signal in frequency domain

plot_spectrum(am_mod_sig, Fs=Fs_after_interp, NFFT=8192, title='AM Signal Spectrum')

plt.show()
