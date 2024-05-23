import matplotlib.pyplot as plt
import numpy as np
import main as m

def sweep(a, b, n, h, arr_x, F, Q):
    ua = m.u(a)
    ub = m.u(b)

    arr_y = np.zeros(n)

    A = []
    B = []
    C = []
    A.append(0.0)
    B.append(1.0)
    C.append(0.0)
    for i in range(1, n - 1):
        A.append(-1 / h**2)
        B.append((2 / h**2) + Q[i])
        C.append(-1 / h**2)
    A.append(0.0)
    B.append(1.0)
    C.append(0.0)

    F[0] = ua
    F[-1] = ub

    alpha = np.zeros(n)
    betta = np.zeros(n)

    alpha[1] = (-C[0] / B[0])
    betta[1] = (F[0] / B[0])

    for i in range(1, n - 1):
        alpha[i+1] = -(C[i]/(B[i] + alpha[i]*A[i]))
        betta[i+1] = (F[i] - A[i]*betta[i])/(B[i] + A[i]*alpha[i])

    # arr_y[n-1] = (F[-1] - A[-1]*betta[-1]) / (B[-1] + A[-1]*alpha[-1])
    arr_y[n-1] = ub
    print(len(alpha))

    for i in range(n - 2, -1, -1):
        arr_y[i] = (alpha[i + 1]*arr_y[i + 1] + betta[i + 1])

    return arr_x, arr_y



x, y = sweep(m.a, m.b, m.N, m.h, m.arr_x, m.F, m.Q)

ux = m.u(x)
fig, ax = plt.subplots()
ax.scatter(x, y, label='y(x)')
plt.legend()

fig1, ax1 = plt.subplots()
ax1.scatter(x, ux, label='u(x)')
plt.legend()

errors = np.abs(ux - y)
fig2, ax2 = plt.subplots()
ax2.scatter(x, errors, label='errors')
print(max(abs(ux - y)))
plt.legend()

plt.show()