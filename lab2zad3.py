import numpy as np
import matplotlib.pyplot as plt

N = 100
fs = 1000
f = [50, 100, 150]
ampl = [50, 100, 150]
t= np.linspace(0, N/fs, N)
sig = ampl[0]*np.sin(2*np.pi*f[0]*t)+ ampl[1]*np.sin(2*np.pi*f[1]*t) +ampl[2]*np.sin(2*np.pi*f[2]*t)
plt.figure()
plt.plot(t,sig)
plt.show()

#macierz A=dct
A = np.zeros((N, N))

for k in range(N):
    for n in range(N):
        scale = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
        A[k, n] = scale * np.cos((np.pi * k * (n + 0.5)) / N)
# S= idct
S= np.linalg.inv(A)

# for i in range(N):
#     plt.figure()
#     plt.plot(t,S[:,i], label=f'kolumnaa {i} S')
#     plt.plot(t,A[i], label=f'Wiersz {i} A', linestyle='--')
#     plt.title(f'Wiersz {i} A; kolumnaa {i} S')
#     plt.legend()
#     plt.show()


#analiza syg
y = A @ sig
# skala czestotilowasci
fscale = (np.arange(N)* fs )/ (2 *N )
# wykres DCT
plt.figure()
plt.plot(fscale, y)
plt.xlabel('f')
plt.ylabel('amplitude')
plt.show()

# rec syg
sig_rec= S @ y
print("rec poparwna?", np.allclose(sig, sig_rec))
err=[]
for n in range(N):
    err.append(sig[n]-sig_rec[n])
print("avg err", np.mean(err))
plt.figure()
plt.stem(fscale, np.abs(err))
plt.show()





