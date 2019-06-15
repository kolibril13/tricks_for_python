import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
l= [1,2,"a"]
t = (1,2,"a")
s= "hello world"
d = {"a":1,
     "b":2}
a =np.array([1,2,3])
df =pd.DataFrame([a,a])
f = open('test.py')
fig, ax = plt.subplots()

[print(type(x)) for x in [l,t,s,d,a, df,f, fig, ax]]
print("##########")

i=np.uint8(13)
i2=-22
f= 3.343434

[print(type(x)) for x in [i,i2,f]]

print("##########")


class Class(object):
    pass
c= Class()

def f(x):
    return x

def g(x):
    return x

[print(type(x)) for x in [Class, c, f, f(2)]]


