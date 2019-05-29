from decorator_lib import *
import functools

@CallReminder
def f(x):
    print(x)
    return x

f(2)
f(5)
f(2)
f(2)
f(44)
f(444)
f(1)
print("The function was called " + str(f.how_often))