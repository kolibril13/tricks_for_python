import numpy as np
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = []
##old way
for i in range(3):
     transposed_row = []
     for row in matrix:
            transposed_row.append(row[i])
     transposed.append(transposed_row)

#new way
original2 =   [[row[i] for i in range(3)] for row in matrix ]
transposed2 = [[row[i] for row in matrix] for i in range(0,3) ]

print(np.array(matrix))
print(np.array(transposed))
print(np.array(transposed2))

