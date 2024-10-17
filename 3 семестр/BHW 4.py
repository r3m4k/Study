import math

theoretical_significance = {'0.4': 0.3964614647513729,
                            '1.0':   0.946083070367183,
                            '10.0':  1.658347594218874,
                            '100.0': 1.5622254668890563}


def f(x):
    if x == 0:
        res = 1
    else:
        res = math.sin(x) / x

    return res


def Byll_method(a, b, n):
    res = 0
    step = (b - a) / n
    for i in range(n // 4):
        x = step*i*4
        res += 7*f(x) + 32*f(x+step) + 12*f(x+step*2) + 32*f(x+step*3) + 7*f(x+step*4)
    res *= 2 * step / 45

    return res


def show(x):
    print(f'   n                    Значение Si({x}), полученное методом Буля')
    res = Byll_method(0, x, 50)
    accuracy = 100 * abs(res / theoretical_significance[str(x)] - 1)
    print(' 50                    ', '{:<20}'.format(res), f'({accuracy} %)')

    res = Byll_method(0, x, 100)
    accuracy = 100 * abs(res / theoretical_significance[str(x)] - 1)
    print('100                    ', '{:<20}'.format(res), f'({accuracy} %)')

    print('Теоритическое значение:', theoretical_significance[str(x)], end='\n\n')


keys = list(theoretical_significance.items())
for i in range(len(keys)):
    show(float(keys[i][0]))

