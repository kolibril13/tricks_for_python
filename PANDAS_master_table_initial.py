import pandas as pd

data = {
    "Oberservation number": 1,
    "item" : 2
        }
df = pd.DataFrame.from_dict(data, orient='index')
df.columns = ['Inital']
df.to_csv("PANDAS_master_tabel.txt")
