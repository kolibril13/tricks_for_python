class Car():
    def __init__(self,color, miles):
        self.color= color
        self.miles= miles
    def __str__(self):
        return f" A {self.color} car with {self.miles} driven miles"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color},{self.miles})"

my_Car=Car("green", 23)
print(repr(my_Car))

#__str__ -> gives an easy representation
#__repr__ -> should be unambiguous