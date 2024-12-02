# Wprowadzenie liczby bramek i punktów bonusowych
gol = int(input("Podaj liczbę bramek zdobytych przez drużynę: "))
bonus = int(input("Podaj punkty bonusowe dla drużyny: "))

# Obliczenie podstawowego wyniku z bramek
wynik = gol * 10

# Sprawdzenie warunków dla punktów bonusowych
if gol > 10:
    wynik += 10  # Dodatkowe punkty za więcej niż 10 bramek
elif gol > 5:
    wynik += 5   # Dodatkowe punkty za więcej niż 5 bramek

# Dodanie punktów bonusowych
wynik += bonus

# Wyświetlenie łącznego wyniku drużyny
print("Łączny wynik drużyny wynosi:", wynik)
