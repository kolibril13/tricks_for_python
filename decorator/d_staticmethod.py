#a und b
class Circle:
    def __init__(self, radius=1):
        self.radius= radius
    @staticmethod
    def pi():
        return 3.14

c=Circle()
print("a",Circle.pi())
print("b",c.pi())

#nur a
class Circle:
    def __init__(self, radius=1):
        self.radius= radius
    def pi():
        return 3.14
c=Circle()
print("a",Circle.pi())
#print("b",c.pi())

# nur b
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    def pi(self):
        return 3.14

c= Circle()
#print("a",Circle.pi())
print("b",c.pi())