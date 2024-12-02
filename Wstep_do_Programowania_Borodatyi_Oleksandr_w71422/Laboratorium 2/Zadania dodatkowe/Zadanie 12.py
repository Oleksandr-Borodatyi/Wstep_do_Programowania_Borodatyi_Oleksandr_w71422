# Zadanie 12

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
            if punkty < 0:
                print("Liczba punktów nie może być ujemna. Spróbuj ponownie.")
                continue
            suma_punktow += punkty
            i += 1
        except ValueError:
            print("Wprowadź poprawną liczbę punktów.")

    # Obliczenie i wyświetlenie średniej
    srednia = suma_punktow / n
    print(f"Średnia liczba punktów w grupie wynosi: {round(srednia, 2)}")
