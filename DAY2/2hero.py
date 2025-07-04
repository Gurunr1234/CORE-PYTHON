class Hero:
    def __init__(self):
        self.name = "guru"
        self.age = 22
        self.height = 5.8
        self.mob = 99779

    def fight(self):
        print("hero is fighting")

    def run(self):
        print("hero is running")

h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.height)
print(h1.mob)

h1.fight()
h1.run()

h1.mob = 66776
h1.age = 21

h1.noOfMovies = 10
h1.isMarried = False

h2 =h1
h3 = h2
print(h2.name)
print(h3.name)
print(h2.age)
h3.fight()
h3.run()