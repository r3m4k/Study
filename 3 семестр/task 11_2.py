class Equipment:

    def __init__(self, name, mass, power, volume):
        self.name = name
        self.mass = mass
        self.power = power
        self.volume = volume

    def __add__(self, obj):
        return Equipment(self.name + ' + ' + obj.name, self.mass + obj.mass, self.power + obj.power, self.volume + obj.volume)

    def __str__(self):
        volumes = round(self.volume, 3)
        return f'Оборудование {self.name}, массой {self.mass} кг, энегропотреблением {self.power}, занимает {volumes} куб.м. пространства'


kettle = Equipment('чайник', 0.5, 2.5, 0.003)
pc = Equipment('ПК', 6, 2.5, 0.1)
microscope = Equipment('электронный микроскоп Talos 200', 400, 4.5, 3.0)
all = pc + kettle + microscope
#print(all)
print(microscope)
