import pandas as pd

#data.to_csv("./data/SAMI/earlies.csv")

morph_key = "Morph_dilyar"
sami = pd.read_csv("./data/SAMI/STELLAR_Details.csv")

earlies = sami[sami[morph_key] == 0]
lates = sami[sami[morph_key] >= 1]
indexNames = lates[lates[morph_key] == 3].index #drop irregulars
lates = lates.drop(indexNames)

#earlies.to_csv("./data/SAMI/earlies.csv")
#lates.to_csv("./data/SAMI/lates.csv")

earlies.to_csv("./data/SAMI/STELLAR_Details_earlies.csv")
lates.to_csv("./data/SAMI/STELLAR_Details_lates.csv")