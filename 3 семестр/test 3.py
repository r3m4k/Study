n = 6
x = 2

for i in range(n):
    j = n - i
    if j % 2:
        flag1 = 1
        flag2 = 2
    else:
        flag1 = 2
        flag2 = 1

    if not i == n-1:
        a = flag2 * x
    else:
        a = 0

    if i == 0:
        fraction = j / (flag1 * x)
        res = (a + fraction)
    else:
        fraction = j / res
        res = (a + fraction)

print(res)
