import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10,10,1000)


def gaussian(x, mu, var):
    return 1/(np.sqrt(2*np.pi* var))*np.exp(-np.power(x - mu, 2.) / (2 * var))
y= gaussian(x, 2 ,2)

# y= x**2
# y= np.random.poisson([x for x in range(100)],100)



plt.plot(x,y)
plt.show()
