import matplotlib.pyplot as plt
import numpy as np


data = [[], [], [], []]
_, angle, data[0], data[1], data[2], data[3] = np.loadtxt('./Исходные файлы/laba 123.txt', unpack=True)

data_mean = np.zeros(len(data[0]))
data_err = np.zeros(len(data[0]))

for i in range(len(data[0])):
    data_mean[i] = (data[0][i] + data[1][i] + data[2][i] + data[3][i]) / 4
    data_err[i] = np.std([data[0][i], data[1][i], data[2][i], data[3][i]])

index_max = np.argmax(data_mean)

for i in range(len(data[0])):
    if data_mean[i] == 0:
        data_err[i] = 0
    else:
        data_err[i] = np.sqrt((data_err[i] / data_mean[i])**2 + (data_err[index_max] / data_mean[index_max])**2)

data_mean = data_mean / data_mean[index_max]

zero_angle = 3

angle = (angle - zero_angle) * np.pi / 180
cos_2 = pow(np.cos(angle), 2)

line = np.polyfit(cos_2, data_mean, 1, cov=True)
k, b = line[0]
dk = line[1][0, 0]
db = line[1][1, 1]

fig, ax = plt.subplots()
plt.rcParams['font.size'] = '16'
fig.set_figheight(8.27)
fig.set_figwidth(11.69)

ax.scatter(cos_2, data_mean)
ax.plot([0, 1], [b, k + b], color='tab:grey', linewidth=2.5)

ax.errorbar(cos_2, data_mean, data_mean * data_err, capsize=4, errorevery=1, linestyle='', ecolor='r',
                 marker='o', markevery=1, ms=7, mfc='none', mec='r')

ax.annotate(f'Доверительная вероятность - 0.7\n'
            f'Коэффиценты прямой:\nk = {k:.3f} (ε = {100 * dk/k:.3f}%)\nb = {b:.3f} (ε = {100 * abs(db/b):.3f}%)',
                xy = (0.1, 0.8), xycoords='axes fraction', size=16,
                    bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

ax.grid()
ax.set_xlabel('$\cos^2($phi$)$', fontsize=16)
ax.set_ylabel('I_0 / I_max', fontsize=16)
fig.suptitle('График зависимости отношения интенсивности к максимальной\n от угла поворота поляризатора $\phi$', fontweight='bold', size=18)


plt.show()
fig.savefig('E:/laba 4.22.pdf')
