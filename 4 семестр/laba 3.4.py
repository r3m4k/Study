import numpy as np
import matplotlib.pyplot as plt


############# Задание 1 #############


def min_to_degree(degree_min):
    min = int(degree_min[degree_min.find('g') + 2 : degree_min.find('m')])
    sec = int(degree_min[degree_min.find('m') + 2 : degree_min.find('s')])
    degree = int(degree_min[: degree_min.find('g')])

    return degree + (min / 60) + (sec / 3600)


def phi_k(num, sec):
    degree_min = alfa_k[num][1]
    min = int(degree_min[degree_min.find('g') + 2 : degree_min.find('m')])
    degree = int(degree_min[: degree_min.find('g')])

    return abs(degree + (min / 60) + (sec / 3600) - alfa_0)


def sec_from_data():
    for j in range(len(alfa_k)):
        seconds = np.zeros(3)
        for i in range(0, 3):
            data = alfa_k[j][i]
            seconds[i] = int(data[data.find('m ') + 2 : data.find('s')])
        phi[j] = phi_k(j, np.mean(seconds))
        d[j] = (abs(k[j]) * l / np.sin( np.pi * phi_k(j, np.mean(seconds)) / 180 )) * 1e6
        print(f'k = {k[j]}     a = ({np.mean(seconds):.2f} +- {np.std(seconds):.2f})"      phi = {phi[j]}')


# l = 546.073e-9
# k = [-1, -2, -3, -4, -5, -6, -7, -8, 1, 2, 3, 4, 5, 6, 7 , 8]
# n = len(k)
#
# phi = np.zeros(n)
# d = np.zeros(n)
# alfa_0 = '92g 0m 32s'
# alfa_0 = min_to_degree(alfa_0)
#
# alfa_k = [
#             ['98g 6m 48s', '98g 6m 46s', '98g 6m 48s'],
#             ['104g 37m 34s', '104g 37m 31s', '104g 37m 33s'],
#             ['111g 7m 59s', '111g 8m 1s', '111g 8m 0s'],
#             ['117g 54m 32s', '117g 54m 39s', '117g 54m 36s'],
#             ['125g 6m 2s', '125g 6m 8s', '125g 6m 6s'],
#             ['132g 56m 33s', '132g 56m 31s', '132g 56m 35s'],
#             ['141g 51m 29s', '141g 51m 27s', '141g 51m 23s'],
#             ['152g 52m 37s', '152g 52m 39s', '152g 52m 37s'],
#
#             ['85g 44m 21s', '85g 44m 24s', '85g 44m 21s'],
#             ['79g 23m 32s', '79g 23m 34s', '79g 23m 30s'],
#             ['72g 53m 0s', '72g 52m 57s', '72g 52m 59s'],
#             ['66g 6m 10s', '66g 6m 16s', '66g 6m 9s'],
#             ['58g 54m 28s', '58g 54m 21s', '58g 54m 26s'],
#             ['51g 3m 38s', '51g 3m 39s', '51g 3m 38s'],
#             ['42g 8m 7s', '42g 8m 5s', '42g 8m 9s'],
#             ['31g 5m 34s', '31g 5m 34s', '31g 5m 39s']
#          ]
#
# sec_from_data()
# print()
#
# def d_error():
#     error = 0
#     d_err = np.zeros(n)
#     for i in range(0, n):
#         d_err[i] = abs(max((abs(k[i]) * l / np.sin( np.pi * (phi[i] + 0.083) / 180 )) * 1e6,
#                        (abs(k[i]) * l / np.sin( np.pi * (phi[i] - 0.083) / 180 )) * 1e6) - d[i])
#         print(f'k = {k[i]}      d = {d[i]:.3f} +- {d_err[i]:.3f}')
#         error += d_err[i]**2
#
#     error = np.sqrt(error) / n
#
#     print(f'\nИтог: d = {np.mean(d)} +- {error} std = {np.std(d)}')
#
#
# d_error()

############# Задание 2 #############


def minutes(degree_min):
    min = int(degree_min[degree_min.find('g') + 2 : degree_min.find('m')])
    sec = int(degree_min[degree_min.find('m') + 2 : degree_min.find('s')])
    degree = int(degree_min[: degree_min.find('g')])

    return degree * 60 + min + sec * 100 / 60

delta_phi = ['0g 1m 27s',
             '0g 3m 3s',
             '0g 4m 39s',
             '0g 6m 38s',
             '0g 8m 54s',
             '0g 11m 54s',
             '0g 17m 21s']

for i in range(0, 7):
    delta_phi[i] = min_to_degree(delta_phi[i])


phi = ['6g 37m 35s',
       '13g 20m 28s',
       '20g 15m 3s',
       '27g 29m 2s',
       '35g 13m 48s',
       '43g 48m 20s',
       '53g 51m 20s']

for i in range(0, 7):
    phi[i] = min_to_degree(phi[i])


l = 576.966       # нм
delta_l = 2.1      # нм

D = np.array([delta_phi[i] * np.pi / (180 * delta_l) for i in range(0, 7)])

phi_theoretical = np.linspace(phi[0], phi[-1])
D_theoretical = np.array([np.tan(phi_theoretical[i] * np.pi / 180) / l for i in range(len(phi_theoretical))])


fig, ax = plt.subplots()
plt.rcParams['font.size'] = '16'
fig.set_figheight(8.27)
fig.set_figwidth(11.69)

for i in range(0, 7):
    print(f'{-i - 1}        D = {D[i] * 180 * 60 / np.pi:.3f}      D_theoretical = {1.08e4 * D_theoretical[i] / np.pi:.3f}')


ax.scatter(np.array([phi[i] for i in range(0, 7)]), D * 180 * 60 / np.pi, label='Экспериментальные значения')
# ax.errorbar(np.array([phi[i] for i in range(0, 7)]), D, D_err,
#             capsize=4, errorevery=1, linestyle='', ecolor='r',
#             marker='o', markevery=1, ms=7, mfc='none', mec='r', label='error')

ax.plot(np.array([phi_theoretical[i] for i in range(len(phi_theoretical))]), 1.08e4 * D_theoretical / np.pi,
        linestyle='--', label='Теоретические значения')
ax.legend()
ax.grid()
ax.set_xlabel('Угол дифракции $\phi$, градусы', fontsize=16)
ax.set_ylabel('D, угл.мин/нм', fontsize=16)
fig.suptitle('График зависимости угловой дисперсии от угла дифракции $\phi$', fontweight='bold', size=18)

# plt.show()

# fig.savefig('./Графики/laba 3.4.pdf')
