import pandas as pd
dane_studenci = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena_Kolokwium': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25] # Zmieniono 'WiekS' na 'Wiek' dla ujednolicenia
}

df_studenci = pd.DataFrame(dane_studenci)
print(df_studenci)

#a)
studenci_powyzej_4 = df_studenci[df_studenci['Ocena_Kolokwium'] > 4]
print("\nStudenci z oceną większą niż 4:")
print(studenci_powyzej_4)

#b)
studenci_posortowani_wiekiem = df_studenci.sort_values(by='Wiek')
print("\nStudenci posortowani według wieku:")
print(studenci_posortowani_wiekiem)

#c)
srednia_wieku_wg_ocen = df_studenci.groupby('Ocena_Kolokwium')['Wiek'].mean().reset_index()
print("\nŚrednia wieku studentów w każdej grupie ocen:")
print(srednia_wieku_wg_ocen)

#d)
dane_poprawa = {
    'Nr_albumu': [2, 4, 5, 6],
    'Ocena_Poprawa': [4.0, 4.5, 3.0, 4.0]
}
df_poprawa = pd.DataFrame(dane_poprawa)
df_polaczony = pd.merge(
    df_studenci,
    df_poprawa,
    on='Nr_albumu',
    how='left'
)
print("\nPołączony DataFrame (Kolokwium + Poprawa):")
print(df_polaczony)

#e)
nazwa_pliku = 'protokol_ocen.csv'
df_polaczony.to_csv(nazwa_pliku, index=False)
print(f"\nZapisano połączony DataFrame do pliku: '{nazwa_pliku}'")

#f)
df_wczytany = pd.read_csv(nazwa_pliku)
print(f"\nWczytano dane z pliku '{nazwa_pliku}'. Pierwsze wiersze:")
print(df_wczytany.head())

#g)
nowy_student = {
    'Nr_albumu': 6,
    'Imię': 'Ewa',
    'Nazwisko': 'Nowicka',
    'Ocena_Kolokwium': 3.5,
    'Wiek': 22
}
df_nowy_student = pd.DataFrame([nowy_student])
# Dołączamy do pierwotnej ramki df_studenci
df_studenci_aktualizacja = pd.concat([df_studenci, df_nowy_student], ignore_index=True)

print("\nDataFrame po dodaniu nowego studenta (Ewa Nowicka):")
print(df_studenci_aktualizacja.tail(2))

#h)
unikalne_oceny = df_studenci['Ocena_Kolokwium'].unique()
print("\nUnikalne wartości w kolumnie 'Ocena_Kolokwium':")
print(unikalne_oceny)

#i)
liczba_studentow_z_5 = (df_studenci['Ocena_Kolokwium'] == 5.0).sum()
print(f"\nLiczba studentów z oceną równą 5: {liczba_studentow_z_5}")