import numpy as np
import pandas as pd
mini_array= np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]] )
def my_func(x):
    return (x, x)

df1= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))
df1=df1.apply(my_func)
print(df1)