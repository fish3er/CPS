import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import buttord, butter, cheby2, cheby1, ellip, freqresp

f_pass = 64e3      # Hz
f_stop = 128e3     # Hz
A_pass = 3         # dB
A_stop = 40        # dB
# zminana na kątowe
wpass = 2 * np.pi * f_pass
wstop = 2 * np.pi * f_stop
# N=20
filters = {}

# Butterworth
N, Wn = buttord(wpass, wstop, A_pass, A_stop, analog=True)

b, a = butter(N, Wn, btype='low', analog=True)
filters['Butterworth'] = (b, a)

# Chebyshev I
N, Wn = cheby1(N=10, rp=A_pass, Wn=wpass, btype='low', analog=True, output='ba')

filters['Chebyshev I'] = (N, Wn)

# Chebyshev II
N, Wn = cheby2(N=10, rs=A_stop, Wn=wstop, btype='low', analog=True, output='ba')

filters['Chebyshev II'] = (N, Wn)

# Elliptyczny
N, Wn = ellip(N=10, rp=A_pass, rs=A_stop, Wn=wpass, btype='low', analog=True, output='ba')
filters['Elliptic'] = (N, Wn)

# Rysowanie charakterystyk częstotliwościowych
w = np.logspace(3, 6, 1000)  # od 1 kHz do 1 MHz
fig, ax = plt.subplots()
for name, (b, a) in filters.items():
    w_, h = freqresp((b, a), w)
    ax.semilogx(w / (2 * np.pi), 20 * np.log10(np.abs(h)), label=name)

ax.set_title("Charakterystyki filtrów analogowych")
ax.set_xlabel("Częstotliwość [Hz]")
ax.set_ylabel("Wzmocnienie [dB]")
ax.axvline(f_pass, color='gray', linestyle='--', label='f_pass')
ax.axvline(f_stop, color='red', linestyle='--', label='f_stop')
ax.grid(True, which='both')
ax.legend()
plt.show()