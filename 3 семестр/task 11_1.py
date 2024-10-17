import numpy as np
import matplotlib.pyplot as plt


class Overtone:
    def __init__(self, E, rho, L, n):
        self.E = E
        self.rho = rho
        self.L = L
        self.n = n

    def frequency(self):
        return self.n ** 2 * np.sqrt(self.E / self.rho) / (2 * self.L)

    def displacement_profile(self, x):
        return np.sin(self.n * np.pi * x / self.L)

    def plot(self):
        x_values = np.linspace(0, self.L, 1000)
        y_values = self.displacement_profile(x_values)
        plt.plot(x_values, y_values, label=f'Овертон {self.n}')
        plt.xlabel('Положение вдоль стержня (м)')
        plt.ylabel('Перемещение')
        for i in range(1, 2):
            next_n = self.n + i
            y_values = self.displacement_profile(x_values) * np.sin(next_n * np.pi * x_values / self.L)
            plt.plot(x_values, y_values, label=f'Овертон {next_n}')
        plt.legend()
        plt.show()


o = Overtone(2.06e11, 1000.0, 7.0, 2)
print('Частота колебаний:', o.frequency())
o.plot()
