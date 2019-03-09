import numpy as np
numbers=[1,2,3,4,5,6,7,8,9]

# print([x+1 if x >= 6 else x+5 for x in numbers])

print("Original: \n", numbers)

## apply a function:

#normal way:
pow2 = []
for x in range(10):
   pow2.append(x**2)

# better way:
print([x**2 for x in numbers])

#apply a condition:
print([x for x in numbers if x%2==0 ])

#apply more conditions:
print([x for x in numbers if x%2==0 if x%3==0])

#apply if and else statement (other way round):
print([x+10  if x%2==0 else x  for x in numbers])


###Nestetd list comprehension
list_of_list = [[1,2,3],[4,5,6],[7,8]]

# Flatten `list_of_list`
print([x for x in list_of_list])
print([y for x in list_of_list for y in x])


#printing a matrix with squre brackets
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print([[row[i] for row in matrix] for i in range(3)])