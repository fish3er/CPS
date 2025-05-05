import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
from scipy.fft import fft

# Wczytywanie pliku .mat
data = scipy.io.loadmat("lab08_am.mat")

# Wybieranie sygnału (przykład: s4)
x = data['s7'].squeeze()

# Parametry
Fs = 1e3             # częstotliwość próbkowania
M = 50               # połowa rzędu filtru
N = 2 * M + 1        # rząd filtru
n = np.arange(-M, M + 1)

# Ręczna definicja filtru Hilberta z oknem (raised cosine window)
h = (1 - np.cos(np.pi * n)) / (np.pi * n)
h[M] = 0  # nadpisanie wartości w n=0

# Konwolucja (pełna)
xh_full = np.convolve(x, h, mode='full')

# Synchronizacja wejścia i wyjścia filtra
Nx = len(x)
x_sync = x[M:Nx - M]                       # ucięcie brzegów
xh_sync = xh_full[2 * M : 2 * M + len(x_sync)]  # wyrównanie opóźnienia

# Sygnał analityczny i obwiednia
z = x_sync + 1j * xh_sync
m = np.abs(z)

# Wykresy
plt.figure()
plt.plot(x, label='x', color='b')
plt.plot(xh_full, label='HT(x)', color='k')
plt.title("Sygnał przed i po Filtrze Hilberta")
plt.xlabel("Numer próbki")
plt.ylabel("Amplituda")
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(x_sync, label='x', color='b')
plt.plot(xh_sync, label='HT(x)', color='k')
plt.plot(m, label='amp', color='r', linewidth=1)
plt.title("Sygnał zsynchronizowany oraz obwiednia AM")
plt.xlabel("Numer próbki")
plt.ylabel("Amplituda")
plt.legend()
plt.grid(True)

# Analiza widmowa
M_f = np.abs(fft(m))
norM = M_f / np.max(M_f)
f = np.arange(len(norM)) * (Fs / len(norM))

plt.figure()
plt.plot(f, norM)
plt.xlim(0, 100)
plt.title("Widmo obwiedni")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)

plt.show()
