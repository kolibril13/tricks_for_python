class MyClass2:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def preset_a():
        return MyClass2(1)
    @staticmethod
    def preset_b():
        return MyClass2(2)
    @staticmethod
    def preset_c_with_extend(extend):
        return MyClass2(3+extend)

    def __str__(self):
        return f"The value of x is {self.x}"

Y2=MyClass2.preset_b()
print(Y2)
Y2=Y2.preset_a()
print(Y2)

