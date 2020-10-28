import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
dataPath = "./data/tng100-1/cutdata/Subhalo_Centrals_minE9_SM_lateType_Gas.pkl"
df1 = pd.read_pickle(dataPath)

G = 4.3*10**(-3) #pc*M^-1*(km/s)^2

def velocities(df):
    df["SubhaloMassInHalfRadStellar"] *=10**10
    velocities = []
    #velocities= (df["SubhaloMassInHalfRad"]/(df["SubhaloHalfmassRad"]))
    #velocities = velocities**(1/2)
    #velocities *=math.sqrt(G*10**(10)/(10**3))
    velocities = ((df["SubhaloMassInHalfRad"]/(df["SubhaloHalfmassRad"]))**(1/2))*math.sqrt(G*10**(10)/(10**3))
    print(velocities)
    df["SubhaloCircVel"]= velocities
    return df

df1=velocities(df1)
df1["SubhaloHalfmassRad"] *=10 #Units in km/s
df1["SubhaloMassInHalfRadGas"] *=10**10
df1["SubhaloMassInHalfRadBaryonic"] = df1["SubhaloMassInHalfRadStellar"]+df1["SubhaloMassInHalfRadGas"]
ax = df1.plot.scatter(x="SubhaloCircVel", y="SubhaloMassInHalfRadBaryonic",s=1, label = "TNG-100")

#Power law
x = np.linspace(0, 200)
y= x**(3.6)*10**4.1
plt.plot(x, y, color = "orange", label = r"$\gamma$ = 3.6")
il.formatplot.CV_SM(title = "Tully Fisher relation", df=df1, x0=10**1)

plt.show()


#df1.plot.scatter(x="SubhaloCircVel", y="SubhaloMassInHalfRadBaryonic",s=1, label = "TNG-100", alpha=0.8, color="crimson")
#il.formatplot.R_SM(title="Effective radius", df = df1, x0= 10**2, x1= 10**4)