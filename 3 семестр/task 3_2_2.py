import math

number_double = int (input('Введите двоичное число: '))
lenght = int(math.log10(number_double)) + 1
number_decimal = 0
i = 0
while lenght:
    number_decimal += (number_double % 10) * pow(2, i)
    i += 1
    lenght -= 1
    number_double //= 10
print ('Вваше число в десятичной системе счисления: ', number_decimal)