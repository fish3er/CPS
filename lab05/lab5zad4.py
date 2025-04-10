# cps_07_analog_transform.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control

# Wymagania
N = 16
f0 = 100
f1, f2 = 10, 100
Rp = 3
Rs = 100

# Chebyshev I  k - sys gain fukjci transferowej filtra  z - zera  p - bieguny b,a - wektory
z, p, k = signal.cheb1ap(N, Rp)  # Analog prototype
b, a = signal.zpk2tf(z, p, k)

# # Chebyshev I
# z, p, k = signal.cheb2ap(N, Rp)  # Analog prototype
# b, a = signal.zpk2tf(z, p, k)
# # Butterworth
# z, p, k = signal.buttap(N)  # Analog prototype
# b, a = signal.zpk2tf(z, p, k)

#częstotliwościowa
f = np.arange(0, 1000.01, 0.01)
w = 2 * np.pi * f
w_Hz = w / (2 * np.pi)
w_rad = w
_, H = signal.freqs(b, a, w_rad)

#
theta = np.linspace(0, 2 * np.pi, 1000)
circle = np.exp(1j * theta)

plt.figure()
plt.semilogx(w_Hz, 20 * np.log10(np.abs(H)))
plt.grid(True)
plt.xlabel('f [Hz]')
plt.title('Analog Proto |H(f)|')

plt.figure()
plt.plot(np.real(z), np.imag(z), 'ro', label='Zeros')
plt.plot(np.real(p), np.imag(p), 'b*', label='Poles')
plt.plot(np.real(circle), np.imag(circle), 'k-', label='Unit Circle')
plt.legend()
plt.grid(True)
plt.title('Analog Proto ZP')

# transformata -> zwraca współczynniki
# b, a = signal.lp2lp(b, a, wo=2 * np.pi * f0)
b, a = signal.lp2hp(b, a, wo=2 * np.pi * f0)
# b, a = signal.lp2bp(b, a, wo=2 * np.pi * np.sqrt(f1*f2), bw=2 * np.pi * (f2 - f1))
# b, a = signal.lp2bs(b, a, wo=2 * np.pi * np.sqrt(f1*f2), bw=2 * np.pi * (f2 - f1))

#  zera i bueguny na podstawie wspołczynników
z = np.roots(b)
p = np.roots(a)

manual = False

if manual:
    b = [3, 2]
    a = [4, 3, 2, 1]
    z = np.roots(b)
    p = np.roots(a)
else:
    k = 0.001
    z = 2j * np.pi * np.array([600, 800])
    z = np.concatenate([z, np.conj(z)])
    p = -1 + 2j * np.pi * np.array([100, 200])
    p = np.concatenate([p, np.conj(p)])
    b, a = signal.zpk2tf(z, p, k)

# zera bieguny
plt.figure()
plt.plot(np.real(z), np.imag(z), 'bo', label='Zeros')
plt.plot(np.real(p), np.imag(p), 'r*', label='Poles')
plt.xlabel('Real')
plt.ylabel('Imag')
plt.grid(True)
plt.title('Zera (o) i Bieguny (*)')
plt.legend()


f = np.arange(0, 1000.1, 0.1) # Hz
w = 2 * np.pi * f #
s = 1j * w
H = np.polyval(b, s) / np.polyval(a, s) # H(s)

plt.figure()
plt.plot(f, 20 * np.log10(np.abs(H))) # ampl na dB
plt.xlabel('f [Hz]')
plt.ylabel('|H(f)| [dB]')
plt.title('Amplitudowa')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(f, np.unwrap(np.angle(H))) # zwraca faze w rad
plt.xlabel('f [Hz]')
plt.ylabel('Faza [rad]')
plt.title('Fazowa')
plt.grid(True)

# impuls
sys = control.tf(b, a)

plt.figure()
t_imp, y_imp = control.impulse_response(sys)
plt.plot(t_imp, y_imp)
plt.title('impulsowa')
plt.grid(True)

# skok
plt.figure()
t_step, y_step = control.step_response(sys)
plt.plot(t_step, y_step)
plt.title('skokowa')
plt.grid(True)

plt.show()
