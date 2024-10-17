import math

gas_const = 8.31

def sound_in_gas (j, M):
    return round(math.sqrt((j * gas_const * 293)/(M / 1000)), 3)

def quant_of_heat (Cv):
    return round((Cv/gas_const + 1) * 100000 * 0.25 * 0.001, 3)


file = open('gases.csv', 'w')

res = '{:<50}'.format(' ')
file.write(res)
gases = ['He', 'H2', 'O2', 'CO2', 'H2O']
for i in range(len(gases)):
    res = '{:<15}'.format(gases[i])
    file.write(res)
file.write('\n')

molar_mass = [4, 2, 32, 44, 18]
res = '{:<50}'.format('Молярная масса газа (г/моль): ')
file.write(res)
for i in range(len(gases)):
    res = '{:<15}'.format(molar_mass[i])
    file.write(res)
file.write('\n')

res = 'Показатель адиабаты при 20°: '
file.write('{:<50}'.format(res))
adiabats = [1.410, 1.660, 1.400, 1.300, 1.330]
for i in range(len(gases)):
    res = '{:<15}'.format(adiabats[i])
    file.write(res)
file.write('\n')

res = 'Скорость звука в газе при 20°: '
file.write('{:<50}'.format(res))
sound_speed = [0, 0, 0, 0, 0]
for i in range(len(gases)):
    sound_speed[i] = sound_in_gas(adiabats[i], molar_mass[i])
for i in range(len(gases)):
    res = '{:<15}'.format(sound_speed[i])
    file.write(res)
file.write('\n')

res = 'Теплоемкость при постоянном объеме (Дж/кг): '
file.write('{:<50}'.format(res))
heat_capacity = [round((gas_const/(i-1)), 3) for i in adiabats]
for i in range(len(gases)):
    res = '{:<15}'.format(heat_capacity[i])
    file.write(res)
file.write('\n')

res = 'Количество теплоты (*) (Дж): '
file.write('{:<50}'.format(res))
heat = [0, 0, 0, 0, 0]
for i in range(len(gases)):
    heat[i] = quant_of_heat(heat_capacity[i])
for i in range(len(gases)):
    res = '{:<15}'.format(heat[i])
    file.write(res)
file.write('\n')

file.write('\n\n(*) – количество теплоты, которое выделится/поглотится при изобарном сжатии 1 л газа на 25% при атмосферном давлении')

file.close()
