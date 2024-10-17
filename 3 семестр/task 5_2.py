import numpy as np
from numpy import linalg as LA
import math

a = np.array([2, 4, 6])
b = np.array([4, 2, 7])
f = np.array([3, 2, 4])

s = np.add(b, -a)
sc_pr = np.dot(s, f)

ang = math.acos(sc_pr/(LA.norm(s) * LA.norm(f))) * 180/math.pi

print(f'Угол между ввектором F = {f} и вектором перемещения S = {s} равен {ang:.2f} градусов')
