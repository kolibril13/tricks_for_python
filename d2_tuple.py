t= (3,4,3,7,4,5) # is inchangeable: items can not be added, removed or changed

for element in t:
    print(element)

if 5 in t:
    print("Yes")

print(t.count(3))
print(t.index(7))