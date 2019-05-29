from decorator.decorator_lib import *
@CountCalls
def g():
    print("hello world")


g()

g()

print(g.nummer)