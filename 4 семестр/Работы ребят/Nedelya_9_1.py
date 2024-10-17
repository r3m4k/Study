import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

Ec=5

def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def find_start_point(E, j, threshold):
    for i in range(1, len(j)):
        if abs(j[i] - j[i-1]) > threshold:
            i=18    
    return i

threshold = 0.05

def find_critical_current(E, j):
    popt, _ = curve_fit(linear_fit, E[j > 0], j[j > 0])
    jc = 1 / popt[0]  # Критический ток
    return jc


def general_fit_func(E, j):
    popt, _ = curve_fit(quadratic_fit, E[j > 0], j[j > 0])
    return quadratic_fit(E, *popt)


data1 = np.loadtxt('magn_current_T50_H200_Nr576.txt')
data2 = np.loadtxt('magn_current_T50_H200_Nr676.txt')
data3 = np.loadtxt('magn_current_T50_H200_Nr900.txt')

E1, j1 = data1[:, 0], data1[:, 1]
E2, j2 = data2[:, 0], data2[:, 1]
E3, j3 = data3[:, 0], data3[:, 1]


plt.figure()
plt.plot(E1, j1, 'o-', label='ВАХ Nr576')
plt.plot(E2, j2, 'o-', label='ВАХ Nr676')
plt.plot(E3, j3, 'o-', label='ВАХ Nr900')
plt.xlabel('Напряженность поля')
plt.ylabel('Плотность тока')
plt.legend()
plt.show()


for E, j, name in [(E1, j1, 'Nr576'), (E2, j2, 'Nr676'), (E3, j3, 'Nr900')]:
    plt.figure()
    plt.plot(E, j, 'o-', label=f'ВАХ {name}')
    
    for i in range(3):
        if i == 0:
            fit_func = linear_fit
        elif i == 1:
            fit_func = quadratic_fit
        else:
            fit_func = cubic_fit

        start_point = find_start_point(E, j, threshold)
        popt, _ = curve_fit(fit_func, E[start_point:], j[start_point:])

        jc = fit_func(5, *popt)

        plt.plot(E, fit_func(E, *popt), label=f'Аппроксимация {i+1}, jc={jc}')

    plt.xlabel('Напряженность поля')
    plt.ylabel('Плотность тока')
    plt.legend()
    plt.title(f'ВАХ {name}')
    plt.show()

mask = (E1 >= 1) & (E1 <= 17)


E1_filtered = E1[mask]
j1_filtered = j1[mask]


interp_func = interp1d(E1_filtered, j1_filtered, kind='quadratic')
E_interp = np.linspace(min(E1_filtered), max(E1_filtered), 1000)
j_interp = interp_func(E_interp)


plt.figure()
plt.plot(E1_filtered, j1_filtered, 'o-', label='Данные (1-17)')
plt.plot(E_interp, j_interp, label='Интерполяция')
plt.xlabel('Напряженность поля')
plt.ylabel('Плотность тока')
plt.legend()
plt.title('Интерполяция данных в диапазоне от 1 до 17')
plt.show()


# In[ ]:




