from decorator_lib import *
import functools

@debug
def f(x):
    print(x)

f(2)