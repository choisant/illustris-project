import pandas as pd

data1 = {"id": [1,2,3,4,5,6], "mass": [8,4,3,2,7,4]}
data2 = {"id": [2,5,6], "velocity": [3,2,1]}

df1 = pd.DataFrame(data = data1)
df2 = pd.DataFrame(data = data2)

df3 = pd.merge(df1, df2,  how='outer', on='id')
print(df3)