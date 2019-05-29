import pandas as pd

original = pd.read_csv("PANDAS_master_tabel.txt", index_col=0)
data = {
    "Oberservation number": 1,
    "item" : 2
        }
original["sosos"] = data.values()
original["hello"] = data.values()
# original.pop("Inital") #delete a value
print(original)
original.to_csv("PANDAS_master_tabel.txt")
original