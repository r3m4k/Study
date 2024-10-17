import math


class solution:

    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.__value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__value >= self.n:
            raise StopIteration
        self.__value += 1
        return self.__value * math.pi / self.a


a = float(input('Введите а: '))
n = int(input('Введите количество положительных решений уравнения y=sin(a * x): '))
solutions = solution(n, a)
for i in solutions:
    print(i)



