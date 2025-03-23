import numpy as np
import matplotlib.pyplot as plt

N=100 # ilosć próbek
A1=1
A2=0.0001
fs=1000
f1=100
f2=125
phi1= 0
phi2= 0

t = np.linspace(0,N/fs,N,endpoint=False)  # wektor czasowy
x = A1 * np.cos(2 * np.pi * f1 * t + phi1) + A2 * np.cos(2 * np.pi * f2 * t + phi2)  # sygnał
f_max=500
f_DtFt=np.linspace(0,f_max,10*f_max+1,endpoint=True)

plt.plot(t,x)
plt.show()
x_DfFT=[]
for f in f_DtFt:
   x_DfFT.append( np.sum( x * np.exp(-2j*np.pi*f*t)))
# widmo ?
freq = np.arange(N) * fs / (N)
x2= np.fft.fft(x)/(N)
plt.stem(freq, np.real(x2))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('FFT Sygnału X2')
plt.show()
# widmo sygnału
plt.plot(f_DtFt, np.real(x_DfFT))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('DTFT Sygnału X3')
plt.show()
