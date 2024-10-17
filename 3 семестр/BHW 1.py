import math

theoretical_significance = 0.5836708999296233


def f(x):
    return math.sin(pow(x, 2))


def Byll_method(a, b, n):
    res = 0
    step = (b - a) / n
    for i in range(n // 4):
        x = step*i*4
        res += 7*f(x) + 32*f(x+step) + 12*f(x+step*2) + 32*f(x+step*3) + 7*f(x+step*4)
    res *= 2 * step / 45

    accuracy = 100 * abs(res / theoretical_significance - 1)
    print('\t\t', res, f'({accuracy}%)', end='')


def rectangle_method(x, y):
    res_left = 0
    for i in range(len(x)-1):
        res_left += (x[i+1] - x[i]) * y[i]

    return res_left


def Simson_method(a, b, n):
    res = 0
    step = (b - a)/n
    for i in range(n//2):
        x = step*i*2
        res += f(x) + 4*f(x+step) + f(x+step*2)
    res = step*res/3
    accuracy = 100 * abs(res / theoretical_significance - 1)
    print('\t\t', res, f'({accuracy}%)', end='')


print('Сравнение значений интеграла от 0 до 10 функции f(x)=sin(x^2):')
print('Теоретическое значение: ', theoretical_significance, end='\n\n')
print('Количесвенная характеристика разбиения (n):')
print('n:                   100                                             1000                                                10000')

# print('Метод Прямоугольников:', end='')
# rectangle_method(0, 10, 100)
# rectangle_method(0, 10, 1000)
# rectangle_method(0, 10, 10000)
# print()

print('Метод Симпсона:', end='')
Simson_method(0, 10, 100)
Simson_method(0, 10, 1000)
Simson_method(0, 10, 10000)
print()

print('Метод Буля:    ', end='')
Byll_method(0, 10, 100)
Byll_method(0, 10, 1000)
Byll_method(0, 10, 10000)
