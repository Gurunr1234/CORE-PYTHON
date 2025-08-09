class A:
    def dispA(self):
        print("Inside dispA")

class B:
    def dispB(self):
        print("Inside dispB")
        
class C(A,B):
    def dispC(self):
        print("Inside dispC")

c = C()
c.dispC()
c.dispB()
c.dispA()