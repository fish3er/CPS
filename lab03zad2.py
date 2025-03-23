import numpy as np
import matplotlib.pyplot as plt

f1=125
N=100 # ilosć próbek
M=100 # ilość rez na końcu
A1=100
A2=200
fs=1000
f1=100
f2=200
phi1= np.pi/7
phi2=-np.pi/11
 # wziekszenia syganłu o M zer
t = np.linspace(0,N/fs,N,endpoint=False)  # wektor czasowy
x = A1 * np.cos(2 * np.pi * f1 * t + phi1) + A2 * np.cos(2 * np.pi * f2 * t + phi2)# sygnał
x_app=x
for i in range(M):
    x_app=np.append(x_app,0)
# skowalowanie
x2= np.fft.fft(x_app)/(N+M)

# DtFT wzór
t_app = np.linspace(0,N/fs,N+M,endpoint=False)
fq=1000 # 0:0.25:1000
fq=np.linspace(0,1000,4*fq+1, endpoint=True)
x3=[]

for freq in fq:
   x3.append( np.sum( x_app * np.exp(-2j*np.pi*freq*t_app)))



freq = np.arange(N+M) * fs / (N+M)
freq1= np.arange(N) *fs /N
# Wizualizacja
plt.figure()

plt.subplot(3, 1, 1)
plt.plot(t,x)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda sygnału')
plt.title('Oryginalny Sygnał X')

plt.subplot(3, 1, 2)
plt.stem(freq, np.real(x2))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('FFT Sygnału X2')

plt.subplot(3, 1, 3)
plt.plot(fq, np.real(x3))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('DTFT Sygnału X3')

plt.tight_layout()
plt.show()

# DtFT wzór dla fa:-2000:0,25:2000
t_app = np.linspace(0,N/fs,N+M,endpoint=False)
fq1=2000 # -2000:0.25:2000
fq1=np.linspace(-fq1,fq1,4*fq1+1, endpoint=True)
x3_1=[]
k=0
for freq in fq1:
   x3_1.append( np.sum( x_app * np.exp(-2j*np.pi*freq*t_app)))

freq_2 = np.arange(N+M) * fs / (N+M)
freq1_2= np.arange(N) *fs /N
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t,x)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda sygnału')
plt.title('Oryginalny Sygnał X')

plt.subplot(3, 1, 2)
plt.stem(freq_2, np.real(x2))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('FFT Sygnału X2')

plt.subplot(3, 1, 3)
plt.plot(fq1, np.real(x3_1))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('DTFT Sygnału X3')

plt.tight_layout()
plt.show()