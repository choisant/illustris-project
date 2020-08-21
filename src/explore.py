import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
start_time = time.time()
np.seterr(divide = 'ignore') 

dataPath = "./data/tng100-1/cutdata/Subhalo_minE8_SM_SMHR.csv"
df = pd.read_csv(dataPath)

df["SubhaloMassDM"] *=10**10
df["SubhaloMassStellar"] *=10**10
df.plot.scatter(x = "SubhaloMassDM", y = "SubhaloMassStellar", s = 1)
plt.axis([10**8, 10**15, 10**8, 10**12.5])
plt.xscale("log")
plt.yscale("log")
plt.show()