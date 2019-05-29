from decorator.decorator_lib import *
import functools


@slow_down(rate=0.1)
def f(counter):
    if counter > 0:
        print(counter)
        f(counter-1)
    else:
        print("liftoff")

f(8)
