import numpy as np
N=20
A = np.zeros((N, N))

for k in range(N):
    for n in range(N):
        scale = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
        A[k, n] = scale * np.cos((np.pi * k * (n + 0.5)) / N)

# ortogonalosc
orthogonal = True
for i in range(N):
    for j in range(i+1, N):
        dot_product = np.dot(A[i], A[j])
        if np.abs(dot_product) > 1e-8:
            orthogonal = False
if orthogonal:
    print("jest ortogonalna")
else:
    print("nie jest ortogonalna")