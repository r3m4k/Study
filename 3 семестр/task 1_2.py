'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math
'''
m = float(input('ввод: m(г) '))
k = float(input('k(кН/м) '))
v = float(input('v_eq (м/с) '))
'''
beggining, rub_m, m, rub_k, k, rub_v, v = input().split(' ')
del beggining, rub_m, rub_k, rub_v

m = float(m)/1000
k = float(k)*1000
v = float (v)

A = math.sqrt((m*pow(v,2))/k)
E = m*pow(v,2)/2

print ('данные о маятнике:  m = ', m, f' кг;  k = {k:.0f} Н/м;  v = {v:.0f} м/с')
print ('обработанные данные:  A = ', A ,'м,  E = ', E, ' кДж')
