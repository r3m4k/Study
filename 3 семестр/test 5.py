import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = np.random.randint(0, 100, 6)

a_filter = np.where(a < 5)
