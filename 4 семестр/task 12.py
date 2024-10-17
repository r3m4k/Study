import math
from sympy import*
from time import time


theoretical_significance = math.pi**4 / 15

u = Symbol('u')

func = 1 / (1 - exp(-u))

def integrate_with_series(n):
    return float(integrate(u**3 * exp(-u) * func.series(exp(-u), n=n).removeO(), (u, 0, oo)))

def task(accuracy):
    print(f'Точность в {accuracy} знаков после запятой:')
    th_sign = int(theoretical_significance * pow(10, accuracy + 1))
    start_time = time()
    i = 1
    res = integrate_with_series(i)

    while int(res * pow(10, accuracy + 1) - th_sign) != 0:
        i += 1
        res = integrate_with_series(i)

    print(f'\tПолученное значение:   {res}')
    print(f'\tТеоретическое значение {theoretical_significance}')
    print(f'\tРазница между ними:    {abs(res - theoretical_significance)}')
    print(f'\tВремя выполнения: {(time() - start_time):.5f} секунд')
    print(f'\tКоличество членов разложения: {i}')
    print()

for i in [2, 3, 4, 5]:
    task(i)
