import illustris_python as il
import matplotlib.pyplot as plt
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

numberOfSubhalos = halos["GroupNsubs"]
centralHalos = halos["GroupFirstSub"]
haloMasses = halos["GroupMassType"]
haloMass = halos["GroupMass"]
haloDmMass = []
haloStellarMass = []

centralHaloDmMass = []
centralHaloStellarMass = []
centrals = 0
fieldHaloDmMass = []
fieldHaloStellarMass = []
fields = 0

maxSH = len(subhaloMasses) #use whole data set
maxH = len(haloMasses)
step = 1 #use a smaller sample. Set equal to 1 if you want all the data shown.
n = 0

for i in range (0,maxSH,step):
    n = n + 1
    mass = subhaloMass[i]
    dm = subhaloMasses[i][1]
    stellar = subhaloMasses[i][4]
    ratio = dm/mass
    if (subhaloFlag[i] > 0) and (mass>1) and ratio>0.5: 
        subhaloDmMass.append(dm*10**10)
        subhaloStellarMass.append(stellar*10**10)        


for i in range (0,maxH, step):
    mass = haloMass[i]
    dm = haloMasses[i][1]
    stellar = haloMasses[i][4]
    ratio = dm/mass
    m = centralHalos[i]
    if (mass >1) and (ratio>0.5):
        if numberOfSubhalos[i] == 1:
            fields = fields + 1
            fieldHaloDmMass.append(dm*10**10)
            fieldHaloStellarMass.append(stellar*10**10)
        if m>0:
            centralHaloDmMass.append(subhaloMasses[m][1]*10**10)
            centralHaloStellarMass.append(subhaloMasses[m][4]*10**10)
            centrals = centrals +1

print("For "+ str(n) + " subhalos, " + str(centrals) + " centrals and " + str(fields) + " field galaxies were found.")
print("Process finished --- %s seconds ---" % int((time.time() - start_time)))

#Subhalo plot
area = np.pi*2
plt.scatter(subhaloDmMass,subhaloStellarMass, s=area, alpha=0.5)
plt.axis([10**10, 10**14, 10**5, 10**14])
plt.xscale("log")
plt.yscale("log")

plt.title("Subhalo SHM, N = " + str(n))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
#plt.savefig("./fig/SHMR/Subhalos.png")
plt.show()

#Only field galaxies plot
area = np.pi*2
plt.scatter(fieldHaloDmMass,fieldHaloStellarMass, s=area, alpha=0.5)
plt.axis([10**10, 10**12, 10**4, 10**11])
plt.xscale("log")
plt.yscale("log")

plt.title("Field Galaxies SHM, N = " + str(fields))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$M_\odot /h $]")
#plt.savefig("./fig/SHMR/FieldHalos.png")
plt.show()


#Only central galaxies plot
area = np.pi*2
plt.scatter(centralHaloDmMass,centralHaloStellarMass, s=area, alpha=0.5)
plt.axis([10**8, 10**15, 10**5, 10**13])
plt.xscale("log")
plt.yscale("log")

plt.title("Central Galaxy SHM, N = " + str(centrals))
plt.xlabel(r'Halo mass [$ M_\odot /h $]')
plt.ylabel(r"Stellar mass [$M_\odot /h $]")
#plt.savefig("./fig/SHMR/CentralHalos.png")
plt.show()

