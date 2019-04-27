import numpy as np
import pandas as pd
mini_array= np.array([[1,2],
                      [4,5],
                      [1,22],
                      [4,5]] )
def my_func(x):
    return (x, x)

df1= pd.DataFrame(mini_array , columns= list("AB") , index= list("abab"))
print(df1)
df2= df1[df1["A"] == 1 ]
print(df2)
print("\n")
df3= df1[(df1["A"]== 1) & (df1["B"] == 2)]
print(df3)