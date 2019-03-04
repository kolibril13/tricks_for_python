import numpy as np
#how to create an array in python
a= np.array([[1,2], [3,4]])
a= np.random.random((4,4))
a= np.random.randint(1,6,(3,3))
a= np.random.poisson(2000,(3,3))
a= np.fromfunction(lambda x,y:x+y,(100,100) ,dtype='uint8')
a= np.array([[x+y for x in range(100)] for y in range(100)], dtype='uint8')
#round
a= [1,2,3 , 3.5]
b=np.floor(a)

#extend in y direction
a= np.uint8([[1,2,3],[4,5,6]])
ext_y=   [[x for x in range(7,10)]]
a_longer_y= np.append(a, ext_y, axis=0)

# extend in x direction
a= np.uint8([[1,2,3],[4,5,6]])
ext_x= [[y] for y in range(11,13)]
a_longer_x= np.append(a, ext_x, axis=1)

#or
a= np.uint8([[1,2,3],[4,5,6]])
# b = np.hstack(a, [2,4])

#multiplication
a= np.array([[1,1],[1,2]]); b= np.array([[3,3],[3,3]])
a *=b

# addition
a= np.array([[1,1],[1,2]]); b= np.array([[3,3],[3,3]])
a +=b


####Methods of numpy
# sum
a= np.array([[1,2], [3,4]])
sum=a.sum()
sum_all_y_for_one_x = a.sum(axis=0)
sum_all_x_for_one_y = a.sum(axis=1)

# variance
a = np.array([[1,2], [3,4]])
a.var()
a.std()
a.dtype
a.astype('uint8')
l=a.tolist()




