import numpy as np
from matplotlib import pyplot as plt

# kalkulacaj biegunów
N=[2, 4,6,8]
# N = [4]
w3db=2*np.pi*100
p=[]
for n in N:
    for k in range(n):
        p.append(w3db*np.exp(1j*(np.pi/2+np.pi/n*2+(k-1)*np.pi/n)))
    # plt.figure()
    poles=np.array(p) # konwesraj na np array uzyć funkcji numpy
    plt.scatter(poles.real, poles.imag, label=f'N={N}', marker='x')
    # plt.show()
plt.grid(True)
circle = plt.Circle((0, 0), w3db, color='b', fill=False, linestyle='dotted')
plt.gca().add_patch(circle)
plt.show()