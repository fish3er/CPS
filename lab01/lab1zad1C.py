import numpy as np
import matplotlib.pyplot as plt

fs=100
T=1
time= np.linspace(0, T, T*fs,endpoint=False)
sinus=[]
for i in range(61):
    f= i * 5 #częstotliwość    print(f)
    y=np.sin(2 * np.pi * f * time)
    y= np.round(y, 8)
    sinus.append(y)
    plt.plot(time, y, 'b-', label='f = %.0f' % f)
    plt.title(f"{f}Hz, {i}")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.grid()
    plt.show()

plt.figure()
plt.plot(time, sinus[1], label='5Hz, i=1')
plt.plot(time, sinus[21], label='105Hz, i=21')
plt.plot(time, sinus[41], label='205Hz, i=41')
plt.legend()
plt.show()

plt.figure()
plt.plot(time, sinus[19], label="95Hz, i=19")
plt.plot(time, sinus[39], label="195Hz, i=39")
plt.plot(time, sinus[59], label="295Hz, i=59")
plt.legend()
plt.show()

plt.figure()
plt.plot(time, sinus[19], label="95Hz, i = 19")
plt.plot(time, sinus[21], label="105Hz, i = 21")
plt.legend()

cosin=[]
for i in range(61):
    f= i * 5 #częstotliwość    print(f)
    y=np.cos(2 * np.pi * f * time)
    cosin.append(y)
    plt.plot(time, y, 'b-', label='f = %.0f' % f)
    plt.title(f"{f}Hz, {i}")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.grid()
    plt.show()

plt.figure()
plt.plot(time, cosin[1], label='5Hz, i=1')
plt.plot(time, cosin[21], label='105Hz, i=21')
plt.plot(time, cosin[41], label='205Hz, i=41')
plt.legend()
plt.show()

plt.figure()
plt.plot(time, cosin[19], label="95Hz, i=19")
plt.plot(time, cosin[39], label="195Hz, i=39")
plt.plot(time, cosin[59], label="295Hz, i=59")
plt.legend()
plt.show()

plt.figure()
plt.plot(time, cosin[19], label="95Hz, i = 19")
plt.plot(time, cosin[39], label="195Hz, i = 39")
plt.plot(time, cosin[59], label="295Hz, i = 59")
plt.legend()
plt.show()

plt.figure()
plt.plot(time, cosin[19], label="95Hz, i = 19")
plt.plot(time, cosin[21], label="105Hz, i = 21")
plt.legend()
plt.show()