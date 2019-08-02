import numpy as np
import matplotlib.pyplot as plt
PIXEL=5
x, y = np.meshgrid(np.linspace(-1,1,PIXEL), np.linspace(-1,1,PIXEL))
d = np.sqrt(x*x+y*y)
sigma, mu = 1.0, 0.0
g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(g)
plt.imshow(g)
# plt.show()
