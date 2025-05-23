import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, welch
from scipy.io.wavfile import write

# --- Parametry ---
fs = 3.2e6          # Częstotliwość próbkowania
N = int(32e6)       # Liczba próbek IQ
fc = 0.5e6          # Przesunięcie częstotliwości nośnej
bwSERV = 80e3       # Pasmo jednej stacji
bwAUDIO = 16e3      # Pasmo audio

# --- Wczytanie danych ---
with open('samples_100MHz_fs3200kHz.raw', 'rb') as f:
    s = np.frombuffer(f.read(2 * N), dtype=np.uint8)

s = s.astype(np.float32) - 127.0
wideband_signal = s[0::2] + 1j * s[1::2]
del s

# --- Przesunięcie stacji do pasma podstawowego ---
n = np.arange(N)
wideband_signal_shifted = wideband_signal * np.exp(-1j * 2 * np.pi * fc / fs * n)

# filtracja
def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    return butter(order, norm_cutoff, btype='low')

# Wybór stacji do odsłuchu
def extract_station(signal, station_freq, fs, bw):
    # Przesunięcie stacji do pasma podstawowego
    n = np.arange(len(signal))
    shifted_signal = signal * np.exp(-1j * 2 * np.pi * station_freq / fs * n)

    # Filtracja
    b, a = butter_lowpass(bw, fs)
    filtered_signal = lfilter(b, a, shifted_signal)

    # Zmniejszenie częstotliwości próbkowania
    decimated_signal = filtered_signal[::int(fs / bw)]  # zmiana próbkowania na pasmo stacji

    return decimated_signal

# Stacja
station_freq = 97e6
station_signal = extract_station(wideband_signal_shifted, station_freq, fs, bwSERV)

# Demodulacja FM
dx = station_signal[1:] * np.conj(station_signal[:-1])
y = np.arctan2(np.imag(dx), np.real(dx))

# Filtracja audio
b_aa, a_aa = butter_lowpass(bwAUDIO, fs)
y_filtered = lfilter(b_aa, a_aa, y)

# Próbkowanie audio
ym = y_filtered[::int(bwSERV / bwAUDIO)]  # Zmiana próbkowania na pasmo audio

# Normalizacja
ym = ym - np.mean(ym)
ym = ym / (1.001 * np.max(np.abs(ym)))

# Zapis do pliku wav
write("output_fm.wav", int(bwAUDIO), ym.astype(np.float32))
print("Zapisano plik 'output_fm.wav'")

# --- Funkcja do rysowania ---
def plot_time_and_psd(signal, fs, title):
    plt.figure(figsize=(12, 4))
    t = np.arange(len(signal)) / fs

    plt.subplot(1, 2, 1)
    plt.plot(t, signal)
    plt.title(f'{title} - przebieg czasowy')
    plt.xlabel("Czas [s]")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    f, Pxx = welch(signal, fs=fs, window='hamming', nperseg=1024)
    plt.semilogy(f, Pxx)
    plt.title(f'{title} - widmo (Welch)')
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Gęstość mocy [dB/Hz]")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# --- Wykres końcowego sygnału audio ---
plot_time_and_psd(ym, bwAUDIO, "Sygnał audio (po filtracji i dekymacji)")
