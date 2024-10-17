import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from random import randint


def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c


depth, temp = np.loadtxt('./Исходные файлы/ice-temp.txt', unpack=True)

fig, ax = plt.subplots(nrows=1, ncols=2)
fig.set_figheight(7.65)
fig.set_figwidth(13.6)

ax[0].plot(depth, temp)
ax[0].set_xlabel('Глубина, м')
ax[0].set_ylabel('Температура, °С')
ax[0].set_title('Зависимость температуры\nот глубины', fontweight='bold')
ax[0].errorbar(depth, temp, xerr = np.random.rand(len(depth)) * 10,
                capsize=6, errorevery=1, linestyle='', ecolor='r',
                marker='o', markevery=1, markersize=6, markerfacecolor='none', markeredgecolor='r')

ax[1].plot(depth, np.gradient(temp, depth))
ax[1].set_xlabel('Глубина, м')
ax[1].set_ylabel('Градиент температуры, °С')
ax[1].set_title('Зависимость градиента температуры\nот глубины', fontweight='bold')


index = 8

coef, _ = curve_fit(quadratic_fit, depth[:index], np.gradient(temp, depth)[:index])
x = np.linspace(depth[0], depth[index])
ax[1].plot(x, coef[0] * x**2 + coef[1] * x + coef[2], label='аппроксимация параболой')

coef, _ = curve_fit(linear_fit, depth[index:], np.gradient(temp, depth)[index:])
x = np.array([depth[index], depth[-1]])
ax[1].plot(x, coef[0] * x + coef[1], label='аппроксимация прямой')


coef, _ = curve_fit(linear_fit, depth, temp)
print('Температура на поверхности', coef[1])

h = randint(2500, 3000)
interp_func = interp1d(depth, temp)
print(f'Температура на глубине {h} - {interp_func(np.linspace(2500, 3000, 501))[h - 2500]}')

plt.show()
