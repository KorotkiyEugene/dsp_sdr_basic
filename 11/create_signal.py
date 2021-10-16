import numpy as np
import matplotlib.pyplot as plt

Fs = 100     # Hz
Ts = 1/Fs

F1 = 1      # Hz

NUM_POINTS = 1e3
PHASE_OFFSET = 0
#PHASE_OFFSET = -np.pi/2

# Time vector
idx = np.arange(NUM_POINTS)
t = idx*Ts

x = np.cos(2*np.pi*F1*t + PHASE_OFFSET)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, x, '-', color='C1')
plt.xlabel('Time values (sec)')
plt.grid(True)

#print("Time vals: %d", t)

plt.subplot(2, 1, 2)
plt.plot(x, '-', color='C2')
plt.xlabel('Index values')
plt.grid(True)

#print("Index vals: %d", idx.astype(int))

plt.show()