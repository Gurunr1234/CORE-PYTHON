class parent:
    def __init__(self):
        self.a = 10

class child(parent):
    def __init__(self):
        # super().__init__()
        parent.__init__(self)
        self.b = 20

c= child()
print(c.b)
print(c.a)