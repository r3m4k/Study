import numpy as np
import scipy.integrate as integrate
from time import time

n = 1
l = 1
m = 1


def func(z, y, x):
    return 8 * np.cos(n * x) * np.cos(l * y) * np.cos(m * z) / np.sqrt(x**2 + y**2 + z**2)

def monte_karlo(n, e):
    x = np.random.uniform(e, np.pi, n)
    y = np.random.uniform(e, np.pi, n)
    z = np.random.uniform(e, np.pi, n)

    return pow(np.pi, 3) * np.sum(func(z, y, x)) / n


for e in [1e-5, 1e-6, 1e-7]:
    print(f'e = {e}')

    result = integrate.tplquad(func, e, np.pi, e, np.pi, e, np.pi)[0]

    print(f'Значение интеграла, полученное с помощью integrate.tplquad(): {result}\n')

    # Метод Монте-Карло

    print('Значения, полученные с помощью метода Монте-Карло:')
    for i in range(6, 9):
        start_time = time()
        res = monte_karlo(pow(10, i), e)
        print(f'\tПри n = 10^{i}:\t{res}')
        print(f'\tТочность: {abs(res - result)} (время выполнения {(time() - start_time):.8f})')
