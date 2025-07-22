class Demo:
    def swap(self, x, y):
        temp = x
        x = y
        y = temp
        return x, y

d1 = Demo()
a = 10
b = 20
print(a)
print(b)

a, b = d1.swap(a, b)
print(a)
print(b)