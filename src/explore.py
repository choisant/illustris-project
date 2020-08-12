import illustris_python as il
import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.time()


#tng100-1
basePath = "./data/tng100-1/output"
subhaloFields = ['SubhaloMassType', 'SubhaloFlag', "SubhaloPos","SubhaloParent"]
haloFields = ["GroupMassType", "GroupNsubs", "GroupPos", "GroupFirstSub"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)



centrals=halos["GroupFirstSub"]
parents=subhalos["SubhaloParent"]
subhaloPos = subhalos["SubhaloPos"]
haloPos = halos["GroupPos"]
subhaloMasses = subhalos["SubhaloMassType"]
subhaloFlag = subhalos["SubhaloFlag"]

n = len(centrals)
count=0
check=0
#print(len(centrals))
#print(len(parents))
#print(len(subhaloMasses))
a=centrals[-1]+3

for i in range(n):
    #print(centrals[i])
    N=centrals[i]
    if N<0:
        count = count + 1
    else:
        if parents[N]==0:
            check=check+1
    
    #if (subhaloFlag[i] > 0) and (subhaloPos[i] in haloPos): #this takes a LONG time for such a big dataset
     #   count=count+1
        
print (n-count)
print (check)
print(len(parents))
print("For "+ str(n) + " subhalos, " + str(count) + " centrals were found.")
print("Process finished --- %s seconds ---" % int((time.time() - start_time)))
