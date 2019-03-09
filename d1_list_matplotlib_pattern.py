import numpy as np
import matplotlib.pyplot as plt

# x= np.uint8([[i for i in range(0,10)] for j in range(0,10)])
x= np.uint8([[0 if (j+i)%2==0 else 1 for i in range(10) ] for j in range(10)])
x= np.fromfunction(lambda x,y: (x+y)%2 , (10,10))
plt.imshow(x, cmap="gray")
plt.show()