var = "Hello"

with open('somefile.txt', 'a') as the_file:
    the_file.write('Hello\n')

with open("data.dat") as f:
    data = f.readlines()
    print(data)
print(var)