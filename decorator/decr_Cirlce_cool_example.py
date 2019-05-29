
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property #.radius is a mutable property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self): #.area is an immutable property
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height): #.cylinder_volume() is a regular method.
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod #Static methods can be called on either an instance or the class.

    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
c=Circle(radius=10)

c=c.unit_circle()

print(c.pi())
print(Circle.pi())