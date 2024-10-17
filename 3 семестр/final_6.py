import matplotlib.pyplot as plt

r1 = 1.45


def resistance_resistor(r_i, a):
    return r_i + a * r1


def total_resistance(resistance_resistors):
    res = 0
    for i in range(len(resistance_resistors)):
        res += 1/resistance_resistors[i]

    return 1/res


a = 0.25
n = int(input('Введите количество резисторов: '))

resistance_resistors = list()

for i in range(n):
    if not i:
        var = r1
    else:
        var = resistance_resistor(resistance_resistors[i-1], a)
    resistance_resistors.append(var)

print(resistance_resistors)
print(f'Общее сопротивление {n} резисторов, подключенных параллельно: ', total_resistance(resistance_resistors))


# Графики

def total_resistance_modern(a):
    resistance_resistors = list()
    y_values = list()
    x_values = list()
    quantity = 100
    for i in range(1, quantity):
        for j in range(i):
            if not j:
                var = r1
            else:
                var = resistance_resistor(resistance_resistors[j-1], a)
            resistance_resistors.append(var)
        y_values.append(total_resistance(resistance_resistors))
        x_values.append(i)
    plt.plot(x_values, y_values)
    plt.title(f'R(n) при а = {a}')
    plt.show()


a = [0.25, 0.4, 0.6]
for i in range(len(a)):
    total_resistance_modern(a[i])
