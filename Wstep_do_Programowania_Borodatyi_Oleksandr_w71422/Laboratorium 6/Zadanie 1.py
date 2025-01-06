#Zadanie 1

import pandas as pd

df = pd.read_csv('demografia.csv', na_values='.')
print(df)

df.set_index("KRAJE", inplace=True)
print(df.idxmax())