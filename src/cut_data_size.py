import illustris_python as il
import pandas as pd
import numpy as np

basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloMassType', 'SubhaloFlag', "SubhaloLen"]
haloFields = ["GroupMass", "GroupMassType", "GroupNsubs", "GroupFirstSub"]
subhalos = il.groupcat.loadSubhalos(basePath,99,fields=subhaloFields)
halos = il.groupcat.loadHalos(basePath,99,fields=haloFields)

dfSubhalos = il.pandasformat.dictToPandas(subhalos)
dfHalos = il.pandasformat.dictToPandas(halos)

#Condition to drop data points
minStellarMass = 0.1 #*10**10 solar masses

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

def minYMass(df, x, Y, haloType):
    particleType = (haloType+"Mass"+Y)
    if haloType == "Subhalo":
        df = subhaloFlagDrop(df)
        df = darkMatterZeros(df)
    #Get indices that fail to meet this condition.
    indexNames = df[df[particleType] < x].index
    df.drop(indexNames, inplace = True)
    return df

def saveDataCSV(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".csv"
    f = open(path, "a+") #Create file if it does not already exist.
    newdf.to_csv(path)

def centralGalaxies(dfHalos, dfSubhalos):
    #dfHalos must have the key-value pair GroupFirstSub
    centralIndices = dfHalos["GroupFirstSub"]
    centralIndices = centralIndices[centralIndices > 0]
    centrals = dfSubhalos.iloc[centralIndices]
    return centrals
    
#newdf = minYMass(dfSubhalos, minStellarMass, Y = "DM", haloType = "Subhalo")
newdf = centralGalaxies(dfHalos, dfSubhalos)
newdf2 = minYMass(newdf, minStellarMass, Y = "Stellar", haloType = "Subhalo")

saveDataCSV(newdf2, haloType="Subhalo", filename = "Centrals_minE9_SM_SMHR", tngFolder = "tng100-1")
#saveDataCSV(newdf, haloType="Subhalo", filename = "minE9_DM", tngFolder = "tng100-1")

