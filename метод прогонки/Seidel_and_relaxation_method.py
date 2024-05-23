import matplotlib.pyplot as plt
import numpy as np
import main as m
import check_result as cr

def relax(n, h, matr_A, F, mu, eps):
    x = np.zeros(n)
    counter = 0
    while not cr.check_res(matr_A, n, x, h, F, eps, counter):
        counter+=1
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(matr_A[i][j] * x_new[j] for j in range(i))
            s2 = sum(matr_A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1-mu)*x[i]+mu*(F[i] - s1 - s2) / matr_A[i][i]
        for i in range(n):
            x[i] = x_new[i]
    print(counter)
    return x

y = relax(m.N, m.h, m.matr_A, m.F, 1.89, 0.05)
ux = m.u(m.arr_x)

fig, ax = plt.subplots()
ax.scatter(m.arr_x, y, label='y(x)')
plt.legend()
fig2, ax2 = plt.subplots()
ax2.scatter(m.arr_x, ux, label='u(x)')
plt.legend()
fig3, ax3 = plt.subplots()
ax3.scatter(m.arr_x, abs(ux-y), label='errors')
plt.legend()

plt.show()