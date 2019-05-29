#a und b
class Circle:
    def __init__(self, radius=1):
        self.radius= radius
    @staticmethod
    def pi():
        return 3.14

c=Circle()
print(c.pi())
print(Circle.pi())


#nur a
class Circle:
    def __init__(self, radius=1):
        self.radius= radius
    def pi():
        return 3.14

print(Circle.pi())

# nur b
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def pi(self):
        return 3.14

c= Circle()
print(c.pi())