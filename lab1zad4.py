import numpy as np
import matplotlib.pyplot as plt


#Mateusz = [77,97,116,101,117,115,122]
fpr = 16000  # Częstotliwość próbkowania 16 kHz
T = 0.1  # Czas transmisji bitu w sekundach (100 ms)
fc = 500  # Częstotliwość sinusoidy 500 Hz
#1600 próbek bit
asci_name= [77,97,116,101,117,115,122]
bit_name=[]
for i in asci_name:
    bit_name.append(bin(i))
print(bit_name)
time = np.linspace(0, T, int(fpr * T * len(bit_name)), endpoint=False)
sig=[]
for bit in bit_name:
    if bit[0]=='1':
        sig.append(-np.sin(2 * np.pi * fc * time))
    else:
        sig.append(np.sin(2 * np.pi * fc * time))
signal = np.concatenate(sig)
print(len(signal))
# Wyświetlanie wykresu
plt.plot(np.arange(0, len(signal)) / fpr, signal)
plt.title("Sygnał transmitujący bity ASCII imienia")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()
