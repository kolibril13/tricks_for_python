class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return other.var == self.var

    def __repr__(self):
        return MyClass.__name__



c1= MyClass(1)
c2= MyClass(1)

d = {
    c1: "hello",
    c2: "world"
}
print(d)

# So now you see that dictionaries test two things:
# the hash value and the equality, if one of them doesn't match,
# then it is going to be assigned as a new key.
####### again:
print("############")
class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)
    def __repr__(self):
        return MyClass.__name__


# So now you see that dictionaries test two things:
# the hash value and the equality, if one of them doesn't match,
# then it is going to be assigned as a new key.

c1= MyClass(1)
c2= MyClass(1)
c3= MyClass(1)


d = {
    c1: "hello",
    c2: "world"
}
d[c3]= " number1"
print(d)