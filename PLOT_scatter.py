import numpy as np
import matplotlib.pyplot as plt

x,y = np.genfromtxt('./media/parameter_kurve.csv', delimiter=',')

plt.scatter(x,y)
plt.show()