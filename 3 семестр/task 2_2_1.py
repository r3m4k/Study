flag = 1
i = 0
number = 0
while flag:
    symbol = input()
    if (ord(symbol) > 47 and ord(symbol) < 58):
        number = number*10 + int (symbol)
        i+=1
    else:
        flag = 0
        
if i == 0:
    print ('Вы не ввели цифру')
else:
    print ('Ваше число: ', number)