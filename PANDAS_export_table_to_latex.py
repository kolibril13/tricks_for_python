import pandas as pd
import numpy as np
write_to_latex= "y"
data  = [[1,2,3],
         [4,5,6],
         [7,8,9.001]]
df = pd.DataFrame(data, columns=['a', 'b', 'c'], index = ["foo", "bar" , "ho"])

if write_to_latex == "y":
    with open('tex/pd__tabel_minimal.tex','w') as tf:
        #here comes the final formation:

        cm0 =lambda x:'%1i'   %x
        cm1 =lambda x:'%1.1f' %x
        cm2 =lambda x:'%1.2f' %x
        cm3= lambda x:'%1.3f' %x

        format= [cm0, cm1, cm3]
        latex_tab = df.to_latex( formatters= format)
        print(latex_tab)
        tf.write(latex_tab)

# # in new way:
#     with open('tex/pd__tabel_minimal.tex','w') as tf:
#         latex_tab = df.to_latex(, formatters= format)
