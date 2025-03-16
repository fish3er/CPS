import numpy as np
import matplotlib.pyplot as plt

ampl= 230
df=50
T=0.1

fs1=10000
fs2=500
fs3=200

# próbki czasu
t1= np.linspace(0,T,int(T*fs1))
t2= np.linspace(0,T,int(T*fs2))
t3= np.linspace(0,T,int(T*fs3))

#wartości sin
y1 = ampl * np.sin(2 * np.pi * df * t1)
y2 = ampl * np.sin(2 * np.pi * df * t2)
y3 = ampl * np.sin(2 * np.pi * df * t3)

plt.plot(t1, y1, 'b-', label='10 kHz (pseudo analog)')
plt.plot(t2, y2, 'ro', label='500 Hz')
plt.plot(t3, y3, 'k-x', label='200 Hz')
plt.xlabel("Czas [s]")
plt.ylabel("Napięcie [V]")
plt.legend()
plt.grid()
plt.show()