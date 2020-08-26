import illustris_python as il
import pandas as pd
import numpy as np

"""
This script takes in the Group catalog data from the .hdf5 files, and uses the pandasformat.py file to convert the data to the pandas DataFrame format.
The data is then run through the desired filter, and saved as a .csv file in the cutdata folder of the relevant simulation.
"""
#read in data
basePath = "./data/tng100-1/output"
subhaloFields = ["SubhaloMass", 'SubhaloMassType', 'SubhaloFlag', "SubhaloLen"]
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

#Saving the data in the correct format
def saveDataCSV(df, haloType, filename, tngFolder):
    path = "./data/"+tngFolder+"/cutdata/"+haloType+"_"+filename+".csv"
    f = open(path, "a+") #Create file if it does not already exist.
    newdf.to_csv(path)
    
#newdf = minYMass(dfSubhalos, minStellarMass, Y = "DM", haloType = "Subhalo")
newdf = centralGalaxies(dfHalos, dfSubhalos)
newdf2 = minYMass(newdf, minMass = 0.1, Y = "Stellar", haloType = "Subhalo")

#saveDataCSV(newdf2, haloType="Subhalo", filename = "Centrals_minE9_SM_SMHR", tngFolder = "tng100-1")