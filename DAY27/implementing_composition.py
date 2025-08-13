class Os:
    def __init__(self):
        self.status = True
        print("os is ready")

    def getOs(self):
        print("os is still executing")

class Mobile:
    def __init__(self, name):
        self.mName = name
        self.o = Os()
        print("mobile is ready")
        print("with os is installed")

m = Mobile("Nokia")
print(m.mName)
print(m.o.status)
m.o.getOs()
del m
print("after deleting m")
print(m.mName)
print(m.o.status)
m.o.getOs()