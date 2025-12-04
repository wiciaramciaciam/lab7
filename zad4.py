import pandas as pd
data= {
    'nr_id': [1, 2, 3, 4, 5],
    'imię': ['Anna','Jan','Katarzyna','Tomasz','Michał'],
    'nazwisko': ['Kowalska','Nowak','Wiśniewska','Kaczmarek','Zieliński'],
    'stanowisko': ['Manager','Programista','Konsultant','Programista','Manager'],
    'wiek': [35, 28, 40, 30, 45],
    'pensja': [8000, 4500, 6000, 5500, 7000]
}

df= pd.DataFrame(data)
print(df)

#a)
pensja_ponad_5000= df[df['pensja']>5000]
print("\nPracownicy którzy mają pensje wieksza niz 5000:")
print(pensja_ponad_5000)

#b)
df_sorted_by_age= df.sort_values(by='wiek')
print("\nPracownicy posortowani według wieku:")
print(df_sorted_by_age)

#c)
grouped_by_position= df.groupby('stanowisko')['pensja'].mean()
print("\nŚrednia pensja według stanowiska:")
print(grouped_by_position)

#d)
awans={
    'nr_id': [2,4],
    'nowe_stanowisko':['Senior programista','Senior programista']
}
df_awans= pd.DataFrame(awans)
df_combined= pd.merge(df, df_awans, on='nr_id', how='left')
print("\nPołączana ramka danych z awansami:")
print(df_combined)

#e)
df_combined.to_csv('pracownicy.csv', index=False)
print("\nZapisano dane do pliku 'pracownicy.csv'.")

#f)
df_from_csy= pd.read_csv('pracownicy.csv')
print("\nWczytane dane z pliku CSV:")
print(df_from_csy)