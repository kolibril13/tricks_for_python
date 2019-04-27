double = lambda x: x * 2

print(double(5))



#in combination with filter:
my_list = [1 ,5,4,8,10,9,2,1,1]
condition_function =lambda x: (x%2) ==0
even_list= list(filter(condition_function, my_list))
print(even_list)