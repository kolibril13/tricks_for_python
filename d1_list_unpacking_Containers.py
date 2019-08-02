a = [1,2,3,4,5]

# unpacking b:
*b, = a
b, *c , d = a
print(b, c)


#unpacking dict:
def add(b,a,c):
    return a+b+c
d = {'a': 2,
     'b': 3,
     'c': 5}
print(add(**d))
