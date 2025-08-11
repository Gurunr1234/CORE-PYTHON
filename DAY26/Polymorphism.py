class Plane:
    def takeoff(self):
        print("The plane is taking off.")
    def fly(self):
        print("The plane is flying.")
    def land(self):
        print("The plane is landing.")

class Cargo(Plane):
    def takeoff(self):
        print("cargo plane is taking off")
    def fly(self):
        print("cargo plane is flying")
    def land(self):
        print("cargo plane is landing")

class Passenger(Plane):
    def takeoff(self):
        print("passenger plane is taking off")
    def fly(self):
        print("passenger plane is flying")
    def land(self):
        print("passenger plane is landing")

class Fighter(Plane):
    def takeoff(self):
        print("fighter plane is taking off")
    def fly(self):
        print("fighter plane is flying")
    def land(self):
        print("fighter plane is landing")

c = Cargo()
p = Passenger()
f = Fighter()

def allowPlanes(ref):
    ref.takeoff()
    ref.fly()
    ref.land()

allowPlanes(c)
allowPlanes(p)
allowPlanes(f)