import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.io.wavfile import read as read_wav
from scipy.io.wavfile import write as write_wav
from scipy.fftpack import fft, fftshift
from scipy.signal import lfilter, firwin
from scipy.signal import hilbert

def filt(sig, Fc=0.5, NFIR=101):
    fir_taps = firwin(NFIR, Fc, window=('blackmanharris'))
    filtered_signal = lfilter(fir_taps, 1.0, sig)
    return filtered_signal

def interpolate(sig, INTERP_ORDER=10, NFIR=101):
    sig_with_zeros = np.zeros(int(len(sig)*INTERP_ORDER))
    sig_with_zeros[::INTERP_ORDER] = sig
    interp_sig = INTERP_ORDER*filt(sig_with_zeros, 1/INTERP_ORDER, NFIR)
    return interp_sig

def decimate(sig, DECIM_ORDER=10, NFIR=101):
    filt_sig = filt(sig, 1/DECIM_ORDER, NFIR)
    decim_sig = filt_sig[::DECIM_ORDER]
    return decim_sig

def plot_spectrum(sig, Fs=100e3, NFFT=8192, title='Spectrum'):
    f = np.linspace(-int(NFFT/2), int(NFFT/2)-1, int(NFFT))*Fs/NFFT
    sigFFT = fft(sig, NFFT)/NFFT
    sigFFT = fftshift(sigFFT)
    spectrum = 20*np.log10(np.abs(sigFFT))
    plt.figure() 
    plt.plot(f, spectrum)   
    plt.ylabel('Power (dBm)')
    plt.xlabel('Frequency (Hz)')
    plt.title(title)
    #plt.ylim([-150, 0])
    plt.grid(True)

def fm_demod(sig, Fs=100e3, FM_dev = 2e3):
    sig_len = len(sig)
    
    fm_demod_sig = np.zeros(sig_len)
    
    last_angle = 0.0
    last_demod_data = 0.0
    
    for ii in range(0, sig_len):
        i = np.real(sig[ii])
        q = np.imag(sig[ii])
        angle = math.atan2(q, i)
       
        angle_change = angle - last_angle
       
        if angle_change > math.pi:
            angle_change -= 2 * math.pi
        elif angle_change < -math.pi:
            angle_change += 2 * math.pi
        
        last_angle = angle
        
        demod_data = angle_change * Fs / (2 * math.pi * FM_dev)
        
        if abs(demod_data) >= 1:
            # some unexpectedly big angle change happened
            demod_data = last_demod_data
        last_demod_data = demod_data
       
        fm_demod_sig[ii] = demod_data
    
    return fm_demod_sig

def fm_mod(sig, Fc=5e3, Fs=100e3, FM_dev=2e3):
    sig_len = len(sig)
    sig = np.array(sig)
    sig_max_val = np.amax(np.absolute(sig)) 
    sig = sig/sig_max_val #normalizing signal (max val = 1, min val = -1)
    
    dF = sig*FM_dev
    F = Fc + dF
    
    phase = 0
    fm_mod_sig = np.zeros(sig_len)
    
    for ii in range(0, sig_len):
       phase = phase + 2*np.pi*F[ii]/Fs
       fm_mod_sig[ii] = np.cos(phase)
    
    return fm_mod_sig

def am_mod(sig, Fc=5e3, Fs=100e3, mod_id=1):
    sig_len = len(sig)
    sig = np.array(sig)
    sig_max_val = np.amax(np.absolute(sig)) 
    sig = sig/sig_max_val #normalizing signal (max val = 1, min val = -1)
    dummy, t, carrier_sig = create_harmonic(Fc=Fc, Fs=Fs, Amp=1, N=sig_len)  
    am_mod_sig = (1 + sig*mod_id)*carrier_sig
    return am_mod_sig    

def am_demod(sig, Fc=1e3, Fs=100e3):
    sig_len = len(sig)
    shifted_to_zero_am_sig = sig*create_complex_exponent(Fc=-Fc, Fs=Fs, Amp=1, N=sig_len)
    sig_iq = filt(shifted_to_zero_am_sig, Fc=0.5, NFIR=101)    
    #print('max abs(real):')
    #print(max(abs(np.real(sig_iq))))
    #print('max abs(imag):')
    #print(max(abs(np.imag(sig_iq))))
    am_demod_sig = 2*abs(sig_iq)-1
    return am_demod_sig

def usb_mod(sig, Fc=5e3, Fs=100e3):
    sig_len = len(sig)
    sig = np.array(sig)
    sig_max_val = np.amax(np.absolute(sig)) 
    sig = sig/sig_max_val #normalizing signal (max val = 1, min val = -1)
    carrier = create_complex_exponent(Fc=Fc, Fs=Fs, Amp=1, N=sig_len)  
    usb_mod_sig = hilbert(sig)*carrier
    return np.real(usb_mod_sig) 
    
def usb_demod(sig, Fc=1e3, Fs=100e3):
    sig_len = len(sig)
    shifted_to_zero_sig = sig*create_complex_exponent(Fc=-Fc, Fs=Fs, Amp=1, N=sig_len)
    sig_iq = filt(shifted_to_zero_sig, Fc=0.5, NFIR=101)    
    am_demod_sig = 2*np.real(sig_iq)
    return am_demod_sig
    
def create_harmonic(Fc=1e3, Fs=20e3, Amp=1, N=2e1):
    time_indexes = np.arange(N)
    time_values = time_indexes/Fs
    phase_values = (2*np.pi*Fc/Fs)*time_indexes
    sig = Amp*np.cos(phase_values)
    return Fs, time_values, sig 
    
def create_complex_exponent(Fc=1e3, Fs=20e3, Amp=1, N=2e1):
    time_indexes = np.arange(N)
    time_values = time_indexes/Fs
    phase_values = (2*np.pi*Fc/Fs)*time_indexes
    sig_real_part = Amp*np.cos(phase_values)
    sig_imag_part = Amp*np.sin(phase_values)
    sig_complex = sig_real_part + 1j*sig_imag_part
    return sig_complex     

def create_from_wav(file_name, N=float('inf')):
    Fs, sig = read_wav(file_name)
    N = min(N, len(sig))
    if len(sig.shape) > 1:
        sig = sig[0:int(N),0]     # Selecting one audio channel
    else:
        sig = sig[0:int(N)]
    time_indexes = np.arange(N)
    time_values = time_indexes/Fs
    return Fs, time_values, sig
     