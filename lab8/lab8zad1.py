import numpy as np
import scipy.io as sio
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parametry
fs = 1000  # Hz
fc = 200  # Hz
t = np.arange(0, 1, 1 / fs)

# dane
mat = sio.loadmat('lab08_am.mat')  # zamień na odpowiedni numer sygnału, np. lab08_am.mat['x8']
x = mat['s7'].flatten()  # Zakładam, że wybierasz 8. realizację (przedostatnia cyfra legitymacji = 8)

# Zaprojektuj filtr Hilberta FIR (przesuwa fazę o -π/2)
numtaps = 129  # musi być nieparzysta liczba
hilbert_fir = signal.remez(numtaps, [0.05, 0.95], [1], type='hilbert', fs=fs)

# Przesunięcie fazowe sygnału x
x_q = signal.lfilter(hilbert_fir, 1.0, x)

# Obwiednia: sqrt(x^2 + x_q^2)
envelope = np.sqrt(x**2 + x_q**2)

# Wykres
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='x')
plt.plot(t, envelope, label='Obwiednia', color='red')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.legend()
plt.grid(True)
plt.title('Sygnał x i jego obwiednia')
plt.show()

# Analiza częstotliwościowa obwiedni
f, Pxx = signal.periodogram(envelope, fs)
plt.figure()
plt.semilogy(f, Pxx)
plt.title('Widmo obwiedni')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Widmowa gęstość mocy')
plt.grid()
plt.show()

# Znalezienie częstotliwości i amplitud (pomijając DC = 0 Hz)
peaks, _ = signal.find_peaks(Pxx, height=0.001)
dominant_freqs = f[peaks]
dominant_amps = np.sqrt(Pxx[peaks])

# wybranie 3 największych czestotliwosci
sorted_indices = np.argsort(dominant_amps)[-3:]  # Największe amplitudy
frequencies = dominant_freqs[sorted_indices]
amplitudes = dominant_amps[sorted_indices]

f1, f2, f3 = frequencies
A1, A2, A3 = amplitudes

print(f"f1 = {f1:.2f} Hz, A1 = {A1:.2f}")
print(f"f2 = {f2:.2f} Hz, A2 = {A2:.2f}")
print(f"f3 = {f3:.2f} Hz, A3 = {A3:.2f}")
