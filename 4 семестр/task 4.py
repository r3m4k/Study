import numpy as np
from numpy import linalg as LA


def quant(num):
    res = 9
    if num > 0:
        res += 1
    return res

A = np.matrix([[3., 1., 0.5],
               [1., 5., 1.5],
               [0.5, 1.5, 8.]], dtype=float)

print('Исходная матрица:\n', A)
vals, vecs = np.linalg.eig(A)
print('Собственные значения матрицы A = ', vals)
print('Собственные вектора матрицы A: \n', vecs, end='\n\n')

print('Проверка:\n')

for i in range(0, 3):
    print('Номер собственного значения: ', i+1)
    print(f'Результат применения оператора А к {i}-му столбцу матрицы собственных векторов данного оператора:')
    res = A @ vecs[:,i]

    print(f'{A[0]}   [{vecs[0, i]:.{quant(vecs[0, i])}f}]   {res[0]}')
    print(f'{A[1]} * [{vecs[1, i]:.{quant(vecs[1, i])}f}] = {res[0]}')
    print(f'{A[2]}   [{vecs[2, i]:.{quant(vecs[2, i])}f}]   {res[0]}')
    print('\n')


vector = np.array([2, 3, 5])
reverse = vecs.T
print('Матрица перехода:\n', reverse, end='\n\n')
print(f'Координаты вектора {vector} в базисе собственных векторов: ', LA.inv(reverse) @ vector)
