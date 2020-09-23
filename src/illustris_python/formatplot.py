import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

def VD_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'$\sigma$ [km/s]')
    plt.ylabel(r"Stellar half-light mass [$ M_\odot /h $]")
    plt.legend()

def Vmax_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'$V_{max}$ [km/s]')
    plt.ylabel(r"Stellar half-light mass [$ M_\odot /h $]")
    plt.legend()

def CV_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'$V_{circ}$ [km/s]')
    plt.ylabel(r"Stellar half-light mass [$ M_\odot /h $]")
    plt.legend()

def C_SM (type, ax, x0=10**9, x1=10**12, y0=-1, y1=1):
    ax.set(xlim = (x0, x1), ylim = (y0, y1))
    ax.set_xscale("log")
    ax.set_ylabel(type + " [mag]")
    ax.set_xlabel(r"Stellar mass [$ M_\odot /h $]")
    ax.legend(loc = 4)
    
def PDF_C (type, ax):
    ax.set_ylabel("PDF")
    ax.set_xlabel(type + " color [mag]")
    ax.legend()

def HM_SM_loglog (title, df, x0=11, x1=14, y0=9.5, y1=12):
    plt.axis([x0, x1, y0, y1])
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'log (Halo mass [$ M_\odot /h $])')
    plt.ylabel(r"log (Stellar mass [$ M_\odot /h $])")
    plt.legend()
    plt.show()

def R_SM (title, df, x0=10**1.5, x1=10**4, y0=10**9, y1=10**13):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Half light radius [kpc/h]')
    plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
    plt.legend()

def SM_SFR (title, df, x0=10**9, x1=10**13, y0=10**(-4), y1=10**0):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Stellar mass [$ M_\odot /h $]')
    plt.ylabel(r"sSFR [$ Gyr^{-1} $]")
    plt.legend()

def FP_3D(df):
    #make the figure
    fig = plt.figure(figsize = (9,6))
    ax = fig.gca(projection='3d')

    #plot the data
    x, y, z = [], [], []
    z = np.log10(list(df["SubhaloMassInHalfRadStellar"]))
    y = np.log10(list(df["SubhaloHalfmassRad"]))
    x = np.log10(list(df["SubhaloVelDisp"]))
    s = list(df["SubhaloMass"])
    s = [i**(1/2) for i in s]

    ax.scatter(xs = x, ys = y, zs = z, alpha=0.8, c=y, cmap=plt.get_cmap("magma"), s = s)

    #plane
    """
    FPz = np.arange(0,12, 0.25)
    FPy = np.arange(0,12, 0.25)
    FPz, FPy = np.meshgrid(FPz, FPy)
    FPx = 0.8*FPz-0.8*FPy -2
    # Plot the surface.
    ax.plot_surface(FPx, FPy, FPz, linewidth=0, antialiased=False, alpha = 0.2)
    """
    #Format
    ax.set_title("Fundamental Plane", fontsize = 14)
    ax.set_zlabel('Mass')
    ax.set_ylabel('Radius')
    ax.set_xlabel('Velocity')
    ax.set_zlim(8, 13)
    ax.set_ylim(1, 4)
    ax.set_xlim(1, 3)
    return ax
