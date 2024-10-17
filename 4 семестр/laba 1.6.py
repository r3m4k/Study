import matplotlib.pyplot as plt
import numpy as np


def print_array(arr):
    for i in range(len(arr)):
        print(f'{arr[i]:.2f}')
    print('\n\n')

def err_koef(voltage):
        if voltage < 20:
                U_k = 20
        else:
                U_k = 200

        return U_k

######### Task 1 #########

def task1():
    angle = np.array([i * 5 for i in range(0, 30)])
    voltage = np.array([81.8, 89.3, 94.7, 99.5, 102.4, 104.2, 106.1, 106.9, 106.5, 105.8, 103.4, 98.6, 92.3, 84.3, 74.5,
                        65.0, 54.6, 46.0, 36.8, 26.9, 19.7, 12.3, 6.6, 3.2, 1.2, 1.0, 2.5, 5.8, 10.7, 17.9])

    U_0 = max(voltage)

    voltage /= U_0
    phi_0 = 35
    angle -= phi_0
    cos_2 = np.array([np.cos(angle[i] * 2 * np.pi / 360)**2 for i in range(0, 30)])


    # print('Cos^2(phi - phi0):\n')
    # print_array(cos_2)

    # print('U(phi)/U(0):\n')
    # print_array(voltage)

    volt_err = np.array([0.04 + 0.02 * voltage[i] / err_koef(voltage[i]) for i in range(0, 30)])

    fig, ax = plt.subplots()
    plt.rcParams['font.size'] = '16'
    fig.set_figheight(8.27)
    fig.set_figwidth(11.69)

    line = np.polyfit(cos_2, voltage, 1, cov=True)
    k, b = line[0]
    dk = line[1][0, 0]
    db = line[1][1, 1]
    print(f'{k} +- {dk}\n{b} +- {db}')
    ax.errorbar(cos_2, voltage, volt_err, capsize=4, errorevery=1, linestyle='', ecolor='r',
                 marker='o', markevery=1, ms=7, mfc='none', mec='r', label='error')
    ax.plot([0, 1], [b, k + b], color='tab:blue', linewidth=2.5)
    ax.annotate(f'Коэффиценты прямой:\nk = {k:.3f} (ε = {100 * dk/k:.3f}%)\nb = {b:.3f} (ε = {100 * db/b:.3f}%)',
                xy = (0.1, 0.8), xycoords='axes fraction', size=16,
                    bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

    ax.grid()
    ax.set_xlabel('cos^2(phi - phi0)', fontsize=16)
    ax.set_ylabel('U(phi)/U(0)', fontsize=16)
    fig.suptitle('График зависимости отношения U(phi)/U(0)\nот квадрата косинуса угла поворота')
    plt.show()
    fig.savefig('laba 1.6_task1.pdf')


######### Task 2 #########

def task2():
    data = [[1.9, 2.0, 2.0, 2.1, 2.1],
            [1.9, 1.8, 1.8, 1.8, 1.9],
            [1.9, 1.8, 1.8, 1.9, 1.9],
            [4.1, 4.1, 3.9, 3.8, 3.8],
            [3.4, 3.4, 3.3, 3.3, 3.3],
            [2.7, 2.5, 2.5, 2.6, 2.5],
            [21.9, 21.7, 21.8, 21.7, 22.0],
            [47.3, 44.7, 39.4, 47.6, 40.0],
            [47.3, 44.7, 39.4, 47.6, 40.0],
            [47.8, 47.6, 46.9, 47.1, 47.4],
            [92.3, 92.6, 89.5, 86.0, 91.6],
            [132.3, 133.8, 133.8, 134.4, 135.5]]

    teta = np.array([i * 5 for i in range(18, 7, -1)])

    koef = 0.9 / 21.82
    for i in range(6, 11):
        for j in range(0, 5):
            data[i][j] *= koef

    y_coords = list()
    U_0 = np.mean([data[0][i] for i in range(0, 5)])
    for i in range (0, 11):
        y_coords.append(np.mean(data[i]))
        # print(f'{teta[i]} --> {y_coords[i]:.3f} +-  {np.std(data[i]):.3f}', end='\t\t')
        # y_coords[i] /= U_0
        # print(f'{y_coords[i]:.2f}')

    fig, ax = plt.subplots()
    plt.rcParams['font.size'] = '16'
    fig.set_figheight(8.27)
    fig.set_figwidth(11.69)
    ax.errorbar(teta, y_coords / U_0, np.array([0.04 + 0.02 * y_coords[i] / err_koef(y_coords[i]) for i in range(0, 11)]), capsize=4, errorevery=1, linestyle='', ecolor='r',
                 marker='x', markevery=1, ms=7, mfc='none', mec='r', label='error')
    ax.grid()
    ax.set_xlabel('Угол падения', fontsize=16)
    ax.set_ylabel('Коэффицент отражения R⊥', fontsize=16)
    fig.suptitle('График зависимости коэффицента отражения\nот угла падения')
    plt.show()
    fig.savefig('laba 1.6_task2.pdf')


task1()
