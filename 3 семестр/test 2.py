class Fff:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, arg):
        if isinstance(arg, numbers.Number):
            return Fff(self.x + arg, self.y + arg)
        else:
            return Fff(self.x + arg.x, self.y + arg.y)

    def show(self):
        print (self.x,' : ',self.y)

f1 = Fff(1,2)
f2 = Fff(5,5)

result = f1 + f2
result2 = f1 + 2

result.show()
result2.show()
