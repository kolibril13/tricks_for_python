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

for i,j in d.iteritems():
    print(i,j)