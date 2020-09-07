#How is the older people's body reacted in different types of activities?
import pandas as pd
import numpy as np

location = 'GOTOV_DataSummary.csv'

df = pd.read_csv(location)

print(df)

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)

print(newdf)
print(newdf.mean())
print(newdf.std())
print(newdf.var())
