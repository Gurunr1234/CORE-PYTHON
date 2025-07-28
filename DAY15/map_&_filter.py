L = ["Rama", "Sita", "Ravana", "Krishna", "Radha"]

k = list(filter(lambda name: name.startswith("R"), L))
print(k)

m = list(map(lambda name: name.upper(), L))
print(m)