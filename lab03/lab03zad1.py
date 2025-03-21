import numpy as np
import matplotlib.pyplot as plt

N=100 # ilosć próbek
A1=100
A2=200
fs=1000
f1=100
f2=200
phi1= np.pi/7
phi2=-np.pi/11

t = np.linspace(0,N/fs,N,endpoint=False)  # wektor czasowy
x = A1 * np.cos(2 * np.pi * f1 * t + phi1) + A2 * np.cos(2 * np.pi * f2 * t + phi2)  # sygnał
plt.plot(t, x)
plt.show()
# A macierz DFT - dyskretnej transformaty Fouriera dla sygnału próbkowanego -> dyskretnego
A = np.zeros((N, N))
for k in range(N):
    for n in range(N):
        A[k, n] = np.exp(-2j*np.pi*k*n/N) / np.sqrt(N)
X = A @ x    # DFT
# signal
freq = np.arange(N) * fs / N
plt.stem(freq, np.real(X))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('Część rzeczywista DFT')
plt.show()

plt.stem(freq, np.imag(X))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część urojona')
plt.title('Część urojona DFT')
plt.show()

plt.stem(freq, np.abs(X))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Magnituda')
plt.title('Moduł DFT')
plt.show()

plt.stem(freq, np.angle(X))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Faza [rad]')
plt.title('Faza DFT')
plt.show()

#rekonstrukcja sygnału
# maciesz
B= A.conj().T
x_rec = B @ X

print("Czy x_rec == x?", np.allclose(x_rec, x))

# Zastosowanie FFT i IFFT
X_fft = np.fft.fft(x)
xr_ifft = np.fft.ifft(X_fft)

# Porównanie wyników FFT i IFFT
print("Czy xr_ifft == x?", np.allclose(xr_ifft, x))

# Różnice między DFT a FFT
diff = np.abs(X - X_fft)
print("Maksymalna różnica między DFT a FFT:", np.max(diff))
