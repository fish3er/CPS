import numpy as np
import matplotlib.pyplot as plt

ampl= 230
df=50
T=1

fs1=10000
fs2=51
fs3=50
fs4=49


t1= np.linspace(0,T,int(T*fs1))
t2= np.linspace(0,T,int(T*fs2))
t3= np.linspace(0,T,int(T*fs3))
t4= np.linspace(0,T,int(T*fs4))

#wartości sin
y1 = ampl * np.sin(2 * np.pi * df * t1)
y2 = ampl * np.sin(2 * np.pi * df * t2)
y3 = ampl * np.sin(2 * np.pi * df * t3)
y4= ampl * np.sin(2 * np.pi * df * t4)
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