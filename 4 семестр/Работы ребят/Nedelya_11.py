#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data = np.loadtxt("data2.txt", delimiter="\t")

E = data[:, 0]
T = data[:, 1]


def integrand(x, A, alpha):
    return A * np.abs(x) ** alpha

# Аппроксимация интегральной функцией
popt, pcov = curve_fit(integrand, E, T)

A = popt[0]
alpha = popt[1]

print(f"Параметр A: {A}")
print(f"Параметр alpha: {alpha}")

# Построение графика и аппроксимация
plt.scatter(E, T, label='Исходные данные')
plt.xlabel('E')
plt.ylabel('T')

E_fit = np.linspace(min(E), max(E), 100)
T_fit = integrand(E_fit, A, alpha)
plt.plot(E_fit, T_fit, color='red', label='Аппроксимация')

plt.legend()
plt.grid(True)
plt.show()


# In[12]:


import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.optimize import minimize


data = np.loadtxt('data2.txt')
E = data[:, 0]
T = data[:, 1]

m = 0.2


def integrand(x, E, A, alpha):
    return (2*m)**0.5 / (E - A * np.abs(x)**alpha)**(0.5)

def period(E, A, alpha):
    result = np.zeros_like(E)
    for i in range(len(E)):
        a[i] = -(E[i]/A)**(1/alpha)
        b[i] = (E[i]/A)**(1/alpha)
        result[i], _ = quad(integrand, a[i], b[i], args=(E[i], A, alpha))
    return result


def error_function(params):
    A, alpha = params
    predicted_T = period(E, A, alpha)
    error = np.sum((T - predicted_T)**2)  
    return error

initial_guess = [1,1]

result = minimize(error_function, initial_guess, method='Nelder-Mead')


A_opt, alpha_opt = result.x
print(f"Оптимальные значения параметров: A = {A_opt}, alpha = {alpha_opt}")


popt, pcov = curve_fit(period, E, T)

plt.scatter(E, T, label='Исходные данные')
plt.plot(E, period(E, A_opt, alpha_opt), color='red', label='Аппроксимация')
plt.xlabel('E')
plt.ylabel('T')
plt.legend()
plt.show()


# In[ ]:




