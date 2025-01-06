#Zadanie 2

import pandas as pd

df = pd.read_csv('demografia.csv')
print(df)

print(df['2022'].idxmax())
