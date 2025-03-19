import numpy as np
import matplotlib.pyplot as plt

ampl= 230
df=50
T=1

fs1=10000
fs2=51
fs3=50
fs4=49


t1= np.linspace(0,T,int(T*fs1),endpoint=False)
t2= np.linspace(0,T,int(T*fs2),endpoint=False)
t3= np.linspace(0,T,int(T*fs3),endpoint=False)
t4= np.linspace(0,T,int(T*fs4),endpoint=False)

#wartości sin
y1 = ampl * np.sin(2 * np.pi * df * t1)
y1=np.round(y1,8)
y2 = ampl * np.sin(2 * np.pi * df * t2)
y2=np.round(y2,8)
y3 = ampl * np.sin(2 * np.pi * df * t3)
y3=np.round(y3,8)
y4= ampl * np.sin(2 * np.pi * df * t4)
y4=np.round(y4,8)
# wyświtlanie
plt.plot(t1, y1, 'b-', label='10 kHz (pseudo analog)')
plt.plot(t2, y2, 'g-o', label='51 Hz')
plt.plot(t3, y3, 'r-o', label='50 Hz')
plt.plot(t4, y4, 'k-o', label='49 Hz')
plt.xlabel("Czas [s]")
plt.ylabel("Napięcie [V]")
plt.legend()
plt.grid()
plt.show()