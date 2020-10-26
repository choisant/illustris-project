import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

dataPath1 = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_earlyType_Gas.pkl"
data = pd.read_pickle(dataPath1)

data["SubhaloMassInHalfRadStellar"] *=10**10 #Stellar mass in normal units
data["SubhaloHalfmassRad"] *=10 #Units in km/s

"""
x, y, z = [], [], []
x = np.log10(list(data["SubhaloMassInHalfRadStellar"]))
y = np.log10(list(data["SubhaloHalfmassRad"]))
z = np.log10(list(data["SubhaloVelDisp"]))

FP = plt.figure().gca(projection='3d')
FP.scatter(xs = x, ys = y, zs = z, c =("red"), s=1)
FP.set_xlabel('Mass')
FP.set_ylabel('Radius')
FP.set_zlabel('Velocity')
"""
fig = il.formatplot.FP_3D(data)

plt.show()
