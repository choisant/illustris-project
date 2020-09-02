import illustris_python as il
import pandas as pd
import numpy as np

"""
This script takes in the Group catalog data from the .hdf5 files, and uses the pandasformat.py file to convert the data to the pandas DataFrame format.
The data is then run through the desired filter, and saved as a .csv file in the cutdata folder of the relevant simulation.
"""
#read in data
basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloMassType', 'SubhaloFlag', "SubhaloLen", "SubhaloSFR", "SubhaloVel", "SubhaloVelDisp", "SubhaloHalfmassRad", "SubhaloMassInHalfRadType"]
haloFields = ["GroupMass", "GroupMassType", "GroupNsubs", "GroupFirstSub"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)

dfSubhalos = il.pandasformat.dictToPandas(subhalos)
dfHalos = il.pandasformat.dictToPandas(halos)

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
    centralIndices = dfHalos["GroupFirstSub"]
    centralIndices = centralIndices[centralIndices > 0]
    centrals = dfSubhalos.iloc[centralIndices]
    return centrals

def lateTypeSFR(df):
    df["SubhalosSFR"]  = df["SubhaloSFR"]/df["SubhaloMassStellar"]
    df["SubhalosSFR"] *=10**(-1) #sSFR in unit Gyr^(-1)
    indexNames1 = df[df["SubhalosSFR"] > 0.36].index
    df.drop(indexNames1, inplace = True)
    indexNames2 = df[df["SubhalosSFR"] < 0.036].index
    df.drop(indexNames2, inplace = True)
    return df

def earlyTypeSFR(df):
    df["SubhalosSFR"]  = df["SubhaloSFR"]/df["SubhaloMassStellar"]
    df["SubhalosSFR"] *= 10**(-1) #sSFR in unit Gyr^(-1)
    indexNames = df[df["SubhalosSFR"] > 0.01148].index
    df.drop(indexNames, inplace = True)
    return df

def lateTypeKinetic(df):
    #Use "Stellar Circularities, Angular Momenta, Axis Ratios" Genel catalogue
    #df.drop(indexNames2, inplace = True)
    return df

def earlyTypeKinetic(df):
    #Use "Stellar Circularities, Angular Momenta, Axis Ratios" Genel catalogue
    #df.drop(indexNames, inplace = True)
    return df

def lateTypeGas(df):
    df["SubhaloGasFraction"]  = df["SubhaloMassInHalfRadGas"]/df["SubhaloMassInHalfRadStellar"]
    indexNames = df[df["SubhaloGasFraction"] < 0.1].index #Ferrero2020
    df.drop(indexNames, inplace = True)
    return df

def earlyTypeGas(df):
    df["SubhaloGasFraction"]  = df["SubhaloMassInHalfRadGas"]/df["SubhaloMassInHalfRadStellar"]
    indexNames = df[df["SubhaloGasFraction"] > 0.1].index #Ferrero2020
    df.drop(indexNames, inplace = True)
    return df

#Saving the data in the correct format
def saveDataCSV(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".csv"
    f = open(path, "a+") #Create file if it does not already exist.
    df.to_csv(path)

def saveDataPickle(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".pkl"
    f = open(path, "a+") #Create file if it does not already exist.
    df.to_pickle(path)

newdf = centralGalaxies(dfHalos, dfSubhalos)
#dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_SFR.csv"
#newdf = pd.read_csv(dataPath)

newdf2 = minYMass(newdf, minMass = 0.1, Y = "Stellar", haloType = "Subhalo")
lates = lateTypeSFR(newdf2)
#saveDataCSV(lates, haloType="Subhalo", filename = "Centrals_minE9_SM_lateType_Gas", tngFolder = "tng100-1")
saveDataPickle(lates, haloType="Subhalo", filename = "Centrals_minE9_SM_lateType_SFR", tngFolder = "tng100-1")
#earlies = earlyTypeGas(newdf)
#saveDataPickle(earlies, haloType="Subhalo", filename = "Centrals_minE9_SM_earlyType_Gas", tngFolder = "tng100-1")