import numpy as np
import pandas as pd

#Working idea:
# 1. data reading
# 2. bringing data in form
# 3. data manipulation
# 4. data plotting
# 5. data saving

mini_array= [[1,2,3],
             [4,8,6],
             [7,5,9]]

s= pd.DataFrame(mini_array, index= [42,43,44], columns= list('ABC'))
print("Original \n",s)
s_a1 = s.head()
s_a2 = s.to_numpy()
s_a3 = s.to_latex()
s_a4 = s.describe()
s_a5 = s.sort_index(axis=1)
s_a6 = s.sort_values(by= 'B')


##Converting columns is possible with 3 methods:
# 1. astype  -> kann so gut wie alles super umwandeln
# 2.  to_numeric()    -> kann gut mit errors umgehen
# 3. infer_objects  ->  makes a very soft coverting of objects to int, float etc.

#Convert all DataFram columns to int64 dtype
s_b1=s.astype(int)
# convert data to stings
s_b2=s.astype(str)

s_b3 = s.astype({"A":int, "B":complex}) # convert A to int64 and B to complex

s_b4= s.apply(pd.to_numeric)  # with to_numeric, returns only new copy


######### Renaming columns
s_test = s.copy()

s_test.index.name= "time [ms]"    # adds an aditional line with the index title

#rename the coumns:
#s.columns = ['a', 'b', 'c']  # make it maniualy
s=s_test.rename(columns={'A':'x', 'B':'y', 'C':'z'}) # with a dictionary, returns copy

s_test.columns = s_test.columns.str.replace('','$')

print(s_test)
