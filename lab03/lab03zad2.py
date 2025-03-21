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
fq=np.linspace(0,1000,4001, endpoint=True)
x3=[]
k=0
for freq in fq:
   x3.append( np.sum( x_app * np.exp(-2j*np.pi*freq*t_app)))



freq = np.arange(N+M) * fs / (N+M)
freq1= np.arange(N) *fs /N
plt.stem(freq1, np.real(x))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('X')
plt.show()

plt.stem(freq, np.real(x2))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('X2')
plt.show()

print(np.real(x2))
plt.stem(freq, np.real(x3))
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Część rzeczywista')
plt.title('X3')
plt.show()