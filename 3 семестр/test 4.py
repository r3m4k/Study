n = 150


def factorial(n):
    res = 1
    if n:
        for i in range(1, n+1):
            res *= i

    return res


def double_factorial(n):
    res = 1
    if n % 2:
        x = 1
        for i in range(n//2 + 1):
            res *= x
            x += 2
    else:
        x = 2
        for i in range(n//2 + 1):
            res *= x
            x += 2

    return res


n = 50
number = (double_factorial(2*n-1)/(2*n+1)*pow(2, n)*factorial(n))
print(number)
