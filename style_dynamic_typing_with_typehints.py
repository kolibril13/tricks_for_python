from typing import Callable,List,Dict, Any
def factorial(i:int) -> int:
    if i < 0:
        return None
    if i==0:
        return 1
    if i >0:
        return i*factorial(i-1)

def map_my_list(func:Callable,l:List[int])-> List[int]:
    l2= [func(i) for i in l]
    return l2

def map_my_dict(func:Callable,dic:Dict[Any,int]) -> Dict:
    d2= {key:func(value) for key,value in dic.items()}
    return d2

print(factorial(12))
# print(map_my_list(factorial,[1,2,3]))
print(map_my_dict(factorial,{"a":2,"b":3}))