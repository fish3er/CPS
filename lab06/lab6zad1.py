import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# === Dane z butter.mat ===
k = 3.989876368752743e+09
p = np.array([
    -48.8244160718102 + 7712.164758116531j,
    -48.8244160718102 - 7712.164758116531j,
    -116.833266045137 + 7642.68591280863j,
    -116.833266045137 - 7642.68591280863j,
    -47.3544207096850 + 7479.968505945371j,
    -47.3544207096850 - 7479.968505945371j,
    -115.362986120200 + 7546.50707602731j,
    -115.362986120200 - 7546.50707602731j
])
z = np.array([0, 0, 0, 0])

# === Parametry ===
fs = 16000  # Hz
t = np.arange(0, 1, 1/fs)  # 1 sekunda

# === Z -> H(s) -> H(z)
b_analog, a_analog = signal.zpk2tf(z, p, k) # analog
b_digital, a_digital = signal.bilinear(b_analog, a_analog, fs) # digital
#metoda bilinearnej transformacji (metoda Tustina)

# chrakterystyka
w_analog, h_analog = signal.freqs(b_analog, a_analog, worN=1024)
w_digital, h_digital = signal.freqz(b_digital, a_digital, worN=1024, fs=fs)

plt.figure(figsize=(12, 5))
plt.plot(w_analog / (2 * np.pi), 20 * np.log10(np.abs(h_analog)), label='Analogowy')
plt.plot(w_digital, 20 * np.log10(np.abs(h_digital)), label='Cyfrowy')
plt.axvline(1189, color='gray', linestyle='--', label='f_low = 1189 Hz')
plt.axvline(1229, color='gray', linestyle='--', label='f_high = 1229 Hz')
plt.title("Charakterystyka amplitudowa filtra")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.legend()
plt.grid()
plt.tight_layout()

# suma dwóch sinusów
f1, f2 = 1209, 1272
x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# filtr ale ręcznie
def custom_filter(b, a, x):
    y = np.zeros_like(x)
    for n in range(len(x)):
        for i in range(len(b)):
            if n - i >= 0:
                y[n] += b[i] * x[n - i]
        for j in range(1, len(a)):
            if n - j >= 0:
                y[n] -= a[j] * y[n - j]
        y[n] /= a[0]
    return y

y_custom = custom_filter(b_digital, a_digital, x)
y_lib = signal.lfilter(b_digital, a_digital, x)

#sygnały w dziedzinie czasu ( dwa się nakładają)
plt.figure(figsize=(12, 5))
plt.plot(t, x, label='Sygnał oryginalny', alpha=0.5)
plt.plot(t, y_custom, label='Filtracja własna', linewidth=1)
plt.plot(t, y_lib, label='Filtracja lfilter', linestyle='dashed')
plt.title("Sygnały w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.legend()
plt.grid()
plt.tight_layout()

#porównanie + fukcja do rysowania
def plot_fft(sig, fs, label):
    f = np.fft.rfftfreq(len(sig), 1/fs)
    mag = np.abs(np.fft.rfft(sig))
    plt.plot(f, 20 * np.log10(mag), label=label)

plt.figure(figsize=(12, 5))
plot_fft(x, fs, "Oryginalny")
plot_fft(y_custom, fs, "Po filtracji (własna)")
plot_fft(y_lib, fs, "Po filtracji (lfilter)")
plt.title("Widmo sygnałów (FFT)")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.legend()
plt.grid()
plt.tight_layout()

plt.show()
