import illustris_python as il
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

"""
This script takes in the Group catalog data from the .hdf5 files, and uses the pandasformat.py file to convert the data to the pandas DataFrame format.
The data is then run through the desired filter, and saved as a .pkl file in the cutdata folder of the relevant simulation.
"""

#filters
def subhaloFlagDrop (df):
    indexNames = df[df["SubhaloFlag"] == 0].index
    df.drop(indexNames, inplace = True)
    return df

def darkMatterZeros (df):
    indexNames = df[df["SubhaloMassDM"] == 0].index
    df.drop(indexNames, inplace = True)
    return df

def minParticles (df, minPart):
    print("Removing galaxies below the minimum mass.")
    indexNames = df[df["SubhaloLen"] < minPart].index
    df.drop(indexNames, inplace = True)
    return df

def minYMass(df, minMass, Y, haloType):
    particleType = (haloType+"Mass"+Y)
    if haloType == "Subhalo":
        df = subhaloFlagDrop(df)
        df = darkMatterZeros(df)
    #Get indices that fail to meet this condition.
    indexNames = df[df[particleType] < minMass].index
    df.drop(indexNames, inplace = True)
    return df

def centralGalaxies(dfHalos, dfSubhalos):
    #dfHalos must have the key-value pair GroupFirstSub
    print("Starting the central galaxies sorting")
    centralIndices = dfHalos["GroupFirstSub"]
    centralIndices = centralIndices[centralIndices > 0]
    centrals = dfSubhalos.iloc[centralIndices]
    return centrals

def lateTypeSFR(df):
    df_copy = df.copy(deep=True)
    indexNames1 = df_copy[df_copy["SubhalosSFR"] > 0.36].index
    df_copy.drop(indexNames1, inplace = True)
    indexNames2 = df_copy[df_copy["SubhalosSFR"] < 0.036].index
    df_copy.drop(indexNames2, inplace = True)
    return df_copy

def earlyTypeSFR(df):
    df_copy = df.copy(deep=True)
    indexNames = df_copy[df_copy["SubhalosSFR"] > 0.01148].index
    df_copy.drop(indexNames, inplace = True)
    return df_copy

def lateTypeGas(df):
    df_copy = df.copy(deep=True)
    df_copy["SubhaloGasFraction"]  = df_copy["SubhaloMassInHalfRadGas"]/df_copy["SubhaloMassInHalfRadStellar"]
    indexNames = df_copy[df_copy["SubhaloGasFraction"] < 0.1].index #Ferrero2020
    df_copy.drop(indexNames, inplace = True)
    return df_copy

def earlyTypeGas(df):
    df_copy = df.copy(deep=True)
    df_copy["SubhaloGasFraction"]  = df_copy["SubhaloMassInHalfRadGas"]/df_copy["SubhaloMassInHalfRadStellar"]
    indexNames = df_copy[df_copy["SubhaloGasFraction"] > 0.1].index #Ferrero2020
    df_copy.drop(indexNames, inplace = True)
    return df_copy

#Saving the data in the correct format
def saveDataCSV(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".csv"
    f = open(path, "a+") #Create file if it does not already exist.
    df.to_csv(path)

def saveDataPickle(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".pkl"
    f = open(path, "a+") #Create file if it does not already exist.
    df.to_pickle(path)

#read in data

basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloMassType', 'SubhaloFlag', "SubhaloLen", "SubhaloSFR", 
                "SubhaloVel", "SubhaloVelDisp", "SubhaloHalfmassRadType", "SubhaloMassInHalfRadType", 
                "SubhaloMassInHalfRad", "SubhaloVmax", "SubhaloStellarPhotometrics", "SubhaloBHMass"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
dfSubhalos = il.pandasformat.dictToPandas(subhalos)
dfSubhalos = il.pandasformat.stellarMasses(dfSubhalos)
print("Changed the masses to stellar masses.")
dfSubhalos = il.pandasformat.ssfr(dfSubhalos)
print("added ssfr")

haloFields = ["GroupMass", "GroupMassType", "GroupNsubs", "GroupFirstSub"]
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)
dfHalos = il.pandasformat.dictToPandas(halos)
print("Done converting to pandas DataFrame")
"""
minSM = minYMass(dfSubhalos, minMass = 10**9, Y = "Stellar", haloType = "Subhalo")
saveDataPickle(minSM, haloType="Subhalo", filename = "MinE9_SM", tngFolder = "tng100-1")
"""
centrals = centralGalaxies(dfHalos, dfSubhalos)
centralsMinMass = minYMass(centrals, minMass = 10**9, Y = "Stellar", haloType = "Subhalo")
saveDataPickle(centralsMinMass, haloType ="Subhalo", filename = "Centrals_minE9_SM", tngFolder = "tng100-1")

lates = lateTypeGas(centralsMinMass)
saveDataPickle(lates, haloType="Subhalo", filename = "Centrals_minE9_SM_lateType_Gas", tngFolder = "tng100-1")

earlies = earlyTypeGas(centralsMinMass)
saveDataPickle(earlies, haloType="Subhalo", filename = "Centrals_minE9_SM_earlyType_Gas", tngFolder = "tng100-1")
#saveDataCSV(earlies, haloType="Subhalo", filename = "Centrals_minE9_SM_earlyType_Gas", tngFolder = "tng100-1")