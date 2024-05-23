import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    y1 = -np.sin(t) / np.sqrt(1 + np.exp(2 * t)) + y[0] * (y[0]**2 + y[1]**2 - 1)
    y2 = np.cos(t) / np.sqrt(1 + np.exp(2 * t)) + y[1] * (y[0]**2 + y[1]**2 - 1)
    return np.array([y1, y2])

def metodMersona(t, ys):
    h = t[1] - t[0]
    y = [ys]
    for i in range(len(t) - 1):
        k1 = f(t[i], ys)
        k2 = f(t[i] + h/3, ys + h/3 * k1)
        k3 = f(t[i] + h/3, ys + h/6 * k1 + h/6 * k2)
        k4 = f(t[i] + h/2, ys + h/8 * k1 + 3/8 * h * k3)
        k5 = f(t[i] + h, ys + h/2 * k1 - 3/2 * h * k3 + 2 * h * k4)
        ys = ys + h * (k1 + 4 * k4 + k5) / 6
        y.append(ys)
    return np.array(y).T

n = np.arange(10, 1001)
e = np.zeros_like(n, dtype=float)
h = np.zeros_like(n, dtype=float)
ys = np.array([1/np.sqrt(2), 0])

a, b = 0, 5
for i in range(len(n)):
    t = np.linspace(a, b, n[i])
    yt = np.array([np.cos(t) / np.sqrt(1 + np.exp(2 * t)), np.sin(t) / np.sqrt(1 + np.exp(2 * t))])
    y = metodMersona(t, ys)
    h[i] = t[1] - t[0]
    e[i] = np.max(np.abs(y - yt))

plt.figure()
plt.plot(h, e)
plt.title('e(h)')
plt.xlabel('h')
plt.ylabel('e')

plt.figure()
plt.plot(h, e / h**5)
plt.title('e/h^5(h)')
plt.xlabel('h')
plt.ylabel('e/h^5')

plt.figure()
plt.plot(h**5, e)
plt.title('e(h^5)')
plt.xlabel('h^5')
plt.ylabel('e')

plt.show()

def f2(t, ys, m, M):
    v1, v2, x, y = ys
    r1 = ((x + m)**2 + y**2)**(3/2)
    r2 = ((x - M)**2 + y**2)**(3/2)
    dv1 = x + 2 * v2 - M * (x + m) / r1 - m * (x - M) / r2
    dv2 = y - 2 * v1 - M * y / r1 - m * y / r2
    dx = v1
    dy = v2
    return np.array([dv1, dv2, dx, dy])

def metodMersona2(a, b, m, M, n, ys, e):
    t = np.concatenate((np.linspace(a, a + e, n), np.linspace(a + e, b - e, n), np.linspace(b - e, b, n)))
    y = [ys]
    for i in range(len(t) - 1):
        h = t[i + 1] - t[i]
        k1 = f2(t[i], ys, m, M)
        k2 = f2(t[i] + h / 3, ys + h / 3 * k1, m, M)
        k3 = f2(t[i] + h / 3, ys + h / 6 * k1 + h / 6 * k2, m, M)
        k4 = f2(t[i] + h / 2, ys + h / 8 * k1 + 3 / 8 * h * k3, m, M)
        k5 = f2(t[i] + h, ys + h / 2 * k1 - 3 / 2 * h * k3 + 2 * h * k4, m, M)
        ys = ys + h * (k1 + 4 * k4 + k5) / 6
        y.append(ys)
    return np.array(y).T

x0 = 0.994
y0 = 0
v10 = 0
v20 = -2.031732629557337
m = 0.012277471
M = 1 - m
e = 0.1
ys = np.array([v10, v20, x0, y0])

y = metodMersona2(0, 11.15, m, M, 1000, ys, e)

plt.figure()
plt.plot(y[2], y[3])
plt.title("График орбиты")

plt.figure()
plt.plot(y[0], y[1])
plt.title("График скорости движения")

plt.show()