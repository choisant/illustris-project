import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataPath = "./data/tng100-1/cutdata/Subhalo_minE9_SM.csv"
dfAll = pd.read_csv(dataPath)

def doublePowerLaw(b, c, M1, N, x):
    y = 2*N*x*((x/M1)**(-b)+(x/M1)**(c))**(-1)
    return y

def meanValuesLogLog (df, ymin, ymax, dy, ykey, xkey):
    #Calculate log-mean 
    dfAll = df.sort_values(ykey)
    ylist = np.arange(ymin, ymax, dy)
    dictAllMean = {"xMean": [], "yMean": [], "xSigma": [], "ySigma": [] }

    for y in ylist:
        dfPart = df[df[ykey] > y-dy]
        dfPart = dfPart[dfPart[ykey] < y+dy]
        dictAllMean["yMean"].append(dfPart[ykey].mean())
        dictAllMean["xMean"].append(dfPart[xkey].mean())
        dictAllMean["ySigma"].append(dfPart[ykey].std())
        dictAllMean["xSigma"].append(dfPart[xkey].std())
    return pd.DataFrame.from_dict(dictAllMean)


#Plot SHMR for all galaxies
dfAll["SubhaloMassDM"] = np.log10(dfAll["SubhaloMassDM"]*10**10)
dfAll["SubhaloMassStellar"] = np.log10(dfAll["SubhaloMassStellar"]*10**10)
dfAllmean = meanValuesLogLog(dfAll, 8.0, 12.0, 0.4, "SubhaloMassStellar", "SubhaloMassDM")

ax = dfAll.plot.scatter(x = "SubhaloMassDM", y = "SubhaloMassStellar", s = 1)
dfAllmean.plot.scatter(x = "xMean", y = "yMean", s = 8, ax = ax)
dfAllmean.plot(x = "xMean", y = "yMean", c="navy", label = "TNG100-1", ax=ax)
dfAllmean.plot.scatter(x = "xMean", y = "yMean", yerr = "ySigma", c = "navy", ax = ax)

#Plot Moster fit
xmin = 10**9
xmax = 10**14
dx = 10**10
x=np.arange(xmin,xmax,dx)
y = doublePowerLaw(b = 1.376, c = 0.608,M1 = 10**11.590, N = 0.0351, x = x)

plt.plot(np.log10(x),np.log10(y), c="red", label= "Moster2012")

plt.axis([9, 14, 9.5, 12.5])
plt.title("Subhalo SHM, N = " + str(len(dfAll["SubhaloMassDM"])))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
plt.savefig("./fig/SHMR/allGalaxiesTNG100-1.png")
plt.show()