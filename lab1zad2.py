import numpy as np
import matplotlib.pyplot as plt

fs=200 #czestotliwość próbkowania
fr=10000 # czętotliwość rekonstrukcji
T =1/fs # okres próbkowania sygnału początkowego
t=1
ampl=230
fsig=50 # 50
#próbkowanie
t_sample=np.linspace(0,t,fs,endpoint="True")
sig_sample=np.sin(2*np.pi*fsig*t_sample)
sig_sample=sig_sample*ampl

t_rec= np.linspace(0,t,fr) # bo 0.1 z 10kHz
sig_rec=np.zeros_like(t_rec) # tablica zer
for n in range(len(t_rec)):
    sig_rec[n]=np.sum(sig_sample * np.sinc((t_rec[n]-t_sample)/T))

sig_analog=ampl*np.sin(2*np.pi*fsig*t_rec)
error = sig_analog - sig_rec
plt.plot(t_rec, sig_rec, label="Zrekonstruowany sygnał", color="green")
plt.plot(t_sample, sig_sample, label="Próbki sygnału")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Rekonstrukcja sygnału metodą splotu z sinc(x)")
plt.legend()
plt.grid()
plt.show()
plt.figure()
plt.plot(t_rec, error)
plt.xlabel("Czas [s]")
plt.ylabel("Błąd")
plt.title("Wykres błędu")
plt.show()
