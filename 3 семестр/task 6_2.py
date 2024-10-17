import math


def oscillation_period (natural_oscillation, attenual = 0):
    if natural_oscillation < attenual:
        print('Период затухающих колебаний равен бесконечности (апериодический процесс)')
    else:
        period = (2*math.pi)/math.sqrt(pow(natural_oscillation, 2) - pow(attenual, 2))
        if not attenual:
            print (f'Период незатухающих колебания равен: {period:.8f} c')
        else:
            print(f'Период затухающтих колебания равен: {period:.8f} c')

w, b = input('Введите собственную частоту колебаний и частоту затухания (Гц) через пробел: ').split(' ')
w = float(w)
b = float(b)

oscillation_period(w)
oscillation_period(w, b)