import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# --- Parametry ---
fs_audio, x = wav.read("mowa8000.wav")  # sygnał audio
x = x / np.max(np.abs(x))  # normalizacja
x_rev = x[::-1]  # wersja odwrócona

fs = 400_000  # sygnał radiowy
fc1 = 100_000  # nośna stacji 1
fc2 = 110_000  # nośna stacji 2
d = 0.25       # głębokość modulacji

# --- Nadpróbkowanie ---
up_factor = fs // fs_audio
x_up = signal.resample_poly(x, up_factor, 1)
x_rev_up = signal.resample_poly(x_rev, up_factor, 1)
t = np.arange(len(x_up)) / fs

# --- DSB-C ---
carrier1 = np.cos(2 * np.pi * fc1 * t)
carrier2 = np.cos(2 * np.pi * fc2 * t)
y_dsb_c = (1 + d * x_up) * carrier1 + (1 + d * x_rev_up) * carrier2

# --- DSB-SC ---
y_dsb_sc = d * x_up * carrier1 + d * x_rev_up * carrier2

# --- Filtr Hilberta FIR ---
numtaps = 63  # krótszy, stabilniejszy
# cutoff = [0.01, 0.99]  # jako ułamki Nyquista (0–1)
hilbert_fir = signal.firwin(numtaps, cutoff=0.99, pass_zero=False, window="hamming")
x_hilb = signal.lfilter(hilbert_fir, 1.0, x_up)
x_rev_hilb = signal.lfilter(hilbert_fir, 1.0, x_rev_up)
x_analytic = x_up + 1j * x_hilb
x_rev_analytic = x_rev_up + 1j * x_rev_hilb

# --- SSB-SC ---
y_ssb_sc_upper = np.real(x_analytic * np.exp(1j * 2 * np.pi * fc1 * t))  # prawa strona
y_ssb_sc_lower = np.real(x_rev_analytic * np.exp(1j * 2 * np.pi * fc2 * t))  # lewa strona
y_ssb = y_ssb_sc_upper + y_ssb_sc_lower

# --- Wykresy: sygnał audio i po modulacji ---
def plot_fft(signal, fs, title):
    N = len(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    spectrum = np.fft.fft(signal)
    plt.plot(freqs[:N//2], 20*np.log10(np.abs(spectrum[:N//2])+1e-10))
    plt.title(title)
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda [dB]")
    plt.grid(True)

plt.figure(figsize=(14, 10))

# --- Wejściowy sygnał audio (po upsamplingu) ---
plt.subplot(3, 2, 1)
plt.plot(t[:1000], x_up[:1000])
plt.title("x(t) po nadpróbkowaniu")
plt.xlabel("Czas [s]")
plt.grid(True)

plt.subplot(3, 2, 2)
plot_fft(x_up, fs, "Widmo sygnału audio x(t)")

# --- DSB-C ---
plt.subplot(3, 2, 3)
plt.plot(t[:1000], y_dsb_c[:1000])
plt.title("DSB-C – sygnał w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.grid(True)

plt.subplot(3, 2, 4)
plot_fft(y_dsb_c, fs, "DSB-C – widmo")

# --- SSB-SC ---
plt.subplot(3, 2, 5)
plt.plot(t[:1000], y_ssb[:1000])
plt.title("SSB-SC – sygnał w dziedzinie czasu")
plt.xlabel("Czas [s]")
plt.grid(True)

plt.subplot(3, 2, 6)
plot_fft(y_ssb, fs, "SSB-SC – widmo")

plt.tight_layout()
plt.show()

