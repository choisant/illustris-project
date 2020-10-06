import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("./data/SAMI/dr1.csv")
df2 = pd.read_csv("./data/SAMI/dr2_stellar_kinematics.csv")
df3 = pd.read_csv("./data/SAMI/dr2_gas.csv")
df4 = pd.read_csv("./data/SAMI/dr2_gas_recom.csv")
datalist = [df1, df2, df3, df4]
#data = pd.DataFrame(data = df1)
data1 = pd.merge(df1, df2, how = "outer", on = 'cataid')
data2 = pd.merge(df3, df4, how = "outer", on = 'cataid')
data = pd.merge(data1, data2, how = "outer", on = 'cataid')
data.sort_values(by = ["cataid"])

data.to_csv("./data/SAMI/allData.csv")