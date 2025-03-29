import numpy as np

def fft_rec(x):
    N = len(x)
    if N <= 1:
        return x

    # podział sygnału
    x_even = fft_rec(x[0:N//2])
    x_odd = fft_rec(x[N//2:])

    twiddle_factors = np.exp(-2j * np.pi * np.arange(N) / N)

    X = np.zeros(N, dtype=complex)
    X[:N // 2] = x_even + twiddle_factors[:N // 2] * x_odd
    X[N // 2:] = x_even + twiddle_factors[N // 2:] * x_odd

    return X


N = 256
x = np.random.randn(N,1) + 1j*np.random.randn(N,1)
print(x)
X1 = np.fft.fft(x)
X2 = fft_rec(x)

# Porównanie wyników (średni błąd)
error = np.mean(np.abs(X1 - X2))
print(f"Implementacja a np.fft: {error:.2e}")