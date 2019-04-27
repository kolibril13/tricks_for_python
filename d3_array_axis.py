import numpy as np
a= np.array([[1,1,1],
             [3,3,3],
             [5,5,5]] )



# axis 0 = will act on all the ROWS in each COLUMN
# axis 1 = will act on all the COLUMNS in each ROW

#example

b= np.concatenate( (a,a) , axis=1)
print(b)
c = np.concatenate( (a,a), axis=0 )
print(c)