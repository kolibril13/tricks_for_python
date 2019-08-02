


# Example with lambda function
# generic function takes op and its argument
def runOp(op, val):
    return op(val)

# declare full function
def add(x, y):
    return x+y

# run example
f = lambda y: add(3, y)
result = runOp(f, 1) # is 4
print(result)


#Example2: is a little faster
from functools import partial

# generic function takes op and its argument
def runOp(op, val):
    return op(val)

# declare full function
def add(x, y):
    return x+y

# run example
f = partial(add, 3)
print(runOp(f, 1)) # is 4


#Example 3: write own wrapper:
# generic function takes op and its argument
def runOp(op, val):
    return op(val)

# declare full function
def add(x, y):
    return x+y

# declare partial function
def addPartial(x):
    def _wrapper(y):
        return add(x, y)
    return _wrapper

# run example
f = addPartial(3)
print(runOp(f, 1)) # is 4



#EXAMPLE with two inputs:
#In short:
def multipy(func, val,val2):
    result= func(val)*val2
    return result
def func(a,b):
     return a+b

print(multipy(lambda x: func(1,x),3,10))