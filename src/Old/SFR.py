import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_SFR.csv"
df = pd.read_csv(dataPath)

def formatPlot (title, df):
    plt.axis([10**9, 10**12, 10**(-4), 10**0])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + " N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Stellar mass [$ M_\odot /h $]')
    plt.ylabel(r"sSFR [$ Gyr^{-1} $]")
    plt.legend()
    #plt.savefig("./fig/SFR/"+title+"TNG100-1_sSFR.png")

df["SubhaloMassStellar"] *=10**10
df["SubhaloSFR"] *=10**(9)
df["SubhalosSFR"]  = df["SubhaloSFR"]/df["SubhaloMassStellar"]
dfLarge = df[df["SubhaloMassStellar"]> 10**(10.5)]
dfSmall = df[df["SubhaloMassStellar"]< 10**(10.5)]
mean = dfSmall["SubhalosSFR"].mean()
print(np.log10(mean))

ax = df.plot.scatter(x="SubhaloMassStellar", y="SubhalosSFR", s=1, label = "TNG100-1")
#plt.plot(y=mean)
x = [10**9, 10**13]
y = [10**(-0.93), 10**(-0.933)] #From genel 2018
ax.plot(x,y, label = "Genel2018 mean", color='orange')
ax.fill_between(x, 10**(-1.43), 10**(-0.43), color="orange", alpha=0.2, label = "Main sequence")
ax.fill_between(x, 10**(-1.933), 0, color="navy", alpha=0.1, label = "Quenched")
formatPlot(title="sSFR in central galaxies", df=df)
plt.show()