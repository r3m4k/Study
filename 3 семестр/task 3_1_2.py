import math

b = float(input('Введите первый член бесконечно убывающей прогрессии: '))
q = float(input('Введите шаг прогресии (по модулю меньше 1) '))
i = 5 #Точность до 5 знака после запятой
i_10 = pow (10, 5)
sum_pr = 0.0
n = 0
flag = 0
result = b/(1-q)
while not flag:
    sum_pr += b
    b *= q
    n += 1
    if not math.floor((result - sum_pr) * i_10):
        flag = 1
print('Для достижения точности вычисления суммы бесконечно убывающей геометрической')
print(f'прогрессии до {i}-го знака после запятой необходимо {n} членов:')
print(f'Это значение по формуле = {result:.8f}, а расчётом = {sum_pr:.8f}')
