import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import chebwin

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
# widmo fft
freq = np.arange(N) * fs / (N)
x2= np.fft.fft(x)/(N)
plt.stem(freq, np.real(x2))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('FFT Sygnału X2')
plt.show()
# widmo DtFT
plt.plot(f_DtFt, np.real(x_DfFT))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('DTFT Sygnału X3')
plt.show()
#     "Rectangular": np.ones(N),
#     "Hamming": np.hamming(N),
#     "Blackman": np.blackman(N),
#     "Chebyshev 100 dB": chebwin(N, at=100),
#     "Chebyshev 120 dB": chebwin(N, at=120)
w= np.hamming(N)
x_w=x*w # mnożenie przez okno
# plt.plot(t,x_w)
# plt.show()
#DfTF dla okna
x_DfFT_w=[]
for f in f_DtFt:
   x_DfFT_w.append( np.sum( x_w * np.exp(-2j*np.pi*f*t)))

plt.plot(f_DtFt, 20*np.log10(np.abs(x_DfFT_w)))
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Moduł DTFT")
plt.title("Widmo DTFT dla okna ")
plt.grid()
plt.show()