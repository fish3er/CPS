import numpy as np
import matplotlib.pyplot as plt


#Mateusz = [77,97,116,101,117,115,122]
fpr = 16000
#  8000 16000 32000 48000
# Częstotliwość próbkowania 16 kHz
T = 0.1  # Czas transmisji bitu w sekundach
fc = 5  # Częstotliwość sinusoidy
#1600 próbek bit
#asci_name= [77,97,116,101,117,115,122]
asci_name=[77]
bit_name=[]
for i in asci_name:
    bit_name.append(bin(i))
print(bit_name)
# 7 liter każda 8 bitów * 0.1 s -> 5,6 s
time = np.linspace(0, T*8*len(asci_name), int(T*8*7*fpr), endpoint=False)
sig = []
for bits in bit_name:
    for bit in bits:
        if bit == '1':
            sig.append(-np.sin(2 * np.pi * fc * time))  # Dla bitu 1
        else:
            sig.append(np.sin(2 * np.pi * fc * time))  # Dla bitu 0

# Łączenie wszystkich sygnałów
signal = np.concatenate(sig)
print(len(signal))
# Wyświetlanie wykresu
plt.plot(np.linspace(0, T*8*len(asci_name), len(signal)), signal)
plt.title("Sygnał transmitujący bity ASCII imienia")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.show()


