import math
import numpy as np


theoretical_significance = {'sin(x^2)': 0.5836708999296233,
                            '1/(x^2 + 1)': 1.47112767430373459}


def f(x, flag):
    if flag == 'sin(x^2)':
        res = math.sin(pow(x, 2))
    elif flag == '1/(x^2 + 1)':
        res = 1/(pow(x, 2) + 1)

    return res


def trapezoid_method(a, b, n, flag):
    res = 0
    step = (b - a) / n
    x = a
    for i in range(n-1):
        res += step*(f(x, flag) + f(x+step, flag)) / 2
        x += step
    return res


def Romberg_method(a, b, flag):
    n_min = 1000
    n_max = 10000
    n = n_min
    gap = 500

    J = list()
    step = list()
    while n <= n_max:
        J.append(trapezoid_method(a, b, n, flag))
        step.append((b - a) / n)
        n += gap
    J = np.asarray(J, dtype=np.double)
    step = np.asarray(step, dtype=np.double)

    return np.polyfit(step, J, 2)[2]


def show(a, b, flag):
    phrase = f'Значение определённого интеграла от {a} до {b} функции {flag} полученное методом Ромберга:'
    res = Romberg_method(a, b, flag)
    print('{:<100}'.format(phrase), res)
    phrase = 'Теоретическое значение:'
    print('{:<100}'.format(phrase), theoretical_significance[flag])
    phrase = 'Точность (%):'
    accuracy = 100 * abs(res / theoretical_significance[flag] - 1)
    print('{:<100}'.format(phrase), accuracy, end='\n\n')


keys = list(theoretical_significance.items())
for i in range(len(keys)):
    show(0, 10, keys[i][0])

