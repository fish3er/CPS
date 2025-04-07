import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
# Częstotliwości w Hz
f0 = 96e6                    # środkowa częstotliwość (96 MHz)
bw = 2e5                   # szerokość pasma (±100 kHz)
w0 = 2 * np.pi * f0          # częst. kątowa środkowa
bw_rad = 2 * np.pi * bw      # szerokość pasma w rad/s

p1 = -2e5 + 1j * w0
p2 = -2e5 - 1j * w0
p3 = -1.7e5 + 1j * (w0 + 1e5)
p4 = -1.7e5 - 1j * (w0 + 1e5)
p5 = -1.7e5 + 1j * (w0 - 1e5)
p6 = -1.7e5 - 1j * (w0 - 1e5)
z1 = 1j * (w0 + 0.7e6)
z2 = -1j * (w0 + 0.7e6)
z3 = 1j * (w0 - 0.7e6)
z4 = -1j * (w0 - 0.7e6)
zeros = [z1, z2, z3, z4]
poles = [p1, p2, p3, p4, p5, p6]

b = np.poly(zeros)
a = np.poly(poles)

# odopowiedź
k=1e13  # wzmocnienie
H = sig.TransferFunction( k * b, a)
f = np.linspace(95e6, 97e6, 10000)
w = 2* np.pi * f# Zakres częstotliwości
w, h = sig.freqresp(H, w)

plt.figure(figsize=(10, 5))
plt.plot(f / 1e6, 20 * np.log10(np.abs(h)), label='|H(f)| [dB]')
plt.axvline((f0 - 1e5) / 1e6, color='green', linestyle='--', label='Pasmo przepustowe')
plt.axvline((f0 + 1e5) / 1e6, color='green', linestyle='--')
plt.axhline(-3, color='red', linestyle='--', label='-3 dB granica')
plt.axhline(-40, color='orange', linestyle='--', label='Tłumienie -40 dB')
plt.title('Ręcznie zbudowany analogowy filtr pasmowo-przepustowy')
plt.xlabel('Częstotliwość [MHz]')
plt.ylabel('Wzmocnienie [dB]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

