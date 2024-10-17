import numpy as np
import matplotlib.pyplot as plt
import math


def reading_variables(file_txt):
    time = list()
    velocity = list()
    variable = ''
    flag = False
    counting = 0

    symb = file_txt.read(1)

    while symb:

        if symb.isdigit() or symb == '.':
            flag = True
            variable += symb

        if not (symb.isdigit() or symb == '.') and flag:
            flag = False
            #print(variable)
            if counting:
                velocity.append(variable)
                counting = 0
            else:
                time.append(variable)
                counting = 1
            variable = ''

        symb = file_txt.read(1)

    time = np.array(time, dtype=np.double)
    velocity = np.asarray(velocity, dtype=np.double)
    # data = np.loadtxt(file_txt)

    return [time, velocity]


file = open('magnet-rel_YBCO_lognorm_Nd3968_Nh0_Hm3000_T15.txt', 'r')
time, magnetic_field = reading_variables(file)
file.close()

log_time = np.array([math.log(time[i], math.e) for i in range(len(magnetic_field))])
log_magnetic_field = np.array([math.log(magnetic_field[i], math.e) for i in range(len(magnetic_field))])

# log_time_filter1 = np.where(log_time < 7.5)
# log_magnetic_field_filter1 = np.where(log_time < 7.5, log_magnetic_field)
#

i = 0
while not log_time[i] > 7.5:
    i += 1
filter1_index = i

while not log_time[i] > 8.5:
    i += 1
filter2_index = i

log_time_filter1 = np.empty(filter1_index, dtype=np.double)
for i in range(len(log_time_filter1)):
    log_time_filter1[i] = log_time[i]

log_magnetic_field_filter1 = np.empty(len(log_time_filter1))
for i in range(len(log_time_filter1)):
    log_magnetic_field_filter1[i] = log_magnetic_field[i]


log_time_filter2 = np.empty(len(log_time) - filter2_index, dtype=np.double)
for i in range(len(log_time_filter2)):
    log_time_filter2[i] = log_time[i + filter2_index]

log_magnetic_field_filter2 = np.empty(len(log_time_filter2))
for i in range(len(log_time_filter2)):
    log_magnetic_field_filter2[i] = log_magnetic_field[i + filter2_index]


print(log_time_filter1[0], log_time_filter1[-1], log_magnetic_field_filter1[0], log_magnetic_field_filter1[-1])
print(log_time_filter2[0], log_time_filter2[-1], log_magnetic_field_filter2[0], log_magnetic_field_filter2[-1])

S1 = np.polyfit(log_time_filter1, log_magnetic_field_filter1, 1)[0]
# S2 = np.polyfit(log_time_filter2, log_magnetic_field_filter2, 1)[0]
print('Скорость релаксации на первом участке: ', S1)
# print('Скорость релаксации на втором участке: ', S2)

plt.plot(log_time, log_magnetic_field)
plt.show()
