from decorator.decorator_lib import *
class Add_and_sub:
    def __init__(self):
        self._x = 42
    @property
    def val(self):
        return self._x
    @val.setter
    def x(self,value):
        self._x = value

    def __iadd__(self, other):
        self._x = other+self._x
        return self
    @debug
    def __isub__(self, other):
        self._x = self._x-other
        return self

    def __repr__(self):
        return f"hello {self._x}"


if __name__ == "__main__":
    a = Add_and_sub()
    print(a.val)
    a += 10
    a -= 20
    print(a.val)
