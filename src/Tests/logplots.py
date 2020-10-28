import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_path = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_lateType_Gas.pkl"
data = pd.read_pickle(data_path)
sami = pd.read_csv("./data/SAMI/STELLAR_Details_lates.csv")

def log_formater(df):
    df_log = df.copy(deep=True)
    for key in df.keys():
        df_log[key] = np.log10(list(df[key]))
    return df_log

data_log = log_formater(data)
sami["V_rot"] = np.log10(list(sami["V_rot"]))

fig1, ax1 = plt.subplots(nrows = 1, ncols = 1, figsize = (8,8))
data_log.plot.scatter(y = "SubhaloMassStellar", x = "SubhaloVmax", color = "orange", label = "TNG", ax = ax1)
sami.plot.scatter(y = "MSAMI", x = "V_rot", color = "blue", label = "SAMI", ax = ax1)

plt.show()