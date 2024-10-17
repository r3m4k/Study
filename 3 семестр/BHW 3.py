import math

theoretical_significance = {'0.06': 0.06762159439330844,
                            '1.0':  0.8427007929497149,
                            '2.0':  0.9953222650189527,
                            '5.0':  0.9999999999984625}


def factorial(x):
    res = 1
    if x > 0:
        i = 1
        while i <= x:
            res *= i
            i += 1

    return res


def erf_lower_1(x, n):      # if x<<1 (x<0.1)
    res = 0
    for i in range(n):
        res += pow(2*x, 2*i+1) / factorial(2*i+1)
    res *= math.exp(-x**2) / (math.sqrt(math.pi))
    return res


def erf(x, n):
    for i in range(n):
        j = n - i
        if j % 2:
            flag1 = 1
            flag2 = 2
        else:
            flag1 = 2
            flag2 = 1

        if not i == n-1:
            a = flag2 * x
        else:
            a = 0

        if i == 0:
            fraction = j / (flag1 * x)
            res = (a + fraction)
        else:
            fraction = j / res
            res = (a + fraction)

    res = 1 - math.exp(-x**2) * res / math.sqrt(math.pi)

    return res


def distribution_error_function(x, n):
    if x < 0.1:
        return erf_lower_1(x, n)
    else:
        return erf(x, n)


def show(x):
    print(f'  n                      Значение erf({x})        Точность(%)')
    for i in range(1, 3):
        n = 20 * i
        res = distribution_error_function(x, n)
        accuracy = 100 * abs(res / theoretical_significance[str(x)] - 1)
        print(f' {n}                     ', '{:<24}'.format(res), f'({accuracy}%)')

    print('Теоритическое значение: ', theoretical_significance[str(x)], end='\n\n')


keys = list(theoretical_significance.items())
for i in range(len(keys)):
    show(float(keys[i][0]))
