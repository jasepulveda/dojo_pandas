import pandas as pd

filename = "./data/bostonHousing1978.xlsx"
df = pd.read_excel(filename)
print(df)
#print(df.head())
