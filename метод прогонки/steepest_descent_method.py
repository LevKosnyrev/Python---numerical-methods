import matplotlib.pyplot as plt
import numpy as np
import main as m

def steepest_descent(matr_A, F, eps):
    x = np.zeros(len(matr_A))
    x_old = x.copy()
    it = 0
    r = np.dot(matr_A, x) - F

    while np.linalg.norm(r) >= eps:
        it += 1
        r = np.dot(matr_A, x_old) - F
        tau = np.dot(r, r) / np.dot(r, np.matmul(matr_A, r))
        x = x_old - tau*r
        x_old = np.copy(x)
    print(it)
    return x

y = steepest_descent(m.matr_A, m.F, 0.05)
ux = m.u(m.arr_x)
errors = abs(ux - y)
print("Максимальная погрешность: ", max(errors))
print("h^2:", m.h**2)

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