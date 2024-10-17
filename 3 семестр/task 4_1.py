import  math

# ВАРИАНТ 2

a = [2, 4, 6]
b = [4, 2, 7]

'''

#Без использования функционала numpy
res = [0]*3
val = 0
for i in range(0, 3):
    res[i] = (a[(i+1)%3] * b[(i+2)%3]) - (a[(i+2)%3] * b[(i+1)%3])
    val += pow(res[i], 2)
print (res)
square = math.sqrt (val)

'''

# С использованием функционала numpy

res = np.cross(a, b)
square = math.sqrt(np.dot(res, res))

print (f'Площади параллелограмма и треугольника, построенные на векторах а = {a} и b = {b} соответсвенно равны:')
print(f'{square:.2f} {(square/2):.2f}')