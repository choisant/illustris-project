import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

dataPath1 = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_earlyType_SFR.pkl"
df1 = pd.read_pickle(dataPath1)
#df1["SubhaloVel"] = df1.eval(df1["SubhaloVel"])

dataPath2 = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_earlyType_Gas.pkl"
df2 = pd.read_pickle(dataPath2)
#df2["SubhaloVel"] = df2.eval(df2["SubhaloVel"])

def formatPlot (title, df):
    plt.axis([10**1.5, 10**2.5, 10**(9), 10**(12)])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + " N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Velocity [km/s]')
    plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
    plt.legend()
    #plt.savefig("./fig/SFR/"+title+"TNG100-1_sSFR.png")

df1["SubhaloMassStellar"] *=10**10
df2["SubhaloMassStellar"] *=10**10
ax = df1.plot.scatter(x="SubhaloVelDisp", y="SubhaloMassStellar",s=1, label = "SFR")
#df2.plot.scatter(x="SubhaloVelDisp", y="SubhaloMassStellar",s=2, color = "orange", label = "GasFraction", ax=ax)
il.formatplot.formatPlotVD_SM(title = "Velocity dispersion", df=df1)

plt.show()