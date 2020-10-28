"""
functions for doing statistical calculations
"""
import numpy as np

def median_values(df, datatype, x_key, y_key, ymin, ymax, bin_out=False):
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


def median_values_log_y(df, datatype, x_key, y_key, ymin=9, ymax=12, bin_out=False):
    if datatype == "sami":
        x_values = df[np.isnan(df[x_key]) == False][x_key]
        y_values = df[np.isnan(df[x_key]) == False][y_key]
    else:
        x_values = df[x_key]
        y_values = df[y_key]
    bins = np.logspace(ymin, ymax, 12)
    y_medians = np.zeros(len(bins) -1)
    x_medians = np.zeros(len(bins) -1)
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
