class charger:
    def __init__(self, name):
        self.cname = name
        print("charger is ready")

    def getCharger(self):
        print("charger is used for charging")

class Mobile:
    print("==================")
    def __init__(self, name):
        self.mname = name
        self.c1 = " "
        print("mobile is ready")

    def hasMobile(self, x):
        self.c1 = x
        print("Both the charger and phone are connected")

m = Mobile("Nokia")
charge = charger("Nokia's charger")
m.hasMobile(charge)
print(m.mname)
print(m.c1)
print(m.c1.cname)
m.c1.getCharger()
del m
print("after deleting")
# print(m.mname)
# print(m.c1)
# print(m.c1.cname)
print(charge.cname)
charge.getCharger()