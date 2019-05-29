class Circle:
    def __init__(self, radius=1):
        self.radius= radius
    @classmethod
    def new_rad(cls):
        return cls(2)

c=Circle()
c=c.new_rad()
print(c.radius)