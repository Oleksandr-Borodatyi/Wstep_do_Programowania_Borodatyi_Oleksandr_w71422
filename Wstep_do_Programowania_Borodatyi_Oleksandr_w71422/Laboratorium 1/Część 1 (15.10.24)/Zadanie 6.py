# Pobiera od użytkownika długość drogi i średnie spalanie
dystans = float(input("Podaj przejechaną drogę w kilometrach: "))
spalanie_na_100_km = float(input("Podaj średnie spalanie (l/100 km): "))

# Oblicza zużycie paliwa (litry) na podstawie długości drogi i spalania.
zużycie_paliwa = (dystans * spalanie_na_100_km) / 100

# Oblicza koszt podróży w złotych, mnożąc zużycie paliwa przez cenę 6.5 zł/l
koszt_podróży = zużycie_paliwa * 6.5

# # Wyświetla przewidywane zużycie paliwa i koszt podróży.
print(f"Przewidywane zużycie paliwa: {zużycie_paliwa} litrów")
print(f"Szacowany koszt podróży: {koszt_podróży} zł")
