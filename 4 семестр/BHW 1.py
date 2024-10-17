import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp


l = 1                   # длина маятника
phi_0 = np.pi / 4       # начальное отклонение
end_time = 3            # время анимации
fps = 25                # количевство кадров в секунду
g = 9.81                # ускорение свободного падения

time = np.linspace(0, end_time, end_time * fps)

def f(t, phi_q):
    phi = phi_q[0]
    q = phi_q[1]

    return [q, -np.sin(phi) * g / l ]

phi = solve_ivp(f, t_span=[0, end_time], y0=[phi_0, 0], t_eval=time).y[0]

x = l * np.sin(phi)
y = -l * np.cos(phi)

fig, ax = plt.subplots()

# Setting limits for x and y axis
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 0.5)

line,  = ax.plot(0, 0)
scat = ax.scatter(x[0], y[0], color="red", s=100)
dot = ax.scatter(0, 0, color="red", s=100)
line_1, = ax.plot([0, 0], [x[0], y[0]])

# line = ax.plt([0, 0], [x[0], y[0]], color="red")

def animation_function(i):
    data = np.stack([x[int(i)], y[int(i)]])
    scat.set_offsets(data)      # расположение маятник

    dot.set_offsets(np.stack([0, 0]))   # точка подвеса

    line_1.set_xdata([0, x[int(i)]])
    line_1.set_ydata([0, y[int(i)]])

    line.set_xdata(x[:int(i)])
    line.set_ydata(y[:int(i)])

    return scat, line, dot, line_1


animation = FuncAnimation(fig,
                          func = animation_function,
                          frames = np.linspace(0, len(phi) - 1, len(phi)),
                          interval = 1000 / fps)
plt.show()
