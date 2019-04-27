import numpy as np
import pandas as pd
mini_array= np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]] )
df1= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))
df2= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))
df3= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))
list= [df1, df2, df3]
df4= pd.concat(list, axis=1)
print(df4)