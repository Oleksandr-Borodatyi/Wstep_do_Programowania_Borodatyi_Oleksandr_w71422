# Zadanie 13 

# Pobranie liczby studentów od użytkownika
n = int(input("Podaj liczbę studentów w grupie: "))

# Sprawdzenie, czy liczba studentów jest większa od 0
if n <= 0:
    print("Liczba studentów musi być większa od 0.")
else:
    suma_punktow = 0
    i = 0  # Indeks studenta

    # Pętla while do wprowadzania punktów
    while i < n:
        try:
            punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
            if punkty < 0 or punkty > 100:
                print("Liczba punktów musi być w przedziale 0-100. Spróbuj ponownie.")
                continue  # Pomija resztę iteracji
            suma_punktow += punkty
            i += 1
        except ValueError:
            print("Wprowadź poprawną liczbę punktów.")

    # Obliczenie i wyświetlenie średniej
    srednia = suma_punktow / n
    print(f"Średnia liczba punktów w grupie wynosi: {round(srednia, 2)}")


# Pobranie liczby studentów od użytkownika
n = int(input("Podaj liczbę studentów w grupie: "))

# Sprawdzenie, czy liczba studentów jest większa od 0
if n <= 0:
    print("Liczba studentów musi być większa od 0.")
else:
    suma_punktow = 0
    licznik = 0  # Liczba wprowadzonych studentów

    # Nieskończona pętla
    while True:
        try:
            punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik + 1}: "))
            if punkty < 0 or punkty > 100:
                print("Liczba punktów musi być w przedziale 0-100. Spróbuj ponownie.")
                continue  # Pomija resztę iteracji
            suma_punktow += punkty
            licznik += 1
            if licznik == n:  # Gdy wszystkie punkty zostały wprowadzone
                break
        except ValueError:
            print("Wprowadź poprawną liczbę punktów.")

    # Obliczenie i wyświetlenie średniej
    srednia = suma_punktow / n
    print(f"Średnia liczba punktów w grupie wynosi: {round(srednia, 2)}")
