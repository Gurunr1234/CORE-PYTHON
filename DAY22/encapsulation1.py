class Person:
    def __init__(self):
        self.__name = " "
    
    def Setter(self, value):
        self.__name = value

    def getter(self):
        return self.__name
    
p = Person()
p.Setter("Rama")
res =  p.getter()
print(res)
print(p.getter())