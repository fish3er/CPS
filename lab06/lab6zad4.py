import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter, freqz, spectrogram, tf2zpk
from numpy.fft import fft, fftfreq

def plot_fft(signal, fs, title="FFT"):
    N = len(signal)
    freqs = fftfreq(N, 1/fs)
    fft_vals = np.abs(fft(signal))
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:N // 2], 20 * np.log10(fft_vals[:N // 2] + 1e-10))
    plt.title(title)
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda [dB]")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_spectrogram(signal, fs, title="Spektrogram"):
    f, t, Sxx = spectrogram(signal, fs=fs, nperseg=1024, noverlap=768)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 20 * np.log10(Sxx + 1e-10), shading='gouraud')
    plt.title(title)
    plt.xlabel("Czas [s]")
    plt.ylabel("Częstotliwość [Hz]")
    plt.colorbar(label="Amplituda [dB]")
    plt.tight_layout()
    plt.show()

def design_lowpass_filter(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    return b, a

def plot_filter_response(b, a, fs):
    w, h = freqz(b, a, worN=8000)
    plt.figure(figsize=(10, 4))
    plt.plot(fs * 0.5 * w / np.pi, 20 * np.log10(np.abs(h) + 1e-10))
    plt.title('Charakterystyka amplitudowa filtru [dB]')
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Wzmocnienie [dB]')
    plt.grid()
    plt.tight_layout()
    plt.show()

    z, p, _ = tf2zpk(b, a)
    plt.figure(figsize=(5, 5))
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Zera')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Bieguny')
    plt.axhline(0, color='gray')
    plt.axvline(0, color='gray')
    plt.title('Zera i bieguny na płaszczyźnie zespolonej')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# === Wczytywanie plików ===

fs1, engine = wavfile.read("engine.wav")
fs2, sing = wavfile.read("sing.WAV")

print(fs1)
print(fs2)

assert fs1 == fs2, "Częstotliwości próbkowania muszą być identyczne!"
fs = fs1

# Mono i wyrównanie długości
engine = engine if engine.ndim == 1 else engine[:, 0] #ewentuialne stereo do mono
sing = sing if sing.ndim == 1 else sing[:, 0]
min_len = min(len(engine), len(sing)) # wyrównanie długości
engine = engine[:min_len] #obcięcie
sing = sing[:min_len]

# Normalizacja ampl
engine = engine / np.max(np.abs(engine))
sing = sing / np.max(np.abs(sing))

# sumowany sygnał
summed = engine + sing
summed = summed / np.max(np.abs(summed)) #znowu normalizacja

# widma
plot_fft(engine, fs, "FFT - Silnik")
plot_spectrogram(engine, fs, "Spektrogram - Silnik")

plot_fft(sing, fs, "FFT - Śpiew")
plot_spectrogram(sing, fs, "Spektrogram - Śpiew")

plot_fft(summed, fs, "FFT - Sygnał zsumowany")
plot_spectrogram(summed, fs, "Spektrogram - Sygnał zsumowany")

#filtr IIR
cutoff = 500  # Odcinamy śpiew
b, a = design_lowpass_filter(cutoff, fs, order=4)
plot_filter_response(b, a, fs)

# filtracja
filtered = lfilter(b, a, summed)

#fft plus spektrogram
plot_fft(filtered, fs, "FFT - Po filtrze")
plot_spectrogram(filtered, fs, "Spektrogram - Po filtrze")

# zapis do odczytu
from scipy.io.wavfile import write
write("f_output.wav", fs, (filtered * 32767).astype(np.int16))
print("Zapisano plik: filtered_output.wav")
