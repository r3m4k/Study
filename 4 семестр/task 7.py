import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

gamma = 0.8
alpha = 0.2
H_eff = np.array([0, 0, 1])


def f(t, m):
    return -gamma * np.cross(m, H_eff) + alpha * np.cross(m, np.gradient(m))
    # return -gamma * np.cross(m, H_eff)



m0 = np.array([1, 0, 0])
time = np.linspace(0, 20, 1000)

sol = solve_ivp(f, [0, 10], m0, t_eval=time)

fig, ax = plt.subplots()
x_coord = sol.y[0]
y_coord = sol.y[1]
z_coord = sol.y[2]
sq = np.empty(1000)

for i in range(0, 1000):
    sq[i] = np.sqrt(x_coord[i]**2 + y_coord[i]**2 + z_coord[i]**2)

ax.plot(sol.t, sol.y[0], label='x компонента')
ax.plot(sol.t, sol.y[1], label='y компонента')
ax.plot(sol.t, sol.y[2], label='z компонента')
ax.plot(time, sq)
ax.set_xlabel('Время')
ax.set_ylabel('Намагниченность')
ax.legend()
fig.suptitle('Зависимость намагниченности от времени')

plt.show()
