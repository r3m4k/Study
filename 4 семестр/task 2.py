import numpy as np
import matplotlib.pyplot as plt
import random


def particle_color(value):
    if (value > 0):
        return 'red'
    else:
        return 'blue'


def distance(x, y, X, Y):
    return np.sqrt ((X - x)**2 + (Y - y)**2)


# Вычисление потенциальной энергии для заряда 1 мкКл в поле заряда q
# x, y - положение пробного заряда
# X, Y - положение заряда, в поле которого помещается пробный заряд

def potential_energy(q, x, y, X, Y):
    _distance = distance(x, y, X, Y)
    if (_distance < 0.025):
        res = 0
    else:
        res = pow(10, 3) * q * pow(10, -12) / (4 * np.pi * e0 * distance(x, y, X, Y))

    return res


xlim = 1.
ylim = 1.
n = 100

e0 = 8.85e-12
X, Y = np.meshgrid(np.linspace(0, xlim, n), np.linspace(0, ylim, n))

columns_quantity = 2
row_quantity = 2

fig, ax = plt.subplots(nrows=row_quantity, ncols=columns_quantity)

levels = 200

for nrow in range(0, row_quantity):
    for ncol in range(0, columns_quantity):
        # Определение конфигурации, которая будет изображена на графике ax[ncol][nrow]
        k = random.randint(1, 5)          # Количество точечных зарядов
        max = random.randint(2, 5)        # Верхняя граница диапозона значения заряда в мкКл
        min = random.randint(-5, -2)      # Нижняя граница диапозона значения заряда в мкКл

        coordinate_x = np.empty(k, dtype=np.double)
        coordinate_y = np.empty(k, dtype=np.double)
        particle_charges = np.empty(k, dtype=int)
        F = np.zeros([n, n])

        for i in range (0, k):
            coordinate_x[i] = xlim * random.random()                                      # Координаты k-ого заряда
            coordinate_y[i] = xlim * random.random()
            particle_charges[i] = random.randint(min, max)                                # Величина k-ого заряда
            while not particle_charges[i]:
                particle_charges[i] = random.randint(min, max)                            # Убеждаемся, что она не равна нулю

            for y_index in range(len(Y[0])):
                for x_index in range(len(X[0])):
                   F[x_index, y_index] += potential_energy(particle_charges[i], X[x_index, y_index],
                                                           Y[x_index, y_index], coordinate_x[i], coordinate_y[i])

        ptr = ax[ncol][nrow].contour(X, Y, F, cmap=plt.cm.jet, levels=levels)
        ax[ncol][nrow].set_title(f'Количество зарядов - {k}')
        ax[ncol][nrow].set_xlabel('Координата Х')
        ax[ncol][nrow].set_ylabel('Координата Y')
        plt.colorbar(ptr)


        # Теперь отметим на графике отрицательные заряды синим цветом, а положительные - красным

        particle_colors = np.empty(k, dtype=str)
        for i in range(0, k):
            particle_colors[i] = particle_color(particle_charges[i])

        ax[ncol][nrow].scatter(coordinate_x, coordinate_y, s=0, c=particle_colors, zorder=2)

        # И добавим подписи к каждому заряду с его величиной в мкКл
        for i, txt in enumerate(particle_charges):
            ax[ncol][nrow].annotate (txt, (coordinate_x[i], coordinate_y[i]), fontsize=14, zorder=3)


fig.tight_layout()
plt.suptitle('Потенциальная энергия заряда 1 мкКл в поле других зарядов', fontsize=18)
plt.show()
fig.savefig('task 2.pdf')
