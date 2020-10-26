import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from matplotlib.ticker import ScalarFormatter

def log_formater(df):
    df_log = df.copy(deep=True)
    for key in df.keys():
        df_log[key] = np.log10(list(df[key]))
    return df_log

def VD_SM (title, ax, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'$\sigma$ [km/s]')
    ax.set_ylabel(r"Stellar mass [$ M_\odot $]")
    ax.grid(True, which="both", linestyle='--')
    ax.legend(loc = 4)

def VSigma_SM (title, ax, x0=0, x1=2.5, y0=10**9, y1=10**12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'$V_{max}/\sigma$')
    ax.set_ylabel(r"Stellar mass [$ M_\odot $]")
    ax.legend()

def Vmax_SM (title, ax, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'$V_{max}$ [km/s]')
    ax.set_ylabel(r"Stellar mass [$ M_\odot $]")
    ax.grid(True, which="both", linestyle='--')
    ax.legend()

def CV_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'$V_{circ}$ [km/s]')
    plt.ylabel(r"Stellar mass [$ M_\odot $]")
    plt.legend()

def C_SM (color, ax, x0=10**9, x1=10**12, y0=-1, y1=1):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_ylabel(color + " [mag]")
    ax.set_xlabel(r"Stellar mass [$ M_\odot $]")
    ax.legend(loc=4)
    
def PDF_C (color, ax):
    ax.set_ylabel("PDF")
    ax.set_xlabel(color + " color [mag]")
    ax.legend()

def HM_SM(title, ax, x0=10**11, x1=10**14, y0=10**(9.5), y1=10**(12)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'Halo mass [$ M_\odot $]')
    ax.set_ylabel(r"Stellar mass [$ M_\odot $]")
    ax.legend()

def R_SM (title, ax, x0=10**(-1), x1=10**2, y0=10**9, y1=10**13):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'Half light radius [kpc]')
    ax.set_ylabel(r"Stellar mass [$ M_\odot $]")
    ax.grid(True, which="both", linestyle='--')
    ax.legend()


def SM_R (title, ax, x0=10**(9), x1=10**13, y0=10**(-1), y1=10**2):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_ylabel(r'Half light radius [kpc]')
    ax.set_xlabel(r"Stellar mass [$ M_\odot $]")
    ax.grid(True, which="both", linestyle='--')
    ax.legend()

def R_VD (title, ax, x0=10**(-1), x1=10**2, y0=10**1.5, y1=10**2.5):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(r'Half light radius [kpc/h]')
    ax.set_ylabel(r'$\sigma$ [km/s]')
    ax.grid(True, which="both", linestyle='--')
    ax.legend(loc=4)

def SM_SFR (title, df, x0=10**9, x1=10**13, y0=10**(-4), y1=10**0):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'Stellar mass [$ M_\odot $]')
    plt.ylabel(r"sSFR [$ Gyr^{-1} $]")
    plt.legend()

def VD_BH (title, df, ax, x0=10**1, x1=10**3, y0=10**(6), y1=10**(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylabel(r"SMBH mass [$ M_\odot $]")
    ax.set_xlabel(r'$\sigma$ [km/s]')
    ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.legend()

def SM_BH (title, df, ax, x0=10**9, x1=10**(13), y0=10**(6), y1=10**(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylabel(r"SMBH mass [$ M_\odot $]")
    ax.set_xlabel(r"Stellar mass [$ M_\odot $]")
    ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.legend()

def DM_BH (title, df, ax, x0=10**10, x1=10**(14), y0=10**(6), y1=10**(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylabel(r"SMBH mass [$ M_\odot $]")
    ax.set_xlabel(r"DM mass [$ M_\odot $]")
    ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.legend()

def R_BH (title, df, ax, x0=10**0, x1=10**2, y0=10**(6), y1=10**(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylabel(r"SMBH mass [$ M_\odot $]")
    ax.set_xlabel(r'Half light radius [ckpc/h]')
    ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.legend()

def FP_3D(df):
    #make the figure
    fig = plt.figure(figsize = (9,6))
    ax = fig.gca(projection='3d')

    #plot the data
    x, y, z = [], [], []
    z = np.log10(list(df["SubhaloMassInHalfRadStellar"]))
    y = np.log10(list(df["SubhaloHalfmassRadStellar"]))
    x = np.log10(list(df["SubhaloVelDisp"]))
    s = list(df["SubhaloMass"])
    s = [(i/(10**(10)))**(1/2) for i in s]

    ax.scatter(xs = x, ys = y, zs = z, alpha=0.8, c=y, cmap=plt.get_cmap("magma"), s=s)

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
    ax.set_title("Fundamental Plane", fontsize=14)
    ax.set_zlabel('Mass')
    ax.set_ylabel('Radius')
    ax.set_xlabel('Velocity')
    ax.set_zlim(8, 13)
    ax.set_ylim(1, 4)
    ax.set_xlim(1, 3)
    return ax
