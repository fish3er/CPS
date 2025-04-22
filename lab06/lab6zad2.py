import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

# wczytywanie
fs, s = wavfile.read('s7.wav')  # Zmień nazwę pliku na odpowiednią, np. s0.wav, s1.wav itd.
s = s.astype(np.float32)

# spktrogram
f, t, Sxx = spectrogram(s, fs, nperseg=4096, noverlap=4096-512)

# Rysowanie spektrogramu
plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title('Spektrogram sygnału DTMF')
plt.ylabel('Częstotliwość [Hz]')
plt.xlabel('Czas [s]')
plt.ylim([500, 1600])  # ograniczamy do pasma DTMF
plt.colorbar(label='Amplituda (dB)')
plt.grid()
plt.show()
