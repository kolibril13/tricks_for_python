import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mini_array= np.array([1,2,3])

df= pd.Series(mini_array)
#options: line, bar , hbar, hist, box , pie, scatter, hexbin
# df.plot(kind= "hist") #histogram
# df.plot(kind= "line") #linie
# df.plot(kind= "area")
df.plot(marker= 'o', linestyle= '')

plt.show()