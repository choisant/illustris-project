import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

sami = pd.read_csv("./data/SAMI/all_data_vrot.csv")

fig1, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize = (8,8))

sami["mass_diff"] = sami["mstar_log"] - sami["MSAMI"]
sami.plot.scatter(x = "mstar_log", y = "mass_diff", ax = ax1)
plt.show()
