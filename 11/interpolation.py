import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, firwin

Fs = 100     # Hz
Ts = 1/Fs

F1 = 1       # Hz

NUM_POINTS = 0.2e3

NFIR = 101
INTERP_ORDER = 10

# Create Signal

t = np.arange(NUM_POINTS)*Ts

sig = np.cos(2*np.pi*F1*t)

# Interpolate

sig_with_zeros = np.zeros(int(NUM_POINTS*INTERP_ORDER))
sig_with_zeros[::INTERP_ORDER] = sig

print(sig)
print(sig_with_zeros)


interp_fir_taps = firwin(NFIR, 1/INTERP_ORDER)

interp_sig = lfilter(interp_fir_taps, 1.0, sig_with_zeros)

interp_sig = INTERP_ORDER*interp_sig;

# Plot results

plt.figure()
plt.title('Signal')
plt.plot(interp_sig[int(NFIR/2):], '-o', color='C1')
plt.stem(sig_with_zeros, linefmt='C2', basefmt='C0')

plt.xlabel('Indexes')
plt.grid(True)

plt.show()