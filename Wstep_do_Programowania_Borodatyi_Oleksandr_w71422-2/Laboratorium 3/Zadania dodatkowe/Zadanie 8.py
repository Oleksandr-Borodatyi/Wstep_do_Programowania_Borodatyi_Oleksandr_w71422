# Zadanie 8

import random

# Pobranie danych od użytkownika
input_data = input("Podaj pięć cyfr rozdzielonych przecinkiem: ")

# Podział ciągu na podstawie przecinków
liczby = input_data.split(',')

# Sprawdzenie, czy użytkownik podał dokładnie 5 liczb
if len(liczby) != 5:
    print("Błąd: Podaj dokładnie pięć liczb rozdzielonych przecinkami.")
else:
    try:
        # Konwersja elementów na liczby całkowite
        liczby = [int(liczba) for liczba in liczby]

        # Zamiana listy na zbiór dla losowości
        liczby_set = set(liczby)

        # Losowanie jednego elementu
        wylosowany = random.choice(list(liczby_set))

        # Sprawdzenie, czy wylosowany element jest najmniejszy lub największy
        min_liczba = min(liczby_set)
        max_liczba = max(liczby_set)

        print(f"Wylosowany element: {wylosowany}")
        if wylosowany == min_liczba:
            print("Wylosowany element jest najmniejszą liczbą.")
        elif wylosowany == max_liczba:
            print("Wylosowany element jest największą liczbą.")
        else:
            print("Wylosowany element nie jest ani najmniejszy, ani największy.")
    except ValueError:
        print("Błąd: Wszystkie podane wartości muszą być cyframi.")
