import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def energy(x, v):
    global i, j

    if not i:
        a_ = a[j]
        b_ = b[1]
    else:
        a_ = a[1]
        b_ = b[j]

    return m * v**2 / 2 + 0.1 * x**4 - a_ * x**2 + b_ * x


def dxdt(t, yz):
    global i, j

    if not i:
        a_ = a[j]
        b_ = b[1]
    else:
        a_ = a[1]
        b_ = b[j]

    y = yz[0]
    z = yz[1]
    return z, (2 * a_ * y - 0.4 * y - b_) / m


a = [-0.3, -0.2, 0.2, 0.3]
b = [-0.7, -0.5, 0.5, 0.7]
m = 1
max_t = 10
n = 50
x_0 = 1
v_0 = 1

t = np.linspace(0, max_t, n)

fig_x, ax_x = plt.subplots(nrows=1, ncols=2)
fig_v, ax_v = plt.subplots(nrows=1, ncols=2)
fig_e, ax_e = plt.subplots(nrows=1, ncols=2)

plt.rcParams['font.size'] = '16'


for i in range(0, 2):
    for j in range(len(a)):
        sol = solve_ivp(dxdt, t_span=[0, max_t], y0=[x_0, v_0], t_eval=t)
        if not i:      # Если левый график
            ax_x[i].plot(sol.t, sol.y[0], label=f'a={a[j]}', linewidth=2.5)
            ax_x[i].annotate(f'Коэффицент b = {b[-1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

            ax_v[i].plot(sol.t, sol.y[1], label=f'a={a[j]}', linewidth=2.5)
            ax_v[i].annotate(f'Коэффицент b = {b[-1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

            ax_e[i].plot(t, energy(sol.y[1], sol.y[0]), label=f'a={a[j]}', linewidth=2.5)
            ax_e[i].annotate(f'Коэффицент b = {b[-1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

        else:           # Если правый график
            ax_x[i].plot(sol.t, sol.y[0], label=f'b={b[j]}', linewidth=2.5)
            ax_x[i].annotate(f'Коэффицент a = {a[1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

            ax_v[i].plot(sol.t, sol.y[1], label=f'b={b[j]}', linewidth=2.5)
            ax_v[i].annotate(f'Коэффицент a = {a[1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

            ax_e[i].plot(t, energy(sol.y[1], sol.y[0]), label=f'b={b[j]}', linewidth=2.5)
            ax_e[i].annotate(f'Коэффицент a = {a[1]}', xy = (0.1, 0.5), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))


        ax_x[i].set_xlabel('Время', fontsize=14)
        ax_x[i].set_ylabel('Координата', fontsize=14)
        ax_x[i].legend(fontsize=16)

        ax_v[i].set_xlabel('Время', fontsize=14)
        ax_v[i].set_ylabel('Скорость', fontsize=14)
        ax_v[i].legend(fontsize=16)

        ax_e[i].set_xlabel('Время', fontsize=14)
        ax_e[i].set_ylabel('Энергия', fontsize=14)
        ax_e[i].legend(fontsize=16)


fig_x.suptitle(f'Зависимость координаты от времени\nНачальная координата: {x_0}, начальная скорость: {v_0}', fontsize=18)
fig_v.suptitle(f'Зависимость скорости от времени\nНачальная координата: {x_0}, начальная скорость: {v_0}', fontsize=18)
fig_e.suptitle(f'Зависимость энергии от времени\nНачальная координата: {x_0}, начальная скорость: {v_0}', fontsize=18)

plt.show()

fig_x.savefig('task 5_coordinate.pdf')
fig_v.savefig('task 5_velocity.pdf')
fig_e.savefig('task 5_energy.pdf')
