import numpy as np
import matplotlib.pyplot as plt
#from scipy.fft import fft, fftfreq

# Parametry sygnału
fs = 10000  # próbkowanie
fn = 50     # nośna
fm = 1      # modulująca
df = 5      # głebokość mod
T = 1
time_cons=np.linspace(0,T,int(T*fs))
time_sample=np.linspace(0,T,int(T*25)) # 25 próbek na sec

#sygnały
mod_sig=df*np.sin(2*np.pi*time_cons*fm) # modulujacy
carr_sig=np.sin(2*np.pi*time_cons*fn) #nośny
sig=np.sin(2*np.pi*(fn+mod_sig)*time_cons) # sygnał zmodulowany

plt.plot(time_cons, mod_sig, label='Sygnał modulujący', color='blue')
plt.plot(time_cons, sig, label='Sygnał zmodulowany (SFM)', color='green', linestyle='--')
plt.title("Sygnał zmodulowany i sygnał modulujący")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.legend()
plt.grid()
plt.show()


