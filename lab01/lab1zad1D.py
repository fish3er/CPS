import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
#sinusiidalna modulacje częsttlowsci
# Parametry sygnału
fs = 10000  # próbkowanie
fn = 50     # nośna
fm = 1      # modulująca
df = 5      # głebokość mod
T = 1
time_cons=np.linspace(0,T,int(T*fs),endpoint=False)
time_sample=np.linspace(0,T,int(T*25),endpoint=False) # 25 próbek na sec

#sygnały
mod_sig=df*np.sin(2*np.pi*time_cons*fm) # modulujacy
mod_sig =np.round(mod_sig,8)
carr_sig=np.sin(2*np.pi*time_cons*fn) #nośny
carr_sig =np.round(carr_sig,8)
sig=np.sin(2*np.pi*(fn+mod_sig)*time_cons) # sygnał zmodulowany
sig=np.round(sig,8)
n_sig=np.sin(2*np.pi*fn*time_cons)
n_sig=np.round(n_sig,8)
plt.plot(time_cons, mod_sig, label='Sygnał modulujący', color='blue', linestyle='--')
plt.plot(time_cons, sig, label='Sygnał zmodulowany (SFM)', color='green', linestyle='-')
#plt.plot(time_cons,n_sig,label='Signał bez mod', color='red', linestyle='--')
plt.title("Sygnał zmodulowany i sygnał modulujący")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.legend()
plt.grid()
plt.show()
##
sampled_signal = sig[::int(fs/25)]  # Próbkowanie sygnału zmodulowanego

# Ciągły sygnał zmodulowany (do porównania)
t_sampled_cont = time_cons[::int(fs/25)]


plt.plot(time_cons, sig, label="Sygnał zmodulowany (ciągły)", color='blue')
plt.plot(time_sample,sampled_signal, label="Sygnał próbkujący (25 Hz)", color='red')
plt.title("Porównanie sygnału zmodulowanego (ciągły vs. próbki)")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.legend()
plt.grid()
plt.show()


error = sig - np.interp(time_cons, time_sample, sampled_signal) # różnica między ciągłym sygnałem a próbkowanym
# Wyświetlanie błędów próbkowania
plt.figure(figsize=(10, 5))
plt.plot(time_cons, error)
plt.title("Błąd próbkowania sygnału zmodulowanego")
plt.xlabel("Czas [s]")
plt.ylabel("Błąd [V]")
plt.legend()
plt.grid()
plt.show()

#Obliczanie widma gęstości mocy (przed i po próbkowaniu)
# Przed próbkowaniem
n = len(sig)
frequencies_cont = fftfreq(n, 1/fs) # transformata
spectrum_cont = np.abs(fft(sig))**2 # moc

# Po próbkowaniu
n_sampled = len(sampled_signal)
frequencies_sampled = fftfreq(n_sampled, 1/25) # transfomataa
spectrum_sampled = np.abs(fft(sampled_signal))**2 # moc

# Wyświetlanie widm gęstości mocy
plt.figure(figsize=(10, 5))
plt.plot(frequencies_cont[:n//2], spectrum_cont[:n//2], label="Widmo gęstości mocy (przed próbkowaniem)", color='blue')
plt.plot(frequencies_sampled[:n_sampled//2], spectrum_sampled[:n_sampled//2], label="Widmo gęstości mocy (po próbkowaniu)", color='red')
plt.title("Widma gęstości mocy przed i po próbkowaniu")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Moc [dB]")
plt.legend()
plt.grid()
plt.show()