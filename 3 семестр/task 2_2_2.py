flag = 1
n, m = input('Введите диапозон через пробел:\t').split(' ')
print ('Простые числа из данного диапозона: ', end='')
n = int(n)
m = int (m)
for number in range (n, m+1):
    if (number == 0) or (number == 1):
        flag = 0
    if flag:
        for i in range (2, abs(number)):
            if abs(number) % i == 0:
                flag = 0
                break
    if flag:
        print (number, end=' ')

    if (number % 10 == 0):
        print('')

    flag = 1