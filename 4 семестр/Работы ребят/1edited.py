import math
import matplotlib.pyplot as plt
import numpy as np
def f(x, n):

    res = np.zeros(0)
    y = np.zeros(100)

    for i in range(0, 100):
        if x[i] == 0 or x[i] == 1/2 or x[i] == 1:
            y[i]=0

        elif x[i] < 1/2:
            y[i] = 1/2

        else:
            y[i] = -1/2

    for i in range(0, n):
        res = np.append(res, y)

    return res


n = 2
x = np.linspace(0, n, 100 * n)
y = f(x, n)


def S(x, N):

    S = list()
    s = 0

    for i in range(len(x)):
        for n in range(1, N + 1):
            s = s + 2/math.pi * 1/(2 * n - 1) * math.sin(2 * math.pi * (2 * n - 1) * x[i])
        S.append(s)
        s = 0

    return S


fig, ax = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(15)

color_of_fourier = np.array([['b', 'c'], ['m', 'r']])

k = 1
for i in range(2):
    for j in range(2):
        N = int(input('Введите количество членов ряда для Фурье-аппроксимации {}: '.format(k)))
        k += 1
        ax[i][j].plot(x, y, color='k', linewidth=1, label=r'$f(x)$')
        ax[i][j].plot(x, S(x, N), color=color_of_fourier[i][j], linewidth=2,
                      label='Аппроксимация при помощи ряда Фурье для N = {}'.format(N),
                      linestyle='--')
        ax[i][j].legend(loc='upper right', fontsize=10)
        ax[i][j].set_xlabel('$x$ values', fontsize=10)
        ax[i][j].set_ylabel('$y$ values', fontsize=10)
        ax[i][j].grid(visible=False)
        ax[i][j].set_xlim(0, n)
        ax[i][j].set_ylim(-0.7, 0.7)

plt.suptitle(r'Аппроксимация f(x) при помощи ряда Фурье', fontsize=15)
plt.tight_layout()
plt.show()
plt.savefig('plot.pdf')
