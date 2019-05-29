from decorator.decorator_lib import *


@slow_down
@timer
@debug
def return_greeting(name):
    return f"Hi {name}"

text= return_greeting("Adam")
print(text)