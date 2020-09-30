import pandas as pd
import numpy as np
from operator import truediv 

def dictToPandas(data):
    keyList = list(data.keys())
    for key in keyList:
        if key != "count":
            dummy = data[key]
            data[key] = list(dummy)

        if key == "SubhaloMassType" or key == "GroupMassType":
            particleTypes = {"SubhaloMassGas": 0, 
                            "SubhaloMassDM": 1, 
                            "None": 2, 
                            "SubhaloMassTracers": 3, 
                            "SubhaloMassStellar": 4, 
                            "SubhaloMassBH": 5}
            masses = np.array(data[key]) #create Series object
            for particle in particleTypes:
                temp = masses[:,particleTypes[particle]]
                data[particle] = list(temp)
            data.pop(key)

        if key == "SubhaloMassInHalfRadType" or key == "GroupMassInHalfRadType":
            particleTypes = {"SubhaloMassInHalfRadGas": 0, 
                            "SubhaloMassInHalfRadDM": 1, 
                            "SubhaloMassInHalfRadNone": 2, 
                            "SubhaloMassInHalfRadTracers": 3, 
                            "SubhaloMassInHalfRadStellar": 4, 
                            "SubhaloMassInHalfRadBH": 5}
            masses = np.array(data[key]) #create Series object
            for particle in particleTypes:
                temp = masses[:,particleTypes[particle]]
                data[particle] = list(temp)
            data.pop(key)

    df = pd.DataFrame(data, dtype=object)
    return df

def stellarMasses(df):
    particleTypes = ["SubhaloMassGas", 
                        "SubhaloMassDM",  
                        "SubhaloMassStellar", 
                        "SubhaloMassBH",
                        "SubhaloMassInHalfRadGas", 
                        "SubhaloMassInHalfRadDM",  
                        "SubhaloMassInHalfRadStellar", 
                        "SubhaloMass",
                        "SubhaloMassInHalfRad",
                        "SubhaloBHMass"]
    
    for particle in particleTypes:
        print(particle + "...")
        df[particle] *= 10**10 #changes the units to stellar mass
    return df

def ssfr(df):
    keys = df.keys()
    if "SubhaloSFR" in keys:
        df["SubhalosSFR"]  = df["SubhaloSFR"]/df["SubhaloMassStellar"]
        df["SubhalosSFR"] *= 10**(9) #sSFR in unit Gyr^(-1)
    return df