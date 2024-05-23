import numpy as np

def check_res(matr_A, n, x, h, F,eps, counter):
    s = 0.0
    A = np.matmul(matr_A, x)
    for i in range(n):
        s += (A[i] - F[i]) ** 2
    print(((h ** 2) * s) ** 0.5 , counter)
    return ((h ** 2) * s) ** 0.5 < eps