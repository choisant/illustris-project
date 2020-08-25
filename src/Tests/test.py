import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time

def doublePowerLaw(b, c, M1, N, x):
    y = 2*N*x*((x/M1)**(-b)+(x/M1)**(c))**(-1)
    return y

xmin = 10**10
xmax = 10**14
dx = 10**10
x=np.arange(xmin,xmax,dx)
y = doublePowerLaw(b = 1.376, c = 0.608,M1 = 10**11.590, N = 0.0351, x = x)

plt.plot(x,y)
plt.xscale("log")
plt.yscale("log")
plt.axis([10**8, 10**15, 10**8, 10**12.5])
plt.show()

#x=np.log10(x)
#y = np.log10(y)

plt.plot(np.log10(x),np.log10(y))
plt.show()
