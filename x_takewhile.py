from itertools import takewhile 
import time
# function to check whether  
# number is even 
def even_nos (x): 
     return(x % 2 == 0) 
  
# iterable (list) 
li =[0, 2, 4, 8, 22, 34, 6, 67] 
  
# output list 
new_li = list(takewhile(even_nos, li)) 
print(new_li) 