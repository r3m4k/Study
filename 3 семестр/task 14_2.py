import numpy as np
import matplotlib.pyplot as plt


def rectangle_method(x, y):
    res_left = 0
    res_right = 0
    for i in range(len(x)-1):
        res_left += (x[i+1] - x[i]) * y[i]
        res_right += (x[i+1] - x[i]) * y[i+1]

    return [res_left, res_right]


def trapezoid_method(x, y):
    res = 0
    for i in range(len(x)-1):
        res += (x[i+1] - x[i]) * ((y[i] + y[i+1])/2)

    return res


def x_axis(array):
    res = np.empty(len(array)-2, dtype=np.double)
    for i in range(0, len(array)-2):
        res[i] = array[i+1]
    return res


def acceleration(time, velocity):
    accelerations = np.array([(velocity[i+2] - velocity[i])/(2 * (time[i+2] - time[i])) for i in range(0, len(velocity)-2)])
    # print(len(x_axis(time)), len(accelerations))
    # print(accelerations)
    plt.plot(x_axis(time), accelerations)
    plt.plot(time, velocity)
    plt.title('График зависимости скорости и ускорения частицы от времени')
    plt.show()


# time, velocity = reading_variables(file)
# print(time[0])
# print(len(time))

with open('velosity_vs_t3.txt', 'r') as file:
    data = np.loadtxt(file)
time = np.array([data[i, 0] for i in range(len(data))])
velocity = np.array([data[i, 1] for i in range(len(data))])

theoretical_significance =  5.683084539
print('Путь пройденный частицей, вычесленный методом:')

res = rectangle_method(time, velocity)[0]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Левых прямоугольников:  ', res, f'(точность: {accuracy}%)')

res = rectangle_method(time, velocity)[1]
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Правых прямоугольников: ', res, f'(точность: {accuracy}%)')

res = trapezoid_method(time, velocity)
accuracy = 100 * abs(res / theoretical_significance - 1)
print('Трапеций:               ', res, f'(точность: {accuracy}%)')
print('Теоретическое значение: ', theoretical_significance)
acceleration(time, velocity)
