# options: a means append, w means write

### option 1:
with open('LAB0_text.txt', 'a') as the_file:
    the_file.write('Hello\n')

matrix= [[1,2,3],
         [4,5,6],
         [7,8,9]]
### option 2a: out: 1,2,3,4,5,6,7,8,9
with open("LAB0.data", "w") as the_file:
    s = ",". join(str(x)  for row in matrix for x in row)
    the_file.write(s)
### option 2b: out: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with open("LAB0.data", "w") as the_file:
    the_file.write(str(matrix))



