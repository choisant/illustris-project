import illustris_python as il
import matplotlib.pyplot as plt
import numpy as np

#tng100-1
basePath = "./data/tng100-1/output"
subhaloFields = ['SubhaloMassType', 'SubhaloFlag', "SubhaloPos"]
haloFields = ["GroupMassType", "GroupNsubs", "GroupPos"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)

subhaloFlag = subhalos["SubhaloFlag"]
subhaloMasses = subhalos["SubhaloMassType"]
subhaloDmMass = []
subhaloStellarMass = []

subhaloPos = subhalos["SubhaloPos"]
haloPos = halos["GroupPos"]
centralHaloDmMass = []
centralHaloStellarMass = []

numberOfSubhalos=halos["GroupNsubs"]
haloMasses = halos["GroupMassType"]
haloDmMass = []
haloStellarMass = []

fieldHaloDmMass = []
fieldHaloStellarMass = []
fields = 0

N= 100 #len(haloMasses)
for i in range (0, N):
    if haloMasses[i][1] >0.01:
        haloDmMass.append(haloMasses[i][1]*10**10)
        haloStellarMass.append(haloMasses[i][4]*10**10)
        if numberOfSubhalos[i] == 1:
            fields = fields + 1
            fieldHaloDmMass.append(haloMasses[i][1]*10**10)
            fieldHaloStellarMass.append(haloMasses[i][4]*10**10)

print(fields)

n = 1000 #len(subhaloMasses)
lost = 0

for i in range (n):
    if (subhaloFlag[i] > 0) and subhaloMasses[i][1]>0.01:
        subhaloDmMass.append(subhaloMasses[i][1]*10**10)
        subhaloStellarMass.append(subhaloMasses[i][4]*10**10)
        """
        if subhaloMasses[i][1]>1:
            if subhaloPos[i] in haloPos: #this takes a LONG time for such a big dataset
                centralHaloDmMass.append(subhaloMasses[i][1]*10**10)
                centralHaloStellarMass.append(subhaloMasses[i][4]*10**10)
        """
    else:
        lost = lost+1

#Subhalo plot
area = np.pi*2
plt.scatter(subhaloDmMass,subhaloStellarMass, s=area, alpha=0.5)
plt.axis([10**8, 10**14, 10**5, 10**14])
plt.xscale("log")
plt.yscale("log")

plt.title("Subhalo SHM")
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
plt.savefig("./fig/SHMR/initialPlotSubhalos.png")
plt.show()

"""
#All halos plot
area = np.pi*2
plt.scatter(haloDmMass,haloStellarMass, s=area, alpha=0.5)
plt.axis([10**8, 10**15, 10**6, 10**14])
plt.xscale("log")
plt.yscale("log")

plt.title("Halo SHM")
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$M_\odot /h $]")
plt.savefig("./fig/SHMR/initialPlotHalos.png")
plt.show()

#Only field galaxies plot
area = np.pi*2
plt.scatter(fieldHaloDmMass,fieldHaloStellarMass, s=area, alpha=0.5)
plt.axis([10**8, 10**12, 10**6, 10**10])
plt.xscale("log")
plt.yscale("log")

plt.title("Field Halo SHM")
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$M_\odot /h $]")
plt.savefig("./fig/SHMR/initialPlotFieldHalos.png")
plt.show()
"""