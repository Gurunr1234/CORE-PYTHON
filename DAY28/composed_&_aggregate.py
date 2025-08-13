class Heart:
    def __init__(self):
        self.status = True
        print("Heart is ready")

    def getHeart(self):
        print("Heart is waiting")

class Car:
    def __init__(self, name):
        self.cName = name
        print("Car is ready")

    def getCar(self):
        print("Car is ready to drive")

class Person:
    def __init__(self, name):
        self.pName = name
        self.h = Heart()
        self.c1 = " "
        print("Person is ready")

    def hasCar(self, x):
        self.c1 = x
        print("Person using the car")

p = Person("John")
c2 = Car("BMW")
p.hasCar(c2)
print(p.pName)
print(p.h.status)
print(p.c1.cName)
p.c1.getCar()
p.h.getHeart()
del p
print("after deleting p")
print(c2.cName)
c2.getCar()
print(p.h.status)  # This will raise an error since p is deleted
print(p.pName)  # This will raise an error since p is deleted