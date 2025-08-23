a=[10, 20, 30, 40, 50, 60, 70]

print(a)
a.remove(30)
print("a= ", a)
a.pop()
print(a)
a.pop(1)
print("a==", a)
print(a.count(10))
print(a.index(50))
a.clear()
print(a)
del a
print(a)