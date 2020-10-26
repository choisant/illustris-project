#import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
start_time = time.time()
np.seterr(divide = 'ignore') 

dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_early.csv"
df1 = pd.read_csv(dataPath)
dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_late.csv"
df2 = pd.read_csv(dataPath)

def formatPlot (title, df):
    plt.axis([10**9, 10**12, 10**(-4), 10**0])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + " N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Stellar mass [$ M_\odot /h $]')
    plt.ylabel(r"sSFR [$ Gyr^{-1} $]")
    plt.legend()
    #plt.savefig("./fig/SFR/"+title+"TNG100-1_sSFR.png")


df1["SubhaloMassStellar"] *=10**10
df2["SubhaloMassStellar"] *=10**10

ax = df1.plot.scatter(x = "SubhaloMassStellar", y = "SubhalosSFR", s = 1, color = 'red')
df2.plot.scatter(x = "SubhaloMassStellar", y = "SubhalosSFR", s = 1, color = 'navy', ax=ax)

formatPlot("sSFR whaty", df1)
plt.show()