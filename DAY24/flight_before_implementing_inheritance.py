class Cargo:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryC(self):
        print("plane carry cargo")

class Passenger:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryP(self):
        print("plane carry passenger")

class Fighter:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryW(self):
        print("plane carry weapons")

c = Cargo()
p = Passenger()
f = Fighter()
c.takeoff()
c.fly()
c.land()
c.carryC()

p.takeoff()
p.fly()
p.land()
p.carryP()

f.takeoff()
f.fly()
f.land()
f.carryW()