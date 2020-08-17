import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
start_time = time.time()


#tng100-1
basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloMassType', 'SubhaloFlag', "SubhaloPos"]
haloFields = ["GroupMass", "GroupMassType", "GroupNsubs", "GroupPos", "GroupFirstSub"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)

subhaloFlag = subhalos["SubhaloFlag"]
subhaloMasses = subhalos["SubhaloMassType"]
subhaloMass = subhalos["SubhaloMass"]
subhaloDmMass = []
subhaloStellarMass = []

maxSH = len(subhaloMasses) #use whole data set
#maxH = len(haloMasses)
step = 100 #use a smaller sample. Set equal to 1 if you want all the data shown.
n = 0

for i in range (0,maxSH,step):
    n = n + 1
    mass = subhaloMass[i]
    dm = subhaloMasses[i][1]
    stellar = subhaloMasses[i][4]
    ratio = dm/mass
    if (subhaloFlag[i] > 0) and (mass>1) and ratio>0.7: 
        subhaloDmMass.append(dm*10**10)
        subhaloStellarMass.append(stellar*10**10)        

#Process data

d = {'DM': (subhaloDmMass), 'S': (subhaloStellarMass)}
dataSet = pd.DataFrame(data = d)
sns.lmplot(x="DM", y="S", data = dataSet, lowess=True, ci=None, scatter = False)
#sns.regplot(x="DM", y="S", data = dataSet)
print("For "+ str(n) + " subhalos.")
print("Process finished --- %s seconds ---" % int((time.time() - start_time)))


#Subhalo plot
area = np.pi*2
plt.scatter(subhaloDmMass,subhaloStellarMass, s=area, alpha=0.4, c="purple")
plt.axis([10**10, 10**14, 10**5, 10**14])
plt.xscale("log")
plt.yscale("log")

plt.title("Subhalo SHM, N = " + str(n))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
#plt.savefig("./fig/SHMR/Subhalos.png")
plt.show()
