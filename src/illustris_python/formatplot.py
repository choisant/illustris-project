import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def VD_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    #plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'Velocity [km/s]')
    plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
    plt.legend()

def CV_SM (title, df, x0=10**1.5, x1=10**2.5, y0=10**9, y1=10**12):
    plt.axis([x0, x1, y0, y1])
    plt.xscale("log")
    plt.yscale("log")
    plt.title(title + ", N = " + str(len(df["SubhaloMassStellar"])))
    plt.xlabel(r'Velocity [km/s]')
    plt.ylabel(r"Stellar mass [$ M_\odot /h $]")
    plt.legend()

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

