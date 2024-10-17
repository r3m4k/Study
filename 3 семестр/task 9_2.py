file = open('Henry Lion Oldie. Master.txt', 'r')

res = {'letter': 0,
       'number': 0,
       'punctuation': 0,
       'other': 0}

quant = 0
symb = file.read(1)
while symb:
       #print(symb, end='')
       if symb.isalpha():
              res['letter'] += 1
              quant += 1
       elif symb.isdigit():
              res['number'] += 1
              quant += 1
       elif not set(".,:;!()").isdisjoint(symb):
              res['punctuation'] += 1
              quant += 1
       else:
              res['other'] += 1
              quant += 1
       symb = file.read(1)
#print (res)

print(f'Всего {quant} символов. Из них: ')
persent = res['letter']/quant
print(f'Букв {persent*100:.2f}%')

persent = res['number']/quant
print(f'Цифр {persent*100:.2f}%')

persent = res['punctuation']/quant
print(f'Знаков перпинания {persent*100:.2f}%')

persent = res['other']/quant
print(f'Других {persent*100:.2f}%')

file.close()
