import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from matplotlib.ticker import ScalarFormatter

TEXTSIZE = 16

def log_formater(df):
    df_log = df.copy(deep=True)
    for key in df.keys():
        if key != "cataid":
            df_log[key] = np.log10(list(df[key]))
    return df_log

def VD_SM(title, ax, x0=1.5, x1=3, y0=9, y1=12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_xlabel(r'log($\sigma$ [km/s])', fontsize=TEXTSIZE)
    ax.set_ylabel(r"log($M_*$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='--')
    ax.legend(loc = 4)

def VSigma_SM(title, ax, x0=0, x1=2.5, y0=10**9, y1=10**12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_xlabel(r'$V_{max}/\sigma$', fontsize=TEXTSIZE)
    ax.set_ylabel(r"$M_*$ [$ M_\odot $]", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def Vmax_SM(title, ax, x0=1.5, x1=2.5, y0=9, y1=12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_xlabel(r'log ($V_{max}$ [km/s])', fontsize=TEXTSIZE)
    ax.set_ylabel(r"log ($M_*$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def CV_SM(title, ax, x0=1.5, x1=2.5, y0=9, y1=12):
    plt.axis([x0, x1, y0, y1])
    plt.title(title)
    plt.xlabel(r'log($V_{circ}$ [km/s])', fontsize=TEXTSIZE)
    plt.ylabel(r"log($M_*$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    plt.legend()

def C_SM(color, ax, x0=9, x1=12, y0=-1, y1=1):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_ylabel(color + " [mag]", fontsize=TEXTSIZE)
    ax.set_xlabel(r"$M_*$ [$ M_\odot $]", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.legend(loc=4)
    
def PDF_C(color, ax):
    ax.set_ylabel("PDF", fontsize=TEXTSIZE)
    ax.set_xlabel(color + " color [mag]", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.legend()

def HM_SM(title, ax, x0=11, x1=14, y0=(9.0), y1=(12)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_xlabel(r'log($M_{halo}$ [$ M_\odot $])', fontsize=TEXTSIZE)
    ax.set_ylabel(r'log($M_{*}$ [$ M_\odot $])', fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def R_SM(title, ax, x0=(-1), x1=2, y0=9, y1=12):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_xlabel(r'log($r_e$ [kpc])', fontsize=TEXTSIZE)
    ax.set_ylabel(r'log($M_*$ [$ M_\odot $])', fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend(loc=4)


def SM_R(title, ax, x0=(9), x1=13, y0=(-1), y1=2):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    #ax.set_title(title)
    ax.set_ylabel(r'log($r_e$ [kpc])', fontsize=TEXTSIZE)
    ax.set_xlabel(r"log($M_*$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def R_VD(title, ax, x0=(-1), x1=2, y0=1.5, y1=3):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))

    #ax.set_title(title)
    ax.set_xlabel(r'log($r_e$ [kpc/h])', fontsize=TEXTSIZE)
    ax.set_ylabel(r'log($\sigma$ [km/s])', fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    ax.legend(loc=4)

def SM_SFR(title, df, x0=9, x1=13, y0=(-4), y1=0):
    plt.axis([x0, x1, y0, y1])
    #plt.title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    plt.xlabel(r'log($M_*$ [$ M_\odot $])', fontsize=TEXTSIZE)
    plt.ylabel(r"log(sSFR [$ Gyr^{-1} $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    ax.grid(True, which="both", linestyle='-')
    plt.legend()

def VD_BH(title, df, ax, x0=1, x1=3, y0=(6), y1=(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_ylabel(r"log($M_{BH}$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.set_xlabel(r'log($\sigma$ [km/s])', fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    #ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def SM_BH(title, df, ax, x0=9, x1=(13), y0=(6), y1=(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_ylabel(r"log($M_{BH}$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.set_xlabel(r"log($M_*$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    #ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def DM_BH(title, df, ax, x0=10, x1=(14), y0=(6), y1=(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_ylabel(r"log($M_{BH}$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.set_xlabel(r"log($M_{DM}$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    #ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.grid(True, which="both", linestyle='-')
    ax.legend()

def R_BH(title, df, ax, x0=0, x1=2, y0=(6), y1=(10)):
    ax.set(xlim=(x0, x1), ylim=(y0, y1))
    ax.set_ylabel(r"log($M_{BH}$ [$ M_\odot $])", fontsize=TEXTSIZE)
    ax.set_xlabel(r'log($r_e$ [ckpc/h])', fontsize=TEXTSIZE)
    ax.tick_params(labelsize=TEXTSIZE)
    #ax.set_title(title + ", N = " + str(len(df["SubhaloMassDM"])))
    ax.grid(True, which="both", linestyle='-')
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