import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


M_0 = 2.77 * 1e6 # kg
R = 13600        # kg/s
m_0 = 2.04 * 1e6 # kg
T = 150          # s
v_ex = 2456      # m/s
n = 150
frame_time = T / n
g = 9.81         # m/s^2
tau = 256        # s


def f(t, vm):
    v = vm[0]
    m = vm[1]

    return v_ex * R / m, -R


def integration(array, lenght):
    int_arr = np.empty(lenght - 1, dtype=np.double)
    sym = 0
    for i in range(lenght - 1):
        sym += frame_time * (array[i] + array[i+1])/2
        int_arr[i] = sym
    return int_arr


time = np.linspace(0, T, n)

sol = solve_ivp(f, t_span=[0, T], y0=[0, M_0], method = 'BDF', t_eval=time)

fig_m, ax_m = plt.subplots()
fig_x, ax_x = plt.subplots()
fig_v, ax_v = plt.subplots()
fig_a, ax_a = plt.subplots()

acceleration = np.diff(sol.y[0])
for i in range(0, n-1):
    acceleration[i] /= time[i+1] - time[i]

distance = integration(sol.y[0], T)
velocity = sol.y[0]


ax_v.plot(time, velocity, label='без учёта g', linewidth=2)
ax_x.plot(time[:-1], distance / 1000, label='без учёта g', linewidth=2)
ax_a.plot(time[:-1], acceleration, label='без учёта g', linewidth=2)
ax_m.plot(time, sol.y[1] * 1e-6)


for i in range(0, n-1):
    cor = g * np.cos( (np.pi * time[i]) / (2 * tau) )
    acceleration[i] -= cor
    velocity[i] -= cor * time[i]
    distance[i] -= cor * time[i]**2 / 2

velocity[-1] -= cor * time[-1]

ax_v.plot(time, velocity, label='с учётом g', linewidth=2)
ax_x.plot(time[:-1], distance / 1000, label='с учётом g', linewidth=2)
ax_a.plot(time[:-1], acceleration, label='с учётом g', linewidth=2)


fig_x.suptitle('Моделирование старта ракеты Сатурн-V')
ax_x.set_xlabel('Время, с', fontsize=14)
ax_x.set_ylabel('Пройденный путь, км', fontsize=14)
ax_x.legend(fontsize=16)

fig_v.suptitle('Моделирование старта ракеты Сатурн-V')
ax_v.set_xlabel('Время', fontsize=14)
ax_v.set_ylabel('Скорость', fontsize=14)
ax_v.legend(fontsize=16)

fig_a.suptitle('Моделирование старта ракеты Сатурн-V')
ax_a.set_xlabel('Время', fontsize=14)
ax_a.set_ylabel('Ускорение', fontsize=14)
ax_a.legend(fontsize=16)

fig_m.suptitle('Зависимость массы ракеты от времени движения')
ax_m.set_xlabel('Время, с', fontsize=14)
ax_m.set_ylabel('Масса, 1e6 кг', fontsize=14)

fig, ax = plt.subplots()
ax.plot(sol.y[0], sol.y[1] * 1e-6)
ax.set_xlabel('Скорость, м/с', fontsize=14)
ax.set_ylabel('Масса, 1е6 кг', fontsize=14)
fig.suptitle('Зависимость массы ракеты от времени движения')

plt.show()
