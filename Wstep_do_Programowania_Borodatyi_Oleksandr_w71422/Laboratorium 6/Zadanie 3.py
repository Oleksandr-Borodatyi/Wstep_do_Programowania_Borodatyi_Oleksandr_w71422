# Zadanie 3

import pandas as pd

df = pd.read_csv('demografia.csv', na_values= ".")
print(df)
maxPk = df.max()[1:]
maxP = maxPk.max()
maxP1 = maxPk.idxmax()
print(maxP, maxP1)
