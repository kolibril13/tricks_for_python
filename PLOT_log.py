import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,1)
fig= plt.figure()
plt.plot(x,x**2)
plt.yscale('log')


plt.show()