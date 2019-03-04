with open("LAB0.data") as f:
    data = f.readlines() #read as stings
string = "".join(x for x in data)
string = string.replace("\n", "")
# string= string.split(",") in case for more complexity
list = [int(x) for x in string]
print(list)

# for element in data:
#     print(element)