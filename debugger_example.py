import numpy as np
import pandas as pd

data=  [[3,3,3],
        [4,4,4],
        [5,5,5]]
a= np.array(data)
df = pd.DataFrame(a, columns=['a', 'b', 'c'], index = ["jo", "ho" , "ho"])
print(df)
b=4