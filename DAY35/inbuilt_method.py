a = [10, 20, 30, 40, 50]
print("a= ", a)
a.insert(2, 25)
print(a)
a.append(60)
a.append(70)
# a.append(80, 90, 100)
b = [80, 90, 100]
a.extend(b)
a.extend([110, 120, 130])
print("a==", a)