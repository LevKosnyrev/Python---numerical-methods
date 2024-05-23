import numpy as np

def getMatrix(n, h, arr, Q):
    A = []
    B = []
    C = []
    A.append(0.0)
    B.append(0.0)
    C.append(1.0)
    for i in range(1, n - 1):
        A.append(-1 / h ** 2)
        B.append(-1 / h ** 2)
        C.append((2 / h ** 2) + Q[i])
    A.append(0.0)
    B.append(0.0)
    C.append(1.0)
    matrix = np.zeros((n, n))
    for i in range(n):
        if i == 0:
            matrix[i][i + 1] = B[i]
            matrix[i][i] = C[i]
        elif i == n - 1:
            matrix[i][i - 1] = A[i]
            matrix[i][i] = C[i]
        else:
            matrix[i][i - 1] = A[i]
            matrix[i][i + 1] = B[i]
            matrix[i][i] = C[i]
    return matrix.copy()