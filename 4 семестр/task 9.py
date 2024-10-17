import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from pprint import pprint


def text_label(index):
        # Функция вернёт значения характеристик, по которым группировка не проводится

        flag = 0
        result = ''
        for key in df.keys():
                if key != char_group:
                        result += f'{key} = {df[key]["file_data"][index]}'
                if flag:
                        result += '\n'
                flag += 1

        return result


def group_indexes():
        df[char_group]['unique'] = np.unique(df[char_group]['file_data'])
        result = list()
        for i in range(len(df[char_group]['unique'])):

                result.append(list())
                for j in range(len(df[char_group]['file_data'])):

                        # Если df[flag]['file_data'][j] равно df[flag]['unique'][i], то добавим
                        # индекс этого элемента в список result[i]
                        if df[char_group]['file_data'][j] == df[char_group]['unique'][i]:
                                result[i].append(j)

        df[char_group]['group_indexes'] = result
        pprint(df)


files = ['./Исходные файлы/magn_current_T50_H200_Nr576.txt',
        './Исходные файлы/magn_current_T50_H200_Nr676.txt',
        './Исходные файлы/magn_current_T50_H200_Nr900.txt',
        './Исходные файлы/magn_current_T77_H0_Nr576.txt',
        './Исходные файлы/magn_current_T77_H0_Nr676.txt',
        './Исходные файлы/magn_current_T77_H200_Nr576.txt',
        './Исходные файлы/magn_current_T77_H200_Nr676.txt']

data = {}

df = {
        'T': {'file_data': list()},
        'H': {'file_data': list()},
        'Nr': {'file_data': list()}
}

# Выделим из названия файлов данные об температуре, величине магнитного поля и деффектах и запишем в словарь
for file in files:
        T_index = file.rfind('_T')
        H_index = file.rfind('_H')
        Nr_index = file.rfind('_Nr')
        end_index = file.find('.txt')

        df['T']['file_data'].append(int(file[T_index + 2 : H_index]))
        df['H']['file_data'].append(int(file[H_index + 2 :Nr_index]))
        df['Nr']['file_data'].append(int(file[Nr_index + 3 : end_index]))

for i in range(len(files)):
        E, j, _ = np.loadtxt(files[i], dtype=np.double, unpack=True)
        data[f'file_{i}'] = {'E': E, 'j' : j}

# pprint(data)
print()

char_group = 'T'        # Характеристика по которой будем группировать

group_indexes()

# Выведем ВАХ, группируя по char_group

plt.rcParams['font.size'] = '16'

for i in range(len(df[char_group]['unique'])):

        fig, ax = plt.subplots()
        fig.set_figheight(7.65)
        fig.set_figwidth(13.6)

        for file_num in df[char_group]['group_indexes'][i]:
                ax.plot(data[f'file_{file_num}']['E'], data[f'file_{file_num}']['j'], 'o-', lw = 2.5, label=text_label(file_num))

        ax.set_xlabel('Напряжённость поля')
        ax.set_ylabel('Плотность тока')
        ax.legend()

        fig.suptitle(f'Вольт-амперная характеристика высокотемпературного проводника\n'
                f'при {char_group} = {df[char_group]["unique"][i]}')
        fig.savefig(f'./Графики/task 9_{char_group}_unique_[{i}].pdf')

# Уберём нулевые значения

for i in range(len(files)):
        E, j, _ = np.loadtxt(files[i], dtype=np.double, unpack=True)
        E_cleared = list()
        j_cleared = list()

        for n in range(len(E)):
                if n == 0:
                        E_cleared.append(E[n])
                        j_cleared.append(j[n])
                else:
                        if E[n] != 0:
                                E_cleared.append(E[n])
                                j_cleared.append(j[n])

        data[f'file_{i}']['E_cleared'] = np.asarray(E_cleared)
        data[f'file_{i}']['j_cleared'] = np.asarray(j_cleared)


pprint(data)

# Найдём критический ток с помощью интерполяции

kinds = ['linear', 'quadratic', 'cubic']

print(f'Величины критического тока при {char_group} = {df[char_group]["unique"][0]}:')

fig, ax = plt.subplots(1, len(df[char_group]['group_indexes'][0]))
fig.set_figheight(7.65)
fig.set_figwidth(13.6)

for file_num in df[char_group]['group_indexes'][0]:
        print('Имя файла: ', files[file_num])
        print('Способ интерполяции:')
        for kind in kinds:
                interp_func = interp1d(data[f'file_{file_num}']['E_cleared'], data[f'file_{file_num}']['j_cleared'], kind=kind)
                print('\t', '{0: <16}'.format(kind, ':'), interp_func(1))

        # interp_func = interp1d(data[f'file_{file_num}']['E'], data[f'file_{file_num}']['j'], kind='quadratic')
        # print('\t', '{0: <16}'.format('quadratic:'), interp_func(1))
        print()
