class Book:
    def __init__(self, value):
        self.__pages = value
    
    def Setter(self, value):
        if value > 0:
            self.__pages = value

    def getter(self):
        return self.__pages
    
b = Book(100)
b.Setter(114)
res = b.getter()
print(res)
b.Setter(-99)
print(b.getter())