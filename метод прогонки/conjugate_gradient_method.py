import matplotlib.pyplot as plt
import numpy as np
import main as m

def conjugate_gradient(matr_A, F, eps):
    x = np.zeros(len(matr_A))
    x_old = x.copy() 
    it = 0
    r_old = F - np.dot(matr_A, x_old)
    po = np.dot(r_old, r_old)
    p = r_old
    q = np.dot(matr_A, p)
    alpha = po / np.dot(p, q)
    x = x_old + alpha * p
    r = r_old - alpha * q

    while np.linalg.norm(np.dot(matr_A, x) - F) >= eps:
        print(np.linalg.norm(np.dot(matr_A, x) - F))  
        it +=1
        po_old = po
        po = np.dot(r, r)
        beta = po / po_old
        p = r + beta * p
        q = np.dot(matr_A, p)
        alpha = po / np.dot(p, q)
        x = x + alpha * p
        r = r - alpha * q
    print(it)
    return x


y = conjugate_gradient(m.matr_A, m.F, 0.05)
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