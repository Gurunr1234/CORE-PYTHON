class A:
    def dispA(self):
        print("Inside dispA")

class B(A):
    def dispB(self):
        print("Inside dispB")
        
class C(B):
    def dispC(self):
        print("Inside dispC")

c = C()
c.dispC()
c.dispB()
c.dispA()