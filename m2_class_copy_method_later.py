import copy

class MyClass:
    def __init__(self, foo, bar=None):
        self.foo = foo
        if bar is not None:
            self.bar = bar
        else:
            self.bar = {'Hello': 'Ciao'}

a=MyClass("hi")
print(a.foo)
print(a.bar)