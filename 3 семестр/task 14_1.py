import numpy as np
import matplotlib.pyplot as plt
import math

U0 = 1
t1 = 1.8
t2 = 1.8
T = 10
T0 = 0.75 * T
n = 1000


def U(t):
    if t < T0:
        voltage = U0 * (1 - math.exp(-t/t1))
    else:
        voltage = U0 * math.exp(-t/t2)

    return voltage


def integral():

    res_rectangle_left = 0
    res_rectangle_middle = 0
    res_rectangle_right = 0
    res_trapezoid = 0
    res_simpson = 0

    step = T/n
    t = 0

    for i in range(n):
        res_rectangle_left += pow(U(t), 2) * step
        res_rectangle_middle += pow(U(t + step/2), 2) * step
        res_rectangle_right += pow(U(t+step), 2) * step

        res_trapezoid += pow((U(t) + U(t + step))/2, 2) * step
        t += step

    for i in range(n//2):
        x = step * i * 2
        res_simpson += pow(U(x), 2) + 4*pow(U(x+step), 2) + pow(U(x+step*2), 2)
    res_simpson *= step / 3

    return [res_rectangle_left, res_rectangle_middle, res_rectangle_right, res_trapezoid, res_simpson]


theoretical_significance = U0 * 0.7

result = integral()
for i in range(len(result)):
    result[i] = math.sqrt(result[i]/T)

print('Теоретическое значение: ', theoretical_significance)
print('Действующие напряжения полученные методом                       Точность (%)')
res = result[0]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Левых прямоугольников:                    ', '{:<20}'.format(res), accuracy)

res = result[1]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Центральных прямоугольников:              ', '{:<20}'.format(res), accuracy)

res = result[2]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Правых прямоугольников:                   ', '{:<20}'.format(res), accuracy)

res = result[3]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Трапеции:                                 ', '{:<20}'.format(res), accuracy)

res = result[4]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Симпсона (парабол):                       ', '{:<20}'.format(res), accuracy)


time = np.array([(i+1) * T/n for i in range(n)])
voltage = np.array([U(time[i]) for i in range(n)])

plt.scatter(time, voltage)
plt.title('График зависимости напряжения от времени')
plt.show()
