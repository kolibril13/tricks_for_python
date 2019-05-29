import pandas as pd
data  = [[1,2,3],
         [4,5,6],
         [7,8,9.001]]
df = pd.DataFrame(data, columns=['a', 'b', 'c'], index = ["foo", "bar" , "ho"])
cm0 =lambda x:'%1i'   %x
cm1 =lambda x:'%1.1f' %x
cm3= lambda x:'%1.3f' %x
format= [cm0, cm1, cm3]
latex_tab = df.to_latex( formatters= format)
print(latex_tab)
#new way
# latex_tab = df.to_latex( data, formatters_col= ['%1i','%1.1f','%1.3f'])

# and maybe also:
# latex_tab = df.to_latex( data, formatters_row= ['%1i','%1.1f','%1.3f'])

