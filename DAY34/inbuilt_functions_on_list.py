a = [10, 20, 30, 40]

print(len(a))
print(max(a))
print(min(a))
print(all(a))

print("=============================")

b = [10, 20, 0, 0, 40]
print(all(b))
print(any(b))
print("=============================")
c= [0, 0, 0, 0, 0, -1]
print(all(c))
print(any(c))


print("=============================")

d = [5, 50, 10, 17, 20, 6]
print(sorted(d))
print(sorted(d, reverse= True))