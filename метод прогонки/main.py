import numpy as np
import create_matrix as cm

def f(x):
    return 1.0 - (6.0 / ((1.0 + x)**4))
  
def q(x):
    return (1.0 + x)**2

def u(x):
    return 1.0 / ((1.0 + x)**2)

a = 0
b = 3
N = 100
h = (b - a) / N
arr_x = np.linspace(a, b, N)
Q = [q(i) for i in arr_x]
F = [f(i) for i in arr_x]
F[0] = u(a)
F[-1] = u(b)
F = np.array(F)
matr_A = cm.getMatrix(N, h, arr_x.copy(), Q)
