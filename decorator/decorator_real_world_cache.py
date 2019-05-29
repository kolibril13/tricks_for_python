from decorator.decorator_lib import *
import functools


@functools.lru_cache(maxsize=None)
def f(x):
    return x

f(2)
f(5)
f(2)
f(2)
f(44)
f(444)
f(1)
print(f.cache_info())