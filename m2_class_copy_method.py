import copy

class MyClass:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"der name lautet: {self.name} and from class : {self.__class__}"
x=MyClass("Hendrik")
x.name="Theo"
y= x
print(x)
print(y)

x=MyClass("Hendrik")
z=copy.copy(x)
z.name="Theo"
print(x)
print(z)