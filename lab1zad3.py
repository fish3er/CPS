import numpy as np
import scipy.io
from scipy.signal import find_peaks


def mycorrelation(x,y):
    X = len(x)
    Y = len(y)
    result_length = X + Y - 1
    r_xy = np.zeros(result_length)
    i=0#  0 do X + Y -2
    for m in range(-(X - 1), Y): # pętla po wektorze "wynikowym"
        # Ustalenie indeksów, dla których oba sygnały są zdefiniowane,
        n_start = max(0, -m) # początek dopasowanie sygnałów
        n_end = min(X, M - m) # koniec dopasowanie sygnałow
        # Sumujemy iloczyny dla przesunięcia m
        for n in range(n_start, n_end): # pętrla po elementach dopasowania
            r_xy[i] += x[n] * y[n + m] # suma wpisana  w podpowiedzni elemeny wynikowego wektora
        i+=1

    return r_xy

# Wczytanie pliku .mat
mat = scipy.io.loadmat("adsl_x.mat") # wczytanie plików danych z matlab
x = mat["x"].flatten()  # pobranie danych zmiennej x z pliku .mat, i konwersja na jednowymierową macierz
# same dante mat["x"] to tablica tablic
M = 32   # prefix
N = 512  # ramka
K = 4    # ilosc blokow

for i in range(K): # ilość ramek
    prefix = x[(i+1)*N - M:(i+1)*N]
    correlation = np.correlate(x, prefix, 'full')
    pocz_pref = find_peaks(correlation, np.max(correlation))
    pocz_pref_x = pocz_pref[0] - M +1 #numeracja do 1 do 2049
    print(pocz_pref_x)