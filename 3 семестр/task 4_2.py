# ВАРИАНТ 2

m, n = input().split(' ')

if (m.isdigit() and n.isdigit()) and ((float(m)%1 == 0) and float(n)%1 == 0):
    m = int(m)
    n = int(n)
    A = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if ((j)%3 == 0) and  j:
                A[i][j] = pow((j),2) - A[i][j-1]
                print(f'A[{i}][{j}] -- b')

            elif not (i)%2:
                A[i][j] = (i)*(j)
                print (f'A[{i}][{j}] -- a')

            elif (i)%2:
                A[i][j] = pow((i), 2) * (j) - A[i-1][j]
                print(f'A[{i}][{j}] -- c')

            else:
                A[i][j] = (i+2) * (j-1)
                print(f'A[{i}][{j}] -- d')

        print ()
    for i in range(m):
        print (A[i])
else:
    print('Ошибка ввода')