import pandas as pd
df= pd.read_csv('demografia.csv')
print(df)

df = pd.read_csv('demografia.csv', decimal=',', na_values=['NA','n/a','NaN'])
df_without_kraj= df.drop(columns=['KRAJE'])
max_przyrost= df_without_kraj.max().max()
print(max_przyrost)

rok_max_przyrost= df_without_kraj.max().idxmax()
indeks_max_przyrost= df_without_kraj[rok_max_przyrost].idxmax()
kraj_max_przyrost= df.loc[indeks_max_przyrost,'KRAJE']
print(f'Największy przyrost ludnosci był w roku {rok_max_przyrost} i wyniosl {max_przyrost} oraz był w kraju {kraj_max_przyrost}')