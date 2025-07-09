class Student:
    def __init__(self, sname, susn, smob, saddr):
        self.name = sname
        self.usn = susn
        self.mob = smob
        self.addr = saddr

s1 = Student("rama", "ivtucs01", 90888, "bng")
s2 = Student("sita", "ivtucs02", 33439, "mys")

print(s1.usn)
print(s2.addr)