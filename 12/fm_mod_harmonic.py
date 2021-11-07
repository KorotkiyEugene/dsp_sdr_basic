import numpy as np
from common import create_harmonic, create_from_wav, fm_mod, plot_spectrum
import matplotlib.pyplot as plt

Fsamp_rate = 100e3    
    
dummy, t, sig = create_harmonic(Fc=0.1e3, Fs=Fsamp_rate, Amp=0.5, N=2e3)   

fm_mod_sig = fm_mod(sig, Fc=5e3, Fs=Fsamp_rate, FM_dev = 2e3)

# Plot signals in time domain

plt.figure()  
plt.plot(fm_mod_sig, color='C2', label='FM modulated signal')
plt.plot(sig, color='C3', label='Modulation signal')
plt.xlabel('Indexes')
plt.ylabel('Signal Values')
plt.legend(loc='upper right')

# Plot fm modulated signal in frequency domain

plot_spectrum(fm_mod_sig, Fs=Fsamp_rate, NFFT=8192, title='FM Spectrum')

plt.show()