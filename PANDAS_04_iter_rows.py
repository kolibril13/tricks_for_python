import numpy as np
import pandas as pd
mini_array= np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]] )
df= pd.DataFrame(mini_array , columns= list("ABC") , index= list("abc"))


for idx, row in df.iterrows():
     #row["A"]=0 #NOT LIKE THIS row is a copy and does not point back to pd
     print(f"IDX:{idx} \nROW: {row} \n")
