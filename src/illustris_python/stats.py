"""
functions for doing statistical calculations
"""
import math
import numpy as np
from sklearn.linear_model import LinearRegression
from uncertainties.umath import *
from uncertainties import ufloat


def median_values(df, datatype, x_key, y_key, ymin=9, ymax=12, bin_out=False):
    """
    Takes in a dataframe and creates bins along y_key-axis. Returns median values.
    """
    if datatype == "sami":
        x_values = df[np.isnan(df[x_key]) == False][x_key]
        y_values = df[np.isnan(df[x_key]) == False][y_key]
    else:
        x_values = df[x_key]
        y_values = df[y_key]
    bins = np.linspace(ymin, ymax, 8)
    x_medians = np.zeros(len(bins) -1)
    y_medians = np.zeros(len(bins) -1)
    for i in range(len(y_medians)):
        larger = y_values[y_values > bins[i]].index
        smaller = y_values[y_values < bins[i+1]].index
        indices = list(set(larger) & set(smaller))
        binlist_x = np.zeros(len(indices))
        binlist_y = np.zeros(len(indices))
        for j in range(len(indices)):
            binlist_x[j] = x_values[indices[j]]
            binlist_y[j] = y_values[indices[j]]
        x_medians[i] = np.median(binlist_x)
        y_medians[i] = np.median(binlist_y)
    if bin_out:
        return x_medians, y_medians, bins
    else:
        return x_medians, y_medians


def median_values_log_y(df, datatype, x_key, y_key, ymin=9, ymax=12, n=12, error_out=False):
    if datatype == "sami":
        x_values = df[np.isnan(df[x_key]) == False][x_key]
        y_values = df[np.isnan(df[x_key]) == False][y_key]
    else:
        x_values = df[x_key]
        y_values = df[y_key]
    bins = np.logspace(ymin, ymax, n)
    y_medians = np.zeros(len(bins) -1)
    x_medians = np.zeros(len(bins) -1)
    y_errors = np.zeros((2, len(bins)-1))
    x_errors = np.zeros((2, len(bins)-1))
    for i in range(len(y_medians)):
        larger = y_values[y_values > bins[i]].index
        smaller = y_values[y_values < bins[i+1]].index
        indices = list(set(larger) & set(smaller))
        binlist_x = np.zeros(len(indices))
        binlist_y = np.zeros(len(indices))
        for j in range(len(indices)):
            binlist_x[j] = x_values[indices[j]]
            binlist_y[j] = y_values[indices[j]]
        x_medians[i] = np.median(binlist_x)
        y_medians[i] = np.median(binlist_y)
        if len(binlist_x>0):
            x_errors[0][i] = x_medians[i] - np.percentile(a=binlist_x, q=25)
            x_errors[1][i] = np.percentile(binlist_x, 75) - x_medians[i]
            y_errors[0][i] = y_medians[i] - np.percentile(binlist_y, 25)
            y_errors[1][i] = np.percentile(binlist_y, 75) - y_medians[i]

    if error_out:
        return x_medians, y_medians, x_errors, y_errors
    else:
        return x_medians, y_medians

def log_errors(x_errors, y_errors, x_medians, y_medians):
    y_e = np.zeros((2, len(x_medians)))
    x_e = np.zeros((2, len(x_medians)))
    x_e[0] = x_errors[0]/(x_medians*np.log(10))
    x_e[1] = x_errors[1]/(x_medians*np.log(10))
    y_e[0] = y_errors[0]/(y_medians*np.log(10))
    y_e[1] = y_errors[1]/(y_medians*np.log(10))
    return x_e, y_e


def lin_reg(X, Y, xmin=1, xmax=3):
    x = X.reshape((-1,1))
    y = Y.reshape((-1,1))
    x_out = np.linspace(xmin, xmax, len(X))
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x,y)
    intercept =  model.intercept_
    print('slope:', model.coef_)
    print('intercept:', intercept)
    print('R^2:', r_sq)
    y_pred_list = model.intercept_ + model.coef_ *x_out
    y_pred = y_pred_list.reshape(1,-1)[0]
    return x_out, y_pred
    
def error_estimate_behroozi(a, M1, c, d, e, delta_a, delta_M1, delta_c, delta_d, delta_e, x):
    x = list(np.log10(x))
    a = ufloat(a, delta_a, tag="a")
    M1 = ufloat(M1, delta_M1, tag="M1")
    c = ufloat(c, delta_c, tag="c")
    d = ufloat(d, delta_d, tag="d")
    e = ufloat(e, delta_e, tag="e")
    def f(x):
        f = -log10(10**(a*x)+1)+d*((log10(1+exp(x)))**c)/(1+exp(10-x))
        return f
    Y_log = list(np.zeros(len(x)))
    for i in range(len(x)):
        Y_log[i] = log10(10**e*10**M1) +f(log10(x[i]/M1)) - f(0)
    Y_log_errors = np.zeros(len(Y_log))
    for i in range(len(Y_log)):
        Y_log_errors[i] = Y_log[i].s
    return Y_log_errors

#X=np.array([9,10,11,12])
#error_estimate_behroozi(a=-1.412, M1=(11.514), c=0.316, d=3.508, e=(-1.777), delta_a=0.02, delta_M1=0.053, delta_c=0.076, delta_d=0.087, delta_e=0.053, x=X)