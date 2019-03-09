s1= "hello world"

s1=s1.capitalize()
print(s1) # -> Hello world

s2= "h,i,j,k,l"
s2=s2.split(",")
print(s2) # -> ['h', 'i', 'j', 'k', 'l']


s3= "h,i,j,k,l"
s3=s3.replace("," , "&")
print(s3) # ->  h&i&j&k&l


s4= "0101101\n01001\n00"
s4=s4.replace("\n","")
l4_char= [char for char in s4]
l4_int = [int(char) for char in s4]
l4_bolean = [bool(int(char)) for char in s4]

print(l4_char)
# -->['0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0']
print(l4_int)
# -->[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
print(l4_bolean)
# --> [False, True, False, True, True, False, True, False, True, False, False, True, False, False]