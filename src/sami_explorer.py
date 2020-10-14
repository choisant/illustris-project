import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#df = pd.read_pickle("./data/SAMI/sami.pkl")
df1 = pd.read_csv("./data/SAMI/allData.csv")
indexNames = df1[df1["r_petro"] < 0].index
df1.drop(indexNames, inplace = True)
df1["radius"] = df1["r_petro"]**(-1)*10/0.68
df1.plot.scatter(x="radius", y ="mstar",s = 3)
plt.show()

