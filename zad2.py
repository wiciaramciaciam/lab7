import pandas as pd
df= pd.read_csv('demografia.csv')

max_przyrost_index= df['2022'].idxmax(skipna=True)
kraj_z_max_przyrostem= df.loc[max_przyrost_index,'KRAJE']
print(f"W 2022 roku największy przyrost ludzi miał kraj: {kraj_z_max_przyrostem}")