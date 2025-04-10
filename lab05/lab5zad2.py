import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, freqresp, impulse, step

# Parametry filtrów
N_list = [2, 4, 6, 8]
fc = 100  # Hz
w3db = 2 * np.pi * fc

# Zakres częstotliwości
f = np.linspace(1, 1000, 1000)
w = 2 * np.pi * f

# Tworzymy filtry i rysujemy charakterystyki
plt.figure(figsize=(12, 6))
for N in N_list:
    # Bieguny filtru Butterwortha
    poles = []
    for k in range(1, N + 1):
        theta = np.pi * (2 * k + N - 1) / (2 * N)
        p = w3db * np.exp(1j * theta)
        poles.append(p)

    poles = np.array(poles)
    A = np.poly(poles)  # wsp. mianownika
    B = [A[-1]]  # filtr normalizowany (stała z A przeniesiona do B)

    H = TransferFunction(B, A)

    # Charakterystyka częstotliwościowa
    _, Hf = freqresp(H, w)
    amp_db = 20 * np.log10(np.abs(Hf))
    phase = np.angle(Hf, deg=True)

    # Amplituda (liniowa)
    plt.plot(f, amp_db, label=f'N={N}')

plt.title('Charakterystyki amplitudowe |H(jω)| [dB] (skala liniowa)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Wzmocnienie [dB]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Amplituda (logarytmiczna skala częstotliwości)
plt.figure(figsize=(12, 6))
for N in N_list:
    poles = []
    for k in range(1, N + 1):
        theta = np.pi * (2 * k + N - 1) / (2 * N)
        p = w3db * np.exp(1j * theta)
        poles.append(p)
    poles = np.array(poles)
    A = np.poly(poles)
    B = [A[-1]]

    H = TransferFunction(B, A)
    _, Hf = freqresp(H, w)
    amp_db = 20 * np.log10(np.abs(Hf))
    plt.semilogx(f, amp_db, label=f'N={N}')

plt.title('Charakterystyki amplitudowe |H(jω)| [dB] (skala logarytmiczna)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Wzmocnienie [dB]')
plt.grid(True, which='both')
plt.legend()
plt.tight_layout()
plt.show()

# Faza (liniowa skala częstotliwości)
plt.figure(figsize=(12, 6))
for N in N_list:
    poles = []
    for k in range(1, N + 1):
        theta = np.pi * (2 * k + N - 1) / (2 * N)
        p = w3db * np.exp(1j * theta)
        poles.append(p)
    poles = np.array(poles)
    A = np.poly(poles)
    B = [A[-1]]

    H = TransferFunction(B, A)
    _, Hf = freqresp(H, w)
    phase = np.angle(Hf, deg=True)
    plt.plot(f, phase, label=f'N={N}')

plt.title('Charakterystyki fazowe ∠H(jω) [stopnie]')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Faza [°]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# dla ustalonego N
N = 4
poles = []
for k in range(1, N + 1):
    theta = np.pi * (2 * k + N - 1) / (2 * N)
    p = w3db * np.exp(1j * theta)
    poles.append(p)
poles = np.array(poles)
A = np.poly(poles)
B = [A[-1]]

H4 = TransferFunction(B, A)

# Odpowiedź impulsowa
t_imp, y_imp = impulse(H4)
plt.figure(figsize=(10, 4))
plt.plot(t_imp, y_imp)
plt.title('Odpowiedź impulsowa filtru (N=4)')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid(True)
plt.tight_layout()
plt.show()

# Odpowiedź na skok jednostkowy
t_step, y_step = step(H4)
plt.figure(figsize=(10, 4))
plt.plot(t_step, y_step)
plt.title('Odpowiedź skokowa filtru (N=4)')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid(True)
plt.tight_layout()
plt.show()
