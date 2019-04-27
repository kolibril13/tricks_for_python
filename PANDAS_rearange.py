import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import os
from scipy.stats import normaltest
from scipy.stats import skewtest
import numpy as np
mini_array= np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]] )
df = pd.DataFrame(mini_array)
print(df)
new_order = [0,2,1]
print(df[df.columns[new_order]])