import math

number_double = input('Введите неотрицательное число в двоичной системе счисления: ')
number_decimal_integer = 0
number_decimal_fractional = 0

number_double_integer = math.floor( float(number_double) )

if number_double_integer:
    lenght_integer = int(math.log10( math.floor(float(number_double)) )) + 1
    lenght_fractional = len(number_double) - lenght_integer - 1
else:
    lenght_integer = 0
    lenght_fractional = len(number_double) - lenght_integer - 2

number_double_fractional = round( (float(number_double) - number_double_integer) * pow(10, lenght_fractional) )

#print(len(number_double), lenght_fractional, number_double_fractional)
if (lenght_fractional<0):
    lenght_fractional = 0

i = 0
while lenght_integer:
    number_decimal_integer += (number_double_integer % 10) * pow(2, i)
    i += 1
    lenght_integer -= 1
    number_double_integer //= 10

i = -1
while lenght_fractional:
    number_decimal_fractional += (number_double_fractional % 10) * pow(2, i)
    i -= 1
    lenght_fractional -= 1
    number_double_fractional //= 10

number_decimal = number_decimal_integer + number_decimal_fractional
print (f'Вваше число в десятичной системе счисления: {number_decimal:.3f}')