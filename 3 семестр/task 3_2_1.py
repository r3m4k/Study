import math


number_decimal = float(input('Введите натуральное десятичное число: '))
if not(number_decimal % math.floor(number_decimal)):
    number_decimal = int (number_decimal)
    number_double = 0
    var = 0
    i = 0
    flag = 1
    while (number_decimal != 0):
        var = var*10 + number_decimal % 2
        if number_decimal % 2 and flag:
            flag = 0
        if flag:
            i += 1
        number_decimal //=2
    var = var*10 + number_decimal
    length = int(math.log10(var)) + 1
    while length:
        number_double = number_double * 10 + var % 10
        var //= 10
        length -= 1
    number_double *= pow (10, i)
    print ('Ваше число в двоичной системе счисление: ', number_double)
else:
    print ('Неправилный ввод')