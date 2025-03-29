import numpy as np
from matplotlib import pyplot as plt

fpr=1000
N=1000
t=np.linspace(0,0.1,N,endpoint=False)

f0=200
ampl=100
sig=ampl*np.sin(2*np.pi*f0*t)

plt.figure()
plt.plot(t, sig, 'bo-')
plt.xlabel('t [s]')
plt.title('x(t)')
plt.grid(True)
plt.show()

sig_fft = np.fft.fft(sig)
f = fpr/N*np.arange(N)

plt.figure()
plt.plot(f, 1 / N * np.abs(sig_fft), 'bo-') # normalizacja
plt.xlabel('f [Hz]')
plt.title('|X(k)|')
plt.grid(True)
plt.pause(0.1)
plt.show()

# pierwsz połowa
k = np.linspace(1, N//2, N//2, dtype=int, endpoint=False)

# Skala normalizowana (moduł)
plt.figure()
plt.plot(f[k], 2 / N * np.abs(sig_fft[k]), 'bo-')  # Skala 2/N
plt.xlabel('f [Hz]')
plt.title('Pierwsza połowa widma FFT')
plt.grid(True)
plt.show()

sig_log = 20 * np.log10(2 / N * np.abs(sig_fft[k]))
plt.figure()
plt.plot(f[k], sig_log, 'bo-')  # Skala 2/N
plt.xlabel('f [Hz]')
plt.title('Pierwsza połowa widma FFT')
plt.grid(True)
plt.show()
