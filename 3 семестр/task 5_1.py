import math
import numpy as np
from numpy import linalg as LA

AB = np.ndarray ((1, 3), 'float')

x, y, z = input('Введите координаты вектора через пробел: ').split(' ')
AB[0, 0] = float(x)
AB[0, 1] = float(y)
AB[0, 2] = float(z)

AB = np.mat(AB)
AB = AB.T

ang_ox, ang_oy, ang_oz = input('Введите углы поворота в градусах вокруг осей OX, OY, OZ через пробел: ').split(' ')
ang_ox = float(ang_ox) * math.pi / 180
ang_oy = float(ang_oy) * math.pi / 180
ang_oz = float(ang_oz) * math.pi / 180

matrix_rotation_ox = np.array ([[1, 0, 0], [0, -math.cos(ang_ox), math.sin(ang_ox)], [0, -math.sin(ang_ox), -math.cos(ang_ox)]])
matrix_rotation_ox = np.mat(matrix_rotation_ox)

matrix_rotation_oy = np.array ([[math.cos(ang_oy), 0, math.sin(ang_oy)], [0, 1, 0], [-math.sin(ang_oy), 0, math.cos(ang_oy)]])
matrix_rotation_oy = np.mat(matrix_rotation_oy)

matrix_rotation_oz = np.array ([[math.cos(ang_oz), -math.sin(ang_oz), 0], [math.sin(ang_oz), math.cos(ang_oz), 0], [0, 0, 1]])
matrix_rotation_oz = np.mat(matrix_rotation_oz)

#print(type(matrix_rotation_ox), type(matrix_rotation_oy), type(matrix_rotation_oz))
print()

AB_rotation_ox = matrix_rotation_ox * AB
print('Результат поворота вектора вокруг оси OX: ', AB_rotation_ox.T)

AB_rotation_oy = matrix_rotation_oy * AB
print('Результат поворота вектора вокруг оси OY: ', AB_rotation_oy.T)

AB_rotation_oz = matrix_rotation_oz * AB
print('Результат поворота вектора вокруг оси OZ: ', AB_rotation_oz.T)
print ()
#Демонстрация некомутативности преобразований поворота

example1 = matrix_rotation_ox * AB
example1 = matrix_rotation_oy * example1
example1 = matrix_rotation_oz * example1

print('Вектор, полученный вращением вокруг OX, OY, OZ: ', example1.T)

example2 = matrix_rotation_oy * AB
example2 = matrix_rotation_oz * example2
example2 = matrix_rotation_ox * example2

print('Вектор, полученный вращением вокруг OY, OZ, OX: ', example2.T)

example3 = matrix_rotation_oz * AB
example3 = matrix_rotation_ox * example3
example3 = matrix_rotation_oy * example3

print('Вектор, полученный вращением вокруг OZ, OX, OY: ', example3.T)