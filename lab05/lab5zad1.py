import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# m zero
pos = [-0.5 + 1j*9, -0.5 - 1j*9, -1 + 1j*10, -1 - 1j*10, -0.5 + 1j*10.5, -0.5 - 1j*10.5]
zeros = [1j*5, -1j*5, 1j*15, -1j*15]

# Tworzenie wielomianów
num = np.poly(zeros) # miejsca zerowe
den = np.poly(pos) # bieguny

# num/den
h = np.polyval(num,10*1j)/np.polyval(den,10*1j)
num=num/h
H = sig.TransferFunction(num, den) # dziedzi


w = np.linspace(1, 30, 1000)  # Zakres częstotliwości
w, h = sig.freqresp(H, w) # oblicza odpowiedź częstotliwościową układu dla wartości częstotliwości
# h to H(jw)
# alpltuda liniowa
plt.plot(w, np.abs(h))
plt.title('Ampl liniowo')
plt.xlabel('Częstotliwość [rad/s]')
plt.ylabel('|H(jω)|')
plt.grid()
plt.show()

# Charakterystyka amplitudowa w skali decybelowej

plt.plot(w, 20 * np.log10(np.abs(h)))
plt.title('Ampl decy')
plt.xlabel('Częstotliwość [rad/s]')
plt.ylabel('20log|H(jω)|')
plt.grid()
plt.show()

# Charakterystyka fazowa

plt.plot(w, np.angle(h, deg=True))
plt.title('Fazowo')
plt.xlabel('Częstotliwość [rad/s]')
plt.ylabel('Faza [stopnie]')
plt.grid()
plt.show()
