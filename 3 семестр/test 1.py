import time

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

n = int(input('Степень 10: '))

num = pow(10, n)
print(num)

'''
start_time = time.time()
factorial(num)
finish_time = time.time() - start_time
print(f'{finish_time:.12f}')
'''

start_time = time.time()

res = 1
for i in range (2, num+1):
    res *= i

finish_time = time.time() - start_time
print(f'{finish_time:.12f}')
