import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import hilbert, resample_poly

# Parametry sygnału
fs = 400e3           # Częstotliwość próbkowania sygnału radiowego [Hz]
fc1 = 100e3          # Częstotliwość nośna pierwszej stacji [Hz]
fc2 = 110e3          # Częstotliwość nośna drugiej stacji [Hz]
dA = 0.25            # Głębokość modulacji

# Wczytanie sygnałów mowy
x1, fsx = sf.read('mowa8000.wav')
x2 = np.flipud(x1)

# Normalizacja
x1 = x1 / np.max(np.abs(x1)) * dA
x2 = x2 / np.max(np.abs(x2)) * dA

# Nadpróbkowanie
upsample_factor = int(fs / fsx)
x1_up = resample_poly(x1, upsample_factor, 1)
x2_up = resample_poly(x2, upsample_factor, 1)

# Dopasowanie długości
N = min(len(x1_up), len(x2_up))
x1_up = x1_up[:N]
x2_up = x2_up[:N]
t = np.arange(N) / fs

# Własna implementacja filtra Hilberta (ręczna aproksymacja)
M = 100
n = np.arange(-M, M+1)
h = np.where(n != 0, (1 - np.cos(np.pi * n)) / (np.pi * n), 0)

# Filtracja Hilberta
x1h = np.convolve(x1_up, h, mode='same')
x2h = np.convolve(x2_up, h, mode='same')

# Modulacja

# 1. DSB-C
y_DSB_C = (1 + x1_up) * np.cos(2*np.pi*fc1*t) + (1 + x2_up) * np.cos(2*np.pi*fc2*t)

# 2. DSB-SC
y_DSB_SC = x1_up * np.cos(2*np.pi*fc1*t) + x2_up * np.cos(2*np.pi*fc2*t)

# 3. SSB-SC
y_SSB_SC = 0.5 * x1_up * np.cos(2*np.pi*fc1*t) - 0.5 * x1h * np.sin(2*np.pi*fc1*t) + \
           0.5 * x2_up * np.cos(2*np.pi*fc2*t) + 0.5 * x2h * np.sin(2*np.pi*fc2*t)

# Funkcja do wykresu widma
def plot_spectrum(signal, fs, title):
    N = len(signal)
    f = np.linspace(0, fs, N, endpoint=False)
    spectrum = np.abs(np.fft.fft(signal)) / N
    plt.plot(f[:N//2], spectrum[:N//2])
    plt.title(title)
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.grid()

# Wykresy
plt.figure(figsize=(12, 10))

# DSB-C
plt.subplot(3, 2, 1)
plt.plot(t[:1000], y_DSB_C[:1000])
plt.title("DSB-C w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

plt.subplot(3, 2, 2)
plot_spectrum(y_DSB_C, fs, "Widmo DSB-C")

# DSB-SC
plt.subplot(3, 2, 3)
plt.plot(t[:1000], y_DSB_SC[:1000])
plt.title("DSB-SC w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

plt.subplot(3, 2, 4)
plot_spectrum(y_DSB_SC, fs, "Widmo DSB-SC")

# SSB-SC
plt.subplot(3, 2, 5)
plt.plot(t[:1000], y_SSB_SC[:1000])
plt.title("SSB-SC w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

plt.subplot(3, 2, 6)
plot_spectrum(y_SSB_SC, fs, "Widmo SSB-SC")

plt.tight_layout()
plt.show()
