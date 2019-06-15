class Ground:
    def __init__(self, name):
        self.name= name
    a=3

class Ext(Ground):
    b=4




g= Ground("tim")
g.name= "otto"

e= Ext("sören")
print(g.name)
print(e.name)
