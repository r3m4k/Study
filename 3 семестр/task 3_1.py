a_0 = float(input ('Введите первый член прогресии: '))
d, q = input ('Шаг арифметической и геометрической прогрессий через пробел:\n').split(' ')
d = float(d)
q = float(q)
n = int(input('Количество членов последовательностей: '))
sum_arith_progession = 0.0
sum_geometric_progression = 0.0
a = a_0
b = a_0

for i in range (n):
    sum_arith_progession += a
    a += d
print (f'Сумма n членов арифметической прогрессии: {sum_arith_progession:.8f}')
print (f'Сумма n членов арифметической прогрессии по формуле: {(2*a_0+d*(n-1))*n/2:.8f}\n\n')

for i in range (n):
    sum_geometric_progression += b
    b *= q
print (f'Сумма n членов геометрической прогрессии: {sum_geometric_progression:.8f}')
print (f'Сумма n членов геометрической прогрессиипо формуле: {a_0*(pow(q, n)-1)/(q-1):.8f}')