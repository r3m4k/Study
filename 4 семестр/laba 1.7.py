import numpy as np


def clearing(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.replace(',', '.')
    print(data)

def analysis(arr):
    print(f'{np.mean(arr):.2f} +-  {np.std(arr):.3f}')

# clearing('laba 1.7.txt')

arr1 = np.array([104.84, 107.54, 108.78, 106.28, 108.38, 107.76, 109.58])
arr2 = np.array([180.16, 180.38, 180.20, 180.36, 180.16, 180.20, 180.08])

data = np.loadtxt('laba 1.7.txt', dtype=np.double, unpack=True)
# print(data)

analysis(arr1)
analysis(arr2)
for i in range(len(data)):
    analysis(data[i])

np.polyfit()
