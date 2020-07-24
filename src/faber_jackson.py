import illustris_python as il
import matplotlib.pyplot as plt
import numpy as np

basePath = "./data/Illustris-3/output"
fields = ['SubhaloMass','SubhaloVelDisp']
subhalos = il.groupcat.loadSubhalos(basePath,135,fields=fields)

mass_msun = subhalos["SubhaloMass"]*1e10/0.704
plt.plot(mass_msun,subhalos['SubhaloVelDisp'],'.')

#Comparative line
x = np.linspace(10**9,10**15,100)
y = x**0.25*0.1
#plt.plot([0, 10**14],[0,10**4])
plt.plot(x,y)

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Total Mass [$M_\odot$]")
plt.ylabel("Velocity dispersion [(km/s)]")
plt.savefig("./fig/test/faber_jackson.png")
plt.show()
