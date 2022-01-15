import numpy as np
from common import create_harmonic, create_from_wav, usb_demod, usb_mod, plot_spectrum
from common import filt, interpolate, decimate, create_complex_exponent
import matplotlib.pyplot as plt  
from scipy.io.wavfile import write as write_wav

CARRIER_FREQUENCY = 200e3 # 200 KHz

# Read samples from wav file    
# Fs, t, audio_sig = create_from_wav('audio.wav', N=2000)
Fs, t, audio_sig = create_from_wav('audio.wav')

print('Audio Fs =', Fs)

# Interpolate
interp_audio_sig = interpolate(audio_sig, INTERP_ORDER=20, NFIR=101)
Fs_after_interp = 20*Fs # New Fs after interpolation

print('Fs after interpolation =', Fs_after_interp)

# Make USB Modulation
usb_mod_sig = usb_mod(interp_audio_sig, Fc=CARRIER_FREQUENCY, Fs=Fs_after_interp)

# Make USB demodulation

demod_sig = usb_demod(usb_mod_sig, Fc=CARRIER_FREQUENCY, Fs=Fs_after_interp)

# Decimate USB demodulated signal

demod_sig_decim = decimate(demod_sig, DECIM_ORDER=20, NFIR=101)

# Plot signals in time domain

# plt.figure()  
# plt.plot(demod_sig_decim, color='C2', label='USB demodulated signal')
# plt.plot(audio_sig/np.amax(np.absolute(interp_audio_sig)), color='C3', label='Modulation audio signal')
# plt.xlabel('Indexes')
# plt.ylabel('Signal Values')
# plt.legend(loc='upper right')

# Plot USB modulated signal in frequency domain

plot_spectrum(usb_mod_sig, Fs=Fs_after_interp, NFFT=8192, title='USB Spectrum After Modulation')
plt.show()

# Save demod audio to wav file

MAX_INT16 = 2**15-1

write_wav('demod_signal.wav', int(Fs), np.asarray(MAX_INT16*demod_sig_decim, dtype=np.int16))
