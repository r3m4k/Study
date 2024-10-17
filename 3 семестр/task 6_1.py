import math

R = 8.31 #Универсальная газовая постоянная


def sound_speed_in_gas (temp, molar_mass, num_degrees_of_freedom):
    g = (num_degrees_of_freedom + 2)/num_degrees_of_freedom
    sound_speed = math.sqrt(g*R*temp*1000/molar_mass)
    print (f'Скорость звука в газе равна {sound_speed:.2f} м/с')

flag = input('Для расчёта скорости звука в одноатомном газе введите "1"; в двухатомном газе - "2"; в трёхатомном - "3": ')
temp, molar_mass = input('Введите температуру (К) и молярную массу (г/моль) газа: ').split(' ')
temp = float(temp)
molar_mass = float(molar_mass)

num_degrees_of_freedom = dict({'1': 3, '2': 5, '3': 6})

sound_speed_in_gas(temp, molar_mass, num_degrees_of_freedom[flag])