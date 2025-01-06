#Zadanie 5

import pandas as pd

# Dane studentów
data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}

# Tworzenie Data Frame
students_df = pd.DataFrame(data)

# a) Wybierz studentów, którzy mają ocenę większą niż 4
students_above_4 = students_df[students_df['Ocena'] > 4]
print("Studenci z oceną większą niż 4:")
print(students_above_4)

# b) Posortuj studentów według wieku
students_sorted_by_age = students_df.sort_values(by='Wiek')
print("\nStudenci posortowani według wieku:")
print(students_sorted_by_age)

# c) Zgrupuj studentów według ocen i oblicz średnią wieku w każdej grupie
grouped_by_grade = students_df.groupby('Ocena')['Wiek'].mean()
print("\nŚrednia wieku w grupach ocen:")
print(grouped_by_grade)

# d) Tworzenie ramki danych z poprawką i łączenie z pierwszym terminem
data_correction = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Ocena_poprawa': [5.0, 4.0, 5.0, 4.5, 3.0]
}
correction_df = pd.DataFrame(data_correction)
merged_df = pd.merge(students_df, correction_df, on='Nr_albumu')
print("\nPołączona ramka danych:")
print(merged_df)

# e) Zapisz DataFrame do pliku CSV
merged_df.to_csv('students_data.csv', index=False)
print("\nDane zapisano do pliku 'students_data.csv'.")

# f) Wczytaj dane z pliku CSV i sprawdź poprawność wczytania
loaded_df = pd.read_csv('students_data.csv')
print("\nWczytane dane z pliku CSV:")
print(loaded_df)

# g) Dodaj nowego studenta do istniejącego Data Frame
new_student = {
    'Nr_albumu': 6,
    'Imię': 'Piotr',
    'Nazwisko': 'Nowicki',
    'Ocena': 3.5,
    'Wiek': 22
}
students_df = pd.concat([students_df, pd.DataFrame([new_student])], ignore_index=True)
print("\nZaktualizowana ramka danych z nowym studentem:")
print(students_df)

# h) Znajdź unikalne wartości w kolumnie z ocenami
unique_grades = students_df['Ocena'].unique()
print("\nUnikalne oceny:")
print(unique_grades)

# i) Sprawdź, ile studentów ma ocenę równą 5
students_with_grade_5 = students_df[students_df['Ocena'] == 5.0]
count_grade_5 = len(students_with_grade_5)
print(f"\nLiczba studentów z oceną 5: {count_grade_5}")
