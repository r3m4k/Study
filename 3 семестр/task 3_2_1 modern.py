import math

# accuracy = int(input('Введите точность (количество знаков после точки): '))
accuarcy = 8
print(f'Точность вычисления - {accuarcy} знаков после запятой')
number_decimal = float(input('Введите неотрицательное число: '))

lenght_integer = int(math.log10(number_decimal) + 1)
lenght_fractional = int(len(str(number_decimal))) - lenght_integer - 1

number_decimal_integer = int(number_decimal)
number_decimal_fractional = number_decimal - number_decimal_integer

if number_decimal_fractional == 0:
    lenght_fractional = 0

number_double = 0.0
if lenght_integer:
    var = 0
    i = 0
    flag = 1
    while (number_decimal_integer != 0):
        var = var * 10 + number_decimal_integer % 2
        if number_decimal_integer % 2 and flag:
            flag = 0
        if flag:
            i += 1
        number_decimal_integer //= 2
    var = var * 10 + number_decimal_integer
    lenght = int(math.log10(var)) + 1
    while lenght:
        number_double = number_double * 10 + var % 10
        var //= 10
        lenght -= 1
    number_double *= pow(10, i)

if lenght_fractional:
    var = 0.0
    i = 1
    number_double_fractional = 0.0
    while i <= accuarcy:
        var = number_decimal_fractional * 2
        number_double_fractional += int(var) * pow(10, -i)
        number_decimal_fractional = round((var - int(var)), lenght_fractional)
        i += 1

    number_double += number_double_fractional
    print(f'Ваше число в двоичной системе счисления: {number_double}')

else:
    print('Ваше число в двоичной системе счисления: ', int(number_double))
