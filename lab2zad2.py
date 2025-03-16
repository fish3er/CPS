import numpy as np
N=20
A = np.zeros((N, N))

for k in range(N):
    for n in range(N):
        scale = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
        A[k, n] = scale * np.cos((np.pi * k * (n + 0.5)) / N)

S=A.transpose()

X= np.random.randn(N, N)
X.transpose()
X_= A @ X
Xrec= S@X_

err_rec = np.linalg.norm(Xrec - X)

print("Original signal:\n", X)
print("\nReconstructed signal:\n", Xrec)
print("\nReconstruction error:",  round(err_rec,8))