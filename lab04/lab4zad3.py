import time

import numpy as np

N=1024
x_r = np.random.normal(size=N)
x_i = np.random.normal(size=N)

start_time = time.time()
y = np.array(x_r) + np.array(x_i) *1j
y = np.fft.fft(y)
#podział
y_r = np.real(y)
y_i = np.imag(y)

x1 = np.zeros(N,dtype=complex)
x2 = np.zeros(N,dtype=complex)

x1[0] = x_r[0]
x2[0] = x_i[0]
x1[N//2] = y[N//2]
x2[N//2] = 0

for k in range(1,N//2):
    x1[k] = 0.5 * (y_r[k] + 1j * y_i[k] + y_r[N - k] - 1j * y_i[N - k])
    x2[k] = 0.5 * (y_r[k] + 1j * y_i[k] - y_r[N - k] + 1j * y_i[N - k])
x1[N//2+1:] = np.conj(x1[1:N//2][::-1])
x2[N//2+1:] = np.conj(x2[1:N//2][::-1])
time_split = time.time() - start_time

# Pomiar czasu dla pełnej transformaty Fouriera zespolonej
start_time = time.time()
Y_complex = np.fft.fft(x_r + 1j * x_i)
time_complex = time.time() - start_time

# Pomiar czasu dla transformaty rzeczywistej (FFT zoptymalizowanej dla danych rzeczywistych)
start_time = time.time()
Y_real = np.fft.rfft(x_r)
time_real = time.time() - start_time

print(f"Czas FFT zespolonej: {time_complex:.6f} s")
print(f"Czas FFT rzeczywistej: {time_real:.6f} s")
print(f"Czas FFT metodą podziału: {time_split:.6f} s")