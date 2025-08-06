class student:
    def __init__(self):
        self.__name1 = " "

    @property
    def dataAccess(self):
        return self.__name1
    
    @dataAccess.setter
    def dataAccess(self, value):
        self.__name1 = value

s = student()
s.dataAccess = "Rama"
res = s.dataAccess
print(res)