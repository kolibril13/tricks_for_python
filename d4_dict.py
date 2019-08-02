d = {
    "a": "Green",
    "b": "Red",
    "c": "Blue"
}

# indeices in lists are parallel to keys in a dict
for i in d:
    print(i)


for i,j in d.items(): # not so fast because d.items returns a list
    print(i,j)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)


d2= {
    "hello":23,
    23:222,
    (1,2): 233,
}
print(d2)

# So now you see that dictionaries test two things:
# the hash value and the equality, if one of them doesn't match,
# then it is going to be assigned as a new key.