#Importowanie biblioteki
import random

# Pytanie użytkownika o średnie spalanie
spalanie_na_100_km = float(input("Podaj średnie spalanie samochodu (l/100 km): "))

# Generowanie losowego dystansu
dystans = random.randint(5, 500)

# Obliczenia
zużycie_paliwa = (dystans * spalanie_na_100_km) / 100
koszt_podróży = zużycie_paliwa * 6.5

# Wyświetlanie wyników
print(f"Droga do pokonania: {dystans} km")
print(f"Przewidywane zużycie paliwa: {zużycie_paliwa} litrów")
print(f"Szacowany koszt podróży: {koszt_podróży} zł")

# Dlaczego wartości generowane przez bibliotekę random są pseudolosowe?
# Wartości generowane przez funkcję random.randint() są pseudolosowe, ponieważ są wynikiem obliczeń matematycznych
# bazujących na z góry ustalonym algorytmie, a nie prawdziwie losowych procesach. Oznacza to, że liczby te mogą być 
# powtarzalne, jeśli znamy punkt początkowy algorytmu