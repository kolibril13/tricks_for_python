class Car():
    def __init__(self,color, miles):
        self.color= color
        self.miles= miles

    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return self.color == other.color
        return NotImplemented

my_Car=Car("green", 23)
my_Car2=Car("green", 23)

print(my_Car == my_Car2)
