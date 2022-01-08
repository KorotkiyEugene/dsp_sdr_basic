import numpy as np
from common import create_harmonic, create_from_wav, am_mod, plot_spectrum
import matplotlib.pyplot as plt

Fsamp_rate = 100e3    
Fmod = 0.1e3        # Frequency of modulation signal 
Fcarrier = 5e3            # Frequency of carrier signal 
    
dummy, t, sig = create_harmonic(Fc=Fmod, Fs=Fsamp_rate, Amp=1, N=2e3)   

am_mod_sig = am_mod(sig, Fc=Fcarrier, Fs=Fsamp_rate, mod_id=1)

# Plot signals in time domain

plt.figure()  
plt.plot(am_mod_sig, color='C2', label='AM modulated signal')
plt.plot(sig, color='C3', label='Modulation signal')
plt.xlabel('Indexes')
plt.ylabel('Signal Values')
plt.legend(loc='upper right')

# Plot fm modulated signal in frequency domain

plot_spectrum(am_mod_sig, Fs=Fsamp_rate, NFFT=8192, title='AM signal Spectrum')

plt.show()