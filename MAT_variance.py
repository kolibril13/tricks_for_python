import numpy as np
a= np.array([1,3,5])

print(a.var())
var_part=1/len( a ) * ( np.sum( [ ( a[i]-a.mean() )  **2 for i in range(0,len(a)) ] ) )
print(var_part)