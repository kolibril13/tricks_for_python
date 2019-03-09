import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10,10,1000)


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
y= gaussian(x, 2 ,2)

# y= x**2
# y= np.random.poisson([x for x in range(100)],100)



plt.plot(x,y)
plt.show()
