#Вариант 2

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


def double_factorial(n):
    if n > 2:
        return n * double_factorial(n-2)
    else:
        return n


n = int(input('Введите натуральное число: '))

print(f'{n}! = {factorial(n)}, {n}!! = {double_factorial(n)}')
