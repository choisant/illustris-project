import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#data.to_csv("./data/SAMI/earlies.csv")

sami = pd.read_csv("./data/SAMI/allData.csv")
earlies = sami[sami["morph"] == 0]
lates = sami[sami["morph"] == 2]

earlies.to_csv("./data/SAMI/earlies.csv")
lates.to_csv("./data/SAMI/lates.csv")

