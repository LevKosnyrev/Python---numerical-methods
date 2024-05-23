import matplotlib.pyplot as plt
import numpy as np
import main as m
import check_result as cr

def jacobi(n, h, F, matr_A, eps):
    x = np.zeros(n)
    xp = np.zeros(n)
    x[:] = 1
    xp[:] = 1
    x[0] = m.u(0)
    x[-1] = m.u(3)
    counter = 0
    while not cr.check_res(matr_A, n, x, h, F, eps, counter):
        counter+=1
        x[0] = (-1 * xp[1] * matr_A[0][1] + F[0])/matr_A[0][0]

        for i in range(1, n-1):
            x[i] = (-1* xp[i-1] * matr_A[i][i-1] - xp[i+1]* matr_A[i][i-1] + F[i])/matr_A[i][i]

        x[-1] = (-1* xp[-2] * matr_A[-1][-2] + F[-1])/matr_A[-1][-1]

        for i in range(n):
            xp[i] = x[i]
    print(counter)
    return x


y = jacobi(m.N, m.h, m.F, m.matr_A, 0.05)
ux = m.u(m.arr_x)

fig, ax = plt.subplots()
ax.scatter(m.arr_x, y, label="y(x)")
plt.legend()

fig1, ax1 = plt.subplots()
ax1.scatter(m.arr_x, ux, label="u(x)")
plt.legend()

fig2, ax2 = plt.subplots()
ax2.scatter(m.arr_x, abs(ux - y), label="errors")
plt.legend()

plt.show()
