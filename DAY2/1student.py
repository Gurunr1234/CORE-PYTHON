class Student:
    def __init__(self):
        self.name = "rama"
        self.age = 23
        self.quali = "BE"
        self.addr = "bng"

    def eat(self):
        print("the student is eating")

    def study(self):
        print("the student is studying")

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.quali)
print(s1.addr)

s1.eat()
s1.study()
