import pandas as pd
import numpy as np

#takes in a dictionary

#debugging
data1 = {
    "count": 4,
    "velocity": [12, 14, 1],
    "mass": np.array([10, 23, 67]),
    "SubhaloMassType": (np.array([[0.11, 5.44, 6.88, 2.99, 21.4, 7.33], [0.11, 5.44, 6.88, 2.99, 1.44, 7.33], [0.11, 5.44, 6.88, 2.99, 5.34, 7.33]])),
    "flag": [True, True, False]
}


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

df = dictToPandas(data1)