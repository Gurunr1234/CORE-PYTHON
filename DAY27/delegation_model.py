class Radio:
    def turnOn(self, x):
        if (x == 1):
            print("Radio is on")
        else:
            print("Radio is off")

class Car:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.r = Radio()

c= Car(60, 80)
print(c.min)
print(c.max)
c.r.turnOn(1)
c.r.turnOn(2)