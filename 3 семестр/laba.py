import math
import numpy as np


a = np.array([
        [2.9, -0.6],
        [3.0, -0.8],
        [3.0, -1.0],
        [3.0, -1.2],
        [3.0, -1.4]
        ])

val = 0.5/30

def func (a, b):
    res = math.log((a + 1.8)/(b+1.8))
    delta = abs(math.log((a + 1.9)/(b+1.7)) - res)
    print(f'{res:.2f} --> {delta:.2f} ({(100*delta/res):0.2f}%)')
    print (f'\t{res/val:.0f} --> {delta/val:.0f}')


for i in range(len(a)):
    func(*a[i])