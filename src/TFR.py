import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_lateType_Gas.pkl"
df1 = pd.read_pickle(dataPath)

G = 4.3*10**(-3) #pc*M^-1*(km/s)^2
h = 0.678 #Planck 2015

def velocities(df):
    df["SubhaloMassInHalfRadStellar"] *=10**10
    velocities = []
    velocities= (df["SubhaloMassInHalfRad"]/(df["SubhaloHalfmassRad"]))
    velocities = velocities**(1/2)
    velocities *=math.sqrt(G*10**(10)/(10**3))
    print(velocities)
    df["SubhaloCircVel"]= velocities
    return df

df1=velocities(df1)

ax = df1.plot.scatter(x="SubhaloCircVel", y="SubhaloMassInHalfRadStellar",s=1)
il.formatplot.CV_SM(title = "Tully Fisher relation", df=df1, x0=10**1)
plt.show()