import numpy as np
import scipy.io
from matplotlib import pyplot as plt
# Wczytanie pliku .mat
mat = scipy.io.loadmat("lab_03.mat") # wczytanie plików danych z matlab
x = mat["x_14"].flatten()  # pobranie danych zmiennej x z pliku .mat, i konwersja na jednowymierową macierz
# same dante mat["x"] to tablica tablic
M = 32   # prefix
N = 512  # ramka
K=8
fs=1 # próbkowanie
for i in range(K):
    # 0 - 31 Pref
    # 32 - 544 Dane
    DFT = np.zeros((N, N), dtype=np.complex128)
    for j in range(N):
        for l in range(N):
            DFT[j, l] = np.exp(-2j * np.pi * j * l / N) / np.sqrt(N)

    X = DFT @ x[i * M:i * M + N]  # DFT
    freq=np.arange(N)*fs/N # spektrum cześtotliwości 0 - 512 Hz ??
    plt.plot(freq,np.real(X))
    plt.show()
    #domin czesttliwosci ???????
    harmonic = freq[np.real(X)> 0.9*np.max(np.real(X))]
    print(harmonic)


