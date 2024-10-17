import numpy as np
from numpy import linalg as LA


def Gayss_method(matrix):
    matrix[0] *= 1/matrix[0, 0]
    matrix[1] -= matrix[1, 0] * matrix[0]

    matrix[1] *= 1/matrix[1, 1]
    matrix[0] -= matrix[0, 1] * matrix[1]

    return matrix


def sign(val):
    if val < 0:
        res = ' - '
    else:
        res = ' + '

    return res


def solution(M):
    global b
    rank = LA.matrix_rank(M)
    if (rank == 3):
        # Выведем на экран полученную сиситему
        # {sign(M[j, 1])} {abs(M[j, 1])} нужны чтобы выводилось на экран "-2у", а не что-то типа "+ -2у"
        # Ну и в остальных местах тоже самое
        print('Решение системы: ')
        for j in range(0, 3):
            print(f'{M[j, 0]}x {sign(M[j, 1])} {abs(M[j, 1])}y {sign(M[j, 2])} {abs(M[j, 2])}z = {b[j]}')
        s = LA.solve(M, b)
        print('\nЯвляется:')
        print(f'x = {s[0]}\ny = {s[1]}\nz = {s[2]}', end='\n\n\n')
    elif rank == 2:
        print('Решение системы: ')
        for j in range(0, 3):
            print(f'{M[j, 0]}x {sign(M[j, 1])} {abs(M[j, 1])}y {sign(M[j, 2])} {abs(M[j, 2])}z = {b[j]}')
        matrix = np.vstack((M.T, b))
        matrix = matrix.T
        matrix = np.delete(matrix, (2), axis=0)
        matrix = Gayss_method(matrix)
        print('\nЯвляется (z - параметр):')
        print(f'x = {matrix[0, 3]} {sign(-matrix[0, 2])} {abs(matrix[0, 2])}z')
        print(f'y = {matrix[1, 3]} {sign(-matrix[1, 2])} {abs(matrix[1, 2])}z', end='\n\n\n')
    elif rank == 1:
        print('Решение системы: ')
        for j in range(0, 3):
            print(f'{M[j, 0]}x {sign(M[j, 1])} {abs(M[j, 1])}y {sign(M[j, 2])} {abs(M[j, 2])}z = {b[j]}')
        coef = M[0, 2]
        print('\nЯвляется (параметры: х, y)')
        M /= coef
        b /= coef
        print(f'z = {b[0]} {sign(-M[0, 0])} {abs(M[0, 0])}x {sign(-M[0, 1])} {abs(M[0, 1])}y')


matrix_list = list()

# b = np.array([float(input('Введите параметр а: ')), float(input('Введите параметр b: ')), float(input('Введите параметр с: '))])
b = np.array([1., 2., 3.])
# Создадим различные матрицы для демонстрации всех вариантов

# rank = 3
M = np.matrix([[2, 3, -1],
               [8, -1, 3],
               [-3, 1, -5]], dtype=float)
matrix_list.append(M)

# rank = 2
M = np.matrix([[-3, 1, -5],
               [16, -2, 6],
               [8, -1, 3]], dtype=float)
matrix_list.append(M)

# matrix = np.vstack((M.T, b))
# matrix = matrix.T
# matrix = np.delete(matrix, (2), axis=0)
# print(matrix)
# print(Gayss_method(matrix))

# rank = 1
M = np.matrix([[2, 3, -1],
               [6, 9, -3],
               [-4, -6, 2]], dtype=float)
matrix_list.append(M)

for i in range(len(matrix_list)):
    solution(matrix_list[i])
