import numpy as np
import matplotlib.pyplot as plt


def p(v, t):
    return gas_const * t / (v * 101325)


gas_const = 8.31
volume, p500, p300, p100 = np.loadtxt("isotherms.txt", dtype=np.double, skiprows=1, unpack=True)
volume /= 1000

pressure = [p100, p300, p500]
pressure = np.asarray(pressure)
temp = [100, 300, 500]

fig, ax = plt.subplots()
ax.grid()
fig.set_figheight(15)
fig.set_figwidth(25)

plt.rcParams['font.size'] = '18'

# theoretical_pressure = list()
theoretical_line_color = ['tab:blue', 'tab:green', 'tab:olive']
theoretical_volumes = np.linspace(volume[0], volume[-1], 100)

for i in range(0, 3):
    pressure[i] += pressure[i] * (1 - 2 * np.random.rand(len(volume))) * 0.02
    errors = np.random.rand(len(volume)) * pressure[i] * 0.1

    theoretical_pressure = p(theoretical_volumes, temp[i])
    ax.plot(theoretical_volumes, theoretical_pressure, linewidth=2, color=theoretical_line_color[i],
            linestyle='--', label=f'теоретическое значение при T={temp[i]}')

    ax.errorbar(volume, pressure[i], errors, capsize=6, errorevery=1, linestyle='', ecolor='r',
                marker='o', markevery=1, markersize=6, markerfacecolor='none', markeredgecolor='r')


ax.set_xlabel('Объём, л', fontsize=16)
ax.set_ylabel('Давление, атм', fontsize=16)
ax.legend(loc='upper right')
plt.suptitle('Зависимость давления одного моля идеального газа\n от его объёма')
plt.show()
fig.savefig('task 1.pdf')
