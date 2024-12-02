#Zadanie 4

# Wczytanie liczby naturalnej n
n = int(input("Podaj liczbę naturalną n: "))

# Inicjalizacja zmiennej do obliczenia silni
silnia = 1

# Obliczenie silni
for i in range(1, n + 1):
    silnia *= i  # Mnożenie kolejnych liczb

# Wyświetlenie wyniku
print("Silnia liczby", n, "wynosi:", silnia)
