def make_thicker(func):
    def wrapper( *args):
        plt.rcParams['lines.linewidth'] = 10.0
        func()
    return wrapper


import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,10,100)

@make_thicker
def plotten():
    plt.plot(x, x**2)
    plt.show()

plotten()