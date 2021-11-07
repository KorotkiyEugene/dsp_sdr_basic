import numpy as np
import matplotlib.pyplot as plt
from common import create_harmonic, create_from_wav

### Program starts here

Fs, t, sig = create_harmonic()

#Fs, t, sig = create_from_wav('audio.wav', 1000)

#print(t)
#print(sig)

plt.figure()    
plt.plot(sig, '-o', color='C2')
plt.xlabel('Signal sample time index')
plt.ylabel('Signal sample value')

plt.figure()
plt.plot(t, sig, '-o', color='C3')    
plt.xlabel('Signal sample time value')
plt.ylabel('Signal sample value')

plt.show() 
