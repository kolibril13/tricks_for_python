from decorator.decorator_lib import *
import functools
import numpy as np


@timer
def f(x):
    """Return the function in squared"""
    return x*x

a=np.ones((1000,1000))
f(a)
print(f.__doc__)
