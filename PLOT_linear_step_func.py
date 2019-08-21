import numpy as np
import matplotlib.pyplot as plt

def linear_step_func(x,x0,x1):
    x = np.maximum(x0,x)
    x = np.minimum(x,x1)
    x = x/x1
    return x

x= np.arange(0,50)
y= [linear_step_func(x_val,10,30) for x_val in x]
plt.plot(x,y)
plt.show()