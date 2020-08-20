import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
start_time = time.time()
np.seterr(divide = 'ignore') 


#tng100-1
basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloFlag', "SubhaloMassType", "SubhaloVel"]
haloFields = ["GroupMass", "GroupMassType", "GroupNsubs", "GroupPos", "GroupFirstSub"]
subhalos = il.groupcat.loadSubhalos(basePath,99, fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99) #,fields=haloFields)

datas = il.pandasformat.dictToPandas(subhalos)

#datas["SubhaloMass"].plot()
#plt.show()
datas["SubhaloMassDM"] = datas["SubhaloMassDM"]*10**10
datas["SubhaloMassStars"] = datas["SubhaloMassStars"]*10**10
datas.plot.scatter(x="SubhaloMassDM", y = "SubhaloMassStars")
print(datas["SubhaloMassDM"])
plt.axis([10**10, 10**14, 10**8, 10**12])
plt.xscale("log")
plt.yscale("log")
plt.show()

"""
subhaloFlag = subhalos["SubhaloFlag"]
subhaloMasses = subhalos["SubhaloMassType"]
subhaloMass = subhalos["SubhaloMass"]
subhaloDmMass = []
subhaloStellarMass = []
subhaloMassList = []
SMHratio = []

maxSH = len(subhaloMasses) #use whole data set
#maxH = len(haloMasses)
step = 10 #use a smaller sample. Set equal to 1 if you want all the data shown.
n = 0

for i in range (0,maxSH,step):
    n = n + 1
    mass = subhaloMass[i]
    dm = np.log10(subhaloMasses[i][1]*10**10)
    stellar = np.log10(subhaloMasses[i][4]*10**10)
    #ratio = subhaloMasses[i][1]/mass
    if (subhaloFlag[i] > 0) and (stellar>8): 
        subhaloDmMass.append(dm)
        subhaloStellarMass.append(stellar) 
        #SMHratio.append(stellar/dm) 
        subhaloMassList.append([stellar, dm])

#Process data

dx = 0.1
sortedList = (np.sort(subhaloMassList, axis = 0))
#print(sortedList)
xlist = np.arange(8.0, 11.5, 0.5)
meanValues = []
for x in xlist:
    masses = []
    for s in sortedList:
        if (s[0] > x-dx) and (s[0] < x+dx):
            masses.append(s)
        elif s[0] > x+dx:
            means = np.mean(masses, axis = 0)
            meanValues.append(means)
            break

dmMasses = []
stellarMasses = []
for e in meanValues:
    stellarMasses.append(e[0])
    dmMasses.append(e[1])

print(meanValues[0])
#d = {'DM': (subhaloDmMass), 'S': (SMHratio)}
#dataSet = pd.DataFrame(data = d)
#sns.lmplot(x="DM", y="S", data = dataSet, lowess=True, ci=None, scatter = False)
#sns.regplot(x="DM", y="S", data = dataSet)


print("For "+ str(n) + " subhalos.")
print("Process finished --- %s seconds ---" % int((time.time() - start_time)))

#Subhalo plot
area = np.pi*2

plt.scatter(subhaloDmMass,subhaloStellarMass, s=area, alpha=0.4, c="purple")
plt.plot(dmMasses, stellarMasses, '--')
plt.scatter(dmMasses, stellarMasses)
plt.axis([10, 14, 8, 12])
#plt.xscale("log")
#plt.yscale("log")

plt.title("Subhalo SHM, N = " + str(n))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass")
#plt.savefig("./fig/SHMR/Subhalos.png")
plt.show()
"""