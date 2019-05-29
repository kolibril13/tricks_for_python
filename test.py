def repeat(times=2):
    def repeat_outer(func):
        def wrapper_inner(*args,**kwargs):
            for _ in range(0, times):
                val = func(*args, **kwargs)
            return val
        return wrapper_inner
    return repeat_outer


import functools


@functools.lru_cache(maxsize=None)
def p():
    print("hello")

p()
p()
p()
p()
p()
print(p.cache_info())