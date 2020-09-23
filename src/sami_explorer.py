import illustris_python as il
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("./data/SAMI/dr1.csv")

ser1 = data["colour_auto_g_i"]
ser1.plot.kde()
plt.show()