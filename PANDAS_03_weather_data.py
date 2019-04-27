import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# tutorial : www.synesthesiam.com

data= pd.read_csv("media/weather_year.csv")

# print(data.head())
data= data.rename(columns={'Max TemperatureF':'max_temp'})
series= pd.Series(data.mean(axis= 0))
# using boolean operations to look for the max value interval
print(data.max_temp[(data.max_temp > 25) & (data.max_temp < 30) ])
