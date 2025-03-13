import numpy as np
import scipy.io
from matplotlib import pyplot as plt
from scipy.signal import find_peaks


def mycorrelation(x, y):
    X = len(x)
    Y = len(y)
    result_length = X + Y - 1
    r_xy = np.zeros(result_length)
    i=0
    for m in range(-(X - 1), Y):
        # Ustalenie indeksów, dla których oba sygnały są zdefiniowane
        n_start = max(0, -m)  # Początek dopasowania sygnałów
        n_end = min(X, Y - m)  # Koniec dopasowania sygnałów

        # Sumujemy iloczyny dla przesunięcia m
        for n in range(n_start, n_end-1):
            r_xy[i] += x[n] * y[n + m]  # Suma iloczynów sygnałów
        i+=1
    return r_xy

def mycorrelation1(x, y):

    # Zamiana, jeśli x jest krótszy niż y
    if len(x) < len(y):
        x, y = y, x

    n = len(x)
    m = len(y)
    result = []

    # Przesuwamy wektor y od początku wektora x do momentu, gdy y mieści się w x
    for i in range(n - m + 1):
        suma = 0
        # Dla każdego przesunięcia obliczamy sumę iloczynów odpowiadających elementów
        for j in range(m):
            suma += x[i + j] * y[j]
        result.append(suma)

    return result

def mycorrelation2(x, y):
    len_x = len(x)
    len_y = len(y)
    correlation = np.zeros(len_x + len_y - 1)

    for k in range(len_x + len_y - 1):
        sum_val = 0
        for l in range(max(0, k + 1 - len_y), min(k + 1, len_x)):
            sum_val += x[l] * y[k - l]
        correlation[k] = sum_val

    return correlation

# Wczytanie pliku .mat
mat = scipy.io.loadmat("adsl_x.mat") # wczytanie plików danych z matlab
x = mat["x"].flatten()  # pobranie danych zmiennej x z pliku .mat, i konwersja na jednowymierową macierz
# same dante mat["x"] to tablica tablic
M = 32   # prefix
N = 512  # ramka
K=4


bestPrefix = list()
bestScore = list()
prefixPoz = list()
y = 0

# Dla gotowej funkcji
for i in range(len(x)):
    # iterowanie od 0
    prefix = x[i:i + M]
    correlation = np.correlate(x, prefix, 'full')
    y = max(correlation)
    z = np.where(correlation == y)[0]
    if len(z) >= 2:
        bestPrefix.append(prefix)
        bestScore.append(correlation)
        prefixPoz.append(i)

for i in range(len(bestScore)):
    plt.plot(bestScore[i])
    plt.show()
print(bestPrefix)
print(y)
print(prefixPoz)

# Dla gotowej funkcji
for i in range(len(x)):
    # iterowanie od 0
    prefix = x[i:i + M]
    correlation = correlation(x, prefix)
    y = max(correlation)
    z = np.where(correlation == y)[0]
    if len(z) >= 2:
        bestPrefix.append(prefix)
        bestScore.append(correlation)
        prefixPoz.append(i)

for i in range(len(bestScore)):
    plt.plot(bestScore[i])
    plt.show()
print(bestPrefix)
print(y)
print(prefixPoz)