from decorator.decorator_lib import *
import functools

@repeat(num_times=23)
def f(x):
    print(x)

f(2)