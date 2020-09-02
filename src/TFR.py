import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

dataPath1 = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_lateType_SFR.pkl"
df1 = pd.read_pickle(dataPath1)
#df1["SubhaloVel"] = df1.eval(df1["SubhaloVel"])

dataPath2 = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_lateType_gas.pkl"
df2 = pd.read_pickle(dataPath2)
#df2["SubhaloVel"] = df2.eval(df2["SubhaloVel"])

def formatPlot (title, df):
    plt.axis([0, 1000, 10**(9), 10**(13)])
    #plt.xscale("log")
    plt.yscale("log")
    plt.title(title + " N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Velocity [km/s]')
    plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
    plt.legend()
    #plt.savefig("./fig/SFR/"+title+"TNG100-1_sSFR.png")

def velocities(df):
    df["SubhaloMassStellar"] *=10**10
    velocities= df["SubhaloVel"]
    meanVel = []
    for v in velocities:
        meanVel.append(math.sqrt(sum(i**2 for i in v)))
        #meanVel.append(np.linalg.norm(v))
        #meanVel.append(v[0])
    df["SubhaloVelAbs"]= meanVel
    return df

df1=velocities(df1)
df2=velocities(df2)

print(df1)
ax = df1.plot.scatter(x="SubhaloVelAbs", y="SubhaloMassStellar",s=1, label = "SFR")
#df2.plot.scatter(x="SubhaloVelAbs", y="SubhaloMassStellar",s=1, color = "orange", label = "GasFraction", ax=ax)
formatPlot(title = "TFR", df=df1)
df1.plot.scatter(x = "SubhaloMassStellar", y="SubhaloVelAbs")
#plt.show()