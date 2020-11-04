class Car():
    def __init__(self, color, miles):
        self.color = color
        self.miles= miles
    def __str__(self):
        return f"The {self.color} car has driven {self.miles}"

if __name__ == '__main__':
    c1= Car("red", 1000)
    c2= Car("blue",10000)
    for car in (c1,c2):
        print(car)