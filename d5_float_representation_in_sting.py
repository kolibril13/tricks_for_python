var3= 123.45678
print(
    f'rounded1    \t {var3:.1f} \n' 
    f'rounded2    \t {var3:.2f} \n' 
    f'zero_pad1   \t {var3:06.1f} \n'  #<-- important line
    f'zero_pad2   \t {var3:07.1f}\n'   #<-- important line
    f'scientific1 \t {var3:.1e}\n'
    f'scientific2 \t {var3:.2e}\n'
)
