def series_sum(i, n):
    res = 1 / i
    if i < (n - 1):
        res += series_sum(i+1, n)

    return res


first_element = int(input('Введите номер первого элемента ряда: '))
quantity = int(input('Введите количество элементов ряда: '))

print('Значение полученное с помощью рекурсии: ', series_sum(first_element, first_element + quantity))

res = 0
for i in range(first_element, first_element + quantity):
    res += 1 / i

print('Значение, полученное с помощью цикла:   ', res)
