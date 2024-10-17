import math


def series_sum(degree_indicator, accuracy, theoretical_significance):
    res = 0
    n = 1
    accuracy += 1
    acc = pow(10, -accuracy)
    while abs(theoretical_significance - res) > acc:
        res += pow(-1, n-1) / pow(n, degree_indicator)
        n += 1

    return n


theoretical_significances = [math.log(2, math.e), math.pi**2 / 12, 7 * pow(math.pi, 4) / 720]

# print(series_sum(4, 3, theoretical_significances[2]))
# print('', theoretical_significances[2])


print('Число членов ряда, необходимых для обеспечения точности 3, 5, 7 знаков после запятой (в указанных точках)')
print('η(1): ', series_sum(1, 3, theoretical_significances[0]), series_sum(1, 5, theoretical_significances[0]),
      series_sum(1, 7, theoretical_significances[0]))

print('η(2): ', series_sum(2, 3, theoretical_significances[1]), series_sum(2, 5, theoretical_significances[1]),
      series_sum(2, 7, theoretical_significances[1]))

print('η(4): ', series_sum(4, 3, theoretical_significances[2]), series_sum(4, 5, theoretical_significances[2]),
      series_sum(4, 7, theoretical_significances[2]))
