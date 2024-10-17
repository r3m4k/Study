import math
import json


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


with open('config_1.json') as file:
    data = json.load(file)

a = data['a']
n = data['n']

for j in range(len(n)):
    solutions = solution(n[j], a)
    print(f'Первые {n[j]} нули функции f(x) = sin({a} * x)', end='\t')
    for i in solutions:
        print(i, end='\t')
    print()
