import pandas as pd
import numpy as np
write_to_latex= "y"
data  = [[1.32434,2,3],
         [4,5,645],
         [7,8,9]]
df = pd.DataFrame(data, columns=['a', 'b', 'c'], index = ["jo", "ho" , "ho"])

if write_to_latex == "y":
    with open('tex/pd__tabel_minimal.tex','w') as tf:
        #here comes the final formation:

        cm0 =lambda x:'%1i'   %x
        cm1 =lambda x:'%1.1f' %x
        cm2 =lambda x:'%1.2f' %x
        cm3= lambda x:'%1.3f' %x
        # format= {"a": cm1,
        #          "b": cm2,
        #          "c": cm3}
        #or in short
        format= [cm1, cm2, cm3]
        # df.columns = df.columns.str.replace('', '$')
        #escape prevents latex from making $ to \$
        latex_tab = df.to_latex(index=False, formatters= format, escape=False)

        print(latex_tab)
        tf.write(latex_tab)