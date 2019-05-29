import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mini_array= np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]] )
df1= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))
df1["A"]= [9,9,9]
print(df1)