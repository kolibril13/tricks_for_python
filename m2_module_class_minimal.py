class Dog:
    z=0
    kind = 'Pudel'         # class variable shared by all instances
    def __init__(self,name = None):
        if name is None:
            name= "Bello"
        self.name = name    # instance variable unique to each instance

if __name__== "__main__":
    d1= Dog()
    print(d1.name)
    d1.name= "Karl Ludwig Eulenstedt"
    print(d1.name)
    print(Dog().name)

