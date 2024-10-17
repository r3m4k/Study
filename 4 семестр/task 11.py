import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import curve_fit


m = 0.2

E, T = np.loadtxt('./Исходные файлы/data2.txt', dtype=np.double, unpack=True)

f = lambda x, E, A, a: 2 * np.sqrt(2 * m / (E - A * pow(x, a)) )

def period(E, A, a):
    T = np.zeros(len(E))
    for i in range(len(E)):
        x_end = (E[i]/A)**(1/a)
        T[i], _ = quad(f, 0, x_end, args=(E[i], A, a))
    return T

coef, _ = curve_fit(period, E, T)

print('Параметры, полученные с помощью фитированния данных:')
print(f'A = {coef[0]}, a = {coef[1]}')

fig, ax = plt.subplots()
plt.rcParams['font.size'] = '16'

ax.scatter(E, T, label='Данные из файла')
ax.plot(E, period(E, *coef), color='red', linestyle='--', label='Аппроксимация данных с помощью cur_fit', linewidth=2.5)

plt.xlabel('E')
plt.ylabel('T')

plt.grid()
plt.legend()
plt.show()
