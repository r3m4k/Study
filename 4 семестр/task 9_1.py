import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from pprint import pprint


def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


data = {
    'file_1': {
        'path': './Исходные файлы/magn_current_T50_H200_Nr576.txt',
    },

    'file_2': {
        'path': './Исходные файлы/magn_current_T50_H200_Nr676.txt',
    },

    'file_3': {
        'path': './Исходные файлы/magn_current_T50_H200_Nr900.txt',
    }
}

####################### READING DATA #######################

for i in range(1, len(data) + 1):
    T_index = data[f'file_{i}']['path'].rfind('_T')
    H_index = data[f'file_{i}']['path'].rfind('_H')
    Nr_index = data[f'file_{i}']['path'].rfind('_Nr')
    end_index = data[f'file_{i}']['path'].find('.txt')

    data[f'file_{i}']['T'] = int(data[f'file_{i}']['path'][T_index + 2 : H_index])
    data[f'file_{i}']['H'] = int(data[f'file_{i}']['path'][H_index + 2 :Nr_index])
    data[f'file_{i}']['Nr'] = int(data[f'file_{i}']['path'][Nr_index + 3 : end_index])

    E, j, _ = np.loadtxt(data[f'file_{i}']['path'], dtype=np.double, unpack=True)
    data[f'file_{i}']['E'] = E
    data[f'file_{i}']['j'] = j

pprint(data)
print('\n')

########################## TASK 1 ##########################

plt.rcParams['font.size'] = '16'

fig, ax = plt.subplots()
fig.set_figheight(7.65)
fig.set_figwidth(13.6)

for i in range(len(data)):
    ax.plot(data[f'file_{i + 1}']['E'], data[f'file_{i + 1}']['j'], 'o-', lw = 2.5,
            label=f"H = {data[f'file_{i + 1}']['H']}\nNr = {data[f'file_{i + 1}']['Nr']}")

ax.set_xlabel('Напряжённость поля')
ax.set_ylabel('Плотность тока')
ax.legend()

fig.suptitle(f'Вольт-амперная характеристика высокотемпературного проводника\n'
                f"при T = {data[f'file_{i + 1}']['T']}", fontweight='bold')

# plt.show()
fig.savefig(f'./Графики/task 9/task 9_1.pdf')
plt.close(fig=fig)

########################## TASK 2 ##########################

for i in range(len(data)):
    plt.rcParams['font.size'] = '16'

    fig, ax = plt.subplots()
    fig.set_figheight(7.65)
    fig.set_figwidth(13.6)
    ax.plot(data[f"file_{i+1}"]['E'], data[f"file_{i+1}"]['j'], 'o-', lw = 2.5)

    annotation = 'Значения критического тока, полученные:\n\n'
    
    print(f'Значения критического тока из файла {data[f"file_{i+1}"]["path"]}, полученные:')
    for fit_func in ['linear', 'quadratic', 'cubic']:
        match fit_func:
            case 'linear':
                coef, _ = curve_fit(linear_fit, data[f"file_{i+1}"]["E"], data[f"file_{i+1}"]["j"])
                x = np.linspace(0, data[f"file_{i+1}"]["E"][-1], 2)
                line = coef[0] * x + coef[1]
                ax.plot(x, line, label='Линейная интерполяция', lw=2.5)
                print(f'\tЛинейной интерполяцией:       {coef[0] + coef[1]}')
                
                annotation += f'    Линейной интерполяцией:            {(coef[0] + coef[1]):.5f}\n'

            case 'quadratic':
                coef, _ = curve_fit(quadratic_fit, data[f"file_{i+1}"]["E"], data[f"file_{i+1}"]["j"])
                x = np.linspace(0, data[f"file_{i+1}"]["E"][-1])
                line = coef[0] * x**2 + coef[1] * x + coef[2]
                ax.plot(x, line, label='Квадратичная интерполяция', lw=2.5)
                print(f'\tКвадратичной интерполяцией:   {coef[0] + coef[1] + coef[2]}')
                
                annotation += f'    Квадратичной интерполяцией:     {(coef[0] + coef[1] + coef[2]):.5f}\n'
                
            case 'cubic':
                coef, _ = curve_fit(cubic_fit, data[f"file_{i+1}"]["E"], data[f"file_{i+1}"]["j"])
                x = np.linspace(0, data[f"file_{i+1}"]["E"][-1])
                line = coef[0] * x**3 + coef[1] * x**2 + coef[2] * x + coef[3]
                ax.plot(x, line, label='Кубическая интерполяция', lw=2.5)
                print(f'\tКубической интерполяцией:     {coef[0] + coef[1] + coef[2] + coef[3]}')
            
                annotation += f'    Кубической интерполяцией:         {(coef[0] + coef[1] + coef[2] + coef[3]):.5f}'
    
    ax.annotate(annotation, xy = (0.5, 0.1), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

    
    ax.set_xlabel('Напряжённость поля')
    ax.set_ylabel('Плотность тока')
    ax.legend()

    path = data[f"file_{i+1}"]["path"]
    fig.suptitle(f'Данные из файла {path}', fontweight='bold')
    fig.savefig(f'./Графики/task 9/task 9_2 {path[path.find("m") : path.find(".txt")]}.pdf')

# plt.show()
plt.close('all')
print('\n')

########################## TASK 3 ##########################

for i in range(len(data)):
    start_index = np.where(data[f"file_{i+1}"]["E"] > 1)[0][0]

    plt.rcParams['font.size'] = '16'

    fig, ax = plt.subplots()
    fig.set_figheight(7.65)
    fig.set_figwidth(13.6)

    ax.plot(data[f"file_{i+1}"]['E'][start_index:], data[f"file_{i+1}"]['j'][start_index:], 'o-', lw = 2.5)

    coef, _ = curve_fit(linear_fit, data[f"file_{i+1}"]["E"][start_index:], data[f"file_{i+1}"]["j"][start_index:])

    x = np.linspace(data[f"file_{i+1}"]["E"][start_index], data[f"file_{i+1}"]["E"][-1], 2)
    line = coef[0] * x + coef[1]
    ax.plot(x, line, label='Линейная интерполяция', lw=2.5)

    ax.annotate(f'Критический ток, полученный\nинтерполяцией прямого участка:\n{(coef[0] + coef[1]):.5f}',
                xy = (0.5, 0.1), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))

    print(f'Критический ток, полученный интерполяцией прямого участка из файла '
          f'{data[f"file_{i+1}"]["path"]}:\t{(coef[0] + coef[1])}')

    ax.set_xlabel('Напряжённость поля')
    ax.set_ylabel('Плотность тока')
    ax.legend()

    path = data[f"file_{i+1}"]["path"]
    fig.suptitle(f'Данные из файла {path}', fontweight='bold')
    fig.savefig(f'./Графики/task 9/task 9_3 {path[path.find("m") : path.find(".txt")]}.pdf')


# plt.show()
plt.close('all')

########################## TASK 4 ##########################

for i in range(len(data)):
    # nonzero_index = np.where(data[f"file_{i+1}"]["E"] != 0)[0][0]

    filter = data[f"file_{i+1}"]["E"] > 0
    plt.rcParams['font.size'] = '16'

    annotation = 'Значения критического тока, полученные методом:\n\n'

    fig, ax = plt.subplots()
    fig.set_figheight(7.65)
    fig.set_figwidth(13.6)

    ax.plot(data[f"file_{i+1}"]['E'][filter], data[f"file_{i+1}"]['j'][filter], 'o-', lw = 2.5)

    for kind, label in zip(['linear', 'quadratic', 'cubic'],
                           ['линейная интерполяция', 'квадратичная интерполяция', 'кубическая интерполяция']):
        interp_func = interp1d(data[f"file_{i+1}"]["E"][filter], data[f"file_{i+1}"]["j"][filter])
        x = np.linspace(data[f"file_{i+1}"]["E"][filter][0], data[f"file_{i+1}"]["E"][filter][-1])
        ax.plot(x, interp_func(x), label=label)
        x = np.linspace(0.5, 1.5)
        x_index = np.argmin(abs(x - 1))
        annotation += f'{label}: {interp_func(x)[x_index]}\n'

    ax.annotate(annotation, xy = (0.4, 0.1), xycoords='axes fraction', size=14,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", ec="steelblue", lw=2))
    print(annotation)
    ax.set_xlabel('Напряжённость поля')
    ax.set_ylabel('Плотность тока')
    ax.legend()

    path = data[f"file_{i+1}"]["path"]
    fig.suptitle(f'Аппроксимация ненулевых значений из файла\n{path}', fontweight='bold')
    fig.savefig(f'./Графики/task 9/task 9_4 {path[path.find("m") : path.find(".txt")]}.pdf')

plt.show()
plt.close('all')
