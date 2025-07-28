class Demo:
    a = 10
    def __init__(self):
        self.b = 20
        self.c = 30

    def instaceDisp(self):
        print(self.b)
        print(self.c)

    @staticmethod
    def staticDisp():
        print(Demo.a)

    @classmethod
    def classDisp(cls):
        print("python")
        print(cls.a)

d1 = Demo()
d1.instaceDisp()
Demo.staticDisp()
Demo.classDisp()