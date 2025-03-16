import numpy as np
import matplotlib.pyplot as plt

N = 100
fs = 1000
f = [50, 100, 150]
ampl = [50, 100, 150]

def generate_signal(numb, fnumb, frq, amp): # numb - ilość próbek ; fnumb - czest próbkowania ; freq - czest syg; amp - ampl
    t = np.arange(numb) / fnumb
    sig = sum(amp * np.sin(2 * np.pi * frq * t))
    return sig

A = np.zeros((N, N))
for k in range(N):
    for n in range(N):
        scale = np.sqrt(1/N) if k == 0 else np.sqrt(2/N)
        A[k, n] = scale * np.cos((np.pi * k * (n + 0.5)) / N)
S = np.linalg.inv(A)

for j in range(len(ampl)):
    generate_signal(N, fs, f[j], ampl[j])
    for i in range(N):
        plt.figure()
        plt.plot(A[i, :], label=f'Wiersz {i} macierzy A')
        plt.plot(S[:, i], label=f'Kolumna {i} macierzy S', linestyle='dashed')
        plt.legend()
        plt.title(f'Wiersz {i} macierzy A i kolumna {i} macierzy S')
        plt.show()
        input("Naciśnij Enter, aby kontynuować...")