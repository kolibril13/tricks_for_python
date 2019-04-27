s= "hello world\n" \

#string formatation
s0_a=s.capitalize()
# print(s0_a) # -> Hello world

s0_b=s+s
# print(s0_b)

## formated sring
var1= 42
var2 = "foo"
## old formating style with tuple in the end
s0_b_old= 'Hello, %s, %s' % (var1, var2)
# print(s0_b_old)
# better
s0_b_better= 'Hello, {}, {}'.format( var1, var2 )
# print(s0_b_better)
#the best: (python 3.6+)
s0_b_best= f'Hello, {var1}, {var2}'
# print(s0_b_better)

var3= 23.2235345
s0_b_example = f'Nomal   \t {var3} \n' \
               f'gerundet\t {var3:.3f} \n' \
               f'gerund  \t {var3:.1f} \n' \
               f'und so  \t {var3:3.4f}' \

print(s0_b_example)

s1_rawstring= r'\n lalala \t \n  \' ' # here the \ is not suppressed
print(s1_rawstring)

combination_raw_and_fomated = rf'lala l \n {var3}'
print(combination_raw_and_fomated)



s2= "h,i,j,k,l"
s2=s2.split(",")
# print(s2) # -> ['h', 'i', 'j', 'k', 'l']


s3= "h,i,j,k,l"
s3=s3.replace("," , "&")
# print(s3) # ->  h&i&j&k&l


s4= "0101101\n01001\n00"
s4=s4.replace("\n","")
l4_char= [char for char in s4]
l4_int = [int(char) for char in s4]
l4_bolean = [bool(int(char)) for char in s4]

# print(l4_char)
# -->['0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0']
# print(l4_int)
# -->[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
# print(l4_bolean)
# --> [False, True, False, True, True, False, True, False, True, False, False, True, False, False]