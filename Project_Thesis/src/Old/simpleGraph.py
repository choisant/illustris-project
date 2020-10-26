import illustris_python as il
import matplotlib.pyplot as plt

#We will look at the subhalos of the catalog
basePath = "./data/Illustris-3/output"
fields = ['SubhaloMass','SubhaloSFRinRad']
subhalos = il.groupcat.loadSubhalos(basePath,135,fields=fields)
print(subhalos) #this is a dictionary
print(subhalos.keys()) #These are the keys
print(subhalos["SubhaloMass"].shape) #This is the total number of subhalos

mass_msun = subhalos["SubhaloMass"]*1e10/0.704
plt.plot(mass_msun,subhalos['SubhaloSFRinRad'],'.')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Total Mass [$M_\odot$]")
plt.ylabel("Star Formation Rate [$M_\odot / yr$")
plt.savefig("./fig/test/simpleGraph.png")
plt.show()