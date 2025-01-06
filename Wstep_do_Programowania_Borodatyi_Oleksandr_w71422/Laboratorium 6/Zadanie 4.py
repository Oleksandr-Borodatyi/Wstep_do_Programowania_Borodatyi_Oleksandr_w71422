#Zadanie 4

import pandas as pd

# Tworzenie Data Frame z danymi o pracownikach

employees = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000]
})

# a) Wybierz pracowników, którzy mają pensję większą niż 5000 PLN

high_salary = employees[employees["Pensja"] > 5000]
print("Pracownicy z pensją większą niż 5000 PLN:")
print(high_salary)

# b) Posortuj pracowników według wieku (od najmłodszych do najstarszych)

sorted_by_age = employees.sort_values("Wiek")
print("\nPracownicy posortowani według wieku:")
print(sorted_by_age)

# c) Zgrupuj pracowników według stanowiska i oblicz średnią pensję w każdej grupie

avg_salary_by_position = employees.groupby("Stanowisko")["Pensja"].mean()
print("\nŚrednia pensja na każdym stanowisku:")
print(avg_salary_by_position)

# d) Utwórz ramkę danych zawierającą informacje o pracownikach, którzy zmienili stanowisko

promotions = pd.DataFrame({
    "ID": [2, 4],
    "Nowe_stanowisko": ["Senior Programista", "Lider Programistów"]
})

# Połącz oryginalny Data Frame z informacjami o zmianie stanowiska

merged = pd.merge(employees, promotions, on="ID", how="left")
print("\nDane o pracownikach po zmianie stanowisk:")
print(merged)

# e) Zapisz przygotowany Data Frame do pliku CSV

merged.to_csv("employees.csv", index=False)
print("\nPlik CSV został zapisany jako 'employees.csv'.")

# f) Wczytaj dane z pliku CSV i sprawdź, czy wczytanie przebiegło poprawnie

loaded_data = pd.read_csv("employees.csv")
print("\nWczytane dane z pliku CSV:")
print(loaded_data)
