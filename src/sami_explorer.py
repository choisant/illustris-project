import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#df = pd.read_pickle("./data/SAMI/sami.pkl")
df1 = pd.read_csv("./data/SAMI/dr1.csv")
df2 = pd.read_csv("./data/SAMI/dr2_stellar_kinematics.csv")
df3 = pd.read_csv("./data/SAMI/dr2_gas.csv")
df4 = pd.read_csv("./data/SAMI/dr2_gas_recom.csv")
datalist = [df1, df2, df3, df4]
data = pd.DataFrame()

for df in datalist:
    for key in df.keys():
        data[key] = df[key]
check = data[data["catid"] == 7841]
print(check["mag_r_band_petrosian"])
#print(data[data["catid"] == 7841])
#plt.plot(data.index, data["catid"])
#plt.show()